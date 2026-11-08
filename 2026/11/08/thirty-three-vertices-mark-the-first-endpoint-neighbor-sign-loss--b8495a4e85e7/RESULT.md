# Thirty-three vertices mark the first endpoint-neighbor sign loss for TR-BDF2 diffusion on paths

## Finding

Let \(P_n\) be the unweighted path on \(n\ge2\) vertices, numbered \(0,1,\ldots,n-1\), and let \(L_n\) be its combinatorial Laplacian. Consider the L-stable, second-order TR-BDF2 end-step for \(u'=-L_nu\), with amplification function
\[
F(z)=\frac{1-(\sqrt2-1)z}{[1+(1-1/\sqrt2)z]^2},\qquad T_n(h)=F(hL_n).
\]
The end-step coefficient transporting unit mass from the first vertex to its neighboring vertex obeys the sharp, complete size classification
\[
\boxed{(T_n(h))_{0,1}>0\ \text{for every }h>0\ \Longleftrightarrow\ 2\le n\le32.}
\]
For every \(n\ge33\), this same coefficient is **strictly negative** at the explicitly given positive timestep
\[
\boxed{h=\frac{110}{1-1/\sqrt2}.}
\]
For \(n\ge33\), the coefficient is positive for sufficiently small and sufficiently large positive timesteps, so its negative set contains a bounded nonempty open interval. No assertion is made here about other entries of \(T_n(h)\) or the number of connected components in that negative set.

## Assumptions and scope

The graph has simple unit-conductance edges and reflecting/graph-Neumann boundary vertices (endpoint degree one). The propagation is the unmodified TR-BDF2 end-step, not stagewise positivity or a limiter/hybrid. The timestep \(h\) is arbitrary positive real, with the dimensionless resolvent parameter \(s=(1-1/\sqrt2)h>0\). The claim concerns exactly the endpoint-adjacent coefficient \((0,1)\), which equals \((n-1,n-2)\) by reflection, for every integer \(n\ge2\). It does not claim entrywise nonnegativity of the entire step operator for small paths.

## Proof

**1. Reduction to a resolvent-ratio test.** Write \(R=(I+sL_n)^{-1}\). Direct partial fraction calculation using \(s=(1-1/\sqrt2)h\) gives
\[
T_n(h)=(1+\sqrt2)R^2-\sqrt2 R.
\]
Because \(I+sL_n\) is an irreducible nonsingular M-matrix, \(R_{0,1}>0\). Thus
\[
(T_n(h))_{0,1}>0\quad\Longleftrightarrow\quad
\rho_n(s):=\frac{(R^2)_{0,1}}{R_{0,1}}>2-\sqrt2.
\]
Differentiating the resolvent yields \(R^2=R+sR'\), so \(\rho_n=1+s\,\partial_s\log R_{0,1}\).

**2. Exact kernel.** Define \(\theta>0\) uniquely by \(\cosh\theta=1+1/(2s)\). The tridiagonal resolvent obeys, for \(0\le i\le j\le n-1\),
\[
R_{i,j}=\frac{\cosh((i+1/2)\theta)\cosh((n-j-1/2)\theta)}{s\sinh\theta\sinh(n\theta)}.
\]
This formula follows from the two linearly independent solutions \(\cosh((i+1/2)\theta)\) and \(\cosh((n-i-1/2)\theta)\) of the interior Jacobi recurrence: each satisfies its endpoint equation, and their discrete Wronskian equals \(\sinh\theta\sinh(n\theta)\). It is directly verifiable by multiplication by \(I+sL_n\), including the diagonal jump and both boundary equations.

Differentiating \(\cosh\theta=1+1/(2s)\) gives \(s\theta'=-\tanh(\theta/2)\). Substitution into the kernel yields the exact identity
\[
\rho_n(s)=\frac12+\tanh(\theta/2)\left[n\coth(n\theta)-(n-3/2)\tanh((n-3/2)\theta)\right]. \tag{1}
\]
The continuous endpoint limits of this ratio are \(2\) as \(s\downarrow0\), and \(1\) as \(s\to\infty\), for every fixed \(n\).

**3. Strict decrease in path size.** For fixed \(\theta>0\) and real \(n\ge3\), define \(x=n\theta\), \(y=(n-3/2)\theta\), and \(g_n=n\coth(n\theta)-(n-3/2)\tanh((n-3/2)\theta)\). As \(y\ge x/2\),
\[
\frac{dg_n}{dn}=A(x)-B(y),\quad
A(x)=\coth x-x\operatorname{csch}^2x,\quad
B(y)=\tanh y+y\operatorname{sech}^2y.
\]
For all \(x>0\), \(A(x)<1\), because \(x>(1-e^{-2x})/2\). If \(y\ge1\), then \(B(y)>1\), since \(y(1+\tanh y)>1\). If \(y<1\), then \(B\) is increasing on \((0,1)\), and \(B(y)\ge B(x/2)>A(x)\). For the last strict inequality, put \(t=x/2\) and \(w=\tanh t\), and calculate
\[
B(t)-A(2t)=\frac{1-w^2}{2w^2}[t(1+w^2)-w]>0.
\]
Therefore \(g_n\), and hence \(\rho_n(s)\), decreases strictly as \(n\) increases through integers \(n\ge3\), for every fixed \(s>0\).

**4. A finite exact positivity certificate at size 32.** Put \(r=e^{-\theta}\in(0,1)\), so \(s=r/(1-r)^2\). From (1), after cancelling \(1-r\),
\[
\rho_n(s)=\frac12+\frac{A_n(r)}{2B_n(r)},
\]
where
\[
A_n(r)=3+(4n-3)(r^{2n-3}+r^{2n})+3r^{4n-3},
\]
\[
B_n(r)=(1+r)\left(\sum_{j=0}^{2n-1}r^j\right)(1+r^{2n-3})>0.
\]
The exact rational inequalities \(1.41421<\sqrt2<1.41422\) give
\[
\frac{58578}{100000}<2-\sqrt2<\frac{58579}{100000}.
\]
For \(n=32\), it therefore suffices to establish strict positivity on \([0,1]\) of
\[
P(r)=50000A_{32}(r)-8579B_{32}(r).
\]
The polynomial has degree \(125\). Its degree-125 Bernstein control coefficients are **strictly positive** on each of the four intervals
\[
[0,1/2],\quad[1/2,3/4],\quad[3/4,7/8],\quad[7/8,1].
\]
This is an exact-rational, fully reproduced certificate, not a floating-point plot: the accompanying `verify.py` constructs both integer power-basis polynomials, forms the rational Bernstein controls, bisects with de Casteljau arithmetic, and checks every control coefficient is strictly positive. Their smallest numerical displayed value is about \(1154.04\) (the underlying comparison is exact). Positivity of Bernstein basis functions proves \(P(r)>0\) throughout \([0,1]\). Hence \(\rho_{32}(s)>2-\sqrt2\) for every \(s>0\), and step 3 extends this to all \(3\le n\le32\). For \(n=2\), direct inversion gives \(\rho_2(s)=2(1+s)/(1+2s)>1\).

**5. An exact negative witness at size 33 and its persistence.** At \(r=10/11\), equivalently \(s=110\), exact integer/rational arithmetic gives
\[
50000A_{33}(10/11)-8578B_{33}(10/11)<0.
\]
The accompanying verifier checks the sign without rounding. It follows that \(\rho_{33}(110)<58578/100000<2-\sqrt2\). Step 3 implies \(\rho_n(110)<2-\sqrt2\) for every \(n\ge33\). The first reduction therefore gives a negative endpoint-neighbor transition at the stated timestep. The endpoint limits in step 2 and continuity yield positivity near zero and infinity.

## Verification

Run `python verify.py` with a standard Python 3 interpreter. The verifier performs the four exact-rational Bernstein interval checks for the degree-125 polynomial, the rational size-33 negative witness, rational enclosures of \(\sqrt2\), and independent exact matrix-inverse checks for small paths. A passing run prints `VERIFY_OK`. The infinite size statements are established analytically by step 3; the finite certificate supplies only the explicit dimension-32 polynomial inequality. No use of numerical root finding is needed.

## Relationship to prior work

Hosea and Shampine (1996) establish the TR-BDF2 method's stability function and efficient implementation; Bonaventura and Della Rocca (first publicly posted 2015) establish general positivity and strong-stability constraints for TR-BDF2, including its finite radius of absolute monotonicity. Neither inspected statement evaluates the path-specific endpoint-neighbor coefficient or the exact threshold between lengths 32 and 33. General impossibility of unconditional monotonicity for higher-order methods is weaker than a precise positive graph family and minimum size statement for this particular entry. Path-graph endpoint transport is not covered by complete-multipartite classifications, except for very small special graphs. The potentially relevant one-dimensional composite parabolic solver of Carroll (1993) was identified, but its full text was not accessible during this examination; it is a residual publication-priority risk rather than evidence of absence.

## Limitations

The theorem concerns one specified off-diagonal matrix entry and not the whole operator, internal stages, or arbitrary weighted/irregular paths. It gives existence, not uniqueness, of a negative timestep interval for \(n\ge33\). The first-public date is for the focal TR-BDF2 positivity paper and does not claim the earlier 1996 stability-function article was first published in 2015. The contribution has not received independent mathematical validation. Full-text access to the Carroll (1993) one-dimensional paper was unavailable, so the originality assessment remains qualified by that concrete source and by unindexed literature.

## References

1. L. Bonaventura and A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, arXiv:1510.04303v1, first submitted 2015-10-14. https://arxiv.org/abs/1510.04303
2. M. E. Hosea and L. F. Shampine, *Analysis and implementation of TR-BDF2*, Applied Numerical Mathematics 20 (1996), 21–37. https://doi.org/10.1016/0168-9274(95)00115-8. Lawful full-text manuscript: https://pages.mtu.edu/~struther/Courses/OLD/Other/LessOld/5628_11/TRBDF2_Hosea_AppNumMath_20_pp21-37_1996.pdf
3. J. Carroll, *A composite integration scheme for the numerical solution of systems of parabolic PDEs in one space dimension*, Journal of Computational and Applied Mathematics 46 (1993), 327–343. https://doi.org/10.1016/0377-0427(93)90030-F (identified; full text not inspected).
