---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

With closed-neighborhood tie retention, a chosen spin flips when same-neighbor count ≥ opposite-neighbor count; cut increment is s−o≥0. For state with i clique ones and j independent-set ones, Q(i,j)=i(N−i)+j(a−2i); permitted flips can first align peripherals opposite the prevailing core bit, then move core occupancy toward the maximum of i(N−i). Thus every state has a positive-probability finite path to some maximum cut and a finite chain almost surely enters the maximum-cut region. Within the maximum, all allowed flips are neutral and instantly reversible, so recurrent SCCs are exactly components of the maximum-cut flip graph. Analytic maximizing populations give 2 singleton polarized classes if b≥a; 2 C(a,(a−b)/2) absorbing if b<a,N even; 2 rank-incidence classes each C(a+1,(a−b+1)/2) when b<a,N odd,b≥2; and one middle-rank class of 2 C(a+1,a/2) if b=1 and a even. The class Laplacian is the bipartite adjacent rank incidence Laplacian, with singular squares (k+1−r)(d−k−r) and eigenvalues r,d+1−r, yielding smallest positive 1 and spectral gap 1/N after single-vertex selection. Independent explicit graph-SCC and numerical spectrum tests across small parameters agree. The gap is class-restricted, not global across separated classes.

## originality

PASS

Stochastic minority updates and cut monotonicity are known from Rouquier–Regnault–Thierry. Their full-text clique and bipartite cases do not give the all-size complete-split recurrent-class counts or spectral gap. Standard Boolean-lattice up/down spectra are prior inputs but do not imply which configurations form the recurrent classes. Published synchronous majority/other graph-type Resultary findings have different update rules. Exact universal class gap and parity attractor classification remain distinct.

## value

PASS

The theorem determines the complete finite-state recurrent decomposition and a universal exact spectral relaxation gap for a natural highly structured family where tied updates can preserve nontrivial fluctuations. Identifying all maximizing cuts as the complete recurrent set is not automatic from the potential function, and proving the same 1/N gap for very different class sizes is a substantial structural Markov-chain invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
