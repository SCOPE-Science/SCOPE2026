# Integer-order collapse and infinite signed inertia of fractional Volterra self-commutators

## Finding
For every real \(\alpha>0\), let the Riemann–Liouville operator on complex \(L^2(0,1)\) be
\[
(J_\alpha f)(x)=\frac1{\Gamma(\alpha)}\int_0^x(x-t)^{\alpha-1}f(t)\,dt,
\qquad D_\alpha=J_\alpha J_\alpha^*-J_\alpha^*J_\alpha.
\]
The compact self-adjoint nonnormality defect \(D_\alpha\) has the following exact rank and signed-inertia classification:
\[
\big(\operatorname{rank}D_\alpha,n_+(D_\alpha),n_-(D_\alpha)\big)=
\begin{cases}
(2m,m,m),&\alpha=m\in\{1,2,3,\ldots\},\\
(\infty,\infty,\infty),&\alpha\notin\mathbb N.
\end{cases}
\]
Here the signed indices count positive and negative eigenvalues with multiplicity. At an integer order \(m\), all nonzero eigenfunctions are polynomials of degree at most \(2m-1\). Moreover, if \(\lambda_1,\ldots,\lambda_{2m}\) are the nonzero eigenvalues, counted with multiplicity, then the exact finite spectral product is
\[
\prod_{j=1}^{2m}\lambda_j=(-1)^m
\frac{\displaystyle\prod_{j=0}^{2m-1}(j!)^2}{\displaystyle\prod_{j=0}^{4m-1}j!}.
\]
Thus every noninteger order, however close to an integer, produces infinitely many eigenvalues of *each* sign, whereas integer orders have precisely finitely many, paired by sign.

## Assumptions and scope
The interval is exactly \((0,1)\), measure is Lebesgue measure, the Hilbert space is complex \(L^2(0,1)\), and the integration order is a strictly positive real number. Adjoint and eigenvalues refer to this Hilbert structure. Rank means operator rank, not rank of a numerical discretization. For infinite inertia no claim is made about the eigenvalues' rate of decay or the nullspace. The finite product refers only to nonzero eigenvalues at positive integer order.

## Proof
**1. Compactness, kernel, and spectral pairing.** Write \(k_\alpha(t)=t^{\alpha-1}/\Gamma(\alpha)\) for \(0<t<1\). Young's inequality gives \(\|J_\alpha\|\le1/\Gamma(\alpha+1)\). Cutting away \(0<t<\varepsilon\) gives a Hilbert–Schmidt integral operator; the removed convolution tail has norm at most \(\varepsilon^\alpha/\Gamma(\alpha+1)\). Therefore \(J_\alpha\), and hence \(D_\alpha\), is compact. For distinct \(x,y\), its integral kernel is
\[
K_\alpha(x,y)=\frac1{\Gamma(\alpha)^2}\left[
\int_0^{\min(x,y)}(x-t)^{\alpha-1}(y-t)^{\alpha-1}\,dt
-\int_{\max(x,y)}^1(t-x)^{\alpha-1}(t-y)^{\alpha-1}\,dt\right].
\]
Both integrals are absolutely convergent away from the diagonal. Let \((Rf)(x)=f(1-x)\). Then \(RJ_\alpha R=J_\alpha^*\), and consequently \(RD_\alpha R=-D_\alpha\). Thus the nonzero spectrum consists of positive/negative pairs with equal multiplicities. It remains to calculate rank.

**2. Every noninteger order has infinite rank.** Fix \(0<\delta<\varepsilon<1/2\) and choose arbitrarily many distinct points \(y_j\in(\varepsilon,1-\varepsilon)\). For \(0<x<\delta\), the *second* integral in the kernel, whose lower endpoint is \(y_j>\varepsilon\), is real-analytic in \(x\) at zero. The first integral has the convergent fractional expansion
\[
\int_0^x(x-t)^{\alpha-1}(y-t)^{\alpha-1}\,dt
=x^\alpha\sum_{k=0}^\infty
(-1)^k\binom{\alpha-1}{k}B(k+1,\alpha)
\,x^k y^{\alpha-1-k}.
\]
All coefficients are nonzero whenever \(\alpha>0\) is not an integer: the beta factor is positive and the generalized binomial coefficient never vanishes. Suppose a finite linear combination of the columns \(K_\alpha(\cdot,y_j)\) vanished on \((0,\delta)\). The sum of their ordinary analytic parts plus \(x^\alpha\) times their analytic fractional parts would vanish. Since \(\alpha\notin\mathbb N\), the two expansions have disjoint exponent sets; comparison of successive leading exponents gives
\[
\sum_j c_j y_j^{\alpha-1-k}=0\quad(k=0,1,2,\ldots).
\]
Taking as many consecutive equations as there are points, factoring \(y_j^{\alpha-1}\), and using the ordinary Vandermonde determinant for the distinct reciprocals \(1/y_j\), gives \(c_j=0\) for every \(j\). Thus arbitrarily many separated kernel columns are linearly independent. If the operator had finite rank, almost every selection of its columns would lie in a fixed finite-dimensional subspace of \(L^2(0,\delta)\), a contradiction. Its rank is infinite. Compactness and the reflection anticommutation then force infinitely many strictly positive and infinitely many strictly negative eigenvalues.

