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

# Finite checks and their scope

The standalone `verify.py` uses only standard-library integers and checks the locating-dominating predicate directly: each unselected vertex must have a nonempty open-neighborhood trace on the selected vertices and no two such traces may coincide.

Run `python3 verify.py` from the directory containing the script. The verifier tests every apex-containing subset for each labelled simple base of order \(1\) to \(5\), checks the \(2\Delta(H)+2\) inequality for each non-LD case, independently checks the two-subdivided-star sharp examples for \(d=2,\ldots,20\), and tests the explicit wheel seven-class partition for \(m=10,\ldots,120\). It also enumerates the maximum singleton-repair count of hub-containing non-LD sets on wheels for \(m=3,\ldots,13\).

The last printed line is `VERIFY_OK`. The unrestricted mathematical proof is the trace argument in `RESULT.md`; finite tests cannot establish an infinite theorem or priority. A future independent audit has not been performed.
