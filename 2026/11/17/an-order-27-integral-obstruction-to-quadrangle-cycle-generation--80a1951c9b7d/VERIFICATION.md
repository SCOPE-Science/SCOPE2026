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

# Finite exact verification

The separate `verify.py` is executable using Python 3.10+ and SymPy and reconstructs all projective points directly from vectors over the prime field of order three. The complete output for the executed verification is supplied as `verification-output.txt`. An independent external audit has not been performed.

The program verifies 234 independent triples, 234 four-point frames, all oriented tetrahedral boundary cycles, a 66-column unimodular integral section, and an 168-by-234 coordinate matrix for the generated homology sublattice. The defining rank loss of three over the prime field of order three is checked by explicit modular elimination; full rank over the prime field of order two is checked separately. A specified exact integral maximal determinant is \(-27\) and exact Smith invariants are \(1^{165},3^3\). Boundary compositions are checked against all 78 oriented edges. These are complete finite algebraic checks for this named complex, not a proof of any broader projective-plane family or a claim of independent certification.

To reproduce: `python3 verify.py`. Compare stdout byte-for-byte with `verification-output.txt`.
