from openai import AzureOpenAI
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

 

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
client = AzureOpenAI(
  api_key=os.environ['AZURE_OPENAI_KEY'],  # this is also the default, it can be omitted
  api_version = "2023-05-15",
  azure_endpoint=os.environ['AZURE_OPENAI_ENDPOINT'] 
  )

model = os.environ['AZURE_OPENAI_DEPLOYMENT']


try:
    # Create an image by using the image generation API

    generation_response = client.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=1,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except client.error.InvalidRequestError as err:
    print(err)

# ---creating variation below---


response = client.Image.create_variation(
  image=open(image_path, "rb"),
  n=1,
  size="1024x1024"
)
=======
# response = openai.Image.create_variation(
#   image=open(image_path, "rb"),
#   n=1,
#   size="1024x1024"
# )

# image_path = os.path.join(image_dir, 'generated_variation.png')

# image_url = response['data'][0]['url']

# generated_image = requests.get(image_url).content  # download the image
# with open(image_path, "wb") as image_file:
#     image_file.write(generated_image)

# # Display the image in the default image viewer
# image = Image.open(image_path)
# image.show()