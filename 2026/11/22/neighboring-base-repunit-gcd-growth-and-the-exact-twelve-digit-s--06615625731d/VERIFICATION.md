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

The roots of P_m are simple nonidentity m-th roots of unity. For a common root z of P_m(X),P_m(X+h), the two unit-modulus equations give Re z=−h/2. For h>2 this is impossible; h=2 translates the only candidate −1 to the excluded root 1. For h=1 the candidates have orders 3 and their translates have order 6, giving exactly the quadratic factor precisely when 6 divides m. After exact monic division, the residual evaluated GCD equals gcd(A(b),B(b),C) where C is the absolute nonzero resultant, giving divisibility, periodicity and the growth dichotomy. Independently expanding the original polynomials in ZZ verified the length-six bound after parity and the length-twelve resultant 1023252616422400. At length twelve there is no common root modulo 2; the listed roots modulo 5,7,13 have exactly the displayed disjoint lift digits modulo the respective squares. Hence the residual is squarefree. CRT gives the eight values and their frequencies; any period has to preserve each nonconstant prime indicator, forcing divisibility by all three primes. The independent replay also rejected all smaller cyclic shifts of the exact evaluated table.

## originality

PASS

The general divisibility and periodicity theorem for coprime polynomial values is established prior work, and the finding does not claim it as new. The supported distinctions are the classification of which equal-length shifted repunit pairs have a common polynomial factor, and the exact two exceptional-length residual laws, in particular the length-twelve local square obstructions and least period. None of the inspected table comparators has these two polynomial inputs. The citation summary in RESULT.md line 99 overgroups Bodin–Dèbes (arXiv:2105.13883) with the univariate periodicity sources: its several-variable theorem concerns gcd/lcm stability and permits infinite sets. This is a literature-description correction, not a flaw in the theorem, whose periodicity proof is self-contained and also matches the separate univariate references.

## value

PASS

Fixing the length and varying the positive base gap is a natural classification of shared divisibility across repunit bases. The unique quadratic-growth family and the two exact initial exceptional spectra give mathematically meaningful boundary data; the length-twelve example separates the coarse resultant bound from sharp simultaneous prime-power divisibility and from the true period.

The dated certificate retains the supplied scientific assessment, sources and limitations.
