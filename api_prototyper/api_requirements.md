# API Requirements - Inventory API

## Domain
E-commerce inventory management system.

## Target Users
* Developers: manage product stock
* Analysts: generate stock reports

## Core Operations
1. Create product
2. Update stock level
3. Get product by ID
4. Search products
5. Delete product
6. List categories
7. Update price
8. Export inventory report

## Data Validation Rules
* SKU must be unique
* Price must be > 0
* Quantity cannot be negative

## Non-Functional Requirements
* Response time < 200ms
* JWT authentication required
* Rate limit: 100 requests/min


