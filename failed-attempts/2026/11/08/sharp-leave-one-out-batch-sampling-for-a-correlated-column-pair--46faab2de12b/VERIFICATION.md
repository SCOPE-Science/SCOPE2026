---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For H=A^T A=[[1,rho],[rho,1]] direct_sum I, each omission residual is rank-one projection onto w_1=sigma e_1-rho e_2, w_2=e_2, w_j=e_j. The two-dimensional expected-operator eigenvalues lead to the unique balancing law p1=p2=1/D*, pj=(1+rho)/D*, D*=2+(n-2)(1+rho), with Gamma*=(1+rho)/D*. Gram determinants yield volume law Dvol=2+(n-2)(1-rho^2) and Gamma_vol=(1+rho)/Dvol>Gamma*. Fixed starting residual w1 closes a symmetric two-line Markov chain, giving exact all-k means ((1+rho^2)/D*)^k and ((1+rho^2)/Dvol)^k. Symbolic n=4,rho=3/5 exact eigenspectra agree. Mathematical correctness does not establish originality.

## originality

FAIL

Decisive published stronger coverage: the 2026-11-08 general all-but-one-coordinate SPD minimax theorem derives the unique optimizing distribution q_i proportional to (Gtilde^(-1) 1)_i for any signable normalized inverse-Hessian Gram. For this source H=A^T A, Gtilde=[[1,rho],[rho,1]] direct_sum I; its formula specializes exactly to p1=p2=1/D*, pj=(1+rho)/D*. The published 2026-10-12 general maximal-block volume sampler theorem gives the exact all-step mean-square Markov operator; this direct-sum two-line specialization yields the submitted fixed-start rates. Thus the submitted claimed main optimizer and all-step volume dynamics are implications of stronger existing results, not independent new mathematics. Same-day ordering of the November 8 optimizer result is uncertain but mathematical coverage is decisive.

## value

FAIL

The optimized probabilities and comparison are a direct small block-diagonal specialization of an already published broad unique-minimax theorem, while the exact volume-sampled finite-step witness follows from a separately published full matrix dynamics formula. The present example illustrates known general laws but does not identify a mathematically motivated unknown invariant beyond them; correct reproducibility and explicit numbers are insufficient value for independent research acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
