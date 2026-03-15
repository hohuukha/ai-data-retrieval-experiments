import random

datasets = [
    "documents",
    "embeddings",
    "media_assets",
    "knowledge_base"
]

def simulate_ai_query():
    reads = random.randint(5, 15)
    accessed = random.choices(datasets, k=reads)

    print("Simulated AI query reads:")
    for item in accessed:
        print("-", item)

if __name__ == "__main__":
    simulate_ai_query()
