# Zariski-chamber support profile of a one-nodal cubic surface resolution

## Finding

Let \(k=\mathbb C\), and let \(X\) be the blow-up of \(\mathbb P^2\) at six distinct points \(p_1,\ldots,p_6\) such that \(p_1,p_2,p_3\) are collinear, no other three are collinear, and all six do not lie on a conic. Thus \(X\) is a weak del Pezzo surface of degree three, and its anticanonical model has exactly one ordinary double point.

Let \(z_j(X)\) denote the number of Zariski chambers of the big cone whose negative part has support on exactly \(j\) distinct irreducible curves; include the nef chamber as \(z_0(X)=1\). Then the complete support-count polynomial is

\[
Z_X(t)=\sum_{j\geq0}z_j(X)t^j=1+22t+156t^2+490t^3+725t^4+447t^5+57t^6.
\]

In particular, \(X\) has exactly \(1898\) Zariski chambers, and no chamber has negative support of size more than six. A smooth cubic surface resolution (the blow-up of six points in general position) instead has \(2764\) chambers, so the one-node specialization changes the total by \(866\). The result counts the chambers on the **smooth minimal resolution** \(X\), not on the singular cubic hypersurface itself.

## Assumptions and scope

The base field is \(\mathbb C\). Points are distinct; the only collinear triple is \(\{p_1,p_2,p_3\}\); there is no conic through all six. Write \(H\) for the pullback of the line class and \(E_i\) for the exceptional curves, so \(H^2=1\), \(E_i^2=-1\), and all other intersections among these basis classes vanish. The canonical class is \(K_X=-3H+\sum_{i=1}^6E_i\). For this almost-general-position configuration \(-K_X\) is nef and big, with self-intersection three; the unique anticanonically contracted curve is \(R=H-E_1-E_2-E_3\), a \((-2)\)-curve.

A negative curve is an irreducible curve with negative self-intersection. We use the established correspondence between Zariski chambers other than the nef chamber and nonempty reduced divisors of negative curves with negative-definite intersection matrix (Bauer--Funke--Neumann, Proposition 1.1). We count every such support once. Multiplicities in a negative part are **not** extra choices in the chamber count.

## Proof

**1. Exhaustion of negative curves.** Because \(-K_X\) is nef, adjunction implies that a negative irreducible curve is a smooth rational curve of self-intersection either \(-1\) or \(-2\). For a curve \(C\ne E_i\), write \(C=dH-\sum_i m_iE_i\), with integers \(d\geq1\), \(m_i\geq0\). If \(C^2=-1\), then \(-K_X\cdot C=1\), so

\[
\sum_i m_i=3d-1,\qquad \sum_i m_i^2=d^2+1.
\]

Cauchy--Schwarz gives \((3d-1)^2\leq6(d^2+1)\), hence \(d\leq2\). If \(d=1\), precisely two multiplicities equal one: the class is \(H-E_i-E_j\). If \(d=2\), precisely five multiplicities equal one: the class is \(2H-\sum_{j\ne i}E_j\). For the unique triple, the three classes \(H-E_i-E_j\) with \(i,j\in\{1,2,3\}\) are reducible as \(R+E_h\), where \(h\) is the remaining index. Exactly the other twelve line classes give irreducible \((-1)\)-curves. A conic through five points is reducible whenever its set includes all three collinear points, so the three classes omitting \(p_4,p_5,p_6\) are reducible; the three conics omitting \(p_1,p_2,p_3\) are irreducible. Together with the six exceptional curves, the list consists of \(6+12+3=21\) irreducible \((-1)\)-curves.

If \(C^2=-2\), then \(-K_X\cdot C=0\), and

\[
\sum_i m_i=3d,\qquad\sum_i m_i^2=d^2+2.
\]

Cauchy--Schwarz yields \(9d^2\leq6(d^2+2)\), hence \(d\leq2\). The degree-one possibility requires a line containing three marked points, giving only \(R\). The degree-two possibility requires a conic containing all six, which is excluded. Thus \(R\) is the only \((-2)\)-curve, and the negative-curve list is complete.

**2. Negative-definiteness criterion.** Two distinct curves in the \((-1)\) list meet either zero or once, as seen from their classes and the intersection form. A pair meeting once has intersection matrix \(\bigl(\begin{smallmatrix}-1&1\\1&-1\end{smallmatrix}\bigr)\), which is not negative definite. Therefore a negative-definite support without \(R\) is exactly a pairwise-disjoint subset of the twenty-one \((-1)\)-curves.

