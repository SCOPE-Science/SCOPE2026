# Self-review

## Correctness — PASS

The claim has a precisely quantified domain: one deterministic time \(x\in[0,1]\), one full real noiseless Brownian state observation, a fixed zero-start Brownian prior, occupation fraction \(Q=\int_0^1\mathbf1_{\{B_t>0\}}dt\), and squared-error Bayes risk. The exact Gaussian sign identity yields a double-integral expression for captured variance. The logarithmic-time change of variables is valid for all interior times; its integrable singularity permits differentiation and produces \(dV(e^{-r})/dr=e^{-2r}(C-G(r))/\pi\). The explicitly evaluated \(C>0\) and strictly increasing unbounded \(G\) prove one and only one global time maximizer, including both boundary times. The exact antiderivative gives the claimed risk, and the separate convergent arcsine series supplies a reproducible check with a uniform tail bound. The standalone verifier was executed successfully on the packaged calculations. No finite scan is used as an infinite proof.

## Originality — PASS, qualified

The closest inspected primary sources were Altmeyer (2017), Ivanovs–Podolskij (2020), Altmeyer–Le Guével (2021), and Cui–Chronopoulou (2023). The first three analyze occupation-functional estimation from fixed regular, typically increasingly dense, observation grids; they do not prove an optimal *freely chosen single observation time* for the nonlinear Brownian sign occupation functional. The fourth optimizes state-path recovery rather than occupation-time conditional risk; even Brownian state-reconstruction sampling at the midpoint does not imply the present off-midpoint optimizer. Related prior published claims concern endpoint linear covariance with sojourn times or randomized sign-function quadrature, neither implying the variance of the full conditional-mean estimate as the observation time changes. This is a statement-and-implication comparison, not a novelty inference merely from different titles. The classical Brownian arcsine law and Gaussian orthant identity are admitted prior tools; the terminal observation special case is not asserted novel.

An equivalent theorem could reside in unindexed occupation/sensor-design literature; accessible primary full texts and available published claims were checked but independent priority confirmation has not been performed. The conclusion is scientific best knowledge, not certification of uniqueness in the literature.

## Value — PASS

A positive occupation fraction is a standard nonlinear discontinuous functional of Brownian paths. With only one full state reading, its optimal sampling location is genuinely different from the endpoint and the state-path reconstruction midpoint. The exact unique optimum \(0.589585110907\ldots\), closed Bayes-risk law, and comparison (about \(79.57\%\) versus \(61.37\%\) of total occupation variance captured by the best versus terminal snapshot) answer an actionable sparse quadrature design problem, rather than a mere normalization check or known-table recomputation. The theorem does not make an application claim beyond the stated information model.

## Scope and remaining scientific risks

The proof depends on the zero-start Brownian log-time sign-correlation kernel. General kernels, noise, adaptive sampling, multiple snapshots, nonzero thresholds, and weighted occupation times are unproved. Several related articles were inspected in their accessible full text, but publication priority could change with an obscure equivalent historical theorem. Numerical verification is not independent audit.

Self-review: passed. Independent audit: not yet performed.
