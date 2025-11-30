#!/usr/bin/env python3
"""
Markdown (.md) files documentation script.

.md files are Markdown documents—plain text files with a .md extension that use 
simple syntax (like # for headings, * for lists) to create formatted content 
that renders as HTML in browsers, GitHub, etc.
"""

def print_markdown_intro():
    """
    Display the main definition and purpose of .md (Markdown) files.
    
    Prints the core explanation of what Markdown files are and how they work.
    """
    print(".md files are Markdown documents—plain text files with a .md extension")
    print("that use simple syntax (like # for headings, * for lists) to create")
    print("formatted content that renders as HTML in browsers, GitHub, etc.")

def print_common_uses():
    """
    Print common practical uses of Markdown files.
    
    Covers typical scenarios where developers use .md files in projects.
    """
    print("\nCommon uses")
    print("README.md: Project documentation in Git repositories (what it does,")
    print("  how to install/use)")
    print("Technical docs, wikis, blogs where you want readable source +")
    print("  nice rendered output")
    print("Notes, API references, changelogs that need structure without")
    print("  complex editors")

def print_why_developers_love_them():
    """
    Explain why developers prefer Markdown files.
    
    Highlights Git compatibility, auto-rendering, and plain text advantages.
    """
    print("\nWhy developers love them")
    print("Markdown is plain text (works with any editor, Git-friendly) but")
    print("converts to rich HTML. GitHub auto-renders .md files, so your")
    print("Cepheid API.py commit message or a new README.md would show")
    print("formatted text automatically.")

def print_example():
    """
    Show a concrete Markdown syntax example.
    
    Demonstrates how # API Reference becomes a big heading when rendered.
    """
    print("Example: # API Reference → big heading when viewed on GitHub.")

def main():
    """
    Main entry point that orchestrates the complete Markdown documentation display.
    
    Calls all functions in sequence to match the exact requested format and content.
    """
    print_markdown_intro()
    print_common_uses()
    print_why_developers_love_them()
    print_example()

if __name__ == "__main__":
    """
    Standard execution guard for the Markdown documentation script.
    
    Ensures main() runs only when script is executed directly, not when imported.
    """
    main()
