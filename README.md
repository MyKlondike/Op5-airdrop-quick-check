title: Quick check Airdrop 5

See the [list of addresses and allocation amounts](https://github.com/ethereum-optimism/op-analytics/blob/main/reference_data/address_lists/op_airdrop_5_simple_list.csv).

This Python script compares wallet addresses from wallets.txt with records from optimism.csv.
If any matches are found (case-insensitive), the script outputs the matching wallet address along with its corresponding balance into res.txt.

Place the wallets.txt and optimism.csv files in the same directory as the script.
Run the script using Python
