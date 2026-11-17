# A scalar criterion for unconditionally positive rational graph-heat steps on complete multipartite networks

## Finding

Let \(F:[0,\infty)\to\mathbb R\) be bounded and continuous with \(F(0)=1\). For every connected unweighted complete multipartite graph \(G=K_{a_1,\ldots,a_r}\), \(r\ge2\), let \(L_G\) be the combinatorial Laplacian and \(T_G(h)=F(hL_G)\) for \(h\ge0\). The following are equivalent:

1. \(T_G(h)\) is entrywise nonnegative for every such graph and every \(h\ge0\).
2. \(0\le F(x)\le1\) for all \(x\ge0\), and \(g(x)=(1-F(x))/x\) is nonincreasing on \((0,\infty)\).

For the two-stage, fourth-order Gauss–Legendre Runge–Kutta end-step applied to graph heat dynamics \(u'=-L_Gu\), the scalar filter is
\[
F(x)=\frac{x^2-6x+12}{x^2+6x+12}.
\]
It satisfies the criterion strictly: \(0<F(x)<1\) for \(x>0\) and \(g(x)=12/(x^2+6x+12)\) is strictly decreasing. Thus every entry of \(T_G(h)\) is strictly positive for \(h>0\), while \(T_G(h)\mathbf1=\mathbf1\) for all \(h\ge0\). There is no timestep restriction, even as the graph size grows.

This does not extend to all graph topologies: for the ordinary four-vertex path, the same method gives the exact negative entry
\[
[T_{P_4}(20)]_{0,1}=-\frac{643260}{32303047}<0,
\]
where path vertices are numbered consecutively \(0,1,2,3\).

## Assumptions and scope

The graph has \(n=\sum_{i=1}^r a_i\) vertices with at least two nonempty independent parts; every edge between distinct parts has unit conductance and no within-part edges exist. Functions of the symmetric Laplacian are defined by ordinary real spectral functional calculus. Boundedness of \(F\) on \([0,\infty)\) is used for the converse. The statement concerns only the final one-step matrix, not internal Runge–Kutta stages or arbitrary nonlinear systems. At \(h=0\), \(T_G(0)=I\).

## Proof

Write \(J_m\) for the all-ones \(m\times m\) matrix. Define orthogonal projectors
\[
P_0=\frac{J_n}{n},\qquad
P_n=\bigoplus_{i=1}^r\frac{J_{a_i}}{a_i}-\frac{J_n}{n},\qquad
P_i=I_{a_i}-\frac{J_{a_i}}{a_i}
\]
where \(P_i\) is extended by zero outside its part. The subspaces are, respectively, constants, part-constant vectors of total sum zero, and within-part zero-sum vectors. Direct evaluation of the graph Laplacian gives eigenvalues \(0\), \(n\), and \(n-a_i\) on those subspaces. Hence
\[
F(hL_G)=P_0+F(nh)P_n+\sum_{i=1}^r F((n-a_i)h)P_i.
\]
If vertices \(u,v\) lie in different parts, the entry is \((1-F(nh))/n\). If they are distinct vertices within part \(i\) of size \(a=a_i\), the entry is
\[
\frac{a+(n-a)F(nh)-nF((n-a)h)}{na}.
\]
For \(h>0\), put \(x=(n-a)h\) and \(y=nh\). The last numerator is
\[
\frac{xy}{h}\bigl(g(x)-g(y)\bigr).
\]
The diagonal entry for a vertex of part \(i\) is
\[
\frac1n+\left(\frac1a-\frac1n\right)F(nh)
+\left(1-\frac1a\right)F((n-a)h).
\]
Its three coefficients are nonnegative. Therefore the two scalar conditions imply all entries are nonnegative; the graph heat step is stochastic because constants form the zero-eigenspace and \(F(0)=1\).

Conversely, suppose all these matrices are entrywise nonnegative. Applying the between-part formula to \(K_2\) with arbitrary \(h\) gives \(F(y)\le1\) for all \(y>0\). Applying the diagonal formula to a vertex in the part of size \(a\) of \(K_{a,1}\), with \(h=x>0\) fixed, gives
\[
\frac1{a+1}+\frac{F((a+1)x)}{a(a+1)}
+\left(1-\frac1a\right)F(x)\ge0.
\]
Letting \(a\to\infty\), boundedness implies \(F(x)\ge0\). At zero \(F(0)=1\).

Finally choose \(K_{a,b}\) with \(a\ge2\), \(b\ge1\), and two distinct vertices in the part of size \(a\). Their off-diagonal nonnegativity forces \(g(bh)\ge g((a+b)h)\). As \(b/(a+b)\) runs over a dense set of rational numbers in \((0,1)\) and \(h\) varies freely, continuity of \(g\) yields \(g(x)\ge g(y)\) for every \(0<x<y\). This proves necessity and completes the equivalence.

For Gauss–Legendre, its numerator is \((x-3)^2+3>0\), its denominator is positive, and \(1-F(x)=12x/(x^2+6x+12)>0\) for \(x>0\). Its \(g\) is strictly decreasing, so the displayed formulas prove strict positivity of all entries. On the four-vertex path, direct rational elimination in \((I+hL/2+h^2L^2/12)^{-1}(I-hL/2+h^2L^2/12)\) at \(h=20\) gives the stated exact negative fraction.

## Verification

The standalone standard-library checker `artifacts/verify_exact.py` constructs the Laplacian and rational matrix functional calculus using exact rational arithmetic, compares it entry by entry with the spectral formula, verifies strict positivity and stochasticity, and evaluates the path counterexample. The executed checks passed on 45 graph/timestep combinations, comparing 1,630 exact matrix entries, and returned \(-643260/32303047\) for the indicated path entry. These finite cases are supplementary to the quantified analytic proof; they are not an exhaustive test of all part sizes, timesteps, or scalar functions.

## Relationship to prior work

Classical spectral methods and the scalar fourth-order Padé/Gauss–Legendre stability function are standard inputs, not newly claimed constructions. Lóczi and Ketcheson analyzed absolute-monotonicity radii of rational stability functions and found zero for the order-four two-stage rational class, a universal monotonicity obstruction. Horváth, Song and Terlaky established threshold criteria for rational discretizations of invariant polyhedra; their sufficient absolute-monotonicity framework does not state the present graph-family-wide if-and-only-if filter criterion. Zappavigna, Colaneri, Kirkland and Shorten established that diagonal Padé maps need not preserve positivity for general positive systems. The present result instead classifies precisely which bounded scalar filters work on every unweighted complete multipartite graph and exhibits a fourth-order filter that works unconditionally on this restricted, infinite family.

## Limitations

The statement does not extend automatically to arbitrary graphs, as the explicit path counterexample confirms. It concerns the exact final matrix in real arithmetic, not floating-point rounding, Runge–Kutta internal stages, positivity for nonlinear systems, or asymptotic mixing quality. In particular the Gauss–Legendre filter tends to one on high-frequency modes at large steps; entrywise positivity is not an assertion of L-stability. Earlier studies of Padé positivity for general positive matrices have not all been available in full text, so publication priority should be checked independently.

## References

1. L. Lóczi and D. I. Ketcheson, “Rational functions with maximal radius of absolute monotonicity,” *LMS Journal of Computation and Mathematics* 17 (2014), 159–205; public preprint dated March 26, 2013, https://arxiv.org/abs/1303.6651 ; https://doi.org/10.1112/S1461157013000326 .
2. Z. Horváth, Y. Song, and T. Terlaky, “Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron,” *Discrete and Continuous Dynamical Systems* 35 (2015), 2997–3013; public preprint dated June 26, 2014, https://arxiv.org/abs/1406.6755 .
3. A. Zappavigna, P. Colaneri, S. Kirkland, and R. Shorten, “Essentially negative news about positive systems,” *Linear Algebra and its Applications* 436 (2012), 3425–3442, https://doi.org/10.1016/j.laa.2011.12.021 .
4. Z. Horváth, “Positivity of Runge-Kutta and diagonally split Runge-Kutta methods,” *Applied Numerical Mathematics* 28 (1998), 309–326, https://doi.org/10.1016/S0168-9274(98)00050-6 .
