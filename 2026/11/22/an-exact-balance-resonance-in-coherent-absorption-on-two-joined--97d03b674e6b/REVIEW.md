# Self-review

## Correctness — PASS
For integers \(m,n\ge3\) with internal clique weights one, bridge weight \(t>0\), and nonbridge trap rate \(\kappa>0\), the proof reduces eventual absorption to the orthogonal projection onto the trap's graph-Laplacian cyclic subspace. The displayed five-class quotient is invariant and has exact Krylov determinant \(-mt^3(m-n)\). Off balance this proves rank five. At balance the rank is four, with a one-dimensional trap-orthogonal eigenmode of norm \(Q=2+1/(m-2)+1/(m-1)\). The projector then yields all sitewise probabilities, including the bridge-site transition from \(1-1/Q\) to exactly \(1\). The exact-rational full-graph checker independently confirms all formulas in 100 parameter instances. Such finite checks supplement the symbolic all-size argument and cannot alone prove it.

## Originality — PASS on examined evidence
Novo et al. (arXiv:1412.7209, 2014) supplied the underlying Krylov approach. Razzoli, Paris and Bordone (*Entropy* 23, 85, 2021, Section 4.3 and Appendix B.3) **already treated equal-size, unweighted-bridge barbell absorption**, deriving a four-dimensional reduced model; the present balanced formula is not claimed as a novelty. Duda and Wong (arXiv:2408.08244, 2024) studied weighted-barbell spatial search using an oracle, rather than local irreversible absorption. Literature and exact-index searches by aliases, broad containment, and reductions found no published result for the all-positive-weight, all-integer **unequal-size** case and its loss-free eigenmode disappearing exactly at balance. An unlocated equivalent theorem or prior finite parameter computation remains possible. Search failure does not prove historical uniqueness.

## Mathematical value — PASS
Two dense communities joined by one bridge are a natural quantum transport testbed. The theorem identifies when structural symmetry creates a perfectly dark mode, explains why an additional single site removes it, and gives complete site-resolved capture probabilities for all sizes and all positive bridge strengths. The bridge-input capture jump persists at arbitrary fixed positive loss and hopping weights, a structural distinction beyond merely executing a general Krylov algorithm.

## Limits and reproducibility
The model uses a finite, single-excitation graph Laplacian with no dephasing or other losses and an absorber at a nonbridge vertex. No statement covers adjacency-Hamiltonian transport, zero bridge conductance, multiple absorbers, or finite-time absorption rates. Run `python3 verify_capture.py` to check full-graph exact-rational small instances; the all-size statement follows from the symbolic quotient proof in `RESULT.md`. See `AUDIT.json` for statement-level prior comparisons and inspected literature.

Self-review: passed. Independent audit: not yet performed.
