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

The embedded `checker.py` executes with the standard Python interpreter and no third-party packages. Run `python checker.py` after extracting the embedded files. It compares recursion with brute-force rooted-walk semantics on all binary-weight models up to three worlds and on reproducibly selected real-valued models through four modal iterations. It also enumerates abstract path-overlap patterns through depth five and checks the overlap count and exponent inequalities used in the proof. These finite checks are not an exhaustive proof of the large-\(n\) limit; the argument in `RESULT.md` supplies the asymptotic reasoning and cites a dependency-graph Poisson approximation theorem. No independent audit has been performed.
