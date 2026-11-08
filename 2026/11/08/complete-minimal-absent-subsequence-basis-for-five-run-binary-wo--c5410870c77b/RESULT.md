# Complete minimal-absent-subsequence basis for five-run binary words

## Finding

For any five positive integers \(a,b,c,d,e\), define the binary word
\[
W=0^a1^b0^c1^d0^e.
\]
A *minimal absent subsequence* of \(W\) is a nonempty binary word not obtainable by deleting positions from \(W\), every one-letter deletion of which is obtainable that way. Let \(\mathcal M(W)\) denote the set of all such words. The following seven words belong to \(\mathcal M(W)\) unconditionally:
\[
\begin{gathered}
0^{a+c+e+1},\quad 1^{b+d+1},\\
0^{a+c+1}1,\quad 0^{a+1}1^{d+1},\\
1^{b+1}0^{e+1},\quad 10^{c+e+1},\quad 10^{c+1}1.
\end{gathered}
\]
There are exactly six further possible members, each subject to the indicated necessary and sufficient condition:

| Additional minimal absent subsequence | Condition |
|---|---|
| \(101^{d+1}\) | \(b\ge2\) |
| \(0^{a+1}10^{e+1}\) | \(c\ge2\) |
| \(1^{b+1}01\) | \(d\ge2\) |
| \(1010^{e+1}\) | \(b,c\ge2\) |
| \(0^{a+1}101\) | \(c,d\ge2\) |
| \(10101\) | \(b,c,d\ge2\) |

No other minimal absent subsequences exist. With \(x=\mathbf1_{b\ge2}\), \(y=\mathbf1_{c\ge2}\), and \(z=\mathbf1_{d\ge2}\), consequently
\[
\boxed{|\mathcal M(W)|=7+x+y+z+xy+yz+xyz.}
\]
The attainable numbers are exactly \(7,8,9,10,13\); thirteen occurs exactly when all three interior runs have length at least two. In particular, the cardinality is independent of the two outer run lengths.

## Assumptions and scope

All exponents in \(W\) are arbitrary **positive integers**, and the underlying alphabet is exactly \(\{0,1\}\); the occurrence relation is scattered-subsequence containment, **not** contiguous-factor containment. A minimal absent subsequence has all proper subsequences present. It is enough to test the single-letter deletions, since scattered-subsequence containment is transitive. The answer is exact, including boundary cases in which interior run lengths equal one. Every absent binary pattern contains some member of \(\mathcal M(W)\) as a scattered subsequence, because repeatedly deleting symbols from an absent pattern eventually reaches a minimal absent one.

## Proof

For a nonempty binary word, its *run skeleton* is its alternating sequence of symbols after contracting each maximal constant-symbol run. We first obtain the exact presence tests for each possible skeleton by assigning an entire run of the pattern to one or more same-symbol source blocks, always maintaining order. When a pattern has only two or three runs, separated pattern runs can use different compatible pairs of source blocks. In the table, every pattern exponent is positive; juxtaposition of inequalities within each parenthesis means logical conjunction, and \(\lor\) denotes disjunction.

| Pattern | Exact subsequence criterion |
|---|---|
| \(0^i1^j\) | \((i\le a,\ j\le b+d)\lor(i\le a+c,\ j\le d)\) |
| \(1^i0^j\) | \((i\le b,\ j\le c+e)\lor(i\le b+d,\ j\le e)\) |
| \(0^i1^j0^k\) | \((i\le a,j\le b,k\le c+e)\lor(i\le a+c,j\le d,k\le e)\lor(i\le a,j\le b+d,k\le e)\) |
| \(1^i0^j1^k\) | \(i\le b,j\le c,k\le d\) |
| \(0^i1^j0^k1^\ell\) | \(i\le a,j\le b,k\le c,\ell\le d\) |
| \(1^i0^j1^k0^\ell\) | \(i\le b,j\le c,k\le d,\ell\le e\) |
| \(0^i1^j0^k1^\ell0^m\) | \(i\le a,j\le b,k\le c,\ell\le d,m\le e\) |
| \(1^i0^j1^k0^\ell1^m\) | Never |

For example, in the first criterion, either the pattern's initial zero run lies wholly in the first source zero block, allowing its ones to be selected across both source one blocks, or it uses zeros also from the middle zero block, after which only the last source one block remains. All table entries follow by this same order-preserving allocation. The single-symbol criteria are \(0^i\) present iff \(i\le a+c+e\), and \(1^i\) present iff \(i\le b+d\).

For a fixed skeleton, an absent pattern is minimal exactly when **every single-letter deletion** satisfies the appropriate presence criterion. To solve these finite conjunctions, first decrease each exponent greater than one by one: that deletion preserves the skeleton. If an exponent is one, deletion removes its entire run; two neighboring equal-symbol runs then coalesce, so apply the criterion for the resulting shorter skeleton. The calculation produces this complete table, where the numbers refer to the displayed words above:

