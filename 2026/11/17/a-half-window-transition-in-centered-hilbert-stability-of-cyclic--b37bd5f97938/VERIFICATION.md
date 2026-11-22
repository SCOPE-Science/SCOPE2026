---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For n≥2 and 1≤w≤n, H_n(x) is the unweighted mean-centered Euclidean seminorm and M_{n,w} is cyclic contiguous forward-window max. On a strict-selector chamber, the map copies input coordinates with multiplicities c_j≤w and its unique global maximum has c_p=w. For 2w≤n, output-centered energy ≤Σ c_j(h_j−mean h)^2≤wH_n(h)^2. For 2w>n, writing R=max h−min h and using convexity of centered copying energy on the coordinate box reduces the worst case to binary endpoints; since one multiplicity is w>n/2, binary copied count t lies in [0,n−w]∪[w,n], hence output H²≤w(n−w)R²/n. Input H²≥R²/2 by the two extreme coordinates. Thus L²≤2w(n−w)/n. A two-site peak baseline p=0,q=w for short windows and q=n−w for long windows has disjoint winning patterns; perturb ε(e_p−e_q) to attain equality in both branches. For w=n output is constant and L=0, for w=1 identity L=1. Continuity over finitely many affine chamber transitions upgrades a branch bound to arbitrary pairs, even with ties. Independent exact two-peak calculations at n=5,7,9,12 corroborate squared factors and equality; not proof for all n.

## originality

PASS

Same operator was studied in published Gini pairwise-variation and truncated-path weighted total-variation theorems. These use mathematically different seminorms and produce different coefficients, so neither exact result dominates the centered Hilbert theorem. The 2013 graph morphology paper is plausible background but accessible abstract concerns lattice adjunctions and image filtering, not a verified equivalent sharp coefficient; authorized full access was unavailable and is a disclosed risk.

## value

PASS

Quantifies genuine two-input instability of the canonical cyclic maximum filter in Euclidean mean-zero geometry with an attained change of behavior exactly at half-window. The sharp coefficient matters for noise/perturbation propagation under nonlinear filters and differs from already studied total-variation and Gini measures; this is a motivated exact nontrivial norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
