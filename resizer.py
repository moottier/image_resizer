from PIL import Image
from PIL.Image import Image as T_Image
from typing import List, Tuple, Union
from argparse import ArgumentParser
import sys, re, os

# Types
Number = Union[float, int]
ImageSize = Tuple[Number, Number]    # L x H

def resize(path: str, size: ImageSize) -> T_Image:
    with Image.open(path) as img:
        img = img.resize(size)
    return img

def save_image(img: T_Image, path):
    split_path = os.path.splitext(path)
    img.save(f'{split_path[0]}-{size[0]}x{size[1]}{split_path[1]}')
    
def parse_size(size: str) -> ImageSize:
    size = size.lower()
    regx = re.compile(r'^(\d+)x(\d+)$')
    matches = regx.match(size)
    if matches: 
        groups = matches.groups()
    else:
        raise ValueError(f"Invalid size while parsing: {size}")
    groups = (int(groups[0]), int(groups[1]))    
    return groups

def validate_size(size: str) -> bool:
    is_valid = True
    size = size.lower()
    if len(size) < 3:
        is_valid = False
    elif len(size) > 20:    # arbitrary maximum
        is_valid = False
    elif 'x' not in size.lower():
        is_valid = False
    elif size[0] == 'x' or size[-1] == 'x':
        is_valid = False
    elif not all([char in '0123456789' for char in size.replace('x','')]):
        is_valid = False
    return is_valid

def validate_path(path: str) -> bool:
    return os.path.isfile(path)

def get_sizes(sizes: List[str]) -> List[ImageSize]:
    image_sizes = []
    for size in sizes:
        if not validate_size(size): raise ValueError(f'Invalid size: {size}')    
        image_sizes.append(parse_size(size))            
    return image_sizes

def resize_images(image_paths: List[str], image_sizes: List[ImageSize]):
    for path in image_paths:
        for size in image_sizes:
            img = resize(path, size)

def get_parser() -> ArgumentParser:
    parser = ArgumentParser(description='Resize images')
    parser.add_argument('img_paths', nargs='+', type=str)
    parser.add_argument('--sizes', '-s', nargs='+', type=str, required=True)
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    for path in args.img_paths:
        if not validate_path(path): raise FileNotFoundError('File not found: {path}')
    for size in args.sizes:
        if not validate_size(size): raise ValueError('Invalid size: {size}')
    
    img_sizes = get_sizes(args.sizes)
    resize_images(args.img_paths, img_sizes)
    