# Scientific review: equal-strength Cole–Cole peak resolution

## Correctness — PASS

The claim is an all-parameter mathematical statement for \(0<\alpha\le1\), \(r>1\), strictly positive equal strengths and a common exponent. Direct rationalization of the original fractional susceptibility gives a positive even loss in the scaled logarithmic frequency \(s\). The substitution \(y=\cosh s\) turns the entire loss curve into a rational function whose derivative has a strictly decreasing quadratic numerator on \(y\ge1\). Its endpoint factorization \(P(1)=(d+c)(d^2-cd-2)\) proves both the unique critical ratio and the impossibility of additional peaks. Solving this quadratic gives the exact two-peak locations, and the endpoint expansion verifies a quartically flat central maximum at equality. Monotonicity in the fractional exponent and the large-separation trough law follow by explicit limits. The package's `verify.py` re-evaluates 1004 supplementary comparisons from the unsimplified physical loss expression and derivatives; these finite tests support but do not replace the analytic proof.

Risk: no hidden sign convention or normalization is assumed. This is the loss defined by minus the imaginary part of the stated complex susceptibility; the different convention that calls \(1-\alpha\) the Cole–Cole broadening exponent is explicitly distinguished. Equality of the strengths and exponents is essential.

## Originality — PASS on examined material

The original Cole–Cole paper (K. S. Cole and R. H. Cole, 1941, DOI 10.1063/1.1750906) introduces the fractional response and analyzes a single relaxation's broadening. Hilfer (2002, DOI 10.1103/PhysRevE.65.061510) gives analytic fractional susceptibility and its single-peak widths; its full author-hosted HTML was examined. Chassagne and coauthors (2016, DOI 10.3389/fchem.2016.00030) use sums of two Havriliak–Negami functions to fit overlapping relaxations; the relevant full-text sections concern reconstruction and electrode polarization, not an exact necessary-and-sufficient peak-count criterion.

Statement-level comparison with accessible previous results found exact three-equal-Debye and four-equal-Debye classifications, respectively. Neither result concerns two components with a continuously varying common fractional exponent; one cannot obtain the two-Cole–Cole critical curve by substituting a parameter in either prior theorem. Broader searches of fractional Cole–Cole mixtures, two shifted reciprocal-cosh kernels, and the local mathematical research index did not uncover an exact duplicate. A negative search is not proof of historical priority: a statistical paper proving a general two-shift mode criterion for generalized secant-hyperbolic distributions might subsume the statement under a change of variables. No such decisive covered theorem was found in the material inspected.

Risk: unexamined specialist dielectric-resolution literature or an equivalently parameterized mixture-modality theorem may predate this formula. The conclusion is an originality judgment on the examined published source material, not an independent priority certification.

## Mathematical value — PASS

Whether multiple dielectric relaxations produce distinguishable peaks is a physical interpretation problem, not a question of arbitrary parameter substitution. This theorem determines the entire mathematical separation boundary in the two-dimensional exponent-versus-timescale plane, rather than a single plotted or numeric case. It also gives exact extremum locations, a quartic transition point, the square-root splitting law and the trough-height asymptotic. The required timescale separation increases from \(3+2\sqrt2\) for Debye response to approximately \(121.715\) already at \(\alpha=1/2\), and diverges exponentially when the fractional exponent approaches zero. These scales are useful benchmark limits for ideal two-component spectral interpretation, regardless of experimental fitting methods.

Risk: the statement is restricted to symmetric equal-strength, same-exponent pairs; unequal amplitudes, measurement noise and finite-window resolvability remain beyond its scope. The value asserted is the exact complete model classification, not a universal empirical detection threshold or a large downstream theorem.

## Close literature and limitations

The first three references in `RESULT.md` were compared for model equivalence and stronger coverage. Their frequency-domain formulas support the model assumptions, but the cited parts do not state or imply the necessary-and-sufficient two-component fractional peak-count threshold without an additional independent calculation. Accessible past work on three and four Debye components has a different mathematical domain. The residual equivalence risk from general mixture-mode theorems remains explicit.

Self-review: passed. Independent audit: not yet performed.
