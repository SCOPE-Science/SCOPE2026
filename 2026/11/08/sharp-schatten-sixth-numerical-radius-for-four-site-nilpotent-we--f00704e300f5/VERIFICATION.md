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

The attached `verify_schatten_sixth_four_site.py` is a standard-library script using exact `fractions.Fraction` arithmetic. In its replayed run it returned `SCHATTEN_SIXTH_FOUR_SITE_EXACT_CHECK_OK 796`. It evaluates the sixth matrix trace and the \(x,y,z\) trace identity on 343 integer-weight triples; each comparison is accompanied by a Schatten-norm denominator identity. It checks the elimination formula on 60 nontrivial triples of rational squared weights and the one-variable derivative on 50 positive rational test points. The root bracketing and two explicit objective values are checked separately.

Separately, symbolic polynomial algebra yielded the exact identities
\[
g'(r)=-6(r^4+3r^3-4r-3)/(r^3+2)^2
\]
and
\[
F=m+y^3+6uy^2+8u^2y+my/(2u).
\]
The proof in `RESULT.md` supplies the global strict-convexity reduction, treatment of all zero-weight boundaries, uniqueness of the positive quartic root, and all equality conditions. None of the finite checks by itself proves those infinite families of assertions. The theorem is for four-site nilpotent shifts with exponent six, and no external audit is implied.
