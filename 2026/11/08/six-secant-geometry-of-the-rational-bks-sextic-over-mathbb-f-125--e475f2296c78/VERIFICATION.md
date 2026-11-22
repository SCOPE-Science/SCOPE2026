---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The final theorem is a finite assertion over K=F5^3 defined by the homogeneous polynomial Y^6-X^5 Z-X Z^5+(Y^2-2XZ)^3, with projective normalized triples covering all 15751 points/lines. A third independently implemented complete integer-field model using the irreducible v^3+2v+1 (different from both source cubics) obtains exactly 136 curve points and the rational-line weight histogram {0:5940,1:3606,2:5460,3:610,4:15,5:0,6:120}. The computed 120 full secants give s(P)={0:6571,1:3720,2:5340,6:120}; on-curve 0:16,6:120, exterior 0:6555,1:3720,2:5340. Verified sum_L w(L)=17136=136*126; sum_L binom(w,2)=9180=binom(136,2); sum_P binom(s,2)=7140=binom(120,2); the 16 uncovered on-curve points equal C(F5), and 6555 external points can each be added individually without creating a 7-point line. Every projective point and line is enumerated, so finite exhaustive arithmetic proves the precise finite result; checking the 124 nonzero multiplication rows certifies a field. Independently the established parametrization gives 126 image points, with 10 extra F5 rational nodal points on the plane curve, agreeing with 136. Source code in verify_direct.py and verify_pairlines.py was read and checked for complete loops and field reductions, but independent results do not rely on their PASS logs.

## originality

PASS

Best-of-knowledge new complete F_125 dual-line weight and six-secant concurrence histograms, including 6555 external uncovered points, are not implied by inspected primary arc-completeness results. The 2024 Korchmaros–Nagy–Szonyi Theorem 7.5 explicitly assumes extension r>=5 and says r=3,4 BKS completeness remains open; Theorem 8.2 supplies the ON-CURVE uncovered locus only. The 2022 original BKS paper identifies rational nodal geometry, not this finite incidence table. Published q=3 quartic and q=7 octic computations concern different curves/fields and do not determine the q=5 case. Independent full enumeration corroborates all asserted data. Priority is qualified by possibility of unindexed numerical work; lack of search matches is not novelty proof.

## value

PASS

The q=5,r=3 BKS sextic is the first natural small-characteristic/low-extension sextic excluded from the main published r>=5 arc completeness classification. Its 6555 off-curve holes and complete 120-six-secant line-concurrence arrangement answer a concrete motivated finite-geometry question, not an arbitrary unmotivated sample. The full line spectrum and external s(P) frequencies are non-implied by the known on-curve classification and may be used in arc extension and finite projective code invariants. No general-q theorem or orbit classification is claimed; the finite result itself is a natural complete instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
