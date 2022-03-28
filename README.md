# Gotcha bot

## Usage
```bash
py gotcha.py --send names.json
```
```bash
py gotcha.py --send '{"Bob": "bob@example.com", "Alice": "alice@example.com"}'
```

**names.json**
```json
{
  "Bob": "bob@example.com",
  "Alice": "alice@example.com",
  "Carl": "carl@example.com",
  "Dave": "dave@example.com"
}
```

**.env**
```bash
GOTCHA_EMAIL=gotcha@example.com
GOTCHA_PASSWORD=password
GOTCHA_NAME=Gotcha bot
GOTCHA_SUBJECT=Gotcha
```
