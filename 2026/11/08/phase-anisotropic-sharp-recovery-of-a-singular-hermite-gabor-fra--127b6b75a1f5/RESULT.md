# Phase-anisotropic sharp recovery of a singular Hermite Gabor frame

## Finding
For each Gaussian width \(\gamma>0\), set \(g_\zeta(t)=(t-\zeta)e^{-\gamma t^2}\), where \(\zeta\in\mathbb C\). Let \(A_\gamma(\zeta)\) be the **optimal lower frame bound** of the rectangular Gabor system \(\{e^{\pi i m t}g_\zeta(t-n):m,n\in\mathbb Z\}\), with value zero when it is not a frame. Define the real two-vectors \(v,u,w\) in the next section, and the two explicit positive constants
\[
K_x(\gamma)=\frac{(v_eu_o-v_ou_e)^2}{u_e^2+u_o^2},\qquad
K_\nu(\gamma)=\frac{(v_ew_o-v_ow_e)^2}{w_e^2+w_o^2}.
\]
**Sharp, uniform angular asymptotic:** as \(\zeta\to0\) through arbitrary complex directions,
\[
\boxed{A_\gamma(\zeta)=2K_x(\gamma)(\operatorname{Re}\zeta)^2+2K_\nu(\gamma)(\operatorname{Im}\zeta)^2+O_\gamma(|\zeta|^3).}
\]
All \(K_x(\gamma),K_\nu(\gamma)\) are strictly positive. Consequently, to leading order among all equal-magnitude complex Gaussian admixtures, the best phase is real if \(K_x>K_\nu\), imaginary if \(K_\nu>K_x\), and any phase if equal. **The preferred phase reverses with Gaussian width:**
\[
\begin{array}{c|cc}
\gamma&K_x(\gamma)&K_\nu(\gamma)\\\hline
1&1.5698121758177\ldots&0.7629046448071\ldots\\
\pi&0.2440756175969\ldots&0.9999580481353\ldots
\end{array}
\]
By continuity, at least one width in \((1,\pi)\) has equal quadratic coefficients. No uniqueness of the crossing is claimed. For the standard width \(\gamma=\pi\), a small *imaginary* admixture provides approximately \(4.09691905\) times the leading lower-frame-bound protection of an equal-sized *real* admixture. The underlying windows have equal \(L^2\) energy for equal \(|\zeta|\), regardless of phase.

## Assumptions and scope
All shifts and modulations use the exact Gabor convention
\[
T_n f(t)=f(t-n),\quad M_{m/2}f(t)=e^{\pi i mt}f(t),\quad n,m\in\mathbb Z.
\]
Fix any real \(\gamma>0\). For \(\sigma\in\{e,o\}\) and \(j\in\mathbb Z\), write \(t_{e,j}=-2j\), \(t_{o,j}=-1-2j\), and define the following absolutely convergent real series:
\[
\begin{split}
v_\sigma&=\sum_{j\in\mathbb Z}e^{-\gamma t_{\sigma,j}^2},\\
u_\sigma&=\sum_{j\in\mathbb Z}(1-2\gamma t_{\sigma,j}^2)e^{-\gamma t_{\sigma,j}^2},\\
w_\sigma&=4\pi\sum_{j\in\mathbb Z}j t_{\sigma,j}e^{-\gamma t_{\sigma,j}^2}.
\end{split}
\]
Set \(v=(v_e,v_o)\), \(u=(u_e,u_o)\), and \(w=(w_e,w_o)\). Each remainder estimate is for fixed width; uniformity in width is not asserted. The result concerns the entire infinite Gabor family and its exact optimal lower bound, rather than a finite Gabor truncation.

