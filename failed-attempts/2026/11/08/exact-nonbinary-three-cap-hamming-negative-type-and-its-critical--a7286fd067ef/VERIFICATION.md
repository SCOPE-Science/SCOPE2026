---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The weight-1 and weight-2 sums of a character of weight j are T_j=(q−1)n−qj and U_j=(T_j²−(q−2)T_j−n(q−1))/2; the remaining nonzero shells sum to −1−T_j−U_j. This remains valid for composite q. The strictly concave multiplier as a function of T_j is maximized at the lattice point nearest (q−2)/2−R(p); the strict inequalities 2<R(p)<3 for 0<p<1 yield the stated unique floor index. At p=0 all nonconstant eigenvalues are −1, and at p=1 a four-coordinate subspace has a weight-3 eigenvalue q−1>0. Strict downward propagation of finite negative type then gives existence, uniqueness and the full threshold range; centering and taking the rank of the Gram matrix proves the embedding claims. The two limits follow by testing p=c/n with fixed q and p=c/q with fixed n, using bounded t in the first case and t=q−n, u=−(n−1)q+n(n−1)/2 in the second. Independent replay: OPENBLAS_NUM_THREADS=1 python3 -B /workspace/branches/independent_checks.py 4; it checks 16 real tensor-layer comparisons and four full powered-distance nullities, not the general theorem.

## originality

FAIL

Distinct same-day Resultary record 620a1519c809 states the identical nonbinary cap-three critical layer, exact root, strictness, endpoint nullity, embedding dimension and exponential-kernel criterion; it also gives a stronger fixed-q expansion. This is equivalent coverage, not a claim about which same-day record came first. The only material-looking difference, the fixed-n large-q leading constant, follows by direct first-order Taylor expansion of the exact root already given there.

## value

FAIL

A full critical-layer theorem for this natural metric is worthwhile, but that theorem and the fixed-q asymptotic are already available in the exact matched record. The fixed-n coefficient is read off by one Taylor expansion of its exact scalar equation and does not constitute a separately substantive claim. No repair is justified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
