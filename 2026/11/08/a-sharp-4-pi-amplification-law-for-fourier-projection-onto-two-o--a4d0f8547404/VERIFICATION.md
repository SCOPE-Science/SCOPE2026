---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The union of x↦(x,±x²) over F_p intersects only at (0,0), hence the convolution kernel is the sum of two quadratic exponential sums minus 1. For v=0 it contributes 3p-2 to the total absolute kernel sum. For u=0, the quadratic Gauss sums contribute B_p; for u,v!=0 the change t=u²/(4v) gives each t exactly p-1 times, with kernel 2sqrt(p)chi(t)cos(2pi t/p)-1 for p=1 mod4 or the analogous sine for p=3 mod4. The l-infinity convolution norm is p^-2 times the l1 kernel. Riemann sums for |sin|/|cos| give 2p/pi and the signed Legendre-character term has O(sqrt(p)log p) interval cancellation; both branches yield (4/pi)sqrt(p)+O(log p/sqrt(p)). Unit-normalization checks give single-parabola (1+(p-1)sqrt(p))/p and Fourier ratio (2sqrt2/pi)p+O(log p). No composite moduli or arbitrary weights are claimed.

## originality

PASS

Iosevich–Li–Yu study spectral synthesis and exact constants for affine-transitive single paraboloids, whereas the reducible union of opposite parabolas is not an affine-transitive single graph and has an interference-driven idempotent norm. Search aliases projection norm / Fourier algebra norm / Gauss pair did not locate an earlier exact same-set formula. The Gauss evaluation and convolution norm identity are classical ingredients but do not give the explicit union norm and 4/pi limit without calculation.

## value

PASS

The naturally defined union of opposite finite parabolas is a first nontrivial test of cancellation/interference in Fourier spectral projections. Its precise sharp endpoint norm and a universal 4/pi amplification relative to a single graph give a motivated family-wide harmonic-analytic invariant, beyond a routine finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
