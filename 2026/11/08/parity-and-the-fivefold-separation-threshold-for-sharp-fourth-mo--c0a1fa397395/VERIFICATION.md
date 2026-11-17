---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For normalized dx/2 on [-1,1] and integer 0<=ell<h of opposite parity, the L2 orthogonality and vanishing odd fourth mixed terms reduce the normalized fourth moment exactly to Q(s)=A(1-s)^2+B s^2+2Cs(1-s), s the higher monomial L2 energy share. A,B,C are stated rational moment coefficients, with A<B; C-B has numerator -2(2h+1)[2h^2-(10ell+4)h-(2ell+1)], and this polynomial crosses between h=5ell+2 and 5ell+3. Opposite parity excludes 5ell+2. Completing the square when C>B gives exact mixed optimizer s=(C-A)/(2C-A-B) and K=(C^2-AB)/(2C-A-B); when C<B strict endpoint domination forces the pure higher monomial. Same-parity first variation of each pure monomial excludes pure maxima; the ell=0 constant case is handled by B>1. Dividing moments by ell yields the stated asymptotic h/ell=5 switch. Independent exact rational moment calculations checked 694 opposite-parity exponent pairs; finite tests are corroboration only.

## originality

PASS

Two highly relevant primary full texts were inspected. Borwein-Erdelyi-Zhang (1994) studies Müntz-Legendre orthogonalization, derivative bounds, Markov and bounded Nikolskii-type inequalities, but not the exact real L2-to-L4 norm for an opposite-parity two-monomial subspace. Borwein-Erdelyi (1995) treats density/Remez inequalities, not this optimization. Indexed Resultary sharp fourth-moment statements concern Fourier characters and other structures, not two real monomials. The elementary moment quadratic is acknowledged as standard; the exact integer threshold and complete equality classification were not found in these sources.

## value

PASS

Sharp finite-dimensional L2-to-L4 embedding constants are natural approximation/functional-analysis invariants. The integer gap threshold h near 5ell and its distinct mixed/pure extremizer types provide a non-obvious complete parameter classification for two-dimensional Müntz subspaces, including an asymptotic phase boundary. This is mathematically useful despite the elementary exact-moment method and despite not solving the same-parity constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
