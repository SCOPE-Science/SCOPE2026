# Endpoint-parallel shattering matroids of exact-transition binary words

## Finding
For every pair of integers \(n\ge2\) and \(0\le k\le n-1\), consider the Boolean concept class
\[
\mathcal H_{n,k}=\left\{x\in\{0,1\}^n:\sum_{i=1}^{n-1}\mathbf1[x_i\ne x_{i+1}]=k\right\},
\]
with a membership query at each coordinate \(i\in[n]\). Put \(r=\min\{k+1,n-k\}\). A coordinate support \(S\subseteq[n]\) is VC-shattered by \(\mathcal H_{n,k}\) **if and only if**
\[
|S|\le r\quad\text{and}\quad\{1,n\}\not\subseteq S.
\]
Consequently, the entire shattering complex is the rank-\(r\) truncation of a partition matroid with one nonsingleton parallel class \(\{1,n\}\) and \(n-2\) singleton parallel classes. In particular,
\[
\operatorname{VCdim}(\mathcal H_{n,k})=r,
\quad
\Phi_{n,k}(z)=\sum_{j=0}^{r}\left[\binom nj-\binom{n-2}{j-2}\right]z^j,
\]
with the second binomial interpreted as zero for \(j<2\). The number of maximum-size shattered supports is \(\binom nr-\binom{n-2}{r-2}\).

There is also a quantified adaptive/nonadaptive separation. For \(1\le k<n\),
\[
k\left\lfloor\log_2\left\lfloor\frac{n-1}{k}\right\rfloor\right\rfloor
\le\operatorname{Ldim}(\mathcal H_{n,k})
\le\left\lfloor\log_2\left(2\binom{n-1}{k}\right)\right\rfloor.
\]
In particular, for each fixed integer \(k\ge1\), as \(n\to\infty\),
\[
\operatorname{Ldim}(\mathcal H_{n,k})=k\log_2 n+O_k(1),
\qquad \operatorname{VCdim}(\mathcal H_{n,k})=k+1
\quad\text{for}\quad n\ge2k+1.
\]
The exact value of \(\operatorname{Ldim}\) for arbitrary finite \(n,k\) is **not** asserted.

## Assumptions and scope
Words are indexed by \(1,\ldots,n\); transitions occur only between successive positions, not cyclically. The starting bit is free, and *exactly* \(k\), rather than at most \(k\), transitions are required. A support is shattered when every one of its binary coordinate labelings extends to at least one member of \(\mathcal H_{n,k}\). Littlestone dimension is the largest depth of a complete adaptive binary membership-query tree. All formulas are valid at both boundary values \(k=0\) and \(k=n-1\), except that the online bounds are stated only for \(k\ge1\). At \(k=0\), the two constant words have Littlestone dimension one.

## Proof
**1. An exact completion interval.** Fix \(S=\{i_1<\dots<i_s\}\), with \(s\ge2\) and \(S\) not containing both endpoints. Let \(a_j=i_{j+1}-i_j\ge1\) for \(1\le j<s\) be the distances between queried coordinates and let \(E=(i_1-1)+(n-i_s)\ge1\) be the total number of exterior adjacency edges. A prescribed labeling \(y_1,\ldots,y_s\) determines \(\delta_j=\mathbf1[y_j\ne y_{j+1}]\) and \(d=\sum_j\delta_j\). Within gap \(j\), the possible numbers of transitions are exactly the integers congruent to \(\delta_j\) modulo two in the interval \([\delta_j,a_j]\): toggling a bit an even number of extra times preserves the endpoint values. Exterior edges can carry any total number \(0,1,\ldots,E\) of transitions, since neither exterior endpoint bit is prescribed.

Define \(\epsilon_j=1\) if \(a_j\not\equiv\delta_j\pmod2\), and \(\epsilon_j=0\) otherwise. The maximum possible transition total for this labeling is
\[
M(\delta)=E+\sum_{j=1}^{s-1}(a_j-\epsilon_j)
=(n-1)-\sum_{j=1}^{s-1}\epsilon_j.
\]
The attainable transition totals are **every integer from \(d\) through \(M(\delta)\)**. Indeed, the interior possibilities form an arithmetic progression of step two, while the exterior interval \([0,E]\), with \(E\ge1\), fills every intermediate parity gap. This remains valid when some interior gap has length one.

