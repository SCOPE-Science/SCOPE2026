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

The proof uses two independent geometric inputs: Bézout inequalities exclude every negative irreducible curve beyond the listed exceptional divisors, one strict-transformed common line, and the lines connecting the off-line point to the collinear points; then a Schur complement classifies all negative-definite supports. The chamber correspondence is Bauer–Funke–Neumann, Proposition 1.1.

Replay with `python3 verification/check.py` (Python standard library only). The verifier constructs exact integral intersection matrices and, for \(n=3,4,5\), enumerates every one of the \(2^{2n+2}\) subsets using rationally exact Bareiss determinants and Sylvester's criterion. A separate combinatorial test and the formula agree on every subset. The checks through \(n=10\) for the closed formula are symbolic/binomial coefficient checks, not exhaustive support checks. See `verification/output.txt` for actual output. These finite checks are not the proof for unrestricted \(n\).

No independent validation, machine-checked infinite proof, or exhaustive literature-priority determination is claimed. The included source comparisons assess only specified material and recorded searches.
