---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The reflecting branch imposes the ghost condition p_(L+1)=f p_L. The two stationary roots u,w give B/A=T(w/u)^(−L); summing the branch balance gives rΔ_L=α−βp_1 and hence (1), with the empty-tooth case checked separately by Δ_0=0. Branch-plus-junction balances force a constant junction mass on the ring, giving (3); Δ_L≤b supplies the strong law at each positive r, while the truncated strong law applies to the infinite unreset occupation mean when ρf≥1. For weak r, implicit root differentiation gives q=f+O(r), T∼c/r and b∼(α−β)/r. In the lattice shift about floor(log_q T), both tails are uniformly geometric (ρ for the positive tail, ρq>1 for the negative tail). The phase error is O(r log(1/r)); the limit sum is positive and bounded away from zero and its first harmonic is a nonzero Euler beta integral, so v/r^(1−s) has no phase-independent limit. At ρ=1/f one may omit 1−q^(−L) with error at most b/T=O(1); this is the bound needed in place of the extraneous factor (1−ρ) on frozen line 126. Replacing q by f costs O(1) since the kernel derivative is bounded by L/4 and geometric L has finite mean. The sum of (f^L+T)^(−1) equals T^(−1)(log_f T+O(1)), and (1−f^(−1))b/T=1+O(r), yielding the full claimed relative O(1/log(c/r)) correction. No numerical phase sample is used to establish nonconstancy.

## originality

PASS

The exact stationary formula, reset-restored drift, and zero-reset threshold are prior results and are not credited as original. The distinct supported result is the singular small-r law for unbounded geometric teeth, including its evaluated, strictly nonconstant amplitude and the exact borderline logarithmic coefficient. The closest prior perturbation formula takes fixed lengths or finite cutoffs and has divergent coefficient moments here.

## value

PASS

This fills a natural singular regime precisely where perturbative reset mobility based on finite moments breaks down. It distinguishes an actually oscillating amplitude from an ordinary regularly varying onset and identifies the sharp logarithmic boundary coefficient. Those sharpen the established statement of positive drift and are meaningful even when the harmonics are too small to resolve numerically.

The dated certificate retains the supplied scientific assessment, sources and limitations.
