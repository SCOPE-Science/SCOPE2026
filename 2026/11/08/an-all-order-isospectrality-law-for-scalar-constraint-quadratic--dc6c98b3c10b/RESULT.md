# An all-order isospectrality law for scalar-constraint quadratic ADMM

## Finding
Let \(n\ge2\) be any integer and consider the strictly convex equality-constrained quadratic
\[
\min_{x_1,\ldots,x_n\in\mathbb R}\sum_{i=1}^n\left(\frac{q_i}{2}x_i^2+g_i x_i\right),\qquad \sum_{i=1}^n a_i x_i=b,
\]
with \(q_i>0\), \(a_i\ne0\), arbitrary real \(g_i,b\), and penalty \(\rho>0\). In direct unrelaxed multi-block ADMM, minimize the augmented Lagrangian over the scalar blocks successively in any fixed permutation, then update the scalar dual. Write
\[
c_i=\frac{\rho a_i^2}{q_i+\rho a_i^2}\in(0,1).
\]
For every fixed update order, the error sweep on all \(n\) primal coordinates and the scalar scaled dual has exactly the characteristic polynomial
\[
\boxed{\chi(\lambda)=\frac{\lambda^2}{\lambda-1}\left[\prod_{i=1}^n(\lambda-c_i)-\lambda^{n-2}(2\lambda-1)\prod_{i=1}^n(1-c_i)\right].}
\]
The apparent pole at \(\lambda=1\) is removable. All coefficients are symmetric in \(c_1,\ldots,c_n\): **every fixed order has the same eigenvalues, with their algebraic multiplicities, and the same asymptotic spectral radius**. This does not imply identical matrices, equal finite-time errors, or order-independence when a different random order is selected at each sweep.

As a consequence for three blocks, let \(s_1=\sum_i c_i\), \(s_2=\sum_{i<j}c_ic_j\), and \(s_3=\prod_i c_i\). Then
\[
\chi(\lambda)=\lambda^2\big[\lambda^2+(s_1-1-2s_2+2s_3)\lambda+s_3\big].
\]
The two nonzero eigenvalues are strictly inside the unit disk for every \(0<c_i<1\). Thus every fixed-order three-block sweep converges linearly in the usual asymptotic sense for the stated positive-definite scalar quadratic family at every positive penalty.

## Assumptions and scope
For a fixed block order \(1,\ldots,n\), use the scaled dual \(u\) with augmented term \(\rho(\sum a_ix_i-b+u)^2/2\), discarding constants in the primal subproblems, and update \(u^+=u+\sum_i a_i x_i^+-b\). The problem has a unique primal solution and unique scalar multiplier because every \(q_i>0\) and at least one \(a_i\ne0\). Center at the unique saddle point, set \(y_i=a_i(x_i-x_i^*)\), and let \(u\) denote the centered scaled-dual error. The choice of fixed permutation amounts to relabeling the pairs \((q_i,a_i)\). No over-relaxation, proximal modification, variable penalty, or per-sweep permutation randomization is included.

## Proof
In the centered variables the entire fixed-order sweep is
\[
y_i^+=-c_i\left(\sum_{j<i} y_j^+ +\sum_{j>i}y_j+u\right),\qquad
u^+=u+\sum_{i=1}^n y_i^+.
\]
Let \(M\) be its \((n+1)\)-dimensional linear error matrix. The first old primal coordinate never appears in a new primal update, so \(M e_1=0\). Moreover the old state with \(y_1=0\), \(y_2=1-1/c_1\), all remaining old primal coordinates zero, and \(u=-1\) maps to \(e_1\). Consequently zero has algebraic multiplicity at least two.

To compute the **complete characteristic polynomial including algebraic multiplicities**, consider the equations \((\lambda I-M)(y,u)=0\). Eliminating within each row the earlier new primal coordinates by elementary triangular row operations of determinant one gives the equivalent characteristic pencil
\[
E_i=(\lambda-c_i)y_i+c_i\left(S+u+(\lambda-1)\sum_{j<i}y_j\right),\quad
E_u=(\lambda-1)u-\lambda S,
\]
where \(S=\sum_j y_j\). The same elementary operations replace the final dual row by \(E_u\), without changing the determinant.

For \(\lambda\ne1\), make the invertible linear change of variables
\[
R_i=S+u+(\lambda-1)\sum_{j<i}y_j,\qquad i=1,\ldots,n+1.
\]
Its determinant is \((-1)^n(\lambda-1)^n\). Since \(R_{i+1}-R_i=(\lambda-1)y_i\), the first \(n\) pencil rows become
\[
(\lambda-c_i)R_{i+1}-\lambda(1-c_i)R_i=0
\]
after multiplication by \(\lambda-1\). The final row becomes \(\lambda^2R_1-(2\lambda-1)R_{n+1}=0\), likewise after multiplication by \(\lambda-1\). This is a cyclic bidiagonal determinant, consisting of a forward product and one wrap-around product. Accounting for the change-of-variables determinant and row scalings gives
\[
\det(\lambda I-M)=\frac{\lambda^2}{\lambda-1}\left[\prod_i(\lambda-c_i)-\lambda^{n-2}(2\lambda-1)\prod_i(1-c_i)\right].
\]
Both sides are polynomials and agree off \(\lambda=1\), hence agree everywhere. The numerator bracket vanishes at one because both product terms equal \(\prod_i(1-c_i)\). Its quotient is monic of degree \(n-1\), proving the stated full-spectrum identity. It is manifestly invariant under arbitrary permutations of the block parameters.