| Run skeleton | All possible minimal absent subsequences |
|---|---|
| \(0\) | \(0^{a+c+e+1}\) |
| \(1\) | \(1^{b+d+1}\) |
| \(01\) | \(0^{a+c+1}1\), \(0^{a+1}1^{d+1}\) |
| \(10\) | \(1^{b+1}0^{e+1}\), \(10^{c+e+1}\) |
| \(010\) | \(0^{a+1}10^{e+1}\) if \(c\ge2\) |
| \(101\) | \(10^{c+1}1\), \(101^{d+1}\) if \(b\ge2\), \(1^{b+1}01\) if \(d\ge2\) |
| \(0101\) | \(0^{a+1}101\) if \(c,d\ge2\) |
| \(1010\) | \(1010^{e+1}\) if \(b,c\ge2\) |
| \(01010\) | None |
| \(10101\) | \(10101\) if \(b,c,d\ge2\) |

For completeness, several boundary reductions show how to audit the table rather than treating it as an enumeration assertion. For skeleton \(01\), the union of two rectangles has precisely two outside corners all of whose one-coordinate predecessors are inside, namely \((a+c+1,1)\) and \((a+1,d+1)\); these give its two entries. Skeleton \(10\) is analogous. The skeleton \(101\) has one rectangular region, so its three exterior corners are \((1,c+1,1)\), \((1,1,d+1)\), and \((b+1,1,1)\). Deleting the singleton zero in the last two words tests whether \(1^{d+2}\) and \(1^{b+2}\) are subsequences; this gives the conditions \(b\ge2\) and \(d\ge2\), respectively. The three-rectangle expression for skeleton \(010\) leaves just the corner \((a+1,1,e+1)\). Deleting its middle singleton one gives \(0^{a+e+2}\), which is present precisely when \(c\ge2\). The four-run \(0101\) rectangle has one surviving exterior corner, \((a+1,1,1,1)\): deleting its interior singleton one gives \(0^{a+2}1\), requiring \(c\ge2\), and deleting its middle singleton zero gives \(0^{a+1}1^2\), requiring \(d\ge2\). Its other corners still have an absent three-run deletion. The \(1010\) case is the reversed analogue, giving \(b,c\ge2\). No exterior corner of the five-run \(01010\) rectangle survives the deletion of a singleton at the opposite end. The entirely absent \(10101\) has five single-letter deletions; those that remove one of its three interior runs embed precisely when \(b,c,d\ge2\). These comparisons prove both necessity and sufficiency of every table entry.

Finally, any pattern with at least six runs has a five-run \(10101\) subsequence (use five consecutive runs beginning with a \(1\)). Because \(10101\) is always absent from the five-run word \(W\), such a pattern cannot be minimal: removing a symbol outside that proper absent subsequence leaves an absent word. All possible skeletons have therefore been exhausted. The patterns in the table are pairwise distinct, and adding their seven unconditional and six conditional entries yields the stated formula. \(\square\)

## Verification

The self-contained Python 3 script `verify.py` independently builds the entire subsequence downset of \(W\), generates its minimally absent boundary by one-letter insertion, and compares that boundary with the 13-template theorem. Running `python3 verify.py` produces `VERIFICATION_OK`. It exhaustively checks all \(4^5=1024\) positive five-tuples with each run length at most four. A separately seeded set of 220 larger five-tuples checks 116099 one-letter deletion witnesses and 6600 randomly generated pattern-membership equivalences. The finite tests are supporting checks only: the proof above establishes the result for arbitrarily large positive parameters.

## Relationship to prior work

Kosche, Koß, Manea and Siemer developed the general combinatorial and algorithmic theory of shortest and minimal absent **scattered subsequences**; their representation and membership methods apply to individual inputs but do not give the explicit five-run basis or its interior-run threshold formula in the inspected sections. Adamson and collaborators studied absent-subsequence counts by length and universality index, not the fixed-host *minimal* boundary classified here. Later algorithms by Manea and collaborators can enumerate the boundary of general strings but do not provide this symbolic 13-template classification in the material inspected. The special contribution is the complete closed form for a natural run-parameterized family, not the definition of minimal absent subsequences nor general-purpose enumeration.

## Limitations

The theorem is specific to a binary five-run word starting and ending in zero; interchanging the two alphabet symbols gives its immediate dual, but arbitrary numbers of runs are not claimed. The formula concerns the cardinality and membership of the **minimal** absent-subsequence antichain, not the number of all absent subsequences. The general algorithmic theorems may make the specialization computable but do not by themselves exhibit the listed closed form without a case reduction. A related 2023 conference paper was available only at abstract level; its full text could not be checked, so possible overlapping results remain an unresolved literature risk. No independent audit has been performed.

## References

1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first public 2021-08-31), https://arxiv.org/abs/2108.13968 .
2. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (first public 2024-07-26), https://arxiv.org/abs/2407.18599 .
3. F. Manea et al., *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471, https://arxiv.org/abs/2504.21471 .
4. Z. Troníček, *On Problems Related to Absent Subsequences*, COCOA 2023, https://doi.org/10.1007/978-3-031-49614-1_26 (abstract-only comparison).
