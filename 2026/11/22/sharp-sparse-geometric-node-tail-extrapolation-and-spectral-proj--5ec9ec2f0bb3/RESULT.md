# Sharp sparse geometric-node tail extrapolation and spectral projector recovery

## Finding
Fix \(0<q<1\) and \(m\ge1\). Given any distinct nonnegative integers \(0\le k_0<\cdots<k_{m-1}\), let \(p_y\) be the unique complex polynomial of degree at most \(m-1\) satisfying \(p_y(q^{k_i})=y_i\). Define the tail extrapolation map \(E_{q,\boldsymbol{k}}:\ell_\infty^m\to\ell_\infty(\{n>k_{m-1}\})\) by \((E_{q,\boldsymbol{k}}y)_n=p_y(q^n)\). Its *exact* operator norm is
\[
\Lambda(q,\boldsymbol{k})=\sum_{i=0}^{m-1}\prod_{j\ne i}\frac{q^{k_j}}{|q^{k_i}-q^{k_j}|}.
\]
For \(m\ge2\), the sharp all-subset classification is
\[
1<\Lambda(q,\boldsymbol{k})\le\mathcal L_m(q):=\prod_{r=1}^{m-1}\frac{1+q^r}{1-q^r},
\]
with equality on the right **if and only if** all index gaps \(k_{i+1}-k_i=1\). The infimum over all such index sets is \(1\), not attained; it is approached by letting all consecutive gaps tend to infinity. For \(m=1\), \(\Lambda=1\). The sign pattern \(y_i=(-1)^{m-1-i}\) realizes the operator norm as a supremum of tail values, approached as \(n\to\infty\). Consequently every number of samples, and every sparse subset of the geometric spectrum, obey the sharp uniform ceiling
\[
\Lambda(q,\boldsymbol{k})\le \mathcal L_\infty(q):=\prod_{r=1}^{\infty}\frac{1+q^r}{1-q^r}<\infty;
\]
the constant is optimal across all finite sample sets.

For the compact positive diagonal operator \(D_qe_n=q^ne_n\) on \(\ell^2(\mathbb N_0)\), let \(\ell_{N,j}(x)\) be the cardinal polynomial on \(1,q,\ldots,q^N\), and let \(P_j\) project onto \(\mathbb Ce_j\). For all integers \(N\ge j\ge0\),
\[
\left\|\ell_{N,j}(D_q)-P_j\right\|=\frac{q^{(N-j)(N-j+1)/2}}{\prod_{r=1}^j(1-q^r)\prod_{r=1}^{N-j}(1-q^r)}.
\]
In particular every coordinate projection is uniformly norm-approximated by explicit polynomials of \(D_q\), at a superexponential rate in the cutoff \(N\) for fixed \(j\).

## Assumptions and scope
All spaces and operators are complex. The geometric ratio is fixed strictly between zero and one; arbitrary finite index sets are allowed, but nodes are positive and strictly decreasing. The data norm is the maximum absolute value, and the extrapolation norm is a supremum over the **later geometric nodes only**, not over the entire original interval. \(D_q\) is the diagonal operator on the specified standard orthonormal basis. No estimate on polynomial coefficients or noise outside the stated nodal data model is asserted.

## Proof
Write \(x_i=q^{k_i}\), so \(x_0>\cdots>x_{m-1}>0\), and define the cardinal polynomials
\[
\ell_i(x)=\prod_{j\ne i}\frac{x-x_j}{x_i-x_j},\qquad p_y(x)=\sum_i y_i\ell_i(x).
\]
For \(0\le x<x_{m-1}\), each factor \(|x-x_j|=x_j-x\) increases as \(x\downarrow0\), so each \(|\ell_i(x)|\) strictly increases to \(|\ell_i(0)|\) for \(m\ge2\). The signs of \(\ell_i(x)\) on that interval are fixed and equal to \((-1)^{m-1-i}\). Thus the \(\ell_\infty\)-to-\(\ell_\infty\) operator norm is the sum of the \(|\ell_i(0)|\), with the displayed alternating sign data attaining its limiting supremum. This yields the first exact formula.

