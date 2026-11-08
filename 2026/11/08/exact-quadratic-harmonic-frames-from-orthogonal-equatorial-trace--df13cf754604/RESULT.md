# Exact quadratic-harmonic frames from orthogonal equatorial traces

## Finding

For integers \(d\ge3\) and \(1\le k\le d\), let \(\mathcal H_2(S^{d-1};\mathbb C)\) be the complex pure-degree-two spherical harmonics with probability-normalized surface \(L^2\) norm. Choose any \(k\) mutually perpendicular unit vectors \(v_1,\ldots,v_k\). Let \(E_i=\{x\in S^{d-1}:\langle x,v_i\rangle=0\}\), equipped with its own probability-normalized surface measure, and define
\[
R_{d,k}f=(f|_{E_1},\ldots,f|_{E_k}),\qquad
\|R_{d,k}f\|^2=\frac1k\sum_{i=1}^k\int_{E_i}|f|^2.
\]
The complete spectrum of \(C_{d,k}=R_{d,k}^{*}R_{d,k}\) is given explicitly below. In particular, \(R_{d,k}\) is injective **if and only if** \(k\ge3\), independently of \(d\). For \(k\ge3\), its exact smallest eigenvalue is
\[
\lambda_{\min}=\frac{d(d+2)}{d^2-1}\left(1-\frac2k\right).
\]
For \(d\ge k+2\), its exact largest eigenvalue is \(d(d+2)/(d^2-1)\) and hence
\[
\frac{\lambda_{\max}}{\lambda_{\min}}=\frac{k}{k-2},\qquad
\operatorname{cond}_2(R_{d,k})=\sqrt{\frac{k}{k-2}}.
\]
In particular, just three mutually orthogonal equators suffice for every quadratic harmonic in every ambient dimension, and the sharp singular-value condition number is \(\sqrt3\) for all \(d\ge5\) (\(\sqrt{5/2}\) for \(d=3\), and \(\sqrt{23/8}\) for \(d=4\)). Among all positive weights on these \(k\) fixed equators summing to one, uniform weighting uniquely maximizes the smallest eigenvalue and minimizes the singular-value condition number (minimization need not be unique).

## Assumptions and scope

A harmonic \(f\in\mathcal H_2\) is represented uniquely by \(f_A(x)=x^{\mathsf T}Ax\), with \(A\in\mathbb C^{d\times d}\) symmetric and \(\operatorname{tr}A=0\). Orthogonal invariance permits \(v_i=e_i\), the first \(k\) coordinate axes. Put \(m=d-k\) and
\[
K_{d,k}=\frac{d(d+2)}{2k(d^2-1)}.
\]
The following eigenvalue list is **with multiplicity**; branches of multiplicity zero are omitted, and numerically coincident values are combined. For off-diagonal quadratics with exactly \(s\) indices among the first \(k\), for \(s=0,1,2\), the eigenvalue is \(2(k-s)K_{d,k}\), with respective multiplicities \(\binom m2\), \(km\), and \(\binom k2\). For diagonal trace-free quadratics the eigenvalues are
\[
(2k-1)K_{d,k}\quad(k-1\text{ times}),\qquad
2kK_{d,k}\quad(m-1\text{ times if }m\ge2),
\]
and, if \(m>0\), \((2k-m/d)K_{d,k}\) once. All of these formulae are exact for \(d\ge3\) and \(1\le k\le d\).

For \(k\ge3\), the largest eigenvalue and spectral condition number are explicitly
\[
\begin{array}{c|c|c}
\text{dimension regime}&\lambda_{\max}/K_{d,k}&\lambda_{\max}/\lambda_{\min}\\
\hline
 d=k&2k-1&(2k-1)/(2k-4)\\
 d=k+1&2k-1/d&(2k-1/d)/(2k-4)\\
 d\ge k+2&2k&k/(k-2).
\end{array}
\]
The bounds concern continuous traces with equator-normalized \(L^2\) norms, not integration of each trace into a scalar, ambient-area concentration, point sampling, or arbitrary nonorthogonal equators.

