# Exact Pell-step finite-horizon coverage of a golden rotation sampler

## Finding

Let \(\alpha=(\sqrt5-1)/2\) and let \(\theta\in\mathbb R\). Define the finite return-time sampler
\[
F_N=\{n\in\mathbb Z:0\le n<N,\ \{n\alpha+\theta\}\in[0,1/2)\}.
\]
For each integer \(H\ge1\), define the maximal two-translate expansion at lag budget \(H\) by
\[
R_H=\max_{1\le k\le H}\lim_{N\to\infty}\frac{|F_N\cup(F_N+k)|}{|F_N|}.
\]
The limit exists for each lag, and the definition is independent of the phase \(\theta\). Put \(q_0=1\), \(q_1=4\), and \(q_{j+2}=4q_{j+1}+q_j\) for all integers \(j\ge0\). Then for the unique integer \(j\ge0\) satisfying \(q_j\le H<q_{j+1}\),
\[
\boxed{R_H=2-(\sqrt5-2)^{j+1}.}
\]
The maximizing positive lag is uniquely \(k=q_j\). There is a sharp, nonconvergent first-order finite-budget loss:
\[
\boxed{\liminf_{H\to\infty}H(2-R_H)=\frac1{2\sqrt5},\qquad
\limsup_{H\to\infty}H(2-R_H)=\frac{2+\sqrt5}{2\sqrt5}.}
\]
No finite lag achieves the infinite-horizon optimum \(2\), although \(R_H\uparrow2\).

## Assumptions and scope

The ambient group is \(\mathbb Z\). The rotation angle is the **fixed irrational number** \(\alpha=(\sqrt5-1)/2\), the observation window is the half-open semicircle \([0,1/2)\), and the phase is arbitrary. The sampling sets \(F_N\) are truncated to nonnegative times below \(N\). The shift budget restricts positive integer lags \(1\le k\le H\), with the unshifted set always included. All densities are ordinary limits as \(N\to\infty\), not finite-sample equalities. Thus the theorem concerns a natural quantitative finite-translate restriction of a non-Følner expansion invariant, rather than an entropy theorem for the rotation itself.

## Proof

**Circle-cover reduction.** Weyl equidistribution gives \(|F_N|/N\to1/2\). For fixed integer \(k\), the difference between \(|F_N\cup(F_N+k)|\) and the count of times \(0\le n<N\) for which \(\{n\alpha+\theta\}\) lies in \([0,1/2)\cup([0,1/2)+k\alpha)\) is at most \(2k\), from the interval endpoints of the truncated integers. The latter count divided by \(N\) tends to the Lebesgue measure of the union of the two semicircles. Setting \(t=\{k\alpha\}\), the normalized union has exactly the value
\[
L(k)=2-2\left|t-\frac12\right|.
\]
Since \(k\alpha=(k\sqrt5-k)/2\), the doubling of its distance to a half-integer is
\[
2\left|\{k\alpha\}-\frac12\right|=
\min_{\substack{\ell\in\mathbb Z\\\ell-k\text{ odd}}}|k\sqrt5-\ell|.
\]
Therefore \(R_H=2-\min_{1\le k\le H,\ \ell-k\text{ odd}}|k\sqrt5-\ell|\). All minima exist because the lag set is finite and nearest eligible integers exist.

**Exact Pell record vectors.** Write \(u=2+\sqrt5\), \(v=2-\sqrt5=-(\sqrt5-2)\), and \(r=\sqrt5-2\). For \(j\ge0\), set
\[
\ell_j=\frac{u^{j+1}+v^{j+1}}2,\qquad
q_j=\frac{u^{j+1}-v^{j+1}}{2\sqrt5}.
\]
The initial pairs are \((\ell_0,q_0)=(2,1)\) and \((\ell_1,q_1)=(9,4)\). Both coordinates satisfy the integer recurrence \(z_{j+2}=4z_{j+1}+z_j\), so they are integers. The differences \(\ell_j-q_j\) are odd by induction modulo two. Moreover
\[
\ell_j-\sqrt5q_j=v^{j+1},\qquad
|\ell_jq_{j+1}-\ell_{j+1}q_j|=1.
\]
The second identity follows at the initial pair and changes only sign under the recurrence; thus consecutive vectors form a unimodular basis of \(\mathbb Z^2\).

