# Cyclic Chebyshev aliasing and a reentrant two-level trace-design boundary

## Finding
For the normalized adjacency matrix \(A=(S+S^{-1})/2\) of a simple cycle with \(n\ge3\) vertices, let \(T_j\) denote the first-kind Chebyshev polynomial and let \(Z_j=z^{\mathsf T}T_j(A)z\), where the entries of \(z\) are independent symmetric signs. For every \(1\le j,k\le n-1\),
\[
\operatorname{Cov}(Z_j,Z_k)=n\bigl({\bf1}_{j=k}+{\bf1}_{j+k=n}\bigr).
\]
Thus the only distinct correlated degrees below \(n\) are the exact cyclic aliases \(j\) and \(n-j\). In particular, for the geometric Chebyshev polynomial \(p_{n-1,r}(x)=\sum_{j=0}^{n-1}r^jT_j(x)\), \(0<r<1\), separating its degrees into two independently sampled contiguous blocks at cutoff \(k\) reduces variance relative to using one shared probe by exactly \(2n r^n\min\{k,n-1-k,\lfloor(n-1)/2\rfloor\}\), when each block is sampled once.

A sharp consequence concerns the smallest simple even cycle, \(C_4\), under the explicitly specified *one-sided Chebyshev-recurrence* work model. If a sample of the first degree block through \(k\) costs \(k\) matrix-vector products and a sample of the final block through degree three costs three products, and positive real sample allocations are optimized at fixed total work, then the uniquely optimal two-block cutoff switches **twice** as \(r\) increases. More precisely, there are exactly two values \(r_-\in(0.237,0.238)\) and \(r_+\in(0.809,0.810)\), with numerical values
\[
r_-=0.237180713823998\ldots,\qquad r_+=0.809548040154000\ldots,
\]
such that cutoff \(k=1\) is strictly optimal for \(0<r<r_-\) and \(r_+<r<1\); cutoff \(k=2\) is strictly optimal for \(r_-<r<r_+\); both tie at the two thresholds. This is reentrance of the lower-cost cutoff in a standard continuous-allocation surrogate, not a statement about optimal integral probe counts or optimized matrix-function implementations.

## Assumptions and scope
A simple unweighted cycle means \(n\ge3\). The shift matrix \(S\) cyclically permutes the standard basis, and \(A=(S+S^{\mathsf T})/2\). The signs in a single probe are independent and equally likely \(\pm1\). For the two-block estimator, probes in different blocks and repeated draws within a block are independent. The constant \(T_0(A)=I\) has zero sign-probe variance.

A two-block partition at integer \(1\le k\le n-2\) uses the matrices \(B_1=\sum_{j=0}^k r^jT_j(A)\) and \(B_2=\sum_{j=k+1}^{n-1}r^jT_j(A)\). The one-per-block comparison uses one probe for each block, with no claim of equal matrix-vector cost versus sharing a probe. For the \(C_4\) work frontier, one-sided Chebyshev recurrence is used without exploiting graph-specific polynomial identities or the faster two-sided evaluation algorithm. With \(m_1,m_2>0\) **real**, the modeled cost is \(W=km_1+3m_2\) and variance is \(V_1/m_1+V_2/m_2\). The result optimizes this continuous relaxation only. In particular, the cost model is not intended to describe a specialized implementation for a known four-vertex matrix.

## Proof
For any integer \(j\ge0\), the identity \(T_j((S+S^{-1})/2)=(S^j+S^{-j})/2\) follows by the Chebyshev recurrence, starting from \(T_0=I\) and \(T_1=A\). For \(1\le j<n\), the diagonal vanishes and
\[
Z_j=\sum_{a=0}^{n-1}z_a z_{a+j\bmod n}.
\]
For two such quadratic forms, centered fourth moments of independent symmetric signs vanish except when the two unordered index pairs coincide. Counting these pairs gives \(n\) matches for \(j=k\), another \(n\) for \(j+k=n\), and no others, proving the covariance identity. It also covers the self-inverse degree \(j=k=n/2\) for even \(n\), where the two contributions add to \(2n\).

For geometric coefficients, an alias pair \(\{j,n-j\}\) contributes shared-probe covariance \(2n r^j r^{n-j}=2n r^n\) but contributes no cross-block covariance when it is split by the cutoff. The number of separated pairs is exactly \(\min\{k,n-1-k,\lfloor(n-1)/2\rfloor\}\). This proves the stated universal variance difference; diagonal terms and a possible even-cycle Nyquist term cancel in the difference.

