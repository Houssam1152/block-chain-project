from tp import blockchain   

bc = blockchain(diff=1)
bc.add_blok("SOHAIB GIVES 500 DZD")
bc.add_blok("ABDOU pays MOHAMMED 2 coins")
print("\n--- FULL CHAIN ---")
for bl in bc.chain:
    print(vars(bl))

print("\n--- VALIDATION ---")
print("Chain valid?", bc.is_valide())
print("\n--- TAMPERING TEST ---")
bc.chain[1].data = "HACKED DATA"
print("Chain valid after tampering?", bc.is_valide())
