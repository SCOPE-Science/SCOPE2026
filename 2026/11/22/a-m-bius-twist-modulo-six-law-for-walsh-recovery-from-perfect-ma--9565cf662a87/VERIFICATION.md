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

# Exact checks and reproducibility

Run `python mobius_walsh_verifier.py` with a standard Python 3 interpreter. The script independently constructs the \(3n\)-edge graph, enumerates every perfect matching by vertex-first backtracking, projects its sign exponent onto the normalized seam/chord coordinates, applies an exact integer Walsh–Hadamard transform, and checks every coefficient against the proposed two-by-two signed transfer for each \(3\le n\le12\). It prints `MOBIUS_WALSH_EXACT_TESTS_PASS 16664` upon success.

The reduced signed spectra have exactly 36 zero characters at \(n=6\) and 1,392 at \(n=12\), with none for the other tested orders. The least nonzero magnitudes follow the alleged residue classes. Further tests multiply the eight six-site blocks and test witnesses through order 206. These are independent finite diagnostics, not proof of the general theorem. The written modulo-four determinant argument and six-step identity give the all-order proof.

The global class-size factor \(2^{2n-1}\) follows from vertex gauge switching on the connected underlying graph. No unreproduced external certificate, independent audit or expert validation is asserted.
