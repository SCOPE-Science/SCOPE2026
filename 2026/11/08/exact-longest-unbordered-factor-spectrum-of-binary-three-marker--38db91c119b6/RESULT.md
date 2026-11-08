# Exact longest-unbordered-factor spectrum of binary three-marker words and its Dirichlet limit law

## Finding
Let \(L(w)\) be the greatest length of a contiguous unbordered factor of a nonempty word \(w\). For every binary word with exactly three occurrences of \(1\), write uniquely
\[
w=0^a1\,0^b1\,0^c1\,0^d,\qquad a,b,c,d\in\mathbb Z_{\ge0}.
\]
Then \(L(w)\) equals the maximum of the following *available* candidate lengths:
\[
\boxed{1+\max(a,b,c,d)},\quad
\begin{array}{ll}
a+b+2 &\text{if }a>b,\\
a+b+c+3 &\text{if }a>c,\\
b+c+2 &\text{if }b\ne c,\\
b+c+d+3 &\text{if }d>b,\\
c+d+2 &\text{if }d>c.
\end{array}
\]
The first candidate is always available; a conditional candidate is omitted when its stated condition fails.

For every \(n\ge5\), writing \(m=\lfloor n/4\rfloor\), the minimum is sharp:
\[
\min_{|w|=n,\ |w|_1=3}L(w)=m+1.
\]
**All** minimizers are exactly the gap quadruples satisfying
\[
b=c=m,\quad 0\le a,d\le m,\quad a+d=n-3-2m.
\]
At lengths \(n=3\) and \(n=4\), the minima are respectively \(1\) and \(3\).

If \(W_n\) is uniform over the \(\binom n3\) binary words with precisely three ones, then \(L(W_n)/n\) converges in distribution to a nonconstant variable \(Z\). For \((A,B,C,D)\sim\mathrm{Dirichlet}(1,1,1,1)\), its explicit representation, apart from null equality sets, is
\[
Z=\begin{cases}
1-\min(A,D),& A>C,\ D>B,\\
1-D,& A>C,\ D<B,\\
1-A,& A<C,\ D>B,\\
B+C,& A<C,\ D<B.
\end{cases}
\]
Its first two moments and variance are exactly
\[
\mathbb EZ=\frac{157}{192},\qquad
\mathbb EZ^2=\frac{3929}{5760},\qquad
\mathrm{Var}(Z)=\frac{2483}{184320}>0.
\]

## Assumptions and scope
A *border* of a nonempty finite word is a nonempty proper prefix equal to a suffix; *unbordered* means that no border exists. A *factor* is a contiguous substring (not a scattered subsequence). Words and factors use the alphabet \(\{0,1\}\), positions are linear rather than cyclic, and the number of ones is exactly three. The maximum includes one-letter factors and excludes the empty factor. Conditional equality cases are covered by the exact finite formula and do not require the limiting-law branch conventions.

## Proof
**Structural border lemma.** A factor with at least two ones which begins with \(0^t1\) (where \(t\ge1\)) and ends in \(1\) is unbordered precisely when \(t\) strictly exceeds the number \(g\) of consecutive zeros immediately before its last \(1\). To prove necessity, if \(t\le g\), its prefix \(0^t1\) is also a proper suffix. For sufficiency, a nonempty border cannot contain zero ones because the factor ends in \(1\). A one-one border would be \(0^t1\) and needs \(t\le g\). A two-one border can occur only when the entire factor has three ones; matching that prefix and suffix forces its two internal gaps to be equal and forces at least \(t\) initial zeros before the second one, implying \(t\le g\), again a contradiction. A proper border cannot contain all three ones because the factor's leading \(0^t\) cannot be reproduced after deleting a positive prefix. The reversed assertion says that a factor beginning with \(1\), ending with \(10^t\), and containing at least two ones is unbordered iff \(t\) strictly exceeds the zeros immediately after the first one.

Every unbordered factor of length greater than one must have *different* endpoint symbols, since identical symbols would themselves form a one-letter border. A factor with one one is therefore of the form \(0^t1\) or \(10^t\), contributing maximum \(1+\max(a,b,c,d)\). A factor with two ones necessarily uses either the first two or the last two consecutive markers. The forward lemma gives candidates \(a+b+2\) (when \(a>b\)) and \(b+c+2\) (when \(b>c\)); its reversal gives \(b+c+2\) (when \(c>b\)) and \(c+d+2\) (when \(d>c\)). A three-one factor has forward candidate \(a+b+c+3\) when \(a>c\), and reversed candidate \(b+c+d+3\) when \(d>b\). Longer initial or terminal zero fragments can only improve an eligible length, so choosing the full available gap gives the stated list, which is both necessary and sufficient.

**Sharp minimum.** Put \(n=4m+r\) with \(0\le r\le3\), and suppose \(n\ge5\). Any minimizer with length at most \(m+1\) must have all four gaps at most \(m\); their deficits from \(m\) total \(3-r\). If \(b\ne c\), the two-marker candidate requires \(b+c\le m-1\), giving \(a+d\ge3m+r-2\) against \(a+d\le2m\). The only boundary case to check beyond the immediately contradictory small cases is \((m,r)=(2,0)\): it forces \(a=d=2\) and \(\{b,c\}=\{0,1\}\), for which a three-marker candidate exceeds \(m+1\). Thus \(b=c=q\). If \(q<m\), the deficit bound gives \(q=m-1\) and \(r\le1\), and the gap sum forces \(a+d=2m+r-1\), so \(a\ge m\) or \(d\ge m\). Accordingly at least one three-marker candidate is available and exceeds \(m+1\). Hence \(q=m\). Conversely, for exactly the displayed minimizers, all inequalities activating the remaining candidates are false, and the longest factor has length \(m+1\). The n=3,4 cases follow by direct consideration of the one and four possible word(s), respectively.

