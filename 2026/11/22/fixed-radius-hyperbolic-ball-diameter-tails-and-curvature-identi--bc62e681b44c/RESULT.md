# Fixed-radius hyperbolic-ball diameter tails and curvature identification

## Finding
Let \(n\geq2\), \(T>0\), and \(\kappa>0\). In the real hyperbolic space of sectional curvature \(-\kappa^2\), choose \(X,Y\) independently and uniformly with respect to hyperbolic volume in the closed geodesic ball \(B_T\) of radius \(T\). Write \(D=d(X,Y)\), \(p=(n-1)/2\), and
\[
I_{n,\kappa,T}=\int_0^T\left(\frac{\sinh(\kappa s)}{\kappa}\right)^{n-1}ds,\quad
f_{n,\kappa,T}=\frac{(\sinh(\kappa T)/\kappa)^{n-1}}{I_{n,\kappa,T}},\quad
c_{\kappa,T}=\frac{\tanh(\kappa T)}{4\kappa}.
\]
As \(\varepsilon\downarrow0\) with \(n,T,\kappa\) fixed,
\[
\Pr(D>2T-\varepsilon)
=C_{n,\kappa,T}\varepsilon^{(n+3)/2}
+O_{n,\kappa,T}(\varepsilon^{(n+5)/2}),\qquad
C_{n,\kappa,T}=\frac{\Gamma(n/2)}{2\sqrt\pi\,\Gamma((n+5)/2)}
\frac{f_{n,\kappa,T}^{\,2}}{c_{\kappa,T}^{(n-1)/2}}.
\]
At the Euclidean endpoint \(\kappa=0\), interpreted by continuous limits,
\[
C_{n,0,T}=\frac{n^2\,2^{n-2}\Gamma(n/2)}{\sqrt\pi\,\Gamma((n+5)/2)\,T^{(n+3)/2}}.
\]
For every fixed \(n\ge2,T>0\), \(\kappa\mapsto C_{n,\kappa,T}\) is continuous and strictly increasing on \([0,\infty)\), with range \([C_{n,0,T},\infty)\). Thus the *single near-diametral probability coefficient*, when the ball radius and dimension are known, determines the magnitude of its constant negative sectional curvature uniquely.

There is also a conditional limit. Write \(r_X=d(0,X)\), \(r_Y=d(0,Y)\), \(\delta=\pi-\angle X0Y\), and \(A=T-r_X\), \(B=T-r_Y\). Under the event \(D>2T-\varepsilon\),
\[
\left(\frac{A}{\varepsilon},\frac{B}{\varepsilon},\frac{c_{\kappa,T}\delta^2}{\varepsilon},
1-\frac{A+B+c_{\kappa,T}\delta^2}{\varepsilon}\right)
\Longrightarrow \operatorname{Dirichlet}(1,1,p,1).
\]
The fourth coordinate can be slightly negative at finite \(\varepsilon\), due to the higher-order distance term, but converges to the stated nonnegative slack.

In dimension \(n=3\) an exact finite-deficit upper-half distance law is available. For \(T\le L\le2T\), put \(J=\int_0^T\sinh^2(\kappa s)\,ds\). Then
\[
\Pr(D>L)=\frac1{4J^2}\int_L^{2T}
[\cosh(\kappa u)-\cosh(\kappa L)]
\left[(2T-u)\cosh(\kappa u)-\frac{\sinh(\kappa(2T-u))}{\kappa}\right]du.
\]
This formula is exact for fixed positive \(\kappa,T\), without an asymptotic approximation.

## Assumptions and scope
Distances are intrinsic ambient hyperbolic geodesic distances, not Euclidean-model chords or network-graph shortest-path lengths. The sampling law is true normalized hyperbolic volume, not a merely exponential/quasi-uniform radial surrogate. Dimension \(n\), ball radius \(T\), and curvature \(\kappa\) are fixed in the small-deficit limit. The ball is convex, and its intrinsic geodesic diameter is \(2T\); the maximum occurs for antipodal boundary points. The \(\kappa=0\) assertion is the Euclidean continuous limit, not a claim that zero curvature is hyperbolic.

## Proof
**1. Exact radial/angular laws.** In polar coordinates about the ball center, the radius \(r\in[0,T]\) has density
\[
q(r)=\frac{(\sinh(\kappa r)/\kappa)^{n-1}}{I_{n,\kappa,T}}.
\]
For two independent uniform directions, the angle \(\theta\in[0,\pi]\) has density
\[
A_n\sin^{n-2}\theta,\qquad
A_n=\frac{\Gamma(n/2)}{\sqrt\pi\,\Gamma((n-1)/2)}.
\]
With \(\delta=\pi-\theta\) the hyperbolic cosine law is exactly
\[
\cosh(\kappa D)=\cosh(\kappa(r_X+r_Y))
-2\sinh(\kappa r_X)\sinh(\kappa r_Y)\sin^2(\delta/2).
\]
This also proves the diameter description, since \(D\le r_X+r_Y\le2T\), with equality exactly at the antipodal boundary pairs.

