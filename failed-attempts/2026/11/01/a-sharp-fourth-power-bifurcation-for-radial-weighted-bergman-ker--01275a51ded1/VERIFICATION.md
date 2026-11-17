---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For q in {0,1,2,3,4} and real m>=0, monomials have exact unnormalized norms pi*B(n+m+1,q+1), giving K(t)=[pi*q!]^-1 sum_n product_{h=1}^{q+1}(n+m+h)t^n. Applying finite differences gives degree<=q+1 numerator over (1-t)^(q+2). The map t=(s-1)/(s+1) sends |t|<1 exactly to Re(s)>0. Independently derived with SymPy, using this series (not the supplied verify.py), the exact complete Routh first columns. For q=0: (1,2m+1); q=1: (2,4(m+1),2(2m^2+4m+1)); q=2: (6,6(2m+3),8(m+1)(m+2),2(2m+3)(2m^2+6m+1)); q=3: (24,48(m+2),8(2m+3)(2m+5),32(m+1)(m+2)(m+3)(m^2+4m+6)/((2m+3)(2m+5)),8(2m^4+16m^3+40m^2+32m+3)). All positive for m>=0. For q=4: first four Routh entries positive, fifth -64(m-1)(m+1)(m+2)(m+3)(m+4)(m+6)/((2m+3)(2m+7)), last 8(2m+5)(2m^4+20m^3+60m^2+50m+3)>0. Thus exactly two right-half-plane roots for m>1 and none for m<1; coefficients of Q(s) positive for m>=0 forbid a positive real s root; conjugate pair is simple. At m=1 Q(s)=120(s+3)(s^2+3)(s^2+4s+7); only +/-i sqrt(3) are on imaginary axis, yielding t=1-e^{+/-pi*i/3} on the excluded unit circle, and no open-disk root. This covers the m=1 singular Routh row. Finite numerical sample at m=2 corroborates but is not an all-real proof. The scalar t roots are realized by z*conj(w)=t with |z|,|w|<1. No claims for q>=5 or fractional q.

## originality

FAIL

FAIL: an already published Resultary full theorem, “Sharp first positive radial-power transition of analytic Bergman-kernel zeros” (publication metadata 2026-11-01), establishes every case of exactly the same full-disk analytic Hilbert-space N(m,q) theorem under renamed parameters, including q=4,m=1 circle crossing and simple conjugate pair for m>1, plus an extra derivative. The 2026-11-08 full fourth-Jacobi theorem strengthens the q=4 case to m>-1. This is statement-level direct coverage, not a title match; the original denominator/area normalization only scales K by a positive factor. Thus no distinct claimed conclusion remains.

## value

FAIL

The original invariant is mathematically motivated: the classical Lu Qi-Keng property on the natural beta-radial disk family, with a sharp first nonzero boundary exponent and a continuous interior exponent. Nevertheless, as a NEW mathematical result the complete classification and sharp bifurcation have already been proved in a public full theorem with even a stronger transversal formula. Re-deriving the same q<=4 Routh table or presenting a different denominator normalization supplies no new structural lemma, unresolved cutoff, motivating counterexample, or useful exact invariant not implied by the covered published theorem. Correctness/reproducibility alone cannot rescue value; therefore FAIL for independent research acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