**Limit law and moments.** Uniformly choosing the three marker positions gives uniform nonnegative integer compositions of \(n-3\) into four gaps. The rescaled gap vector converges weakly to the uniform measure on the three-dimensional simplex, i.e. the Dirichlet law indicated above. Dividing the exact candidate lengths by \(n\) and ignoring the measure-zero strict-inequality boundaries gives four cases. When \(A>C\) and \(D>B\), the two available three-marker factors dominate, producing \(\max(1-A,1-D)=1-\min(A,D)\); when just one of those inequalities holds it gives the corresponding \(1-D\) or \(1-A\); otherwise the available two-marker factor of length asymptotic to \(B+C\) dominates every individual gap. Almost-sure continuity of this piecewise limit yields convergence in distribution. Since \(0\le L(W_n)/n\le1\), moments also converge.

For exact moments, partition the simplex into the 24 strict coordinate-order chambers, each of probability \(1/24\). Inside one chamber let the sorted coordinates be \(X_1>\cdots>X_4\), put \(X_5=0\) and \(T_j=j(X_j-X_{j+1})\). The vector \((T_1,T_2,T_3,T_4)\) has the standard uniform Dirichlet law, and \(X_j=\sum_{i=j}^4T_i/i\). In each chamber the indicated piecewise expression for \(Z\) becomes an exact rational linear form \(\sum_i q_iT_i\), with a constant term represented by \(\sum T_i=1\). Thus
\[
\mathbb E(Z\mid\text{chamber})=\frac14\sum_iq_i,\quad
\mathbb E(Z^2\mid\text{chamber})=\frac{(\sum_iq_i)^2+\sum_iq_i^2}{20}.
\]
Enumerating the 24 orderings in rational arithmetic yields \(157/192\) and \(3929/5760\) and hence variance \(2483/184320\). The accompanying standalone checker makes this finite symbolic moment calculation reproducible.

## Verification
The included `VERIFY.py` uses only the Python standard library. Run `python3 VERIFY.py` from the directory containing it. It independently obtains the longest unbordered factor by constructing the prefix-function for every suffix and examining zero-valued border lengths. It checks the all-gap classification for **31,465** three-marker words at all lengths \(3\le n\le30\), verifies every minimizing quadruple at \(5\le n\le64\), and enumerates all 24 Dirichlet chambers using exact rational arithmetic. Successful replay prints `DIRECT_PREFIX_FUNCTION_OK 31465`, `SHARP_MINIMUM_CLASSIFICATION_OK 64` and `EXACT_DIRICHLET_MOMENTS_OK 157/192 3929/5760 2483/184320`. Finite enumeration supports the universal proof but is not a substitute for it.

## Relationship to prior work
Goč–Mousavi–Shallit address unbordered factors of automatic sequences, not finite binary strings conditioned to have exactly three ones. Loptev–Kucherov–Starikovskaya and Cording–Gagie–Knudsen–Kociumaka study expected maximal unbordered-factor length under **unrestricted** random-string models, rather than a fixed sparse content. Kociumaka–Kundu–Mohamed–Pissis supply a general fast longest-unbordered-factor algorithm. Sekizaki–Mieno relate unbordered factors to run-length encoding, a broadly applicable structural reduction, but their statement does not provide this six-candidate gap classification, sharp set of minimizers, or conditional limit moments. General period/border inequalities also do not determine the invariant: the binary word `01001100` has longest unbordered factor length \(6\) yet shortest period \(7\). The formulas above concern a distinct fixed-composition exact-spectrum problem, not a claim of a new unrestricted algorithm or all-words extremal theorem.

## Limitations
The classification is for exactly three ones over a binary alphabet. The limiting Dirichlet law assumes uniform sampling from that fixed-content family; it is not a limit theorem for independent fair letters or arbitrary weights. No explicit elementary probability density for \(Z\) is asserted, and there is no claim that comparable formulas for higher weights follow. Independent mathematical validation has not been performed. Historical priority remains subject to otherwise unindexed equivalent formulations.

## References
- D. Goč, H. Mousavi, J. Shallit, *On the Number of Unbordered Factors*, arXiv:1211.1301 (first posted 2012-11-06), https://arxiv.org/abs/1211.1301.
- A. Loptev, G. Kucherov, T. Starikovskaya, *On Maximal Unbordered Factors*, arXiv:1504.07406 (2015), https://arxiv.org/abs/1504.07406.
- Š. Holub, M. Müller, *Fully Bordered Words*, arXiv:1504.02222 (2015), https://arxiv.org/abs/1504.02222.
- P. H. Cording, T. Gagie, M. B. T. Knudsen, T. Kociumaka, *Maximal Unbordered Factors of Random Strings*, arXiv:1704.04472 (2017), https://arxiv.org/abs/1704.04472.
- T. Kociumaka, R. Kundu, M. Mohamed, S. P. Pissis, *Longest Unbordered Factor in Quasilinear Time*, LIPIcs ISAAC 2018, https://doi.org/10.4230/LIPIcs.ISAAC.2018.70.
- S. Sekizaki, T. Mieno, *Algorithms for Computing Longest Unbordered Factors on Run-Length Encoded Strings*, arXiv:2507.16285 (2025), https://arxiv.org/abs/2507.16285.
- P. Gawrychowski, G. Kucherov, B. G. Sach, T. Starikovskaya, *Computing the Longest Unbordered Substring*, SPIRE 2015, https://doi.org/10.1007/978-3-319-23826-5_24.
