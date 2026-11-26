# Sharp fourth moments for the even quadratic spherical packet in every dimension

## Finding
Let \(S^{n-1}\subset\mathbb R^n\) carry probability-normalized rotation-invariant measure \(\sigma\). For every integer \(n\ge2\), let \(\mathcal H_j\) be the complex spherical harmonics of degree \(j\), and put \(V_n=\mathcal H_0\oplus\mathcal H_2\). Set
\[
\gamma_n=\frac{2\sqrt2(n-2)\sqrt{n+2}}{(n+4)\sqrt{n-1}},\qquad
\delta_n=\frac{3(n+2)(5n^2-13n+12)}{(n-1)(n+4)(n+6)}.
\]
For \(n=2\), let \(r_n=\sqrt3/2\). For each \(n\ge3\), let \(r_n>0\) be the unique positive zero of
\[
2r^3+3\gamma_n r^2+(\delta_n-3)r-\gamma_n=0.
\]
Then the exact sharp constant is
\[
\boxed{\sup_{0\ne f\in V_n}\frac{\int|f|^4\,d\sigma}{(\int|f|^2\,d\sigma)^2}
=\frac{r_n^4+6r_n^2+4\gamma_n r_n+\delta_n}{(1+r_n^2)^2}.}
\]
Write
\[
Y_\omega(x)=n\sqrt{\frac{n+2}{2(n-1)}}\left((\omega\cdot x)^2-\frac1n\right),\qquad \omega\in S^{n-1}.
\]
Every nonzero complex extremizer is **exactly** \(f=\lambda(r_n+Y_\omega)\), with \(\lambda\in\mathbb C\setminus\{0\}\) and \(\omega\in S^{n-1}\); conversely each is an extremizer. In particular, both harmonic components are always nonzero. For \(n=2\), the sharp quotient is \(15/7\); for \(n=4\), it is \(21/5\).

## Assumptions and scope
All functions are restrictions to the real unit sphere, all measures are probability-normalized, and complex coefficients are allowed. The degree-zero component consists of constants. Degree-two harmonics are trace-free homogeneous quadratic forms. No degree-one harmonics are included. The normalization gives \(\int Y_\omega\,d\sigma=0\) and \(\int Y_\omega^2\,d\sigma=1\).

## Proof
**Quadratic moments.** Let \(Q(x)=x^\top A x\) with a real symmetric trace-free \(n\times n\) matrix \(A\), and set \(p_j=\operatorname{tr}(A^j)\). Gaussian polar integration, using \(g=R x\) with standard Gaussian \(g\), gives the exact formulas
\[
\begin{aligned}
\mathbb E Q^2&=\frac{2p_2}{n(n+2)},\\
\mathbb E Q^3&=\frac{8p_3}{n(n+2)(n+4)},\\
\mathbb E Q^4&=\frac{12p_2^2+48p_4}{n(n+2)(n+4)(n+6)}.
\end{aligned}
\]
These follow directly from the Gaussian quadratic-form cumulants \(\kappa_j=2^{j-1}(j-1)!p_j\), the condition \(p_1=0\), and \(\mathbb E R^{2j}=n(n+2)\cdots(n+2j-2)\). We now prove the needed spectral bounds, including equality cases.

**Third power sum.** At fixed \(p_1=0\), \(p_2>0\), a maximum or minimum of \(p_3\) on this compact regular constraint manifold has, by Lagrange multipliers, at most two distinct eigenvalues: each satisfies a quadratic equation. If \(k\) entries equal one eigenvalue and \(n-k\) the other, direct substitution gives
\[
\frac{|p_3|}{p_2^{3/2}}=\frac{|n-2k|}{\sqrt{n k(n-k)}}.
\]
For \(n\ge3\), this is largest only for \(k=1\) or \(n-1\); its maximum is \((n-2)/\sqrt{n(n-1)}\). For \(n=2\), \(p_3=0\) identically. Hence
\[
|\mathbb E Q^3|\le\gamma_n(\mathbb E Q^2)^{3/2},
\]
with equality in positive sign for a rank-one-direction trace-free quadratic, up to a positive scalar (and for \(n=2\) every nonzero real quadratic has cubic moment zero).

**Fourth power sum.** The maximization of \(p_4\) under the same constraints has each eigenvalue a root of the cubic \(4t^3-2\lambda t-\eta\). For at most two distinct eigenvalues the quotient is
\[
\frac{p_4}{p_2^2}=\frac{n}{k(n-k)}-\frac3n,
\]
maximized for \(k=1\) or \(n-1\), with value \((n^2-3n+3)/(n(n-1))\). Suppose there are three distinct eigenvalues \(a<b<c\). A repeated extreme eigenvalue would allow a tangent perturbation \((1,-1)\) in two identical entries. The constrained Hessian along this direction is positive, since the derivative of the stationary cubic at either extreme is \(4(a-b)(a-c)>0\), or \(4(c-a)(c-b)>0\), contradicting a maximum. Therefore \(a\) and \(c\) each have multiplicity one and \(b\) has multiplicity \(n-2\). The stationary cubic has no quadratic term, so \(a+b+c=0\); trace-freeness gives \(a+(n-2)b+c=0\). For \(n\ge4\) this forces \(b=0\) and \(c=-a\), yielding \(p_4/p_2^2=1/2\), strictly less than the two-valued one-outlier value for \(n\ge4\). For \(n=3\), Newton's identities give \(p_4/p_2^2=1/2\) for every trace-free triple, and the two-valued case attains it. Thus
\[
\mathbb E Q^4\le\delta_n(\mathbb E Q^2)^2,
\]
with simultaneous equality in both the cubic and quartic inequalities for precisely the real zonal quadratics needed below. The second-moment normalization yields the stated \(Y_\omega\).