On \(C_4\), \(T_1(A)=T_3(A)\), and \(T_2(A)=S^2\). The preceding covariance identity gives the exact variances of the two independent blocks:
\[
\begin{array}{c|cc|cc}
k&V_1&V_2&C_1&C_2\\ \hline
1&4r^2&8r^4+4r^6&1&3\\
2&4r^2+8r^4&4r^6&2&3
\end{array}
\]
where \(C_i\) denotes modeled work per sample. By Cauchy–Schwarz,
\[
(V_1/m_1+V_2/m_2)(C_1m_1+C_2m_2)\ge(\sqrt{C_1V_1}+\sqrt{C_2V_2})^2,
\]
with equality uniquely at \(m_1/m_2=\sqrt{V_1C_2/(V_2C_1)}\). Accordingly, the two optimized variance-work products are
\[
K_1=4r^2\left(1+r\sqrt{3(2+r^2)}\right)^2,
\qquad K_2=4r^2\left(\sqrt{2+4r^2}+\sqrt3\,r^2\right)^2.
\]
The sign of \(K_2-K_1\) equals that of
\[
\Delta(r)=1-2r^2+2\sqrt3\,r^2\sqrt{2+4r^2}-2\sqrt3\,r\sqrt{2+r^2}.
\]
Let \(U(r)=1-2r^2\) and \(R(r)=-48r^6-16r^4+28r^2-1\). Every genuine zero of \(\Delta\) satisfies \(R=4\sqrt3\,r^2U\sqrt{2+4r^2}\), hence is a root of
\[
P(r)=2304r^{12}+768r^{10}-2048r^8-608r^6+720r^4-56r^2+1.
\]
An exact rational Sturm calculation finds exactly four simple roots of \(P\) in \((0,1)\), one in each of \((0.164,0.165)\), \((0.237,0.238)\), \((0.751,0.752)\), and \((0.809,0.810)\). Rational interval bounds show that \((\operatorname{sgn}R,\operatorname{sgn}U)\) in these intervals are, in order, \((-1,+1),(+1,+1),(+1,-1),(-1,-1)\). Thus the first and third polynomial roots are extraneous consequences of squaring; precisely the second and fourth pass the necessary sign test. The sign test is also sufficient because \(U+2\sqrt3\,r^2\sqrt{2+4r^2}>0\) throughout \((0,1)\), so taking the positive square root recovers \(\Delta=0\). Finally, \(\Delta>0\) near \(r=0\) and \(r=1\), and \(\Delta<0\) at \(r=1/2\); continuity and the exactly two simple zeros give all strict regimes and boundary ties.

## Verification
Run `python verify.py` with `sympy>=1.12`. The program recomputes the elimination polynomial, exact rational Sturm root counts, admissibility signs, the two threshold approximations, Chebyshev shift identities for cycles \(3\le n\le8\), and sign-probe covariance formulas by independent finite enumeration for \(3\le n\le7\). These finite checks supplement, but do not replace, the universal algebraic proof. The roots are algebraic rather than exact decimal data.

## Relationship to prior work
Hallman and Troester, *A Multilevel Approach to Stochastic Trace Estimation* (arXiv:2103.10516, first publicly posted March 18, 2021), give the general block estimator, continuous work-allocation formula and dynamic-programming level selection. Their equations (2.6)–(3.4) already imply how to optimize levels once their variances are supplied. In particular their general continuous-allocation principle is **not** claimed as new. Their Remark 1 discusses the nontriviality of cross-degree covariance. The claim here is the explicit full cyclic covariance classification and sharp, twice-reversing optimal cutoff for the geometric family in the stated work model; these are not stated in the inspected text. Hallman, *Faster Stochastic Trace Estimation with a Chebyshev Product Identity* (arXiv:2101.00325, January 1, 2021), supplies a faster alternative polynomial-evaluation algorithm that changes the cost model; the reentrant cutoff is not universal across implementation models. Cortinovis and Kressner (arXiv:2005.10009, May 20, 2020) analyze broad randomized trace-estimator concentration, not this cyclic covariance/level-phase classification. An equivalent consequence of earlier cyclic/Fourier trace-probing literature remains a publication-priority risk.

## Limitations
This is an exact structural test case, not an efficiency recommendation for a known four-vertex cycle: its trace may be computed directly. The reentrant claim uses real-valued idealized allocation and a one-sided, degree-proportional matrix-vector cost, not integer budgets, wall-clock cost, or the two-sided Chebyshev identity. It optimizes among **exactly two nonempty contiguous blocks** on \(C_4\), not all possible numbers of levels or other probe distributions. The general covariance identity assumes uniform signs and the specific normalized cycle adjacency. The polynomial itself is a finite geometric Chebyshev expansion, not a claim of optimal interpolation error. Publication priority needs independent specialist assessment.

## References
1. E. Hallman and D. Troester, *A Multilevel Approach to Stochastic Trace Estimation*, arXiv:2103.10516 (March 18, 2021), https://arxiv.org/abs/2103.10516.
2. E. Hallman, *Faster Stochastic Trace Estimation with a Chebyshev Product Identity*, arXiv:2101.00325 (January 1, 2021), https://arxiv.org/abs/2101.00325.
3. A. Cortinovis and D. Kressner, *On Randomized Trace Estimates for Indefinite Matrices with an Application to Determinants*, arXiv:2005.10009 (May 20, 2020), https://arxiv.org/abs/2005.10009.
