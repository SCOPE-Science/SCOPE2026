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

The exact uncovered-voter characterization JR(W) iff every candidate d has fewer than q=ceil(n/k) supporters outside the committee's covered voters follows by taking an uncovered cohesive group of q voters. Every DR winner must have exactly q approvals. If no ordered pair of distinct candidates (c,d) has |S_c|=q and |S_d\S_c|>=q, every k-selection from the Z quota-sized columns is JR; a union bound gives P[T != binom(Z,k)] <= m(m-1)b tau, with b=Pr(Bin(n,p)=q), tau=Pr(Bin(n-q,p)>=q). Independent columns imply Z~Bin(m,b). In the fixed-k window p=1/k+beta/sqrt(n)+o(n^-1/2), m/sqrt(n)->c, local CLT gives m b->mu=c*k exp[-k^2 beta^2/(2(k-1))]/sqrt(2 pi (k-1)), while the JR obstruction is exponentially small via q-(n-q)p ~ n/k^2. Thus T converges to binom(Poisson(mu),k), including the zero and off-window regimes for polynomial m. This is an analytic proof; a separate literal-voter-cohesion vs compact-JR exhaustive check over 512 small approval profiles found zero discrepancies.

## originality

PASS

Best-of-knowledge PASS: the complete distributional count law in the growing-candidate square-root window for Distinctive Representation is neither the deterministic worst-case DR complexity theorem, fixed-m SJR/SSJR Bernoulli result, nor laminar-profile deterministic enumeration. The previously published ingredients local CLT and Poisson thinning are acknowledged, while the finite all-quota JR validity coupling and full committee-count phase transition are not implied by those prior statements.

## value

PASS

DR is a computationally difficult representation axiom in general approval elections. The explicit finite reduction to column-sum quotas, an exponentially small JR obstruction and the complete Poisson-binomial critical window answer a natural and quantitatively sharp random-instance feasibility/counting problem. That is a motivated probabilistic classification, not an unmotivated parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
