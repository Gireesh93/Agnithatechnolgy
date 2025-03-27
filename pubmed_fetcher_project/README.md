# 📄 PubMed Paper Fetcher  

## 🔍 Overview  
This Python program fetches research papers from **PubMed** based on a user-specified query. It identifies papers where at least one author is affiliated with a pharmaceutical or biotech company and saves the results as a CSV file.  

---

## 🚀 Features  
- **Fetches research papers** using the **PubMed API**.  
- **Filters results** to identify papers with non-academic authors.  
- **Saves results as a CSV file** with the following columns:  
  - `PubmedID` – Unique identifier for the paper.  
  - `Title` – Title of the paper.  
  - `Publication Date` – Date the paper was published.  
  - `Non-academic Author(s)` – Authors affiliated with non-academic institutions.  
  - `Company Affiliation(s)` – Names of pharmaceutical/biotech companies.  
  - `Corresponding Author Email` – Email of the corresponding author.  
- **Command-line interface** with the following options:  
  - `-h` or `--help` → Display usage instructions.  
  - `-d` or `--debug` → Print debug information.  
  - `-f filename.csv` → Save results to a specified CSV file.  

---

## 🛠 Installation  

### 1️⃣ Prerequisites  
Ensure you have **Python 3.8+** installed on your system.  

### 2️⃣ Install Poetry  
If you haven’t installed `poetry`, do so using:  
```bash
pip install poetry
