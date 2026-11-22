# Isolated-run factor avoidance preserves consecutive-window shattering on chains and cycles

## Finding

Let \(r\ge2\) be an integer and write \(m=r+2\). For \(n\ge0\), let \(\mathcal L_{n,r}\subseteq\{0,1\}^n\) be all words having no *contiguous* factor \(0\,1^r\,0\). For \(n\ge m\), let \(\mathcal C_{n,r}\) be all words on the indexed cycle \(\mathbb Z/n\mathbb Z\) having no *cyclic* length-\(m\) factor \(0\,1^r\,0\), including factors crossing the boundary. Concept membership is the bit at each indexed coordinate.

**Theorem (joint path–cycle replacement law).** For either family, a support \(S\) of queried coordinates is VC-shattered if and only if it contains no \(m\) successive coordinates (in the linear or circular order, respectively). Thus forbidding \(0\,1^r\,0\) gives exactly the same shattered supports as forbidding \(1^m\) on the same domain, though the concept families themselves differ.

Let \(B_m(x)=\sum_{j=0}^{m-1}x^j\). The complete face polynomials, counting every labeled shattered support by cardinality, are

\[
\Phi_{n,r}(z)=\sum_{k=0}^{n}\bigl[x^k\bigr]B_m(x)^{n-k+1}z^k,
\qquad
\sum_{n\ge0}\Phi_{n,r}(z)t^n=\frac{B_m(zt)}{1-tB_m(zt)}.
\]

For the cycle (\(n\ge m\)),

\[
\Psi_{n,r}(z)=\sum_{k=0}^{n-1}\frac{n}{n-k}\bigl[x^k\bigr]B_m(x)^{n-k}z^k.
\]

In particular, the dimensions satisfy

\[
\operatorname{VCdim}(\mathcal L_{n,r})=n-\left\lfloor\frac{n}{m}\right\rfloor,
\qquad
\operatorname{VCdim}(\mathcal C_{n,r})=n-\left\lceil\frac{n}{m}\right\rceil\quad(n\ge m).
\]

Hence at every \(n\ge m\) not divisible by \(m\), imposing periodic boundary conditions lowers the maximum shattered rank by precisely one; when \(m\mid n\) the ranks coincide. For \(r=2\), \(n=9\), the line has rank \(7\) but the cycle rank \(6\), and their full polynomials are

\[
\begin{aligned}
\Phi_{9,2}(z)&=1+9z+36z^2+84z^3+120z^4+101z^5+44z^6+6z^7,\\
\Psi_{9,2}(z)&=1+9z+36z^2+84z^3+117z^4+90z^5+30z^6.
\end{aligned}
\]

## Assumptions and scope

The alphabet is binary, positions are labeled, and a query tests a *single coordinate bit*. The forbidden factor is exactly \(0\,1^r\,0\), not a scattered subsequence or a family of factors. Cyclic windows have \(m\) distinct positions because \(n\ge m\); no claim about cyclic words with shorter period or length \(n<m\) is needed. The theorem is stated for \(r\ge2\) because the shorter isolated-one case has a previously catalogued trigram classification. Its proof also works for \(r=1\), but that is not claimed as a new finding. The empty linear word is the unique member of \(\mathcal L_{0,r}\).

## Proof

**Gap characterization.** In a linear binary word, a contiguous factor \(0\,1^r\,0\) occurs exactly when two *consecutive zero positions* have distance \(r+1=m-1\). This is immediate since the \(r\) positions strictly between such zeros are all ones. The identical statement holds for successive zero positions around a cycle with at least two zeros; if a cycle has one zero, its successor is itself at distance \(n\), which is at least \(m\), and hence not a forbidden gap. With no zeros the word is admissible.

**Necessity.** If \(S\) contains an interval of \(m\) successive positions, its labeling on those positions by \(0\,1^r\,0\) cannot be extended to an admissible word. It therefore cannot be shattered.

**Sufficiency, including the circular case.** Suppose that \(S\) contains no complete length-\(m\) interval. Fix an *arbitrary* Boolean labeling on \(S\), and initially set every unqueried coordinate to one. Mark the zero positions of this word. If there is a forbidden gap between two successive zeros, it has length \(m-1\), so its endpoints and its \(r\) interior positions form one length-\(m\) interval. Because this interval is not contained in \(S\), at least one of its interior coordinates is unqueried (the endpoints are labeled zero, hence queried). Change one such interior coordinate from one to zero. The former bad zero gap splits into two strictly shorter positive gaps, neither of which has length \(m-1\). All other consecutive-zero gaps are unchanged. Thus the number of bad gaps decreases by exactly one. Repeat until no bad gap exists. The process terminates after finitely many insertions, changes no queried bit, and yields an admissible word. The same gap-splitting argument works around the circle; the cases of zero or one original zero are already admissible. Since the labeling was arbitrary, \(S\) is shattered.

