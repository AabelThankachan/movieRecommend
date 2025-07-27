import pickle
import gzip

# Load your original .pkl file
with open("similarity.pkl", "rb") as f_in:
    data = pickle.load(f_in)

# Compress and save as .pkl.gz
with gzip.open("similarity.pkl.gz", "wb") as f_out:
    pickle.dump(data, f_out)

print("✅ similarity.pkl has been compressed to similarity.pkl.gz")
