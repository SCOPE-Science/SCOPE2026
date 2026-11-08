---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The unrestricted result follows directly from uniform root splitting and the exact mean recurrence f_k(m): f=0 for m<k, f=1 at m=k, and f=2(m+1)/((k+1)(k+2)) for m>k. Subtracting the linear continuation yields a finite defect d_k whose mass is zero, first moment k/3 and second moment k(3k-1)/6. Conditioning on I and using symmetry for Q=(2I-n+1)^2 gives Cov(Q,X)=8/n [k(3k-1)/6-(n-1)k/3]=4k(3k+1-2n)/(3n). No assumption of disjoint boundary layers is used. For n=2, Q is constant and covariance vanishes; k=n has deterministic X=1 and lies outside the formula. The sign follows exactly from 3k+1-2n; summing over k gives zero total covariance and known weighted path-length covariance (n-2)(n-1)(n+1)/9. Independent exact-fraction calculations checked all k for n=2..60, defect moments k=1..100, and independent direct BST insertion-permutation enumeration for n=2..7; the analytical proof, not those finite checks, establishes all n.

## originality

FAIL

A decisive prior-implication check fails originality: Dennert and Grübel (2010), equations (2.1) and (3.3), already give the complete conditional mean of each fringe-size count for EVERY root left-subtree size. Because the root imbalance Q=(2I-(n-1))^2 is a deterministic function of that same I, their theorem directly determines Cov(g(I),X_{n,k}) for EVERY root-only g by a one-line tower expectation. Taking g=Q and evaluating elementary finite polynomial sums gives precisely 4k(3k+1-2n)/(3n) and its 2/3 sign boundary. The sign-resolved expression is not printed in the primary paper, but the stronger all-split conditional profile already covers this special mixed moment mathematically. The algebra and boundary moments are sound but do not introduce an independent mathematical mechanism; an unmatched equation string is not novelty. The published Resultary scalar path-length covariance alone does NOT imply all individual k terms, and is not the decisive coverage source.

## value

PASS

For the classical random-BST fringe-size profile, size-by-size covariance with first-pivot balance is a natural, interpretable all-n classification: it determines which small and large fringe strata oppose or reinforce squared root imbalance and pinpoints the sharp 2/3 sign switch including finite boundary cases. Its two moment conservation identities illuminate the already-known path-length aggregate and its cancellation, so the precise signed vector could be useful as an explanatory benchmark. This passes the motivation/value test independently of correctness and novelty, although originality fails because the evaluated formula is already a short implication of the 2010 complete conditional profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
