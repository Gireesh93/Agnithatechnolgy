import re
from typing import List, Dict

# Keywords that indicate company affiliations
COMPANY_KEYWORDS = ["pharma", "biotech", "inc", "ltd", "corporation", "gmbh", "s.a.", "llc"]
EMAIL_COMPANY_DOMAINS = ["@pfizer.com", "@novartis.com", "@merck.com"]


def is_company_affiliation(affiliation: str) -> bool:
    """
    Checks if an affiliation belongs to a pharmaceutical or biotech company.
    
    :param affiliation: The author's affiliation.
    :return: True if the affiliation is a company, else False.
    """
    affiliation_lower = affiliation.lower()
    return any(keyword in affiliation_lower for keyword in COMPANY_KEYWORDS)


def extract_company_authors(authors: List[Dict]) -> List[Dict]:
    """
    Filters out authors affiliated with companies.

    :param authors: List of author dictionaries.
    :return: List of dictionaries with non-academic author details.
    """
    company_authors = []
    for author in authors:
        if is_company_affiliation(author.get("affiliation", "")) or any(
            domain in author.get("email", "").lower() for domain in EMAIL_COMPANY_DOMAINS
        ):
            company_authors.append({
                "Name": author.get("name", "Unknown"),
                "Company": author.get("affiliation", "Unknown"),
                "Email": author.get("email", "N/A")
            })
    
    return company_authors
