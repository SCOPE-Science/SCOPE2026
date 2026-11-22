# Scientific review

## Correctness — PASS

The observation covariance is \(\begin{pmatrix}1+\eta&r\\r&1+\eta\end{pmatrix}\), which is positive definite because \(\eta>0\). Direct integration gives the exact squared-kernel Gram entries, and Gaussian conditioning gives integrated posterior risk as one minus a rational information function. The coefficient of \(\cosh(2\alpha(c-1/2))\) is strictly negative at every permitted half-separation, establishing global midpoint centering. Exact inward derivative signs at both separation endpoints establish strict separation and strict interiority for all positive parameters. Uniform derivative control and the implicit function theorem establish high-noise uniqueness, the location coefficient, and the cubic inverse-noise regret. The included checker independently evaluates 42 symbolic/numerical assertions; the proof, not sampled checks, establishes continuum assertions.

## Originality — PASS on inspected literature, qualified

Ji and Müller, *Optimal Designs for Longitudinal and Functional Data* (arXiv:1604.05375v1, 2016, Sections 1–2, 8, and supplementary discussion) derives the general noisy trajectory recovery criterion; it does not give the exact stationary exponential two-sample optimum or its \(\eta^{-1}\) separation and \(\eta^{-3}\) regret. Baran, Sikolya and Stehlík (2013, doi:10.1016/j.spl.2013.03.003) treat a two-dimensional Ornstein–Uhlenbeck sheet with ordered distinct observations and an unknown trend, not independent measurement-error replication or the claimed law. The Kriging paper by Baldi Antognini and Zagoraiou (2010, doi:10.1016/j.jspi.2010.03.027) directly concerns exponential covariance and IMSPE, but its accessible abstract specifies deterministic computer simulations and ordinary Kriging; **full text was unavailable**, so absence of the present theorem there cannot be certified. Mukherjee's 2001 dissertation, *Optimal designs for estimating the path of a stochastic process*, reports exact OU noiseless path-design conditions in its accessible abstract, but the dissertation text was inaccessible and is a priority risk. Closest indexed mathematical results include OU Bayesian quadrature for the **variance of an integral** (rather than the integral of variance), a cosine-kernel noisy two-landmark theorem on a circle, and exponential-kernel interpolation-matrix conditioning. None of their accessible claim statements imply the present precise noisy OU path theorem. No uniqueness of priority or full-literature exhaustion is asserted.

## Value — PASS

The all-noise structural theorem resolves whether two independent noisy measurements should be collocated or placed at the boundaries, for a fundamental stationary Markov covariance. The new leading constants quantify how the best separated design departs from the best replicated design as independent noise grows. This gives a concrete benchmark for continuous-time trajectory reconstruction, with nontrivial behavior hidden beyond the leading order of the high-noise information criterion. The gain is \(O_\alpha(\eta^{-3})\), so its practical importance is model and noise dependent; the contribution is an exact structural and asymptotic boundary result rather than a claimed universal engineering improvement.

## Closest sources and limitations

- Ji and Müller (2016), https://arxiv.org/html/1604.05375v1 — complete relevant Sections 1–2 and 8 consulted; a general criterion rather than the explicit theorem.
- Baran, Sikolya and Stehlík (2013), https://doi.org/10.1016/j.spl.2013.03.003 — author proof text consulted; different dimensional and noise setting.
- Baldi Antognini and Zagoraiou (2010), https://doi.org/10.1016/j.jspi.2010.03.027 — only abstract and related citations available; full-document comparison unresolved.
- Mukherjee (2001), https://docs.lib.purdue.edu/dissertations/AAI3043760/ — catalog abstract only, potentially relevant general product covariance conditions.

High-noise uniqueness is proved only for sufficiently large \(\eta\), not for arbitrary noise. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
