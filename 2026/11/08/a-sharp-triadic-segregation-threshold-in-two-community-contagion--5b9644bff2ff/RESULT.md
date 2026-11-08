# A sharp triadic segregation threshold in two-community contagion

## Finding
For the triangle-only, equal-community mean-field system of Landry and Restrepo (2023), let the normalized triadic transmission rate be \(\lambda>0\), and let the triangle community-assortativity parameter satisfy \(0\leq\varepsilon<1\). There is a **hyperbolically locally asymptotically stable unequal-prevalence equilibrium** for at least one \(\lambda\) if and only if
\[
\varepsilon>\varepsilon_*:=\frac{9+24\sqrt3}{61}\approx0.829003596420542.
\]
For \(\varepsilon<\varepsilon_*\), every unequal-prevalence equilibrium, if one exists, is a hyperbolic saddle. At \(\varepsilon=\varepsilon_*\), no unequal-prevalence equilibrium is hyperbolically asymptotically stable: any such equilibrium has nonpositive determinant, with the only possible zero at a nonhyperbolic point. At every \(\varepsilon\in(\varepsilon_*,1)\), the theorem constructs two distinct, symmetry-related, hyperbolically stable unequal-prevalence equilibria at a suitable positive transmission rate.

## Assumptions and scope
The state variables \(x,y\in[0,1]\) are the infected/adopting fractions of two equally sized communities, with recovery rate normalized to one, zero pairwise transmission, and only three-person transmission. The model is **exactly the triangle-only restriction of equations (15)–(16)** of Landry and Restrepo, *Opinion disparity in hypergraphs with community structure* (2023):
\[
\begin{aligned}
\dot x&=-x+\frac{\lambda}{4}(1-x)\bigl[(x+y)^2+\varepsilon(3x^2-2xy-y^2)\bigr],\\
\dot y&=-y+\frac{\lambda}{4}(1-y)\bigl[(x+y)^2+\varepsilon(3y^2-2xy-x^2)\bigr].
\end{aligned}
\]
Here \(\varepsilon=0\) corresponds to no triangle community preference, while \(\varepsilon\uparrow1\) approaches disconnection of the two communities. Both \(\lambda\) and \(\varepsilon\) are held constant. The result concerns equilibria and their local linear stability in this deterministic two-dimensional mean-field model, not finite-population stochastic absorption or arbitrary pairwise transmission.

## Proof
Set \(s=(x+y)/2\) and \(d=(x-y)/2\). Exact algebra yields
\[
\begin{aligned}
\dot s&=-s+\lambda\bigl[s^2(1-s)+\varepsilon d^2(1-3s)\bigr],\\
\dot d&=d\bigl[-1+\lambda(2\varepsilon s(1-s)-s^2-\varepsilon d^2)\bigr]. \tag{1}
\end{aligned}
\]
If \(\varepsilon<1\), an asymmetric equilibrium cannot lie on the boundary of the unit square: at \((x,0)\) with \(x>0\), the second right-hand side is \(\lambda(1-\varepsilon)x^2/4>0\), and neither variable can equal one at equilibrium. For \(\varepsilon=0\), direct subtraction of the two equations also rules out asymmetric equilibria. Thus consider \(0<\varepsilon<1\) and \(d\ne0\), with \(0<x,y<1\).

At equilibrium, equating each infection pressure to the corresponding odds \(x/(1-x)\) and \(y/(1-y)\), then subtracting, gives
\[
\lambda=\frac{1}{2\varepsilon sQ},\qquad Q=(1-s)^2-d^2>0.
\]
Substitution into the mean equation in (1) yields
\[
d^2=\frac{s^2[2\varepsilon(1-s)-1]}{\varepsilon(1-2s)}.\tag{2}
\]
The physical constraints \(0<x,y<1\) imply \(0<|d|<s\) and \(|d|<1-s\). If \(s\ge1/2\), formula (2) forces \(d^2>s^2\) (and at \(s=1/2\) has no solution), contradicting these constraints. Therefore every asymmetric equilibrium satisfies
\[
\frac12<\varepsilon<1,\qquad 0<s<1-\frac{1}{2\varepsilon}<\frac12.
\]
Conversely, for any such \(s,\varepsilon\), (2) gives \(0<d^2<s^2\) and \(Q>0\), and the displayed \(\lambda\) gives exactly two asymmetric equilibria \((s\pm d,s\mp d)\).

Define
\[
\begin{aligned}
D(s,\varepsilon)&=3\varepsilon s^2-4\varepsilon s+\varepsilon+s^2,\\
P(s,\varepsilon)&=\varepsilon(12s^3-17s^2+8s-1)+4s^3-3s^2,\\
T(s,\varepsilon)&=\varepsilon(2s^2-s-1)+2s^2-s+1.
\end{aligned}
\]
At an asymmetric equilibrium, \(D=\varepsilon(1-2s)Q>0\). Differentiating (1), imposing both equilibrium identities, and simplifying gives the exact Jacobian invariants
\[
\operatorname{tr}J=\frac{T}{D},\qquad
\det J=\frac{[2\varepsilon(1-s)-1]P}{D^2}.\tag{3}
\]
The prefactor of \(P\) is strictly positive. Thus any \(P<0\) gives a saddle, and \(P>0\), together with \(T<0\), gives a hyperbolic sink.

