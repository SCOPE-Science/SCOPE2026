# Review of the centered-star maximal-function perturbation theorem

## Correctness — PASS

The theorem concerns nonnegative inputs and explicitly distinguishes the absolute-value maximal operator on signed inputs. In edge coordinates the centered maximal function is the finite maximum-of-linear-forms map \(F_i(x)=\max\{x_i,x_i/2,\mu\}-\max\{0,\mu\}\), with \(\mu=\sum_jx_j/(m+1)\). All differentiability cells have explicitly bounded \(\ell_1\) Jacobian column sums. The negative-mean case needs the crucial fact that at most \(m-1\) leaves select the global mean; its contradiction proof holds for every integer \(m\ge2\). Continuity of a finite piecewise-affine map extends cellwise bounds globally. Explicit positive inputs attain the constant; the two-vertex case is handled separately. An explicit signed sequence gives a divergent quotient. The standalone exact-rational tests passed, but are not substituted for the universal proof.

## Originality — PASS (qualified)

The foundational 2014 paper determines vertex \(\ell_p\) bounds for finite-graph maximal operators, whereas the present target is a two-input graph-edge BV stability constant. González-Riquelme–Madrid's 2020 work gives a sharp *one-input* star variation contraction and a qualitative continuity theorem for general data, neither of which yields the sharp difference estimate. Their 2020 sequel and the 2026 general-graph variational paper likewise concern single-input or vertex-norm constants. The available abstract for Liu–Xue concerns one-input variation and continuity; its full text was not examined. The prior comparison searches found no explicit identical or stronger two-input formula. Risks: the exact piecewise-affine calculation could be implicit in unindexed special cases or continuity proofs; absence from index searches does not establish historical priority.

## Value — PASS

The two-input modulus is the natural robustness constant for a nonlinear maximal filter measured in discrete BV. It differs sharply from the known single-input variation-diminishing constant: the optimal perturbation factor for \(m\ge2\) is exactly twice that factor, increasing toward \(2\). Explicit attaining input pairs give a concrete instability mechanism. The signed-domain infinite-modulus boundary is not a standalone trivial result: it explains why the nonnegative restriction is indispensable and aligns with published continuity restrictions. The result covers every star order, including the singular two-vertex case.

## Remaining limits

No classification of all extremizing pairs is asserted. No generalization to weighted, fractional or uncentered maximal operators is claimed. Historical-priority certainty is limited by incomplete inspection of the Liu–Xue full text and possible alternate nonlinear-map formulations.

Self-review: passed. Independent audit: not yet performed.
