---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For a uniform random endofunction [n]→[n], rooted-forest counting gives P(C_n=m)=m(n)_m/n^{m+1}. Conditional on m cyclic vertices, their permutation is uniform, so F_n has rencontres Q_m. Unconditionally the n fixed-point indicators are independent Bernoulli(1/n), hence F_n~Bin(n,1/n), E(F_n|C_n)=1 and Cov(F_n,C_n)=0; m=1 shows dependence and I>0 for all n≥2. Exact entropy identity I=Σ_m w_{n,m}D(Q_m||Pois(1))−D(Bin(n,1/n)||Pois(1)) is a KL chain rule. Alternating-series derangement remainder gives D(Q_m||Pois1)≤(e2^{m+1}+1)/(m+1)!, allowing dominated convergence n w→m. A likelihood expansion with factorial-moment tail bounds makes Bin-Pois KL O(n⁻²). Therefore n I→Σ_{m≥1}mD(Q_m||Pois1)=3.692926238979770132438700...; independent high-precision 35-term summation and rigorous 30-tail bound <1.5×10⁻24 reproduced the number. Finite enumeration of maps through 6 in source script is not an infinite argument.

## originality

PASS

Best-of-knowledge PASS for the precise new component only; earlier mathematically overlapping statements are credited in the four comparisons. Full source limitations and residual risks recorded, no failed search treated as proof.

## value

PASS

Shows that two natural functional-graph counts remain information-theoretically dependent at a quantified sharp rate even though their covariance vanishes exactly for every n. The information originates in rare small cyclic cores and differs qualitatively from typical √n-size core behavior. Its KL coefficient is an independently useful exact information invariant, not a restatement of the previously known total-variation dependence coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
