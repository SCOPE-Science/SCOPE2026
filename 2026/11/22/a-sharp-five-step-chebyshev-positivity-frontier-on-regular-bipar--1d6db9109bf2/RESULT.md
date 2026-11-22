# A sharp five-step Chebyshev positivity frontier on regular bipartite graph Laplacians

## Finding
Let \(G\) be any finite connected, simple, unweighted, \(d\)-regular bipartite graph, with \(d\ge1\), adjacency matrix \(B\), and combinatorial Laplacian \(L=dI-B\). For every \(\mu>0\), let \(H=\mu I+L\), whose exact spectral endpoints are \(\mu\) and \(\mu+2d\). Write
\[
\kappa=\frac{\mu+2d}{\mu},\qquad P=\frac Bd,\qquad z=1+\frac\mu d>1.
\]
Starting from zero, take the degree-\(m\) classical Chebyshev minimax residual on this *exact* spectral interval:
\[
r_m(H)=\frac{T_m(P)}{T_m(z)},\qquad
x^{(m)}=H^{-1}(I-r_m(H))b.
\]
Here \(T_m\) is the Chebyshev polynomial of the first kind. The inverse expression is a *polynomial in \(H\)* of degree \(m-1\); no matrix inverse is needed to compute the iterate.

**Theorem.** For every such graph, every \(\mu>0\), and every nonnegative vector \(b\), the final approximations \(x^{(1)},x^{(2)},x^{(3)},x^{(4)}\) are entrywise nonnegative. At the fifth iterate, the following universal condition is exact:
\[
\bigl[\forall G,\mu,b\ge0:\ \kappa\le\kappa_*\implies x^{(5)}\ge0\bigr],
\qquad \kappa_*=9+4\sqrt5.
\]
More precisely, if \(\kappa\le\kappa_*\), the fifth Chebyshev inverse polynomial is entrywise nonnegative on every graph in the specified class. Conversely, for **every** fixed \(\kappa>\kappa_*\), there is a finite connected regular bipartite graph and a strictly positive \(b\) for which its fifth iterate has a negative coordinate. Boolean hypercubes provide these sharpness witnesses.

An explicit rational instance takes the 32-dimensional Boolean hypercube with graph degree \(d=32\), \(z=21/20\), \(\mu=8/5\), and condition number \(\kappa=41\). For any adjacent vertices \(u,v\), the fifth inverse polynomial has entry
\[
(C_5(H))_{uv}=-\frac{17825}{49113088}<0,
\]
while \(H^{-1}\) is strictly positive entrywise.

## Assumptions and scope
The graph is finite, nonempty, connected, simple, unweighted, regular and bipartite. All the quantifiers in the positivity assertion range over graphs of this form, shifts \(\mu>0\) and data \(b\ge0\); the sharpness assertion allows graph size and degree to vary with \(\kappa\). The algorithm is the classical **final** degree-\(m\) Chebyshev semi-iterative approximation with exact spectral endpoints and initial value zero, not a claim about individual internal Richardson stages.

Connected regular bipartite graphs have adjacency eigenvalues \(d\) and \(-d\), so \(H\) really has endpoints \(\mu\) and \(\mu+2d\). The graph degree \(d\), dimension \(|V|\), and number of iterations \(m\) have distinct meanings. The positivity of the exact inverse follows independently from
\[
H^{-1}=\frac1{dz}\sum_{j=0}^{\infty}z^{-j}P^j,
\]
with strict positivity for every entry by connectedness.

## Proof
**1. Polynomial reduction.** Because \(H=d(zI-P)\), the exact-interval Chebyshev residual is \(T_m(P)/T_m(z)\). Define
\[
D_m(z,t)=\frac{T_m(z)-T_m(t)}{z-t}.
\]
The numerator vanishes at \(t=z\), so this is a polynomial in \(t\) of degree \(m-1\). The final iterate is
\[
x^{(m)}=C_m(H)b,\qquad C_m(H)=\frac{D_m(z,P)}{dT_m(z)}.
\]
Since \(z>1\), \(T_m(z)>0\). Since \(P\ge0\) entrywise, every coefficientwise nonnegative expansion of \(D_m(z,P)\) gives a nonnegative final inverse approximation.

**2. Positivity through four steps.** Directly from \(T_0(t)=1\), \(T_1(t)=t\), and \(T_{m+1}(t)=2tT_m(t)-T_{m-1}(t)\),
\[
\begin{aligned}
D_1(z,P)&=I,\\
D_2(z,P)&=2zI+2P,\\
D_3(z,P)&=(4z^2-3)I+4zP+4P^2,\\
D_4(z,P)&=(8z^3-8z)I+(8z^2-8)P+8zP^2+8P^3.
\end{aligned}
\]
Every displayed coefficient is nonnegative for \(z>1\). Therefore \(C_m(H)\ge0\) entrywise for \(m=1,2,3,4\) on every eligible graph and for all condition numbers.

**3. Exact universal fifth-step region.** The next divided difference is
\[
\begin{aligned}
D_5(z,P)={}&(16z^4-20z^2+5)I
+(16z^3-20z)P\\
&+(16z^2-20)P^2+16zP^3+16P^4.
\end{aligned}
\]
The constant coefficient equals \(1\) at \(z=1\) and has derivative \(8z(8z^2-5)>0\) for \(z>1\). The coefficients of \(P^3,P^4\) are positive. The remaining two coefficients are nonnegative exactly when \(z^2\ge5/4\). Hence every coefficient is nonnegative when \(z\ge\sqrt5/2\). Since \(\kappa=(z+1)/(z-1)\), this is equivalent to
\[
\kappa\le \frac{\sqrt5+2}{\sqrt5-2}=9+4\sqrt5,
\]
establishing sufficiency, including the boundary.

