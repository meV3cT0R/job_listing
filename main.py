import json
import scraper

if __name__ == "__main__":
    with open("data.json", "w",encoding="utf-8") as f:
        f.write(json.dumps(scraper.scrape(input("Enter keywords:"))))
        print("Data has been stored in data.json")
        