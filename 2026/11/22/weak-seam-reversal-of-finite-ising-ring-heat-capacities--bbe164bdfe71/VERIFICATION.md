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

The empty edge set and full cycle are the only even subgraphs of this zero-field ring. The partition-function ratio therefore yields (C_+−C_−)/k_B=2K² f'' at fixed r, n, with f=atanh(tanh(K)^(n−1) tanh(rK)). For r=1, direct differentiation yields the stated numerator polynomial; multiplying the quadratic-in-j summand by (1−y)^3 cancels interior terms and gives the four endpoint coefficients. The resulting strictly positive factorization applies for every 0<t<1. At K→0, f starts with rK^n. At fixed 0<r<1 write q=e^(−2K), w=e^(−2rK). The even wall sum is 1+O(qw+q²), and the odd sum divided by w is 1+(n−1)q/w+O(q²+q³/w); all the displayed higher orders are o(q/w) and retain that order under the required K derivatives. Hence f'' is asymptotic to −2(n−1)(1−r)² q/w. Continuity gives a crossing. In the crossover scaling q=εe^(−2s), a=w/q→1 uniformly on compact s, analytic even/odd expansion gives the q² coefficient B_n(1)=(n²−1)/6. The logarithmic odd prefactor contributes −2ε²(n−1)a/(n−1+a)^2 to f'', while 16q² B_n(1) is the leading even-order contribution. Differentiation of the analytic remainder and a'=2εa give compact C¹ convergence of ε^−2 f'' to the stated strictly decreasing function; its simple zero gives the constant and local uniqueness. Independent replay: python3 /workspace/branches/independent_replay.py 1, using centered excitation-energy variances in the even and odd wall ensembles; 48 high-temperature, low-temperature, uniform and crossover values matched. This bounded check does not prove the two asymptotic statements.

## originality

PASS

The finite defective-ring partition function and the periodic/antiperiodic heat-capacity framework are prior. The supported distinction is the exact all-size sign at zero field for equal-strength bonds, the high/low-temperature order reversal at any fixed weaker nonzero seam, and especially the evaluated logarithmic crossing window with its constant and local uniqueness. The inspected exact formulas supply the starting point, not a comparison theorem for these derivatives or a result in the joint asymptotic regime.

## value

PASS

Changing frustration at fixed seam magnitude is a direct comparison of thermal fluctuations in a standard finite model. The result identifies an actual boundary between rigid ordering and reversal and gives an explicit singular scale for approaching that boundary. This resolves information not available from simply giving partition functions or plotting specific heat, and the sharp coefficient and local uniqueness are usable benchmarks for finite-ring analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
