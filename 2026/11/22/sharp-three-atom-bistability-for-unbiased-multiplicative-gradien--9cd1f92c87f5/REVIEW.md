# Scientific review

## Correctness — PASS

For nonzero scalar multiplicative oracles the clipped mean field is continuous, odd and piecewise affine, with breakpoint values \(H(c/a_1)=c\mu/a_1\), \(H(c/a_2)=c(s_1p_1+s_2p_2+s_3p_3a_3/a_2)\), and \(H(c/a_3)=cS\). The signs and linearity prove the exact support-minimality and sign-pattern threshold. The explicit oracle has an exact four-branch field, so its equilibrium locations and deterministic mean-map basins are proved without limiting experiments. For genuine clipped SGD, a stopped-square supermartingale and the exact square-summable steps establish the \(1-\pi^2/24\) lower probability of convergence to the wrong stable point. Unclipped SGD is an eventual nonnegative squared-error supermartingale with a vanishing mean. The rational checker tests finite specializations only; the proof handles all required quantifiers. Boundary equality is a touching zero, not falsely called a double simple root.

## Originality — PASS (qualified)

Nekrasova et al. (2026), Appendices H.4 and H.5, give respectively a unique shifted attractor under additive noise and an outward-escaping two-point multiplicative oracle. Koloskova et al. (2023), Section 3.1/Appendix C.5, present additive Bernoulli fixed-point bias. The earlier Faw et al. (2023) oracle is the two-point construction identified by the 2026 paper, and its two-point multiplicative failure is not the balanced inward-field, minimal-three-atom bistability statement. Searches for clipped-gradient multiple equilibria, aliases, signed curvature phase diagrams, and stochastic wrong attractors found no stronger theorem implying the result. This is a best-knowledge novelty judgment, not proof of historical uniqueness; the relevant primary Faw proposition and proof were inspected directly in the 2023 PMLR PDF, although unindexed material remains a priority risk.

## Value — PASS

The result supplies a sharp **minimal stochastic-oracle complexity threshold** separating two-atom inward clipping from three-atom multistability. Its coherent exact five-zero phase diagram makes the pathology visible even though the optimum is locally attracting and the far-field clipped drift is inward; the positive-probability Robbins–Monro wrong-limit theorem shows the phenomenon is not only an expectation-map artifact. The unclipped comparison isolates clipping as the mechanism. The constraints \(\mu,S>0\) and strict atom ordering make this a structural boundary, rather than a routine restatement of generic clipping bias.

## Scientific limitations and closest related literature

The support-minimality classification is restricted to scalar signed multiplicative curvatures and nonzero distinct magnitudes in the three-atom representation. Sampled losses need not each be convex. No complete distribution of the stochastic limit is established. Closest literature: Nekrasova et al. (2026, arXiv:2610.28107, Appendix H.4–H.5); Koloskova et al. (2023, arXiv:2305.01588, Sections 3.1 and C.5); Faw et al. (2023, arXiv:2302.06570, via the two-point example reproduced in the 2026 paper). The source search and full-text access do not eliminate historical-priority risk.

Self-review: passed. Independent audit: not yet performed.
