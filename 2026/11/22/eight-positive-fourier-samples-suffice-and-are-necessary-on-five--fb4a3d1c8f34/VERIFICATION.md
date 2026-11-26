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

The Toeplitz frame identity is exactly the normalized Laurent moment condition on degrees −4 through 4. For six or seven grid nodes the nodal polynomial times z^−4 has exponents in that range, so its constant coefficient e2 or −e3 must vanish. Padding any smaller support with zero-weight nodes is legitimate for the corresponding obstructions. Since Φ_(2p)(−1)=p, reduction ζ→−1 sends the symmetric sums to coefficients of (1+x)^a(1−x)^(s−a). Independent exact expansion gives e2 values 15,5,−1,−3,−1,5,15 (none divisible by 7) and e3 values −35,−5,5,3,−3,−5,5,35 (prime divisors only 3,5,7). For the upper bound the proposed eight indices are distinct since 0<a<b<p−a<p, and cos(πb/p)=sin(π/(2p)). Lagrange interpolation in X² independently recovers E,C,D from the moments 1,1/2,3/8, and the two odd moments fix the mass differences. Symbolic substitution verifies precisely the stated formulas and all Chebyshev cancellations. Uniform positivity follows from 1/4<c²<1/2 and 0<d<1/4: C,D>0; E−Δ_E has positive numerator by the displayed strict bounds; C+Δ_C has positive numerator (c+d)(1−4cd). The bounds on a follow directly at 11 and from p/4+1<p/3 thereafter. Conjugate pairing kills imaginary moments. For 3 the conjugate moments exhaust every nonconstant mode on six roots and force the uniform rule; for 5 and 7 the even-frequency subgroup supplies the witnesses and rank/parity supply the lower bounds. No finite numerical sampling is used for the infinite-prime assertion. The supplied checker was inspected, not executed.

## originality

PASS

The new-to-current-knowledge claim is the exact support law under the full twice-prime grid restriction and the uniform positive eight-node witness, not the general Parseval/quadrature correspondence or a free-node formula. The closest framework and indexed analogues do not give the two-sided result under these constraints.

## value

PASS

The exact minimum is a natural resource for tight measurement on a fixed consecutive Fourier aperture. The prime-dependent exceptions and sharp large-prime budget are accompanied by a search-free strictly positive construction and an arithmetic obstruction reusable for restricted quadrature. They add more than a rank bound, a free-node existence theorem, or a list of small instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
