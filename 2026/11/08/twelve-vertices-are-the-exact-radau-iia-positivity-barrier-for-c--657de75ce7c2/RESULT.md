# Twelve vertices are the exact Radau IIA positivity barrier for complete multipartite graph heat flow

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be any connected, unweighted, complete multipartite graph, where \(r\ge2\), every \(n_i\) is a positive integer and \(N=\sum_i n_i\). Write \(L\) for its combinatorial Laplacian. Consider the two-stage, third-order Radau IIA end-step on graph heat flow:

\[
T_h=\left(I-\frac h3L\right)
\left(I+\frac{2h}{3}L+\frac{h^2}{6}L^2\right)^{-1},\qquad h\ge0.
\]

**Sharp order theorem.** If \(2\le N\le11\), then \(T_h\) is entrywise nonnegative for every \(h\ge0\), and is strictly positive for every \(h>0\). If \(N\ge12\), then every part of \(G\) has a timestep at which all the diagonal entries corresponding to that part are negative. In particular, for a part of size \(p\), the explicit choice

\[
 h_p=\frac8{N-p}
\]

makes all \(p\) corresponding diagonal entries strictly negative. Every off-diagonal entry remains strictly positive for all \(h>0\), regardless of \(N\). Thus **the method is positive at all positive timesteps on every such graph exactly in orders at most eleven**, while every graph of order at least twelve loses and subsequently regains entrywise positivity as the timestep increases.

This includes cliques, stars, all balanced and unbalanced complete bipartite graphs and all higher-part multipartite graphs. It is a claim about endpoint matrices on these finite, unweighted, loopless networks; it does not claim positivity of internal Radau stages or of Radau IIA on arbitrary graph topologies.

## Assumptions and scope

The Laplacian is \(L=D-A\), where each graph edge has unit weight. The network has \(N\) vertices, at least two nonempty parts, no self-loops, and real nonnegative timestep \(h\). Entrywise nonnegativity means all entries are \(\ge0\); stochasticity means all row sums are one. Graph-heat flow has generator \(-L\). The Radau IIA scalar stability filter is

\[
R(z)=\frac{1-z/3}{1+2z/3+z^2/6}
=\frac{2(3-z)}{z^2+4z+6}.
\]

The matrix inverse defining \(T_h=R(hL)\) exists for all \(h\ge0\) because the Laplacian spectrum is nonnegative and the denominator is strictly positive on that interval.

## Proof

**1. Complete multipartite projectors.** The Laplacian eigenvalues are zero on constants, \(N-n_i\) on sum-zero vectors supported inside part \(i\), and \(N\) on vectors constant on each part with total sum zero. Let \(P_0=\mathbf 1\mathbf 1^{\mathsf T}/N\), \(P_i=I_{n_i}-J_{n_i}/n_i\) on the \(i\)-th block (extended by zero elsewhere), and \(P_N=I-P_0-\sum_iP_i\). These are mutually orthogonal spectral projectors. Therefore

\[
T_h=P_0+\sum_iR((N-n_i)h)P_i+R(Nh)P_N.
\]

Its rows sum to one, because \(R(0)=1\) and \(L\mathbf1=0\).

**2. Off-diagonal entries have fixed positive sign.** Put \(p=n_i\), \(q=N-p>0\), and \(D(z)=z^2+4z+6\). For vertices in *different* parts the entry is

\[
\frac{1-R(Nh)}N=\frac{h(Nh+6)}{D(Nh)}>0\quad(h>0).
\]

For distinct vertices in the *same* part, the entry is

\[
\begin{aligned}
&\frac1N-\frac{R(qh)}p+\left(\frac1p-\frac1N\right)R(Nh)\\
&\qquad=\frac{q h^2\,[qN h^2+6(p+2q)h+18]}{D(qh)D(Nh)}>0\quad(h>0).
\end{aligned}
\]

Both are elementary rational identities obtained by substituting the displayed \(R\). The within-part expression is used only when \(p\ge2\).

**3. Positivity through order eleven.** The common diagonal entry for every vertex of part size \(p\) is

\[
d_p(h)=\frac1N+\left(1-\frac1p\right)R(qh)
+\left(\frac1p-\frac1N\right)R(Nh).
\]

The coefficients of the two \(R\)-terms are nonnegative and sum to \(1-1/N\). Direct differentiation gives

\[
R'(z)=\frac{2(z^2-6z-18)}{D(z)^2},\qquad
\min_{z\ge0}R(z)=\frac{5-3\sqrt3}{2}=:\eta<0.
\]

The minimum occurs at \(z=3+3\sqrt3\). Hence, for every \(p,h\),

\[
d_p(h)\ge\frac{1+(N-1)\eta}{N}.
\]

For \(N\le11\), the numerator is at least
\(1+10\eta=26-15\sqrt3>0\), the final inequality following from \(26^2>3\cdot15^2\). Combining with step 2 proves strictly positive entries for \(h>0\) and nonnegativity at \(h=0\).

