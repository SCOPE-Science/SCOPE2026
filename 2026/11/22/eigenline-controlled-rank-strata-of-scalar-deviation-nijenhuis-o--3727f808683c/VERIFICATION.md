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

With t-coordinate beta on N(V), the (v,w) torsion has t-coordinate up to sign beta(v)beta(Tw), so invertibility of T gives beta=0. The (t,t) and (t,v) equations then reduce to ETc=0 and E[T,E]=0, with all other basis pairs automatic. Substituting E=u tensor phi gives phi(Tu)phi=phi(u)(phi composed with T), separating the two stated branches. For each projective functional line a fixed representative gives unique u: in the square-zero branch the two covector constraints allow q^(d-2)-1 nonzero vectors off the eigenlines and q^(d-1)-1 on them, yielding K_T. In the other branch each of H_T/(q-1) lines gives (q-1)q^(d-1) vectors u, and all nonzero E permit q^(d-1) c values. At a=0 count c in ku (q choices in the square-zero branch and one in the eigenline branch) versus off ku to split ranks one and two. At a nonzero, the rank is 1+rank(aI+E); the only singular possibility is the unique a=-phi(u) in the eigenline branch, producing rank d. This yields exactly the displayed polynomial, with coincident degrees combined at d=2, and the corank-one claim is only made for d>=3. The shift M=N-aI has M^2(t)=Ec and M^2(V)=0 in the square-zero branch; index three means phi(c) is nonzero while phi(Tc)=0. This gives q^(d-1)-q^(d-2) c values exactly off the eigenlines, and neither the zero nor eigenline branch contributes. These deductions do not use semisimplicity or a characteristic restriction.

## originality

PASS

The closest distinct work classifies rank-one square-zero operators for an almost-abelian Lie algebra, not rank-one deviations for this non-skew bracket. No inspected original statement gives or implies the full two-branch finite-field rank and shifted-index census. The exact entry under 3727f808683c is this record itself.

## value

PASS

The quotient scalar a makes rank(D-aI) an intrinsic stratum of a basic one-generator extension, not an arbitrary subset of matrices. The full rank distribution detects rational eigenlines at corank one for d>=3 and connects them to a different phenomenon, shifted nilpotency of index three, which can occur even when corank one is absent. The formulas hold for nonsemisimple as well as semisimple actions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
