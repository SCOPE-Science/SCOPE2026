# Interval-shaped Buchweitz support for unions of two integer intervals

## Finding

Let \(a,q\ge 1\) and \(b\ge a+2\) be integers, and let \(A=[0,a]\cup[b,b+q]\subset\mathbb Z\), where brackets denote *inclusive integer intervals*. Define the \(n\)-fold sumset \(nA=\{x_1+\cdots+x_n:x_i\in A\}\), the Buchweitz difference
\[
\beta_A(n)=|nA|-(2n-1)(|A|-1),\qquad n\ge2,
\]
and its positive support \(\mathcal B(A)=\{n\ge2:\beta_A(n)>0\}\).

**Theorem.** For every such \(a,q,b\), \(\mathcal B(A)\) is an interval of integers (possibly empty, finite, or unbounded). In fact \(2\notin\mathcal B(A)\), and for every \(n\ge2\) the exact difference is
\[
\beta_A(n)=n(b-2a-q-2)+(a+q+2)
 -\sum_{k=0}^{n-1}\max\bigl\{0,b-1-na+k(a-q)\bigr\}.
\tag{1}
\]
For example, \(A=\{0,1,4,5\}\) has \(\mathcal B(A)=\{3\}\).

## Assumptions and scope

All parameters and sumset indices are integers in the stated ranges. The two blocks have at least two elements each and are disjoint. Translation and reflection preserve the cardinality of every iterated sumset, and thus preserve \(\beta_A\) and \(\mathcal B(A)\). This is a statement about all two-block integer sets of this form, not about arbitrary finite subsets or arbitrary numerical-semigroup gapsets.

## Proof

**1. Exact sumset gaps.** For each \(n\ge2\), choosing exactly \(k\) of the \(n\) summands in the right block produces the full integer interval
\[
I_k=[kb,\ k(b+q)+(n-k)a],\qquad k=0,1,\ldots,n.
\]
Both its left and right endpoints strictly increase with \(k\), since \(b+q-a\ge q+2>0\). The number of omitted integers strictly between consecutive intervals is therefore the positive part of
\[
d_k(n)=(k+1)b-\bigl(k(b+q)+(n-k)a\bigr)-1
=b-1-na+k(a-q),\quad 0\le k<n.
\]
The union spans from \(0\) to \(n(b+q)\). Counting its internal omissions yields
\[
|nA|=n(b+q)+1-\sum_{k=0}^{n-1}\max\{0,d_k(n)\},
\]
proving (1) since \(|A|=a+q+2\). In particular, \(2A\) is a union of at most three intervals, each having respectively \(2a+1\), \(a+q+1\), and \(2q+1\) elements; hence \(|2A|\le3(a+q+1)\) and \(\beta_A(2)\le0\).

