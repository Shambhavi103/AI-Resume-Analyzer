import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_jobs(cleaned_resume_text, job_file):

    # Read job datasetdef match_jobs(cleaned_resume_text, job_file):
    jobs = pd.read_csv(job_file)

    # Resume text + all job skill text
    documents = [cleaned_resume_text] + jobs["Skills"].tolist()

    # Convert text to TF-IDF vectors
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    # Resume vector
    resume_vector = tfidf_matrix[0]

    # Job vectors
    job_vectors = tfidf_matrix[1:]

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(resume_vector, job_vectors)

    jobs["Match Score"] = similarity_scores.flatten() * 100

    jobs = jobs.sort_values(by="Match Score", ascending=False)

    return jobs