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

# Reproducibility and proof limits

Run `python check_sunlet.py` and `python verify_generating.py` using Python 3. The latter uses `mpmath` only for its optional high-precision numerical value; all exact-rational assertions use the standard library. The first program computes the Markov recurrence directly on subsets of currently vacant endpoints and compares it with an independently written first-edge expectation formula on 19 finite graphs. The second constructs the numerator of the expected-coverage generating function through rational coefficient arithmetic, verifies 110 exact identities, and checks the sign and alternating bound at 92 sizes. Both completed without errors after extraction from the final package.

The finite checks are not an infinite proof. The proof in `RESULT.md` relies on a full graph decomposition, an analytic generating function, an exact absolutely convergent alternating tail, and a strict ratio bound valid for every finite size \(n\ge3\). These steps independently justify the infinite conclusion.

The result is not a claim of exhaustive bibliographic priority. Restricted access to historical full texts leaves a genuine prior-art risk; scientific review is not an independent external audit.
