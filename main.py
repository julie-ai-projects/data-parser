from parser import scrape_data
from analyzer import analyze_data

def main():
    data = scrape_data("https://example.com")
    analyze_data(data)

if __name__ == "__main__":
    main()
