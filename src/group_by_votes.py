"""
Logic to group the tables by votes
"""

import pymupdf, fitz
import os
import collections
from typing import List, Dict

def split_pdf_by_vote(input_pdf_path: str, output_dir: str = ".", max_vote_num: int = 14):
    """
    Splits a PDF based on page content matching "Annexure A to Vote {n}".

    Args:
        input_pdf_path: Path to the source PDF ('Annexure_A_Pages.pdf').
        output_dir: Directory where the output 'Vote_{n}.pdf' files will be saved.
                    Defaults to the current directory.
        max_vote_num: The highest vote number to check for (default is 14).

    Returns:
        A list of filenames that were successfully created. Returns None on error.
    """
    if not os.path.exists(input_pdf_path):
        print(f"Error: Input file not found at '{input_pdf_path}'")
        return None

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: '{os.path.abspath(output_dir)}'")

    # Dictionary to store page indices (0-based) for each vote number
    # Use defaultdict for convenience: pages_by_vote[vote_num] will automatically be [] if not yet set
    pages_by_vote = collections.defaultdict(list)
    created_files = []

    try:
        # Open the source document
        with pymupdf.open(input_pdf_path) as source_doc:
            print(f"\nProcessing '{input_pdf_path}' ({source_doc.page_count} pages)...")

            # 1. Classify pages by Vote number
            for page_num, page in enumerate(source_doc):
                found_vote = False
                # Check for patterns "Annexure A to Vote 1" through "Annexure A to Vote 14"
                for vote_n in range(10, max_vote_num + 1):
                    search_text = f"Annexure A to Vote {vote_n}"
                    instances = page.search_for(search_text, quads=False)
                    if instances:
                        print(f"  Page {page_num + 1} matches: '{search_text}'")
                        pages_by_vote[vote_n].append(page_num)
                        found_vote = True
                        break # Assume a page belongs to only one vote number

                if not found_vote:
                     print(f"  Warning: Page {page_num + 1} did not match any 'Annexure A to Vote {{n}}' pattern.")

            print("\nFinished scanning pages. Creating output PDFs...")

            # 2. Create a new PDF for each Vote number that has matching pages
            for vote_n in range(10, max_vote_num + 1):
                page_indices = pages_by_vote.get(vote_n) # Use .get() to handle potential missing keys safely

                if page_indices: # Check if there are pages for this vote number
                    output_filename = f"Vote_{vote_n}.pdf"
                    output_filepath = os.path.join(output_dir, output_filename)
                    print(f"  Creating '{output_filename}' with {len(page_indices)} page(s)...")

                    new_vote_doc = None # Initialize for finally block
                    try:
                        new_vote_doc = pymupdf.open() # Create a new empty document
                        for page_index in page_indices:
                            # Insert the specific page from the source document
                            new_vote_doc.insert_pdf(source_doc, from_page=page_index, to_page=page_index)

                        # Save the newly created PDF for this vote number
                        new_vote_doc.save(output_filepath, garbage=4, deflate=True)
                        created_files.append(output_filepath)

                    except Exception as save_error:
                        print(f"    Error creating or saving '{output_filename}': {save_error}")
                    finally:
                        if new_vote_doc:
                            new_vote_doc.close()
                else:
                    print(f"  No pages found for Vote {vote_n}. Skipping file creation.")

    except Exception as e:
        print(f"\nAn critical error occurred during processing: {e}")
        return None # Indicate failure

    print(f"\nProcess finished. {len(created_files)} file(s) created.")
    return created_files

def invoke_split_pdf_by_vote():
    input_file = os.path.join(os.getcwd(), 'data', 'votes', 'Vote_1.pdf')  # The PDF created in the previous step
    output_directory = "votes"      # Folder to save the split PDFs

    # --- Run the script ---
    if os.path.exists(input_file):
        successful_files = split_pdf_by_vote(input_file, output_directory)
        if successful_files is not None:
            print("\nSuccessfully created files:")
            for f in successful_files:
                print(f"- {f}")
        else:
            print("\nPDF splitting process encountered an error.")
    else:
        print(f"Error: Input file '{input_file}' not found in the current directory.")

# process the pdf of vote 1 and seperate votes from 10 -> 14
# populate those votes accordingly

def count_text_instances(pdf_path: str, search_phrases: List[str]) -> Dict[str, int]:
    """
    Searches a PDF document for multiple text phrases across all pages
    and counts the total number of instances for each phrase.

    Args:
        pdf_path: The file path to the PDF document.
        search_phrases: A list of exact text strings to search for (case-sensitive).

    Returns:
        A dictionary where keys are the search phrases and values are the
        total counts of instances found for each phrase throughout the document.
        Returns an empty dictionary if the file cannot be processed or is not found.
    """
    results = {phrase: 0 for phrase in search_phrases} # Initialize counts to 0

    if not os.path.exists(pdf_path):
        print(f"Error: File not found at '{pdf_path}'")
        return {} # Return empty dict on file not found

    doc = None # Initialize doc to None for finally block
    try:
        # Use a 'with' statement for robust file handling
        with fitz.open(pdf_path) as doc:
            total_pages = doc.page_count
            print(f"Processing '{pdf_path}' ({total_pages} pages)...")

            # Iterate through each page in the document
            for page_num, page in enumerate(doc):
                # Optional: Print progress
                # if (page_num + 1) % 10 == 0 or page_num == total_pages - 1:
                #     print(f"  Scanning page {page_num + 1}/{total_pages}...")

                # For each page, search for each of the target phrases
                for phrase in search_phrases:
                    # page.search_for() returns a list of Rect objects (bounding boxes)
                    # The length of this list is the number of times the phrase appears on this page
                    instances_on_page = page.search_for(phrase, quads=False)
                    count_on_page = len(instances_on_page)

                    # Add the count from this page to the total count for the phrase
                    if count_on_page > 0:
                        results[phrase] += count_on_page

    except Exception as e:
        print(f"An error occurred while processing '{pdf_path}': {e}")
        return {} # Return empty dict on error

    print("Processing complete.")
    return results


def invoke_count_text_instances():
    pdf_file = os.path.join(os.getcwd(), 'data', 'votes', 'Vote_1.pdf')  # Path to the PDF you want to search'Vote_1.pdf' # Path to the PDF you want to search

    phrases_to_search = [
        "Vote 10",
        "Vote 11",
        "Vote 12",
        "Vote 13",
        "Vote 14"
    ]

    # Call the function to get the counts
    instance_counts = count_text_instances(pdf_file, phrases_to_search)

    # Print the results
    if instance_counts: # Check if the dictionary is not empty (i.e., no error occurred)
        print("\nTotal instances found for each phrase:")
        for phrase, count in instance_counts.items():
            print(f"- '{phrase}': {count} instance(s)")
    else:
        print("\nCould not retrieve counts due to an error or file not found.")

invoke_split_pdf_by_vote()
