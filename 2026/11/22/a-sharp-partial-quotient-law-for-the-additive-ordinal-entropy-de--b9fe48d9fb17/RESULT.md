# A sharp partial-quotient law for the additive ordinal-entropy defect of rotations

## Finding
Let \(\alpha=[0;a_1,a_2,\ldots]\in(0,1)\) be irrational. For uniform \(x\in[0,1)\), let \(H_n(\alpha)\) denote the Shannon entropy (natural logarithms) of the ordinal permutation sorting
\[\{x\},\{x+\alpha\},\ldots,\{x+(n-1)\alpha\}.\]
Write \(p_k/q_k\) for its regular continued-fraction convergents, with \(q_k<q_{k+1}\) for all sufficiently large \(k\). Define the nonnegative additive entropy defect
\[\Delta_\alpha(n)=\log n-H_n(\alpha),\qquad M_k(\alpha)=\max_{q_k\le n<q_{k+1}}\Delta_\alpha(n).\]
Then
\[\boxed{\sup_{n\ge2}\Delta_\alpha(n)<\infty\quad\Longleftrightarrow\quad\sup_j a_j<\infty.}\]
More precisely, if every partial quotient is at most \(A\), then \(\Delta_\alpha(n)\le\log(3(A+1))\) for every \(n\ge2\). If \(a=a_{k+1}\to\infty\) along any sequence of indices, then
\[\boxed{M_k(\alpha)=\log a+O(\log\log a),\qquad\lim_{a_{k+1}\to\infty}\frac{M_k(\alpha)}{\log a_{k+1}}=1,}\]
where the error estimate has absolute constants and is uniform in the earlier partial quotients. In particular, the entropy deficit can diverge for rotations with irrationality exponent exactly two, even though their ordinal entropy still satisfies \(H_n(\alpha)/\log n\to1\).

## Assumptions and scope
The state is the irrational rotation \(R_\alpha(x)=\{x+\alpha\}\) on \([0,1)\), with its ordinary order of real representatives and Lebesgue-uniform initial point. No nonconsecutive sampling or alternative observation is considered. All \(n\) coordinates are distinct; hence there is no tie convention. All logarithms are natural. The continued-fraction recurrence is \(q_{k+1}=a_{k+1}q_k+q_{k-1}\), with \(q_{-1}=0\), \(q_0=1\). The block maximum is taken for sufficiently large \(k\) to avoid the possible initial repeated denominator. The last asymptotic is along every subsequence with \(a_{k+1}\to\infty\), not for an arbitrary fixed bounded-type rotation.

## Proof
**1. Ordinal entropy equals a gap entropy.** The ordering can change only where one of the real-valued coordinates crosses zero, namely at the \(n\) distinct points \(-j\alpha\bmod1\), \(0\le j<n\). Between successive cuts the ordering is fixed; at each cut a different coordinate becomes the first element of the ordered list. Thus all \(n\) arcs have distinct ordinal permutations. Reflecting these cuts preserves the multiset of arc lengths. If \(g_1,\ldots,g_n\) are the circular gaps of \(\{j\alpha\bmod1:0\le j<n\}\), then
\[H_n=-\sum_{i=1}^{n}g_i\log g_i,\qquad 0\le\Delta_\alpha(n)=\sum_{i=1}^n g_i\log(ng_i).\]
The second quantity is the Kullback--Leibler divergence from the uniform distribution on \(n\) cells.

**2. Universal convergent-block upper bound.** Put \(q=q_k\), \(Q=q_{k+1}\), and \(p=p_k\). The classical convergent inequality \(|\alpha-p/q|<1/(qQ)\) implies that each of the first \(q\) orbit points \(r\alpha\bmod1\), \(0\le r<q\), is within circular distance \(1/Q\) of the regular grid point \(rp/q\bmod1\). Since \(p\) is coprime to \(q\), the largest circular gap among these \(q\) points is at most \(1/q+2/Q\le3/q\). Inserting additional points cannot enlarge a gap. Therefore, whenever \(q\le n<Q\), each ordinal probability is at most \(3/q\), and
\[H_n\ge\log(q/3),\qquad 0\le\Delta_\alpha(n)\le\log(3n/q)\le\log(3Q/q)\le\log(3(a_{k+1}+1)).\tag{1}\]
If \(a_j\le A\) for every \(j\), the same argument covers all \(n\ge2\), by choosing the consecutive denominators surrounding \(n\), and gives the claimed uniform bound.

**3. Clusters created by a large partial quotient.** Suppose \(a=a_{k+1}\ge16\), and take \(b=\lfloor a/\log a\rfloor\ge2\) and \(n=bq<Q\). Let \(\delta=|q\alpha-p|<1/Q\). Write every observation index uniquely as \(r+sq\) with \(0\le r<q\) and \(0\le s<b\). For each fixed \(r\), these \(b\) orbit points lie on a consistently oriented circular arc, spaced at distance \(\delta\), of total length \((b-1)\delta\).

The base points \(r\alpha\bmod1\) are separated by circular gaps of length at least \(1/q-2/Q>(1-2/a)/q\), because they are within \(1/Q\) of a permuted regular \(q\)-grid. Moreover \((b-1)\delta<b/Q\le1/(q\log a)<(1-2/a)/q\) when \(a\ge16\). Hence these \(q\) cluster arcs are pairwise disjoint, even when one crosses zero. The \(n\) resulting circular gaps split into \(q(b-1)\) intracluster gaps, each of length \(\delta\), and exactly \(q\) intercluster gaps. The total mass of the first group is
\[\varepsilon=q(b-1)\delta<\frac{b-1}{a}\le\frac1{\log a}<\frac12.\tag{2}\]

