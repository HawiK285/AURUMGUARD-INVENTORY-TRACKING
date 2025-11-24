# AurumGuard – Serverless Jewelry & High-Value Asset Tracking

AurumGuard is a serverless inventory tracking solution for **high-value assets** (jewelry, luxury items, collectibles, etc.), designed for both companies and individual owners. It reduces losses, improves visibility, and makes it easier to prove ownership when working with insurers or auditors.

See `AurumGuard_Inventory_Tracking_Project_Overview.pdf` for a deeper project overview.

---

## Architecture

AurumGuard is built as a fully serverless application on **AWS**. Each service has a specific role:

- **Amazon S3 – Frontend & Static Website Hosting**  
  Hosts the entire web dashboard (HTML, CSS, JavaScript) using S3 static website hosting.  
  Users open the S3 website URL in their browser to access the AurumGuard UI.

- **Amazon API Gateway (REST)**  
  Acts as the **front door** for the backend.  
  Exposes a REST endpoint like `/items` that the frontend calls with `fetch()` to load inventory data.

- **AWS Lambda (Python)**  
  Implements the **business logic** in a function such as `AurumGuardItemsFn`.  
  API Gateway invokes this Lambda, which reads asset records from DynamoDB and returns JSON to the client.

- **Amazon DynamoDB**  
  Stores the inventory data for high-value assets (for example, rings, earrings, sapphire necklaces).  
  Each item can include fields such as:
  `tenantId`, `itemId`, `name`, `category`, `metal`, `stone`, `size`,  
  `costPrice`, `retailPrice`, `isUnique`, and `imageUrl`.  
  The `tenantId` design also allows for multi-tenant use (multiple customers or stores).

- **AWS CloudShell + AWS CLI**  
  Used to **build, deploy, and test** the entire stack from the command line:  
  uploading `index.html` to S3, configuring API Gateway, deploying the Lambda function, and seeding DynamoDB.

- **AWS IAM**  
  Provides the **security layer** with roles and policies so that:  
  - API Gateway is allowed to invoke the Lambda function  
  - Lambda is allowed to read from DynamoDB  
  - S3 can safely host the public website without exposing sensitive resources  

### Request Flow

1. The user opens the S3 website URL in their browser.  
2. The browser downloads `index.html`, CSS, and JavaScript from **Amazon S3**.  
3. JavaScript on the page calls the **API Gateway** REST endpoint (e.g., `/items`).  
4. **API Gateway** invokes the **AWS Lambda** function.  
5. **Lambda** queries **DynamoDB** for the tenant’s inventory items.  
6. The JSON response is returned to the browser and rendered as product cards with images and pricing.

---

## Features

- Modern, dark-themed dashboard hosted on **Amazon S3**.  
- Dynamic product cards loaded from a **live AWS REST API**.  
- Supports unique pieces, internal cost vs. retail price, and asset metadata (category, metal, stone, size, etc.).  
- Designed for **multi-tenant inventory tracking** with `tenantId` to separate different customers or businesses.  

---

## Business Value

- **For companies** – Reduce losses and shrinkage, gain real-time visibility into expensive stock, and simplify audits with a clear record of every high-value item.  
- **For individuals** – Track expensive jewelry and other valuable assets in one place, provide proof of ownership for insurance and claims, and keep photos + details together in a secure, cloud-based system.




