---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Let u=Av and w=v-mu u. Then u and w are orthogonal and w is nonzero exactly when v is not an eigenvector. The row projections give independent standard Gaussian vectors X=Su/||u|| and Y=Sw/||w||. The inverse quotient is R=mu+sigma Z/||X|| with Z=X^T Y/||X||; conditional on X, Z is standard normal with a law independent of X. Since ||X||^2 is chi-square with s degrees of freedom, this gives the stated Student law for every s>=1. Its continuous density is strictly positive at zero with the given gamma-factor coefficient, and the sign probability is its CDF at zero. For positive t the two tails integrate this density over (0,1/t) and (-1/t,0) respectively. Hence each has coefficient c_s and the two first partial moments diverge; near zero, |R|^{-p} is integrable exactly for p<1 and the remainder contributes finitely. Conditional on ||Su||=r the law is N(mu,||w||^2/r^2); for r in [a,b] the densities have a common finite bound and positive values at zero. The event has positive probability, so the mixture retains the same tail order and moment cutoff, with a generally different coefficient. For w=0 the quotient is identically the positive eigenvalue whenever Su is nonzero, almost surely. The frozen example gives mu=5/17 and sigma=3/17. The uploaded script and recorded output were inspected, not rerun; the quadrature tests window mass rather than proving separate signed asymptotics.

## originality

FAIL

Two distinct indexed results cover the same real-Gaussian one-vector quotient and the exact distribution and tails. The Cauchy-limits record explicitly includes each signed tail and both infinite partial first moments, and adds an independent-average limit. The condition-number record gives the same Gaussian regression conditional on the complete sketched predictor, so the claimed norm-only screening extension follows directly by mixing that conditional law over a compact interval. The October and November archive dates do not establish priority or authorship of the shared result. An earlier primary paper already states the identical reciprocal quotient but the inspected passage uses embedding accuracy, not the Gaussian law or its inverse-moment implications.

## value

PASS

The harmonic projection supplies a natural, practically motivated scalar example where positive definiteness is insufficient for even an existing ordinary mean, and where checking the size of the sketched column cannot eliminate the singular denominator. The precise distribution separates rare pole events from embedding-conditioned accuracy. This structural warning is worthwhile but does not make the equivalent covered theorem a new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
