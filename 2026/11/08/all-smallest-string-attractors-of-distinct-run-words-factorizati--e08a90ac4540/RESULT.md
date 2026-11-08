# All smallest string attractors of distinct-run words: factorization and a bivariate census

## Finding

Let \(q\ge2\), let \(c_1,\ldots,c_q\) be pairwise distinct symbols, and let \(a_1,\ldots,a_q\) be positive integers. For the *finite, linear* word
\[
W=c_1^{a_1}c_2^{a_2}\cdots c_q^{a_q},
\]
its smallest string-attractor size is exactly \(q\). Every smallest attractor is obtained by choosing one position \(p_i\) in each run, subject precisely to the local conditions
\[
p_i=\operatorname{last}(i)\quad\text{or}\quad p_{i+1}=\operatorname{first}(i+1)\qquad(1\le i<q).
\tag{1}
\]

Partition the indices of runs of length at least two into maximal nonempty consecutive blocks \(B\), separated by singleton runs. The number of smallest attractors is exactly
\[
N(a_1,\ldots,a_q)=\prod_B\left(1+\sum_{i\in B}(a_i-1)\right),
\tag{2}
\]
with empty product equal to \(1\). In particular, if all runs have length at least two, then \(N=a_1+\cdots+a_q-q+1\).

For a fixed ordered alphabet of \(q\) distinct letters, let \(T_{n,q}\) be the sum of these counts over all positive length compositions \((a_1,\ldots,a_q)\) of \(n\). Then
\[
T_{n,q}=\sum_{j=0}^{\min(q-1,n-q)}\binom{q-1}{j}\binom{n-j}{q},
\qquad n\ge q\ge1,
\tag{3}
\]
where the natural one-run extension is \(N(a_1)=a_1\). The univariate and bivariate generating functions are
\[
\sum_{n\ge q}T_{n,q}x^n
=\frac{x^q(1+x)^{q-1}}{(1-x)^{q+1}},
\qquad
\sum_{q\ge1}\sum_{n\ge q}T_{n,q}x^ny^q
=\frac{xy}{(1-x)(1-x-xy-x^2y)}.
\tag{4}
\]
The formulas count labeled positions of attractor sets, not words up to alphabet permutation or cyclic rotation.

## Assumptions and scope

Positions are \(1,\ldots,n\), where \(n=\sum_i a_i\). A string attractor \(\Gamma\) of a finite word \(W\) means that for every nonempty factor \(u\) occurring contiguously in \(W\), at least one occurrence interval of \(u\) contains an element of \(\Gamma\). The alphabet letters \(c_i\) are all distinct, even for nonadjacent runs; each letter occurs in exactly one run. These are ordinary non-circular factors and attractors. The quantity \(T_{n,q}\) sums attractor counts over ordered run-length compositions with fixed symbol order; it does not count alternative permutations of the symbols. No assumption on the numerical sizes of the positive run lengths is made.

## Proof

**1. Sharp minimum.** The factor \(c_i\), a one-letter word appearing only in run \(i\), forces any attractor to meet each of the \(q\) disjoint runs. Thus every attractor has at least \(q\) selected positions. Choose the last position of every run. Each constant-letter factor \(c_i^t\), for \(1\le t\le a_i\), has a suffix occurrence ending at that selected position. Any factor containing more than one distinct letter crosses some run boundary. Its occurrence contains the last position of the run on the left of that boundary. Consequently the selected \(q\) positions form an attractor. This proves the minimum size and the one-position-per-run form of all minimizers.

**2. Exact locality criterion.** In a \(q\)-position selection, the mixed factor \(c_ic_{i+1}\) occurs exactly once: at the boundary between runs \(i\) and \(i+1\). To attract it, the selection must contain either the last position of run \(i\) or the first position of run \(i+1\). This proves the necessity of (1). Conversely, assume (1) holds. Each constant-letter factor has an occurrence through the chosen position in its run: the length-\(t\) intervals within a run cover every position as the interval slides. Any factor containing two or more letters crosses at least one boundary, whose two endpoint positions are both inside that factor's occurrence. By (1) at least one endpoint is chosen, so that factor is attracted. Thus (1) is also sufficient; no other factor imposes additional restrictions.

**3. Factorization and local count.** A singleton run has the same first and last position, so it automatically satisfies both neighboring constraints, independently of their other endpoints. Consequently the allowed choices factor across maximal blocks of non-singleton runs.

