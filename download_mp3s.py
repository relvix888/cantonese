import requests
import os

def download_mp3s(url_file="urls.txt"):
    """
    Reads a list of URLs from a file and downloads each MP3.

    Args:
        url_file (str): The name of the text file containing the URLs.
    """
    try:
        with open(url_file, 'r') as f:
            urls = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file '{url_file}' was not found.")
        return

    print(f"Found {len(urls)} URLs. Starting download...")
    
    download_count = 0
    for url in urls:
        url = url.strip()
        if not url:
            continue
            
        try:
            # Get the filename from the URL (e.g., 'aau2.mp3')
            filename = os.path.basename(url)
            
            # Download the file
            print(f"Downloading {filename}...")
            response = requests.get(url)
            response.raise_for_status() # Raise an exception for bad status codes
            
            # Save the file
            with open(filename, 'wb') as f:
                f.write(response.content)
            
            download_count += 1
            
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {url}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {url}: {e}")
            
    print(f"\nDownload finished. Successfully downloaded {download_count} files.")

if __name__ == "__main__":
    download_mp3s()
