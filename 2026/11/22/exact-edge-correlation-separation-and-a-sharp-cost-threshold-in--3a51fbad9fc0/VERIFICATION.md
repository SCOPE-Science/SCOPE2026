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

# Reproduction and scope

With Python 3 and SymPy 1.12 or newer, execute `python checker.py` from the directory containing this document and the checker. The program reconstructs donation-game payoffs on all sixteen configurations of the four-cycle, forms both the label-preserving orbit-quotient hitting systems and the full fourteen-transient-state hitting systems, and solves them by exact rational/symbolic linear algebra. It checks the two-parameter zero-cost identity, alternating neutrality, both fixed-parameter positive-cost formulas, the polynomial sign transformation for the unique threshold, the strict comparison between layouts, and an exact positive-cost rational example.

The sign certificate uses the bijection \(c=2t/(1+t)\) between the open intervals \((0,2)\) and \((0,\infty)\), positive coefficients of transformed denominators, and one Descartes sign variation for the crossing numerator. A finite run of numerical fixation simulations would not suffice to establish the theorem. The program does use numerical root approximation only to print a human-readable value; the defining polynomial and unique-root proof are exact.

Assumptions: uniform initial cooperator; no mutation; symmetric edge-specific benefits; two costs per cooperative donor, one per edge; pre-replacement fitness; linear fitness; and strict fitness positivity. These conclusions do not cover arbitrary graph sizes, alternative stochastic update rules or evolving edge games. Historical priority is subject to independent literature review.
