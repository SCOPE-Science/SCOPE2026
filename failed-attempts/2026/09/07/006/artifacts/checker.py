"""Stdlib verifier for A(16,6,7) codes. Usage: python3 checker.py code_best77.json
Checks: each entry 16-bit weight 7, pairwise Hamming distance >=6 (intersection <=4).
Rerunnable in seconds with stdlib only. Exits 0 on success, 1 on failure.
"""
import json, sys

def popcnt16(x):
    return bin(x).count("1")

def verify(masks, n=16, w=7, d=6):
    assert len(masks) == len(set(masks)), "duplicate codewords"
    for idx, c in enumerate(masks):
        assert 0 <= c < (1 << n), f"codeword {idx} out of range: {c}"
        wt = popcnt16(c)
        assert wt == w, f"codeword {idx} weight {wt} != {w}"
    pairs = 0
    for i in range(len(masks)):
        for j in range(i+1, len(masks)):
            pairs += 1
            dist = popcnt16(masks[i] ^ masks[j])
            assert dist >= d, f"pair ({i},{j}) distance {dist} < {d}: {masks[i]:016b} vs {masks[j]:016b}"
    return pairs

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "code_best77.json"
    with open(path) as f:
        data = json.load(f)
    # accept either {"masks": [...]} or plain list
    masks = data["masks"] if isinstance(data, dict) and "masks" in data else data
    pairs = verify(masks)
    print(f"OK: {len(masks)} codewords, weight 7, length 16, min distance >=6 ({pairs} pairs checked)")
