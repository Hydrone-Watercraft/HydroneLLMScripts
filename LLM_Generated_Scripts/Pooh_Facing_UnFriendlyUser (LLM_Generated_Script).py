# Generated from prompt: Pooh_Facing_UnFriendlyUser (prompt)
# Source prompt file: prompts_water_drone\Pooh_Facing_UnFriendlyUser (prompt).txt


# Winnie-the-Pooh meets an unfriendly approach: gentle, cautious, and kind within a 1m pool (radius 0.5m). Max_DURATION = 30s

send_command(-20, -20, pump=80, duration=0.5)  # Startled recoil: "Oh, bother!"—a quick splash backward (~0.20 m)

send_command(0, 0, pump=45, duration=1.5)  # Pooh hums softly, staying calm

send_command(10, 10, pump=50, duration=0.5)  # A small, polite peek forward (~0.10 m), showing friendliness
send_command(-10, -10, pump=55, duration=0.5)  # And back again (~0.10 m), keeping a courteous distance

send_command(20, -20, pump=40, duration=0.25)  # Turn 45° CW to sidestep the tension
send_command(12, 12, pump=40, duration=0.75)  # Gentle diagonal glide (~0.18 m) with calming ripples

send_command(0, 0, pump=45, duration=1.0)  # Pause; a thoughtful hum

send_command(-20, 20, pump=45, duration=0.5)  # Turn 90° ACW for a softer angle
send_command(10, 10, pump=42, duration=1.0)  # Slow approach (~0.20 m), showing no harm

send_command(0, 0, pump=70, duration=0.8)  # Friendly fountain pulse—Pooh's gentle offer of goodwill

send_command(20, -20, pump=45, duration=0.25)  # Turn 45° CW to face the user again
send_command(-10, -10, pump=55, duration=0.6)  # Cautious retreat (~0.12 m), respecting space

send_command(0, 0, pump=45, duration=1.0)  # Soft hum; thinking what a Bear of Very Little Brain might do

send_command(10, -10, pump=40, duration=4.0)  # Slow 360° turn in place (2x slower), a shy, soothing circle

send_command(10, 10, pump=45, duration=0.4)  # Tiny approach (~0.08 m), hopeful and gentle
send_command(-15, -15, pump=75, duration=0.2)  # Little flinch (~0.06 m back) if things still feel unfriendly

send_command(20, -20, pump=45, duration=0.5)  # Turn 90° CW to drift aside
send_command(10, 10, pump=40, duration=0.8)  # Side glide (~0.16 m), keeping the mood light

send_command(-20, 20, pump=45, duration=0.5)  # Turn 90° ACW back to face the user

send_command(0, 0, pump=65, duration=1.2)  # A warm, longer fountain—Pooh's friendly "Would you like some honey?"

send_command(0, 0, pump=40, duration=2.0)  # Calm pause, inviting peace

# Gentle square drift around the center to show harmlessness and keep safe distance
send_command(10, 10, pump=45, duration=0.7)  # Forward (~0.14 m)
send_command(20, -20, pump=45, duration=0.5)  # Turn 90° CW
send_command(10, 10, pump=45, duration=0.7)  # Forward (~0.14 m)
send_command(20, -20, pump=45, duration=0.5)  # Turn 90° CW
send_command(10, 10, pump=45, duration=0.7)  # Forward (~0.14 m)
send_command(20, -20, pump=45, duration=0.5)  # Turn 90° CW
send_command(10, 10, pump=45, duration=0.7)  # Forward (~0.14 m) back near the start of the loop

send_command(10, 10, pump=60, duration=0.3)  # Friendly nudge forward (~0.06 m) with a kind splash

send_command(0, 0, pump=45, duration=1.0)  # Soft hum; Pooh remains gentle and patient

# A shy bow
send_command(20, -20, pump=45, duration=0.25)  # Turn 45° CW (a polite angle)
send_command(10, 10, pump=50, duration=0.5)  # Bow forward (~0.10 m)
send_command(-10, -10, pump=50, duration=0.5)  # Bow back (~0.10 m)
send_command(-20, 20, pump=45, duration=0.25)  # Turn 45° ACW back to straight

send_command(0, 0, pump=40, duration=2.0)  # Steady calm: "Let's be friends?"

send_command(-10, 10, pump=50, duration=2.0)  # Slow 180° ACW turn in place—showing openness from all sides
send_command(0, 0, pump=45, duration=0.15)  # Final peaceful hum

# Total_time = 0.5+1.5+0.5+0.5+0.25+0.75+1.0+0.5+1.0+0.8+0.25+0.6+1.0+4.0+0.4+0.2+0.5+0.8+0.5+1.2+2.0+0.7+0.5+0.7+0.5+0.7+0.5+0.7+0.3+1.0+0.25+0.5+0.5+0.25+2.0+2.0+0.15 = 30.0 seconds