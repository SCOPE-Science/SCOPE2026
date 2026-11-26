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

Direct differentiation with w=−z, r=y/x² and h=wx gives w'=4x, x'=−wrx², r'=1−r+2hr², h'=h²(4/w²−r). The respective signs at w=3, r=1/2, r=2 and h=1/10 are strictly inward (the upper r derivative is at most −1/5 and h'≤−h²/18). On every finite interval x≤x0 and w≤w0+4x0t, so (1/x)'=wr is bounded there and x cannot hit zero. All coordinates stay finite on bounded times, proving forward-global continuation, including boundary initial data. The h bound implies h→0; if w≤W, then x≥1/(1/x0+2Wt) and w'=4x contradicts bounded w. Variation of constants gives r→1 since 2hr²→0. Thus (1/h)'→1, implying th→1, and (w²)'=8h yields w²/(8 log t)→1 by integral comparison. The equivalents follow from x=h/w and y=rx². The allowed set contains an open subset, but includes boundary points. Frozen check.py was inspected, not executed: its line 13 is a no-op, so the claimed automatic check of the lower-r face should not be credited. The exact sign there is 1/2+h/2>0 by the proof, so the flaw does not affect the theorem.

## originality

PASS

The coordinatewise leading physical-time escape theorem is distinct from the inspected earlier equilibrium, compactification and homoclinic results. A separate same-date record demonstrably covers the leading limits and goes further, but its own Relationship to prior work and reference 4 explicitly credit this exact frozen finding, naming its identifier. That is an attributed extension, not evidence the frozen result duplicates an independent antecedent. This assessment does not infer priority from date or claim exhaustive historical precedence.

## value

PASS

The equilibrium-line degeneration raises the natural question whether projected convergence toward the line forces a finite equilibrium limit. The theorem constructs an open basin of forward-global exceptions and gives all three coordinate rates in physical time with universal leading constants. This is a quantitative dynamical distinction not fixed by the equilibrium classification or merely locating a point at infinity. It is not a global basin or sharp trapping-bound claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
