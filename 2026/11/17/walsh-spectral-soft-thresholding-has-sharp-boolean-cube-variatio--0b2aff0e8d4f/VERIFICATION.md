---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The nonlinear map is continuous piecewise affine in Walsh coordinates. Every nonconstant active mask A is realized in an open threshold chamber and has derivative the corresponding Walsh projection modulo constants, so integrating along line segments and local witness perturbations proves the nonlinear sharp modulus equals max_A ||P_A||_{V->V}. Graph coarea/layer cake on indicator cuts is exact for any finite graph and P_A annihilates constants. Each P_A commutes with cube coordinate differences; orthogonal l1-l2 projection bounds give V(P_A f)<=sqrt(N)V(f). Random half-mask signs have a Rademacher sum over N/2 frequencies; its second/fourth moments and Hölder give (N-2)/(2 sqrt(6N)) lower bound from a singleton. Omitting the highest parity character gives 2-4/N witness, proving strict expansion for all d>=3. Independent exact rational all-masks/all-cuts enumeration (d=1,2,3) gave 1,1,3/2 with actual local active-chamber attainment; finite witnesses are not the all-d growth proof.

## originality

PASS

Best-of-knowledge originality: Walsh spectral soft thresholding: Boolean-cube edge variation amplification. The particular all-parameter statement is not directly implied by inspected previously published sources. Novelty limitations and primary material not obtained in full are retained below.

## value

PASS

The graph edge-variation modulus is a natural stability quantity for Fourier/Walsh shrinkage. The exact nonlinear mask/cut identification, first expansive cube dimension and exponential dimension dependence contrast with Euclidean nonexpansivity and with maximum-edge Lipschitz spectral projection constants; this is a meaningful sharp structural instability result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
