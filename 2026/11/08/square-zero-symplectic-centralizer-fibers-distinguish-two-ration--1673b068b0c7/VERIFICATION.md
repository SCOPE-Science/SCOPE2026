---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For odd q and nonsingular symmetric S(4×4), direct sp8 block multiplication reduces X²=[X,N_S]=0 to C=0, AS+SA^T=0, A²=0, AB=BA^T with symmetric B. When A=0, symmetric B rank-r strata give the four-degree rank polynomial and q^10 total. For A≠0, skew-adjointness makes rank(A) even and A²=0 makes rank≤2; its image is a maximal totally isotropic plane. Nonsplit quadratic four-spaces admit none; split ones have 2(q+1) such planes with q−1 nonzero A each. In a Witt-adapted basis AB=BA^T gives six linear degrees of freedom in symmetric B, and the resulting X always has rank four. Hence split adds 2(q²−1)q⁶ z⁴, nonsplit adds zero, for every odd prime power. Independent exhaustive F3 skew-A enumeration found 16 split/0 nonsplit, with compatible B kernel dimension 6. Finite tests corroborate, not replace, the Witt/linear algebra proof.

## originality

PASS

General finite-field commuting nilpotent-pair enumerations and orthogonal square-zero tuple classification supply important components, particularly the split 4-form count 2(q²−1), but neither determines these fixed-rational-orbit square-zero sp8 centralizer fibers with their rank-four-only discrepancy and free compatible symmetric B blocks. The exact rank polynomial remains best-of-knowledge original.

## value

PASS

Rational nilpotent orbits sharing a geometric Jordan partition have different centralizer square-zero rank spectra; this is a meaningful sharp arithmetic-orbit invariant and a complete natural fixed-rank fiber census. It makes the split/nonsplit distinction observable only at the top rank, a structural exact fact rather than an arbitrary finite number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
