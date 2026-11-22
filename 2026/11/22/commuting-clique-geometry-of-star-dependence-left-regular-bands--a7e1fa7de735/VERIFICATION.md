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

# Verification evidence

The exact algebraic claims are proved in `RESULT.md`, Steps 1–5. Run `python3 check_star_band.py` using the Python standard library; the script independently builds the finite band multiplication using concatenation and first-occurrence reduction, then compares all pairwise commuting results against the theorem. It tests centralizers and the family of maximal commutative submonoids for every integer \(1\le m\le6\); a separate maximal-clique enumeration covers \(1\le m\le4\), and direct polynomial coefficient enumeration covers \(1\le m\le3\). The recorded output is `check_star_band_output.txt`.

The finite checks are neither an exhaustive all-parameter proof nor an independent audit. The normal-form and counting argument, rather than computational extrapolation, establishes the formula for every integer \(m\ge1\). All statements assume the left-regular-band relations, including arbitrary-word absorption, which distinguish the finite monoid from ordinary generator-idempotent graph products.
