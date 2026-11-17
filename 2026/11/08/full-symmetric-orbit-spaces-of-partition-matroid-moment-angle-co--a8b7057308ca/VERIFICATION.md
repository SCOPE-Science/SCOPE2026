---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

For K=join_i D_{p_i}, its minimal-nonface graph is a disjoint union of complete components corresponding to block sizes >=2 plus singleton isolates; therefore Aut(K)=S_{m1}×∏_{p>=2}(S_p wr S_{m_p}). Polyhedral products turn joins into Cartesian products equivariantly, so after block-permutation quotients the literal orbit is a product of SP^{m_p}(Y_p). For p>=2, Y_p=Z_{D_p}/S_p is the strict pushout A=SP^p(S1), B=D²×SP^{p-1}(S1), C=S1×SP^{p-1}(S1), where boundary map sends (w,M) to {w}∪M. Compact-to-Hausdorff verifies the repeated-boundary-coordinate quotient. SP^q(S1)→S1 by multiplying coordinates is a homotopy equivalence: unordered roots identify SP^q(C×) with C^{q-1}×C×, and SP^q(S1)→SP^q(C×) is a homotopy equivalence. The attaching H1 matrix [[1,1],[0,-1]] is unimodular, giving π1(Y_p)=0 and reduced integral H3(Y_p)=Z with all other reduced groups zero; simply connected homology-Whitehead gives Y_p≃S³. Taking symmetric powers preserves homotopy equivalence via coordinatewise homotopies; p=1 factors are contractible. For odd-degree generators the S_{m_p} exterior invariants are Q in degree0 and one Q in degree3, and no higher wedges, yielding the exterior ring on distinct p>=2 sizes. Read actual verify.py finite block automorphisms and determinant checks; independently checked matrix determinant -1 and example K=D2 (two solid-torus gluing, S³). No extrapolation from finite experiments is used in the uniform proof.

## originality

PASS

Best-of-knowledge after Resultary and primary-literature comparison, the combination of exact wreath-product Aut(K), literal full vertex-permutation orbit space and integral homotopy product of SP^{m_p}(S³) is not implied by the inspected prior results. Morton supplies the homotopy ingredient SP^q(S1)→S1, not the moment-angle orbit-space classification. Bahri–Bendersky–Cohen–Gitler treat symmetric products of polyhedral products in a different functorial role, while Yu and Limonchenko–Solomadin study quotients by torus subgroups, not full permutation automorphism groups. No closely matched covering theorem was found; lack of universal literature access remains a documented priority risk.

## value

PASS

The full automorphism orbit space of a partition-matroid moment-angle complex is a canonical finite-symmetry quotient, and all finite block profiles are classified by a concrete integral homotopy type rather than one small example. It exposes a non-obvious uniform S³ building block and retains finite symmetric-power homotopy information lost from rational Betti numbers; researchers studying permutation quotients, toric topology, and integral torsion can use the precise product. The new classification is mathematically motivated independently of code reproducibility or speculative downstream conjectures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
