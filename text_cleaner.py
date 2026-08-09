import re

def clean_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove extra spaces and new lines
    text = re.sub(r'\s+', ' ', text)

    # Remove special characters except +, #, .
    text = re.sub(r'[^a-z0-9+#.\s]', '', text)

    return text.strip()


if __name__ == "__main__":

    sample = """
    Name: Shambhavi Fadipatil

    Skills:
    Python, SQL, Machine Learning!!!
    C++, C#, .NET

    Email: xyz@gmail.com
    """

    cleaned = clean_text(sample)

    print("Original Text:\n")
    print(sample)

    print("\nCleaned Text:\n")
    print(cleaned)
    