**4. Sharpness by hypercube walk counts.** Fix any \(1<z<\sqrt5/2\). Let \(G=Q_d\), the hypercube on \(2^d\) vertices, with degree \(d\). For vertices \(u,v\) of Hamming distance one, bipartiteness gives \((P^2)_{uv}=(P^4)_{uv}=0\). Exactly \(3d-2\) three-step coordinate-flip sequences end at that neighbor (one triple-flip of its coordinate and three permutations for each other coordinate), so
\[
(P)_{uv}=\frac1d,\qquad (P^3)_{uv}=\frac{3d-2}{d^3}.
\]
Inserting these into the fifth divided difference yields exactly
\[
(C_5(H))_{uv}=\frac{16z}{d^2T_5(z)}
\left(z^2-\frac54+\frac{3d-2}{d^2}\right).
\]
The prefactor is positive and the parenthesis tends to \(z^2-5/4<0\) as the integer \(d\to\infty\). Choose any sufficiently large finite \(d\). Then \((C_5(H))_{uv}<0\), so \(b=e_v\) yields a negative coordinate. For a strictly positive right-hand side take \(b=e_v+\varepsilon\mathbf1\) with \(\varepsilon>0\) sufficiently small: because \(P\mathbf1=\mathbf1\),
\[
C_5(H)\mathbf1
=\frac{1-T_5(z)^{-1}}{d(z-1)}\mathbf1>0,
\]
and the negative entry persists by continuity. Meanwhile \(H^{-1}b>0\) entrywise, establishing a genuine positivity violation by the approximation rather than the system.

**5. Explicit rational witness.** For \(d=32\) and \(z=21/20\), one has \(\mu=d(z-1)=8/5\), \(\kappa=41\). Evaluating the adjacent-vertex formula gives precisely \(-17825/49113088\). Taking
\[
\varepsilon=\frac{74865}{155443712}
\]
produces a strictly positive right-hand side and retains a negative adjacent component. All assertions about arbitrary graph sizes and all real \(\kappa\) are proved in steps 1--4, not inferred from this example.

## Verification
The standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It reconstructs Chebyshev polynomials by recurrence, independently verifies the divided differences and all listed coefficients at rational \(z\), directly enumerates short random-walk paths on small Boolean hypercubes, checks the exact adjacent-vertex formula, and verifies the explicit 32-dimensional rational witness and positive-data perturbation. The script displays its finite-check count and rational witness. These checks corroborate identities and finite cases; the universal graph bound and sharpness for every supercritical condition number are analytic.

## Relationship to prior work
Chebyshev semi-iteration, minimax residuals and graph Laplacian inverse problems are classical. Golub and Varga (1961), Gutknecht and Röllin (2002), and Gribling, Kerenidis and Szilágyi (2021) provide the polynomial minimax and linear-system framework; Jambulapati, Shiragur and Sidford (2018) discuss graph Laplacians and inverse symmetric \(M\)-matrices. None of these standard formulas alone supplies the stated sharp positivity bound on regular bipartite graph matrices.

The directly relevant published result *Condition three is the sharp positivity frontier for the degree-three Chebyshev semi-iterate* proves a universal \(\kappa=3\) boundary on **arbitrary Stieltjes matrices for degree three**, and explicitly excludes higher degrees from its classification. The present result instead concerns **regular bipartite shifted Laplacians**, protects degrees one through four at every condition number, and obtains the distinct optimal threshold \(9+4\sqrt5\) for degree five. The Stieltjes theorem's counterexamples are not members of the restricted homogeneous graph class, so neither statement implies the other. Related hypercube heat-integrator positivity theorems concern rational heat propagators rather than the Chebyshev approximation to an inverse.

## Limitations
This is a worst-case, graph-uniform classification at fixed degrees up to five, not a pointwise criterion for a given graph and not a classification of degree six or higher. For \(\kappa>9+4\sqrt5\), some eligible graphs may still produce nonnegative fifth-step operators; the theorem guarantees existence of a counterexample, not universal failure. Graph size of the hypercube witnesses can be large close to the threshold. The iterates use exact spectral endpoints and exact arithmetic at the mathematical level; finite-precision implementation and positivity of intermediate stages are not addressed. Historical priority is provisional because older monotone Chebyshev and \(M\)-matrix literature could contain an equivalent graph-specialized result.

## References
1. Gene H. Golub and Richard S. Varga, *Chebyshev Semi-Iterative Methods, Successive Overrelaxation Iterative Methods, and Second Order Richardson Iterative Methods*, Numerische Mathematik 3 (1961), Parts I and II.
2. Martin H. Gutknecht and Stefan Röllin, *The Chebyshev Iteration Revisited*, Parallel Computing 28 (2002), 263--283, DOI: 10.1016/S0167-8191(01)00139-9.
3. Arun Jambulapati, Kirankumar Shiragur and Aaron Sidford, *Efficient Structured Matrix Recovery and Nearly-Linear Time Algorithms for Solving Inverse Symmetric M-Matrices*, arXiv:1812.06295, first posted 2018-12-15, https://arxiv.org/abs/1812.06295.
4. Sander Gribling, Iordanis Kerenidis and Dániel Szilágyi, *Improving quantum linear system solvers via a gradient descent perspective*, arXiv:2109.04248, first posted 2021-09-09, https://arxiv.org/pdf/2109.04248.
5. *Condition three is the sharp positivity frontier for the degree-three Chebyshev semi-iterate*, public research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-condition-three-is-the-sharp-positivity-frontier-for-the-degree--6e9af63df14e/RESULT.md.
