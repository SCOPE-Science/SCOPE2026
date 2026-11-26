---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

I checked the all-length proof in RESULT.md:30–80. Every occurrence avoiding the proposed marks lies inside one of the listed gaps. For c≥a the two kinds of mixed gap factors 0^i1^j and 1^i0^j relocate across the right and left boundaries of the central run, respectively. For c<a and b=1 the only mixed gap factors are 10^i, which relocate to the selected second 1. For c<a and b≥2 the sole potentially mixed gap is 0^(c−1)1^(b−1), and its mixed factors relocate to the first boundary. The selected runs accommodate all pure gap factors, including when a gap is empty. For necessity in the third case, 0^a1 and 10^a must cross the outer boundaries, while 1^(b−1)0^c1 must cross both central boundaries. Their unique intervals [0,a], [a+1,a+b+c], [a+2b+c−1,2a+2b+c−1] are disjoint also at b=2. In every case the two single letters require two different positions. The substitution c=1+r, a=c+1+t, b=2+s is bijective and yields length 9+3r+2s+2t, proving the exceptional generating function and the two shortest exceptions. Comparing the order-three poles at 1 gives leading coefficients 1/6 and 1/2 there; all other poles give O(n) coefficients. Hence the density is 1/3.

## originality

PASS

The strongest available close statements concern all four-run words, a different restricted five-run family, or a different invariant of exactly the same words. None gives the five-run threshold or thereby implies the exception count. This is a bounded assessment, not a priority guarantee.

## value

PASS

This gives a complete boundary, with optimal certificates, for an unbounded natural family of binary palindromes. It identifies exactly when three disjoint compulsory factors defeat a two-position attractor. The density is a useful consequence, not the sole contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
