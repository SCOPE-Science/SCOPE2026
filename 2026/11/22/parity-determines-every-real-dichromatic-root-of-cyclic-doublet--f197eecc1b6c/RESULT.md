# Parity determines every real dichromatic root of cyclic doublet digraphs

## Finding

For each integer \(r\ge3\), let \(D_r\) be the digraph comprising \(r\) independent two-vertex layers arranged cyclically, with all four arcs directed from each layer to the next. Its dichromatic polynomial, counting colorings by an arbitrary named palette of size \(q\) for which every individual color class induces an acyclic digraph, is

\[
P_{D_r}(q)=q^{2r}-q(2q-1)^r+2^{r-1}q(q-1).
\]

**All-order real-root classification.** If \(r\) is even, the only real zeros are \(0\) and \(1\), both simple. If \(r\) is odd, there are exactly four distinct simple real zeros: \(0\), \(1\), and precisely two negative zeros. No other real zeros occur. In the odd case, writing these negative zeros as \(-t_1\) and \(-t_2\), one has \(0<t_1<\tfrac12<t_2\). In addition \(\vec\chi(D_r)=2\) and the number of named two-color acyclic colorings is \(4^r-2\cdot3^r+2^r\).

## Assumptions and scope

The vertex set is \(\{(i,b):i\in\mathbb Z/r\mathbb Z,\ b\in\{0,1\}\}\). For every \(i\), exactly the arcs \((i,b)\to(i+1,c)\), for all \(b,c\in\{0,1\}\), are present. There are no intralayer arcs or reverse arcs; as \(r\ge3\), this is a loopless oriented simple digraph. A coloring from a named \(q\)-color palette is valid when it has no monochromatic directed cycle. Color classes may be empty and colors are distinguished. The polynomial counts valid maps for each nonnegative integer \(q\), by polynomial interpolation. Every quantifier in the theorem ranges over integer \(r\ge3\); the polynomial's real zeros refer to its extension as a real-variable polynomial, not to an integral palette.

## Proof

**Counting.** Every arc moves one layer forward modulo \(r\), so any directed cycle visits all \(r\) layer indices. Conversely, if a color is represented in each layer, selecting one vertex of that color per layer gives a directed cycle of length \(r\). Thus a coloring is invalid precisely when at least one color appears in every layer. For a fixed color, each layer has \(q^2-(q-1)^2=2q-1\) ordered vertex-colorings containing that color, yielding \((2q-1)^r\) across the graph. Two specified distinct colors both appear in every layer in exactly \(2^r\) assignments, since each layer must use them once in either order. Three specified colors cannot all appear in a two-vertex layer. Inclusion-exclusion gives

\[
q^{2r}-q(2q-1)^r+\binom q2 2^r
=q^{2r}-q(2q-1)^r+2^{r-1}q(q-1).
\]

This proves the polynomial identity for all nonnegative integers \(q\), and therefore identically. At \(q=1\) it vanishes; at \(q=2\) it equals \(4^r-2\cdot3^r+2^r>0\), since both colors may occur and a two-color arrangement avoiding a color in at least one layer exists. The digraph itself has a directed cycle, so the dichromatic number is two.

**Positive real zeros.** Set

\[
F_r(x)=P_{D_r}(x)/x=x^{2r-1}-(2x-1)^r+2^{r-1}(x-1).
\]

