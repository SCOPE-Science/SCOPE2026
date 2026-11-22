# Exact spectral-optimal sensor amplitudes for positive diagonal operator orbits

## Finding
Let \(n\ge2\), \(N\ge n-1\), and let \(0<a_1<\cdots<a_n<1\) be pairwise distinct real numbers. Write \(A=\operatorname{diag}(a_1,\ldots,a_n)\) on complex Euclidean space \(\mathbb C^n\). For each single sensor \(g\in\mathbb C^n\) with \(\|g\|_2=1\), define the finite-horizon orbit-frame operator
\[
W_N(g)=\sum_{k=0}^{N}A^k gg^* A^k.
\]
Put
\[
C_{ij}=\sum_{k=0}^{N}(a_i a_j)^k
=\frac{1-(a_i a_j)^{N+1}}{1-a_i a_j},\quad
\varepsilon_i=(-1)^{i-1},\quad
H_{ij}=\varepsilon_i (C^{-1})_{ij}\varepsilon_j,
\]
\[
r_i=\sum_{j=1}^n H_{ij},\qquad L=\sum_{i=1}^n r_i.
\]
Then every entry of \(H\), every \(r_i\), and \(L\) is strictly positive. The exact best achievable lower orbit-frame bound is
\[
\boxed{\max_{\|g\|_2=1}\lambda_{\min}(W_N(g))=\frac1L.}
\]
Moreover, equality holds **if and only if**
\[
\boxed{|g_i|^2=\frac{r_i}{L}\quad(1\le i\le n),}
\]
with arbitrary complex phases. Thus the optimal vector of squared sensor magnitudes is unique for every admissible spectrum and horizon. No numerical optimization over sensor coefficients is needed: invert one explicitly given positive-definite matrix and sum its checkerboard-signed inverse rows.

For the exact three-mode example \(n=3\), \(N=2\) and \((a_1,a_2,a_3)=(1/4,1/2,3/4)\), one obtains
\[
H=\begin{pmatrix}173&297&127\\297&521&227\\127&227&101\end{pmatrix},
\quad(r_1,r_2,r_3)=(597,1045,455),\quad L=2097.
\]
Consequently \(\max\lambda_{\min}(W_2(g))=1/2097\), achieved exactly when \((|g_1|^2,|g_2|^2,|g_3|^2)=(597,1045,455)/2097\).

## Assumptions and scope
The horizon \(N\) is an integer, the observation times are precisely \(k=0,1,\ldots,N\), the evolution is a positive diagonal self-adjoint contraction with distinct eigenvalues strictly between zero and one, and the sensor has unit Euclidean norm. All bounds are finite-dimensional and deterministic. The lower frame bound is the smallest eigenvalue of \(W_N(g)\); phase changes are unitary congruences and cannot affect its spectrum. If \(N<n-1\), the orbit has fewer than \(n\) vectors, so the lower frame bound is zero for every \(g\). If two eigenvalues coincide, the orbit of any single sensor fails to span the corresponding two-dimensional eigenspace, and the lower frame bound is likewise zero.

## Proof
**1. Strict total positivity of the orbit kernel.** Form the rectangular Vandermonde matrix \(V\) with entries \(V_{ik}=a_i^k\), \(1\le i\le n\), \(0\le k\le N\). Then \(C=VV^{\mathsf T}\). For every ordered pair of row/column index sets \(I,J\) of equal size \(m\), Cauchy–Binet yields
\[
\det C[I,J]=\sum_{0\le k_1<\cdots<k_m\le N}
\det V[I,(k_1,\ldots,k_m)]\,
\det V[J,(k_1,\ldots,k_m)].
\]
Every generalized Vandermonde determinant in this sum is strictly positive: the nodes are strictly increasing and positive, and the exponents strictly increase. For \(m\le n\le N+1\), the sum is nonempty. Hence every minor of \(C\) is strictly positive. In particular, \(C\) is positive definite and invertible. Cofactor inversion of a strictly totally positive matrix gives the *strict checkerboard inverse rule*,
\[
(-1)^{i+j}(C^{-1})_{ij}>0
\quad(1\le i,j\le n),
\]
so the matrix \(H\) defined above is symmetric, positive definite, and strictly positive entrywise.

**2. A universal upper bound.** Suppose first that no coordinate of \(g\) vanishes. Let \(d_i=|g_i|>0\), \(D=\operatorname{diag}(d_1,\ldots,d_n)\), \(d=(d_i)\), and \(E=\operatorname{diag}(\varepsilon_1,\ldots,\varepsilon_n)\). Up to diagonal unitary congruence, \(W_N(g)=DCD\), while its inverse is spectrally equivalent to \(D^{-1}HD^{-1}\). Since \(\|d\|_2=1\), the Rayleigh inequality gives
\[
\lambda_{\max}(D^{-1}HD^{-1})
\ge d^{\mathsf T}D^{-1}HD^{-1}d
=\boldsymbol 1^{\mathsf T}H\boldsymbol 1=L.
\]
Inverting the positive-definite eigenvalues proves \(\lambda_{\min}(W_N(g))\le1/L\). If a coordinate vanishes, \(W_N(g)\) is singular and its smallest eigenvalue is zero, still strictly below \(1/L\).

