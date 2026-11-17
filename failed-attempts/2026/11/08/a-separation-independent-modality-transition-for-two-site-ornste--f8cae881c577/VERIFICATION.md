---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The stationary OU renewal mixture is positive, even, normalized and uniquely invariant by reset coupling. The source-free ODE gives (e^{a x²} p′)′=((r-kappa)/D)e^{a x²}p and p′(0)=0, fixing strict derivative signs on (0,b). Every Gaussian component decreases strictly for x>b; jump at b is -r/(2D). At r=kappa the explicit density a e^{ab²} F_a(max(|x|,b)) solves both ODEs, jump, continuity and normalization. The transformed plateau-mass integral is pointwise increasing and tends to zero/one at separation endpoints. Independent bounded normalization, jump, plateau and monotonicity checks passed. The proof is analytical, not a finite-grid inference.

## originality

FAIL

FAIL: a separately published mathematical record dated 2026-11-08 proves the exact same stationary two-atom model as a special case of symmetric reset measures supported outside a gap, including the complete three-regime global shape and identical critical density. The additional monotone plateau mass is an immediate elementary consequence of that explicit density. Both records share a date; coverage rather than unverified ordering is decisive.

## value

FAIL

FAIL: stationary mode transitions are scientifically meaningful in themselves, but this exact two-atom global phase diagram and plateau density are already supplied by the broader symmetric-gap theorem; the additional monotone plateau-mass observation follows immediately by calculus and does not create an independently useful unknown result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
