import requests
from typing import List, Dict

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"


def fetch_pubmed_papers(query: str, max_results: int = 10) -> List[Dict]:
    """
    Fetches papers from PubMed based on a query.
    
    :param query: PubMed query string.
    :param max_results: Number of papers to fetch.
    :return: List of dictionaries with paper details.
    """
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()
    data = response.json()
    
    paper_ids = data["esearchresult"]["idlist"]
    
    if not paper_ids:
        print("No papers found.")
        return []
    
    # Fetch detailed summaries
    details_params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    details_response = requests.get(PUBMED_SUMMARY_URL, params=details_params)
    details_response.raise_for_status()
    details = details_response.json()

    papers = []
    for paper_id in paper_ids:
        paper_info = details["result"].get(paper_id, {})
        papers.append({
            "PubmedID": paper_id,
            "Title": paper_info.get("title", "Unknown"),
            "PublicationDate": paper_info.get("pubdate", "Unknown")
        })
    
    return papers
