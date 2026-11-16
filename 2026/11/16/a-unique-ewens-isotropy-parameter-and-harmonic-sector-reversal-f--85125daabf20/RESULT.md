# A unique Ewens isotropy parameter and harmonic-sector reversal for derangement assignments

## Finding

Fix an integer \(n\ge4\) and a real parameter \(\theta>0\). Choose a fixed-point-free permutation \(\Pi\) of \([n]\) with probability proportional to \(\theta^{K(\Pi)}\), where \(K\) counts cycles. Let \(X_{ij}=\mathbf1\{\Pi(i)=j\}\) for \(i\ne j\). Write
\[
 Z_0=1,\quad Z_1=0,\qquad Z_m=(m-1)(Z_{m-1}+\theta Z_{m-2})\quad (m\ge2).
\]
Thus \(Z_m\) is the weighted derangement count, with the parameter \(\theta\) understood. The covariance \(\Sigma_{n,\theta}=\operatorname{Cov}((X_{ij})_{i\ne j})\) has the complete spectrum
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
0&2n-1\\
\lambda_+=\frac1{n-1}+\frac{\theta Z_{n-2}+2\theta Z_{n-3}+2\theta^2 Z_{n-4}}{Z_n}&\frac{n(n-3)}2\\
\lambda_-=\frac1{n-1}+\frac{(2-\theta)Z_{n-2}+2\theta Z_{n-3}}{Z_n}&\frac{(n-1)(n-2)}2.
\end{array}
\]
Both nonzero eigenvalues are strictly positive. The \(\lambda_+\) sector consists of symmetric, zero-diagonal real coefficient matrices with zero row sums; the \(\lambda_-\) sector consists of skew-symmetric matrices with the same zero-margin constraints. The nullspace consists exactly of coefficient arrays \(A_{ij}=u_i+v_j\).

There is exactly one positive parameter \(\theta_n\) at which the nonzero covariance becomes a scalar multiple of the identity on the affine tangent space. Explicitly,
\[
\theta_4=\frac12,\qquad \theta_5=1,
\]
and, for every \(n\ge6\), \(\theta_n\) is the **unique** solution in \((0,1)\) of
\[
1-\theta=\frac{\theta^2Z_{n-4}(\theta)}{Z_{n-2}(\theta)}.
\]
For \(0<\theta<\theta_n\), the skew-symmetric harmonic sector has larger covariance eigenvalue; for \(\theta>\theta_n\), the symmetric sector has larger eigenvalue. At equality the common covariance eigenvalue is
\[
\boxed{\lambda_*(n)=\frac{n(n-2)}{(n-1)(n^2-3n+1)}.}
\]
The unique isotropy tuning has the sharp large-order law
\[
\boxed{1-\theta_n=\frac1{(n-2)(n-3)}+O(n^{-4}),\qquad n\to\infty.}
\]
In particular, \(n^2(1-\theta_n)\to1\). This is an exact finite-dimensional harmonic sampling classification, not a central-limit or approximate isotropy statement.

## Assumptions and scope

The sample space is all derangements on \([n]\), and every such permutation has positive weight because \(\theta>0\). The covariance uses ordinary Euclidean coordinates on the \(n(n-1)\) allowed ordered edges, so its eigenvalues refer to squared \(\ell^2\) analysis energy. A matrix coefficient \(A\) defines the random score \(\sum_i A_{i,\Pi(i)}\). All finite statements hold for every \(n\ge4\) and \(\theta>0\); only the final formula assumes \(n\to\infty\). No conclusion is asserted at \(\theta=0\), where the sampling support changes.

## Proof

**1. Exact weighted counts.** The derangement normalizer is \(Z_m=\sum_{\pi\text{ derangement of }[m]}\theta^{K(\pi)}\). The usual insert-or-pair argument gives the recurrence displayed above: in a derangement on \(m\) labels, either the distinguished label belongs to a two-cycle, weighted by \(\theta(m-1)Z_{m-2}\), or is inserted in a cycle of a derangement on \(m-1\) labels, in \(m-1\) ways without changing its cycle count.

