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

# Verification and scope

Run `python3 verify_incidence.py` from the directory containing this file. The code exhaustively enumerates row subsets, computes ordered injective non-induced motif embeddings directly, and checks exact unconditional and vacancy-conditioned rational moments. Seven test cases include matching, star, biclique, path and overlapping double-star motifs, with distinct row-size profiles. It also checks 638 exact rational formula/sign instances for the two-star family. All checks passed in the local Python 3 execution.

The general theorem is established by the conditional sampling argument and strict concavity in RESULT.md; the finite checks cannot establish general validity or historical originality. The 1999 projected-graph subgraph article was not inspected in full. The reference date for the accessible 2008 source is the first posted arXiv version, not the later revision.