For the three-block corollary write \(B=s_1-1-2s_2+2s_3\) and \(D=s_3\). A real monic quadratic \(\lambda^2+B\lambda+D\) has both roots strictly inside the unit disk iff \(1-D>0\), \(1+B+D>0\), and \(1-B+D>0\). Here \(1-D>0\), and direct factorization gives
\[
1+B+D=\sum_{i=1}^3 c_i\prod_{j\ne i}(1-c_j)>0,
\]
\[
1-B+D=1+\prod_{i=1}^3(1-c_i)+\sum_{i<j}c_ic_j>0.
\]
Thus the strict Schur conditions hold for all admissible three-block parameters, with no penalty restriction.

## Verification
The accompanying standard-library Python script `verify.py` constructs each sweep matrix directly and computes its characteristic polynomial by exact rational Faddeev–LeVerrier operations, independently of the symbolic formula. It exhausts all fixed permutations for the chosen rational samples at \(n=2,3,4,5\) and checks four additional permutations at each of \(n=6,7\). It checks the strict-Schur factorizations at rational sample triples and exact unequal finite-time examples. The recorded output `verification_output.txt` contains the assertion count. The proof above, not the finite checks, establishes the all-parameter and all-dimension conclusions.

The finite-time distinction is concrete. For \((c_1,c_2,c_3,c_4)=(1/5,2/5,3/5,4/5)\) and old state \((y_1,y_2,y_3,y_4,u)=(1,-2,3,-1,1/3)\), the complete orders \((3,2,1,4)\) and \((2,4,3,1)\) yield squared Euclidean norms \(248323/140625\) and \(1718953/140625\), respectively, despite identical characteristic polynomials. This uses the dimensionless centered scaled-dual norm, not an objective-value bound.

## Relationship to prior work
Mihić, Zhu and Ye (arXiv:1903.01786, first submitted March 5, 2019) compare randomized and cyclic multi-block ADMM for general quadratic programs. Cipolla and Gondzio (2023) analyze general quadratic random-order ADMM through a linear-algebra lens and give settings where ordering affects convergence; those general matrix settings do not imply the rank-one scalar-constraint invariance here. Sun, Luo and Ye (arXiv:1503.06387) compare random-permutation and cyclic schemes and predate the motivating source, but do not supply the present full characteristic identity in the material inspected. Ke, Ma and Zhang (2018) study general three-block separable quadratic ADMM; their article covers the three-block class, while the present statement extends to every block count and imposes a single scalar equality. Their complete article was not inspectable, leaving a possible specialist precedence risk. A separately published exact symmetric three-scalar-block penalty optimizer treats the special case of three **equal** curvatures, and neither proves nor contradicts order invariance for arbitrary heterogeneous blocks and arbitrary \(n\). Published algorithms and general convergence bounds are not claimed as new.

## Limitations
The conclusion concerns only the complete characteristic polynomial of a fixed-order exact scalar-block ADMM for a separable positive-definite quadratic with one scalar equality. It does not imply uniform finite-time norm contraction, optimality of a particular order, convergence for all larger block counts, or results for per-sweep random order selection. The three-block strict-stability corollary is an explicit consequence of the derived polynomial and may overlap earlier specialist results. Precedence against all unpublished, inaccessible, or differently formulated rank-one Gauss–Seidel results cannot be ruled out; no independent validation has been performed.

## References
1. S. Mihić, L. Zhu and Y. Ye, “Managing Randomization in the Multi-Block ADMM for Quadratic Optimization,” arXiv:1903.01786 (first posted March 5, 2019), https://arxiv.org/abs/1903.01786.
2. F. Cipolla and J. Gondzio, “A linear algebra perspective on the random multi-block ADMM: the QP case,” 2023, https://doi.org/10.1007/s10092-023-00546-0.
3. R. Sun, Z.-Q. Luo and Y. Ye, “On Efficiency of Random Permutation for ADMM and Coordinate Descent,” arXiv:1503.06387, https://arxiv.org/abs/1503.06387.
4. Y. Ke, C. Ma and H. Zhang, “Convergence of ADMM for Three-Block Separable Quadratic Programming Problems with Linear Constraints,” 2018, https://doi.org/10.4208/eajam.240817.010318.
5. “Critical-damping penalty for symmetric three-block ADMM,” published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-critical-damping-penalty-for-symmetric-three-block-admm--88ef47013166.
