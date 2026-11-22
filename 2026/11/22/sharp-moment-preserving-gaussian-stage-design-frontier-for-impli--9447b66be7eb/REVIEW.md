# Scientific review

## Correctness — PASS

The claim is a sharp **all-probability-law** minimization statement for a scalar rational amplification function with four fixed moments (including total mass). The proof constructs the two-point Gauss law, an exact cubic Hermite interpolant, and an explicit signed interpolation-error factor. The latter reduces global optimality to positivity of two monotone cubic endpoint factors. Equality is classified, including the critical endpoint case. The converse uses a genuine three-atom moment-preserving perturbation from the inverse-function/implicit-function theorem with an invertible confluent Vandermonde Jacobian. The maximizing stability radius follows from the Gaussian law's exact amplification cubic and strict uniqueness at that radius. The symbolic verifier independently checks the crucial polynomial identities; it supplements, but does not replace, the global argument.

## Originality — PASS, qualified

The original implicit randomized RK2 analysis (Bochacik and Przybyłowicz, arXiv:2404.19059v1, first public 2024-04-29) fixes uniform independent stages and calculates their stability properties. A publicly available theorem titled *Sharp mean-square A-stability for two-point randomized theta integration* treats arbitrary two-point coefficient laws, and its symmetric-case stability inequality already implies the Gaussian two-node real-axis stability cubic. That cubic **alone is prior-covered**. The surviving claim is the exact moment-constrained **optimization over arbitrary Borel laws** and the novel necessity transition at the positive root of \(11r^3+28r^2+6r-12=0\), proved using an exact Hermite-contact sign and a feasible three-atom perturbation. Classical Gauss–Legendre error bounds provide the general interpolation technique, but do not state this rational-objective transition or its distributional stability consequence. No matched stronger published theorem was identified after searches comparing moment constraints, aliases, two-point results, support-size extensions, and implications; this is not a proof of publication priority.

## Value — PASS

Random-stage implicit methods naturally invite stage-law design while retaining low-order stage statistics. Matching moments through degree three is exactly the calibration preserved by two-point Gauss–Legendre sampling; it is not a random parameter slice. The theorem identifies a sharp step-dependent change in whether that canonical design is *globally* optimal, and proves its unique stability-radius optimality against arbitrary-support competitors. A three-atom construction proves the sharp boundary is an actual change of optimizer, not a mere certificate failure. The 22.19% scalar real-axis radius gain against uniform stage sampling is a quantitatively meaningful but narrowly scoped consequence.

## Prior work and limitations

The 2024 preprint's main algorithms and stability section were inspected in available full text. The publicly available two-point randomized-theta theorem was also read in full and its symmetric-case implication was explicitly excluded from the novelty claim. The abstract of Trefethen's 2022 quadrature article and other quadrature-background sources were checked; background techniques and named Gaussian rules are not claimed as new. Remaining risks include older optimal-moment measures or a specialized result establishing the same rational sign transition under different terminology. The result is limited to real-negative scalar test equations and independent stage laws; it does not establish nonlinear order or complex mean-square A-stability.

Self-review: passed. Independent audit: not yet performed.
