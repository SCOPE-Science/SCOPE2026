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

# Reproducibility

The analytic proof uses three inequalities on nonnegative row sums and an equality characterization from the positive Perron eigenvector of an irreducible block. It covers all real \(\gamma\geq1\), all finite dimensions \(n\geq2\), all nonnegative symmetric zero-diagonal affinities having a positive maximum edge, and all positive total budgets. Equality requires a maximum-weight edge and equal areas at its endpoints.

Run `python checker.py` in a directory with Python 3.10+ and NumPy available. The source has no data downloads, hidden support files or randomness outside a fixed seed. It executes exact rational tests of the three-site examples, checks the exponent comparison, and independently constructs randomized symmetric matrices and compares their spectral radius with the bound and the two-site optimizer; the replay recorded 8,103 passing assertions.

The 8,103 finite tests do not prove the all-parameter statement, nor do they verify novelty. Prior literature comparisons include a full HTML-text mathematical-methods and results inspection for Bertuzzo et al. (2015), metadata and abstract inspections for Hanski–Ovaskainen (2000), Etienne–Heesterbeek (2000), Etienne (2004), and Nicol–Possingham (2010), and dedicated Research-record searches. Some full texts were inaccessible and historical priority remains provisional. Independent audit has not been performed.