Simultaneous conjugation acts transitively on allowed directed edges, so \(p:=\mathbb E X_{ij}=1/(n-1)\). For two admissible, different edges with different sources and destinations, set \(q_2,q_c,q_d\) for a reciprocal directed two-cycle, a directed chain on three distinct labels, and four distinct labels respectively. The exact joint probabilities are
\[
q_2=\frac{\theta Z_{n-2}}{Z_n},\qquad
q_c=\frac{Z_{n-2}+\theta Z_{n-3}}{Z_n},\qquad
q_d=\frac{Z_{n-2}+2\theta Z_{n-3}+\theta^2Z_{n-4}}{Z_n}.
\]
Indeed, a reciprocal prescribed pair closes a two-cycle, leaving a weighted derangement. A prescribed length-two directed chain contracts to one special symbol in an \((n-2)\)-symbol permutation. The special symbol may be fixed (closing an original three-cycle), whereas all other symbols may not. This adds \(\theta Z_{n-3}\) to \(Z_{n-2}\). Two disjoint prescribed edges contract to two special symbols allowed to be fixed, producing the four terms \(Z_{n-2}\), two copies of \(\theta Z_{n-3}\), and \(\theta^2 Z_{n-4}\). Each contraction preserves the cycle number after accounting for these permitted closures. Pairs sharing a source or target have zero joint probability.

**2. Orthogonal harmonic decomposition.** Let \(U\) be the space of arrays of the form \(A_{ij}=u_i+v_j\) for \(i\ne j\), of dimension \(2n-1\). Such a score is constant. Its orthogonal complement \(W\) consists of zero-diagonal arrays with every row and column sum zero, of dimension \(n^2-3n+1\). The transpose involution splits \(W=W_+\oplus W_-\), with dimensions \(n(n-3)/2\) and \((n-1)(n-2)/2\). The dimensions follow respectively from the rank-\(n\) unsigned complete-graph incidence map and the rank-\((n-1)\) oriented incidence map. These spaces are the symmetric and alternating harmonic sectors for simultaneous label permutation.

Fix \(A\in W\) and an edge \((i,j)\). The coefficients of distinct edges sharing a row or column sum to \(-2A_{ij}\). The reciprocal edge contributes \(A_{ji}\), the two chain classes contribute \(-2A_{ji}\), and the remaining four-distinct-label class contributes \(A_{ij}+A_{ji}\). Subtracting the constant mean-product term, which vanishes against a zero-total-sum \(A\), yields
\[
(\Sigma A)_{ij}=(p+q_d)A_{ij}+(q_2-2q_c+q_d)A_{ji}.
\]
Consequently \(\lambda_+=p+q_2-2q_c+2q_d\) and \(\lambda_-=p-q_2+2q_c\), giving the stated formulas and their multiplicities. Moreover, \(\lambda_+=p+q_2+2(q_d-q_c)>0\), whereas \(\lambda_-=p-q_2+2q_c>0\), since \(0\le q_2\le p\) and \(q_d\ge q_c\). Thus the displayed kernel is complete.

**3. Unique crossing.** Cancellation gives
\[
\lambda_+-\lambda_-=\frac{2}{Z_n}\bigl((\theta-1)Z_{n-2}+\theta^2Z_{n-4}\bigr).
\]
When \(n=4\), \(Z_2=\theta\), \(Z_0=1\), and the only positive zero is \(\theta=1/2\). When \(n=5\), \(Z_1=0\), and the only zero is \(\theta=1\). For \(n\ge6\), introduce \(r_m(\theta)=Z_m/Z_{m-1}\), \(m\ge3\), so that
\[
r_3=2,\qquad r_m=(m-1)\left(1+\frac\theta{r_{m-1}}\right)\quad(m\ge4).
\]
Inductively each \(r_m\) is nondecreasing in \(\theta\) and each \(r_m/\theta\) is strictly decreasing: for the first statement use \(\theta/r_{m-1}\), and for the second use \(r_m/\theta=(m-1)(1/\theta+1/r_{m-1})\). The base case is \(r_3=2\). Hence
\[
\frac{\theta^2Z_{n-4}}{Z_{n-2}}=\frac{\theta^2}{r_{n-2}r_{n-3}}
\]
is strictly increasing on \((0,\infty)\), whereas \(1-\theta\) strictly decreases. At \(\theta\downarrow0\) the left side tends to zero and the right side tends to one; at \(\theta=1\) the left side is positive and the right side zero. A unique crossing in \((0,1)\) follows, with the stated sign reversal.