**2. Reduce to the larger left block.** Reflection through \(b+q\) swaps the block lengths and transforms the separating coordinate to \(b'=b+q-a\). Thus, without loss of generality, assume \(a\ge q\). Then \(d_k(n)\) increases with \(k\). Put
\[
n_0=\max\bigl\{2,\lceil(b-1)/a\rceil\bigr\}.
\]
For \(2\le n<n_0\), all the \(d_k(n)\) are positive: the intervals \(I_k\) are pairwise separated, and counting their lengths gives
\[
|nA|=(n+1)\bigl(1+n(a+q)/2\bigr),\qquad
\beta_A(n)=(n-2)\bigl((a+q)(n-1)/2-1\bigr).
\tag{2}
\]
In particular \(\beta_A(n)>0\) for every \(3\le n<n_0\).

**3. Concavity after the first overlap.** For \(n\ge n_0\), we have \(d_0(n)\le0\). Reverse the gap indices by writing \(j=n-1-k\), and put \(h=a-q\ge0\), \(c=b-1-a\). Then
\[
d_{n-1-j}(n)=c-q(n-1)-hj.
\]
Since \(d_0(n)\le0\), every term with \(j\ge n\) has nonpositive argument. Therefore the *entire* gap count in (1) becomes
\[
G(n)=\sum_{j=0}^{\infty}\max\{0,c-q(n-1)-hj\}.
\tag{3}
\]
For each fixed \(n\ge n_0\), this sum is finite (indeed it has no nonzero terms with \(j\ge n\)); this also covers \(h=0\). Each summand is the maximum of two affine functions of \(n\), hence convex in \(n\). Taking sums proves that \(G(n)\) is convex on integers \(n\ge n_0\), i.e. its second discrete differences are nonnegative. By (1), \(\beta_A(n)\) is consequently concave there. The positive support of any concave real-valued sequence on an integer interval is an interval: values between two positive entries are at least their positive linear interpolation.

**4. No gap between the two regimes.** If \(n_0\le3\), the region before concavity has no positive indices, because \(\beta_A(2)\le0\), so the preceding paragraph proves the result. Suppose \(n_0\ge4\), write \(t=d_0(n_0-1)\). By minimality, \(t\) is a positive integer, so \(d_0(n_0)=t-a\ge1-a\); also \(d_k(n_0)\ge1-q\) for every \(1\le k<n_0\). Compared with counting all \(I_k\) as disjoint, the loss of cardinality is at most
\[
(a-1)+(n_0-1)(q-1).
\]
Using the disjoint-interval count from (2) as a baseline gives
\[
\begin{aligned}
\beta_A(n_0)&\ge
(n_0-2)\bigl((a+q)(n_0-1)/2-1\bigr)
-(a-1)-(n_0-1)(q-1)\\
&=a\bigl((n_0-1)(n_0-2)/2-1\bigr)
+q(n_0-1)(n_0-4)/2+2>0,
\end{aligned}
\]
where the last inequality uses \(n_0\ge4\) and \(a,q\ge1\). Thus (2) supplies all the positive integers \(3,\ldots,n_0-1\), \(n_0\) itself is positive, and concavity shows that any later positive indices form a contiguous continuation from \(n_0\). In combination with \(\beta_A(2)\le0\), this proves the theorem. \(\square\)

**Eventual behavior.** Once \(n\ge\max\{n_0,1+\lceil(b-1-a)/q\rceil\}\), all adjacent gaps vanish and (1) becomes exactly \(\beta_A(n)=n(b-2a-q-2)+(a+q+2)\), after orienting \(a\ge q\) as above. Consequently, the positive support is unbounded exactly when \(b-2a-q-2\ge0\) in that orientation. Formula (1) decides the finite cases without an asymptotic approximation.

## Verification

Run `python3 verify.py` using Python 3 standard library; the expected stdout is in `verification_output.txt`. The checker compares an independent iterated-bitset definition, direct union-of-interval counting, and formula (1) in 5940 finite instances; checks the positive support through index 81 for 11520 parameter cases; and independently probes the first-overlap positivity boundary in 4940 instances. These checks test the algebra and boundary arithmetic but are **not** the proof for unbounded parameters and indices; the proof is above.

## Relationship to prior work

Eliahou, García-García, Marín-Aragón, and Vigneron-Tenorio introduced this formal \(\mathcal B(A)\) and, in Question 4.1 of their study, asked whether it is always an interval for an arbitrary finite integer set, especially a numerical-semigroup gapset. Their constructions treat particular sets with more than two blocks and prove realizations of various intervals. The present result is an affirmative **two-block subfamily** statement with an exact all-index cardinality formula; it does not settle their unrestricted question. General eventual sumset-cardinality results used in that study do not by themselves settle all-index positive-support connectedness.

## Limitations

The proof requires both blocks to have at least two points and makes no assertion for arbitrary finite unions, singleton blocks, or arbitrary gapsets. The interval-support conclusion does not assert global unimodality of \(\beta_A\). Possible unindexed equivalent results under the terminology of unions of intervals or additive set growth remain an originality risk; the calculation is independently reproducible. No independent audit has been performed.

## References

1. S. Eliahou, J. I. García-García, D. Marín-Aragón, and A. Vigneron-Tenorio, *The Buchweitz Set of a Numerical Semigroup*, arXiv:2011.09187, first publicly posted 18 November 2020, https://arxiv.org/abs/2011.09187 .
2. The same authors, *Bulletin of the Brazilian Mathematical Society*, 54, article 4 (published online 6 December 2022), DOI:10.1007/s00574-022-00322-8, especially §§2–4 and Question 4.1, https://doi.org/10.1007/s00574-022-00322-8 .
