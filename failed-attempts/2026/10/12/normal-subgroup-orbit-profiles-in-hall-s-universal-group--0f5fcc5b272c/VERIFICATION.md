---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Hall local finiteness makes every marked finite-tuple subgroup finite. Evaluation F_V(n)-><g_i> has a finite-index normal kernel, and equal kernels are equivalent to an isomorphism of the marked finite subgroups. Rzepecki/Hall inner ultrahomogeneity realizes it by conjugation, while all group automorphisms preserve words. Every finite quotient embeds by Hall universality. Abelian exponent-m relatively free group is (Z/m)^n; prime-power subgroup count is exactly Birkhoff rectangular formula. A Gaussian coefficient has size p^{k(N-k)} up to fixed p constant, with subgroup-type exponent sum r_i(n-r_i), giving the claimed O(log n) remainder.

## originality

FAIL

Decisive prior implication: Hall/Rzepecki inner ultrahomogeneity makes finite marked-subgroup isomorphisms inner-conjugate, which is exactly equality of relatively free word kernels; existing Birkhoff formula and Gaussian estimates then supply the rest.

## value

FAIL

The exact finite-tuple orbit profiles are natural and correctly interpretable, but for this particular group they consist of a routine relabeling of the already-known marked finite quotient/quantifier-free type orbit classification followed by insertion of Birkhoff classical subgroup counts. The asserted sharp growth is the routine Gaussian-binomial degree estimate. No independently motivated unknown invariant or nonmechanical mathematical gap beyond these direct consequences remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