Set \(r_s=x_{s+1}/x_s=q^{k_{s+1}-k_s}\) for \(s=0,\ldots,m-2\). Each \(0<r_s\le q\). For \(j<i\), the factor in \(|\ell_i(0)|\) contributed by \(j\) equals \((1-\prod_{s=j}^{i-1}r_s)^{-1}\); for \(j>i\), it equals \((\prod_{s=i}^{j-1}r_s)/(1-\prod_{s=i}^{j-1}r_s)\). Every one of these positive factors is nondecreasing in every \(r_s\) and, for every adjacent gap \(r_s\), at least one factor in a strictly positive summand increases strictly with \(r_s\). Hence \(\Lambda\) is strictly increasing in each \(r_s\), proving unique maximality at \(r_s=q\), i.e. consecutive indices. Sending every \(r_s\) to zero gives \(\Lambda\to1\); for \(m\ge2\) at least one alternating cardinal weight is negative while all sum to one, hence \(\Lambda>1\).

For consecutive indices, scaling all nodes reduces them to \(1,q,\ldots,q^{m-1}\). Directly collecting factors in \(\ell_i(0)\) yields, with \((q;q)_r:=\prod_{s=1}^r(1-q^s)\) and \((q;q)_0:=1\),
\[
|\ell_i(0)|=\frac{q^{(m-1-i)(m-i)/2}}{(q;q)_i(q;q)_{m-1-i}}.
\]
The finite \(q\)-binomial theorem (or an induction in \(m\)) sums these terms to \(\prod_{r=1}^{m-1}(1+q^r)/(1-q^r)\). The infinite product converges because the logarithms of its factors are \(O(q^r)\). Taking \(m\to\infty\) through consecutive index sets proves global sharpness.

Finally, the spectral theorem for the explicitly diagonal \(D_q\) gives \(\ell_{N,j}(D_q)e_i=\delta_{ij}e_i\) for \(i\le N\). For \(i>N\), \(|\ell_{N,j}(q^i)|\) strictly increases to \(|\ell_{N,j}(0)|\), whence the operator-norm difference equals \(|\ell_{N,j}(0)|\). The factor formula immediately above, with \(m=N+1\) and \(i=j\), gives the displayed expression. Its denominator converges to the strictly positive Euler product \((q;q)_\infty\) in the second factor, and the numerator decays as \(q^{(N-j)^2/2+O(N)}\). This completes the proof.

## Verification
The accompanying standalone `checker.py` uses exact rational arithmetic for three geometric ratios, arbitrary sparse patterns with up to four sample points, and the stated projection coefficients. It reports `GEOMETRIC_SPECTRAL_EXTRAPOLATION_EXACT_OK 9327`. These finite checks are diagnostics, not a replacement for the universal proof. Reproduce with `python3 checker.py` (Python standard library only).

## Relationship to prior work
Tao's 2026 local Bernstein paper proves lower bounds for classical Lebesgue constants on real intervals and explicitly defines Lagrange fundamental polynomials; the present theorem instead treats tail extrapolation on a **discrete** geometrically accumulating sequence and classifies the worst sparse index sets. Masjed-Jamei, Milovanović and Jafari (2011) study geometric-node quadrature using the finite \(q\)-binomial theorem, but do not in their displayed results address the sparse-index extrapolation norm or norm recovery of coordinate spectral projections. Ibrahimoglu (2016) surveys ordinary interpolation Lebesgue constants and condition numbers. The 2026 diagonal-commutant work of Wang and Yao treats qualitative polynomial weak-operator closure, not the explicit optimal norm rates here. None of these statements is represented as newly invented.

## Limitations
The theorem concerns strictly geometric nodes and only the tail containing smaller positive nodes. It does not establish whole-interval interpolation stability, approximation of arbitrary functions, or sharp constants for general non-geometric spectra. The originality comparison was bounded, not an exhaustive survey of all classical geometric-grid literature; a direct earlier identity for the sparse extremum may remain undiscovered. Independent review has not been performed.

## References
1. Terence Tao, *Local Bernstein theory, and lower bounds for Lebesgue constants*, arXiv:2603.21453, first posted 2026-03-23, https://arxiv.org/abs/2603.21453.
2. M. Masjed-Jamei, G. V. Milovanović and M. A. Jafari, *Explicit forms of weighted quadrature rules with geometric nodes*, Math. Comput. Modelling 53 (2011), 1133–1139, https://doi.org/10.1016/j.mcm.2010.11.076.
3. B. A. Ibrahimoglu, *Lebesgue functions and Lebesgue constants in polynomial interpolation*, J. Inequal. Appl. 2016:93, https://doi.org/10.1186/s13660-016-1030-3.
4. M. Wang and X. Yao, *Commutants of diagonal operators*, arXiv:2611.22802 (2026-11-17), https://arxiv.org/abs/2611.22802. Listed only as later supporting context, not as the dating source.
