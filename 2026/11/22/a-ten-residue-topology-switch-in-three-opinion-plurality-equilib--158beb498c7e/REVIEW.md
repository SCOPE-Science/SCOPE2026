# Scientific review

## Correctness — PASS

For all \(n\ge3\), local fixed-point constraints are exactly encoded by a finite, explicitly defined rung transfer, with ordinary and Möbius closures given by ordinary and rail-swap traces. The 36-dimensional antisymmetric characteristic polynomial is verified by the fully reconstructed symbolic integer matrix in `verify.py`; its quartic Newton sums yield the exact infinite family of seam differences. The golden-ratio angular roots and Rouché bound prove the ten-residue signs for all lengths, with exact finite boundary cases. An independent direct graph implementation exhaustively tests all initial opinions for lengths three through six. Scope and lower bound of verification are stated in `VERIFICATION.md`.

## Originality — PASS, with residual historical risk

An exact binary-majority prism/Möbius recurrence exists, but it is not equivalent to the ternary unique-plurality stationary problem and does not yield the mod-ten sign law. Existing randomized plurality consensus work studies different update rules. The fixed states are also exactly pure Nash equilibria of a unit-weight three-color coordination game on these cubic graphs, but the inspected general equilibrium literature does not supply this exact all-length prism/Möbius enumeration or its twist sign law. An earlier finite pentagonal-prism computation already obtains the single length-five prism count, which is credited rather than reclaimed. Specific public-source claim comparisons and remaining historical risks appear in `AUDIT.json`. No directly covering all-length ternary seam formula was identified by the documented searches, but exhaustive world-literature priority is not established.

## Value — PASS

A prism and Möbius ladder differ by only the manner in which the two rails are closed. The exact stationary-state difference is a natural topology-response invariant in a three-opinion local coordination model. Its positive/negative direction reverses with ten distinct length residues, an effect not apparent from either the graph degree profile or the binary two-cycle seam response. The full all-length recurrence and proven sign rule make the result useful as an exact baseline for studying how boundary topology controls multistable local opinion systems, without requiring a downstream theorem about basins.

## Limits and close literature

The theorem enumerates fixed states, not complete recurrent periods or attraction probabilities. Relevant comparisons include Becchetti et al., arXiv:1310.2858; Benjamini et al., arXiv:1405.2486; Apt et al., arXiv:1501.07388; and the public binary-majority prism/Möbius seam census cited in `RESULT.md`. The 2021 two-choice anti-coordination Nash-equilibrium enumeration on circular ladders was separately inspected; it does not cover the named three-choice coordination equilibrium or its Möbius comparison. Further independently indexed equivalent formulas remain possible.

Self-review: passed. Independent audit: not yet performed.
