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

The nonnegative fundamental Hermite–Fejer basis h_k=T_n(x)^2(1-xx_k)/(n^2(x-x_k)^2) partitions unity, making every BV output a linear combination of step responses F_m. BV seminorm is exactly the maximum Var(F_m), attained by a one-jump input. All n nodal derivative zeros plus one interior extremum in each of the n-2 equal-label gaps exhaust deg F_m<=2n-2 derivative, proving the exact variation accounting. The angular kernel splits into direct and reflected csc^2 terms; reflected double sums stay uniformly bounded and direct tails give <=(2/pi^2)(log m+log(n-m))+O(1). Evaluating central-step gaps at angles j*pi/n yields both harmonic lower tails and 4/pi^2 log n+O(1). Independent numerical optimization for n=8,16,32,64 produced 1.8685,2.1509,2.4323,2.7134 respectively, consistent with the logarithmic slope (the additive constant persists).

## originality

PASS

Classical Hermite–Fejer positivity and BV input pointwise approximation-rate estimates do not determine the output BV seminorm. The 1990 Al-Jarrah–Rababah article Theorems 1–2 address pointwise |H_nf(x)-f(x)| for f continuous at x, not variation over the output interval; its Jacobi parameter family does not dominate this new operator norm. Best-of-knowledge original with older-source priority risk.

## value

PASS

This establishes that a positive L-infinity-contractive polynomial interpolation operator can nonetheless amplify bounded variation without bound, and quantifies the exact sharp leading constant. It isolates central single-jump extremizers and a natural BV stability invariant needed in oscillation-aware approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
