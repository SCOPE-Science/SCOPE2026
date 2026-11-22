---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational verification

The claim is verified by two independently constructed programs, `game_color_check.cpp` (C++17) and `game_color_check.py` (Python standard library). Both are self-contained, use no external data or imports beyond the Python standard library, and enumerate every vertex deletion for the two fixed finite labelled graphs.

```sh
g++ -std=c++17 -O2 game_color_check.cpp -o game_color_check
./game_color_check
python3 game_color_check.py
```

Both runs completed with the terminal `ALL CHECKS PASS`. For all 11 Grötzsch deletion indices and all 12 Chvátal deletion indices, both implementations separately reported `game3=0` and `game4=1`, with explicit three-colourable and non-two-colourable checks. Original graphs are checked to be four-chromatic, and four game colours are sufficient on each.

Every game search recursively examines *all* legal assignments of a palette colour to an uncoloured vertex, with existential choice on Alice turns and universal choice on Bob turns. The uncoloured count strictly decreases. Memoized states differ only by permutations of the palette names; no unproved graph automorphisms are used. A fully coloured position is Alice-winning, and an uncoloured vertex with all colours appearing on neighbours proves immediate Bob victory since colours cannot be erased. No randomized, partial, timed-out, or depth-limited search is used. The proof is for precisely 23 finite deletion games, not for a general class of critical graphs.

No human-independent verification or formal-proof certificate is claimed.
