def main() -> None:
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print()
    print("=== Achievement Analytic ===")
    unique = alice | bob | charlie
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievement: {len(unique)}")
    common = alice & bob & charlie
    print(f"Common to all players: {common}")
    all_item = alice | bob | charlie
    shared = (alice & bob) | (bob & charlie) | (alice & charlie)
    rare = all_item - shared
    print(f"Rare achievements (1 player) {rare}")
    AB_common = alice & bob
    print(f"Alice vs Bob common {AB_common}")
    unique_alice = alice - bob 
    print(f"Alice unique: {unique_alice}")
    unique_bob = bob - alice
    print(f"Bob unique: {unique_bob}")
 
if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    main()