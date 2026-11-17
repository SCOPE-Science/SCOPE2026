---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

F(x)=(x²-6x+12)/(x²+6x+12) has positive denominator for x≥0. Exact rational C3,C4,C5 entries have positive numerators; independently checked via exact matrix inversion. The cycle pseudoinverse nearest-neighbor entry (n-1)(n-5)/(12n) yields T_n(h)_{0,1}=-(n-1)(n-5)/(nh)+O_n(h^-2), strictly negative for large h when n≥6. At h=8 exact C6 entry is -6584/580537. For n≥7 source proves a uniform Fourier periodization tail <0.071 versus first Fourier coefficient <-0.086 using rational enclosures |r|<0.54, which proves negativity at fixed h=8 for all sizes; independent direct rational checks for C7..C10 corroborate, not replace, infinite analytic bound.

## originality

FAIL

The exact main all-n all-h positivity iff n≤5 and nearest-neighbor large-h asymptotic are already proved in October25 and another November8 primary mathematical publication. The previous publication even gives the same C6 rational h=8 witness. The submitted uniform h=8 extension for n≥7 is not stated in those earlier texts, but is a nonsharp auxiliary strengthening of a fully covered main theorem, not accepted as the original whole claim.

## value

FAIL

The all-cycle sharp order frontier and nearest-neighbor sign law were completely established earlier. The only distinctive extra fixed timestep h=8 is not claimed optimal and is a convenient non-sharp common certificate; without a motivated minimal threshold or additional natural invariant, it does not support original mathematical value at the level of the complete submitted main classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
