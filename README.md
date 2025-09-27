# garden-app

Simple gardening advice utility providing tips by month or season.

## Usage

Run directly as a CLI:

```
python garden_advice.py --month March
python garden_advice.py --season spring
```

Or import in Python:

```python
from garden_advice import get_garden_advice

print(get_garden_advice(month="April"))
print(get_garden_advice(season="winter"))
```

## Tests

```
python -m unittest -v
```

## Repository link

See `repo.txt` for the GitHub URL.