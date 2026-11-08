# Environmental response speed reverses Hopf criticality in logit ecological games

## Finding

For the two-strategy logit game–environment feedback system below, the criticality of an interior Hopf bifurcation depends on the environmental response speed, although the Hopf rationality threshold and equilibrium location do not. An explicit first Lyapunov coefficient gives a sharp dichotomy: if the environmental replenishment parameter satisfies \(\theta\ge 1/3\), every existing interior Hopf bifurcation under the stated payoff assumptions is **supercritical**. If \(0<\theta<1/3\), sufficiently strong payoff variation can make the coefficient cross through zero at a unique positive environmental speed. The same fixed payoff matrix then has supercritical Hopf onset at slower environmental response and subcritical Hopf onset at faster response.

More precisely, let \(s<0\), \(R>-s\), \(T>0\), \(P>0\), \(0<\theta<1\), and \(\varepsilon>0\). Define
\[
 a=s-R+P-T,\qquad b=R-s,\qquad c=-(P+s),
\]
and let \(x,n\in[0,1]\) evolve in physical time according to
\[
 \dot x=\frac{1}{1+\exp[-\beta(a x n+b x+c n+s)]}-x,\qquad
 \dot n=\varepsilon n(1-n)((1+\theta)x-1),\quad\beta>0.
\]
Put
\[
 x_0=\frac{1}{1+\theta},\quad h=x_0(1-x_0),\quad z=1-2x_0,
 \quad L=\log(1/\theta),\quad D=R+T+\theta(P+s),
\]
\[
 Q=\frac{D}{1+\theta}>0,\quad u=b x_0+s=\frac{R+\theta s}{1+\theta}>0.
\]
At any existing interior Hopf point, the rationality and environmental equilibrium are
\[
 \beta_H=\frac{Q+h a L}{h(bQ+a u)},\qquad
 N=\frac{u-L/\beta_H}{Q}\in(0,1).
\]
The qualifier *existing* means \(\beta_H>0\), \(0<N<1\); in particular the formulas do not assert existence outside these inequalities. Set
\[
 p=b+aN>0,\quad q=a x_0+c=-Q<0,\quad
 C_1=2+\frac{za}{q},\quad C_2=-2q+za.
\]
In the canonical local coordinates defined in the proof, the cubic radial Hopf coefficient is exactly
\[
 \boxed{\displaystyle
 \ell(\varepsilon)=-\frac{\beta_H}{16}
 \big[pC_1+\varepsilon(1+\theta)N(1-N)C_2\big].}
\]
Its two parameter factors simplify to
\[
 C_1=\frac{(1+\theta)(R+T+P+s)}{D}>0,\qquad
 C_2=\frac{(3-\theta)(R+T)+(3\theta-1)(P+s)}{1+\theta}.
\]
Consequently, \(C_2\ge0\) implies \(\ell(\varepsilon)<0\) for every \(\varepsilon>0\). If \(C_2<0\), there is a unique
\[
 \boxed{\displaystyle
 \varepsilon_*=-\frac{pC_1}{(1+\theta)N(1-N)C_2}>0}
\]
with \(\ell<0\) when \(0<\varepsilon<\varepsilon_*\), and \(\ell>0\) when \(\varepsilon>\varepsilon_*\). The condition \(C_2<0\) is equivalent to
\[
 0<\theta<\frac13,\qquad
 (1-3\theta)(P+s)>(3-\theta)(R+T).
\]
For nonzero \(\ell\), a positive crossing of the Hopf trace as \(\beta\) increases gives a locally attracting small periodic orbit on the \(\beta>\beta_H\) side when \(\ell<0\), and a locally repelling small periodic orbit on the \(\beta<\beta_H\) side when \(\ell>0\). This is a local bifurcation assertion only.

