---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Over F_{3^f}, deleting a vertex from cocktail-party C_{r+1} leaves 2r+1 vertices with r disjoint missing edges. Pair-antisymmetric modes have zero adjacency eigenvalue, symmetric pair vectors x_i and unmatched z have quotient (z,S) map Q_r=[[0,−1],[r,1−r]], with r−1-dimensional eigenvalue-one kernel U. For r mod3=1,2 the quadratic quotient polynomials are irreducible and transform through temporal z+z^{-1} into separable Φ8 or Φ5; for r mod3=0, the 1-primary sector instead has one spatial Jordan block length 2 and r−2 single blocks, while zero-primary is r+1 single blocks. The temporal companion T(u,v)=(Au−v,u) has λ=0 order-four modes; λ=1 gives J2(−1) and J4(−1), whose t-fixed nullity is min(blocksize,3^{ν3(t)}) for even t. Summing yields exact E_r(t) in the source for all t, with sharp global orders 36,24,60 by residue, intact graph 12,12,36, all period counts by Möbius inversion and maximal-order densities by independence of summands. I independently reconstructed adjacency/time matrices over F3 for r=2..6, verified every t≤120 fixed nullity and sharp orders. The unbounded r and extension-field formulas come from the invariant factor proof, not the tested range.

## originality

PASS

Comparisons made against specific mathematical statements, with natural aliases, stronger/other model hypotheses and integral versus finite-field distinctions; same-finding indexed hit not counted as independent earlier coverage.  Restricted bibliographic coverage remains as residual risk.

## value

PASS

Vertex deletion of a canonical strongly regular cocktail-party graph causes a genuine modular spectral phase change: the allowed temporal orders create new fifth/eighth-root motion, with a complete all-size period population law. This is an exact natural classification, not a trivial finite experiment or restatement of reversibility; it captures the structural effect of a small graph perturbation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
