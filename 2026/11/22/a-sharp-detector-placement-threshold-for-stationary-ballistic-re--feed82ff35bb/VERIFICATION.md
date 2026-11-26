---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

In equilibrium a flight sampled at a clock time is weighted by its duration L/v. Conditional on its speed the phase is uniform, so X(0) is uniform and independent of the biased speed law ψ(dv)=(φ(dv)/v)/∫φ(du)/u. The two-time binary law is determined by H=P(1,1) and the common one-time marginal (L−a)/L. Given X(0)>a, no reset can occur for t<a/v_+. Integrating X(0)>a+vt yields H(t)=L⁻¹∫(L−a−vt)_+ ψ(dv). Put ℓ=L−a, z=ℓ/t and z₀=ℓv_+/a. Then K(z)=LzH(ℓ/z)/ℓ is the lower stop-loss potential, whose distributional second derivative equals ψ on z>z₀. The unobserved [v_−,z₀] part contributes exactly zM−m there, determined by its mass M and first moment m. Thus the observed restriction and these two moments are necessary and sufficient for pair-law equivalence. At z₀=v_− the only hidden mass is an endpoint atom fixed by normalization; at z₀<v_− none is hidden. When z₀>v_−, choose three nonzero smooth bumps with disjoint compact supports below min(z₀,v_+) and above v_−. There is a nonzero signed combination with both moments zero, and disjointness ensures it is not the zero function. Add and subtract a small multiple from a strictly positive continuous density to obtain different full-support laws with equal data, including when the entire support is hidden. Unbiasing by v and normalizing is bijective. This proves a≥Lv_+/(v_−+v_+) iff identification holds. As an independent replay, take L=1, admissible speeds [1,4], shared ψ-atoms of mass 1/10 at 1 and 4, and distribute the other 4/5 at 7/6 versus 2/5 each at 13/12 and 5/4. At a=3/4 the differing atoms are all below z₀=4/3 and have matched mass and mean, so all short-lag data agree. At a=4/5 and t=6/35 the second law gives H greater by exactly 1/175. The equilibrium construction applies even to deterministic or lattice flight times; the theorem is not a fresh-start convergence claim. The supplied exact-rational script was inspected but not run.

## originality

PASS

The ballistic equilibrium marginal, renewal length bias, residual-survival identity and stop-loss inversion are known components. The supportable increment is the finite-window equivalence class for this binary spatial observation and the sharp detector cutoff, including critical atoms and smooth full-support ambiguity below it. The closest full-text and catalogue comparisons do not give or cover that inverse criterion; priority remains best-of-knowledge only.

## value

PASS

Every speed law has the same stationary spatial marginal, so even a perfect spatial histogram cannot identify the kinetics. One binary detector at short lags can instead identify the entire law exactly above a quantitative placement boundary; below it the theorem tells precisely what is and is not learned. This gives a useful sensor design criterion, not merely a transform evaluation, with no promise of stable noisy inversion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
