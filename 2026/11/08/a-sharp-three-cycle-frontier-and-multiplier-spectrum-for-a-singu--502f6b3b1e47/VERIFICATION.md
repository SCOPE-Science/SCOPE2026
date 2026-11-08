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
# Verification

Execute `python verify.py` with SymPy installed. The script performs exact arithmetic for: conjugate map iterate numerator; third-iterate sextic discriminant; double cubic at \(A=3\); two cubics at \(A=4\) and all three sign-change brackets in each; factorization into the invariant cubics; invariance under the rational map; multiplier formulas from symmetric polynomials; and the rational polynomial determining the flip boundary. It also compares the multiplier products at four rational sample parameters against direct numerical products over the three cubic roots.

The proof in `RESULT.md` supplies non-computational arguments not inferable from these finite tests: absence of negative real cycles, root-count continuation across \(1<A<3\) and \(3<A<4\), positivity of roots and the compact trapping interval to which Sharkovskii's theorem applies. It distinguishes the special \(y=1\) point at infinity from finite original coordinates, and excludes the original pole. The symbolic tests are exact identities in the indicated polynomial ring, not samples over the parameter continuum. The sample tests are sanity checks only. No independent external audit was performed; the 1992 related source was not available in complete text.
