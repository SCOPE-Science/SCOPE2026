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

# Verification and limits

The self-contained script `verify_constructive.py` independently checks the two-part legal-update construction, cut maximizers, the count \(6(2^n-1)\), and the \(2n\)-transition face exit count for all \(1\le n\le6\). Its exact observed output is in `verify_constructive_output.txt`; it checks \(299592\) labelled configurations.

The separate script `verify_scc.py` explicitly constructs every vertex-update transition and finds closed strongly connected components for \(1\le n\le4\). It independently confirms a single recurrent component, its equality with global max cuts, and transition reversibility. Its exact observed output is in `verify_scc_output.txt`; it checks \(4680\) labelled configurations.

Run `python verify_constructive.py` and `python verify_scc.py` in Python 3. The latter imports NetworkX (tested with version 3.6.1; the optional pinned dependency is listed in `requirements.txt`). No external datasets or services are needed.

The infinite-family theorem is justified by the symbolic proof in `RESULT.md`, not extrapolated from finite tests. No independent audit, mixing upper bound, spectral-gap calculation or historical-priority certification is claimed.
