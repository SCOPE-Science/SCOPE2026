---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The root component decomposes exactly as 1+Bin(m,p)+Y_L, where P(Y_L>=j)=p^j. Computing E[Y_L] and E[Y_L²] gives the stated polynomial. For m>=3,L>=3 its derivative coefficient signs are +,-,+,-, hence at most three positive roots counted with multiplicity. The correction terms W_L′(3/4)=112−A_L−B_L decrease for L>=14 and satisfy A_14+B_14<75/2; W_L′(2/3)<45. For the stated m interval these and the two endpoint derivatives have signs +,-,+,-, forcing exactly three simple roots. Independently evaluated exact rational polynomial signs for representative m,L, and separately checked Descartes patterns. Finite examples do not prove the infinite parameter bounds.

## originality

PASS

Finite rooted tree percolation, SIR and Cayley-tree cluster distributions have extensive prior theory. The inspected references do not state the rooted-broom variance-versus-p phase portrait. A bimodal size distribution at fixed p does not imply two peaks of variance as p changes; SIR recovery-induced variance excess is a different model, even for a tree.

## value

PASS

The non-unimodal root-outbreak-variance curve on a natural broom family is a motivated finite-tree counterexample, while the three-critical-point structural bound and explicit all-L existence interval give reusable exact boundaries. This is not merely a numerical witness or a claim of smallest possible tree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
