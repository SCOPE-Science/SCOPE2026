# Two sampled equations attain the full greedy Kaczmarz worst-case guarantee on regular-simplex frames

## Finding

Let \(n\ge2\), \(m=n+1\), and let \(u_1,\ldots,u_m\in\mathbb R^n\) be unit vectors satisfying \(\langle u_i,u_j\rangle=-1/n\) for \(i\ne j\). For any error vector \(e\ne0\), draw a uniformly random \(\beta\)-subset \(B\subseteq\{1,\ldots,m\}\) *without replacement*, select an index maximizing \(|\langle u_i,e\rangle|\) over \(i\in B\), and apply the ordinary orthogonal Kaczmarz projection \(e'=e-\langle u_i,e\rangle u_i\). The sharp worst-case expected relative squared-error decrement

\[
\gamma_{n,\beta}=\inf_{e\ne0}\mathbb E_B\frac{\|e\|_2^2-\|e'\|_2^2}{\|e\|_2^2}
\]

is exactly

\[
\boxed{\gamma_{n,\beta}=\begin{cases}
1/n,& n\text{ odd, all }1\le\beta\le n+1,\\
1/n,& n\text{ even and }\beta=1,\\
(n+1)/n^2,& n\text{ even and }2\le\beta\le n+1.
\end{cases}}
\]

Hence two sampled equations already attain the same sharp *one-step worst-case* guarantee as inspecting all \(n+1\) equations. In odd dimensions no sample size improves this sharp guarantee over uniform single-row Kaczmarz. This is not an assertion that the algorithms have identical trajectories, finite-step distributions, or asymptotic expected rates.

## Assumptions and scope

The equations \(\langle u_i,x\rangle=b_i\) are consistent; the error is measured from their unique solution (the simplex rows span \(\mathbb R^n\)). All row norms are one; \(\beta\)-subsets are sampled uniformly without replacement, and the largest squared residual within the sample is chosen. Ties may be resolved arbitrarily. Expectations are conditional on the current deterministic nonzero error. Computation uses exact orthogonal projections, not relaxed, noisy, or block updates.

The simplex exists for each \(n\ge2\): identify \(\mathbb R^n\) with \(\mathbf1^\perp\subset\mathbb R^{n+1}\) and set \(u_i=\sqrt{m/(m-1)}(e_i-\mathbf1/m)\). It obeys \(\sum_i u_i=0\) and \(\sum_i u_i u_i^{\mathsf T}=(m/n)I\).

## Proof

**1. Reduce to a zero-sum sequence.** Set \(z_i=\langle u_i,e\rangle/\|e\|_2\). Then \(\sum_i z_i=0\) and \(S=\sum_i z_i^2=m/n\). Conversely every real zero-sum vector of squared norm \(m/n\) arises this way, because the analysis map of the regular-simplex frame is an isometry up to the factor \(\sqrt{m/n}\). The projection identity gives \(\gamma_{n,\beta}=\inf\mathbb E\max_{i\in B} z_i^2\). Monotonicity in \(\beta\) is immediate by coupling nested uniform subsets.

**2. A sharp odd-cardinality square-dispersion lemma.** If \(m=2k+1\ge3\) and \(z_1,\ldots,z_m\) are real with zero sum, then

\[
D:=\sum_{i<j}|z_i^2-z_j^2|\ge S:=\sum_i z_i^2.
\]

Here is a proof, including the boundary of zero coordinates. Sort \(a_1\le\cdots\le a_m\), the absolute values of the \(z_i\), and put \(t=a_1\), \(\Delta_i=a_{i+1}-a_i\ge0\). Because the nonnegative and nonpositive parts of the zero-sum sequence have equal total absolute mass, and one of their index sets has at most \(k\) elements (zeros may be assigned to either side), the largest \(k\) magnitudes carry at least half the total mass. Thus

\[
\sum_{j=k+2}^{m}a_j\ge\sum_{j=1}^{k+1}a_j,
\quad T:=\sum_{i=1}^{m-1}h_i\Delta_i\ge t,
\]

where \(h_i=i-1\) for \(i\le k+1\) and \(h_i=m-i\) for \(i\ge k+1\). In particular \(0\le h_i\le k\). Direct summation by parts yields

\[
D-S=-m t^2+\sum_{i=1}^{m-1}c_i(a_{i+1}^2-a_i^2),
\qquad c_i=(i-1)(m-i)\ge k h_i.
\]

Since \(a_{i+1}^2-a_i^2=2t\Delta_i+\Delta_i^2+2\Delta_i\sum_{j<i}\Delta_j\), the inequality \(h_j\le k\) implies

\[
\begin{aligned}
\sum_i c_i(a_{i+1}^2-a_i^2)
&\ge 2ktT+k\sum_i h_i\Delta_i^2+2k\sum_{j<i}h_i\Delta_i\Delta_j\\
&\ge 2ktT+\left(\sum_i h_i\Delta_i\right)^2=2ktT+T^2.
\end{aligned}
\]

The second inequality is termwise: \(kh_i\ge h_i^2\) and \(kh_i\ge h_i h_j\). As \(T\ge t\ge0\) and \(m=2k+1\), it follows that \(D-S\ge -mt^2+2ktT+T^2\ge0\). Nothing in the proof assumes nonzero coordinates or distinct magnitudes.

**3. Two-row lower bound for even \(n\).** For a uniformly random pair of distinct indices,

\[
\mathbb E\max(z_i^2,z_j^2)=\frac{S}{m}+\frac{D}{m(m-1)}.
\]

With \(m\) odd, Step 2 implies this is at least \(S/(m-1)=m/[n(m-1)]=(n+1)/n^2\). Every larger sample has at least as large an expected maximum.

**4. Matching extremizer for even \(n\).** With \(n=m-1\) even, take \(z\) proportional to \((1,\ldots,1,-1,\ldots,-1,0)\), with \(n/2\) entries of each sign and one zero, scaled to \(\sum z_i^2=m/n\). Every nonzero squared coordinate equals \(m/n^2\); any subset of size at least two contains a nonzero coordinate, so its maximum is exactly \(m/n^2\). The same construction also shows the full-greedy lower bound cannot be improved. For \(\beta=1\), the tight-frame identity gives the exact constant \(S/m=1/n\) for every error.

**5. Odd \(n\).** When \(n\) is odd, \(m=n+1\) is even. The sample maximum always exceeds or equals the sample average, whose expectation is \(S/m=1/n\). A zero-sum vector with \(m/2\) positive and \(m/2\) negative entries, all of equal magnitude and normalized to \(S=m/n\), makes *every* sampled square equal to \(1/n\). This proves equality for every \(\beta\).

These five steps prove every assertion for all stated dimensions and all admissible sample sizes.

## Verification

The standalone dependency-free `verify.py` performs exact integer/rational checks of the dispersion inequality on zero-sum vectors on bounded grids, the coefficient inequalities for fifty odd cardinalities, and sharp extremizer formulas for dimensions \(2\) through \(23\). Its recorded output is in `verification_output.txt`. The infinite-dimensional-parameter theorem is established by the preceding analytic argument, not by the finite experiments.

## Relationship to prior work

De Loera, Haddock and Needell introduced sampled Motzkin/Kaczmarz selection for linear feasibility; their 2016 preprint gives general projection guarantees. Haddock and Ma's December 2019 preprint (arXiv:1912.03544, especially §§2–4, Theorem 1 and Remarks 2–3) gives one-step and iterated dynamic-range bounds for sampled greedy Kaczmarz on general matrices. Those results imply non-sharp bounds for the unit tight frame and do not state the dimension-parity classification or the fact that two residual evaluations reach the exact full-greedy minimax decrement. General maximal-residual coherence bounds address a different residual-norm performance metric. The exact one-step simplex-frame threshold and odd-cardinality square-dispersion inequality are the contribution here; the underlying Kaczmarz method and regular-simplex frame identities are not new.

## Limitations

Worst-case conditional one-step squared-error contraction is the only optimized performance criterion. It does not establish equality of actual expected multistep convergence, distributional behavior, total work, or noisy/inconsistent feasibility trajectories. The result is for exactly regular-simplex rows, not arbitrary equiangular or nearly tight frames. Earlier equivalent sharp-frame or statistical order-selection inequalities may exist outside the compared literature.

## References

1. J. A. De Loera, J. Haddock, D. Needell, *A Sampling Kaczmarz–Motzkin Algorithm for Linear Feasibility*, arXiv:1605.01418v1 (2016), https://arxiv.org/abs/1605.01418.
2. J. Haddock, A. Ma, *Greed Works: An Improved Analysis of Sampling Kaczmarz–Motzkin*, arXiv:1912.03544v1 (2019), https://arxiv.org/abs/1912.03544; SIAM J. Mathematics of Data Science 3 (2021), DOI:10.1137/19M1307044.
3. Related published numerical residual-spike comparison: *Sharp coherence frontier for residual spikes in maximal-distance Kaczmarz*, published-finding corpus record `2026/9/21/SCOPE-kaczmarz-coherence-residual-spike-frontier--332a15a5d36f` (distinct metric).
