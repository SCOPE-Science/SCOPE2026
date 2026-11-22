# Scientific review

## Correctness — PASS

The eigenvalue of the alternating Fourier mode is exactly \(4m^2\), and all resolvent terms commute. The shifted hyperbolic-secant representation follows by direct algebra; its Fourier coefficients follow from the classical Fourier transform of \(\operatorname{sech}\). The exponentially summable Fourier series has alternating coefficients at the two selected phases. The resolvents are strictly positive inverse \(M\)-matrices, yielding strict positivity of all off-diagonal transition entries; a quantified spectral upper bound supplies the diagonal positivity and the conservative CFL margin. A geometric tail bound justifies replacing the finite quadrature by the infinite periodic multiplier. The two explicit integer subsequences generate the required phases. The standalone checker corroborates 98 local identities and finite tests. Risk: numerical constants are approximations of exact infinite series; none is needed as a proof premise.

## Originality — PASS, qualified

The central representational and consistency ingredients have antecedents. The 2026 Bonito–Guermond–Nazarov paper supplies the sinc and CFL method, and the 2015/2017 Bonito–Pasciak literature establishes exponential quadrature error estimates. The novelty asserted here is narrower: an exact two-subsequence *opposite-bias* spectral limit on a naturally refined periodic lumped finite-element grid while the whole step remains entrywise positive and meets the paper's conservative CFL. Direct comparisons of the inspected main results and sinc-error sections do not show that combination. Separate searches for aliases and Mellin/Poisson equivalents were conducted; an earlier unindexed exact treatment of the same periodic multiplier remains a priority risk. The use of Poisson summation alone is not claimed as novel.

## Value — PASS

The question is motivated by the practical distinction between monotonicity and high-frequency spectral fidelity in positive fractional diffusion solvers. It exposes a precise log-spacing obstruction with two computable signed constants, while preserving positivity, mass conservation and the explicit sufficient CFL. The sharp negative result identifies why a mesh-independent logarithmic spacing cannot be justified by monotonicity alone. The example is not asserted to characterize typical convergent quadrature choices: its intentionally fixed \(k=8\) makes the effect substantial.

## Closest literature and limitations

Bonito–Guermond–Nazarov, arXiv:2611.20833v1, Sections 2.2–2.3 and 3.3–3.4; Bonito–Lei–Pasciak, arXiv:1709.06619, Section 3; Bonito–Pasciak, arXiv:1508.05869, Section 7. Their error bounds inform the need to refine the quadrature spacing but do not establish the two explicit CFL-admissible subsequence constants. The theorem is for one-dimensional periodic lumped linear elements, pure diffusion, fixed log spacing and the Nyquist mode. It is not an adverse claim about the appropriately refined high-order scheme.

Self-review: passed. Independent audit: not yet performed.