**Global minimality between successive records.** Fix \(j\ge0\) and integers \(0<k<q_{j+1}\), \(\ell\in\mathbb Z\). Unimodularity gives unique integers \(a,b\) such that \((\ell,k)=a(\ell_j,q_j)+b(\ell_{j+1},q_{j+1})\). If \(b\ge1\), then \(a\le-1\), because \(k<q_{j+1}\). If \(b\le-1\), then \(a\ge1\), because \(k>0\). If \(b=0\), then \(a\ge1\). Consequently
\[
|\ell-\sqrt5k|=r^{j+1}|a-rb|\ge r^{j+1},
\]
with equality only when \((a,b)=(1,0)\). Since \(\ell_j-q_j\) is odd, this exact lower bound is attained by the eligible pair \((\ell_j,q_j)\). Thus \(q_j\) is the unique optimal lag for every \(q_j\le H<q_{j+1}\), and the exact formula for \(R_H\) follows.

**Sharp oscillation constants.** The closed form gives \(q_jr^{j+1}\to1/(2\sqrt5)\) and \(q_{j+1}r^{j+1}\to(2+\sqrt5)/(2\sqrt5)\). On each full integer plateau \(q_j\le H<q_{j+1}\), \(H(2-R_H)=Hr^{j+1}\) increases with \(H\). Evaluating at the left endpoint \(q_j\) and the right endpoint \(q_{j+1}-1\) yields the displayed liminf and limsup. Irrationality makes each finite-lag loss strictly positive, completing the proof.

## Verification

The accompanying `verify.py` independently tests the exact Pell identities for nine records, enumerates all optimal lag changes through lag \(5472\), and compares eight finite sampled-set unions with their predicted equidistributed union measures. The checker reports `VERIFY_OK Pell_identities=9 horizon_minimizers=5472 direct_density_tests=8`. These finite checks are corroboration; equidistribution and global uniqueness across arbitrarily large horizons are proved above, not inferred from the computations.

## Relationship to prior work

Carrasco-Vargas, *Averages of sub-additive functions through non-Følner sequences* (arXiv:2611.08408v1, first public 2026-11-05), defines the full supremum of finite-translate growth of sampling sets and connects that constant to entropy scaling. That general theorem does not identify the exact **finite lag-budget maximizers** of the present half-circle golden-rotation sampler. The integer sequence \(1,4,17,72,\ldots\) is classical in approximating \(\sqrt5\), and no priority is claimed for its recurrence or Pell identities. The assessed content is the exact dynamical translation-growth staircase, its unique minimizing lags, and the sharp oscillatory finite-budget limits. General Beatty sumset estimates concern sums of two growing finite Beatty sets rather than this fixed-lag union expansion. Priority outside the inspected sources requires further literature review.

## Limitations

The result is specific to the golden rotation angle, the half-circle window, positive two-translate budgets, and infinite-time density limits. It does not classify arbitrary irrational angles, non-half-circle windows, multiple simultaneous shifts, or finite-time worst-case discrepancies. The rotation itself has zero entropy; any interpretation as a multiplier for positive-entropy systems uses the separate general entropy proportionality principle. Independent mathematical validation has not been performed.

## References

- N. Carrasco-Vargas, *Averages of sub-additive functions through non-Følner sequences*, arXiv:2611.08408v1 (2026-11-05), https://arxiv.org/html/2611.08408v1 .
- J. Pitman, *Sumsets of Finite Beatty Sequences*, Electronic Journal of Combinatorics **8**(2), #R15 (2001), https://doi.org/10.37236/1614 .
