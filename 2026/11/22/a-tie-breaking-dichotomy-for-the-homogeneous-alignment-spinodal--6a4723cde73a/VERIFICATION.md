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

For the explicitly defined, occupied-center iid-neighbor dynamics the symmetric point is fixed, and the orientation-permutation-equivariant derivative is scalar on the two-dimensional tangent space. Conditional on m occupied sites I re-enumerated the derivatives without multinomial weights: fix one position first to heading 1 and then to heading 2, average the difference of each event indicator over the 3^(m−1) other words, and sum over the differentiated positions. For the tied-and-central-1 event the center derivative and each neighbor derivative are treated separately. This gave unique-plurality numerators (1,2,12,36,120,420,1330) and tied-and-central-1 numerators (0,1,0,6,6,30,80), with denominators 3^(m−1). Binomial mixing gives P,T. The scalar derivative of the total tied-event probability is zero by exchange symmetry, so the reorientation derivatives are (1−3η/2)P and (1−3η/2)P+(1−η)T. The flow subtracts 1 from each rate. In the representation s=ρ/(1−ρ), the polynomial (1+s)^6(P−1)/s has a negative constant and strictly positive higher coefficients, so there is exactly one positive root; bisection gives ρ*=0.212447606903894 to the displayed precision. For I, the first two binomial-mixture entries of a_m+b_m are 1 and every subsequent entry exceeds 1. Thus P+T−1>0 at all 0<ρ≤1 and its leading term comes from two occupied neighbors, 15ρ²·(1/3)=5ρ². The strictly positive slope magnitude 3P/2+T gives a unique threshold in (0,1), asymptotic to (10/3)ρ². At ρ=1, P=1330/729 and T=80/729 give 601/1995 and 681/2075; at ρ=ρ*,η=0 the random-tie rate is exactly zero, not strictly stable. These checks establish the intrinsic closures defined in the frozen record, independently of the spatial paper's notation or dynamics.

## originality

PASS

The two response kernels are already motivated and specified in different parts of the same model paper: uniform ties in the simulation algorithm and η-dependent incumbent transfers in the mean-field equation. The incumbent derivative is consequently obtainable by taking the properly normalized homogeneous independent-neighbor derivative of that kernel; it is not an independent new update rule or a different physical model. The distinct checked contribution is the explicit paired six-neighbor growth-rate formulas and the all-density sign contrast, including the exact random-tie cutoff and the incumbent low-density scale. No distinct exact or dominating statement covering that comparison was verified.

## value

PASS

In the same motivated homogeneous closure a change only on tied configurations changes whether dilute spontaneous alignment is linearly possible at zero noise. The negative first-density correction of R cancels for I, and the first positive alignment term for I comes from exactly two occupied neighbors; this yields a quadratic noise scale and explains why the qualitative phase portrait of the orientation modes differs. The exact all-density inequalities and threshold are stronger than a numerical comparison, without implying any spatial phase boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
