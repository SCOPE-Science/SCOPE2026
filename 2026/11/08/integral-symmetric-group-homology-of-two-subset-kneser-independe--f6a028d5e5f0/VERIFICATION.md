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

# Reproducibility and limits

Run `python3 verify_kneser.py` using Python 3.9 or newer; only the standard library is required. The expected exact standard output is `verify_kneser.out`. The script enumerates all independent faces from the elementary star/triangle classification for ground sets of sizes 4 through 7, checks every signed fixed-simplex Lefschetz sum against the uniform character formula over 5,904 relabelings, verifies simplicial Betti numbers directly modulo two and three for each tested size, verifies all triangle boundary cycles and an explicit integral identity minor on the non-tree chords, and checks the alternating face count.

The infinite family and integral lattice are proved in RESULT.md by a structural relative-chain argument and a split-exact lattice computation. No finite test certifies an infinite family by itself. The code verifies particular cases and algebraic sign normalizations but does not constitute independent mathematical review.
