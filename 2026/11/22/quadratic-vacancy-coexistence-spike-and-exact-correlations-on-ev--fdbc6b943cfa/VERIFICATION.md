---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Under the specified coordinate-plus-antipode convention the adjacency eigenvalue at Walsh weight k is n−2k+(−1)^k; for even n its minimum 1−n occurs exactly at n,n−1. The energy bound is (D−D*)K with D*=(n−1)J/2, with equality exactly on this eigenspace, including zero. Full and empty states attain the lower envelope on the two strict sides. Independently, after parity untwisting, a ternary minimizer at D* is an affine function b+Σd_i x_i on the Boolean cube, with b integer and every d_i an integer from a single-coordinate difference. Its range width is Σ|d_i|≤2. Width 0 gives the three constants; one nonzero increment of size 1 gives four half-occupied states per coordinate (two signs and two allowed baselines), one of size 2 gives two full states per coordinate, and two size-1 increments give four half states per pair. This proves that there are no other sectors and yields the displayed counts and ground energy for all even n≥4. In the original character basis the full states are signed single modes, the half states are signed half-sums of distinct modes. Summing over the signs eliminates mixed terms and gives coefficient 2+n for each diagonal character product. The diagonal character sum is (−1)^r(n+1−2r), giving the stated uniform threshold correlation after division by 1+2(n+1)^2. Independent exact enumeration of the bounded increment vectors at n=4,6 gives (empty, half, full)=(1,40,10),(1,84,14), and sums of spin products [30,−18,6,6,−18] and [56,−40,24,−8,−8,24,−40] over the respective state sets, matching the formula at all r. Replay: node /workspace/branches/independent_finite_checks.js (record 2 block).

## originality

PASS

The spectrum, spectral bound and same-graph binary rigidity are established premises. The inspected distinct prior claims do not classify the ternary intersection of the minimum eigenspace or give the folded-cube vacancy coexistence ensemble. The spin-one threshold location is a direct spectral consequence and is not independently credited as new; the supported distinct contribution is the exact ternary classification, labeled count and critical spin-product law for this family.

## value

PASS

The exact coexistence ensemble tests what ternary vacancies change in a frustrated, symmetric graph whose binary sector is already understood. An energy envelope alone would miss both the isolated half-density sector of quadratic cardinality and its effect on spin observables. This is a natural zero-temperature finite-cluster benchmark over an unbounded even-dimensional family, with a concrete Clebsch-graph check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
