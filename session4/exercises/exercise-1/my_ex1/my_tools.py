import os  # Import the os module for interacting with the operating system
import requests  # Import the requests module for making HTTP requests
import random 


def load_data(file_path):
    data_list = []
    # Open the file 'image_urls.txt' in the read mode
    with open(file_path, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Strip whitespace characters from the beginning and end of the line
            line_data = line.strip()
            # Append to the list
            data_list.append(line_data)
        # Return the cleaned data
        return(data_list)


def get_img(img_url):
    # Define the output directory where images will be saved
    output_dir = "/Users/darek/dev/BDA/bda/session4/exercises/exercise-1/my_ex1/output"
    # Create the output directory if it does not exist, if exists do not create
    os.makedirs(output_dir, exist_ok=True)

    # Example URL for demonstration; replace line_data with the actual URL in your code
    #line_data = "https://example.com/path/to/image.jpg"
    # Make an HTTP GET request to download the image content from the web
    img_bytes = requests.get(img_url).content

    # Define the base name for the image file; you can customize this as needed
    # name = "photo-1"
    # Create the full image file name with the .jpg extension
    #img_name = f'{name}.jpg'
    img_name = f'{random.randint(1, 1000)}.jpg'

    # Create the full path for saving the image file
    full_path = os.path.join(output_dir, img_name)
    # full_path = output_dir+'/'+img_name

    # Open the image file in the write-binary mode and save the image content on local disk
    with open(full_path, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded and saved in {output_dir}...')






