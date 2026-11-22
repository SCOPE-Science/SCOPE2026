# Mathematical review

## Correctness — PASS

The exact differentiation and unitary conjugation reduce the three-node Fourier Gram tangent to a real symmetric matrix plus traceless diagonal. Near-minimizer compactness justifies passing from positive finite-step weights to the tangent minimax. A fixed all-ones Rayleigh vector gives the operator lower bound, and equality uniquely forces row-balanced weights. The balanced characteristic polynomial yields the exact closed phase interval. Independent convex symmetrization reduces the half-spread minimization to one variable; its monotone branches meet at the sharp solution. The two-node argument and all numerical constants follow from exact eigenvalues. The bundled algebraic checker passes. Finite checks supplement, and do not replace, the analytic proof.

## Originality — PASS (same-model, historically qualified)

Wind-Andersen's 2026 paper [1] explicitly establishes Frobenius first-order orthogonality at square DFTs and, in Section 8.3, already supplies a four-node example of spectral improvement, which is duly credited rather than claimed anew. Its proof does not give the operator-norm Rayleigh saturation window, its exact three-node threshold, or the two opposing exact minimax corrections. Kircheis–Potts [2] optimize other density-compensation objectives and perturbed-node interpolation [3] addresses stability, rather than this fixed-grid minimax. Targeted searches of the mathematical findings database for three-node Fourier spectral scaling, phase transitions, and aliases returned related Fourier quadrature, spectral conditioning and positivity results but no implication of the combined theorem. This does not exclude unindexed specialist literature or independent earlier proofs.

## Value — PASS

For numerical Fourier inversion, worst-case distortion depends on the full singular spectrum rather than average squared Gram error. The theorem identifies the **minimal** grid where a Frobenius-optimal weight can be strictly suboptimal in two worst-case spectral metrics, gives their conflicting remedies, and determines the precise node-velocity interval in which the best operator error is fixed by an invariant Rayleigh direction. This sharp phase diagram and explicit condition-number proxy can benchmark density-compensation optimizers. Its first-order, three-node scope is deliberately limited; no general reconstruction-rate guarantee follows.

## Closest literature and remaining risks

[1] Wind-Andersen (2026), Sections 7 and 8.3, https://arxiv.org/html/2611.02379v1 — closest direct parent, including prior four-node spectral example.

[2] Kircheis–Potts (2023), Section 2, https://arxiv.org/html/2304.00094v2 — exact/least-squares density compensation, different spectral objective.

[3] Austin–Trefethen (2017), https://arxiv.org/abs/1612.04018 — perturbed-point interpolation and quadrature.

Limits include fixed frequency set, first-order asymptotics, partial optimization outside the sharp interval and incomplete historical exhaustiveness.

Self-review: passed. Independent audit: not yet performed.