## Proof

**First and fourth moments.** For the probability measure on \(S^{D-1}\),
\[
\mathbb E[x_ax_bx_cx_e]
=\frac{\delta_{ab}\delta_{ce}+\delta_{ac}\delta_{be}+\delta_{ae}\delta_{bc}}{D(D+2)}.
\]
Consequently, for any complex symmetric matrix \(B\),
\[
\int_{S^{D-1}}|x^{\mathsf T}Bx|^2\,d\sigma
=\frac{2\|B\|_F^2+|\operatorname{tr}B|^2}{D(D+2)}.
\]
In particular, the source norm of trace-free \(A\) is \(2\|A\|_F^2/[d(d+2)]\).

**Equator moment identity.** Let \(A^{(i)}\) be the principal submatrix deleting row and column \(i\). Then \(\operatorname{tr}A^{(i)}=-A_{ii}\) and \(\|A^{(i)}\|_F^2=\|A\|_F^2-2\sum_j|A_{ij}|^2+|A_{ii}|^2\). The preceding moment formula in dimension \(d-1\) gives
\[
\int_{E_i}|f_A|^2
=\frac{2\|A\|_F^2-4\sum_j|A_{ij}|^2+3|A_{ii}|^2}{(d-1)(d+1)}.
\]
Thus the Rayleigh quotient of \(C_{d,k}\) at nonzero \(A\) equals
\[
K_{d,k}\left(2k-4\frac{\sum_{i\le k,j}|A_{ij}|^2}{\|A\|_F^2}
+3\frac{\sum_{i\le k}|A_{ii}|^2}{\|A\|_F^2}\right).
\tag{1}
\]

**Invariant splitting and all multiplicities.** Coordinate sign flips make every off-diagonal matrix unit an eigenvector. Such a matrix has squared Frobenius norm twice the squared modulus of its coefficient, and its selected-row mass is \(s/2\) of its squared Frobenius norm when \(s\) endpoints lie in the chosen coordinate subset. Equation (1) therefore gives \(2(k-s)K_{d,k}\). Counting unordered pairs proves the three off-diagonal multiplicities.

On the diagonal trace-zero subspace \(V=\{(a_1,\ldots,a_d):\sum a_i=0\}\), (1) becomes \(K_{d,k}(2k I-P_VP_I P_V)\), where \(P_I\) selects the first \(k\) coordinates and \(P_V\) is orthogonal projection to \(V\). The compression \(P_VP_I P_V\) has eigenvalue one on selected-coordinate vectors summing to zero (dimension \(k-1\)), zero on unselected-coordinate vectors summing to zero (dimension \(m-1\)), and \(m/d\) on the remaining block-constant trace-zero direction when \(m>0\). This proves the remaining eigenvalues and multiplicities. Their sum of multiplicities equals \(d(d+1)/2-1\).

**Injectivity and sharp extremes.** If \(k\le2\), the nonzero harmonic \(x_1x_2\) vanishes on both selected equators (or its subset), showing failure of injectivity. If \(k\ge3\), the smallest spectral factor among the displayed values is \(2k-4>0\), on pairs of selected coordinates. The largest factor is \(2k-1\), \(2k-1/d\), or \(2k\) according as \(m=0,1,\ge2\). This proves all exact bounds and their equality cases. For \(k=3\), the minimum is always attained by the three span elements \(x_ix_j\) with \(1\le i<j\le3\).

