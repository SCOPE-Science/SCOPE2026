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
# Reproducibility

Execute `python3 verify_mobius_cut.py` using Python 3.9 or newer with only its standard library. The exact output from a verified execution is embedded in `verification_output.txt`.

The verifier constructs the ordinary three-cut complex from disconnected triples and builds its Alexander dual independently from connected triples. For every integer \(4\le n\le13\), each one of the symbolic proof's \(6n\) elementary collapses is checked against the *current* face set for free-face status, and the remaining graph's connectivity and edge count are checked exactly. For \(4\le n\le7\), all \(2^{2n}\) vertex subsets are checked against three mutually equivalent definitions and the actual complement-of-disconnected-triple facets. For \(n=4,5,6\), independent mod-two boundary elimination of the ordinary cut complex checks the complete reduced Betti support and ranks.

The infinite-family theorem is proved by the mathematical collapse argument in `RESULT.md`; these finite runs do not establish all dimensions by extrapolation. The mod-two checks alone would not certify torsion-freeness, which instead follows from the integral simplicial collapse and Alexander duality. No independent external review or audit has been performed.
