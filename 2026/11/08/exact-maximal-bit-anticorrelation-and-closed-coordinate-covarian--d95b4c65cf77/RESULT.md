# Exact maximal bit anticorrelation and closed coordinate covariance in a fixed-point-free affine map

## Finding

The two-branch fixed-point-free map introduced in Lawnik–Moysis–Volos (2023), restricted to the natural equal-endpoint affine family, admits **exact stationary covariance formulas for both its coordinate and its branch bit at every time lag**. These formulas identify a sharp obstruction to using this family as a source of decorrelated binary output.

For real parameters \(0<s,b<1\), define a map on \([0,1]\) by
\[
F_{s,b}(x)=\begin{cases}
s+(1-s)x/b,&0\le x\le b,\\
s(x-b)/(1-b),&b<x\le1.
\end{cases}
\]
Let \(\widehat F_{s,b}\) denote the associated circle map, with \(0\) and \(1\) identified. Throughout, formulas for symbolic orbits use its canonical representative in \([0,1)\). Set \(\delta=s+b-1\). When \(\delta\ne0\), write
\[
q=\frac{sb}{\delta},\quad
L=\log\frac{(1-s)(1-b)}{sb},\quad
\rho=\frac{\log((1-s)/b)}{L}.
\]
When \(\delta=0\), set \(L=0\) and \(\rho=s\). Always \(0<\rho<1\). The circle map is exactly conjugate to rotation by \(\rho\): for \(\delta\ne0\),
\[
h(x)=\frac{\log|x-q|-\log|-q|}{L}\pmod1,
\qquad h\circ\widehat F_{s,b}=R_\rho\circ h,
\]
where \(R_\rho(u)=u+\rho\pmod1\). If \(\delta=0\), take \(h(x)=x\). Let \(\mu=h^{-1}_*\mathrm{Leb}\) be the probability invariant under \(\widehat F_{s,b}\), let \(X_n=\widehat F_{s,b}^{\circ n}(X_0)\), and define \(B_n={\bf1}_{\{X_n>b\}}\), with \(X_0\sim\mu\). Set \(t_n=\{n\rho\}\in[0,1)\).

**Exact all-lag coordinate covariance.** With \(m=\mathbb E_\mu[X_0]\), for every integer \(n\ge0\),
\[
\operatorname{Cov}_\mu(X_0,X_n)=K_L(t_n),\quad
K_L(t)=\begin{cases}
\dfrac{\cosh(|L|(\tfrac12-t))}{2|L|\sinh(|L|/2)}-\dfrac1{L^2},&L\ne0,\\[5pt]
\dfrac12(t^2-t+\tfrac16),&L=0.
\end{cases}
\]
In particular, this is an exact formula, rather than an asymptotic or a numerical fit.

**Exact branch-bit covariance and sharp anticorrelation.** The natural branch bit has mean \(\mathbb E_\mu[B_n]=\rho\), and for every integer \(n\ge0\),
\[
\operatorname{Cov}_\mu(B_0,B_n)=(\rho-t_n)_++(\rho+t_n-1)_+-\rho^2,
\qquad v_+=\max(v,0).
\]
At lag one this reaches the lowest covariance possible for any pair of Bernoulli random variables with a common success probability \(\rho\):
\[
\boxed{\operatorname{Cov}_\mu(B_0,B_1)=-\min\{\rho,1-\rho\}^2.}
\]
More strongly, outside the countable set of trajectories meeting a branch boundary, the bit sequence is a mechanical rotation code. If \(\rho\) is irrational, it is Sturmian and has **exactly \(N+1\) distinct length-\(N\) factors for every \(N\ge1\)**, as well as the deterministic discrepancy bound
\[
\left|\sum_{j=0}^{N-1}B_j-N\rho\right|<1
\quad(N\ge1).
\]
For rational \(\rho=p/q\) in lowest terms, every circle orbit has period \(q\) and every branch-bit word is periodic. For irrational \(\rho\), the coordinate and branch-bit covariances have nonzero recurrent excursions rather than decay to zero. In fact,
\[
\limsup_{n\to\infty}\operatorname{Cov}(B_0,B_n)=\rho(1-\rho),\quad
\liminf_{n\to\infty}\operatorname{Cov}(B_0,B_n)=-\min\{\rho,1-\rho\}^2.
\]

## Assumptions and scope

The map is precisely the \(d=1\), \(a=c=s\) subfamily of equation (15) in Lawnik–Moysis–Volos (2023), with the paper's threshold \(b\). The equal-endpoint condition \(F(0)=F(1)=s\) makes the interval map a continuous, orientation-preserving circle homeomorphism after endpoint identification. This identification matters: the source's convention gives \(F(b)=1\), whereas the canonical representative of the circle image of \(b\) is \(0\). These values are identical on the circle but generate different single-bit representatives at exceptional boundary encounters; the covariance statements are unaffected, since such points form a null set under \(\mu\). Symbolic statements are made for canonical circle representatives or for real orbits avoiding boundaries.

