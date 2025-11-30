#!/usr/bin/env python3
"""
Script to display Cepheid library API reference in formatted output.

This script prints API documentation information for the Cepheid Rust library
in a clean, readable format matching the provided example. The output includes
links to GitHub and Hexdocs.pm documentation for modules and their descriptions.
"""

def print_api_reference():
    """
    Print the API Reference section with GitHub and Hexdocs links.
    
    Format:
        API Reference
        [GitHub link]
        [Hexdocs link]
    """
    print("API Reference")
    print("[](https://github.com/jmcguigs/cepheid)")
    print("[](https://hexdocs.pm/cepheid/api-reference.html#modules)")
    print()

def print_modules():
    """
    Print the Modules section with module names, descriptions, and documentation links.
    
    Lists all modules with their individual Hexdocs.pm documentation URLs.
    """
    print("Modules")
    print("[Cepheid](https://hexdocs.pm/cepheid/Cepheid.html)")
    print("Documentation for [Cepheid](https://hexdocs.pm/cepheid/Cepheid.html).")
    print()
    
    print("[Cepheid.Normalization.Magnitude](https://hexdocs.pm/cepheid/Cepheid.Normalization.Magnitude.html)")
    print("Functions for normalizing the magnitude of light curves.")
    print()
    
    print("[Cepheid.Periodicity.Pdm](https://hexdocs.pm/cepheid/Cepheid.Periodicity.Pdm.html)")
    print("Functions for Phase Disperion Minimization (PDM) analysis.")
    print()

def main():
    """
    Main entry point that orchestrates printing of API reference documentation.
    
    Calls functions to display API reference header and module documentation
    in the exact format requested.
    """
    print_api_reference()
    print_modules()

if __name__ == "__main__":
    """
    Standard Python idiom to run main() when script is executed directly.
    
    Allows the script to be imported as a module without automatically executing.
    """
    main()
