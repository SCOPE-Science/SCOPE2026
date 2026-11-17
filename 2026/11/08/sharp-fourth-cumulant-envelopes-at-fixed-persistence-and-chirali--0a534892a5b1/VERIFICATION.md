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

For an initially uniform angle and Poisson i.i.d. turn increments with first harmonic z and second w, the angular Fourier generator has decay rates a_j=alpha(1-m_j). The second/fourth moment hierarchy yields a linear asymptotic fourth-cumulant rate K=3v^4/alpha^3[Re((1-z)^-2(1-w)^-1)-2 Re((1-z)^-1)Re((1-z)^-2)] for |z|<1,w!=1. All second harmonics obey |w-z²|<=1-|z|², and the entire disk is feasible via two-atom chord laws and mixtures. Inverting 1-w maps the disk to another disk if Im z !=0 or half-plane when Im z=0, and direct affine optimization gives the full stated sharp K intervals, attaining boundary turn laws and sign thresholds. Independent exact rational boundary witnesses for z=i/2 gave K=162/125 and -288/125, with a zero sharp upper bound at z=(1+i)/2; an independent generator-based check corroborated the moment normalizations. Nonrelaxing w=1 and |z|=1 excluded.

## originality

PASS

PASS, qualified: Sevilla 2019 Eq.(54) gives the arbitrary-kernel forward fourth-moment transform, which is an acknowledged essential input. The new constrained inverse design is the exact feasible w-disk at prescribed first z and optimization of the fourth-cumulant coefficient over every angular probability law, including full positive/negative/no-positive phase boundaries and two-angle extremizers. Britton et al 2026 discuss dependence on higher angular modes without the all-law interval; trapped swimming and second-moment diffusion results are different observables. An unindexed global trigonometric-moment extremization might dominate.

## value

PASS

The first angular harmonic fixes the complete velocity covariance and diffusivity, while sharp fourth-cumulant signs differ within that covariance-equivalence class. Exactly identifying all attainable rates, extremal finite-angle controls and chiral no-positive curve is a natural transport-design identifiability and inverse problem, not merely a forward moment computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
