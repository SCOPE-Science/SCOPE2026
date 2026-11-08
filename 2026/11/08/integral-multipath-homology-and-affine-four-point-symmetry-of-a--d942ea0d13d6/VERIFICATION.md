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
# Verification of the cyclic doubled-triangle multipath complex

Execute `python3 verify.py` with Python 3 standard library; no external datasets or libraries are needed. The verifier enumerates each of 4096 possible subsets, independently tests path-forest admissibility twice, verifies the complete face vector and 278 nonempty faces, reconstructs every signed integer chain differential, and verifies the chain condition in all degrees. Two complete integral cancellation orders use only ±1 pivots and check that all remaining integer boundary matrices are zero. This is an integral homology proof, rather than a field-only experiment. An embedded octahedral sphere represents the generator of the natural degree-only matching-join complex.

The same executable checks all 24 automorphisms and their signed cellular actions. It evaluates traces on simplicial chains and boundary images using exact finite-field arithmetic modulo 1009. Since the integral cancellation proves the ranks and rational homology dimensions at most four, the calculated modular traces uniquely identify their integer values, yielding the full rational character. The accompanying `verify_output.txt` records a successful execution of the included verifier, but the actual calculations in `verify.py` are the evidence to replay.

Scientific limits: no full homotopy equivalence, general-family formula, equivariant integral lattice classification or external independent audit is asserted. No mathematical claim is based on failure of a database search.
