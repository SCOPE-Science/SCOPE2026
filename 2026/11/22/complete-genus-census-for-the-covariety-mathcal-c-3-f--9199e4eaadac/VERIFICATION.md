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

The condition 3 in PF forces positive membership to be closed under translation by 3, leaving a unique threshold in each class. If 2 belongs, closure and 2+3=5 force Frobenius 3; 1 is also excluded. Testing the three minimal sums between nonzero residue classes gives exactly b<=2a, a<=2b+1, c<=a+b+1, with all sums involving the positive zero-residue tail automatic. The last gaps have three distinct residues, and their omissions total a+b+c-1. Fixing the largest gap gives the stated three domains; the fixed a+b slice gives exactly the two endpoints in the coefficient law. For F=3k the two violations are disjoint; with h=floor(N/2), d=floor(N/3), each violation count is d(d+3)/2+(h-d)(N-h-d), for N=k-1 and N=k-2 respectively. Subtraction from k^2-(k-1)(k-2)/2 and evaluation by k mod 6 proves the ceiling count, including k=2. The other two counts are direct interval products. This proves the stated period bound and the two leading constants. An independently written bitmask check (`python3 /tmp/opencode/frozen_checks.py genus` in the review environment) enumerated all subsets below F=4..18, compared the full genus histograms to the displayed formulas and agreed. The check corroborates, not substitutes for, the unbounded proof. Frozen verify.py and its recorded evidence were inspected, not executed.

## originality

PASS

Prior work already contains the exact family as a specialization and computes every fixed-genus stratum algorithmically. The distinct contribution supported here is the uniform explicit classification and evaluated count by genus across all F>=4. No inspected theorem or matching census establishes the same evaluated formulas.

## value

PASS

Genus strata are a natural invariant of this prescribed-gap family and an explicit target of prior algorithms. The census replaces a separate enumeration at each F and genus with direct coefficient access, across all multiplicities, and exhibits genuinely different leading densities in different Frobenius residue classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