The specified \(\mu\) is invariant for every parameter. For irrational \(\rho\), it is the unique invariant probability measure of the circle homeomorphism. For rational \(\rho\), invariant probabilities are not unique; the covariance formulas refer only to the explicitly defined \(\mu\), not to arbitrary invariant measures. These formulas do not claim any mixing or chaotic behavior. The claim is a complete quantitative covariance law for two natural observables in this family, not a new general theorem about circle rotations or the previously known rotation-number formula.

## Proof

**1. Explicit conjugacy and reference measure.** The branch slopes are
\[
\alpha=\frac{1-s}{b},\qquad \beta=\frac{s}{1-b}.
\]
If \(\delta\ne0\), direct substitution gives the common affine fixed center \(q=sb/\delta\): on either branch, \(F(x)-q=\alpha(x-q)\) or \(F(x)-q=\beta(x-q)\), respectively. When \(\delta<0\), \(q<0\); when \(\delta>0\), \(q>1\). Furthermore
\[
\frac{1-q}{-q}=\frac{(1-s)(1-b)}{sb}=\frac\alpha\beta,
\]
so \(L=\log(\alpha/\beta)\), and \(h(0)=0\), \(h(1)=1\), \(h'(x)=1/[L(x-q)]>0\). On the left branch, \(h(F(x))-h(x)=\log\alpha/L=\rho\); on the right branch it is \(\log\beta/L=\rho-1\). These are the same on the circle. If \(\delta=0\), \(\alpha=\beta=1\) and \(F(x)=x+s\pmod1\) directly. Thus \(h\) is the required orientation-preserving conjugacy.

In particular, when \(L\ne0\) the invariant measure has the explicit density
\[
\frac{d\mu}{dx}=\frac{1}{|L|\,|x-q|}\quad(0<x<1),
\]
while \(\mu\) is uniform when \(L=0\). The inverse conjugacy on \([0,1)\) is
\[
X(u)=q(1-e^{Lu})\quad(L\ne0),\qquad X(u)=u\quad(L=0),
\]
where \(u\) is uniform, and \(X_n=X(\{u+n\rho\})\). The mean for \(L\ne0\) is \(m=q+1/L\), and for \(L=0\) it is \(1/2\).

**2. Fourier coefficients and coordinate covariance.** For each nonzero integer \(k\), direct integration yields
\[
\widehat X(k)=\int_0^1X(u)e^{-2\pi iku}\,du
=-q\frac{e^L-1}{L-2\pi ik}=\frac{1}{L-2\pi ik},
\]
because \(-q(e^L-1)=1\). The same expression extends to \(L=0\) by continuity. Parseval's identity on the rotation circle now gives
\[
\operatorname{Cov}(X_0,X_n)
=\sum_{k\in\mathbb Z\setminus\{0\}}
\frac{e^{2\pi ikt_n}}{L^2+4\pi^2k^2}.
\]
This series is absolutely convergent. When \(L\ne0\), the complete periodic Green function of \(-d^2/du^2+L^2\) is
\[
G_L(t)=\frac{\cosh(|L|(\tfrac12-t))}{2|L|\sinh(|L|/2)}\quad (0\le t\le1).
\]
Indeed, \(G_L\) solves the homogeneous equation away from the origin, is periodic with continuous values, and has derivative jump \(-1\), so its Fourier coefficient at \(k\) is \((L^2+4\pi^2k^2)^{-1}\). Subtracting its constant Fourier mode \(1/L^2\) proves \(K_L\). If \(L=0\), integrate the corresponding zero-mean Green equation twice to obtain \(K_0(t)=\tfrac12(t^2-t+1/6)\). This proves the coordinate formula, including the exact degenerate boundary.

**3. Branch code, exact bit covariance, and extremality.** Because the left endpoint \(b\) maps to the top endpoint \(1\), the rotation conjugacy shows \(h(b)=1-\rho\). Thus \(B_n={\bf1}_{[1-\rho,1)}(\{u+n\rho\})\) except on null boundary cases. This is precisely
\[
B_n=\lfloor u+(n+1)\rho\rfloor-\lfloor u+n\rho\rfloor.
\]
Telescoping proves \(\sum_{j=0}^{N-1}B_j=\lfloor u+N\rho\rfloor\) for \(0\le u<1\) and the strict discrepancy bound at all nonboundary phases. A circle interval of length \(\rho\) overlapping its translate by \(t_n\) has Lebesgue length \((\rho-t_n)_++(\rho+t_n-1)_+\). Subtracting the squared mean gives the bit covariance. For lag one, \(t_1=\rho\), hence the joint success probability is \((2\rho-1)_+\) and the centered covariance is \(-\min(\rho,1-\rho)^2\). The Fréchet inequality \(\Pr(B_0=B_1=1)\ge\max(0,2\rho-1)\) proves this is the absolute possible lower covariance for the stated marginals. For irrational \(\rho\), every infinite code is aperiodic, while the length-\(N\) partition has at most \(N+1\) cells; the Morse–Hedlund lower bound forces exactly \(N+1\) distinct factors. Density of \(\{n\rho\}\) and continuity of the covariance kernel give the claimed limsup and liminf. For rational \(\rho\), the conjugacy to the rigid \(q\)-cycle gives the exact periodicity claim.

**4. Nonexpansion statement.** Away from finitely many branch encounters, \((F^{\circ n})'(x)=(F^{\circ n}(x)-q)/(x-q)\) because the same affine center applies to every branch. Since \(q\notin[0,1]\), these derivatives are bounded above and away from zero uniformly in \(n\), giving Lyapunov exponent zero at all such points. In the \(L=0\) case every derivative equals one. This is compatible with the nondecaying covariance and confirms that the two-branch map is an integrable, nonmixing circle system on the chosen surface. This last observation is background to the covariance result, not the novelty claim.

## Verification

The self-contained Python 3 file `check.py` evaluates the map and inverse conjugacy independently, numerically integrates the centered stationary covariances for the coordinate and branch bit at lags \(0,1,2,3,11\), and compares these computations with both analytical kernels for six parameter pairs, including both sides of \(s+b=1\) and the exact equal-slope case. Run `python3 check.py` from the same directory. Its terminal success marker is `CIRCLE_COVARIANCE_AND_STURMIAN_CHECK_OK`. The numerical quadrature approximates piecewise continuous integrands and has a finite grid error; it is not a proof of the all-lag identities or Sturmian complexity. The complete proof is analytical above.

## Relationship to prior work

Lawnik–Moysis–Volos (2023), Section 4, equation (15), supplies this map family and numerical phase/Lyapunov diagrams; it acknowledges nonchaotic parameter regions but does not provide the present stationary coordinate or branch-bit covariance functions. Laurent–Nogueira (2021), Corollary on page 36, gives the logarithmic rotation number of a broad two-interval affine circle-homeomorphism family; the rotation-number formula and generic circle conjugacy are therefore **not claimed as original**. Their work does not state the specific stationary observables, the hyperbolic-cosine all-lag covariance, the exact branch-bit joint law, or Fréchet-sharp lag-one anticorrelation for this map. Gaivão–Laurent–Nogueira (2024) further studies rotation numbers for piecewise affine interval maps; it too is background to the rotation classification rather than a source of the stated covariance identities. The all-lag covariance identities are the added observable-level results, with a direct implication for deterministic bit generation.

## Limitations

The theorem is restricted to \(d=1\) and the equal-endpoint surface \(a=c\). It does not classify chaotic regions of the full nonlinear source family. The interval convention at the discontinuity must be handled by identifying endpoints or excluding the countable set of boundary-hitting initial states. Rational rotation admits many invariant measures, so all stationary covariance assertions explicitly use \(\mu=h^{-1}_*\mathrm{Leb}\). This is an explicit special-family calculation; broader classical rotation theory is fully acknowledged. Equivalent observable-level calculations in literature not found by the searches remain possible, and no independent mathematical audit has been performed.

## References

1. M. Lawnik, L. Moysis, C. Volos, *A Family of 1D Chaotic Maps without Equilibria*, Symmetry **15** (2023), 1311, DOI:10.3390/sym15071311. First public date verified from the paper: 2023-06-27. Equation (15), Section 4 and Figures 4–5.
2. M. Laurent, A. Nogueira, *Dynamics of 2-interval piecewise affine maps and Hecke–Mahler series*, Journal of Modern Dynamics **17** (2021), 33–63; arXiv:1907.08655. See Corollary on printed page 36 for the already-known logarithmic rotation number.
3. J. P. Gaivão, M. Laurent, A. Nogueira, *Rotation number of 2-interval piecewise affine maps*, Aequationes Mathematicae **99** (2025), 511–530, first public online 2024-04-22, DOI:10.1007/s00010-024-01064-2. Its MSC classifications include 37E05.
4. A. Dzhalilov, D. Mayer, S. Djalilov, A. Aliyev, *An Extension of Herman's Theorem for Nonlinear Circle Maps with Two Breaks*, Russian Journal of Nonlinear Dynamics **14** (2018), 553–577, DOI:10.20537/nd180409. Background on absolutely continuous invariant measures of circle maps with break points.
