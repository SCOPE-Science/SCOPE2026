---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Replayed RESULT.md:30–67 for the unnormalized Laplacian. A²=(k−μ)I−μA+μJ gives the r,s levels on the orthogonal complement of constants; connectedness gives r<k, and s<0<r. Interpolate e^(−tL²)=αI+βA+γJ. The α coefficient is a convex combination of two positive exponentials and β>0 for t>0; β+γ=[1−α+(v−k)β]/v>0, and diagonal entries are positive by positive definiteness. The nonedge coefficient is (1−h)/v. Each row sums to one, so its absolute sum adds twice the negative mass, exactly the claimed expression; choosing signs of any row attains it, including at t=0 and the threshold. With x=k−r and y=k−s, h′ is a positive factor times (y/x)e^{−(y²−x²)t}−1, proving the unique peak at the displayed time. Since h starts at one and tends to zero, there is exactly one subsequent crossing of one. The nonedge derivative of the kernel is −μ at zero, so h′(0)=vμ and the norm slope is 2(v−k−1)μ=2k(k−1). The inspected supplied script tests three graphs, with exact adjacency checks and floating-point time samples; no execution of that script or formal verification is claimed.

## originality

FAIL

The full sharp transient law, not just eventual positivity, has demonstrable existing coverage. Two distinct broader Resultary records give exactly this norm, peak and sign pattern at fractional exponent 2. The height and degree-only slope require only substitution and differentiation of those statements. Both broader records are cataloged later than the frozen item; this is a judgment of mathematical coverage at review, not an assertion of earlier priority, chronology of discovery, or dependence.

## value

FAIL

The precise bounded-input amplification, peak and time of positivity recovery are naturally motivated quantitative data. But as a separate exact-invariant contribution, this slice supplies no additional mathematical result beyond evaluating the broader norm and cutoff at exponent two and differentiating; the apparent degree-only specialization takes just the standard SRG identities. This is not a finding that the broader transient analysis lacks scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
