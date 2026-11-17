---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The exact periodized resolvent expansion for c_{n,j}(h) with a=h/(h+2), b=h/(h+1) was reconstructed and the integer numerators for n=2..5 independently calculated: all are coefficient-positive except (5,4), whose numerator is four times p(h)=25h^8+300h^7+1300h^6+2850h^5+3450h^4+2240h^3+560h^2-160h-96. Descartes plus exact rational endpoint signs give its unique positive recovery root. For every n>=5, the coefficient of P^4 in the stability series is (2*5/16-1)h^4=-3h^4/8; for each fixed finite n, Fourier diagonalization gives T_n(h) tending to the strictly positive uniform projection as h→infinity. Mass conservation follows from Q1=0. This proves the infinite n conclusion rather than only checking finite samples.

## originality

PASS

An October 13 pure-birth Richardson result treats an absorbing, noncirculant generator, with its first five-state recovery near 0.3959 and an upper positivity cutoff at 2+2sqrt2. It does NOT imply the five-cycle unique threshold near 0.297835688, all-step positivity n<=4, or eventual recovery for every n. Implicit Taylor/Radau and centered-advection papers use other stability maps. The specific cycle coefficient classification is not covered by inspected sources.

## value

PASS

Preservation of Markov positivity by higher-order extrapolation is a mathematically motivated structural question; a sharp size-four/five obstruction and a unique algebraic recovery boundary give exact, reusable cycle-test information beyond routine stability order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
