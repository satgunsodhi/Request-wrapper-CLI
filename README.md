# Requester CLI

A simple command-line interface for making HTTP requests. Requester CLI allows you to easily perform GET, POST, PUT, and DELETE requests and save responses to files.

## Usage

Requester CLI supports the following commands:

### GET Request

```bash
requester /get <url>
```

### POST Request

```bash
requester /post <url> <path_to_json_file>
```

### PUT Request

```bash
requester /put <url> <path_to_json_file>
```

### DELETE Request

```bash
requester /delete <url>
```

## Examples

### GET Example

```bash
requester /get https://api.example.com/products
```

### POST Example

Create a file named `data.json` with your JSON data:
```json
{
  "name": "New Product",
  "price": "49.99"
}
```

Then run:
```bash
requester /post https://api.example.com/products data.json
```

### PUT Example

```bash
requester /put https://api.example.com/products/123 data.json
```

### DELETE Example

```bash
requester /delete https://api.example.com/products/123
```

## Response

Responses are automatically saved to:
- `response.json` for JSON responses
- `response.txt` for non-JSON responses

## Features

- Easy-to-use command-line interface
- Support for common HTTP methods (GET, POST, PUT, DELETE)
- Automatic response saving
- URL validation
- JSON format validation

## Development

To contribute to this project:

1. Clone the repository
2. Install development dependencies: `pip install .`
3. Make your changes
4. Submit a pull request

## Author

Satgun Sodhi