**2. Necessity and sufficiency.** The labeling alternating at every consecutive queried position has \(d=s-1\), hence shattering requires \(k\ge s-1\). The labeling with \(\delta_j\) chosen opposite to the parity of \(a_j\) has \(\epsilon_j=1\) in every gap; it has maximum possible total \(M=n-s\), hence shattering requires \(k\le n-s\). Conversely, whenever \(s-1\le k\le n-s\), every labeling has \(d\le s-1\le k\) and \(M\ge n-s\ge k\). By the completion interval it is extendible, so the support is shattered.

If \(S\) includes both \(1\) and \(n\), every word in the class satisfies \(x_1\oplus x_n\equiv k\pmod2\), so two endpoint labels cannot be prescribed independently; such an \(S\) is not shattered. Every singleton is shattered because the class is closed under global bit complementation and is nonempty. The empty support is also shattered. Combining these cases gives the claimed criterion with \(r=\min\{k+1,n-k\}\).

**3. Matroid and enumeration.** On the ground set \([n]\), take the partition matroid in which no independent set may contain both elements of \(\{1,n\}\), while every other element occupies its own rank-one block. Truncating this matroid to rank \(r\) gives exactly the shattered supports just characterized. A size-\(j\) support is forbidden only when it contains both endpoints; there are \(\binom{n-2}{j-2}\) such supports. This proves the polynomial, rank, and extremal-support formula. The complex is pure and has the usual matroid exchange property; no claim about a previously unknown general matroid theorem is needed.

**4. Adaptive bounds.** A word is uniquely determined by its first bit and the set of \(k\) transition edges, so \(|\mathcal H_{n,k}|=2\binom{n-1}{k}\). A depth-\(d\) complete shattered mistake tree has \(2^d\) distinct consistent leaf hypotheses, giving the stated upper bound. For the lower bound, partition the first \(k\lfloor(n-1)/k\rfloor\) adjacency edges into \(k\) consecutive blocks of length \(m=\lfloor(n-1)/k\rfloor\). Restrict to words beginning with zero and having exactly one independently placed switch in each block and none outside. In each block, point queries act as threshold queries on the \(m\) possible switch positions, up to a known bit complement depending on block parity. Binary search produces a complete depth-\(\lfloor\log_2 m\rfloor\) tree for each block. Concatenating these trees yields depth \(k\lfloor\log_2 m\rfloor\). For fixed \(k\), the upper and lower bounds both equal \(k\log_2 n+O_k(1)\), while the VC formula eventually equals \(k+1\).

## Verification
The standalone Python file `check_exact_switches.py` directly enumerates all binary words, query supports, and label traces for every \(2\le n\le11\) and every \(0\le k<n\), independently comparing the direct shattering test with the structural condition and coefficient formula. It tests 40,960 supports and also computes exact finite Littlestone dimensions through \(n=9\), checking both analytical bounds. Running `python check_exact_switches.py` prints `EXACT_SWITCH_SHATTERING_PASS`; captured output is in `check_output.txt`. These finite computations corroborate, but do not replace, the unrestricted proof.

## Relationship to prior work
Hunter Johnson's *Binary strings of finite VC dimension* (arXiv:2101.06490) studies shattering arising from translates and substrings of a fixed word, not the coordinate supports shattered by a class of words with exactly a specified number of switches. Ghazi, Golowich, Kumar and Manurangsi (arXiv:2007.03668) establish general closure inequalities for Littlestone dimension; they do not give the all-parameter shattering complex or the endpoint obstruction. Haghtalab, Roughgarden and Shetty (arXiv:2102.08446, Section 3.4) use disjoint independent threshold regions to establish large online dimensions at fixed VC complexity. Thus the **qualitative threshold-tree method is prior art**, rather than a novel technique here. The proposed contribution is the exact all-\(n,k\) shattering criterion, its matroid identification, and complete support-count polynomial for the *exact-transition* family. A claim of exhaustive historical priority would be unwarranted.

## Limitations
The online result provides matching fixed-\(k\) asymptotics, not an exact Littlestone formula for every pair of finite parameters. The class requires binary labels, a linear order with free endpoint labels, and exactly the stated transition count; cyclic or multialphabet variants are not covered. Earlier equivalent statements in the literature under the terminology of sign-change classes, segmented classifiers, or irredundant support systems remain a real priority risk. There is no independent mathematical audit.

## References
1. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668v1, first public July 7, 2020. https://arxiv.org/abs/2007.03668
2. H. R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490v1, first public January 16, 2021. https://arxiv.org/abs/2101.06490
3. N. Haghtalab, T. Roughgarden, A. Shetty, *Smoothed Analysis with Adaptive Adversaries*, arXiv:2102.08446v1, first public February 16, 2021. https://arxiv.org/abs/2102.08446
