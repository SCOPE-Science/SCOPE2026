---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification notes

`checker.py` evaluates each conditional directed-row balance by enumerating all off-diagonal arc subsets and then averages over all nine weighted two-dimensional color difference types. For each \(n=2,3,4\), it computes \(\Pr(Z_n=0)\), \(\mathbb E Z_n\), and \(\mathbb E(Z_n)_2\) as exact rational numbers. It crosschecks \(\mathbb EZ_n\) against a distinct binomial-outdegree formula, and for \(n=3\) it independently enumerates every directed arc assignment to reproduce \(\Pr(Z_n=0)\). It also checks the exact mean identity at \(n=300\) against the predicted limit \(1/\pi\) to within an explicitly stated finite tolerance.

Confirmed rational finite values:

- \(n=2\): \(\Pr(Z_n=0)=11/16\), \(\mathbb E Z_n=5/16\), \(\mathbb E(Z_n)_2=0\).
- \(n=3\): \(\Pr(Z_n=0)=41665/65536\), \(\mathbb E Z_n=105/256\), \(\mathbb E(Z_n)_2=3009/32768\).
- \(n=4\): \(\Pr(Z_n=0)=21479399/33554432\), \(\mathbb E Z_n=1743/4096\), \(\mathbb E(Z_n)_2=36819/262144\).

The checks are finite and do not prove the infinite-dimensional convergence. The mathematical proof in RESULT.md establishes that convergence through a conditional two-dimensional lattice local limit, the random-color central limit theorem, and an elementary conditional Poisson-binomial approximation. The non-Poisson variance and exact uniform mixing distribution follow analytically. No external or independent review has been performed.
