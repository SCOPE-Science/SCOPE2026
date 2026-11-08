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

## Reproduction

Use `python3 verify.py` from the directory containing the extracted research documents. The checker imports only Python standard-library modules and tests normalized mixed areas by separately forming integer convex hulls of \(P\), \(Q\), and all pairwise vertex sums for \(P+Q\). The exact integer shoelace formula avoids floating-point errors.

## Actual checks

The verifier was run on the exact file included with these documents and returned `PASS: 22198 integer-arithmetic checks. Universal statements require the accompanying proof.` The verified constructions include the arbitrary coprime-width low-area realizations, semigroup realizations, the universal mixed-area-seven family, the mixed-area-four constructions for \(d=1,2,3,4\), and the determinant witnesses and mixed-area-two construction for \(d=1,2\). Randomized finite pairs were drawn with a documented fixed seed.

## Limits

Finite checks are not an exhaustive search over lattice polytopes, do not establish impossibility of missing values, and cannot establish infinite claims. The signed determinant divisibility argument, forced segment structure, and constructive range proof in `RESULT.md` supply the universal justification. Historical originality is not independently certified.