**Optimal equator weights.** Give the \(k\) equator traces positive weights \(w_1,\ldots,w_k\) with sum one, and write \(C(w)\) for their Gram operator. Every off-diagonal quadratic \(x_ix_j\), \(i<j\le k\), is an eigenvector of \(C(w)\) with eigenvalue
\[
\frac{d(d+2)}{d^2-1}(1-w_i-w_j).
\]
The sum of the two largest weights exceeds \(2/k\) unless all \(w_i=1/k\). Therefore \(\lambda_{\min}(C(w))\le d(d+2)(1-2/k)/(d^2-1)\), with strict inequality for nonuniform weights, and equality for the uniform weights by the complete spectrum. To minimize the condition number, average \(C(w)\) over all permutations of the \(k\) selected coordinate axes; the average is \(C(1/k,\ldots,1/k)\). Convexity of the maximum eigenvalue and concavity of the minimum eigenvalue show its spectral condition number cannot increase under averaging. Taking square roots yields the claimed singular-value condition-number optimum. No unique condition-minimizer assertion is needed.

## Verification

The standalone `check_equator.py` constructs full and equatorial fourth-moment Gram matrices independently in the nonorthonormal harmonic basis \(\{x_i^2-x_d^2\}_{i<d}\cup\{2x_ix_j\}_{i<j}\). It solves generalized eigenvalue problems for all \(3\le d\le11\), \(1\le k\le d\) and compares the complete predicted spectrum, rank thresholds, and extreme ratios. Random-weight perturbations test maximin and condition-number optimality; independent unit-sphere Monte Carlo moments test the fourth-moment normalization. The replay passed 670 assertions. These finite computations are checks, not substitutes for the proof for all \(d,k\).

## Relationship to prior work

Quellmalz (2020) studies the generalized Funk–Radon transform, which **integrates each entire equatorial section into one scalar** and varies the section normal over a continuum. Quellmalz, Weissinger, Hubmer, and Erchinger (2023) give a frame decomposition of the same continuum-normal Funk transform; their Theorem 3.2 concerns inversion of those scalar integral data. Neither operator is the present **pointwise/function-valued trace on only \(k\) sections**, and their published formulas do not imply the stated finite-trace Gram matrix without a new analysis.

Xiao and Zhuang (2023) construct spherical framelets from spherical designs for partial spherical data. Their accessible abstract identifies point-grid/framelet construction rather than complete trace spectra for orthogonal equatorial subspheres; the full preprint could not be inspected, so its noncoverage is not asserted from snippets. Roddy and McEwen (2021) develop Slepian wavelets for incomplete spherical regions; this is ambient-area concentration, different from probability-normalized codimension-one traces. The present result is not a general Funk–Radon inversion or a general spherical sampling theorem.

## Limitations

The design requires mutually orthogonal section normals, continuous complete traces, probability normalization on each equator, and pure harmonic degree two. It does not treat arbitrary directions, scalar equatorial averages, higher degrees, mixed bandlimits, noisy discrete sampling, or finite-sample quadrature. The uniqueness assertion concerns maximin weighting on the given sections, not all geometries. Some exact rational factors may follow implicitly from representation theory or older restriction formulas; this is a residual historical-priority risk. Independent scientific validation has not been performed.

## References

- Y. Xiao and X. Zhuang, *Spherical framelets from spherical designs*, arXiv:2303.05365, first posted 2023-03-09; *SIAM Journal on Imaging Sciences* 16 (2023), 2072–2104. DOI: 10.1137/22M1542362. Primary MSC 42C15.
- M. Quellmalz, L. Weissinger, S. Hubmer, P. D. Erchinger, *A Frame Decomposition of the Funk-Radon Transform*, arXiv:2303.05179, first posted 2023-03-09; in *Scale Space and Variational Methods in Computer Vision* (2023), pp. 42–54.
- M. Quellmalz, *The Funk–Radon transform for hyperplane sections through a common point*, *Analysis and Mathematical Physics* 10 (2020), art. 38. DOI: 10.1007/s13324-020-00383-2.
- P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02023, first posted 2021-06-03; *IEEE Transactions on Signal Processing* 70 (2022), 6142–6153.
