import os

# Path to the cleaned repository URLs file
urls_file = 'cleaned_repo_urls.txt'

# Directory where repositories will be cloned
clone_dir = 'cloned_repositories'

# Create the directory if it doesn't exist
os.makedirs(clone_dir, exist_ok=True)

# Read repository URLs from the file
with open(urls_file, 'r') as f:
    repo_urls = f.read().splitlines()

# Clone repositories
for repo_url in repo_urls:
    repo_name = repo_url.split('/')[-1].replace('.git', '')

    # Check if the folder already exists
    repo_path = os.path.join(clone_dir, repo_name)
    suffix = 1
    while os.path.exists(repo_path):
        repo_path = os.path.join(clone_dir, f"{repo_name}_{suffix}")
        suffix += 1
    
    print(f"Cloning '{repo_name}' from {repo_url} to {repo_path}")
    os.system(f"git clone {repo_url} {repo_path}")

print("Cloning process completed.")
