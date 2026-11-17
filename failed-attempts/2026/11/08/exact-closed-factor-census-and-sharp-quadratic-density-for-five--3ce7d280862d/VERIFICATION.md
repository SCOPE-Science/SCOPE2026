---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Every closed factor of a five-run word can be sorted by number of its constant runs. One-run factors and empty factor contribute 1+max(a,c,e)+max(b,d); two-run factors cannot have borders. Balanced end fragments give three-run terms x+y+z-I*h; four-run mixed borders give z(x+y). Five-run factors close either by a mixed border exactly when b=d and both zero end fragments fit the central zero run, contributing I*x*y, or by a pure-zero border when equal outer fragments exceed the middle zero run. The elementary identities reduce the sum to n+1+z(x+y)+I(xy-min(x,y)), with x=min(a,c), y=min(c,e), z=min(b,d). Since n>=1.5(x+y)+2z and xy<=(x+y)^2/4, the quadratic terms are <=n^2/8. Witness lengths (2k,k,2k,k,2k) attain 8k^2+6k+1, padding the last zero-run extends to every large n. The exact formula was algebraically reduced to the October 25 formula and tested on 243 tuples; finite checks are not universal proof.

## originality

FAIL

DEFINITIVE prior coverage: the October 25 published closed-factor spectrum theorem gives the entire same arbitrary-five-positive-run exact count of nonempty closed factors. Add one for the current empty-factor convention and simplify the October 25 elementary run identities to obtain precisely the November 8 boxed formula; prior work also proves the same 1/8 asymptotic plus a stronger extremizer rigidity theorem.

## value

FAIL

FAIL: The older October 25 result already provides the same entire exact five-parameter count (up to including the empty factor), the same optimal coefficient 1/8, and a strictly stronger rigidity description of extremizers. The November formulation supplies no independently motivated new invariant, boundary, or genuinely new mathematical assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