## Proof
**1. Exact scalar Zak multiplier.** Let \(Zf(x,\nu)=\sum_{k\in\mathbb Z}f(x-k)e^{2\pi i k\nu}\). For an integer translation lattice and half-integer modulation lattice, the Zak-transform Parseval identity gives the exact frame multiplier
\[
\mathscr F_\zeta(x,\nu)=|Zg_\zeta(x,\nu)|^2+|Zg_\zeta(x,\nu+1/2)|^2.
\]
For sufficiently regular windows, the optimal lower bound is the minimum of this continuous multiplier on a fundamental Zak torus. Separate even and odd translates:
\[
\begin{array}{ll}
E=\sum_j e^{-\gamma(x-2j)^2}e^{4\pi i j\nu},&D_E=\sum_j(x-2j)e^{-\gamma(x-2j)^2}e^{4\pi i j\nu},\\
O=\sum_j e^{-\gamma(x-1-2j)^2}e^{4\pi i j\nu},&D_O=\sum_j(x-1-2j)e^{-\gamma(x-1-2j)^2}e^{4\pi i j\nu}.
\end{array}
\]
The phase \(e^{2\pi i\nu}\) of the odd block cancels on taking the sum of squares, so
\[
\mathscr F_\zeta(x,\nu)=2\bigl(|D_E-\zeta E|^2+|D_O-\zeta O|^2\bigr).
\]
The scalar \(A_\gamma(\zeta)\) is the minimum of this expression over \(x\in[0,1]\), \(\nu\in[0,1/2]\), with equivalent torus edges identified.

**2. There is exactly one singular Zak fiber.** To prove this afresh, expand \(W=D_EO-ED_O\) by grouping terms with \(n=j+k\). The difference \((x-2j)-(x-1-2k)=1+2(k-j)\) and completion of squares give
\[
W(x,\nu)=S_\gamma\sum_{n\in\mathbb Z}(-1)^n e^{-2\gamma(x-1/2-n)^2}e^{4\pi i n\nu},
\]
where
\[
S_\gamma=\sum_{j\in\mathbb Z}(4j+1)e^{-\gamma(4j+1)^2/2}
=e^{-\gamma/2}\prod_{r\ge1}(1-e^{-4\gamma r})^3>0.
\]
The latter equality is Jacobi's theta-derivative product identity. By the Jacobi triple product, the Gaussian Zak sum \(\sum_n e^{-2\gamma(y-n)^2}e^{2\pi i n\tau}\) has exactly one zero per unit Zak torus: \(y\equiv\tau\equiv1/2\pmod1\), and this zero is simple. Hence \(W\) vanishes precisely when \(x\equiv0\pmod1\), \(\nu\equiv0\pmod{1/2}\). At this point oddness of the summands yields \(D_E=D_O=0\), whereas \(E=v_e>0\), \(O=v_o>0\). Thus the two odd/even factors have a common zero at \(\zeta=0\) only at this fiber. The same Wronskian argument implies they have no common zero for any \(\zeta\ne0\); compactness therefore ensures a positive lower bound when \(\zeta\ne0\). This is a qualitative input, not itself the new quantitative finding.

**3. First-order geometry at the singular fiber.** At \((x,\nu)=(0,0)\), differentiate the odd/even first-moment vector \(D=(D_E,D_O)\):
\[
D(x,\nu)=u\,x+i w\,\nu+O_\gamma(x^2+\nu^2),\qquad(E,O)(x,\nu)=v+O_\gamma(|x|+|\nu|).
\]
Indeed the formulas for \(u,w\) in the scope section are the two exact derivatives. The triple-product simple-zero statement for \(W\) shows that each determinant \(\det(v,u)\) and \(\det(v,w)\) is nonzero: they are, up to signs and a factor of \(i\), its nonzero partial derivatives at the singular fiber. In particular, \(u\) and \(w\) are nonzero, and the two positive constants in the claim are well-defined. The real Hessian of \(\mathscr F_0\) is positive definite in the coordinates \((x,\nu)\), because \(u\) is real and \(iw\) imaginary.

