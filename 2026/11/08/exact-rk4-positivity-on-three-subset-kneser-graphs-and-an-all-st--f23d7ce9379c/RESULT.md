# Exact RK4 positivity on three-subset Kneser graphs and an all-step nonedge sign law

## Finding

For every integer \(n\ge9\), let \(G_n=KG(n,3)\) be the graph whose vertices are the three-element subsets of \(\{1,\ldots,n\}\), with adjacency exactly for disjoint pairs. Its degree is \(d_n=\binom{n-3}{3}\), adjacency matrix is \(A_n\), and combinatorial Laplacian is \(L_n=d_nI-A_n\). The completed classical fourth-order Runge–Kutta heat update is
\[
T_n(h)=I-hL_n+\frac{h^2L_n^2}{2}-\frac{h^3L_n^3}{6}+\frac{h^4L_n^4}{24},\qquad h\ge0.
\]
Put \(x=d_nh\). Define the four-by-four integer-polynomial matrix \(M_n\), indexed by \(r,s\in\{0,1,2,3\}\), by
\[
(M_n)_{rs}=\binom{3-r}{s}\binom{n-6+r}{3-s},
\]
with out-of-range binomial coefficients equal to zero. Set \(v^{(0)}=(0,0,0,1)^\mathsf T\), \(v^{(j+1)}=M_nv^{(j)}\), and
\[
p_{n,r}(x)=\sum_{j=0}^{4}\frac{x^j}{j!}\sum_{k=0}^{j}(-1)^{j-k}\binom jk\frac{v^{(k)}_r}{d_n^k}.
\]
These finite formulas specify rational polynomials exactly, without numerical root conventions. In particular \(p_{n,0}(x)=x f_n(x)\) for a cubic \(f_n\). **The cubic has exactly one positive real root \(\rho_n\)**, and
\[
\boxed{T_n(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad0\le h\le\rho_n/d_n.}
\]
Every diagonal entry and every off-diagonal entry between intersecting triples is strictly positive at every \(h>0\), including beyond the positivity threshold. Only entries joining disjoint triples can become negative; those entries vanish at \(h=\rho_n/d_n\) and remain negative for every larger \(h\). For illustration \(\rho_9\approx1.5536082883\), giving \(h_*\approx0.0776804144\). The strict all-step positivity of the intersecting-triple entries begins sharply at ground-set order nine: at \(n=8\), intersecting triples with one common element have entry \(x^2(43x^2-480x+1200)/240000\), which is negative at \(x=5\).

## Assumptions and scope

Here \(n\) is any integer at least nine; \(h\) is any real nonnegative timestep; all Kneser edges have unit weight; no intermediate Runge–Kutta stage constraints are imposed. Entrywise nonnegativity guarantees preservation of the nonnegative orthant for every initial vector. The graph is simple, finite, connected and regular. The theorem is about the completed RK4 matrix, not numerical rounding, a different Runge–Kutta method, unequal edge weights or arbitrary Kneser rank.

## Proof

Fix triples \(X,Y\), with \(r=|X\cap Y|\). A triple \(Z\) disjoint from \(X\) and meeting \(Y\) in \(s\) elements is obtained by choosing \(s\) of the \(3-r\) elements in \(Y\setminus X\), and \(3-s\) of the \(n-6+r\) elements outside \(X\cup Y\). Thus the number of such \(Z\) is exactly \((M_n)_{rs}\). An induction on the walk length shows \((A_n^j)_{XY}=v^{(j)}_r\). Expanding the polynomial \(T_n(x/d_n)\) proves that its \((X,Y)\) entry is precisely \(p_{n,r}(x)\).

For \(r=0\), direct expansion gives \(p_{n,0}(x)=x(c_0+c_1x+c_2x^2+c_3x^3)\). For every real \(n\ge9\), the rational coefficient signs are
\[
c_0>0,\qquad c_1<0,\qquad c_2>0,\qquad c_3<0,
\]
and the discriminant of \(c_1+2c_2x+3c_3x^2\) is strictly negative. Consequently the derivative \(f_n'(x)\) is negative at zero and everywhere else, and \(f_n\) decreases from a positive value to minus infinity. Hence it has exactly one positive root; \(p_{n,0}(x)\) is positive for \(0<x<\rho_n\) and negative for \(x>\rho_n\).

For \(r=1,2\), the same finite recurrence yields \(p_{n,r}(x)=x^2(a_r+b_rx+c_rx^2)\), with \(a_r>0\), \(c_r>0\) and \(b_r^2-4a_rc_r<0\) for all real \(n\ge9\). Both quadratic factors are therefore strictly positive for every real \(x\), establishing strict positivity on these two intersection classes for all positive timesteps.

For completeness, the stated nonstandard symbolic sign conditions are **finite polynomial identities with exact positive-coefficient certificates**, rather than claims inferred from parameter sampling. Substitute \(n=9+t\). In each of the eleven rational expressions \(c_0,-c_1,c_2,-c_3,-\operatorname{disc}_x(f_n'),a_1,c_1^{\mathrm{quad}},-\operatorname{disc}_x(a_1+b_1x+c_1^{\mathrm{quad}}x^2),a_2,c_2^{\mathrm{quad}},-\operatorname{disc}_x(a_2+b_2x+c_2^{\mathrm{quad}}x^2)\), the simplified denominator is positive and **every coefficient of the numerator in \(t\)** is strictly positive. The embedded `verify.py` constructs each expression from the displayed recurrence, expands these eleven exact integer polynomials, and asserts these signs for all coefficients, including the constant terms. Since \(t\ge0\), these checks prove all required inequalities for the full continuum \(n\ge9\), not just a finite sample. The coefficient identities are mechanically reproducible using symbolic integer and rational arithmetic and are the explicit finite algebraic certificates in the proof.

Finally \(L_n\) is symmetric positive semidefinite. For every real \(y\ge0\), the fourth-order exponential Taylor polynomial \(R_4(-y)=\sum_{j=0}^4(-y)^j/j!\) is strictly positive: Taylor's integral remainder gives \(R_4(-y)>e^{-y}>0\) for \(y>0\). Therefore \(T_n(h)=R_4(-hL_n)\) is positive definite, and its diagonal entries are strictly positive. Taken together, the four classes give the asserted if-and-only-if result and its nonreentrant sign law. For the \(n=8\) boundary, direct substitution in the same recurrence gives the displayed quadratic, whose value at \(x=5\) is \(-5/384\).

## Verification

Run `python verify.py` in a directory containing the embedded file, with SymPy installed (see `requirements.txt`). It reconstructs the four-class walk recurrence, checks the eleven all-parameter symbolic sign certificates exactly, and compares all adjacency-power entries through degree four with independently enumerated graphs at \(n=9,10,11\). The actual extracted run returned `VERIFY_OK 11 universal shifted-sign certificates; 1845 direct adjacency-power entries; positivity for all integer n>=9`. The graph enumerations are independent spot checks, not the infinite proof, which relies on the algebraic sign certificates. No external computer proof assistant, formal certification, or independent mathematical audit is claimed.

## Relationship to prior work

The underlying disjoint-subset graph is the classical Kneser graph as described, for example, by Matoušek and Ziegler (2002). Horváth (2004/2005) analyzes positivity-step thresholds of general Runge–Kutta methods and invariant cones, not the exact Kneser-family completed-RK4 sign classification. Bresten and collaborators (2013) study multistep SSP Runge–Kutta coefficients rather than the fixed standard RK4 endpoint on Kneser graph diffusion. Known exact results for the Johnson graph \(J(n,3)\), whose adjacency means *two* common elements rather than zero, do not imply the present result: their adjacency and walk algebras differ, despite both acting on triples. Likewise generic strongly regular graph results do not cover \(KG(n,3)\), which is not strongly regular at \(n\ge9\). The exact named comparisons and residual literature risk are recorded in `AUDIT.json`.

## Limitations

The threshold is given as the unique root of an explicitly specified cubic rather than in radicals. No result is asserted for \(n\le8\) except the displayed boundary witness; those cases may have different graph-distance behavior. General rank \(k\), edge weights, and intermediate RK stages are outside the claim. A negative literature search cannot establish priority against every obscure, unpublished, or unindexed equivalent theorem. The review is same-model only and has not been independently audited.

## References

1. J. Matoušek and G. M. Ziegler, *Topological lower bounds for the chromatic number: A hierarchy*, arXiv:math/0208072, first submitted 9 August 2002, https://arxiv.org/abs/math/0208072.
2. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics **53** (2005), 341–356, available online 27 October 2004, https://doi.org/10.1016/j.apnum.2004.08.026.
3. C. Bresten, S. Gottlieb, Z. Grant, D. Higgs, D. I. Ketcheson and A. Németh, *Strong Stability Preserving Multistep Runge–Kutta Methods*, arXiv:1307.8058, first submitted 30 July 2013, https://arxiv.org/html/1307.8058v2.
