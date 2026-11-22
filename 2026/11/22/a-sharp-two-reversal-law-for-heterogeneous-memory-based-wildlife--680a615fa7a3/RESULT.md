# A sharp two-reversal law for heterogeneous memory-based wildlife detectors

## Finding

Consider a continuously monitored individual whose time since its last known location is \(t\geq0\). Under the Gaussian mean-reversion and common-footprint hazard model defined below, the instantaneous competing-risk preference between two detectors can change strictly at most twice as \(t\) increases. This upper bound is sharp: even with a monotonically moving predicted animal position, two fixed detectors can have a strict \(+,-,+\) preference sequence. A necessary-and-sufficient three-sign criterion characterizes exactly when two switches occur, with explicit switching times given by a quadratic.

In particular, place detector \(+\) at \(+a\), detector \(-\) at \(-a\), and write \(\eta=\log(b_+/b_-)\), \(\rho=e^{-\kappa t}\), and
\[
Q(\rho)=-\eta\sigma^2\rho^2+2a(x_0-s)\rho+\eta(w^2+\sigma^2)+2as.
\]
Except when the two hazards are identical for all times, their ranking changes exactly twice at finite positive times if and only if \(\eta\ne0\), the quadratic vertex \(\rho_v\) is strictly in \((0,1)\), \(Q(0)\) and \(Q(1)\) have the sign of the nonzero leading coefficient, and \(Q(\rho_v)\) has the opposite sign. In the equal-gain case \(b_+=b_-\), at most one preference reversal is possible.

The bound is attained with \(a=\sigma=1\), \(w^2=1/10\), \(x_0=23/160\), \(s=103/160\), and \(b_+/b_-=e^{-1}\). Here
\[
Q(\rho)=(\rho-1/4)(\rho-3/4),
\]
so detector \(+\) has the larger instantaneous hazard for \(0\leq t<\log(4/3)/\kappa\), detector \(-\) for \(\log(4/3)/\kappa<t<\log(4)/\kappa\), and detector \(+\) again for \(t>\log(4)/\kappa\). Both the last known location and the activity center lie strictly between the two detector sites. The two strict reversals persist under sufficiently small perturbations of all parameters.

## Assumptions and scope

Fix \(a,w,\sigma,\kappa,b_+,b_->0\), and real locations \(x_0,s\). An individual last had a known location \(x_0\) at time zero and has an activity center \(s\). The Gaussian mean-reversion clock has mean and variance
\[
m(t)=s+(x_0-s)e^{-\kappa t},\qquad v(t)=\sigma^2(1-e^{-2\kappa t}).
\]
Both competing detectors use the same Gaussian spatial response width \(w\), but may have different positive baseline hazard strengths \(b_+,b_-\). Their stipulated, positive instantaneous cause-specific detection hazards after that last sighting are
\[
h_{\pm}(t)=\frac{b_{\pm}w}{\sqrt{w^2+v(t)}}\exp\left[-\frac{(\pm a-m(t))^2}{2(w^2+v(t))}\right].
\]
This form is the Gaussian spatial-response average under the unconditioned OU transition distribution, or equivalently a directly specified capture-history-dependent competing-risks hazard. It is **not** asserted to be the exact filtering hazard of a latent moving animal after conditioning additionally on the absence of intervening detections. Conditional on a detection occurring at time \(t\), the instantaneous cause probabilities are proportional to \(h_+(t)\) and \(h_-(t)\). The ranking concerns these instantaneous risks, **not** integrated first-capture probabilities, overall abundance, or the best detector layout. A switch means a strict change of sign of \(h_+(t)-h_-(t)\) as \(t\) passes a finite positive time.

## Proof

**Gaussian response identity.** For a normal random variable \(X\) of mean \(m\) and variance \(v\geq0\), completing the square gives
\[
\mathbb E\exp[-(X-z)^2/(2w^2)]=\frac{w}{\sqrt{w^2+v}}\exp[-(z-m)^2/(2(w^2+v))].
\]
It also holds for \(v=0\) by continuity. Thus the hazard form above is well defined for every \(t\geq0\).

**Reduction to a quadratic.** Put \(\rho=e^{-\kappa t}\in(0,1]\) and \(D(\rho)=w^2+\sigma^2(1-\rho^2)>0\). The common Gaussian normalizing factor cancels, so direct subtraction of the squared distances yields
\[
\log\frac{h_+(t)}{h_-(t)}=\eta+\frac{2a[s+(x_0-s)\rho]}{D(\rho)}=\frac{Q(\rho)}{D(\rho)}.
\]
Because \(D(\rho)>0\) and \(\rho\) decreases strictly and continuously from \(1\) toward \(0\), strict rankings are exactly the signs of \(Q\) on \((0,1)\). If \(\eta\ne0\), this polynomial has degree two; therefore it has at most two distinct roots and at most two strict changes of sign in that interval. If \(\eta=0\), it is linear. If it vanishes identically, both detector hazards are equal at all times, and no strict preference switch is present.

