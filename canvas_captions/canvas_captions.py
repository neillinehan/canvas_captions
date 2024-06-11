import urllib.request
import json
import os

def write_wistia_captions_to_file(captions_url: str) -> None:
    """
    Fetches captions from a Wistia JSON file at a given URL and writes them to a text file.
    This function is specifically designed to work with Wistia caption JSON files and may not work with JSON files from other sources.

    Parameters:
    captions_url (str): The URL where the Wistia captions JSON file is located.

    Returns:
    None
    """
    try:
        # Open the connection to the URL
        with urllib.request.urlopen(captions_url) as url:
            # Convert the response data to a Python dictionary
            data = json.loads(url.read().decode())

        # Extract the lines of text from the data
        lines = data['captions'][0]['hash']['lines']

        # Flatten the list of lines and extract the text
        flat_list = [item for sublist in lines for item in sublist['text']]

        # Join the strings with a space
        long_str = ' '.join(flat_list)

        # Extract the filename from the URL
        filename = os.path.splitext(os.path.basename(captions_url))[0]

        # Open the file in write mode
        with open(f"{filename}.txt", "w") as f:
            # Write the string to the file
            f.write(long_str)

    except Exception as e:
        print(f"An error occurred: {e}")
