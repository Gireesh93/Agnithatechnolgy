import argparse
import json
from pubmed_fetcher.fetch import fetch_pubmed_papers
from pubmed_fetcher.filter import extract_company_authors
from pubmed_fetcher.utils import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed with non-academic author filtering.")
    parser.add_argument("query", type=str, help="PubMed search query")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file")

    args = parser.parse_args()
    
    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    papers = fetch_pubmed_papers(args.query)

    for paper in papers:
        authors = [
            {"name": "Dr. John Doe", "affiliation": "Pfizer Inc.", "email": "john@pfizer.com"}, 
            {"name": "Dr. Jane Smith", "affiliation": "Harvard University", "email": "jane@harvard.edu"}
        ]  
        company_authors = extract_company_authors(authors)
        paper["NonAcademicAuthors"] = ", ".join([a["Name"] for a in company_authors])
        paper["CompanyAffiliations"] = ", ".join([a["Company"] for a in company_authors])
        paper["CorrespondingAuthorEmail"] = ", ".join([a["Email"] for a in company_authors])
    
    if args.file:
        save_to_csv(args.file, papers)
    else:
        print(json.dumps(papers, indent=4))

if __name__ == "__main__":
    main()
