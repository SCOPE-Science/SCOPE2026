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

Independently eliminated the landmark block: with F the complement, the only nonzero Nyström residual block is ((tI+L)_{FF})^{-1}. For a,b surviving vertices on the two shores, the within-shore contrast eigenvalues are t+n and t+2 with multiplicities a−1,b−1 when both shores remain, and the constant-on-shore block is [[t+n,−b],[−a,t+2]]. This gives residuals R_A=n/(t+2), R_B=1/(t+n)+(n−3)/(t+2)+(2t+n+2)/(t²+(n+2)t+4), and R_C=(n−2)/(t+2)+(2t+n+2)/((t+1)(t+n+1)). Exact subtraction independently reproduces all three numerators (workspace/branches/correctness_checks.py, traces). The signs give A vs C at alpha and A vs B at beta; the quartic has all positive coefficients for n=3 and only its constant negative for n≥4. The sign of n³−8n²+16n−12 is negative at 3,4,5 and positive from 6 onward by monotonicity on [4,∞). Thus for n=4,5 gamma<beta<alpha, and for n≥6 alpha<beta<gamma. This verifies endpoint, optimizer and multiplicity statements including the n=3 exception. Uniform convergence of P_n/n³ on bounded intervals and sign bracketing give gamma→√2. ‘No other ties’ means optimal ties, not all equality points of suboptimal scores. The frozen checker was inspected, not executed.

## originality

PASS

Pass for the exact all-n optimal phase diagram, including the degenerate small shore, sharp n=6 frontier and small-size alternative. The same-day general-biclique record supplies much of the score algebra in broader parameters but its phase theorem and finite-size test are stated for p≥3, and do not give the full p=2 frontier or fallback A/B phase. Credit the shared formula framework without inferring priority from date.

## value

PASS

This exact fixed-budget design example distinguishes a genuine two-transition optimizer from a single-transition optimizer at a sharp size cutoff. It gives every minimizer and tie for the smallest nontrivial shore; the vanishing lower threshold and surviving upper threshold are quantitatively different from the p≥3 limit. The grounded-block calculation alone does not give that frontier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
