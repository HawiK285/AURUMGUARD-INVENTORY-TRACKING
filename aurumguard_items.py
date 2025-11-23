import json
import os
import uuid
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
ITEMS_TABLE = os.environ.get('ITEMS_TABLE', 'aurumguard-items')

BASE_HEADERS = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
}

def convert_decimals(obj):
    if isinstance(obj, list):
        return [convert_decimals(o) for o in obj]
    if isinstance(obj, dict):
        return {k: convert_decimals(v) for k, v in obj.items()}
    if isinstance(obj, Decimal):
        return float(obj)
    return obj

def lambda_handler(event, context):
    method = event.get("httpMethod", "")
    path = event.get("path", "")
    headers = event.get("headers") or {}

    tenant_id = headers.get("x-tenant-id", "demo-tenant")

    if path.endswith("/items") and method == "GET":
        return list_items(tenant_id)
    elif path.endswith("/items") and method == "POST":
        body = json.loads(event.get("body") or "{}")
        return create_item(tenant_id, body)
    else:
        return {
            "statusCode": 404,
            "headers": BASE_HEADERS,
            "body": json.dumps({"message": "Not Found"})
        }

def list_items(tenant_id):
    table = dynamodb.Table(ITEMS_TABLE)
    resp = table.query(
        KeyConditionExpression=Key("tenantId").eq(tenant_id)
    )
    items = convert_decimals(resp.get("Items", []))

    return {
        "statusCode": 200,
        "headers": BASE_HEADERS,
        "body": json.dumps(items)
    }

def create_item(tenant_id, body):
    table = dynamodb.Table(ITEMS_TABLE)
    item_id = str(uuid.uuid4())

    item = {
        "tenantId": tenant_id,
        "itemId": item_id,
        "name": body.get("name", "Unnamed item"),
        "category": body.get("category", "OTHER"),
        "metal": body.get("metal", None),
        "stone": body.get("stone", None),
        "size": body.get("size", None),
        "costPrice": body.get("costPrice", 0),
        "retailPrice": body.get("retailPrice", 0),
        "isUnique": body.get("isUnique", False),
        "imageUrl": body.get("imageUrl", None)
    }

    table.put_item(Item=item)
    item_out = convert_decimals(item)

    return {
        "statusCode": 201,
        "headers": BASE_HEADERS,
        "body": json.dumps(item_out)
    }
