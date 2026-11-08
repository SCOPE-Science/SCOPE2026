# Universal two-term clearance and a single infection peak at the vaccination tricritical point

## Finding

In the deterministic three-compartment minimal vaccination–epidemic mean-field equations of Pires, Sampaio Filho, Herrmann and Andrade Jr. [1], the tricritical epidemic is globally cleared from every initially infected state. At the precise tricritical parameters below, all initial triples with positive infection satisfy

\[
 i(t)=\sqrt{\frac{\eta}{2\gamma(\gamma+\eta)}}\,t^{-1/2}
 +\frac{2\gamma+\eta}{2\gamma(\gamma+\eta)}\,t^{-1}
 +O(t^{-3/2}\log t),\qquad t\to\infty.
\]

The two displayed coefficients are independent of initial conditions. In addition, the infected fraction has at most one positive-time local maximum: it has exactly one if initially \(s(0)/i(0)>\gamma/\eta\), and is strictly decreasing after time zero otherwise. At the unique peak, the susceptible-to-infected ratio is precisely \(\gamma/\eta\). Both the exact signed \(t^{-1}\) correction and the complete one-peak classification refer to the same deterministic model; the \(t^{-1/2}\) critical exponent itself was already known [1,2].

## Assumptions and scope

Let \(s(t),i(t),v(t)\) be the susceptible, infected, vaccinated population fractions, respectively, with \(s+i+v=1\). The original mean-field model is

\[
\begin{aligned}
 \dot s&=-\eta s-(1-\eta)\lambda si+\gamma i,\\
 \dot i&=(1-\eta)\lambda si+(1-\sigma)\lambda vi-\gamma i,\\
 \dot v&=\eta s-(1-\sigma)\lambda vi.
\end{aligned}
\]

Assume \(0<\gamma<1\), \(0<\eta<(1-\gamma)/2\), and choose the exact tricritical parameters from [1]:

\[
 \lambda=\frac{\gamma+\eta}{1-\eta},\qquad
 \sigma=1-\frac{\gamma(1-\eta)}{\gamma+\eta}.
\]

These restrictions ensure \(0<\eta,\gamma,\lambda,\sigma<1\). Quantify over every initial state \((s_0,i_0,v_0)\) in the closed physical simplex \(s_0,i_0,v_0\geq0\), \(s_0+i_0+v_0=1\), with \(i_0>0\). The boundary \(i_0=0\) is excluded from the asymptotic claim because it is the exactly disease-free invariant face. Time is the unchanged continuous time of the stated mean-field ODE. No assertion is made for finite stochastic populations, spatial lattices, or parameters away from the exact tricritical point.

## Proof

**1. Exact reduction and positivity.** At the chosen parameters, \((1-\eta)\lambda=\gamma+\eta\) and \((1-\sigma)\lambda=\gamma\). Using \(v=1-s-i\), the two independent equations become exactly

\[
 \dot s=-\eta s+\gamma i-(\gamma+\eta)si,\qquad
 \dot i=\eta si-\gamma i^2.
 \tag{1}
\]

The nonnegative simplex is forward invariant: on \(s=0\), \(\dot s=\gamma i\geq0\); on \(v=0\), \(\dot v=\eta s\geq0\); and \(\dot i=i(\eta s-\gamma i)\), so \(i(t)>0\) for every finite \(t\) when \(i_0>0\). Boundedness inside the simplex guarantees existence for all \(t\geq0\).

**2. Global single-peak classification.** Set

\[
 r=\frac{s}{i},\qquad R=\frac{\gamma}{\eta},\qquad p=R(R+1)>0.
\]

Equation (1) implies the exact identities

\[
 \dot r=\gamma-\eta r-\eta i\,r(r+1),\qquad
 \dot i=\eta i^2(r-R).
 \tag{2}
\]

At any crossing of \(r=R\), one has \(\dot r=-\eta i p<0\). Therefore it can only cross from above to below. If \(r_0>R\), then until the crossing \(i(t)\geq i_0\) and \(r(t)\geq R\), so \(\dot r\leq-\eta i_0p\). A crossing occurs at a unique finite time, no later than \((r_0-R)/(\eta i_0p)\), and it is exactly the unique infected maximum. If \(r_0\leq R\), it remains below \(R\) for positive time and infection strictly decreases there. This includes \(s_0=0\).

**3. Global convergence.** After the unique possible peak, \(i\) is strictly decreasing, hence tends to a limit \(\ell\geq0\). Suppose \(\ell>0\). Since \(r\geq0\), its equation gives \(\dot r\leq\gamma-\eta r-\eta\ell r(r+1)\). The comparison scalar equation has a unique positive attracting equilibrium \(r_\ell<R\); hence \(\limsup r\leq r_\ell<R\). Eventually \(\dot i\leq-\eta\delta i^2\) for some \(\delta>0\), contradicting \(\ell>0\). Thus \(i\to0\). Equation (2) also yields \(\dot r+\eta(r-R)=-\eta i r(r+1)\); since \(r\) is bounded by \(\max\{r_0,R\}\) and \(i\to0\), variation of constants gives \(r\to R\). Consequently \(s=ri\to0\) and \(v\to1\).

**4. Asymptotic tracking of the stable ratio.** Put \(w=r-R\). The exact ratio equation is

\[
 \dot w=-\eta w-\eta i\bigl[p+(2R+1)w+w^2\bigr].
 \tag{3}
\]

