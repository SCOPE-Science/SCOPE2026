# Strict Gaussian precision signs for part-size counts in uniform integer compositions

## Finding

Fix an integer \(m\geq 2\). Draw an ordered composition of the integer \(n\) uniformly from the \(2^{n-1}\) compositions, and let \(C_{n,r}\) be the number of parts of length \(r\), for \(1\leq r\leq m\). Put \(p_r=2^{-r-1}\). The centered vector, divided by \(\sqrt n\), converges to a nondegenerate centered Gaussian with covariance matrix
\[
\Sigma_m(r,s)=p_r\mathbf 1_{\{r=s\}}+(3-r-s)p_rp_s.
\]
Define
\[
a_m=\frac{1-2^{-m}}2,\qquad d_m=\frac{m+2}{2^{m+1}},\qquad e_m=\frac{m^2+4m+6}{2^{m+1}},\qquad \Delta_m=a_me_m+d_m^2.
\]
The covariance matrix is strictly positive definite and its inverse has the **exact** form
\[
\boxed{(\Sigma_m^{-1})_{rs}=\frac{\mathbf 1_{\{r=s\}}}{p_r}+\frac{a_mrs+d_m(r+s)-e_m}{\Delta_m}.}
\]
For every \(m\ge3\), every off-diagonal entry of \(\Sigma_m^{-1}\) is strictly positive. Thus all pairwise *Gaussian linear partial correlations*, conditional on the remaining \(m-2\) part-size coordinates, are strictly negative. The exceptional two-dimensional matrix has \((\Sigma_2^{-1})_{12}=0\). For every fixed pair \(r\ne s\), the corresponding partial correlation tends to \(-1\) as \(m\to\infty\) (with \(m\ge\max\{r,s\}\)). In particular, the singleton and doubleton counts are asymptotically uncorrelated in their two-dimensional limit, but become negatively partially correlated on including the length-three count.

A supporting *finite-size* classification holds: for every \(n\ge2\) and every distinct \(1\le r,s\le n\), \(\operatorname{Cov}(C_{n,r},C_{n,s})<0\). When \(n\ge r+s+1\), its value is
\[
\operatorname{Cov}(C_{n,r},C_{n,s})=-\frac{(r+s-3)(n-r-s)+3(r+s)+rs-5}{2^{r+s+2}}.
\]
This scalar formula supplies the covariance asymptotics; the precision sign classification and its degeneration as the collection of observed lengths expands constitute the central result.

## Assumptions and scope

All compositions are *unrestricted, ordered, positive-integer compositions* of fixed total \(n\), sampled uniformly. For the Gaussian statement, \(m\) stays fixed while \(n\to\infty\). Only after the Gaussian covariance has been formed is \(m\to\infty\) taken, holding the selected lengths \(r,s\) fixed. These are sequential limits, not a joint growing-dimensional central limit theorem. A Gaussian linear partial correlation means \(-P_{rs}/\sqrt{P_{rr}P_{ss}}\) for the Gaussian precision matrix \(P=\Sigma_m^{-1}\), not an assertion about exact finite-sample conditional independence or correlation given discrete counts.

## Proof

**1. Moments and covariance.** Let \(A(z)=z/(1-z)\) be the generating function for one unrestricted part. Marking occurrences of each selected size gives the multivariate generating function
\[
F(z;u_1,\ldots,u_m)=\left(1-A(z)-\sum_{r=1}^m(u_r-1)z^r\right)^{-1}.
\]
The coefficient of \(z^n\) at unit marks is \(2^{n-1}\) for \(n\ge1\). At unit marks, differentiation gives
\[
\partial_{u_r}F=z^r\frac{(1-z)^2}{(1-2z)^2},\qquad
\partial_{u_r}\partial_{u_s}F=2z^{r+s}\frac{(1-z)^3}{(1-2z)^3}.
\]
The second identity gives a second *factorial* moment when \(r=s\), and an ordinary mixed moment otherwise. For \(k\ge1\), the coefficient identities are
\[
[z^k]\frac{(1-z)^2}{(1-2z)^2}=2^{k-2}(k+3),\qquad
[z^k]\frac{(1-z)^3}{(1-2z)^3}=2^{k-4}(k+2)(k+7).
\]
At \(k=0\), both coefficients equal \(1\), and the second displayed polynomial formula must not be applied. Consequently, for \(n\ge r+s+1\),
\[
\mathbb EC_{n,r}=\frac{n-r+3}{2^{r+1}},\qquad
\mathbb E\big[C_{n,r}(C_{n,s}-\mathbf1_{\{r=s\}})\big]
=\frac{(n-r-s+2)(n-r-s+7)}{2^{r+s+2}}.
\]
For every fixed \(m\), if \(n\ge2m+1\), subtracting the products of the means gives
\[
\operatorname{Cov}(C_{n,r},C_{n,s})=
\frac{n-r+3}{2^{r+1}}\mathbf1_{\{r=s\}}
+\frac{n(3-r-s)+r^2+rs+s^2-6(r+s)+5}{2^{r+s+2}}.
\]
Division by \(n\) yields the claimed \(\Sigma_m\). For \(r\ne s\), if \(\max(r,s)\le n<r+s\), the two counts cannot simultaneously be positive, so their covariance is negative. If \(n=r+s\), the covariance equals \([7-3(r+s)-rs]2^{-r-s-2}<0\). If \(n>r+s\), the numerator in the negative formula is strictly positive because \(r+s\ge3\) and \(3(r+s)+rs-5\ge6\).

