# Balance maximizes covariance anisotropy for two-clique polar graph polytopes

## Finding

Let \(a,b\ge2\) be integers, let \(G_{a,b}\) be obtained by identifying one vertex of \(K_a\) and \(K_b\), and let \(N=a+b-1\). Define the symmetric edge polytope in \(H=\{x\in\mathbb R^N:\sum_i x_i=0\}\) by
\[
P_G=\operatorname{conv}\{\pm(e_i-e_j):ij\in E(G)\},
\qquad Q_G=P_G^{\circ}\subset H.
\]
All covariances and volumes use the induced Euclidean metric on \(H\), with \(X\) uniformly distributed by intrinsic \((N-1)\)-volume on \(Q_G\). Put
\[
c_a=\frac{a+2}{12a},\qquad c_b=\frac{b+2}{12b},\qquad
\Delta=(a-b)^2+(a-1)(b-1)(a+2)(b+2).
\]
Then \(\operatorname{Cov}(X)\) has exactly the following positive eigenvalues, listed with multiplicities:
\[
\begin{array}{c|c}
\lambda_A=c_a&a-2\\
\lambda_B=c_b&b-2\\
\lambda_{\pm}=\displaystyle\frac{ab+a+b\pm\sqrt{\Delta}}{12N}&1\ \text{each}.
\end{array}
\]
An eigenvalue with multiplicity zero is omitted. The extreme eigenvalues are always \(\lambda_-\) and \(\lambda_+\), respectively, and both inequalities are strict relative to all present block-contrast eigenvalues. Consequently the intrinsic covariance condition number is \(\kappa_{a,b}=\lambda_+/\lambda_-\).

For any fixed \(N\ge3\), among all integers \(a,b\ge2\) satisfying \(a+b=N+1\), the condition number is strictly increasing as the two clique sizes become more balanced: its unique minimum up to interchange is at \(\{a,b\}=\{2,N-1\}\), and its unique maximum up to interchange is at \(\{a,b\}=\{\lfloor(N+1)/2\rfloor,\lceil(N+1)/2\rceil\}\). In particular,
\[
\kappa_{a,b}\le N,
\qquad \kappa_{a,b}=N\ \Longleftrightarrow\ a=b.
\]
At fixed \(a\ge2\), the highly unequal limit is finite and explicit:
\[
\lim_{b\to\infty}\kappa_{a,b}=
\frac{a+1+\sqrt{a^2+a-1}}{a+1-\sqrt{a^2+a-1}}.
\]
Thus increasing the total vertex count need not make the polar volume distribution arbitrarily anisotropic; balancing the two cliques does, with exactly linear growth.

## Assumptions and scope

The two cliques are unweighted, simple and meet at precisely one common hub; no edges connect their other vertices. The polar is taken **within** the zero-sum hyperplane; polarity in the full space would be unbounded. The probability law is normalized intrinsic continuous volume, **not** a uniform choice among vertices of either polytope. The Euclidean metric is the restriction of the standard coordinate metric, not an arbitrary metric chosen to make the product orthogonal. Parameters \(a=2\) or \(b=2\) are included, with the corresponding absent contrast eigenclass.

## Proof

**1. Factorization of the uniform-volume law.** Label the hub \(0\), the remaining vertices of the first clique \(A\) of size \(p=a-1\), and those of the second \(B\) of size \(q=b-1\). For \(z_0=0\) define \(\Pi_N=I_N-N^{-1}\mathbf1\mathbf1^{\mathsf T}\), and set \(x=\Pi_Nz\). The map from the \(N-1\) free coordinates of \(z\) to \(H\) is an invertible linear map with constant Jacobian. Since differences are unchanged by \(\Pi_N\), the inequalities of \(Q_G\) become
\[
|z_i-z_j|\le1\quad(ij\in E(G)).
\]
They separate into the first and second clique, hence the anchored free-coordinate domain is a Cartesian product. Its uniform distribution is the product of the uniform distributions on the two complete-clique anchored Lipschitz domains, and \(X=\Pi_NZ\) for the corresponding independent factors.

**2. The complete-clique second moment.** On the centered complete-clique domain
\[
L_r=\{y\in\mathbb R^r:\sum_i y_i=0,\ \max_i y_i-\min_i y_i\le1\},\qquad r\ge2,
\]
the permutation symmetries and central reflection imply \(\mathbb EY=0\) and \(\operatorname{Cov}(Y)=c_r\Pi_r\), where \(\Pi_r=I_r-r^{-1}\mathbf1\mathbf1^{\mathsf T}\). It remains to compute \(c_r\). Partition \(L_r\) into the \(r!\) order chambers. In a fixed chamber, consecutive sorted-coordinate gaps \(d_1,\ldots,d_{r-1}\) are nonnegative and sum to at most one. Their map to \(L_r\) is linear with a constant nonzero Jacobian, the same for every chamber by permutation symmetry. The vector \((d_1,\ldots,d_{r-1},1-\sum d_i)\) therefore has the \(\operatorname{Dirichlet}(1,\ldots,1)\) law. A difference spanning \(k\) successive gaps has the \(\operatorname{Beta}(k,r-k)\) distribution and second moment \(k(k+1)/(r(r+1))\). The exact identity \(r\sum_i y_i^2=\sum_{i<j}(y_i-y_j)^2\) gives
\[
\mathbb E\|Y\|_2^2
=\frac1{r^2(r+1)}\sum_{k=1}^{r-1}(r-k)k(k+1)
=\frac{(r-1)(r+2)}{12r},
\]
because the displayed finite sum is \(r(r-1)(r+1)(r+2)/12\). Therefore \(c_r=(r+2)/(12r)\).

