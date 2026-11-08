# Robust coexistence of optimal and nonoptimal attractors under alternating quartic gradient steps

## Finding
Let \(\ell(x)=(x^2-1)^2/4\), and let the real gradient step of size \(s>0\) be \(g_s(x)=x-s\ell'(x)=(1+s)x-sx^3\). Alternate a large step \(a\) with a small step \(b\), so that the two-step epoch map is \(F_{a,b}=g_b\circ g_a\). At the distinguished pair \((a,b)=(2,1/2)\), \(F_{2,1/2}\) has **exactly nine real fixed points**:
\[
0,\qquad \pm1,\qquad \pm\frac1{\sqrt2},\qquad
\pm\sqrt{\frac{3-\sqrt2}{2}},\qquad
\pm\sqrt{\frac{3+\sqrt2}{2}}.
\]
Precisely four are attracting: \(\pm1\) and \(\pm1/\sqrt2\). All four have zero epoch multiplier (are superattracting), while the other five fixed points are strictly repelling. The two nonoptimal attracting points generate the **strictly period-two, schedule-synchronized orbits**
\[
\frac1{\sqrt2}\overset{g_2}{\longmapsto}\sqrt2
\overset{g_{1/2}}{\longmapsto}\frac1{\sqrt2},
\qquad
-\frac1{\sqrt2}\overset{g_2}{\longmapsto}-\sqrt2
\overset{g_{1/2}}{\longmapsto}-\frac1{\sqrt2}.
\]
Their two phases have loss \(1/16\) and \(1/4\); their time-average loss is \(5/32>0\), unlike the zero loss of the attracting minima \(\pm1\).

Moreover, there exists an open neighborhood \(U\subset(0,\infty)^2\) of \((2,1/2)\) such that **for every \((a,b)\in U\)** the epoch map has exactly nine distinct real fixed points, four attracting and five repelling. Two attracting branches remain the true minima \(\pm1\); the two other attracting branches remain off the minima and give nonconstant two-phase orbits with positive asymptotic mean loss. Thus the coexistence of successful and unsuccessful locally attracting learning outcomes persists under small changes in both step sizes.

## Assumptions and scope
The state is any real number. Updates are deterministic, with the large step \(a\) occurring first each epoch, followed by the small step \(b\). Attraction and repulsion mean local asymptotic stability or instability for the scalar **epoch map** \(F_{a,b}\). No claim is made that the four attracting epoch-fixed points exhaust every periodic attractor of higher epoch period. Rates \(2\) and \(1/2\) are distinguished by the fixed-rate dynamics: \(g_2\) is the Chebyshev endpoint after linear rescaling, while \(g_{1/2}'(\pm1)=0\) gives superattraction at the minimizing fixed points.

## Proof
Direct substitution and polynomial factorization give the exact identity
\[
F_{2,1/2}(x)-x
=\frac{x}{2}(x^2-1)(2x^2-1)(4x^4-12x^2+7).
\]
The quartic factor has the four real roots \(\pm\sqrt{(3\pm\sqrt2)/2}\); all nine listed roots are distinct. Differentiating \(F_{2,1/2}=g_{1/2}\circ g_2\) gives the epoch multipliers
\[
\begin{array}{c|c}
\text{fixed points}&F_{2,1/2}'\\\hline
0&9/2\\
\pm1&0\\
\pm1/\sqrt2&0\\
\pm\sqrt{(3-\sqrt2)/2}&27-18\sqrt2\\
\pm\sqrt{(3+\sqrt2)/2}&27+18\sqrt2
\end{array}
\]
Both \(27-18\sqrt2>1\) and \(27+18\sqrt2>1\). Hence exactly four points are locally attracting (in fact superattracting), and the remaining five are repelling. The identities \(g_2(1/\sqrt2)=\sqrt2\) and \(g_{1/2}(\sqrt2)=1/\sqrt2\), together with oddness, give the two nonoptimal orbits. Direct evaluation of \(\ell\) yields the two positive losses and their average.

For the persistence claim, \(F_{a,b}(x)-x\) depends polynomially on the three variables \((a,b,x)\). At the distinguished pair each of its nine real roots is simple, because its derivative in \(x\) is \(F_{2,1/2}'(x)-1\ne0\). The real implicit-function theorem gives nine distinct continuous (indeed analytic) real fixed-point branches for all parameters in a sufficiently small open neighborhood. The degree of \(F_{a,b}-x\) is exactly nine for positive \(a,b\), because its leading term is \(ba^3x^9\); hence there are no further real or complex roots. The epoch multipliers vary continuously, and all nine are strictly separated from modulus one at the distinguished pair. Shrinking the neighborhood preserves the four-attracting, five-repelling classification. The fixed points \(\pm1\) remain exact fixed points for every \((a,b)\), with multiplier \((1-2a)(1-2b)\). The other attracting branches remain separated from \(\pm1\), and their two successive phases remain distinct. Since \(\ell(x)>0\) for real \(x\notin\{-1,1\}\), their mean loss remains positive. Local attraction supplies disjoint nonempty open basins for each of the four attracting branches.

## Verification
The standalone `verify.py` uses SymPy exact arithmetic to reconstruct the ninth-degree epoch polynomial, its factorization, all nine fixed points and multipliers, the two strict alternating cycles, their exact loss values, and the nondegenerate Jacobians required for the implicit-function continuation. Execute `python3 verify.py` with SymPy installed. The reported output is `VERIFY_OK exact_epoch_factorization=1 fixed_points=9 attracting=4 repelling=5 loss_mean=5/32 IFT_nondegenerate=2`. The analytic implicit-function theorem, not finite numerical sampling, proves the parameter-open persistence.

## Relationship to prior work
Hofmann, *The Map Behind the Flow: Finite-Step Gradient Descent as a Dynamical System* (arXiv:2607.04993v1, 6 July 2026), develops the constant-step cubic gradient dynamics, its fixed-rate criticality and the Chebyshev endpoint \(g_2\). It does not analyze the composition of two different step sizes, the exact two-step fixed-point census, or their simultaneously attracting nonoptimal and optimal branches. Goujaud, Scieur, Dieuleveut, Taylor and Pedregosa (2022) give convergence rates for cyclic step sizes, chiefly on strongly convex quadratic problems, with local nonquadratic convergence near a minimizer. Oymak (2021) studies periodic large/small-step schedules for linear regression. Neither local spectral result gives the existence or stability of off-minimum nonlinear attractors in this quartic system. The new assertion is the two-rate **composition classification and its robust bistability**, not the pre-existing Chebyshev description, the gradient rule, or the general implicit-function theorem.

## Limitations
This is a complete census only of **epoch-fixed** points, not of all periodic points or all global attractors. The open parameter neighborhood is proved to exist but its largest extent is not determined. No claim concerns stochastic gradients, momentum, higher-dimensional objectives, or performance across arbitrary initialization distributions. Historical priority is assessed against the sources named here and targeted searches, not certified by an independent reviewer.

## References
1. T. Hofmann, *The Map Behind the Flow: Finite-Step Gradient Descent as a Dynamical System*, arXiv:2607.04993v1 (public 2026-07-06), https://arxiv.org/html/2607.04993v1. In particular Sections 2.1, 2.5–2.7 and related-work discussion.
2. B. Goujaud, D. Scieur, A. Dieuleveut, A. Taylor and F. Pedregosa, *Super-Acceleration with Cyclical Step-sizes*, Proceedings of Machine Learning Research 151 (2022), pp. 3028–3065, https://proceedings.mlr.press/v151/goujaud22a/goujaud22a.pdf. In particular Sections 3–5 and Appendix E.
3. S. Oymak, *Provable Super-Convergence with a Large Cyclical Learning Rate*, IEEE Signal Processing Letters 28 (2021), https://arxiv.org/pdf/2102.10734. In particular Introduction and Theorem 1.
