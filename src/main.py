from textnode import TextNode, TextType
from inline_markdown import *
from markdown_block import *

def main():
    text = '''
    # This is a heading

    This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

    - This is the first list item in a list block
    - This is a list item
    - This is another list item
    '''

    blocks = markdown_to_blocks(text)
    print(blocks)

main()