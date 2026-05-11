# Cross-Language Specification - E-commerce Recommendation Engine

## Algorithm
Collaborative Filtering for Product Recommendations:
- Analyze user purchase history to find similarities between users.
- Identify products bought by similar users that the target user has not purchased.
- Rank products based on frequency and similarity score.
- Return the top N recommendations.

## Inputs
- **User Database:** A list/JSON of users and their purchased product IDs.
- **Current User ID:** The ID of the user for whom recommendations are being generated.
- **Product Metadata:** A list of all available products.

## Outputs
- **JSON Object:** Containing a list of recommended product IDs and their calculated relevance scores.

## Edge Cases
- **New User (Cold Start):** User has no purchase history.
- **Out of Stock:** Recommended products are no longer available in metadata.
- **Single Purchase:** User has only bought one item, limiting similarity data.
- **Empty Catalog:** No products available in the database.

## Test Cases
- `user_history_dense.json` -> Returns top 5 relevant products with scores > 0.8.
- `user_new_001.json` -> Returns top trending products (fallback) as user has no history.
- `user_niche_buyer.json` -> Returns specialized items specific to user's unique category.
- `empty_catalog.json` -> Returns an empty list with a status message "No products available".
- `malformed_user_id.json` -> Returns an error message: "Invalid User ID format".
