# Cycle-type regression of inversions and a three-support covariance law

## Finding

Let \(\Pi\) be a uniformly random permutation of \(\{1,\ldots,n\}\), \(n\ge3\). Write \(C_j\) for the number of cycles of length \(j\), and \(V=\#\{(a,b):1\le a<b\le n,\ \Pi(a)>\Pi(b)\}\) for the ordinary one-line inversion count. Then the exact conditional expectation given the entire cycle-type vector is

\[
\boxed{\mathbb E[V\mid C_1,\ldots,C_n]
=\frac{n(n-1)}4+\frac{n(1-C_1)}6-\frac{C_1(C_1-1)}{12}+\frac{C_2}{6}.}
\tag{1}
\]

Thus the conditional regression depends on the cycle type only through fixed points and 2-cycles. Its covariance with each cycle-size count is supported on exactly three sizes:

\[
\boxed{\operatorname{Cov}(C_j,V)=
\begin{cases}
-(n+1)/6,&j=1,\\
1/12,&j=2,\\
1/6,&j=n,\\
0,&3\le j<n.
\end{cases}}
\tag{2}
\]

For \(n=3\), the three cases \(j=1,2,n\) are distinct and (2) holds. Summation over all \(j\) recovers \(\operatorname{Cov}(\sum_j C_j,V)=-(2n-1)/12\), but that scalar identity does not specify the cycle-size resolution (2).

## Assumptions and scope

Cycles are disjoint cycles of the one-line permutation \(\Pi\), including singleton cycles. Inversions use the ordinary numerical order of positions and values, not the standard-cycle-word pattern statistic. Conditional expectation in (1) means averaging uniformly over all permutations of the given cycle type; this is the same as averaging a fixed representative over its uniformly random relabelings (conjugates). All statements hold for each integer \(n\ge3\) without asymptotic assumptions.

## Proof

**Step 1: conjugacy-averaged inversion probability.** Fix a permutation \(\pi\) with \(f=C_1(\pi)\) fixed points and \(t=C_2(\pi)\) transpositions. Conjugate \(\pi\) by an independent uniformly random relabeling \(\sigma\). For an unordered original pair \(\{a,b\}\), whether it contributes an inversion to \(\sigma\pi\sigma^{-1}\) is the event that the relative order of \(\sigma(a),\sigma(b)\) is opposite to that of \(\sigma(\pi(a)),\sigma(\pi(b))\). All relative ranks of the distinct labels involved are equally likely.

The inversion probabilities for such an original pair are: \(0\) when both vertices are fixed; \(1/3\) when exactly one vertex is fixed; \(1\) when they form a 2-cycle; \(2/3\) when they are adjacent along a directed cycle of length at least three; and \(1/2\) otherwise. For the three-distinct-label cases, among the six relative orders exactly two (respectively four) reverse the two comparisons. For four distinct labels, exchanging the two image labels pairs opposite outcomes. These cases partition the unordered pairs: the numbers in the four exceptional categories are \(\binom f2\), \(f(n-f)\), \(t\), and \(n-f-2t\), respectively. Consequently, relative to the uniform baseline \(\mu=n(n-1)/4\),

\[
\begin{aligned}
\mathbb E[V\mid \text{cycle type of }\pi]-\mu
&=-\frac12\binom f2-\frac16f(n-f)+\frac12t+\frac16(n-f-2t)\\
&=\frac{n(1-f)}6-\frac{f(f-1)}{12}+\frac t6.
\end{aligned}
\]

This proves (1), including the degenerate all-fixed and single-cycle boundaries.

**Step 2: cycle factorial moments.** For nonnegative integers \(r_1,\ldots,r_n\), direct designation of disjoint labeled cycles yields

\[
\mathbb E\prod_{j=1}^n(C_j)_{r_j}
=\begin{cases}\prod_{j=1}^n j^{-r_j},&\sum_j jr_j\le n,\\0,&\sum_j jr_j>n.\end{cases}
\tag{3}
\]

Here \((x)_r=x(x-1)\cdots(x-r+1)\), \((x)_0=1\). Formula (3) follows by choosing the disjoint supports and cyclic orders of the designated cycles, then permuting the remaining labels. In particular \(\mathbb EC_j=1/j\), \(\mathbb EC_1(C_1)_2=3\) for \(n\ge3\), and \(\mathbb E(C_1)_2=1\).

**Step 3: covariances and all boundaries.** Taking the covariance of (1) with \(C_j\),

\[
\operatorname{Cov}(C_j,V)=-\frac n6\operatorname{Cov}(C_j,C_1)-\frac1{12}\operatorname{Cov}(C_j,(C_1)_2)+\frac16\operatorname{Cov}(C_j,C_2).
\tag{4}
\]

For \(j=1\) and \(n\ge3\), equation (3) gives \(\operatorname{Var}(C_1)=1\), \(\operatorname{Cov}(C_1,(C_1)_2)=2\), and \(\operatorname{Cov}(C_1,C_2)=0\), hence the first line of (2). For \(3\le j\le n-2\), all three covariances on the right of (4) vanish by (3). If \(j=n-1\ge3\), the first covariance remains zero while the other two equal \(-1/(n-1)\) and \(-1/(2(n-1))\), respectively; their contributions cancel exactly. If \(j=n\), the three covariances are \(-1/n\), \(-1/n\), and \(-1/(2n)\), giving \(1/6\).

For \(j=2\) and \(n\ge4\), (3) gives \(\operatorname{Cov}(C_2,C_1)=\operatorname{Cov}(C_2,(C_1)_2)=0\), \(\operatorname{Var}(C_2)=1/2\), yielding \(1/12\). At \(n=3\), \(\operatorname{Cov}(C_2,(C_1)_2)=-1/2\) and \(\operatorname{Var}(C_2)=1/4\), giving \(1/24+1/24=1/12\) as required. This completes the proof.

## Verification

The standalone Python 3 program `verify.py` enumerates each permutation of \(3\) through \(8\) labels and recomputes cycle types, ordinary inversions, conditional class averages, means, and all cycle-size covariances using exact rational arithmetic. It makes 135 exact assertions and passes. The finite enumeration is supplemental; (1)--(4) are proofs for every \(n\ge3\).

Run from the directory containing the files: `python3 verify.py`.

## Relationship to prior work

Gladkich and Peled analyze Mallows-weighted cycle lengths, linking inversion tilt with cycles, but not this exact class-wise inversion regression. Work on the inversion statistic conditional on the number of fixed points determines a coarser conditional mean: conditioning additionally on 2-cycle count is not implied by such a fixed-point conditional expectation alone. A published formula for the covariance of the **total** cycle count with each position-specific inversion indicator, and hence its total covariance with inversion count, does not determine the individual cycle-size covariances or (1). Standard cycle factorial moments are used as prior input; they are not claimed as new.

## Limitations

The result is a first conditional moment and a covariance profile, not the full inversion distribution conditional on cycle type. Originality is assessed relative to the cited and inspected literature; unlocated historical equivalent formulas remain possible. No independent mathematical audit has been performed.

## References

1. A. Gladkich and R. Peled, *On the Cycle Structure of Mallows Permutations*, arXiv:1601.06991 (first submitted 2016-01-26), https://arxiv.org/abs/1601.06991.
2. R. Arratia and S. Tavaré, *Independent Process Approximations for Random Combinatorial Structures*, arXiv:1308.3279 (2013 preprint deposit of earlier work), https://arxiv.org/abs/1308.3279.
3. R. G. Pinsky, *The inversion statistic in derangements and in other permutations with a prescribed number of fixed points*, arXiv:2505.02058 (2025), https://arxiv.org/abs/2505.02058.
4. *Linear inversion-gap profile for cycle count in a uniform random permutation*, published mathematical result (2026), formula for total cycle-count/inversion covariance and positional-gap resolution; no individual cycle-size regression claimed.
