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

With h=α+2>1, the standard power-weighted upper-half-plane Bergman kernel is Kα=c[-i(z−w̄)]^(−h). For real (1,a,b) coefficients of f,a f′,b f′′, mixed derivatives cancel odd total orders and yield exact B/K=[t⁴+(h)_2(2b−a²)t²+(h)_4 b²]/t⁴, t=z−w̄ in upper half plane. Our independent symbolic expansion of all nine derivative-pair contributions reproduced this quartic exactly, including h=2 numerator t⁴+(12b−6a²)t²+120b². For b=0 the nonzero roots are real (t=0 factors are outside domain). For b≠0, set u=t² and C=(h)_2(2b−a²), E=(h)_4 b²>0; C<2sqrt(E) always, so all t roots are real iff C≤−2sqrt(E), equivalent to a²≥2b+2Q_h|b| with Q_h=sqrt((h+2)(h+3)/(h(h+1))). Below threshold u roots form one nonreal conjugate pair, giving precisely two simple upper-half-plane t zeros; all upper-half-plane t are realized by interior (z,w) via z=x/2+iy/2,w=−x/2+iy/2. At equality there are two doubled real t roots, inaccessible. The result covers real a,b all α>−1 only; finite numerical checks corroborate algebra, not all-parameter proof.

## originality

PASS

Bounded semantic Resultary search plus primary-literature comparison finds no earlier theorem dominating the precise full stated claim. Explicit equivalences and narrower covered portions are identified. This is best-of-knowledge, not a guarantee of global novelty. The unweighted h=2 specialization is known; only the weight-dependent all-α extension is novel.

## value

PASS

The real three-term differential-jet Gram kernel is a natural finite-dimensional family; the sharp weight-dependent zero-free phase diagram reveals a sign-sensitive restoration of zero-freeness. Although the h=2 unweighted specialization is known, extending the exact boundary to every integrable real weight α>−1 and proving precise zero multiplicities is a meaningful complete classification, not just a numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