The concrete admissible witness \(\theta=1/4\), \(s=-1\), \(R=2\), \(T=1\), \(P=40\) has \((a,b,c)=(36,3,-39)\), and
\[
 \beta_H=\frac{85+48\log4}{108},\qquad
 N=\frac{595-204\log4}{51(85+48\log4)},\qquad
 p=\frac{675}{85+48\log4}.
\]
Here \(C_1=70/17\), \(C_2=-6/5\), and
\[
 \varepsilon_*=\frac{140p}{51N(1-N)}\approx315.436450053502.
\]
In particular the same game has \(\ell(100)\approx-1.098541482137\) and \(\ell(400)\approx0.431201718511\), establishing opposite Hopf criticalities with every other model parameter held fixed.

## Assumptions and scope

All four payoff-gap parameters and both dynamical parameters satisfy the strict inequalities above. The scalar \(x\) is the fraction cooperating and \(n\) is a normalized environment, each between zero and one. The rationality \(\beta\) is varied only locally around \(\beta_H\); \(\varepsilon\) is varied to alter the environmental time scale. The logistic decision term is evaluated with the displayed bilinear payoff difference; no quasi-steady reduction, diffusion, noise, or network averaging is used. An interior Hopf exists only when the formula for \(N\) lies strictly between zero and one, so no boundary-degenerate cases are included.

## Proof

**1. Equilibrium and spectral crossing.** An interior environmental equilibrium has \((1+\theta)x-1=0\), hence \(x=x_0\). Since the logit response equals \(x_0\) exactly when its argument is \(L\), the other equilibrium equation is \(\beta(u-Qn)=L\), giving \(n=(u-L/\beta)/Q\). Write \(F\) and \(G\) for the two right-hand sides. At the interior equilibrium,
\[
 F_x=\beta h(b+an)-1,\quad F_n=\beta h q<0,\quad
 G_x=\varepsilon(1+\theta)n(1-n)>0,\quad G_n=0.
\]
Thus the determinant is positive, and zero trace is equivalent to \(\beta h(b+an)=1\), which solves to the displayed \(\beta_H\). The trace crosses zero with positive speed because
\[
 \left.\frac{d\operatorname{tr}J}{d\beta}\right|_{\beta_H}
 =h\left(b+\frac{au}{Q}\right)
 =h\frac{(1+\theta)(PR-Ts)}{D}>0.
\]
The purely imaginary pair is simple, with frequency \(\omega=\sqrt{AB}>0\) for \(A=-\beta_H hq\) and \(B=\varepsilon(1+\theta)N(1-N)\).

**2. Exact local Hopf coefficient.** Let \(S(w)=(1+e^{-w})^{-1}\). At the equilibrium, the derivatives of \(S(\beta g)\) with respect to \(g\) are
\[
 H_1=\beta_H h=\frac1p,\quad H_2=\beta_H^2 h z,\quad
 H_3=\beta_H^3 h(1-6x_0+6x_0^2).
\]
Because \(g=axn+bx+cn+s\), direct differentiation yields
\[
 F_{xx}=H_2p^2,\quad F_{xn}=H_2pq+H_1a,\quad
 F_{nn}=H_2q^2,
\]
\[
 F_{xxx}=H_3p^3,\qquad
 F_{xnn}=H_3pq^2+2H_2aq.
\]
Set \(X=x-x_0\), \(Y=\sqrt{A/B}(n-N)\). The linearization becomes \(\dot X=-\omega Y\), \(\dot Y=\omega X\). The standard planar cubic radial averaging formula in these canonical coordinates (with the quadratic near-identity correction included) simplifies here to
\[
 16\ell=F_{xxx}+\frac BA F_{xnn}
 +\frac{F_{xn}}{A}\left(F_{xx}+\frac BA F_{nn}\right).
\]
Indeed the canonical second component has vanishing \(G_{XX}\), \(G_{YY}\), \(G_{XXY}\) and \(G_{YYY}\) at the equilibrium; its mixed second derivative is allowed but multiplies the zero pure second derivatives in the formula. This calculation includes the nonlinear logistic curvature and the bilinear-payoff mixed derivative. Substitution of \(H_1p=1\) and the identity
\[
 (1-6x_0+6x_0^2)-(1-2x_0)^2=-2h
\]
gives
\[
 16\ell=-\beta_H\left[p\left(2+\frac{za}{q}\right)+B(-2q+za)\right],
\]
which is the claimed coefficient without any approximation or missing environmental-time factor.

