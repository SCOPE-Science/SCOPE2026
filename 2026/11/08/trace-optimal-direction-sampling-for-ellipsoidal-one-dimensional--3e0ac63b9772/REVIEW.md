# Scientific review

## Correctness — PASS
The objective is explicitly the one-dimensional ellipsoidal alignment mean with a gradient selected before an independent direction. The alignment-matrix representation, \(\operatorname{tr}(SM)=1\), the exact equality case, and the Haar tilt construction give an analytic proof of the universal upper bound and attainment for all real SPD shapes. The strict sampling comparison follows from sign symmetry and a coordinate swap identity. A circle-integral identity gives the planar power family and unique exponent. The packaged standard-library checker passes 622 structured exact and numerical checks. These checks corroborate, rather than stand in for, the analytic proof.

## Originality — PASS, with historical-priority risk
The source's Sections 2.2 and 3.4 supply the alignment statistic and analyze Haar and inverse-square-root metric-guided sampling, including the metric-guided mean. They neither optimize worst-gradient means among arbitrary direction distributions nor derive this trace-tilted full-support sampler and the planar opposite-power identity. The earlier randomized-subspace work [2,3] treats coordinate sampling and probabilistic descent under distinct formulations. Classical E-optimal experimental design is conceptually close: the elementary trace bound and eigenvector-weighted distribution should not be presented as independently novel. No covering statement of the *combined exact alignment classification* was identified in the inspected sources or mathematical-record searches. An equivalent unindexed optimal-design derivation remains a material priority risk.

## Value — PASS
In the new ellipsoidal trust-region geometry, the direction law changes how far a one-dimensional section reaches along a gradient, so a sharp worst-direction mean is an intrinsic robustness measure. The theorem specifies the exact attainable design, a full-support implementable sampler with cost, and a strict benchmark ordering of the paper's two stated sampling choices, with a potentially nearly dimension-fold improvement in this narrow metric. The planar power-family uniqueness shows how to attain the optimum without rejection in a natural low-dimensional setting. These are mathematical geometry-of-sampling results, not claims about whole-algorithm iteration complexity.

## Closest literature and boundaries
Chen and Xie (2026, arXiv:2610.24866), Sections 2.2/3.4; Chen, Hu and Wu (2020, arXiv:2006.06589), Sections 2/4; Roberts and Royer (2023, arXiv:2204.01275), Section 3; and classical E-optimal-design connections including Dereziński and collaborators (2019, arXiv:1902.00995). The statistic is a mean, not a high-probability event; smooth metric normalization and rejection costs are shape-dependent. Only one-dimensional subspaces and an exact planar power-family identification are asserted. Historical priority and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