The zero at \(x=0\) is simple because \(F_r(0)=-(-1)^r-2^{r-1}<0\), and \(x=1\) is simple because \(F_r(1)=0\) and \(F'_r(1)=2^{r-1}-1>0\). For \(0<x<\tfrac12\), if \(r\) is even, then \(F_r(x)<x^{2r-1}-2^{r-1}(1-x)<0\), as \(x^{2r-1}\le x<1-x\). If \(r\) is odd, then \(x^{2r-1}+(1-2x)^r\le x+(1-2x)=1-x<2^{r-1}(1-x)\), giving \(F_r(x)<0\) as well.

For \(\tfrac12\le x<1\), use \(x^2-(2x-1)=(1-x)^2\) and the difference-of-powers bound

\[
0\le x^{2r}-(2x-1)^r\le r x^{2r-2}(1-x)^2.
\]

Consequently,

\[
\begin{aligned}
x^{2r-1}-(2x-1)^r
&\le(1-x)\bigl[x^{2r-1}+r x^{2r-2}(1-x)\bigr]\\
&\le(1-x)(1+r/2)<2^{r-1}(1-x),
\end{aligned}
\]

where the last strict inequality holds for all integers \(r\ge3\). Hence \(F_r(x)<0\) throughout \(0<x<1\).

For \(x=1+y>1\), direct binomial expansion of \(F_r(1+y)\) gives the first terms

\[
F_r(1+y)=(2^{r-1}-1)y-(r-1)y^2+(r-1)y^3+\sum_{j=4}^{2r-1}c_jy^j,
\]

where each \(c_j\ge0\). Indeed for \(4\le j\le r\), \(c_j=\binom{2r-1}{j}-2^j\binom rj\ge0\): at \(j=3\) the ratio of these binomials is already larger than or equal to \(8\), and its successive multiplicative factors \((2r-1-j)/(r-j)\), for \(j\ge3\), are greater than \(2\) whenever defined. More precisely equality at \(j=3\) gives \(c_3=r-1>0\), while for \(j>r\) there is no subtracted term. Since \(y^2-y\ge-1/4\) for \(y>0\),

\[
F_r(1+y)\ge y\left[2^{r-1}-1+(r-1)(y^2-y)\right]
\ge y\left[2^{r-1}-1-\frac{r-1}{4}\right]>0.
\]

Thus there is no positive real root beyond \(1\).

**Negative real zeros.** Write \(x=-t\) with \(t>0\). For even \(r\),

\[
P_{D_r}(-t)=t\left[t^{2r-1}+(2t+1)^r+2^{r-1}(t+1)\right]>0,
\]

so none exists. For odd \(r\),

\[
P_{D_r}(-t)=t H_r(t),\qquad
H_r(t)=t^{2r-1}-(2t+1)^r+2^{r-1}(t+1).
\]

Here \(H_r(0)=2^{r-1}-1>0\), while \(H_r(1/2)=2^{-(2r-1)}-2^{r-2}<0\), and \(H_r(t)\to+\infty\) as \(t\to\infty\). Thus one positive root lies below \(1/2\) and another above it. In descending powers of \(t\), the coefficients of \(H_r\) have exactly two sign variations: the leading term is positive; the coefficients of degrees \(r,r-1,\ldots,2\) are strictly negative; the linear term has either sign or vanishes; and the constant \(2^{r-1}-1\) is positive. Descartes' rule of signs bounds the number of positive roots counted with multiplicity by two, so these two roots are the only ones and each is simple. Mapping back by \(x=-t\) yields exactly the claimed two simple negative roots for odd \(r\). Together with the positive and zero cases this proves the classification.

## Verification

The accompanying standalone `verify.py` explicitly builds each digraph, enumerates color maps, and independently tests for monochromatic directed cycles via topological sorting. It matches the polynomial for \(13\) finite instances with \(3\le r\le6\) and palettes \(1\le q\le4\) where feasible. It also performs exact integer checks of the binomial expansion and Descartes sign variations for \(3\le r\le80\). The observed terminal output is `VERIFY_OK cases= 13`. These are reproducibility cross-checks, not replacements for the all-order argument given above. Run with `python3 verify.py` (standard library only).

## Relationship to prior work

Crew, Keller, Kuehr, Lin, Monroy Rodríguez and Williams (2026) study general dichromatic-polynomial coefficients and real-root density. Their source includes a general recursion, which could be applied to this family, but the inspected sections do not state the exact cyclic-doublet enumerator or an all-order parity dichotomy for *every* real root. Hochstättler and Wiehe (2019) give structural representations of digraph chromatic polynomials; these do not themselves provide this graph-specific real-zero classification. Akbari and coauthors (2017) study dichromatic polynomials and coefficient properties, not this infinite oriented doublet family. Earlier literature on majority-stable sets of cyclic blowups deals with a distinct coloring restriction, and prior sink-polynomial root results treat a distinct generating polynomial. Exact historical priority cannot be certified from available indices; the 2022 journal study by González-Moreno and coauthors was accessible in abstract only and remains a source of residual uncertainty.

## Limitations

The theorem concerns exactly two independent vertices in each cyclic layer, for \(r\ge3\); it does not claim the same real-root pattern for larger or unequal layer sizes, for orientations containing digons, or for ordinary chromatic, acyclic-sink, or majority-stable-set polynomials. The two negative roots are uniquely characterized but no explicit radical formula or asymptotic estimates are proved. Historical priority and independent assessment remain open. Finite code verification does not certify infinitely many parameters.

## References

- L. Crew, B. Keller, K. Kuehr, S. Y. Lin, M. I. Monroy Rodríguez, T. Williams, *Properties of the Dichromatic Polynomial*, arXiv:2611.13273v1, first posted 2026-11-09, https://arxiv.org/abs/2611.13273.
- W. Hochstättler and J. Wiehe, *The Chromatic Polynomial of a Digraph*, arXiv:1911.09547, https://arxiv.org/abs/1911.09547.
- S. Akbari et al., *Chromatic Number and Dichromatic Polynomial of Digraphs*, arXiv:1711.06293, https://arxiv.org/abs/1711.06293.
- D. González-Moreno et al., *The Dichromatic Polynomial of a Digraph*, *Graphs and Combinatorics* 38 (2022), article 85, https://doi.org/10.1007/s00373-022-02484-0. Only its abstract was accessible in this review.