**3. Sharp sign conditions and nondegenerate examples.** Since \(D>0\) and \(R+s>0\), the expression for \(C_1\) is positive. For \(\theta\ge1/3\), \(C_2>0\): it is immediate when \(P+s\ge0\); otherwise \(-R<P+s<0\) gives
\[
 (1+\theta)C_2>(3-\theta)(R+T)-(3\theta-1)R
 =4(1-\theta)R+(3-\theta)T>0.
\]
When \(0<\theta<1/3\), solving \(C_2<0\) yields the displayed strict payoff inequality, and the affine dependence of \(16\ell\) on \(\varepsilon\) gives the unique crossing. At the explicit witness, \(1.38<\log4<1.39\) proves \(0<N<1\), \(\beta_H>\beta_{\mathrm{int}}=5\log4/7\), and \(315<\varepsilon_*<316\). The computed signs at \(100\) and \(400\) are therefore strict. With a simple imaginary eigenpair, positive trace-crossing speed, and \(\ell\ne0\), the classical nondegenerate planar Hopf theorem supplies the stated stable or unstable small cycles on the corresponding sides of \(\beta_H\).

## Verification

Run \(\texttt{python verify.py}\) using Python 3.11 or later. The script uses only the standard library, checks the exact rational identities for \(C_1\) and \(C_2\) on multiple admissible rational parameter sets, evaluates the explicit witness to high decimal precision, and compares the unsimplified derivative-based cubic coefficient with its reduced formula at two environmental speeds. It prints \(\texttt{VERIFY_OK}\) on success. The global sign statements and existence of small cycles are proven analytically above; finite arithmetic tests are not being substituted for those proofs.

## Relationship to prior work

Paarporn's 2023 feedback-evolving logit game introduces the model, computes equilibrium and interior Hopf thresholds, and expressly leaves the first Lyapunov coefficient and stable-cycle conditions for future investigation. The present result fixes the sign for a large payoff region and exhibits a sharp transition to subcritical Hopf onset within its own admissible assumptions. Gavin, Cao and Paarporn (2024) analyze fixed points for single-environment-free logit games, not this two-dimensional environment-coupled cubic coefficient. A 2026 article by Gavin, Paarporn and Cao has a closely relevant general stability title and abstract; its full text could not be inspected, so it remains a material publication-priority risk rather than evidence of noncoverage. Earlier replicator-based environmental game results do not themselves give this logit derivative calculation.

## Limitations

The statement is local to interior Hopf points. At \(\varepsilon=\varepsilon_*\) the cubic coefficient is zero, but no fifth-order coefficient is established, so neither a genuine Bautin bifurcation nor the existence of two simultaneous cycles is claimed. No claim is made about global basins, persistence of cycles far from onset, or stochastic finite-population games. The full text of the 2026 closely related article remains unverified; originality is a best-knowledge assessment pending that comparison and independent scientific validation.

## References

1. K. Paarporn, *The madness of people: rational learning in feedback-evolving games*, arXiv:2311.02745v1, first public 2023-11-05, https://arxiv.org/html/2311.02745v1 .
2. R. Gavin, M. Cao and K. Paarporn, *An Analysis of Logit Learning with the r-Lambert Function*, arXiv:2409.05044, first public 2024-09-08, https://arxiv.org/abs/2409.05044 .
3. R. Gavin, K. Paarporn and M. Cao, *Learning to Avoid Tragedies: Boundedly Rational Agents in Feedback-Evolving Games*, IEEE Transactions on Automatic Control (2026), DOI:10.1109/TAC.2026.3685548, https://doi.org/10.1109/TAC.2026.3685548 .
4. A. R. Tilman, J. B. Plotkin and E. Akçay, *Evolutionary games with environmental feedbacks*, Nature Communications 11 (2020) 915, https://doi.org/10.1038/s41467-020-14531-6 .
