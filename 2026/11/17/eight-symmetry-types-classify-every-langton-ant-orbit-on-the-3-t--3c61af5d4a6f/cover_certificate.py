"""Independent finite orbit-and-symmetry covering certificate on the 3x3 torus."""
from collections import defaultdict

SIDE = 3
N_CELLS = SIDE * SIDE
N_STATES = (1 << N_CELLS) * N_CELLS * 4
# State encoding: 4 * (9 * black_mask + row_major_position) + direction.
# Compass direction 0=N, 1=E, 2=S, 3=W; positive is clockwise.
REPS = {18: 116, 30: 128, 42: 43, 66: 0,
        70: 40, 74: 42, 78: 120, 102: 385}
EXPECTED_ORBITS = {18: 24, 30: 24, 42: 24, 66: 24,
                   70: 72, 74: 72, 78: 24, 102: 24}

def decode(state):
    direction = state % 4
    k = state // 4
    return k // N_CELLS, k % N_CELLS, direction

def encode(bits, pos, direction):
    return 4 * (N_CELLS * bits + pos) + direction

def move(pos, direction):
    x, y = pos % SIDE, pos // SIDE
    if direction == 0:
        y = (y - 1) % SIDE
    elif direction == 1:
        x = (x + 1) % SIDE
    elif direction == 2:
        y = (y + 1) % SIDE
    else:
        x = (x - 1) % SIDE
    return y * SIDE + x

def step(state):
    bits, pos, direction = decode(state)
    old_color = (bits >> pos) & 1
    direction = (direction + (3 if old_color else 1)) % 4
    return encode(bits ^ (1 << pos), move(pos, direction), direction)

def symmetry(state, rotation, reflect, tx, ty):
    """D4 symmetry; reflection also complements all colors."""
    bits, pos, direction = decode(state)
    def site(p):
        x, y = p % SIDE, p // SIDE
        if reflect:
            x = SIDE - 1 - x
        for _ in range(rotation):
            x, y = SIDE - 1 - y, x
        return ((y + ty) % SIDE) * SIDE + ((x + tx) % SIDE)
    new_bits = (1 << N_CELLS) - 1 if reflect else 0
    for p in range(N_CELLS):
        if (bits >> p) & 1:
            new_bits ^= 1 << site(p) if reflect else 0
            if not reflect:
                new_bits |= 1 << site(p)
    if reflect:
        direction = (4 - direction) % 4
    direction = (direction + rotation) % 4
    return encode(new_bits, site(pos), direction)

def main():
    # Full verification of invertibility (as a permutation) and equivariance.
    successors = [step(state) for state in range(N_STATES)]
    assert len(set(successors)) == N_STATES
    for rotation in range(4):
        for reflect in (0, 1):
            for tx in range(SIDE):
                for ty in range(SIDE):
                    for state in range(N_STATES):
                        assert step(symmetry(state, rotation, reflect, tx, ty)) == symmetry(
                            successors[state], rotation, reflect, tx, ty)
    occupied = bytearray(N_STATES)
    grand_total = 0
    for period, representative in sorted(REPS.items()):
        seen = set()
        current = representative
        for _ in range(period):
            assert current not in seen
            seen.add(current)
            current = successors[current]
        assert current == representative
        orbit_union = set()
        for rotation in range(4):
            for reflect in (0, 1):
                for tx in range(SIDE):
                    for ty in range(SIDE):
                        image = symmetry(representative, rotation, reflect, tx, ty)
                        for _ in range(period):
                            orbit_union.add(image)
                            image = successors[image]
                        assert image == symmetry(representative, rotation, reflect, tx, ty)
        expected_size = period * EXPECTED_ORBITS[period]
        assert len(orbit_union) == expected_size, (period, len(orbit_union), expected_size)
        assert all(occupied[x] == 0 for x in orbit_union)
        for x in orbit_union:
            occupied[x] = 1
        grand_total += len(orbit_union)
        print(f"period={period}, representative={representative}, "
              f"cycles={EXPECTED_ORBITS[period]}, states={len(orbit_union)}")
    assert grand_total == N_STATES and all(occupied)
    assert sum(EXPECTED_ORBITS.values()) == 288
    print(f"CERTIFICATE_OK states={grand_total} cycles=288 symmetry_period_classes=8")

if __name__ == '__main__':
    main()