**2. Local deficit with controlled support.** Let \(A=T-r_X\), \(B=T-r_Y\). The exact cosine law and smoothness at the compact family of maximizing configurations give the uniform expansion
\[
2T-D=A+B+c_{\kappa,T}\delta^2
+O_{n,\kappa,T}\big((A+B+\delta^2)^2\big),\qquad
c_{\kappa,T}=\frac{\sinh^2(\kappa T)}{2\kappa\sinh(2\kappa T)}=\frac{\tanh(\kappa T)}{4\kappa}.
\]
If \(D>2T-\varepsilon\), then \(A+B<\varepsilon\) by the triangle inequality; the monotonic angular part of the exact cosine law gives \(\delta=O_{\kappa,T}(\sqrt\varepsilon)\). Thus all event mass lies in the neighborhood where the expansion is uniform. Both radial densities are \(f_{n,\kappa,T}(1+O(\varepsilon))\), and the angular density is \(A_n\delta^{n-2}(1+O(\varepsilon))\).

**3. Simplex-volume integral and remainder.** Scale \(A=\varepsilon x\), \(B=\varepsilon y\), \(\delta=\sqrt{\varepsilon/c_{\kappa,T}}z\). With \(p=(n-1)/2\), the leading mass is
\[
f_{n,\kappa,T}^2 A_n c_{\kappa,T}^{-p}\varepsilon^{p+2}
\int_{x,y,z\ge0\atop x+y+z^2<1}z^{n-2}\,dx\,dy\,dz.
\]
The integral equals
\[
\frac12\int_0^1 z^{n-2}(1-z^2)^2dz
=\frac14\mathrm B(p,3)=\frac{\Gamma(p)}{2\Gamma(p+3)}.
\]
Substitution of \(A_n\) yields exactly \(C_{n,\kappa,T}\). To justify the displayed error, one can instead use the exact squared half-angle cutoff
\[
Q(r_X,r_Y;L)=\frac{\cosh(\kappa(r_X+r_Y))-\cosh(\kappa L)}
{2\sinh(\kappa r_X)\sinh(\kappa r_Y)},\quad L=2T-\varepsilon,
\]
valid on \(r_X+r_Y>L\). The conditional angular probability is the regularized beta integral \(I_Q(p,p)\), since \((1+\cos\theta)/2\sim\operatorname{Beta}(p,p)\). On \(A+B<\varepsilon\), \(Q\) is \((\varepsilon-A-B)/(4c_{\kappa,T})\) times a positive smooth factor \(1+O(\varepsilon)\). The beta integral is \(Q^p/(p\mathrm B(p,p))(1+O(Q))\), uniformly for small \(Q\ge0\). Inserting this with the smooth radial densities and integrating over the fixed rescaled simplex proves the relative \(O(\varepsilon)\) error, including at the boundary where \(Q=0\).

**4. Conditional configuration.** In the scaled coordinates \(x=A/\varepsilon\), \(y=B/\varepsilon\), \(v=c_{\kappa,T}\delta^2/\varepsilon\), the leading joint measure has density proportional to \(v^{p-1}\mathbf 1_{\{x,y,v\ge0,\,x+y+v<1\}}\). Its normalized law, after adjoining slack \(1-x-y-v\), is exactly \(\operatorname{Dirichlet}(1,1,p,1)\). Uniform integrable domination from the exact cutoff establishes weak convergence.

**5. Curvature identifiability.** For \(q=n-1>0\),
\[
f_{n,\kappa,T}^{-1}=\int_0^T\left(\frac{\sinh(\kappa s)}{\sinh(\kappa T)}\right)^q ds.
\]
For each \(0<s<T\), this integrand decreases strictly with \(\kappa>0\): differentiate its logarithm and use that \(x\coth x\) is strictly increasing for \(x>0\). Consequently \(f_{n,\kappa,T}\) increases strictly with \(\kappa\). Also \(c_{\kappa,T}=T[\tanh(\kappa T)/(\kappa T)]/4\) decreases strictly, since \(\tanh x/x\) decreases on positive \(x\). Both factors of \(C_{n,\kappa,T}\) are therefore strictly increasing. At \(\kappa\downarrow0\), \(f\to n/T\) and \(c\to T/4\), giving the stated Euclidean coefficient. At \(\kappa\to\infty\), \(f\sim(n-1)\kappa\) and \(c\sim1/(4\kappa)\), so \(C\to\infty\). Continuity, strict monotonicity, and the intermediate value theorem prove the inverse-curvature assertion.

