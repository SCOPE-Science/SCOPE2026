---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The Bernoulli augmentation coupling K~Bin(n,x), U~Bernoulli(x) takes X=K/n and Y=(K+U)/(n+1). Direct conditioning gives E|X-Y|=2x(1-x)/(n+1). Each path moves from a degree-n trough to an adjacent degree-(n+1) tent peak. The explicit continuous tent spline has slope +1 on [j/n,(j+1)/(n+1)] and -1 on [(j+1)/(n+1),(j+1)/n], so h(Y)-h(X)=|X-Y| on every atom and coupling is W1 optimal by its matching 1-Lipschitz witness. At any interior x all 2(n+1) atoms have positive probability. Equality in the two triangle inequalities forces the same oriented maximal increment on every adjacent interlacing interval; endpoint saturation then forces linearity between knots, giving exactly +/-h plus constants, including n=1. Independent rational arithmetic reconstructed cumulative-distribution W1 for n=1..9 at x=2/5, matching the formula, and source verify_bernstein.py checks 184 rational instances; neither finite check substitutes for the coupling proof.

## originality

FAIL

The result is covered in its principal sharp coefficient and universal extremizer by an already published broader theorem: Sharp centered-cell Bernstein comparison and its parity-dependent minimax constants (Resultary, 2026-11-17), Finding (1) and Proof 1, for arbitrary one-cell jitter laws. Its Section 4 explicitly identifies the Bernoulli law nu_x=(1-x)delta_0+x delta_1 as B_{n+1}, stating the same exact 2x(1-x)/(n+1) discrepancy as a previously established special case. Rigidity of the potential at a single interior x is not separately stated there but follows by the routine equality case of its universal pointwise-sharp coupling for positive Bernoulli weights. The submission offers no independently substantial original remainder. The shared public date does not establish intellectual chronology; rejection is a mathematical coverage judgment, not attribution.

## value

FAIL

The exact coefficient and universal extremizer would be useful if new, but both are explicit special cases of a published general interpolation comparison. The only additional uniqueness phrasing is immediate equality saturation along a finite chain of interlacing grid intervals once all Bernoulli outcomes have positive weights. That routine equality case does not supply a motivated independent gap under the same value standard. Correctness and reproducibility are not novelty or value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