Write \(A(s)=12s^3-17s^2+8s-1\). If \(s\le1/4\) and \(A(s)\le0\), then \(P<0\); if \(A(s)>0\), monotonicity in \(\varepsilon<1\) and the identity \(P(s,1)=(2s-1)^2(4s-1)\le0\) again give \(P<0\). For \(1/4<s<1/2\), \(A(s)>0\) (its derivative is \(36(s-4/9)(s-1/2)\), and its endpoint values are positive). Set
\[
F(s)=\frac{s^2(3-4s)}{A(s)}.
\]
In this interval \(P>0\) precisely when \(\varepsilon>F(s)\). Its derivative factors as
\[
F'(s)=\frac{2s(2s-1)(8s^2-12s+3)}{A(s)^2}.
\]
Consequently \(F\) has the unique global minimum at \(s_*=(3-\sqrt3)/4\), and direct simplification gives \(F(s_*)=\varepsilon_*\).

Finally, \(P>0\) automatically entails \(T<0\). Indeed, with \(R(s)=8s^4-14s^3+16s^2-7s+1\),
\[
T(s,F(s))=\frac{(2s-1)R(s)}{A(s)}<0.
\]
To see \(R(s)>0\), put \(u=4s-1\); then
\[
32R(s)=\left(u^2-\tfrac32u\right)^2+\frac{59}{4}\left(u-\frac{18}{59}\right)^2+\frac{37}{59}>0.
\]
Moreover \(T\) strictly decreases with \(\varepsilon\) on \(1/4<s<1/2\). Hence equations (3) and the minimization of \(F\) rule out hyperbolic asymmetric sinks for \(\varepsilon\le\varepsilon_*\).

For any \(\varepsilon\in(\varepsilon_*,1)\), choose \(s=s_*\). Because \(\varepsilon_*>\sqrt3-1=1/[2(1-s_*)]\), formula (2) gives an admissible positive \(d^2<s_*^2\). Choose \(\lambda=[2\varepsilon s_*((1-s_*)^2-d^2)]^{-1}\). Then \(P>0\) and \(T<0\), proving the existence of the two asserted sinks. At the boundary \(\varepsilon=\varepsilon_*\), any determinant-zero asymmetric equilibrium must have \(s=s_*\), and is nonhyperbolic. This proves the stated hyperbolic threshold.

An exact interior example is \(\varepsilon=9/10\), \(s=1/3\), \(d^2=2/27\), \(\lambda=9/2\). Its two equilibria are \((1/3\pm\sqrt{2/27},1/3\mp\sqrt{2/27})\), with Jacobian trace \(-1\) and determinant \(6/25\), hence eigenvalues \(-2/5,-3/5\).

## Verification
Run `python3 verify.py` from this directory with Python 3.9 or later. It uses only the standard library and exactly checks the original two vector-field equilibrium equations in a rational quadratic extension for 544 admissible rational parameter pairs, as well as the independent Jacobian trace and determinant expressions. It also checks the explicit stable witness and discriminant-threshold approximation. A separate symbolic-algebra identity check established the displayed factorizations. Numerical and finite algebraic tests are not substituted for the preceding universal analytic proof.

## Relationship to prior work
Landry and Restrepo (arXiv:2302.13967, equations (15)–(20), numerical phase diagrams in Figures 3–5) derive the two-community mean-field model, characterize symmetric equilibria, and numerically locate disparity regions for selected combined pairwise/triadic interaction parameters. The present theorem takes their natural pure-triadic parameter axis and obtains an exact algebraic minimum over *all positive triadic transmission rates* for hyperbolically attracting asymmetric equilibria, including a constructive parameterization and universal exclusion below the threshold. Cisneros-Velarde and Bullo (arXiv:2005.11404) give general sufficient bistability conditions for multi-group simplicial SIS systems, but not an exact critical community-assortativity constant for these equations. Cui et al. (arXiv:2306.00619) treat a more general directed hypergraph SIWS framework, including indirect pathways; its broad epidemic results do not explicitly supply this exact sharp two-community pure-triad threshold. The proof here does not assert that the general concepts of higher-order contagion or symmetry-breaking multistability are new.

## Limitations
The conclusion concerns local hyperbolic stability, not global basins of attraction. At the critical parameter \(\varepsilon=\varepsilon_*\), the determinant vanishes at a special nonhyperbolic equilibrium, whose nonlinear stability is not classified here; this is explicitly excluded from the positive statement. The disconnected endpoint \(\varepsilon=1\), nonzero pairwise transmission, imbalanced communities, and finite-population stochastic extinction are outside scope. Literary priority remains subject to unindexed equivalent results and further independent examination of broader models.

## References
1. Nicholas W. Landry and Juan G. Restrepo, *Opinion disparity in hypergraphs with community structure*, arXiv:2302.13967 (first public version 2023-02-27), Physical Review E 108, 034311 (2023). https://arxiv.org/abs/2302.13967 ; https://doi.org/10.1103/PhysRevE.108.034311
2. Pedro Cisneros-Velarde and Francesco Bullo, *Multi-group SIS Epidemics with Simplicial and Higher-Order Interactions*, arXiv:2005.11404. https://arxiv.org/abs/2005.11404
3. Shaoxuan Cui, Fangzhou Liu, Hildeberto Jardón-Kojakhmetov and Ming Cao, *General SIS diffusion process with indirect spreading pathways on a hypergraph*, arXiv:2306.00619. https://arxiv.org/abs/2306.00619
