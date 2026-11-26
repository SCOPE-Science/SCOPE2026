---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With R=b-C>0 the low digit obeys 1<=R+jd<=b-p-d-2<b, so s_j=1+R+jd=b-1-h_j. For any prime q|s_j the chosen m=1+tL gives b^m≡b mod q, trivially if q|b and by Fermat otherwise. Thus a common prime must divide b-1 and h_j, which divides H. The start increases with t. Every p terms represent all residue classes mod p and s_b(N)≡N mod p, proving the sharp obstruction. All primes of Q are odd and different from p, so CRT gives the stated density for the particular class (not necessarily the density of all admissible bases), and b-1=2^u p^a meets all conditions above C. Independently built the four full integers for b=41, d=4, p=5, m=991 and divided repeatedly by 41: sums 19,23,27,31 and gcds all 1. The frozen verify.py and recorded result report broader but finite examples only.

## originality

FAIL

The scientific sharpness assertion and infinitude on every base in the frozen family are covered by the published short-even-strides theorem with strictly weaker hypotheses. The density is the count of one chosen residue class inside the pre-existing sharpness range. The particular closed start formula is not asserted to have been printed earlier; it is the old simultaneous exponent lemma applied to a prescribed safe residue in a no-carry subclass. No claim of within-day historical priority between the two dated entries is necessary for the coverage verdict.

## value

FAIL

A genuine sharpness range for the fixed-step conjecture would have value, but this range is wholly inside a published tractable one. The additional fixed residue class density is a direct CRT count, not the density of all sharp bases, and the exponent formula has no size or effectiveness advantage established against the earlier construction. The frozen record supplies a worked subclass rather than a standalone advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
