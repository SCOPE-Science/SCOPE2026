# Scientific review

## Correctness

**PASS.** The complete map on all \(3^{12}=531441\) labelled states was enumerated. The C++ functional-graph indegree elimination and separately structured Python memoized trajectory classification agree on every one of the 52 joint transient-period classes. Exact cycle counts are periods 1, 3, 4, 7, 10, 11 with 1, 4768, 294, 1012, 504, 8 cycles respectively. The maximum first-periodic entry is ten updates, attained by 64 inputs: 32 in the period-three basin and 32 in the period-eleven basin. The Python program checks the three-excitations-per-vertex pattern on all eight eleven-cycles and eight explicit graph automorphisms whose action on one eleven-cycle reaches all eight eleven-cycles. Directly replayable codes and captured outputs are supplied. Full enumeration, not a partial simulation, supports the finite conclusion.

## Originality

**PASS, qualified.** Gravner–Lyu–Sivakoff's general Theorem 3 concerns conservative initial cycle integrals and asymptotic excitation activity; Doba's complete article gives the maximum cycle-density criterion and reports an eleven-period trajectory for a **different graph**. Hence the occurrence of an eleven-cycle in an excitable network, the update rule, and broad finite-graph activity criteria are prior art. Neither inspected primary work gives the exact Chvátal temporal orbit counts, the transitive automorphism orbit of its eight period-eleven cycles, or the class-by-class entry times. The static Chvátal-graph table counts Hamiltonian cycles, not GHCA temporal cycles. Searches for graph-name, parameter, and equivalent dynamical formulations did not identify the exact census. An unindexed earlier equivalent remains possible.

## Mathematical value

**PASS.** The Chvátal graph is a canonical small extremal graph of chromatic number four without triangles; exact excitation behavior tests how its nontrivial cycle structure supports recurrent waves. The equality of all eight eleven-cycles modulo graph symmetry is structural information beyond a numeric orbit count, and the two-period split of maximally delayed initial states is a distinguished basin-boundary phenomenon. The result is limited to this one graph but supplies a complete, reproducible dynamical benchmark, not a textbook deduction or a known-table recomputation.

## Boundaries and literature

The conclusion is a computer-assisted fixed-graph classification. No inference is made about universal chromatic thresholds or every 4-regular graph. Model first-posting evidence: arXiv:1610.07320v1, 2016-10-24. Closest full-text comparisons: Gravner, Lyu and Sivakoff, *Annals of Applied Probability* 28 (2018), pp.3324–3357; Doba, *Complex Systems* 27 (2018), pp.101–126. Graph identity: Chvátal (1970) and the MathWorld graph entry. The original 1970 article was not inspected in full, and global historical novelty cannot be guaranteed. Independent human or external validation was not performed.

Self-review: passed. Independent audit: not yet performed.
