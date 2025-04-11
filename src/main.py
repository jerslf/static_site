from textnode import TextNode, TextType
from inline_markdown import *
from markdown_blocks import *

def main():
    text = '''
    # This is a heading

    This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

    - This is the first list item in a list block
    - This is a list item
    - This is another list item
    '''

    markdown_to_html_node(text)
    #print(blocks)

main()