import scraper
import json

if __name__ == "__main__":
    with open("data.json", "w") as f:
        f.write(json.dumps(scraper.scrape(input("Enter keywords:"))))
        print("Data has been stored in data.json")
        