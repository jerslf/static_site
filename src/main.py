from textnode import TextNode, TextType

def main():
    node = TextNode("Hello jer", TextType.LINK, "https://www.boot.dev")
    print(node)

main()