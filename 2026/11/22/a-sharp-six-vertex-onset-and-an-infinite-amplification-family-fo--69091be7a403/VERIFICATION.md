---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The claimed object is location-specific neutral fixation on a simple unweighted tree with δ the dB probability. Ordered copying u→v has probability ((1−δ)/d_u+δ/d_v)/N. On a tree, propagating w_v/w_u=q_(v→u)/q_(u→v) balances each edge, and the weighted mutant count has zero conditional drift; a finite positive-probability route to consensus and bounded convergence give fixation w_v/sum(w) including δ=0,1. Through order five only the five-vertex fork is not bidegreed: maximum degree ≤2 is a path, degree N−1 a star, and the five-vertex degree-3 nonstar has pendant branch lengths 1,1,2. The bidegreed theorem applies to all other trees; a singleton, if adjoined by the absorbing convention beyond the update rule's N≥2 domain, is trivial. I independently multiplied the fork weights in t=δ/(1−δ); their common denominator has coefficients (23,101,128,48) in ascending powers, and the derivative numerators agree with the four listed strict-sign certificates. For D_{1,3} the same polynomial method gives the reported rational function and a single strict maximum; the cubic is decreasing (its derivative is convex with negative endpoint values) and bisection gives 0.0336810499232197 and fixation 0.2110651074585313. The boundary derivatives and pure-rule limits follow by differentiating and evaluating the exact weight formula. At δ=m^−1/2, the small hub weight tends to 1/2 and the large-hub edge ratio divided by the large-leaf edge ratio tends to 1, so the normalizer divided by m tends to 1/2, proving the third asymptotic. The positive derivative at 0 and negative derivative at 1 give interior improvement over both endpoints. Replay paths for the frozen algebraic certificate: `verify.py`, lines 49–91, and the exact weight formula in RESULT.md Proof 2–4; the frozen script was inspected, not executed. This is not a threshold over all graphs or a global optimal-factor theorem.

## originality

PASS

Generic neutral nonmonotonicity, the neutral balance formulation, and bidegreed monotonicity are prior. The supported distinct contribution is the all-tree sharp order-six onset, exact small-side-leaf witness, and infinite one-sided double-star family with an achievable asymptotic factor of two. The strongest primary examples are cyclic, and the bidegreed theorem leaves precisely the small obstruction and witness outside its domain.

## value

PASS

The theorem answers a natural structural restriction of an existing mixed-updating question. It identifies the first acyclic obstruction and shows why its small six-vertex improvement is not the substantive limit: the same geometry at larger order admits a factor approaching two over the better pure rule. The exact lower-order monotonicity certificate and infinite-family scaling are independently useful, with no claim to an optimal universal factor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
