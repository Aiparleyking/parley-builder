# auto_save.py

import os
from datetime import datetime

def save_daily_picks(picks, vip_picks, output_folder="daily_picks"):
    """
    Saves today's picks and VIP picks into text files.

    Args:
        picks (list): List of dictionaries for normal picks.
        vip_picks (list): List of dictionaries for VIP picks.
        output_folder (str): Folder to save the files into.
    """

    # Create folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    today = datetime.now().strftime("%Y-%m-%d")

    normal_path = os.path.join(output_folder, f"{today}_picks.txt")
    vip_path = os.path.join(output_folder, f"{today}_vip.txt")

    # Save normal picks
    with open(normal_path, "w") as f:
        f.write("=== Daily Picks ===\n\n")
        for pick in picks:
            f.write(f"Name: {pick['name']}\n")
            f.write(f"Team: {pick['team']}\n")
            f.write(f"Opponent: {pick['opponent']}\n")
            f.write(f"Confidence: {pick['confidence']} Stars\n")
            f.write("\n")

    # Save VIP picks
    with open(vip_path, "w") as f:
        f.write("=== VIP Picks ===\n\n")
        for pick in vip_picks:
            f.write(f"🔥 Name: {pick['name']}\n")
            f.write(f"Team: {pick['team']}\n")
            f.write(f"Opponent: {pick['opponent']}\n")
            f.write(f"Confidence: {pick['confidence']} Stars\n")
            f.write("\n")

    print(f"\n💾 Picks saved to {output_folder}!")

