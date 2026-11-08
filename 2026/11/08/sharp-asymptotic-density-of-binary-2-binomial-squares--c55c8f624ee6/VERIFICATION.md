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

# Reproducibility and limits

The standalone Python 3 script `verify.py` uses the built-in `collections` and `math` modules. Running `python3 verify.py` reproduces Gaussian-binomial polynomials and their squared coefficient sums for every half-length from 1 through 100. For lengths 1 through 12, it independently computes the full pair \((K,I)\) for all binary words and verifies the collision count; it also checks selected exact integers and scaled ratios approaching the theorem's constant. Successful output begins `VERIFY_OK`.

The proof's unbounded step is the published uniform local limit theorem of Canfield, Janson and Zeilberger, Theorem 4.5 of arXiv:0908.2089. The exact distribution's variance is \(k(n-k)(n+1)/12\), and the only application is for \(|k-n/2|\le n^{2/3}\), where both multiplicities tend to infinity proportionally to \(n\). The tail of the outer mixture is handled independently by binomial concentration. Finite tests are supplementary and do not certify the asymptotic theorem by extrapolation.