**Real optimization.** Every real \(f\in V_n\) is \(f=a+Q\), where \(a=\mathbb E f\) and \(Q\) is real trace-free quadratic. Put \(t=(\mathbb E Q^2)^{1/2}\). The preceding inequalities give
\[
\mathbb E(a+Q)^4\le a^4+6a^2t^2+4|a|\gamma_n t^3+\delta_n t^4.
\]
The upper bound is attained for every nonnegative magnitude pair \((|a|,t)\), choosing \(Q\) as a zonal quadratic and its sign to make the cubic mixed term nonnegative. For \(t>0\), write \(r=|a|/t\); dividing by \((a^2+t^2)^2\) gives
\[
F_n(r)=\frac{r^4+6r^2+4\gamma_n r+\delta_n}{(1+r^2)^2}.
\]
An exact derivative calculation gives
\[
F_n'(r)=-\frac{4(2r^3+3\gamma_nr^2+(\delta_n-3)r-\gamma_n)}{(1+r^2)^3}.
\]
For \(n\ge3\), \(\gamma_n>0\) and the cubic's coefficient sequence has exactly one sign change, irrespective of the sign of \(\delta_n-3\); it therefore has exactly one positive zero by Descartes' rule and its sign goes from negative to positive. Hence \(F_n\) has one global maximum at \(r_n>0\). For \(n=2\), \(F_2'(r)=-4r(2r^2-3/2)/(1+r^2)^3\), so its unique positive maximizing ratio is \(\sqrt3/2\); direct substitution gives \(15/7\). Both endpoints \(t=0\) and \(a=0\) have strictly smaller quotient. The cubic inequality's equality cases force the full stated real-extremizer classification for \(n\ge3\); in dimension two every trace-free quadratic is zonal after a rotation, giving the same statement.

**Complex extremizers.** Write any complex \(f\in V_n\) as \(u+iv\) with real \(u,v\in V_n\). If \(C_n\) denotes the just-proved real optimum, then
\[
\begin{aligned}
\mathbb E|f|^4&=\mathbb E u^4+2\mathbb E(u^2v^2)+\mathbb E v^4\\
&\le\bigl(\sqrt{\mathbb E u^4}+\sqrt{\mathbb E v^4}\bigr)^2\\
&\le C_n(\mathbb E u^2+\mathbb E v^2)^2.
\end{aligned}
\]
Equality in Cauchy--Schwarz entails \(u^2\) proportional to \(v^2\) almost everywhere unless one vanishes. On the connected real-analytic sphere, two real quadratic polynomial restrictions with proportional squares must themselves be linearly proportional: their product difference factors into two analytic functions whose product vanishes identically. Thus every complex extremizer has constant complex phase times a real extremizer. This proves the theorem.

## Verification
The supplied `checker.py` independently reconstructs the exact spherical even moments from the beta distribution of one coordinate, checks the normalized cubic and quartic zonal moments for dimensions \(2\le n\le25\), verifies the derivative identity symbolically, and checks the exact values \(C_2=15/7\), \(C_4=21/5\). It passed 144 assertions. Finite checks support, but do not replace, the proof above. Reproduce with `python checker.py` after installing SymPy.

## Relationship to prior work
The general work of Dai, Gorbachev, and Tikhonov establishes Nikolskii estimates for spherical polynomials and a lacunary harmonic regime. Their 2019 paper treats asymptotic-order estimates at degree separations at least three, not the exact sharp finite even packet \(\mathcal H_0\oplus\mathcal H_2\), whose separation is two. The published pure-degree-two sharp fourth-moment theorem concerns \(\mathcal H_2\) alone; it provides the quartic coefficient \(\delta_n\) but neither determines the new mixed sharp constant nor classifies its nonzero constant-component extremizers. General asymptotic spherical polynomial estimates likewise do not imply this finite-degree exact result.

## Limitations
This theorem concerns only constants plus degree-two spherical harmonics, with probability-normalized measure; degree-one and higher-degree components are excluded. It gives an algebraic cubic characterization rather than elementary radicals for general \(n\). Independent review and exhaustive historical-priority verification have not been performed. A formula equivalent under real quadratic-form moment inequalities in older literature remains a residual priority risk.

## References
- F. Dai, D. Gorbachev, S. Tikhonov, *Nikolskii inequality for lacunary spherical polynomials*, arXiv:1905.00323v1, May 1, 2019; particularly the assumptions and Theorem 1.
- F. Dai, D. Gorbachev, S. Tikhonov, *Nikolskii constants for polynomials on the unit sphere*, arXiv:1708.09837v1, August 31, 2017; published in Journal d'Analyse Mathématique 140 (2020), 161–185.
- *Sharp L4/L2 norm and extremizers for degree-two spherical harmonics*, published mathematical finding dated September 20, 2026; separate pure-degree-two comparison, not used as a premise of the proof.
