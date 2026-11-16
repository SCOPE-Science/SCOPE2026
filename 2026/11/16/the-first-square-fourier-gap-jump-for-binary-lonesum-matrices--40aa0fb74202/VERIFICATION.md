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
# Verification

The reproducible integer checker `checker.py` requires only Python 3. Running `python3 checker.py DIR` regenerates both CSV certificates, with fixed row-major bit coordinates and reproducible lexicographic frequency representatives.

The two lonesum predicates (nested rows, forbidden permutation patterns) agree for every binary matrix at each square size two, three, four. An independent direct-character orbit calculation, using all 317 row/column-permutation frequency orbits, agrees with every entry from a full integer Walsh butterfly. The full transform passes Parseval, complement-translation zeros, and the congruence modulo 16. The exact 4-by-4 counts are 6902 lonesum matrices, 32768 nonzero modes, 34 positive magnitudes, 6360 modes of minimum magnitude 6, and 317 signed-frequency orbits. Baselines at square sizes two and three have minimum 2.

Replayed success message: `SQUARE_LONESUM_ORBIT_WALSH_EXACT_PASS`.

The finite exhaustive checker establishes only the explicitly enumerated dimensions. The all-rectangle Fourier-support proof is mathematical and uses the established Stirling enumeration. No independent mathematical audit or publisher certification was performed; historical priority remains bounded.
