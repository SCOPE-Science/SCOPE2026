# Self-review

## Correctness — PASS

The claim is defined for any nonsingular symmetric Hessian of index \(k\) and a fixed SPD metric. The symmetric part of the product of the ideal and approximate orthogonal reflectors is exactly \(I-2(P-Q)^2\). In the absolute-Hessian norm, this yields a contraction with squared coefficient \(1-\eta\mu(2\cos(2\vartheta)-\eta L)\), for every eligible changing projector. A balanced two-dimensional saddle has exactly \(1-2\eta L\cos(2\vartheta)+(\eta L)^2\) squared amplification, establishing both sharp boundaries. The verifier passed exact-rational multi-index and boundary tests; numerical stress checks are not used in place of the proof.

## Originality — PASS, with specified priority risks

Huang et al. (arXiv:2603.25390v2, §5, Theorem 5.2) prove a sufficient small-projector-error condition at a fixed step in the ordinary metric norm, rather than this iff universal quadratic absolute-Hessian energy result. Zhao's regional-reflector Euler theorem proves sufficiently-small-step convergence and explicitly states that it does not optimize the step law. Chu and Lin (DOI 10.1137/24M1710905) study generalized reflector flows and different alignment geometry. Exact-angle and implication searches against published mathematical records yielded no known covering claim, but this is not proof of priority. The arXiv:2611.09049 perturbed-HiSD full text and arXiv:2607.03030 full text were unavailable; their coverage is unresolved and remains a historical-priority risk.

## Value — PASS

The sharp \(45^\circ\) angular safety boundary and simultaneously sharp step ceiling are directly motivated by the cost of inexact negative-eigenspace calculations in saddle search. They give a condition-number-independent *angle feasibility* boundary if the step is adjusted, while the contraction factor still depends on the smallest spectral magnitude. The result concerns one-step and arbitrary-switch energy stability on quadratics, not general nonlinear or metric-norm convergence.

Self-review: passed. Independent audit: not yet performed.
