# Benchmark Tasks for Backend Development

This document defines three distinct technical tasks designed to be completed within a 15–30 minute window. These tasks focus on core backend logic, data transformation, and validation.

---

## Task 1 - CRUD Endpoint: User Registration
**Requirements**: 
Implement a POST `/users` endpoint that handles user registration. The system must validate the input format and ensure data integrity before "storing" the record.

**Inputs**: 
- JSON Body: `{ "name": string, "email": string }`

**Outputs**: 
- Success: JSON object of the created user including a generated unique ID.
- Failure: Error message detailing the validation breach.

**Acceptance Criteria**: 
- Returns a `201 Created` status code on successful validation and storage.
- Returns a `400 Bad Request` if the email format is invalid (e.g., missing '@' or domain).
- Returns a `400 Bad Request` if the name field is empty or missing.

---

## Task 2 - Data Transformation: Currency Converter Service
**Requirements**: 
Create a utility function or endpoint that converts a transaction amount from a base currency (USD) to a target currency using a provided exchange rate map.

**Inputs**: 
- Amount (Decimal)
- Target Currency (String, e.g., "EUR", "GBP")
- Rates Map (Object/Dict, e.g., `{"EUR": 0.92, "GBP": 0.78}`)

**Outputs**: 
- A JSON object containing the `original_amount`, `converted_amount`, and `currency_symbol`.

**Acceptance Criteria**: 
- The output amount must be rounded to exactly two decimal places.
- Must throw a "Currency Not Supported" error if the target currency is missing from the rates map.
- Handles zero or negative input amounts by returning a validation error.

---

## Task 3 - Middleware: API Key Authentication
**Requirements**: 
Develop a middleware component that intercepts incoming requests to protect sensitive routes. It must check for a specific header and validate the token against a hardcoded or environment-stored key.

**Inputs**: 
- Request Headers (specifically `X-API-KEY`)

**Outputs**: 
- Success: Forwards the request to the next handler.
- Failure: Terminates the request with an error response.

**Acceptance Criteria**: 
- Returns `401 Unauthorized` if the `X-API-KEY` header is missing.
- Returns `403 Forbidden` if the provided key does not match the authorized system key.
- Successfully allows the request to proceed if the key matches exactly.