**3. Exact attainment and uniqueness.** Define \(d_i=\sqrt{r_i/L}\), so \(\sum_i d_i^2=1\). Positivity of \(H\) implies \(r_i>0\). Direct multiplication gives
\[
(D^{-1}HD^{-1})d=D^{-1}H\boldsymbol1
=D^{-1}r=Ld.
\]
The matrix \(D^{-1}HD^{-1}\) is strictly positive entrywise and positive definite. By the Perron–Frobenius theorem, its strictly positive eigenvector \(d\) belongs to the simple *largest* eigenvalue. Therefore that eigenvalue is exactly \(L\), proving equality in the displayed optimal lower-bound formula.

Conversely, if a sensor achieves equality, its coordinate magnitudes are all positive and the Rayleigh inequality of Step 2 is equality. Thus \(d\) is a largest-eigenvalue eigenvector of \(D^{-1}HD^{-1}\), necessarily with eigenvalue \(L\). Multiplying the eigenequation by \(D\) yields \(H\boldsymbol1=L(d_i^2)_{i=1}^n\), or \(d_i^2=r_i/L\) for every coordinate. Arbitrary coordinate phases amount to diagonal unitary congruence, completing the equality classification.

**4. Exact example.** Rational inversion for the three nodes and three observations listed above yields
\[
C=\begin{pmatrix}
273/256&73/64&313/256\\73/64&21/16&97/64\\313/256&97/64&481/256
\end{pmatrix},
\]
and its checkerboard-signed inverse \(H\) has the entries stated in the finding. The row sums and their total give \(L=2097\). The general proof then establishes the exact minimum eigenvalue and optimizer without numerical eigenvalue approximations.

## Verification
The accompanying stand-alone `verify_optimal_sensor.py` runs under Python 3 with no third-party dependencies. It uses exact rational arithmetic to independently build orbit Gram matrices, invert them, confirm every strict minor, confirm the checkerboard signs and row sums, and check positive-semidefinite sharpness certificates (all principal minors of \(C-\operatorname{diag}(1/r_i)\) are nonnegative, with determinant zero and the prescribed null vector). It checks the displayed three-mode instance and additional deterministically selected rational systems with two, three and four modes. It reports `OPTIMAL_ORBIT_SENSOR_RATIONAL_OK 885` on successful completion. These finite checks are diagnostics; the strict total-positivity and Perron–Frobenius argument above supplies the all-dimensional, all-horizon proof.

## Relationship to prior work
Giribet and Feldberg (2026) formulate finite-horizon dynamical observability, its frame Gramian, and reconstruction under unmodeled forcing; they do not optimize the magnitudes of one sensor for the smallest frame eigenvalue. Aguilera, Cabrelli, Negreira and Paternostro (2025, updated 2026) use “optimal” to mean minimal numbers of orbit generators and construct Parseval frames, not this finite-horizon unit-energy sensor optimization. Wu (2026) optimizes sampling-time sets and temporal weights while holding the operator and generating vectors fixed; this is a different design variable and objective. Wan, Roy and Saberi (2008) optimize spectral radii of nonnegative matrices under linear resource constraints, but their stated allocation constraint does not give the reciprocal-square sensor constraint here. Strict total positivity, checkerboard inverses, Rayleigh bounds and Perron–Frobenius theory are established ingredients, not claimed discoveries. The assessed contribution is their exact synthesis into a sharp all-mode, all-admissible-horizon sensor law with unique squared-amplitude allocation.

## Limitations
The theorem assumes a single freely orientable complex sensor, distinct positive real modal eigenvalues, a full consecutive observation horizon, and a unit sensor-energy budget. It does not optimize spatially constrained physical sensor placements, multiple sensors, nonnormal evolutions, complex eigenvalue configurations, arbitrary temporal sampling weights, or condition numbers. A general positive-matrix scaling principle may contain the algebraic core in an older alternative formulation; a literature search does not establish absence of such a formulation.

## References
1. J. I. Giribet and S. Feldberg, *Augmented Dynamical Sampling under unmodeled Forcing*, arXiv:2611.17137v1, publicly posted 12 November 2026. https://arxiv.org/html/2611.17137v1
2. A. Aguilera, C. Cabrelli, F. Negreira and V. Paternostro, *Optimal Dynamical Frames*, arXiv:2506.00567 (2025; v3 posted July 2026). https://arxiv.org/html/2506.00567v3
3. J. Wu, *Optimal weighted sampling of positive and normal operator orbits*, arXiv:2610.31278, 22 October 2026. https://arxiv.org/abs/2610.31278
4. Y. Wan, S. Roy and A. Saberi, *A new focus in the science of networks: towards methods for design*, Proceedings of the Royal Society A 464 (2008), 513–535, doi:10.1098/rspa.2007.0050. https://doi.org/10.1098/rspa.2007.0050
