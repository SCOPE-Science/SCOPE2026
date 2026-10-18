---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The scale-two intrinsic Čech facets are closed graph neighborhoods N[v]={v,v+e_i}, by Adams–Shukla–Singh Lemma 3.1. Their Theorem 4.1 supplies K_n≃ wedge^{β_n}S² with β_n=2^{n-2}(n²-3n+4)-1, so rational positive-degree homology occurs only in H2; the published equivalence need not be equivariant. For nonzero translation a, every invariant simplex must be union of two-element a-orbits. A weight-1 or weight-2 a yields exactly 2^{n-1} invariant edges, each orientation reversed (signed degree-one trace -1), hence Lefschetz number 2^{n-1} and H2 trace 2^{n-1}-1. Weight>=3 gives no fixed faces, L=0, H2 trace -1. Character orthogonality and Krawtchouk sums Σwt1 χ=n-2k and Σwt2 χ=((n-2k)²-n)/2 yield claimed multiplicities and β_n. Independently enumerated n=2,3,4 exact face sets, signed traces and Fourier inversion; read actual verify_cech.py script. Infinite-n claim rests on uniform combinatorial argument and published homological premise.

## originality

FAIL

A separate published full hyperoctahedral character theorem computes the rational H2 trace for EVERY element of Aut(Q_n)=F2^n⋊S_n at the SAME intrinsic Čech scale 2 and proves the translation-invariant S_n-module is Λ²Q^n. The public RESULT.md states the previous translation-only character is obtained by setting σ=id and directly provides the full character formula. This strictly stronger theorem implies each submitted translation trace, and Fourier inversion determines all m_{n,k}. No change of object, parameter, or normalization is required: the stronger result contains the same K_n, T_n, and H2 and dominates every submitted representation claim. Adams–Shukla–Singh only provided nonequivariant β but the published full-action result supplies the missing character.

## value

PASS

Exact complete translation isotypic multiplicities for a natural family of graph Čech complexes are useful rational equivariant invariants beyond Betti totals and could guide full automorphism representations. They have substantive mathematical motivation, but are covered by the already published stronger group-character theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
