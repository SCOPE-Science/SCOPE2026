# Mathematical review

## Correctness

PASS. For a nontrivial conference strongly regular graph with \(v\equiv5\pmod8\), the binary reduction of the standard common-neighbor identity is \(A^2=A+I+J\). The one-site update \(B=A+ee^{\mathsf T}\) satisfies \(B^3+I=ww^{\mathsf T}+uu^{\mathsf T}\), where \(u=Ae\) and \(w=\mathbf1+e\). The vectors are independent and mutually orthogonal under the ordinary characteristic-two bilinear form, so this defect matrix has rank two and square zero. This proves \(B^6=I\) for every admissible graph and characteristic-two finite field. The fixed-point calculation gives a one-dimensional fixed space; the restriction to \(\operatorname{span}(u,w)\) rules out primitive period two. Its third-iterate fixed space has dimension \(v-2\). These steps prove the exact orbit counts without extrapolating finite experiments. Separate matrix and direct-state computations agreed at the tested sizes. A wrong graph parameter parity or changing the state-field characteristic would invalidate the proof; those conditions are explicit.

## Originality

PASS on the inspected evidence, subject to historical-priority uncertainty. The closest strongly regular graph code literature proves the unperturbed identity and rank but does not state a rank-one diagonal perturbation orbit classification. The closest indexed one-site feedback theorem is for Boolean cubes: it shares the intervention but its base operator satisfies a different identity and its temporal populations are incompatible with the present conference theorem. A reversible two-time-layer strongly regular wave classification uses an invertible operator on doubled configuration space, and so does not imply the first-order one-site result. Generalized Paley papers establish graph construction, parameters and automorphisms rather than the new nilpotent rank-two identity. Exact all-size equivalent reformulations in unindexed work cannot be ruled out, and a visual rendering of one older open-access PDF was not accessible; extracted full-text sections were examined.

## Value

PASS. The result identifies a uniform dynamical transition caused by a single vertex-local feedback change on an infinite, canonical strongly regular graph class: the unmodified binary update has a nontrivial transient sector, whereas the modified update is globally reversible with exact six-step clock. The exact counts of all three allowed least periods are not merely a small example or a known parameter substitution; the proof isolates the rank-two square-zero mechanism governing every graph in the parameter class, over all characteristic-two extension fields. The result supplies a structural benchmark for feedback sensitivity of finite linear graph automata. It does not claim arbitrary feedback configurations, other congruence classes, or independent priority certification.

## Closest literature and limits

The unperturbed binary code identity appears in Haemers, Peeters and van Rijckevorsel, *Binary Codes of Strongly Regular Graphs* (1999), Proposition 3.1; Paley graph background appears in Lim and Praeger, *On generalised Paley graphs and their automorphism groups* (arXiv:math/0605252, first public preprint 2006-05-10). The finite check programs enumerate only selected prime-order examples; the algebraic proof covers the full graph and field scope. Unindexed historical equivalents and lack of independent external validation are residual risks.

Self-review: passed. Independent audit: not yet performed.
