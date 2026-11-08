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

The seven-dimensional regular-differential basis and semilinear Cartier matrix are written in `RESULT.md`; all exponents in iterates are entrywise inverse Frobenius powers. The polynomial conditions for the four profiles are \(\det H\), \(H\), and \(H^{[4]}H\). The equality \(TT^{[1/4]}=0\iff H^{[4]}H=0\) uses entrywise raising to the sixteenth power.

To reproduce finite-field checks, run `python3 verify.py` in the folder containing the file. It has no dependencies beyond the Python standard library and performs complete \(\mathbb F_2\) and \(\mathbb F_4\) monic-octic enumerations plus a deterministic \(\mathbb F_8\) sample. The exact output is in `verify_output.txt`. These finite calculations do not establish the infinite-field theorem; the proof uses Cartier identities, semilinear rank algebra, and geometry of an explicit projective embedding.

The general p-rank classification has not undergone independent external mathematical audit. Its historical novelty is provisional, especially relative to potentially unindexed cyclic-cover literature.
