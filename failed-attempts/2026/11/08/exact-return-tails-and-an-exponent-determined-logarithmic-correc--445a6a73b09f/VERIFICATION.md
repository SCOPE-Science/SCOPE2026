---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Full RESULT.md reconstructs the exact interval model for all fixed 0<ell<1 and normalized Lebesgue on H=(-c,0) union (0,c), including the null endpoint/branch convention. The crossing image z=g(x) increases monotonically, its remaining excursion follows phi(z)=z+z^(1+ell), and phi(1-c)=1 prevents a skipped return, proving Q(n)=g^{-1}(delta_{n-1})/c for all integers n>=1. With w_m=delta_m^(-ell), inverse recurrence gives w_m-w_{m-1}=ell-ell(ell+1)/(2 w_m)+O(w_m^-2); first deriving w_m=ell*m+O(log m) validates summation, and summability of renormalized increments yields finite K and O(log m/m) remainder. The shift m=n-1 produces D=(ell-K)/ell^2. g inverse derivative at zero is (2+ell)^-1 and its relative remainder O(n^-1/ell)=o(1/n) for ell<1. I inspected all seven actual snapshot Git blobs; independent high-precision original-map iterates and inverse thresholds checked 640 two-sided trajectories for four exponents, consistent with proof. Finite checks are not an infinite proof. The ell=1/2 specialization C=8/(5c), B=3 is consistent.

## originality

FAIL

The explicit conditional return law and subleading logarithmic coefficient are correct, but not an independently unknown result under implication-based priority. Coates–Luzzatto–Muhammad already build the exact central crossing/preimage partition (their equations (4)–(6)), covering the return-survivor threshold as its symmetric special case. The general Fatou-coordinate existence/asymptotic theorem of Mardešić–Resman–Rolin–Županović (2018), especially Proposition 6.4 and Appendix Remark 7.1, applies to the convergent parabolic germ phi^{-1} with phi(z)=z+z^(1+ell). From the Abel equation, the logarithmic term of its formal Fatou coordinate has coefficient (1+ell)/2: putting Psi(z)=-z^(-ell)/ell+A log z+... and Psi(phi(z))-Psi(z)=1 yields A=(1+ell)/2 by cancellation of the z^ell term. Inverting the time coordinate gives w_m=ell m-(1+ell)/2 log m+K+o(1), then B=(1+ell)/(2ell^2) follows by the elementary crossing-map derivative g'(0)=2+ell. The constant K is the orbit-dependent Abel-coordinate additive constant and the rest is an algebraic specialization. No matching theorem title/number is required for coverage.

## value

FAIL

First-return statistics of intermittent maps are naturally motivated and precision beyond the leading tail can be useful. However the submitted full finite-time identity is the obvious special-case interval/cylinder enumeration of Coates–Luzzatto–Muhammad, and the only claimed harder subprincipal log coefficient is a direct specialization of the established general power-logarithmic Fatou-coordinate expansion. K is an orbit-dependent additive integration constant, not an independently unknown exact invariant. Once the stronger prior methods are used, the result is a correct pedagogical calculation but no distinct mathematical gap, structural lemma, or unentailed exact quantity survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