**Exact two-switch criterion.** Write \(Q(\rho)=A\rho^2+B\rho+C\), where \(A=-\eta\sigma^2\), \(B=2a(x_0-s)\), and \(C=\eta(w^2+\sigma^2)+2as\). For \(A\ne0\), its vertex is \(\rho_v=-B/(2A)\). It has two distinct roots strictly in \((0,1)\) precisely when \(0<\rho_v<1\), both endpoint values \(C\) and \(A+B+C\) have the sign of \(A\), and the vertex value \(C-B^2/(4A)\) has the opposite sign. For necessity, the two interior roots enclose the vertex and place the endpoints outside; for sufficiency, the intermediate value theorem places one root on each side of the vertex, and degree two excludes further roots. The strict inequalities also guarantee that each root reverses the instantaneous preference. If the two roots are \(0<\rho_-<\rho_+<1\), their chronological switching times are \(\kappa^{-1}\log(1/\rho_+)\) and \(\kappa^{-1}\log(1/\rho_-)\).

**Sharp construction and robustness.** With the parameter values in the finding, \(\eta=-1\), \(A=1\), \(B=-1\), and \(C=3/16\). The two roots are exactly \(1/4\) and \(3/4\), with strictly positive endpoint values and strictly negative vertex value \(-1/16\). Since \(Q(\rho)=(\rho-1/4)(\rho-3/4)\), the stated alternating preference follows under the monotone change \(\rho=e^{-\kappa t}\). Each strict criterion inequality depends continuously on the physical parameters, giving a nonempty open set of double-reversal models, not merely one algebraically tuned example.

## Verification

The included standalone \`checker.py\` requires only Python 3 and can be run with \`python3 checker.py\`. It verifies the rational polynomial coefficients, both exact roots, interior strict sign inequalities, the chronological preference sequence, and 20,000 seeded parameter cases comparing the hazard-log-ratio formula against direct Gaussian exponent differences. The randomized assertions supplement, but do not replace, the all-parameter analytic proof. The source file's output was: \`PASS 60017 formula, root and criterion assertions\`.

## Relationship to prior work

Panchaud and collaborators (arXiv:2408.17278, first public version 30 August 2024) formulate continuous-time spatial capture-recapture with Ornstein–Uhlenbeck memory of the last detected location and a competing-risk hazard. Their treatment provides the movement-memory motivation, but the inspected methods and discussion do not establish a sharp ranking-switch count or the two-reversal example under heterogeneous baseline detector strengths. Dey and collaborators (arXiv:2205.06320) explicitly motivate heterogeneity in baseline detection across detectors, but their spatial random-effects models do not analyze the evolving OU recapture-ranking sign. Efford and Boulanger (2019) analyze SECR survey designs and detector rates without the present moving two-hazard preference phase diagram. Distiller and Borchers (2015) use competing-risk capture hazards without an OU-memory ranking law. General Gaussian convolution and quadratic root theory are standard and are not claimed as new; the specific sharp and robust ecological two-reversal classification is the claimed finding.

## Limitations

This is an exactly specified parametric benchmark, not a validated animal-movement prediction or an optimal camera-placement recommendation. Gaussian OU transitions, equal detection widths, known center, perfect knowledge of the most recent location, constant baseline efficiencies, and a stated history-dependent hazard are substantive assumptions. Different widths, latent-center integration, censoring-dependent movement filtering, or non-Gaussian paths may yield different switching counts. The proof does not resolve historical priority over all surveillance and competing-risk literature; an independent external audit has not been performed.

## References

- Panchaud, C., King, R., Borchers, D., Worthington, H., Durbach, I., and Van Dam-Bates, P. (2024). *Incorporating Memory into Continuous-Time Spatial Capture-Recapture Models*. arXiv:2408.17278. https://arxiv.org/abs/2408.17278 (first public version 2024-08-30).
- Dey, S., Moqanaki, E. M., Milleret, C., Dupont, P., Tourani, M., and Bischof, R. (2022). *Modelling spatially autocorrelated detection probabilities in spatial capture-recapture using random effects*. arXiv:2205.06320. https://arxiv.org/abs/2205.06320.
- Efford, M. G., and Boulanger, J. (2019). *Fast evaluation of study designs for spatially explicit capture–recapture*. Methods in Ecology and Evolution. https://doi.org/10.1111/2041-210X.13239.
- Distiller, G., and Borchers, D. L. (2015). *A spatially explicit capture–recapture estimator for single-catch traps*. Ecology and Evolution. https://doi.org/10.1002/ece3.1748.
- McClintock, B. T., et al. (2021). *An integrated path for spatial capture–recapture and animal movement modeling*. Ecology. https://doi.org/10.1002/ecy.3473.
