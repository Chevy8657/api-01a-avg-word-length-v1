# Average Word Length

Single-purpose API. Stateless. Deterministic. Returns JSON only.

## Endpoints
- GET `/health`
- GET `/v1/avg-word-length?text=`

## Example

Request:
`/v1/avg-word-length?text=Hello%20world`

Response:
```json
{
  "input": "Hello world",
  "average_word_length": 5.0
}
