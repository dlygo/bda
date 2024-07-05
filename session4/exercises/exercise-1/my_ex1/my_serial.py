from my_tools import *
import time

img_urls = load_data('/Users/darek/dev/BDA/bda/session4/exercises/exercise-1/image_urls.txt')

t1 = time.perf_counter()

for img_url in img_urls:
    get_img(img_url)

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')