**3. Integer orders, full rank, and determinant.** Let \(\alpha=m\in\mathbb N\), and set \(F_{x,y}(t)=(x-t)^{m-1}(y-t)^{m-1}\). Choose its polynomial primitive \(G_{x,y}\) satisfying \(G_{x,y}(0)=0\). Since the two powers have a common even total degree, the kernel simplifies globally to the polynomial
\[
K_m(x,y)=\frac{G_{x,y}(x)+G_{x,y}(y)-G_{x,y}(1)}{((m-1)!)^2}.
\]
Its total degree is at most \(2m-1\). Write \(K_m(x,y)=\sum_{i,j=0}^{2m-1}A_{ij}x^iy^j\). All coefficients with \(i+j>2m-1\) vanish. Directly expanding the two endpoint primitives, or applying the beta integral to the two homogeneous contributions, gives on the antidiagonal
\[
A_{i,2m-1-i}=
\frac{(-1)^{m-1-\min(i,2m-1-i)}}{i!(2m-1-i)!}
\quad(0\le i\le2m-1).
\]
Every antidiagonal entry is nonzero. Hence \(A\) is anti-triangular and invertible, with
\[
\det A=\frac{(-1)^m}{\left(\prod_{j=0}^{2m-1}j!\right)^2}.
\]
The range of \(D_m\) equals the full \(2m\)-dimensional polynomial space \(\mathcal P_{2m-1}\): in monomial coordinates the action on that space is \(AH\), where \(H_{ij}=\int_0^1x^{i+j}dx=(i+j+1)^{-1}\) is positive definite. Thus \(\operatorname{rank}D_m=2m\), and pairing forces exactly \(m\) positive and \(m\) negative eigenvalues.

Finally, the nonzero spectral product is \(\det(AH)=\det A\det H\). The classical Hilbert determinant identity for an \(n\)-by-\(n\) matrix, \(\det H_n=\prod_{j=0}^{n-1}(j!)^4/[(2j)!(2j+1)!]\), at \(n=2m\) gives exactly the asserted factorial product. This ends the proof.

## Verification
The accompanying `verify.py` reconstructs the integer polynomial kernel from the primitive formula using exact rational arithmetic, checks every antidiagonal coefficient and zero above it, compares the full rational determinant with the factorial expression for several orders, and checks finite Vandermonde certificates for sampled noninteger orders. Its finite calculations are consistency tests; the arguments above prove the statements for every positive real order and every positive integer order.

## Relationship to prior work
The Riemann–Liouville/Volterra fractional integration family is classical; Shkarin's 2006 study explicitly treats fractional Volterra powers and their orbit behavior, not the self-commutator rank dichotomy. Lyubich–Tsedenbayar (2010) develops singular-value boundary problems for polynomials in the integer Volterra operator and does not treat the present fractional self-commutator family. Khadkhuu–Tsedenbayar (2022) calculates self-commutator norms for the first two integer powers, which are included here as previously studied cases, but not the noninteger signed-inertia classification. Published work on finite-horizon stable rational convolution links self-commutator rank to rational realization degree; the fractional noninteger kernel is not a rational-impulse-response specialization. A distinct fractional Cesàro–Hardy self-commutator exhibits its own order-sensitive rank behavior; its definition and self-commutator are different. No theorem about those operators alone implies the full claim here without an additional transfer theorem.

## Limitations
There is no quantitative eigenvalue-decay result for noninteger orders. The theorem does not determine the nullspace or individual eigenvalues outside the integer finite spectral determinant. Historical equivalence to an unindexed generalized truncated-convolution result remains possible; novelty has not been independently certified. The result concerns only the classical power-law Volterra family on the unit interval and does not claim the same phase transition for arbitrary kernels or other boundary conditions.

## References
- S. Shkarin, “Antisupercyclic operators and orbits of the Volterra operator,” *J. London Math. Soc.* 73 (2006), 506–528, https://doi.org/10.1112/S0024610706022563 (public online record dated 24 April 2006).
- Yu. Lyubich and D. Tsedenbayar, “The norms and singular numbers of polynomials of the classical Volterra operator in \(L^2(0,1)\),” *Studia Math.* 199 (2010), 171–184, https://doi.org/10.4064/sm199-2-3.
- L. Khadkhuu and D. Tsedenbayar, “A note on self-commutators of Volterra operator and its square,” *Journal of Applied Science and Engineering A* 3 (2022), 11–16, https://doi.org/10.5564/jasea.v3i1.2455.
- Classical Cauchy–Hilbert determinant formula for \(((i+j+1)^{-1})\); applied here by elementary finite-dimensional linear algebra.
