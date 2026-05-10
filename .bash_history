mktir api_prototyper
cd api_prototyper
mkdir api_prototyper
cd api_prototyper
cat api_requirements.md
cat <<EOF > api_requirements.md
# API Requirements - Inventory API

## Domain
E-commerce inventory management

## Target Users
- Developers: manage product stock
- Analysts: generate stock reports

## Core Operations
1. Create product
2. Update stock level
3. Get product by ID
4. Search products
5. Delete product
6. List categories
7. Update price
8. Bulk import products
9. Export inventory report
10. Set stock alerts
11. Update category
12. Get product history

## Data Rules
- SKU must be unique
- Price must be > 0

## Non-Functional
- Response time < 200ms
- JWT authentication required
EOF

cat api_requirements.md
git add api_requirements.md
git commit -m "Add API requirements document"
git push origin main
cd ..
git init
git remote add origin https://github.com/aytacxuduyeva/holbertonschool-ai4devs.git
