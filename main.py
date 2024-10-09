with open('wallets.txt', 'r') as wallet_file, open('optimism.csv', 'r') as optimism_file:
    wallet_lines = wallet_file.read().splitlines()
    optimism_lines = optimism_file.read().splitlines()

optimism_dict = {}
for line in optimism_lines:
    address, balance = line.split(',')
    optimism_dict[address.lower()] = balance

with open('res.txt', 'w') as result_file:
    for wallet in wallet_lines:
        wallet_lower = wallet.lower()
        if wallet_lower in optimism_dict:
            result_file.write(f"{wallet},{optimism_dict[wallet_lower]}\n")

print("The comparison is complete. The results are recorded")
