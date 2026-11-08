---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and verification

Run `python3 verify.py` with a standard Python 3 interpreter. No third-party dependencies are required. The program directly constructs the weighted Laplacian action and the Krylov controllability sequence rather than using the spectral closed form to compute ranks.

Observed completed output:

```
PASS 322 two-prime full Krylov-rank tests, 785 exceptional-mode residual tests, 196 unweighted modular-size tests
```

For each \(n\) from \(3\) through \(48\), seven rational leaf conductances were checked with two finite-field primes. At \(t=1\) and \(t=\tfrac12\), the exact predicted rank deficit of two was compared against full finite-field ranks, including all exceptional sizes in this interval. For \(n\) from \(3\) through \(64\), each eligible mode's analytic coordinates were tested against the explicit weighted Laplacian eigenvalue equation, with residual tolerance \(2\times10^{-10}\); these checks use floating-point arithmetic. Both modular size laws were also independently compared against the exceptional-weight formula for \(3\le n\le100\).

Finite-field checks are finite cases and may differ from characteristic-zero ranks in rare parameter configurations. Floating-point mode checks do not prove exact identities. The proof in RESULT.md supplies the infinite-family spectral simplicity, complete mode characterization, nonzero-root argument, parameter-boundary treatment, and PBH rank theorem. These scientific results have received a self-review; an independent mathematical audit has not been performed.
