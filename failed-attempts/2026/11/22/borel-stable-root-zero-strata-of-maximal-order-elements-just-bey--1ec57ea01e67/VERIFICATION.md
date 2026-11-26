---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Frobenius gives (I+N)^r=I+N^r, and N^(pr)=0 since pr≥r+2; order p^(k+1) is therefore equivalent to N^r≠0 and is attained by the unit first-superdiagonal matrix. Only the two length-r products and the top-right sum with one two-step jump can be nonzero. The third coordinate is a nonzero linear form in the second superdiagonal iff some adjacent omitted pair contains the first-superdiagonal zero set. Excluding the three patterns where a length-r product survives leaves exactly one internal zero or two consecutive zeros. This uses only field multiplication, so characteristic two and infinite fields cause no exception. Borel conjugacy multiplies the simple-root coordinates by nonzero ratios of consecutive diagonal entries, as also seen in the quotient by matrices vanishing on the first superdiagonal. With z=1/q and t=1−z the probability is t^r(1+z)+t[(r−1)zt^r+rz²t^(r−1)]=t^r(1+rz+z²); multiplying by group size gives the stated count. At n=r+1 only one ordinary product survives. Own direct repeated squaring over F4 in /workspace/branches/independent-replays.py 1 checks all 4096 elements of UT4 and finds 3600 order-four elements, including the expected conditional counts. This corroborates the extension-field case, not the general proof. The frozen prime-field enumeration and recorded output were inspected, not executed.

## originality

FAIL

Verified structural coverage, not merely overlap in an unconditional numerical count: the distinct same-day Resultary f5d834a0af02 proof gives the same coordinate functions and explicitly the same adjacent-pair criterion by first-superdiagonal zero pattern. Specializing m=r and asking whether its target is zero yields the exact empty/full/hyperplane-complement classification. The extension to arbitrary characteristic-p fields and Borel invariance are immediate from the same path formula and diagonal rescaling and do not leave a substantively distinct theorem. This does not assign historical priority between the same-day records.

## value

FAIL

The exact order-support classification is a natural question, but the useful adjacent-zero obstruction and full fiber geometry are already mechanically available from the stronger matching proof. Recasting its zero-fiber complement in order language and adding elementary Borel rescaling do not leave a separate useful unknown exact fact. No substantive surviving repair was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