If \(h\) is the complete-clique hub and \(U_i=Y_i-Y_h\) for all \(i\ne h\), then direct covariance subtraction yields
\[
\operatorname{Cov}(U_i,U_j)=c_r(\delta_{ij}+1).
\]
Consequently the anchored preprojection covariance is block diagonal, with the two nonzero blocks \(c_a(I_p+J_p)\) and \(c_b(I_q+J_q)\), where \(J_s\) is the all-ones matrix.

**3. Spectrum in the intrinsic Euclidean metric.** The first block's zero-sum contrast subspace has eigenvalue \(c_a\) and dimension \(p-1=a-2\). The second block has eigenvalue \(c_b\) and dimension \(b-2\). The remaining two nonzero eigenvalues of \(\Pi_N\operatorname{Cov}(Z)\Pi_N\) equal those of its Gram-reduced two-dimensional matrix
\[
B=\frac1{12N}
\begin{pmatrix}
 b(a+2)&-\sqrt{(a-1)(b-1)(a+2)(b+2)}\\
 -\sqrt{(a-1)(b-1)(a+2)(b+2)}&a(b+2)
\end{pmatrix}.
\]
This uses the equality of the nonzero eigenvalues of \(AA^{\mathsf T}\) and \(A^{\mathsf T}A\), with \(A\) the projected square root of the covariance on the two normalized block-sum vectors. Its trace and determinant are
\[
\operatorname{tr}B=\frac{ab+a+b}{6N},\qquad
\det B=\frac{(a+2)(b+2)}{144N}>0,
\]
which gives the displayed radical formula and shows positive definiteness on \(H\).

For the extreme-eigenvalue ordering, the diagonal entries of \(B\) strictly exceed \(c_a\) and \(c_b\), respectively, because \(ab>N\) for \(a,b\ge2\). Hence \(\lambda_+>\max(c_a,c_b)\). Furthermore,
\[
\det(B-c_a I)=-\frac{(a-1)(b-1)(a+2)^2}{144a^2N}<0,
\quad
\det(B-c_b I)=-\frac{(a-1)(b-1)(b+2)^2}{144b^2N}<0.
\]
Each scalar lies strictly between the eigenvalues of \(B\). Thus \(\lambda_-<\min(c_a,c_b)\), proving the claimed extremality even when either block has size one and its contrast class is absent.

**4. Sharp balance law.** At fixed \(N=a+b-1\), put \(s=ab\). The ratio \(\lambda_+/\lambda_-\) is a strictly increasing function of \((\operatorname{tr}B)^2/\det B\), because the eigenvalues are strictly positive. This scalar simplifies to
\[
R_N(s)=\frac{4(s+N+1)^2}{N(s+2N+6)},
\qquad
R_N'(s)=\frac{4(s+N+1)(s+3N+11)}{N(s+2N+6)^2}>0.
\]
At fixed sum \(a+b=N+1\), the integer product \(s=ab\) increases strictly as the smaller clique size increases toward balance, proving both sharp extremal assertions. The same monotonicity compares all pairs with the formal balanced real pair; at \(a=b=r\), direct substitution yields
\[
\lambda_+=\frac{r+2}{12},\qquad
\lambda_-=\frac{r+2}{12(2r-1)},\qquad
\kappa_{r,r}=2r-1=N.
\]
Thus \(\kappa_{a,b}\le N\) with equality exactly at equal clique sizes (which requires odd \(N\)). Finally, dividing the two radical eigenvalues by \(b\) and sending \(b\to\infty\) gives the stated finite limit. Its denominator is positive because \((a+1)^2-(a^2+a-1)=a+2>0\).

## Verification

The standalone standard-library checker `artifacts/verify.py` integrates all complete-clique anchored second moments over every order chamber with exact rational Dirichlet moments for sizes \(2\) through \(6\). For all \(25\) ordered two-clique profiles it reconstructs and projects the full covariance, checks all \(1325\) matrix entries implicitly through the eigen-invariant tests, verifies each present contrast eigenspace and both residual trace/determinant formulas, and checks exact rational balance monotonicity over \(1936\) parameter profiles with \(3\le N<90\). Execute `python3 artifacts/verify.py` from the extracted package directory. The finite replay corroborates; the proof above establishes all integers \(a,b\ge2\).

## Relationship to prior work

Higashitani, Jochemko and Michałek [1] study symmetric edge polytopes using facet descriptions and Ehrhart methods. D'Alì, Delucchi and Michałek [2] identify their Lipschitz-polar metric interpretation and record that identifying one vertex gives a direct sum of the **primal** polytopes and a product rule for their Ehrhart numerators. Those facts justify the choice of object but give neither the intrinsic Euclidean covariance of the **polar** uniform-volume law nor the extremal condition-number classification. Kohn, Shapiro and Sturmfels [3] develop general moment methods for polytopes; their generic theory does not evaluate this family. A previously known covariance formula for the vertex-uniform **graphical zonotope** of the same two-clique graph concerns a different polytope and a different probability measure, and does not imply the result here.

## Limitations

The result applies only to two unweighted cliques meeting in exactly one vertex and to the specified intrinsic Euclidean metric. It does not assert a universal extremal law among all connected graphs or all metric choices. The novelty comparison is a best-knowledge literature assessment, not a proof of historical priority. The exact computations cover only finite instances, while the infinite-family claim is proved analytically. No independent mathematical audit has been performed.

## References

[1] A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, first public July 20, 2018; *Mathematika* 65 (2019), 763–784.

[2] A. D'Alì, E. Delucchi, M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193, first public October 11, 2019; *Electronic Journal of Combinatorics* 29 (2022), #P3.24; especially §§2.3, 4.2.

[3] K. Kohn, B. Shapiro, B. Sturmfels, *Moment Varieties of Measures on Polytopes*, arXiv:1807.10258 (first public July 30, 2018); general moments and simplex generating functions.
