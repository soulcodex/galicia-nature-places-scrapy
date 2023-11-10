# Extract Nature Places - Scrapy Implementation :space_invader: :palm_tree:

This is a PoC using the Python **scrapy** library to retrieve data from pages of the government of Galicia, Spain related with
beautiful natural places that exist here in Galicia and that are sure to be a must visit whenever you come to Galicia.

### Requirements :scroll:

- Python >= 3.8
- venv

### Getting started :arrow_forward: :fire:

```bash
python3 -m venv .venv
. venv/bin/activate
pip install -r requirements.txt
```

### Running the scrapper :runner:

```bash
scrapy crawl galicia_places_spider -o galicia-places.json
```