The curve \(R\) meets precisely \(E_1,E_2,E_3\) and the proper transforms of the lines \(L_{45},L_{46},L_{56}\), each with intersection one, and meets the remaining fifteen \((-1)\)-curves in zero. Let \(T\) be a pairwise-disjoint set of \((-1)\)-curves, and let \(r(T)\) be the number of its members meeting \(R\). The intersection matrix of \(T\cup\{R\}\) has a \(-I\) block and a last Schur complement equal to \(-2+r(T)\). It is negative definite precisely when \(r(T)\leq1\). This gives an exhaustive geometric criterion, not merely a heuristic subset filter.

**3. Exact finite recurrence.** Construct the graph \(G\) whose vertices are the twenty-one \((-1)\)-curves, with an edge exactly when distinct curves intersect. Write \(N(v)\) for the neighbors of a vertex \(v\), and mark a vertex by \(\epsilon_v\in\{0,1\}\) according as its curve is disjoint from or meets \(R\). For any induced vertex set \(A\), define

\[
P_A(t,u)=\sum_{T\subseteq A\atop T\text{ independent}}t^{|T|}u^{r(T)}.
\]

This polynomial is determined by the base case \(P_\varnothing=1\) and the exact deletion recurrence

\[
P_A(t,u)=P_{A\setminus\{v\}}(t,u)+t u^{\epsilon_v}P_{A\setminus(\{v\}\cup N(v))}(t,u).
\]

Its ordinary specialization is

\[
P_G(t,1)=1+21t+135t^2+370t^3+465t^4+237t^5+21t^6.
\]

Retaining only the coefficients of \(u^0\) and \(u^1\), one obtains

\[
[u^0+u^1]P_G(t,u)=1+21t+120t^2+260t^3+210t^4+36t^5,
\]

where \([u^0+u^1]\) denotes the sum of those two coefficients, not a formal projection of polynomials in \(t\). The exact twenty-one-vertex recurrence and a separate exhaustive subset dynamic program reproduce these coefficients. The total chamber polynomial therefore equals

\[
Z_X(t)=P_G(t,1)+t[u^0+u^1]P_G(t,u)
=1+22t+156t^2+490t^3+725t^4+447t^5+57t^6.
\]

The constant term corresponds to the nef chamber; all other terms correspond to nonempty negative-definite supports. Evaluating at \(t=1\) gives \(1898\).

## Verification

Run `python3 verify.py` from the directory containing this document and `verify.py`. It uses only the Python standard library. The verifier builds all curve classes in the \((H,E_1,\ldots,E_6)\)-basis, reconstructs their complete integral intersection matrix, verifies that exactly six curves meet \(R\), evaluates the deletion recurrence with memoization, and **independently** loops over all \(2^{21}\) subsets using a distinct incremental bit-mask test. Both methods return the same coefficients. As a separate baseline, it reconstructs the twenty-seven \((-1)\)-classes of a smooth cubic and returns the classical \(2764\) chambers.

Exact expected lines include `combined_support_profile=(1, 22, 156, 490, 725, 447, 57)`, `chambers_total=1898`, and `ALL_CHECKS_PASSED`; full output is in `verification_output.txt`. This is a finite exhaustive computation combined with the proof that the curve list and negative-definiteness criterion are exhaustive. No approximate floating-point calculations occur.

## Relationship to prior work

Bauer, Funke and Neumann (first public preprint December 4, 2009) established the negative-definite-support correspondence and counted \(2764\) chambers for **six general** blow-up points. Their full text explicitly assumes general position in the main enumerative theorem. Bauer and Schmitz (April 19, 2012) improved the general exact-count algorithm and studied chambers of a different surface, the Segre--Schur quartic. Lubbes (February 27, 2013) classified root subsystems of weak del Pezzo surfaces and includes the rank-six \(A_1\) case but does not tabulate this chamber-support polynomial. The new numerical conclusion is the full specialization profile for the minimal resolution of a cubic with one node, not a new general chamber algorithm nor a new classification of weak del Pezzo roots.

## Limitations

This calculation applies to the minimal resolution over \(\mathbb C\) in the specified six-point configuration; it does not count chambers on the singular cubic itself, on every type of singular cubic, or on blow-ups with additional collinearities, infinitely near points, or a conic containing all six. It makes no claim about volumes or shapes of the individual chambers. Independent historical priority and independent scientific validation have not been established; earlier computations in specialized tables could cover the same coefficients despite the searches reported with this result.

## References

- T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958, first submitted 2009-12-04. In particular Proposition 1.1, Theorem for blow-ups of general points, and Section 3.
- T. Bauer, D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373, first submitted 2012-04-19. Introduction and Section 1.
- N. Lubbes, *Algorithms for singularities and real structures of weak Del Pezzo surfaces*, arXiv:1302.6678, first submitted 2013-02-27. Sections 1--2 and rank-six \(A_1\) entry of Table 13.
