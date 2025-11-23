# AurumGuard – Serverless Jewelry Inventory Tracking

AurumGuard is a serverless inventory tracking solution for high-value jewelry assets,
designed for both companies and individual owners. It reduces losses, improves visibility,
and makes it easier to prove ownership when working with insurers.

## Architecture

- **Amazon S3** – Static website hosting for the jewelry dashboard.  
- **Amazon API Gateway (REST)** – Front door for the `/items` inventory API.  
- **AWS Lambda (Python)** – Serverless function to read inventory from DynamoDB.  
- **Amazon DynamoDB** – NoSQL table storing jewelry items (tenantId, name, category, metal,
  stone, size, costPrice, retailPrice, isUnique, imageUrl).  
- **AWS CloudShell + AWS CLI** – Used to deploy and manage the stack.  
- **AWS IAM** – Roles and policies securing Lambda, API Gateway, and S3 access.

## Features

- Modern dark-themed jewelry dashboard hosted on S3.  
- Dynamic product cards loaded from a live AWS REST API.  
- Supports unique pieces, costs, and retail pricing.  
- Designed for multi-tenant inventory tracking.

## Business Value

- **For companies** – Reduce losses, gain real-time visibility, and simplify audits.  
- **For individuals** – Track expensive jewelry and provide proof of ownership
  for insurance and claims.

See `AurumGuard_Inventory_Tracking_Project_Overview.pdf` for a deeper project overview.
## Architecture

AurumGuard is built as a fully serverless application on AWS:

- **Amazon S3** – Hosts the static jewelry dashboard (HTML/CSS/JS) using S3 static website hosting.
- **Amazon API Gateway (REST)** – Exposes the `/items` endpoint that the frontend calls with `fetch`.
- **AWS Lambda (Python)** – Contains the business logic (`AurumGuardItemsFn`) that reads jewelry items.
- **Amazon DynamoDB** – Stores jewelry inventory records such as rings, earrings, and sapphire necklaces
  with fields like `tenantId`, `itemId`, `name`, `category`, `metal`, `stone`, `size`, `costPrice`,
  `retailPrice`, `isUnique`, and `imageUrl`.
- **AWS CloudShell + AWS CLI** – Used to deploy and test S3, API Gateway, Lambda, and DynamoDB from the command line.
- **AWS IAM** – Provides roles and policies so API Gateway can invoke Lambda, Lambda can read DynamoDB, and
  S3 can safely host the public website.

**Request flow:**

1. The user opens the S3 website URL in their browser.
2. The browser downloads `index.html`, CSS, and JavaScript from **Amazon S3**.
3. JavaScript calls the **API Gateway** REST endpoint (`/items`).
4. **API Gateway** invokes the **AWS Lambda** function.
5. **Lambda** queries **DynamoDB** for the tenant’s jewelry items.
6. The JSON response is returned to the browser and rendered as product cards with jewelry images.

### Diagram