Because \(w\to0\) and \(\dot i/i=\eta iw\to0\), the following elementary stable-filter principle applies: if \(z'=-\eta z+a i^k+o(i^k)\) for fixed \(k\geq1\), then \(z/i^k\to a/\eta\). Indeed division by \(i^k\) gives a scalar equation with damping \(\eta+k\dot i/i\to\eta\), and its forcing tends to \(a\). Using (3) first gives \(w=-pi+o(i)\), then the source bound yields \(w=-pi+O(i^2)\). Define \(h=w+pi\). Direct differentiation with \(\dot i=\eta i^2w\) gives

\[
 \dot h=-\eta h-\eta i\bigl[(2R+1)w+w^2\bigr]+p\eta i^2w.
 \tag{4}
\]

Inserting \(w=-pi+O(i^2)\) and applying the same stable-filter argument gives \(h=p(2R+1)i^2+o(i^2)\). Subtracting this quadratic term in (4), observing \((i^2)'=O(i^4)\), and applying the stable filter once more to its \(O(i^3)\) forcing proves the stronger remainder bound

\[
 w=-pi+p(2R+1)i^2+O(i^3).
 \tag{5}
\]

The exponential homogeneous transients are negligible against each power of \(i\), since already \(\dot i/i\to0\).

**5. Reciprocal-square integration and the second coefficient.** Substitute (5) into the second identity of (2):

\[
 \dot i=-K i^3+L i^4+O(i^5),\quad
 K=\eta p=\frac{\gamma(\gamma+\eta)}{\eta},\quad
 L=K(2R+1).
 \tag{6}
\]

For \(y=i^{-2}\), this means \(\dot y=2K-2Li+O(i^2)\). Since \(y/t\to2K\), initially \(i(t)\sim c_0t^{-1/2}\) with \(c_0=(2K)^{-1/2}\). Integrating \(\dot y=2K+O(t^{-1/2})\) yields \(y=2Kt+O(\sqrt t)\), hence \(i=c_0t^{-1/2}+O(t^{-1})\). A second integration then gives

\[
 y(t)=2Kt-4Lc_0\sqrt t+O(\log t).
\]

Taking the negative square root,

\[
 i(t)=\frac{1}{\sqrt{2K}}t^{-1/2}+\frac{L}{2K^2}t^{-1}+O(t^{-3/2}\log t).
\]

Since \(L/(2K^2)=(2R+1)/(2\eta p)=(2\gamma+\eta)/[2\gamma(\gamma+\eta)]\), the claimed universal coefficients follow. The remainder constant may depend on the initial condition; both displayed coefficients do not.

## Verification

The accompanying `verify.py` checks the exact symbolic identity (2), the two stable-manifold tracking coefficients, \(K\), \(L\), and the second asymptotic coefficient for unrestricted positive parameter symbols. It also integrates the full reduced ODE at the source's example parameters \(\eta=1/10\), \(\gamma=7/100\) and checks both peak regimes and convergence of the scaled correction. Run with `python verify.py` (Python 3, SymPy, SciPy and NumPy). These diagnostics supplement, and do not replace, the infinite-time proof above.

For those source parameters, \(\lambda=17/90\), \(\sigma=107/170\), and the formula specializes to

\[
 i(t)=\sqrt{\frac{500}{119}}\,t^{-1/2}+\frac{1200}{119}\,t^{-1}+O(t^{-3/2}\log t).
\]

The first parameter-dependent coefficient is \(\sqrt{500/119}\approx2.049800\); the second is \(1200/119\approx10.084034\).

## Relationship to prior work

Reference [1], Section II.1 (mean-field Equations (1)–(6)) already determines the tricritical parameter pair and the stationary critical exponent; Section III and Figure 6 numerically find a tricritical time-decay exponent consistent with \(1/2\). Those are prior results, not part of the novelty claim here. The present result gives a full-simplex peak classification and the explicit initial-condition-independent finite-time asymptotic coefficient at order \(t^{-1}\), after confirming the leading \(t^{-1/2}\) amplitude.

Reference [2], Section 2, Equation (15), gives the exact \(t^{-1/2}\) decay for a one-component cubic mean-field tricritical normal form. That simpler scalar equation does not encode the susceptible-ratio relaxation that creates the nonzero \(t^{-1}\) term in (6) or the full-simplex one-peak test (2). Two related published mathematical epidemic analyses, on multiple exposure and on nonlinear SIRS feedback [3,4], also derive precise critical decays but have different dynamical equations and no formula for this vaccination model. Equivalent discoveries elsewhere remain possible.

## Limitations

This is a deterministic, well-mixed, exact-tricritical theorem with an initially infected population. It gives no finite-population extinction-time distribution, spatial-lattice scaling law, or away-from-tricritical crossover. It does not say that the already known tricritical exponent is novel. The asymptotic \(O(\cdot)\) is pointwise in each admissible initial condition, not uniform as the initial infection approaches zero. Although the cited primary works and accessible comparison summaries were examined, an unindexed equivalent analysis may exist; no independent external validation has been performed.

## References

1. M. A. Pires, C. I. N. Sampaio Filho, H. J. Herrmann, and J. S. Andrade Jr., *Tricritical behavior in epidemic dynamics with vaccination*, arXiv:2306.08135, first posted 2023-06-13. https://arxiv.org/abs/2306.08135 (Section II.1 and Section III).
2. S. Lübeck, *Tricritical directed percolation*, arXiv:cond-mat/0608339, posted 2006-08-15. https://arxiv.org/abs/cond-mat/0608339 (Section 2, Equation (15)).
3. *Global attraction and two-term critical relaxation at the multiple-exposure disease-free degeneracy*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-global-attraction-and-two-term-critical-relaxation-at-the-multip--45a437e4957f (accessible public summary; different Li–Ma multiple-exposure system).
4. *Universal extinction crossover at the pitchfork edge of a nonlinear SIRS model*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-extinction-crossover-at-the-pitchfork-edge-of-a-nonlin--c1921b9ff104 (accessible public summary; different nonlinear SIRS system).
