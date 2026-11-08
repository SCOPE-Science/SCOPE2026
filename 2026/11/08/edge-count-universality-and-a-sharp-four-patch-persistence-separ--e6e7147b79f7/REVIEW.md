# Scientific review

## Correctness — PASS

The contact-process finite-state generator is exactly reconstructed in equation (1) of RESULT.md, with full occupancy as the starting configuration and the empty state absorbing. `verification.py` independently builds the symbolic transition matrix and a separate exact-rational Taylor recursion. The all-rate polynomial inequality is proved by positive coefficients and positive denominator factors, not sampled rates. The general low-rate link formula follows from a pure-death martingale perturbation interpretation; the second-order motif form follows from vertex permutation invariance of the double generator insertion. No larger-tree extremal statement is made.

## Originality — PASS with priority uncertainty

Mountford et al. (2012, arXiv:1203.2972v1) study asymptotic survival on growing graphs; van de Bovenkamp and Van Mieghem (2015, doi:10.1103/PhysRevE.92.032806) compute exact star and complete lifetimes and compare 64-node path/star numerically under different normalizations. Cator and Van Mieghem (2013, doi:10.1103/PhysRevE.87.012811) study modified metastable star/complete dynamics. None of the inspected material implies the same-link-budget four-site star–path strict inequality for *every* positive per-edge rate plus the graph-wide first- and second-order motif hierarchy. Standard linear-system methods and qualitative star versus path comparisons are acknowledged prior work. Unindexed historical small-graph tables and inaccessible full text remain priority risks.

## Value — PASS

The motivated object is expected time to total vacancy of a finite patch network under a fixed number of habitat links. The proved first-order edge-budget universality and second-order motif entry explain exactly when link placement, as opposed to link quantity, can influence persistence. The complete all-rate separation on the first competing four-patch trees supplies a benchmark for topology-sensitive small-network reliability. This is not a field-data extrapolation.

## Boundaries and unperformed assessment

General positive colonization rates are included only for the four-patch star–path comparison. Other starting states, heterogeneous clocks, and larger-graph extremal inequalities are not addressed. Publication priority remains subject to further human literature review.

Self-review: passed. Independent audit: not yet performed.
