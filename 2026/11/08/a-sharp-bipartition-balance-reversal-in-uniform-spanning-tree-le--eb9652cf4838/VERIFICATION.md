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
# Reproducibility and boundaries

Execute `python3 verify.py` with a standard Python 3 installation. The script independently generates graph Laplacian cofactors using fraction-free integer elimination, counts all spanning trees of small graphs, compares exact rational expected leaf counts, and tests \(2\le a\le120\), \(1\le b\le120\) for the claimed sign rule. The observed output was `VERIFY_OK 14416 exact assertions`.

The proof of the all-parameter theorem is analytic and given in `RESULT.md`; passing a finite checker does not itself establish a universal identity. The base complete-bipartite weighted polynomial is attributed to prior literature. Historical priority is not externally certified. No independent audit has been performed.