**4. Conditional Shannon bound.** Label a randomly chosen gap by whether it is intracluster or intercluster, assigning probability to each gap equal to its length. Conditional on being intracluster its index is uniform over \(q(b-1)\) gaps; conditional on the other group its entropy is at most \(\log q\). Writing \(h(t)=-t\log t-(1-t)\log(1-t)\), Shannon's chain rule yields
\[H_{bq}\le h(\varepsilon)+\varepsilon\log(q(b-1))+(1-\varepsilon)\log q=\log q+h(\varepsilon)+\varepsilon\log(b-1).\]
Since \(h\) increases on \([0,1/2]\), equation (2) implies the explicit quantitative lower bound
\[\Delta_\alpha(bq)\ge\log b-h(1/\log a)-\frac{\log(b-1)}{\log a}.\tag{3}\]
As \(a\to\infty\), \(\log b=\log a-\log\log a+o(1)\), the binary entropy term tends to zero, and the final term is at most one. Thus
\[M_k\ge\log a-\log\log a-1-o(1).\tag{4}\]
Combining (4) with (1) gives \(M_k=\log a+O(\log\log a)\) with the leading constant one. Every unbounded sequence of positive integer partial quotients has a subsequence tending to infinity, so the defect is unbounded in that case. Together with Step 2, this proves the equivalence.

**5. A critical-exponent illustration.** The irrational with continued fraction \(\alpha=[0;1,2,3,4,\ldots]\) has \(a_j=j\to\infty\). Its denominator recurrence implies \(q_j\ge j!\) and \(q_{j+1}\le(j+2)q_j\); consequently \(\log q_{j+1}/\log q_j\to1\) and the standard convergent formula gives irrationality exponent two. Nevertheless, (4) makes its additive entropy defect unbounded. This separates the theorem from the leading-order \(H_n/\log n\) law.

## Verification
The standalone file `check.py` requires Python 3 and `mpmath`; run `python check.py`. It reconstructs the exact circular cut-pattern correspondence at lengths 2 through 12, checks 703 finite gap-entropy bounds, and explicitly verifies the short-gap cluster counts and the lower entropy-defect inequalities for selected convergents with next partial quotients 73, 100, 1000 and 10000. Arbitrary precision is used for the irrational orbit coordinates, and the code reports finite checks only. The all-irrational quantifiers, classification, and block asymptotic are established by Steps 1--5, not by numerical extrapolation.

## Relationship to prior work
Maga and Szepessy [1] establish generic nonconvergence of normalized permutation entropy and give general zero-rate results for rotations; they do not establish boundedness of this additive defect or its dependence on partial quotients. Goda [2] proves that a one-dimensional Kronecker sequence is quasi-uniform exactly for badly approximable slopes, using Halton's three-gap structure; the upper bound (1) is compatible with this geometric theorem, but its mesh-ratio criterion alone does not give the reverse Shannon-defect implication or the sharp logarithmic growth across a large-partial-quotient block.

A published all-slope analysis [3] gives the complete accumulation interval of \(H_n/\log n\) in terms of irrationality exponent. In particular, it cannot distinguish exponent-two rotations with bounded versus unbounded partial quotients; the present additive criterion and asymptotic do. An exact golden-rotation calculation [4] determines a finite-order Fibonacci entropy-defect profile for one bounded-type frequency, not an all-slope arithmetic dichotomy. Cheng, Ospina, Vinhage and Zhai [5] compute polynomial slow entropy for Sturmian shifts, a different invariant although the same rotation gaps underlie their word frequencies. Three-gap and convergent facts are used as established classical tools; the new statement concerns the probability-weighted Shannon defect across *all* continued-fraction blocks.

## Limitations
The result concerns a specific real-valued, uniform-phase observation of an irrational circle rotation, not an arbitrary conjugate observable, noisy ordinal samples, nonconsecutive time selections, or a positive entropy rate. The quantitative bound in (4) determines the leading coefficient \(1\) of the block maximum but not a complete order-one constant. Historical priority cannot be established by search alone: a prior equivalent additive Shannon-gap characterization under another terminology remains possible. No independent scientific audit has been performed.

## References
[1] Balázs Maga and Sára Szepessy, *The generic behavior of permutation entropy for continuous maps*, arXiv:2611.12789v1, first public 2026-11-09, https://arxiv.org/html/2611.12789.

[2] Takashi Goda, *One-dimensional quasi-uniform Kronecker sequences*, arXiv:2404.16352v1, first public 2024-04-25, https://arxiv.org/abs/2404.16352; open-access full text https://link.springer.com/article/10.1007/s00013-024-02039-0.

[3] *Irrationality exponent and the complete logarithmic ordinal-entropy spectrum of rotations*, published research record, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-irrationality-exponent-and-the-complete-logarithmic-ordinal-entr--e37534938d5c.

[4] *Fibonacci staircase and sharp entropy-defect oscillation for golden-rotation ordinal patterns*, published research record, 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-fibonacci-staircase-and-sharp-entropy-defect-oscillation-for-gol--5bbf3af57625.

[5] Minhua Cheng, Carlos Ospina, Kurt Vinhage, Yibo Zhai, *Slow Entropy and Variational Dynamical Systems*, arXiv:2405.11137v1, first public 2024-05-18, https://arxiv.org/html/2405.11137v1.