**2. A nondegenerate Gaussian limit.** A uniform composition is encoded by independent fair cut indicators in the \(n-1\) internal gaps. For each fixed \(r\), an interior length-\(r\) part is the local cut pattern consisting of a cut, followed by \(r-1\) noncuts, followed by a cut. Summing the corresponding indicators, with only a bounded number of boundary corrections, expresses the vector of part-size counts as a sum of bounded, stationary, \((m+1)\)-dependent vector-valued variables. The multivariate central limit theorem follows by the elementary blocking argument: divide the sequence into blocks of length \(\lfloor n^{1/4}\rfloor\), omit fixed-width separating gaps, apply independent-block Lindeberg convergence to each linear projection, and show that discarded terms have variance \(o(n)\) by finite dependence. Cramér–Wold gives the joint Gaussian limit; its covariance is \(\Sigma_m\) as computed above.

Positive definiteness can also be checked independently. If \(G\) has the geometric law \(\Pr(G=r)=2^{-r}\), and \(h(G)=t_r\) for \(r\le m\) and \(0\) otherwise, then, writing \(\lambda=\mathbb E h(G)/\mathbb E G\),
\[
t^\top\Sigma_m t=\frac12\operatorname{Var}(h(G)-\lambda G).
\]
The variance cannot vanish for nonzero \(t\): for all integers \(G>m\), the variable in parentheses equals \(-\lambda G\), so constancy forces \(\lambda=0\); then all \(t_r=0\). Hence \(\Sigma_m\) is positive definite.

**3. Inverse and its signs.** Put \(D=\operatorname{diag}(p_1,\ldots,p_m)\), let the \(r\)-th row of \(U\) be \((p_r,rp_r)\), and take \(B=\begin{pmatrix}3&-1\\-1&0\end{pmatrix}\). Then \(\Sigma_m=D+UBU^\top\), and
\[
B^{-1}+U^\top D^{-1}U=
\begin{pmatrix}a_m&-d_m\\-d_m&-e_m\end{pmatrix},
\]
using the three exact truncated geometric sums \(\sum_{r\le m}p_r=a_m\), \(\sum_{r\le m}rp_r=1-d_m\), and \(\sum_{r\le m}r^2p_r=3-e_m\). Woodbury's identity gives the displayed precision formula. For distinct positive indices \(r,s\), the numerator \(a_mrs+d_m(r+s)-e_m\) is minimized at \(\{r,s\}=\{1,2\}\), where it equals
\[
2a_m+3d_m-e_m=1-\frac{m^2+m+2}{2^{m+1}}.
\]
It is zero at \(m=2\), and strictly positive at every \(m\ge3\): the base inequality \(16>14\) at \(m=3\) propagates by induction since \(2(m^2+m+2)\ge(m+1)^2+(m+1)+2\). Since \(\Delta_m>0\), all the precision signs follow.

**4. Limiting partial correlations.** For fixed \(r,s\), \(a_m\to1/2\), \(d_m\to0\), \(e_m\to0\), and \(\Delta_m\to0\). Multiplying the precision formula by \(\Delta_m\) yields
\[
\Delta_m(\Sigma_m^{-1})_{ij}\longrightarrow\frac{ij}{2}
\qquad(i,j\text{ fixed}).
\]
The normalized negative precision ratio therefore tends to \(-1\) for any distinct fixed \(r,s\), as claimed.

## Verification

The accompanying `verify.py` is standalone standard-library Python. It enumerates every cut pattern (every composition) for \(2\le n\le12\), computes exact rational mixed moments, tests the finite covariance formula and strict pairwise signs, verifies the conservation identity \(\sum_r r C_{n,r}=n\), and for \(1\le m\le14\) exactly inverts the rational matrix and checks the rank-two precision formula, identity matrix products and sign classification. It also checks the key scalar inequality for dimensions through \(29\). The run of the included script completed with `VERIFY_OK exact_assertions= 3737`. Enumeration and finite matrix tests corroborate, but do not replace, the symbolic proof for arbitrary integers.

## Relationship to prior work

Bender and Canfield's 2005 paper develops the unrestricted-composition multivariate marking generating function (Example 1) and a general multivariate normal approximation (Theorem 1 and Section 2). These foundational results already encode the part-size joint law and Gaussian covariance; neither the generating function nor the Gaussian limit is claimed as a novel method here. Their 2009 extension treats much broader locally restricted classes. Malandro (arXiv:1108.0337, first submitted August 1, 2011) explicitly develops part-size mean generating functions for bounded compositions, without stating this inverse-covariance sign law. The new, narrower assertion here is the **exact inverse of the limiting covariance matrix, its uniform positive off-diagonal classification, and the approach of all fixed-pair Gaussian partial correlations to \(-1\)**, together with the finite distinct-size sign law as an auxiliary result.

## Limitations

The precision results apply to the limiting Gaussian law for a *fixed* number of observed part sizes, followed by a second limit in that number. They do not assert Gaussian convergence with a dimension growing with the integer being composed. Negative Gaussian partial correlation does not imply conditional negative association of the original discrete part counts. No independent expert review or priority certification is claimed. Explicit part-size marking generating functions have long been available, so a more specialized source not found in the examined literature could already contain this matrix-inversion or sign classification.

## References

- E. A. Bender and E. R. Canfield (2005), *Locally Restricted Compositions I. Restricted Adjacent Differences*, Electronic Journal of Combinatorics 12, R57, https://doi.org/10.37236/1954. First verified publication: 2005-11-07.
- E. A. Bender and E. R. Canfield (2009), *Locally Restricted Compositions II. General Restrictions and Infinite Matrices*, Electronic Journal of Combinatorics 16, R108, https://doi.org/10.37236/197.
- M. E. Malandro (2011), *Integer compositions with part sizes not exceeding \(k\)*, arXiv:1108.0337, https://arxiv.org/abs/1108.0337.
