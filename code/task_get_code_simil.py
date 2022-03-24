# Imports
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer



# Prepare directories
df = pd.read_csv('data/manual_code.csv', encoding='utf-8', sep=';')

# Get first three rows
print(df.head(3))


# Train a model to detect the language
df = df[df['platafor'].notnull()]


# Get subset
subset = df[(df.platafor == 'WIN') & (df.tipo == 'SQLFUNC')]



# Get text features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(subset['corpo'].values)
arr = X.toarray()


# Debug print
print(arr)

# Obtain similarities based on cosine
print(subset['corpo'])



# Process similarities
sims = cosine_similarity(arr)
for i in range(sims.shape[0]):
    for j in range(sims.shape[1]):
        if i == j:
            sims[i][j] = 0



# Get maximum similarity values
max_similarity = np.argmax(sims, axis=1)


# Get interest similarity values
similarity_values = sims[np.arange(len(sims)), max_similarity]
print(similarity_values)


# Convert this to .CSV results
subset['most_similar'] = subset.iloc[max_similarity]['corpo'].values
subset['similarity_values'] = similarity_values
subset['most_similar_idx'] = max_similarity

# Debug print
print(subset.head(5))


# Save results into .CSV
subset.to_csv('resultados.csv')


# Some debug prints
print(subset.iloc[33])
print(print(subset.iloc[33].corpo))
print(print(subset.iloc[2578].corpo))
