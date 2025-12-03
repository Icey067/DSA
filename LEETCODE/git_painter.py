import os
import random
from datetime import datetime, timedelta

# --- CONFIGURATION ---
DAYS_TO_GO_BACK = 365       # How far back to start (e.g., 1 year)
MAX_COMMITS_PER_DAY = 5     # Max commits on a busy day
FREQUENCY = 0.6             # 0.0 to 1.0 (Higher = more days with commits)
# ---------------------

def git_commit(date_str):
    # 1. Create a dummy change
    with open('history.txt', 'a') as file:
        file.write(f'{date_str}\n')
    
    # 2. Stage the file
    os.system('git add history.txt')
    
    # 3. Commit with the specific date
    # We set both Author and Committer dates to ensure the graph picks it up
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = date_str
    env['GIT_COMMITTER_DATE'] = date_str
    
    cmd = f'git commit -m "History update: {date_str}"'
    
    # Run the command with the modified environment
    # We use subprocess to pass the env vars easily, or just os.system with export
    # For simplicity in this script, we use the --date flag which covers the graph visual
    os.system(f'git commit --date="{date_str}" -m "Commit for {date_str}"')

def main():
    today = datetime.now()
    
    print(f"Start painting git history for the last {DAYS_TO_GO_BACK} days...")

    for day_offset in range(DAYS_TO_GO_BACK):
        current_date = today - timedelta(days=day_offset)
        
        # Random logic: Should we commit on this day?
        if random.random() < FREQUENCY:
            # How many times?
            num_commits = random.randint(1, MAX_COMMITS_PER_DAY)
            
            for _ in range(num_commits):
                # Add random hours/minutes to make it look natural
                random_hour = random.randint(0, 23)
                random_minute = random.randint(0, 59)
                random_second = random.randint(0, 59)
                
                commit_date = current_date.replace(
                    hour=random_hour, 
                    minute=random_minute, 
                    second=random_second
                )
                
                # Format: "YYYY-MM-DD HH:MM:SS"
                date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')
                
                git_commit(date_str)
                print(f"Committed: {date_str}")

    print("--- Done! Run 'git push' to update GitHub. ---")

if __name__ == "__main__":
    main()