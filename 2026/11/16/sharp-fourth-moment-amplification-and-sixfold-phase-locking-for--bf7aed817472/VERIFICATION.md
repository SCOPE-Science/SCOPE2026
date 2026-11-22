---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For Fourier support 0,1,2,3 modulo 6, Parseval gives E^2+2|R1|^2+2|R2|^2+|R3|^2, where R3=2Re(c3 conjugate(c0)) is self-inverse due to sixfold torsion. Putting outer energy A=|c0|^2+|c3|^2 and inner energy B=|c1|^2+|c2|^2, Cauchy/triangle/AM-GM imply |R1|<=sqrt(AB)+B/2, |R2|<=sqrt(AB), |R3|<=A. They are simultaneously attained by symmetric positive magnitudes (sqrt(A/2),sqrt(B/2),sqrt(B/2),sqrt(A/2)); the exactly sharp quotient is F(t)=(3t^4+4t^3+12t^2+4)/(2(1+t^2)^2). Its derivative sign is -t(t^3+3t^2-3t-2), with one positive root rho~1.145102691200422; both endpoints lower, giving C6~2.892164358578031. At the positive maximum equality forces magnitudes (1,rho,rho,1); alignment of R1 gives affine phases and the R3 collision forces eta^6=1, precisely six projective extremizers. Independently checked algebraic derivative, 3000 random complex inputs against direct six-point fourth moments, and all six equality cases. The proof, not random testing, gives the all-complex-vector inequality.

## originality

PASS

Best-of-knowledge new finite-cyclic four-out-of-six fourth-moment norm and sixfold phase-rigidity classification beyond known continuous even-moment symmetrization and nearby finite three/co-singleton/subgroup-hole cases.

## value

PASS

The six-point cyclic group is the smallest nontrivial setting for a consecutive four-character support with two omitted frequencies. Its self-inverse third autocorrelation changes the exact fourth-moment sharp constant and collapses continuous affine-phase equality to six isolated projective directions. This is a meaningful sharp finite Fourier amplification and equality-orbit invariant, rather than a routine norm restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
