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

# Mathematical verification and reproducibility

The proof requires no generated finite certificate. To check the claim, fix integers \(k\ge2\), \(r\ge k\), \(m\ge1\); take a rank-\(r\) complex bundle \(E\to S^{2k}\) and form \(F=E^{\oplus m}\), rank \(R=rm\).

1. Check the cited general equivalence between the number of spectral components and the maximum number of nonzero orthogonal idempotents in arXiv:2611.12208v1, Proposition 3.1. Under the endomorphism-section identification, projections have continuous positive-rank ranges and yield bundle decompositions.
2. Check \(c_k(F)=m c_k(E)\) from the Whitney-sum formula: every positive cohomology group \(H^{2j}(S^{2k};\mathbb Z)\) vanishes for \(0<j<k\). This also rules out decomposing \(F\) entirely into rank-less-than-\(k\) bundles when \(c_k(E)\ne0\).
3. Check the unitary-group fibration \(U(s)\to U(s+1)\to S^{2s+1}\), whose long exact sequence gives \(\pi_{2k-1}(U(k))\cong\pi_{2k-1}(U(R))\) for \(R\ge k\). Block inclusion realizes the given clutching map with one rank-\(k\) block and \(R-k\) trivial lines.
4. Check the classical Bott top-Chern integrality factor \((k-1)!\), which ensures \(c_k(E)=0\) implies triviality for rank \(r\ge k\). Once a maximal decomposition exists, the identity \(\sum_j(r_j-1)=k-1\) forces precisely one rank-\(k\) block; for \(k\ge2\), all line bundles over \(S^{2k}\) are trivial.

Simple arithmetic examples: \((k,r,m)=(2,2,1)\) gives depth \(1\) when \(c_2(E)\ne0\), and \((2,2,3)\) gives \(5\); \((3,3,2)\) gives \(4\) when \(c_3(E)\ne0\). In each case the trivial-bundle depth is \(rm\). These checks merely illustrate the proved formula and do not replace the topology-based proof.

Limits: No claim for nonstable rank \(r<k\), for arbitrary compact bases, or for odd spheres. Published topological inputs are used as theorems rather than independently certified here. No independent mathematical audit has been performed.