**Linear face polynomial.** Identify a support with its binary indicator, using one for selected coordinates. If it has \(k\) selected and \(q=n-k\) unselected coordinates, its selected runs in the \(q+1\) gaps between and outside the unselected coordinates have lengths in \(\{0,\ldots,m-1\}\). Therefore there are \([x^k]B_m(x)^{q+1}\) such supports. Summing with weights \(z^k\) gives \(\Phi\). By the unique factorization of a support indicator into a first selected run followed by any number of pairs of one unselected symbol and a selected run, the bivariate generating series is \(B_m(zt)/(1-tB_m(zt))\), as claimed.

**Cyclic face polynomial.** Fix \(k\) selected and \(q=n-k>0\) unselected coordinates. Mark one of the \(q\) unselected coordinates and then record the \(q\) successive selected-run lengths, each from \(0\) to \(m-1\), totaling \(k\). This gives exactly \(n[x^k]B_m(x)^q\) marked labeled supports. Every unmarked support is counted \(q\) times, proving the factor \(n/q\). The all-selected cycle is never shattered for \(n\ge m\), hence \(q\ge1\).

**Dimension.** On a chain of length \(n\), every block of \(m\) successive positions must contain an unselected coordinate. At least \(\lfloor n/m\rfloor\) zeros are needed by disjoint complete blocks; placing a zero at positions \(m,2m,\ldots\) attains this bound. On a cycle the \(q\) unselected coordinates partition the circle into \(q\) gaps, each containing at most \(m-1\) selected positions. Thus \(n\le mq\), implying \(q\ge\lceil n/m\rceil\). Balanced cyclic gaps attain equality. Subtract the minimum zeros from \(n\).

## Verification

The embedded standalone `verify.py` enumerates all legal words and all query supports independently of the gap proof, directly tests every trace, and compares with the stated rank-wise coefficient formulas. It completed 70 linear/circular parameter cases for \(1\le r\le4\) and length at most ten, comprising 16,260 support decisions. The certified scope of this experiment is finite; the all-length assertion follows from the gap-splitting proof above. It also verifies every predicted maximum rank in those finite cases. Reproduce using `python verify.py` with Python 3 and no external packages.

## Relationship to prior work

Johnson's *Binary strings of finite VC dimension* (arXiv:2101.06490, public January 16, 2021) develops string-based VC and mask notions for factors of a *single* word. Here the concept family instead consists of *all* words avoiding a fixed contiguous factor, and the result is coefficient-wise rather than merely a dimension bound. Mészáros and Rónyai (2013) study shattering-extremal families in general; the present theorem supplies an explicit shattering replacement and two boundary-dependent enumerators for a particular regular-language class. Bernardini and collaborators (2021) study constructions with forbidden substrings and prefix/suffix constraints, but their stated algorithmic problems do not give these support polynomials.

A known complete classification of single forbidden binary *trigrams* includes the \(r=1\) isolated-run instance; that instance is explicitly excluded from the novelty claim. A separate indexed result on avoiding both monochromatic trigrams considers a different forbidden language. Counting binary supports with no \(m\) consecutive selected positions is classical; **the new claim is the shattering-preserving identification with the length-\(m\) isolated-run forbidden language, simultaneously for every \(r\ge2\), and its exact cyclic boundary correction**, not the underlying run-composition count in isolation.

## Limitations

No claim is made for multiple simultaneous forbidden factors, for arbitrary palindromic factors, for online/Littlestone dimension, or for a circular word with \(n<m\). The theorem establishes a self-contained combinatorial identity but not absolute publication priority; relevant full texts outside the inspected sources, especially generic results on partial-word completion, may contain an equivalent reduction. The most closely related indexed special-case and two-factor records were compared by their recoverable claims, but a full inspection of the indexed two-factor record was unavailable. Independent validation has not been performed.

## References

1. Hunter R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490, first posted 2021-01-16. https://arxiv.org/html/2101.06490v2
2. Tamás Mészáros and Lajos Rónyai, *Shattering-Extremal Set Systems of Small VC-Dimension*, 2013. https://doi.org/10.1155/2013/126214
3. Giulia Bernardini, Alberto Marchetti-Spaccamela, Solon P. Pissis, Leen Stougie, Michelle Sweering, *Constructing Strings Avoiding Forbidden Substrings*, 2021. https://doi.org/10.4230/LIPIcs.CPM.2021.9
