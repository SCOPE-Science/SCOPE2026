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

For 0<p<1, t=2/p>2. Existence of an H^p coefficient-norm maximizer follows from normal-family compactness, Fatou and positive homogeneity. Brevig–Sovik outer-extremizer theorem (arXiv:2610.21788 Theorem 1) applies to the nonzero bounded functional L=a0+a1+a2, making each maximizer zero-free. Its H^2 root g=f^(p/2) has unit Hilbert norm and expansion coefficients b0,b1,b2; the coefficient formula and Parseval yield F_t(x,y)=[1+t(x+y)+t(t-1)x²/2]/(1+x²+y²)^(t/2), x=|b1|/|b0|, y=|b2|/|b0|. Both boundary axes have strictly positive inward derivatives and F decays at infinity, so the global maximizer is interior. The critical equations yield y=x/[1+(t-1)x] and the quartic Q_t(x) with exactly one positive root in (0,1) by Descartes sign changes and Q_t(0)<0<Q_t(1). I independently verified the exact identity R-yN=-Q_t(x)/(2D²) with symbolic algebra. The unique maximizer obeys real Schur quadratic stability (y<1 and x<1+y), so the normalized analytic t-th power attains the bound; equality of triangle and Parseval phases excludes additional maximizers other than common unimodular multiples. External outer-extremizer Theorem 1 is a necessary genuine mathematical premise, not proved by the finite checker.

## originality

PASS

PASS best of knowledge for three-term a0+a1+a2. Published Hardy extremal structure and a0+tau a2 sharp profiles are acknowledged as essential predecessors. Their functional omits a1, so no direct implication determines the simultaneous three-coefficient norm or its unique quartic optimizer; a classical equivalent Caratheodory-Fejer functional remains possible.

## value

PASS

The endpoint of the natural degree-two Taylor section is a function of all three early coefficients, and isolated sharp coefficients or mixed a0+tau a2 do not determine it. An exact all-0<p<1 norm and complete extremizer classification reduces a natural nonlinear Hardy quasi-Banach extremal question to a uniquely determined quartic root, providing directly reusable coefficients and equality cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
