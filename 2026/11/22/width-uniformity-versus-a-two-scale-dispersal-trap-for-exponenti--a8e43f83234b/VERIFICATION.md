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

The objective integrates the one-sided exponential density over the habitat union, with endpoints immaterial. At equal widths, rescaling gives F(t)=(1−e^(−t))e^(−αt)(1+e^(−δt)), with α>0 and δ≥1. Its log-curvature is −1/(4 sinh²(t/2))+δ²/(4 cosh²(δt/2)), strictly negative since cosh(δx)>sinh(δx)≥δ sinh(x) for x>0. The log derivative tends to +∞ and −α at the respective ends, proving unique maximization, also at contact. At scaled widths and L>2 the derivative has four distinct exponential terms. Dividing by the slowest exponential and applying Rolle inductively gives at most three distinct real zeros. For L≥9 the derivative signs at 0,1/L,1/2,log 2 are +,−,+,−. In particular g''<−2 on [0,1/9], and (e−2)/e²>3/32 gives the negative sign at 1/L; the upper bound 1−2/L−3L/32 is −19/288 at 9 and decreases thereafter. At 1/2 use 2/e−e^(−1/2)>129/1100 and Le^(−L/2)≤9e^(−9/2)<11/100. The latter comparisons follow from 27/10<e<11/4 (the exponential series suffices) and exact rational squared inequalities. The three critical points are therefore strict extrema in alternating order. For the right maximum t₃, the test point t₃/L increases the objective by g(t₃/L)−g(Lt₃)>0: the first term is greater than 1/(4L) using 1/2<t₃<log 2, and the second is smaller than e^(−L/2)<1/(4L). Since the positive objective vanishes at both ends, this leaves the first maximum uniquely global. At L=2 the two intervals form one and the derivative has its sole zero at log(4)/3.

## originality

PASS

The supported distinction is an exact two-band theorem for the one-sided exponential rate objective: all-separation strict log-concavity at equal widths versus a uniform L≥9 two-peak guarantee and a strict global ordering at scaled widths. Neither general exponential-polynomial root bounds, related Gaussian scale optimization nor evolutionary landscape studies supply this exact conjunction. No priority is claimed for the zero-counting method or the qualitative possibility of fitness valleys.

## value

PASS

For a fixed minimal habitat geometry the theorem separates two effects: increasing gaps alone between two equal-width windows cannot make local optima compete, while scaled unequal windows can produce a persistent suboptimal peak separated by a valley. The contrast is uniform on all admissible equal separations and on a continuous sufficient regime of scaled separations, and the result says which peak wins rather than just exhibiting a plot or bounding the number of possible extrema. This gives a useful analytic benchmark for richer models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
