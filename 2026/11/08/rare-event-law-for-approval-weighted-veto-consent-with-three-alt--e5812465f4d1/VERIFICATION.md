---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and verification

From the directory containing `RESULT.md` and `check.py`, run `python3 check.py` using Python 3.9 or later. The checker uses only the standard library.

The literal implementation enumerates every coalition of disapproving voters and applies the strict AWVC inequality with normalized counting measure on three candidates. For each of the 5,004 anonymous six-ranking histograms with between one and nine voters, it independently compares the literal consent set with the four-count characterization and asserts that at most one candidate survives. It reconstructs exact probabilities by weighting the six-ranking histograms with multinomial coefficients and separately by the collapsed four-class formula. It also checks the \(n=12\) value \(24023/157464\) and the rational lattice-series constant \(14904/121\).

Observed execution: all assertions passed. The executable verifies finite combinatorial identities, not the infinite asymptotics. The unbounded-rate and sharp-leading-constant claims are justified analytically in `RESULT.md` by a likelihood-ratio inequality, a matching feasible type, a multinomial change of measure, mode domination, a summable geometric series and Stirling's formula.

The science is limited to strict uniform rankings with exactly one top-approved candidate per voter, three alternatives for the distributional formulas, and the subsequence \(6\mid n\) for the sharp prefactor. No independent scientific audit or external formal certification was performed.
