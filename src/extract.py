"""
Extract the code from the PDF file and incrementally process it.
Loads the final result into a set of CSV files.

Inputs: PDF file
Outputs: 
    - csv files
    - grouped into n votes (in this case 14)
    - each csv file representing a table in the vote.
"""

import camelot, pymupdf, os

def count_pages_with_text_pymupdf(pdf_path: str, search_text: str) -> int:
    """
    Counts the number of pages in a PDF file that contain the specified text.

    Args:
        pdf_path: The file path to the PDF document.
        search_text: The exact text string to search for (case-sensitive).

    Returns:
        The total number of pages where the search_text was found.
        Returns -1 if the file cannot be processed or doesn't exist.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}")
        return -1

    match_count = 0
    try:
        # Use a 'with' statement to ensure the document is closed properly
        with pymupdf.open(pdf_path) as doc:
            # Iterate through each page in the document
            for page_num, page in enumerate(doc):
                # search_for returns a list of Rect objects where text is found
                # An empty list means the text was not found on this page
                instances = page.search_for(search_text, quads=False) # quads=False simplifies output

                # If the list is not empty, the text was found on this page
                if instances:
                    match_count += 1
            

    except Exception as e:
        print(f"An error occurred while processing '{pdf_path}': {e}")
        return -1 # Indicate an error occurred

    return match_count

# --- Example Usage ---
pdf_file = os.path.join(os.getcwd(), 'data', 'WCEPRE_2024.pdf')  # <<< REPLACE with the actual path to your PDF file
search_term = "Annexure A"

# Check if the file exists before calling the function
if os.path.exists(pdf_file):
    total_pages_found = count_pages_with_text_pymupdf(pdf_file, search_term)

    if total_pages_found >= 0:
        print(f"The text '{search_term}' was found on a total of {total_pages_found} pages in '{pdf_file}'.")
else:
    print(f"Error: The file '{pdf_file}' does not exist.")
