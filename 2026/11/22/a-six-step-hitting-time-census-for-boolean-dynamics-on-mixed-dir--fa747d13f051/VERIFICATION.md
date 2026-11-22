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

The symbolic proof in `RESULT.md` works for all integers m,k at least one. Its critical computations are the Boolean hub recurrence, the seven nested complete-occupation tests, independent assignments to the two OR summaries, and subtraction of cumulative counts. The last shell is nonempty whenever k at least one.

The included `verify_rose.py` was executed from this package's source code with Python 3 and no third-party packages. For 33 parameter pairs satisfying 1+m+2k at most 16 it independently evaluated the actual synchronous AND update on all 299,696 labelled states; for cases of size at most 13 it also checked via Boolean in-neighbor predecessor propagation. Representative counts and success line are preserved in `verification_output.txt`. Large-parameter integer sum consistency was also checked.

The finite checks do not establish the theorem for arbitrarily large graphs; that conclusion is justified by the exact symbolic argument. The 2007 relevant exponent paper was accessible only in summary; no full-document negative coverage conclusion is made. Historical equivalence remains a risk. No independent audit or validation is claimed.