**4. Global minimum and optimized coefficient.** The unique zero of the unperturbed multiplier and compactness confine every global minimizer for small \(\zeta\) to a neighborhood of the singular fiber. Positive definiteness and comparison with the value at that fiber imply \(|x|+|\nu|=O_\gamma(|\zeta|)\) for the minimizer. Consequently Taylor's theorem, uniformly in the phase of \(\zeta\), reduces its value to
\[
2\min_{x,\nu\in\mathbb R}\|ux+iw\nu-\zeta v\|_{\mathbb C^2}^2+O_\gamma(|\zeta|^3).
\]
The real and imaginary parts decouple. Orthogonal projection of \(v\) onto the real line spanned by \(u\) and the real line spanned by \(w\) gives exactly
\[
2\biggl[\frac{\det(v,u)^2}{\|u\|^2}(\operatorname{Re}\zeta)^2+\frac{\det(v,w)^2}{\|w\|^2}(\operatorname{Im}\zeta)^2\biggr]+O_\gamma(|\zeta|^3).
\]
This proves the claimed sharp, phase-uniform asymptotic. Since \(\|g_\zeta\|_2^2=\int(t^2+|\zeta|^2)e^{-2\gamma t^2}\,dt\), equal-magnitude comparisons are also equal-energy comparisons.

**5. Preference reversal.** The analytic Gaussian series allow rigorous evaluation using \(|j|\le5\), with the combined omitted weighted tails smaller than \(10^{-35}\) for either \(\gamma=1\) or \(\gamma=\pi\). Elementary bounds on exponentials and \(\pi\) give \(1.56<K_x(1)<1.58\), \(0.76<K_\nu(1)<0.77\), \(0.24<K_x(\pi)<0.25\), and \(0.99<K_\nu(\pi)<1.01\). These separated intervals prove strict inequalities in opposite directions; no reliance on floating-point equality is necessary. Continuity of all defining series and positivity of the denominators yield at least one crossover by the intermediate value theorem.

## Verification
`CHECK.py` evaluates the coefficient series at 55-digit precision, independently computes directly truncated Zak sums and their Wronskian identity, and minimizes the exact finite-sum Zak multiplier for three small mixing amplitudes and five complex phases at each of two widths. On the documented run it passed 98 deterministic assertions. In each test the minimized multiplier agrees with the sharp quadratic prediction to the expected small-amplitude order. The checker is finite; the infinite statement follows from the Zak transform, Jacobi product, uniqueness of the zero, compactness, and uniform Taylor expansion proved above.

## Relationship to prior work
Faulhuber and Petersen (first public September 2, 2026; arXiv:2609.02610) classify the **frame set of the pure first Hermite window** and identify the half-density obstruction, using Wronskians and Gaussian shift-invariant functions. A separately available qualitative classification of Gaussian–first-Hermite mixtures already establishes the all-or-nothing assertion that a nonzero Gaussian admixture removes that obstruction at half density. **Neither qualitative frame existence nor Wronskian zero location yields the present explicit optimal lower-bound coefficient without the independent minimization of the two real fiber directions.** The new contribution is precisely the two sharp coefficients, uniform phase-dependent expansion, and width-induced reversal in optimal regularization phase. General Gaussian optimal-bound work such as Faulhuber–Steinerberger (2016) treats a different window family. No priority is claimed for Jacobi identities, the qualitative mixture classification, or the general Zak frame criterion.

## Limitations
The expansion is a local \(|\zeta|\to0\) statement, with constants depending on fixed \(\gamma\). It does not provide the full optimal lower bound at arbitrary mixture magnitude, uniform estimates as \(\gamma\to0\) or \(\infty\), the number of crossover widths, or conclusions for other lattice densities. The numerical values are evaluations of exact convergent series and are not substituted for the proof. Equivalent asymptotic perturbation results under different terminology remain a publication-priority risk.

## References
1. M. Faulhuber and P. Petersen, *The frame set of the first Hermite function*, arXiv:2609.02610 (first public 2026-09-02), https://arxiv.org/html/2609.02610v2.
2. M. Faulhuber and S. Steinerberger, *Optimal Gabor frame bounds for separable lattices and estimates for Jacobi theta functions*, arXiv:1601.02972 (2016), https://arxiv.org/abs/1601.02972.
3. Classical Zak-transform frame characterization and Jacobi triple-product and theta-derivative identities, in their standard normalization specified above.
