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

On polynomials [D,C_s]=(s-1)C_sD and iterating yields (s-1)^k C_sD^k; integration on this core gives the stated orthogonal-output weights. The identity atom contributes zero. Tonelli of the square of each moment gives the geometric-derivative kernel for the Hilbert–Schmidt norm, and 1-st>=max(1-s,1-t) bounds it by one. For an atom at s the norm is 1/(1+s), proving sharpness as s decreases to zero. For the trace iff, Tonelli gives the integral of Phi(s)=(1-s) sum sqrt(j+1)s^j. At s=e^{-h}, h^{3/2} times the sum converges by a Riemann sum with exponential tail to Gamma(3/2); Phi is comparable to (1-s)^(-1/2) near one, and extends with value 1 at zero. For k>=2 the successive-factor comparison reduces to (j+k)^2-(j+k+1)(j+1)=(k-2)j+k^2-k-1>0, proving the claimed weighted binomial estimate from equality at j=0. Summing the negative-binomial generating function cancels (1-s)^k and gives sqrt(k!)rho((0,1)). For an atom, the j=0 term alone tends to sqrt(k!), giving sharpness by squeezing. The l^2 or l^1 bounds give compact bounded extensions from the dense core. Beta integration gives the weights, with consecutive ratio sqrt((j+1)(j+k+1))/(j+alpha+k+1)<1 and decay j^(-alpha-k/2). The p-series criterion proves each stated endpoint exclusion (p>0); it does not assert a sharp p=1 threshold separately for each k>2. Independent bounded checks: 287 weighted-binomial comparisons, 6 atomic norm sums and 930 beta weight ratios, /workspace/branches/spectral_design_replays.js, fockCheck. The frozen checker was inspected, not executed; its rational matrices use the unnormalized monomial basis and its numerical truncations do not prove ideal membership.

## originality

PASS

The moment representation and weighted-shift interpretation are not claimed to be new. The closest inspected exact shift commutator treats a single Cantor measure with unit Hardy shift weights. The operator-ideal results for H_rho itself and the algebra of pairs of weighted shifts do not cover the sharp positive-mixture bounds for its Fock annihilation commutators or their trace endpoint. No exact prior coverage of the hierarchy was found in the bounded comparison.

## value

PASS

The structural regularization is uniform over dilation mass arbitrarily near the identity. B1 may fail to be trace class even while all higher iterates are: the exact half-order boundary moment and the sharp beta examples distinguish the two universal thresholds. The nontrivial part is the sharp nature of the ideal gain and its endpoint mechanism, not the elementary computation of a single shift matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