For a block of \(t\ge1\) consecutive runs with lengths \(a_i\ge2\), mark each selected run position as \(L\) if it is its last position, \(F\) if it is its first, or \(I\) if it is strictly internal. Each adjacent condition says the left symbol is \(L\) or the right symbol is \(F\). A configuration with no \(I\) therefore has the form \(L^sF^{t-s}\) for a unique \(0\le s\le t\): there are \(t+1\) configurations. A configuration with an internal choice must have exactly one \(I\), say at index \(j\), because all positions to its left must be \(L\) and all to its right must be \(F\); in particular two \(I\)'s cannot occur. The \(j\)th run has \(a_j-2\) internal positions. Hence the block contributes
\[
(t+1)+\sum_{j\in B}(a_j-2)=1+\sum_{j\in B}(a_j-1),
\]
proving (2). Singleton runs each have precisely one choice.

**4. Complete length/run census.** Introduce \(x\) for word length and \(y\) for each run. The class of singletons has weight \(S=xy\). For a positive-length non-singleton block, each run length is at least two. Set
\[
f(x)=\sum_{a\ge2}x^a=\frac{x^2}{1-x},\qquad
g(x)=\sum_{a\ge2}(a-1)x^a=\frac{x^2}{(1-x)^2}.
\]
Using the block weight \(1+\sum(a_i-1)\), the generating function of one block is
\[
B(x,y)=\sum_{t\ge1}\left[y^tf(x)^t+ty^t g(x)f(x)^{t-1}\right]
=\frac{yf(x)}{1-yf(x)}+\frac{yg(x)}{(1-yf(x))^2}.
\]
Any run-length sequence is a sequence of singleton runs and non-singleton blocks, with distinct blocks separated by at least one singleton. Counting the empty sequence as well, its generating function is
\[
1+G(x,y)=\frac{1+B(x,y)}{1-S(1+B(x,y))}.
\]
Direct algebraic simplification gives
\[
G(x,y)=\frac{xy}{(1-x)(1-x-xy-x^2y)}
=\sum_{q\ge1}\frac{x^q(1+x)^{q-1}}{(1-x)^{q+1}}y^q.
\]
Finally, the binomial theorem gives
\[
[x^n]\frac{x^q(1+x)^{q-1}}{(1-x)^{q+1}}
=\sum_{j=0}^{\min(q-1,n-q)}\binom{q-1}{j}\binom{n-j}{q},
\]
proving (3) and (4). For \(q=1\), each selected position of a unary word is an attractor, so \(T_{n,1}=n\), consistent with the generating functions. \(\square\)

## Verification

The accompanying standalone Python 3 script `verify.py` uses an occurrence-by-occurrence factor-attractor test without invoking the theorem. It verifies every one-per-run selection for 339 vectors of run lengths with \(2\le q\le5\), \(1\le a_i\le3\) and total length at most \(12\), totaling 6,786 selections. It then compares the composition sum obtained from (2) with the closed binomial formula for 54 pairs \((n,q)\), \(2\le q\le7\) and \(q\le n\le q+8\). All checks passed. Run with `python3 verify.py`. The proof above, not the finite tests, establishes the infinite-family claims.

## Relationship to prior work

Dvořáková and Hendrychová (arXiv:2308.00850, first publicly submitted on 1 August 2023, MSC 68R15) develop minimum attractors in Rote and generalized pseudostandard binary families. Mantaci et al. (Theoretical Computer Science, 2021) study general combinatorial operations on attractors and provide, for example, a concatenation upper bound; the latter does not give equality, all minimizers or the composition census here. Restivo and collaborators study related infinite-word attractor profiles. Banbara et al. (CPM 2026) explicitly enumerate all smallest attractors for Fibonacci and period-doubling words, illustrating that minimum-attractor multiplicities carry information beyond minimum size; those binary word classes do not imply the present distinct-run formula. The present result concerns arbitrary-length unique-symbol runs in a finite linear word, not binary morphic or circular conjugate words.

## Limitations

The pairwise distinctness of **all** run symbols is essential to the proof: if a symbol occurs in multiple runs, mixed factors need not have a unique occurrence and the singleton-symbol lower bound may change. The formulas do not address circular factors, strings with repeated run symbols, or smallest attractors across different alphabet permutations. They are ordinary same-author mathematical arguments with finite computational cross-checks, not external certification. The literature comparison is non-exhaustive; an earlier equivalent theorem under an unsearched terminology cannot be ruled out.

## References

1. L. Dvořáková and V. Hendrychová, *String attractors of Rote sequences*, arXiv:2308.00850 (first posted 2023-08-01), https://arxiv.org/html/2308.00850v5 .
2. S. Mantaci, A. Restivo, G. Romana, G. Rosone and M. Sciortino, *A Combinatorial View on String Attractors*, Theoretical Computer Science (2021), https://doi.org/10.1016/j.tcs.2020.11.006 . Author-posted full text: https://pages.di.unipi.it/rosone/Papers/MRRRS_TCS2021.pdf .
3. A. Restivo et al., *String Attractors and Infinite Words*, arXiv:2206.00376, https://arxiv.org/abs/2206.00376 .
4. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno and Y. Okamoto, *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.33, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.33 .
