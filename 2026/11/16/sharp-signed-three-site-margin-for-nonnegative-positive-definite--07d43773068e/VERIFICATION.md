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

For continuous real globally nonnegative positive-definite normalized f, Bochner gives f(y)=int cos<xi,y> dmu with a symmetric probability measure. For c=(-1,1,1) and sites 0,x,-x the Gram quadratic form is exactly 3-4f(x)+2f(2x). The identity 5/4-2cos(t)+cos(2t)-cos(3t)/4=(1-cos(t))(2cos(t)-1)^2/4 is an exact Chebyshev factorization, independently verified by rational symbolic expansion. Its integral and f(3x)>=0 give energy-1/2=f(3x)/2+(1/2)int(1-u)(2u-1)^2dmu>=0, u=cos<xi,x>. Equalities force u∈{1,1/2} almost surely and equal mass on both phase classes, while global nonnegative admissibility is still required. The normalized f(y)=(1+cos(y))/2 at x=pi/3 has f(x)=3/4, f(2x)=1/4, f(3x)=0, so energy=1/2; extension to any d via one coordinate establishes dimension-free sharpness. Nonnegative deficit yields the stated phase-concentration stability by a direct Markov bound. No global Loewner assertion is inferred from this single-vector test.

## originality

PASS

PASS best of knowledge for the nonnegative-function three-site sharp 1/2 signed margin, not for generic Bochner, Krein or elementary trigonometric identities. The 2011 original formulates a broader Loewner conjecture, the 2026 Vybíral paper refutes its unrestricted eight-site version, and Pevnyi–Sitnik gives general positive-definite inequalities, but no inspected source proves this stronger exact special-vector margin and equality law. Older correlation-inequality formulations remain a specific priority risk.

## value

PASS

The original nonnegative-positive-definite Gram-matrix conjecture fails for certain larger configurations; testing the smallest symmetric signed center-vs-pair configuration is a motivated boundary question. The sharp positive 1/2 margin, exact deficit decomposition, full phase equality conditions and stability estimate identify a surviving quantitative rigidity in a natural minimal configuration. This is not a routine Bochner positivity statement (which alone only gives a zero lower bound).

The dated certificate retains the supplied scientific assessment, sources and limitations.