**4. A negative diagonal in every part at order twelve and above.** Fix any part size \(1\le p<N\), put \(q=N-p\), \(t=p/N\in(0,1)\), and choose \(h_p=8/q\). Since \(R(8)=-5/51\), direct substitution and cancellation yield the exact rational identity

\[
\boxed{\quad
d_p(8/q)=-\frac{N(255-110t+15t^2)-2848+1056t}
{51N(51-22t+3t^2)}.\quad}
\]

The denominator is positive for \(0<t<1\). Set \(A(t)=255-110t+15t^2\). It is positive on \([0,1]\), since it decreases there and \(A(1)=160\). For every \(N\ge12\), the numerator after its minus sign satisfies

\[
N A(t)-2848+1056t
\ge 12A(t)-2848+1056t
=4(45t^2-66t+53)>0.
\]

The final quadratic is strictly positive for all real \(t\), because its leading coefficient is positive and its discriminant is \(66^2-4\cdot45\cdot53<0\). Consequently \(d_p(h_p)<0\) for **every** part \(p\) of **every** \(N\ge12\) multipartite graph. This proves the sharp cutoff, including the boundary \(N=12\), without finite enumeration.

**5. Positivity is lost and regained.** At \(h=0\), \(T_h=I\); by continuity the diagonals remain positive for all sufficiently small \(h>0\). The off-diagonal entries are positive there by step 2. As \(h\to\infty\), \(R(\lambda h)\to0\) for every nonzero eigenvalue \(\lambda\), so \(T_h\to P_0=J/N\) entrywise. Thus every such graph of order at least twelve has a nonpositive intermediate step but strictly positive end-step matrices at both sufficiently small and all sufficiently large positive steps.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library and exact `fractions.Fraction` arithmetic. For a declared finite collection of multipartite examples it constructs the full Laplacian, inverts the Radau rational denominator by exact Gauss–Jordan elimination, compares every transition entry to the spectral-projector formula, tests stochastic row sums, and checks the negative witness in each part. It additionally checks the explicit witness expression for integer pairs through order fifty. Run `python3 verify.py` next to this file. The completed replay reported 196 exact matrix/witness cases, 16,580 exact entry comparisons and 1,510 exact stochastic-row tests, plus 741 integer-pair witness inequalities. These are regression tests only: the all-order and all-timestep statements are established by the foregoing algebraic inequalities, not by an extrapolation from finite tests.

## Relationship to prior work

Horváth, Song and Terlaky (2014) analyze step-size thresholds for invariant polyhedra under rational discretizations, including a sufficient absolute-monotonicity-radius criterion (their Theorem 3.12); that criterion does not directly provide the sharp cardinality cutoff or the individual negative witnesses above. Lóczi and Ketcheson (2013) study absolute-monotonicity radii for rational approximations and Runge–Kutta methods, an unrestricted-method setting distinct from this particular structured Laplacian family. Horváth (1998) gives general Runge–Kutta positivity criteria, while Horváth (2005, Theorem 17 and Remarks 18–19) treats positivity on a smaller eigenvector-defined cone, explicitly discussing two-stage Radau IIA. Those statements neither require entrywise nonnegativity on all initial nonnegative vectors for complete multipartite Laplacians nor determine a sharp graph-order cutoff. Both full texts were inspected. The balanced complete bipartite case is a special subfamily of the present theorem; it does not establish the assertion for arbitrary multipartite profiles. A general all-size scalar-filter characterization, if applied to this sign-changing filter, shows failure on *some* graph but does not alone yield the exact universal cutoff at twelve vertices or the part-specific rational witnesses. These comparisons do not establish global novelty, and specialist coverage may remain unindexed.

## Limitations

The theorem is specific to the *unweighted complete multipartite* Laplacian and the stated *two-stage third-order Radau IIA endpoint* stability function. It does not classify every positive or negative timestep interval for an individual graph with \(N\ge12\), nor address other Runge–Kutta stage values, arbitrary weighted graphs, general Markov generators, or global method strong-stability preservation. The source comparison was not an independent publication-priority audit. A short specialist 2004 follow-up was available only through its abstract; the 1998 and 2005 Horváth articles were inspected in full. The possibility of unindexed equivalent specialist coverage remains. All matrices and computations in `verify.py` were independently replayed against the packaged source but cannot replace the proof of its universal claims.

## References

- Z. Horváth, Y. Song, T. Terlaky, *Steplength Thresholds for Invariance Preserving of Discretization Methods of Dynamical Systems on a Polyhedron* (first public arXiv version June 26, 2014), https://arxiv.org/abs/1406.6755 .
- L. Lóczi, D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity* (first public arXiv version March 26, 2013), https://arxiv.org/abs/1303.6651 ; https://doi.org/10.1112/S1461157013000326 .
- Z. Horváth, *Positivity of Runge–Kutta and diagonally split Runge–Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326, https://doi.org/10.1016/S0168-9274(98)00050-6 .
- Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356, https://doi.org/10.1016/j.apnum.2004.08.026 .
- Z. Horváth, *Positively invariant cones of dynamical systems under Runge–Kutta and Rosenbrock-type discretization*, PAMM 4 (2004), 688–689, https://doi.org/10.1002/pamm.200410325 .
