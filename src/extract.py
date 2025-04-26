"""
Extract the code from the PDF file and returns a subset of pages that contain the given text.
This script uses PyMuPDF library to handle PDF files efficiently.
The extracted pages are then saved to a new PDF file.
"""

import camelot, pymupdf, os

def extract_pages_with_text(source_pdf_path: str, output_pdf_path: str, search_text: str):
    """
    Creates a new PDF containing only the pages from the source PDF
    where the specified text is found.

    Args:
        source_pdf_path: Path to the original PDF file.
        output_pdf_path: Path where the new PDF with matching pages will be saved.
        search_text: The exact text string to search for (case-sensitive).

    Returns:
        True if the new PDF was created successfully, False otherwise.
    """
    if not os.path.exists(source_pdf_path):
        print(f"Error: Source file not found at {source_pdf_path}")
        return False

    matching_page_indices = []
    new_doc = None # Initialize new document variable

    try:
        # Open the source document
        with pymupdf.open(source_pdf_path) as source_doc:
            print(f"Opened '{source_pdf_path}', processing {source_doc.page_count} pages...")

            # Iterate through each page to find matches
            for page_num, page in enumerate(source_doc):
                # Optional: Print progress
                # print(f"  Scanning page {page_num + 1}...")

                # Search for the text on the current page
                instances = page.search_for(search_text, quads=False)

                if instances:
                    print(f"  Found '{search_text}' on page {page_num + 1}")
                    matching_page_indices.append(page_num) # Store the 0-based index

            # Check if any matching pages were found
            if not matching_page_indices:
                print(f"No pages containing '{search_text}' were found in the source PDF.")
                return False

            print(f"\nFound text on {len(matching_page_indices)} page(s). Creating new PDF...")

            # Create a new, empty PDF document to store the matching pages
            new_doc = pymupdf.open()

            # Insert the matching pages from the source doc into the new doc
            for page_index in matching_page_indices:
                # print(f"  Adding page {page_index + 1} to the new PDF...")
                # insert_pdf copies pages based on 0-based indices
                new_doc.insert_pdf(source_doc, from_page=page_index, to_page=page_index)

            # Save the new PDF
            # garbage=4 cleans up unused objects, deflate=True compresses the output
            new_doc.save(output_pdf_path, garbage=4, deflate=True)
            print(f"\nSuccessfully created new PDF with matching pages at: {output_pdf_path}")
            return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        # Ensure the new document is closed if it was created
        if new_doc:
            new_doc.close()
            # print("New document closed.")


# --- Example Usage ---

source_file = os.path.join(os.getcwd(), 'data','WCEPRE_2024.pdf')  # <<< REPLACE with the path to your original PDF
output_file = os.path.join(os.getcwd(), 'data','Annexure_A_Pages.pdf') # <<< Name for the new PDF file
search_term = "Annexure A"

# Optional: Add a timestamp to the output filename to avoid overwriting
# base, ext = os.path.splitext(output_file)
# timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# output_file = f"{base}_{timestamp}{ext}"

# Run the extraction process
success = extract_pages_with_text(source_file, output_file, search_term)

if success:
    print("Extraction process completed.")
else:
    print("Extraction process failed or found no matching pages.")
