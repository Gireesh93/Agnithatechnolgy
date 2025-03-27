import csv
from typing import List, Dict

def save_to_csv(filename: str, papers: List[Dict]):
    """
    Saves the fetched papers to a CSV file.
    
    :param filename: Name of the CSV file.
    :param papers: List of paper dictionaries.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["PubmedID", "Title", "PublicationDate", "NonAcademicAuthors", "CompanyAffiliations", "CorrespondingAuthorEmail"])
        writer.writeheader()
        for paper in papers:
            writer.writerow(paper)
    
    print(f"Saved results to {filename}")
