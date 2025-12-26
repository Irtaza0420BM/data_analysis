import pandas as pd

fl_data = pd.read_csv("Rofan_Historical (Hair Colors) - FL.csv", header=None)
ml_data = pd.read_csv("Rofan_Historical (Hair Colors) - ML.csv", header=None)


def analyze(df, name):
    print(f"\n{name}")
    print(f"Shape: {df.shape}")
    
    colors = {}
    total = 0
    
    for i in range(0, len(df), 3):
        color = str(df.iloc[i, 0]).strip().lower()
        
        if color not in colors:
            colors[color] = 0
        
        for j in range(1, len(df.columns)):
            if pd.notna(df.iloc[i+2, j]):
                colors[color] += 1
                total += 1
    
    print(f"Total Shows: {total}")
    print(f"Unique Colors: {len(colors)}\n")
    
    for color, count in sorted(colors.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total * 100) if total > 0 else 0
        print(f"{color}: {count} shows ({percentage:.1f}%)")


def search(df_fl, df_ml, keywords):
    results = []
    seen = set()  # Track unique shows
    
    # Search FL
    for i in range(0, len(df_fl), 3):
        color = str(df_fl.iloc[i, 0]).strip().lower().replace('\n', ' ')
        for j in range(1, len(df_fl.columns)):
            if pd.notna(df_fl.iloc[i+2, j]):
                show = str(df_fl.iloc[i+2, j]).replace('\n', ' ').strip()
                if any(kw.lower() in show.lower() for kw in keywords):
                    if show not in seen:
                        seen.add(show)
                        results.append({
                            "Show Name": show,
                            "Data Source": "FL",
                            "Hair Color": color,
                            # "Score": "",
                            # "Rating": "",
                            # "Want to Watch": ""
                        })
    
    # Search ML
    for i in range(0, len(df_ml), 3):
        color = str(df_ml.iloc[i, 0]).strip().lower().replace('\n', ' ')
        for j in range(1, len(df_ml.columns)):
            if pd.notna(df_ml.iloc[i+2, j]):
                show = str(df_ml.iloc[i+2, j]).replace('\n', ' ').strip()
                if any(kw.lower() in show.lower() for kw in keywords):
                    if show not in seen:
                        seen.add(show)
                        results.append({
                            "Show Name": show,
                            "Data Source": "ML",
                            "Hair Color": color,
                            # "Score": "",
                            # "Rating": "",
                            # "Want to Watch": ""
                        })
    
    # Write to CSV with proper quoting
    df_results = pd.DataFrame(results)
    df_results.to_csv("search_results.csv", index=False, quoting=1)
    print(f"\nFound {len(results)} shows. Saved to 'search_results.csv'")
    return df_results


    
analyze(fl_data, "FL Analysis")
analyze(ml_data, "ML Analysis")

search(fl_data, ml_data, ["husband", "hubby", "wife" , "marriage" , "married", "love", "bride"])