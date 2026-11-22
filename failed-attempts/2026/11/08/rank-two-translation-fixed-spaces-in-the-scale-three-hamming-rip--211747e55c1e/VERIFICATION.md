---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For an H action on a finite simplex complex, a geometric fixed barycentric point has equal coordinates on each complete orbit, and the orbit-barycenter complex is PL equivalent to the fixed locus. Translation orbits are W cosets, admissible exactly when d(W)<=r; for Rips flagness, pairwise cross-coset diameters determine all simplices. A rank-two binary generator matrix has three nonzero column types of multiplicities a,b,c, so nonzero weights are a+c,b+c,a+b. Requiring each <=3 forces active support <=4 and exactly the four weight patterns {1,1,2}, {1,2,3}, {2,2,2}, {2,3,3}. For support 2, coset graph Q_(n-2); support 3 even parity and mixed type, the allowed generator vectors form a basis of quotient F_2^(n-2), again Q_(n-2); support 4, compatible quotient edges on four cosets form C4 with no edges across unused-coordinate tails. All are triangle-free so the orbit complex is precisely the graph. For scale 2, exactly support-two and even-parity support-three types give 2^(n-2) isolated coset vertices; all others empty, including r<2. Counting plane supports gives C(n,2)+4C(n,3) cube cases, 6C(n,4) circle unions and C(n,2)+C(n,3) at scale 2. Q_0 is one point, and the case s=4 occurs only for n>=4; cube-graph Euler characteristic yields the stated integral loop count. Independent Python directly enumerates all 3516 rank-two subgroups across n=2..7, computes coset graph edges by Hamming cross-diameter and checks components, degrees, graph distances, binomial distributions and absence of triangles without calling the source verifier. Exact Git object reconstruction from eight independently fetched blob SHAs matched the assigned tree. Finite tests corroborate the unrestricted orbit/code proof and do not substitute for it.

## originality

FAIL

A publicly published 2026-10-25 RESULT.md proves a PL classification of geometric fixed loci of EVERY binary translation subgroup of rank >=2 at inclusive Hamming scale three, and its rank-two specialization is identical to the submitted scale-three three-way classification, down to the four nonzero weight multisets and cube graph versus 2^(n-4) four-cycle components. The 2026-10-18 published scale-0-to-2 classification independently includes the rank-two discrete set, exact count C(n,2)+C(n,3), and no fixed points below scale two. The submitted scale-three subgroup totals C(n,2)+4C(n,3) and 6C(n,4) follow by immediate support enumeration of the four already classified rank-two codeword patterns; the zero-skeleton inclusion likewise follows from keeping coset vertices as edges enter. This is substantive prior implication, not an unsuccessful search or similarity of names.

## value

FAIL

As a stand-alone theorem, a full natural fixed-space classification could be significant. However, the scale-three trichotomy and integral circle/cube models are already in the older stronger higher-rank theorem; the lower-scale discrete classification and its exact subgroup count are separately published. The submitted additional binomial totals are elementary counting over the exact four code types in the prior theorem, and the stated filtration inclusion retains the same coset vertices and adds edges. No previously unknown natural invariant, new structural lemma, sharp boundary, meaningful residual classification or independent mathematical question remains. This is a scientific-value judgment about the duplicate submitted result, not a claim that fixed-point topology is unimportant or that short exact results are inherently valueless.

The dated certificate retains the supplied scientific assessment, sources and limitations.