**6. Exact dimension-three upper-half law.** When \(n=3\), \((1+\cos\theta)/2\) is uniform on \([0,1]\), so \(\Pr(D>L\mid r_X=s,r_Y=t)=Q(s,t;L)\) whenever \(s+t>L\ge T\ge|s-t|\). Multiply by the two radial densities proportional to \(\sinh^2(\kappa s)\sinh^2(\kappa t)\). Change variables \(u=s+t\), \(v=s-t\); the domain is \(L\le u\le2T\), \(|v|\le2T-u\) with Jacobian \(1/2\). The product \(\sinh(\kappa s)\sinh(\kappa t)=[\cosh(\kappa u)-\cosh(\kappa v)]/2\), and the elementary \(v\)-integral yields the displayed exact one-dimensional integral. The formula at \(L=2T\) is zero by continuity.

## Verification
The standalone `checker.py` computes exact finite-deficit probabilities with Gauss-Legendre integration of the radial triangle and the exact regularized-beta spherical cap law; it checks the limiting coefficient for dimensions 2, 3, 4, 5, at multiple radii and curvatures including Euclidean \(\kappa=0\). It separately integrates the dimension-three one-dimensional expression, tests curvature-coefficient monotonicity through dimension seven, and reports `HYPERBOLIC_BALL_FIXED_RADIUS_CHECKS_OK 36`. These are numerical consistency tests; the proof above establishes all quantifiers. Reproduce using `python checker.py` with Python 3, NumPy and SciPy.

## Relationship to prior work
Krioukov et al. (2010) introduce hyperbolic geometry as a framework for complex networks. Kiwi and Mitsche (2014) explicitly set out the two-dimensional hyperbolic sampling measure and exact cosine law for random graph models, but address graph-distance bounds rather than the fixed-ball ambient-metric endpoint tail or curvature identification. Alanis-Lobato and Andrade-Navarro (2016) calculate an **approximate** two-dimensional hyperbolic pair-distance density, explicitly replacing the exact law of cosines by a large-radius approximation; their formula does not imply the fixed-radius true-volume sharp endpoint coefficient, higher-dimensional formula, conditional Dirichlet law, or three-dimensional exact upper-half integral. The published 2026 result *Three-regime radial–angular distance-deficit laws in expanding hyperbolic balls* studies first the limit in which ball radius goes to infinity, and only then the tail of that limiting random variable; it expressly excludes uniform finite-radius claims, and cannot produce the fixed-radius \(\varepsilon\downarrow0\) coefficient or its strictly monotonic curvature dependence by taking its stated limit. Standard spherical-beta and hyperbolic cosine formulas are inputs, not claimed novelties.

## Limitations
No result here concerns nonconstant curvature, anisotropic sampling, random graph shortest-path distances, or the full distance distribution in general dimension. The exact one-dimensional upper-half formula requires \(n=3\) and \(\kappa>0\). Small-deficit error constants are not claimed uniformly as \(T\), \(\kappa\), or dimension vary. Curvature is identifiable only when dimension, geodesic radius and volume-sampling convention are known. The historical literature comparison does not prove absolute novelty, and no independent mathematical audit has been performed.

## References
1. D. Krioukov, F. Papadopoulos, M. Kitsak, A. Vahdat and M. Boguñá, *Hyperbolic Geometry of Complex Networks*, arXiv:1006.5169v1, publicly submitted 2010-06-26. https://arxiv.org/abs/1006.5169
2. M. Kiwi and D. Mitsche, *A Bound for the Diameter of Random Hyperbolic Graphs*, arXiv:1408.2947v1, publicly submitted 2014-08-13. https://arxiv.org/abs/1408.2947
3. G. Alanis-Lobato and M. A. Andrade-Navarro, *Distance Distribution between Complex Network Nodes in Hyperbolic Space*, *Complex Systems* 25 (2016), 223–236. https://doi.org/10.25088/ComplexSystems.25.3.223 ; https://content.wolfram.com/sites/13/2018/02/25-3-3.pdf
4. *Three-regime radial–angular distance-deficit laws in expanding hyperbolic balls*, publicly available published-finding corpus mathematical research record (2026), RESULT.md (full text inspected), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-regime-radial-angular-distance-deficit-laws-in-expanding-h--a5d5220f2e29
