---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Proved on all labelled K_{2,n}, n>=1, three additive colours and unnormalized counting convolution. Splitting by equal pole colours (3(-1)^(n-z)2^z) versus unequal (9*1_{α=γ=S}-3*1_{T=0}) yields W=3*1_{T=0}[(-1)^(n-z)2^z-1+3*1_{α=γ=S}], with T=α+γ+S. Each leaf-frequency vector has exactly 3 balanced pole-charge pairs, one exceptional, two ordinary, hence all signed multiplicities A_z, B_z exactly as stated. Extra zeros arise only A_0 and B_1 for even n, totaling (n+4)2^(n-1); minimal positive modulus 3 odd, 9 even. Direct independently implemented exact 3-colour character transform for n=1..5 matched each coefficient and multiplicity, including n1 and n2 edge cases; the formula and 2-adic case analysis give general proof. Triangle inequality maximized at zero frequency gives conditioning norms.

## originality

FAIL

A published all-shore-size K_{m,n} ternary Fourier theorem gives every coefficient explicitly and a complete balanced zero classification; specialize m=2 to recover the assigned K_{2,n} coefficient expression identically. The current signed histogram and smallest nonzero magnitude follow by direct binomial counting/powers of two from that exact stronger formula. Hence the narrow contribution is covered even without literal matching numbers in the stronger title. Same-day publication ordering unresolved and is not claimed to prove historical priority.

## value

PASS

All-frequency ternary convolution spectrum of a natural growing two-shore graph is a motivated spectral-recovery invariant, with an exact even-shore cancellation and sharp 3-versus-9 gap. Nonetheless its statement is already implied by a stronger known exact theorem and cannot be certified as a new finding; no independently valuable uncovered consequence remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
