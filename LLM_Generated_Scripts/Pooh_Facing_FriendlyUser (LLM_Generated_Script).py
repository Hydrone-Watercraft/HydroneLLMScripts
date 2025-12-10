# Generated from prompt: Pooh_Facing_FriendlyUser (prompt)
# Source prompt file: prompts_water_drone\Pooh_Facing_FriendlyUser (prompt).txt


# Winnie-the-Pooh spots the friendly user and offers a gentle, honey-ish hello from the pool's center.
send_command(0, 0, pump=60, duration=1.0)  # Soft hello mist, Pooh hums a little "hummy hum"

# Pooh toddles forward carefully (0.3 m at speed 10 → 1.5 s), staying well within the 0.5 m radius.
send_command(10, 10, pump=0, duration=1.5)  # Position ≈ +0.3 m toward the user

send_command(0, 0, pump=70, duration=0.8)   # Warm, friendly fountain pulse—Pooh smiles

# Curious glances, gentle and slow, without moving from the spot.
send_command(10, -10, pump=0, duration=0.5) # Turn ~45° clockwise to peek
send_command(0, 0, pump=50, duration=0.5)   # Thoughtful hum
send_command(-10, 10, pump=0, duration=1.0) # Turn ~90° anti-clockwise to peek the other side
send_command(0, 0, pump=50, duration=0.5)   # Another soft hum
send_command(10, -10, pump=0, duration=0.5) # Return to face the user

# A tiny friendly step closer (0.1 m at speed 10 → 0.5 s). Now at +0.4 m.
send_command(10, 10, pump=0, duration=0.5)

# A delighted, gentle spin—full 360° at slow speed with a honey-spray shimmer.
send_command(10, -10, pump=60, duration=4.0) # In-place twirl; no translation

# Pooh offers a little "honey" splash and edges forward just a smidge (0.1 m → now at +0.5 m max).
send_command(10, 10, pump=80, duration=0.5)
send_command(0, 0, pump=100, duration=1.0)   # Big friendly gush

# Give the friend a bit of space (back 0.2 m at speed 10 → 1.0 s). Position returns to +0.3 m.
send_command(-10, -10, pump=50, duration=1.0)

# Rhythmic "hummy hum" bounces—Pooh rocks happily without drifting from +0.3 m.
send_command(0, 0, pump=70, duration=1.5)    # Cycle 1: hum
send_command(10, 10, pump=80, duration=0.25) # Tiny hop forward +0.05 m → +0.35 m
send_command(-10, -10, pump=60, duration=0.25) # Settle back -0.05 m → +0.30 m

send_command(0, 0, pump=70, duration=1.5)    # Cycle 2: hum
send_command(10, 10, pump=80, duration=0.25) # +0.35 m
send_command(-10, -10, pump=60, duration=0.25) # +0.30 m

send_command(0, 0, pump=70, duration=1.5)    # Cycle 3: hum
send_command(10, 10, pump=80, duration=0.25) # +0.35 m
send_command(-10, -10, pump=60, duration=0.25) # +0.30 m

send_command(0, 0, pump=70, duration=1.5)    # Cycle 4: hum
send_command(10, 10, pump=80, duration=0.25) # +0.35 m
send_command(-10, -10, pump=60, duration=0.25) # +0.30 m

# A happy two-part twirl like a little hug and back—end facing the friend.
send_command(10, -10, pump=60, duration=2.0) # 180° clockwise
send_command(-10, 10, pump=60, duration=2.0) # 180° anti-clockwise (return to face user)

# Final gentle wave of the fountain—Pooh hums a friendly goodbye.
send_command(0, 0, pump=70, duration=0.7)

# Total_time = 1.0 + 1.5 + 0.8 + 0.5 + 0.5 + 1.0 + 0.5 + 0.5 + 0.5 + 4.0 + 0.5 + 1.0 + 1.0
#             + (1.5+0.25+0.25)*4 + 2.0 + 2.0 + 0.7 = 30.0 seconds