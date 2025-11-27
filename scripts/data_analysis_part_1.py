import pandas as pd

match_list = []

# Separating the wimbledon matches (Semi's and Finals) between 2000 and 2024
for n in range(2000,2025):
    if n == 2020:
        continue
    next_file = pd.read_csv(f"../ATP match data/atp_matches_{n}.csv")
    wimbledon_matches = next_file[next_file['tourney_name'] == "Wimbledon"]
    spec_matches = wimbledon_matches[(wimbledon_matches['round'] == "F") | (wimbledon_matches['round'] == "SF")]
    match_list.append(spec_matches)

    # print(wimbledon_matches)

comb_match_list = pd.concat(match_list)

comb_match_list.to_csv("../ATP match data/wimbledon_f_sf.csv", mode="a", header=True)