**4. Equality scale and asymptotics.** Every permutation matrix has exactly \(n\) ones, so for the mean matrix \(C\) with entries \(C_{ij}=1/(n-1)\) off-diagonal,
\[
\operatorname{tr}\Sigma=\mathbb E\|X-C\|_F^2=n-\frac{n}{n-1}=\frac{n(n-2)}{n-1}.
\]
At the unique equality parameter the entire covariance on \(W\) has this trace evenly distributed over its dimension \(n^2-3n+1\), proving \(\lambda_*\).

For \(0<\theta\le1\), the ratio recurrence gives, uniformly, \(r_m=m-1+\theta+O(m^{-1})\) as \(m\to\infty\), because \(r_{m-1}\ge m-2\) and \(r_{m-1}=m-2+O(1)\). The crossing equation implies \(1-\theta_n=O(n^{-2})\). It follows that \(r_{n-2}(\theta_n)=n-2+O(n^{-1})\) and \(r_{n-3}(\theta_n)=n-3+O(n^{-1})\). Substitution in \(1-\theta_n=\theta_n^2/[r_{n-2}r_{n-3}]\) gives the asserted \(O(n^{-4})\) refinement and its sharp coefficient.

## Verification

The included standard-library Python program `check.py` independently enumerates all derangements for \(4\le n\le8\), at each of four rational values of \(\theta\). It checks their weighted normalizers, one-edge and all three distinct feasible pair types, and variance identities on explicit symmetric and skew zero-margin test matrices using exact rational arithmetic. It also checks low-order crossing values and the asymptotic scaling numerically. The executable completed with `PASS: 191 exact weighted-permutation, eigenvalue, root and asymptotic checks`. Finite tests are not the proof of the unrestricted theorem.

## Relationship to prior work

Da Silva, Jamshidpey and Tavaré (2020) establish the conditioned Ewens derangement model and its cycle-count moments. Their formulae for cycle-count moments are already known and not claimed as new here. A published classification of **uniform** derangement assignment-score covariance [2] gives two sectors and isotropy only for \(n=5\) at \(\theta=1\); substituting \(\theta=1\) into the formulas above recovers that result. A distinct published Löwner-ellipsoid result [3] already constructs an isotropic probability mixture of **two conjugacy classes** for every \(n\ge4\). Thus existence of some isotropic distribution is also explicitly prior work. The present claim is the complete **conditioned Ewens one-parameter** spectral law and, especially, the unique positive cycle-fugacity achieving isotropy in that natural full-support statistical family, with its sharp tuning scale and harmonic-sector reversal. Literature on Ewens cycle-count covariance [4] addresses a different observable space. A study of optimal variance for additive cycle statistics [5] likewise does not diagonalize the entrywise assignment-score covariance.

## Limitations

The theorem makes no assertion for non-Ewens class weights or general forbidden-position patterns. The isotropic law is unique only **within this one-parameter Ewens family**, not among all derangement probability measures; a two-class alternative was known previously. The large-\(n\) expansion is for the isotropy parameter, not a uniform-in-\(\theta\) limit of covariance spectra. Pre-existing class-function formulas may permit independent rediscovery of some intermediate identities; priority of the specific Ewens spectral crossing remains provisional pending independent literature review.

## References

[1] P. H. da Silva, A. Jamshidpey and S. Tavaré, *Random derangements and the Ewens Sampling Formula*, arXiv:2006.04840v1, first public 2020-06-08, https://arxiv.org/abs/2006.04840 .

[2] *The complete covariance spectrum of uniform derangement assignment scores*, published mathematical record, 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-the-complete-covariance-spectrum-of-uniform-derangement-assignme--a208797ec285 .

[3] *Exact Löwner ball and two-class isotropic contacts of derangement matching polytopes*, published mathematical record, 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-l-wner-ball-and-two-class-isotropic-contacts-of-derangemen--eeae40a3d5d5 .

[4] *A singular covariance transition for cycle counts in Ewens derangements*, published mathematical record, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-singular-covariance-transition-for-cycle-counts-in-ewens-deran--38e40b444e08 .

[5] Ž. Baronėnas, E. Manstavičius and P. Šapokaitė, *A sharp inequality for the variance with respect to the Ewens Sampling Formula*, arXiv:2003.05975v1, https://arxiv.org/abs/2003.05975 .
