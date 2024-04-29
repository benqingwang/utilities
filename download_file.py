import requests

def download_file(url, local_filename):
    # Send a GET request to the URL
    with requests.get(url, stream=True) as r:
        # Raise an exception for bad responses
        r.raise_for_status()
        # Open a local file in binary write mode
        with open(local_filename, 'wb') as f:
            # Write the content to the file in chunks
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

# URL of the file you want to download
url = "http://example.com/somefile.pdf"
# Local path where the file will be saved
local_filename = "downloaded_file.pdf"

# Call the function to download the file
download_file(url, local_filename)
