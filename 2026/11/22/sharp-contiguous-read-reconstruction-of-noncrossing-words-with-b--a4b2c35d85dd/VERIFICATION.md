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

# Reproduction

Run `python verify.py` with a standard Python 3 interpreter. It reconstructs each full directed contiguous factor spectrum independently from words, groups all eligible words by that spectrum, and tests whether a group containing a noncrossing word ever has more than one word. It tests parameter tuples `(k,q,nmax)=(2,4,7),(3,3,11),(3,4,8),(4,3,10)`, the sharpness pairs for \(2\le k\le8\), and the first ten coefficients of the bounded-block partition generating series for multiplicity ceilings \(2,4,6\). No third-party packages are required.

The bounded tests are exhaustive only for the named ranges and do not prove the theorem for arbitrary length, alphabet, or read size. Infinite correctness is supplied by the de Bruijn trail argument in `RESULT.md`. The general Euler-trail switching criterion is a standard reconstruction lemma, not a new lemma of this result.
