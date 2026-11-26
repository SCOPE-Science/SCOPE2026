# Genus-neutral short-chord deletion and exact parity covariance in random polygon gluings

## Finding

Choose uniformly one of the \((2n-1)!!\) perfect matchings \(\pi\) of \(2n\) cyclically ordered polygon sides, where \(n\ge2\). Glue paired sides with the usual orientation reversal to obtain a closed orientable surface of genus \(G_n\). Write \(S_n\) for the number of matched *cyclically adjacent* side pairs, including the pair straddling the final and initial labels. Such pairs are precisely the one-sided faces in the corresponding one-vertex ribbon graph.

For every integer \(0\le k\le n\) and every bounded function \(h\),

\[
\boxed{\mathbb E[(S_n)_k h(G_n)]
=\frac{2^k(n)_{\underline{k}}}{(2n-1)_{\underline{k}}}\,\mathbb E[h(G_{n-k})].}
\]

Here \((a)_{\underline{k}}=a(a-1)\cdots(a-k+1)\), with value \(1\) at \(k=0\); \(G_0=0\). Equivalently, putting \(P_n(u)=\mathbb E[u^{G_n}]\), the **entire finite bivariate law** is

\[
\mathbb E[t^{S_n}u^{G_n}]=
\sum_{k=0}^{n}\frac{(t-1)^k}{k!}
\frac{2^k(n)_{\underline{k}}}{(2n-1)_{\underline{k}}}P_{n-k}(u).
\]

The exact covariance is strictly negative and has a parity-dependent rational form:

\[
\boxed{\operatorname{Cov}(S_n,G_n)=
\begin{cases}
-\dfrac{n^2}{(2n-1)(n+1)},&n\ \text{even},\\[4pt]
-\dfrac{n-1}{2n-1},&n\ \text{odd}.
\end{cases}}
\]

It converges to \(-1/2\). Nevertheless, with \(W_n=(2G_n-n+\log n)/\sqrt{\log n}\),

\[
(S_n,W_n)\ \Longrightarrow\ (P,Z),
\qquad P\sim\operatorname{Poisson}(1),\quad Z\sim N(0,1),\quad P\perp Z.
\]

## Assumptions and scope

Only uniform perfect matchings of a cyclic polygon with \(2n\) labelled sides are included, with \(n\ge2\). The count is cyclic, **not** the linear-adjacency statistic that omits the wrap-around pair. For the small residual systems used in the identity, define \(G_0=G_1=0\); no convention about \(S_1\) is needed. The genus is that of the orientable surface formed by attaching edge bands to a disc along the matched side pairs and capping all boundary components. All expectations are with respect to the uniform measure. The asymptotic statement takes integer \(n\to\infty\).

## Proof

**Genus-preserving deletion.** Let \(\gamma=(1\,2\,\ldots\,2n)\) and let \(\pi\) be the fixed-point-free involution representing the matching. The number of faces is \(F_n=c(\gamma\pi)\), so Euler's formula gives \(2G_n=n+1-F_n\). If \(\pi\) contains a cyclically adjacent pair, the corresponding element is a fixed point of \(\gamma\pi\). Deleting that pair and relabelling the remaining endpoints cyclically removes exactly one fixed-point cycle and changes neither remaining permutation cycles nor orientable genus. Iteration handles any family of disjoint adjacent pairs, including pairs meeting the cyclic seam. The empty matching has genus zero.

**Exact factorial deletion.** The number of size-\(k\) collections of vertex-disjoint edges of the cycle on \(2n\) labels is

\[
A_{n,k}=\frac{2n}{2n-k}\binom{2n-k}{k}\quad(0\le k\le n).
\]

In particular \(A_{n,n}=2\). For any such collection, the number of perfect matchings containing it is \((2n-2k-1)!!\), and their residual genus has exactly the distribution of \(G_{n-k}\). Counting an ordered choice of \(k\) short chords in every matching, then dividing by \((2n-1)!!\), gives

\[
\mathbb E[(S_n)_k h(G_n)]
=\frac{k! A_{n,k}(2n-2k-1)!!}{(2n-1)!!}\mathbb E[h(G_{n-k})].
\]

Using \((2r-1)!!=(2r)!/(2^r r!)\) simplifies the coefficient to \(2^k(n)_{\underline k}/(2n-1)_{\underline k}\). This also proves the bivariate probability-generating function by \(t^{S_n}=\sum_{k=0}^{S_n}(S_n)_k(t-1)^k/k!\). No asymptotic or independence assumption enters the finite identity.

**Exact genus mean and covariance.** The Harer--Zagier formula in the normalization \(F_n=n+1-2G_n\) is

\[
1+2\sum_{n\ge0}x^{n+1}\mathbb E[y^{F_n}]
=\left(\frac{1+x}{1-x}\right)^y.
\]

Differentiation in \(y\) at \(1\), followed by coefficient extraction from \(\log((1+x)/(1-x))=2\sum_{j\ge1,\ j\ \mathrm{odd}}x^j/j\), yields

\[
\mathbb E F_n=2\sum_{\substack{1\le j\le n\\j\ \mathrm{odd}}}\frac1j
+\frac{\mathbf1_{\{n\ \mathrm{even}\}}}{n+1}.
\]

Consequently,

\[
\mathbb E G_n-\mathbb E G_{n-1}=
\begin{cases}
\dfrac{n}{2(n+1)},&n\ \mathrm{even},\\
\dfrac{n-1}{2n},&n\ \mathrm{odd}.
\end{cases}
\]

Taking \(k=1\) and \(h(g)=g\) in the factorial deletion identity gives \(\mathbb E[S_nG_n]=(2n/(2n-1))\mathbb E G_{n-1}\), while \(\mathbb E S_n=2n/(2n-1)\). Subtraction gives the displayed exact covariance and its \(-1/2\) limit.

**Joint limit.** The classical Harer--Zagier genus local limit theorem (Chmutov--Pittel) gives \((2G_m-m+\log m)/\sqrt{\log m}\Rightarrow N(0,1)\). For each fixed \(k\), replacing \(m=n\) by \(m=n-k\) changes the centering on this scale by \(o(1)\); moreover \(2^k(n)_{\underline k}/(2n-1)_{\underline k}\to1\). For any bounded continuous test function \(f\), factorial deletion therefore yields

\[
\mathbb E[(S_n)_k f(W_n)]\longrightarrow\mathbb E f(Z).
\]

Uniformly in \(n\ge2\), the factorial moment coefficient is at most \(2^k\), since \((n)_{\underline k}\le(2n-1)_{\underline k}\). Thus the expansion for \(\mathbb E[t^{S_n}f(W_n)]\) is dominated by \(\|f\|_\infty\sum_{k\ge0}(2|t-1|)^k/k!\), and for \(0\le t\le1\) tends to \(e^{t-1}\mathbb E f(Z)\). Uniqueness of the probability generating function in the first coordinate, along with weak convergence in the second, gives the asserted independent Poisson--normal limit. This joint statement does not contradict nonvanishing *unscaled* covariance because the genus standard deviation grows like \(\sqrt{\log n}/2\).

## Verification

The standalone \(\texttt{check.py}\) independently enumerates every labelled perfect matching for \(2\le n\le7\), computes genus via cycles of \(\gamma\pi\), and directly counts cyclic adjacent pairs. It compares all genus-by-short-chord table cells with coefficient extraction from the deletion identity, checks the marginal means and parity covariance, and reports **125 passing exact integer/rational assertions**. Enumeration is finite corroboration; the preceding deletion argument, Harer--Zagier identity and limit theorem establish the all-\(n\) statements.

## Relationship to prior work

Paguyo (2021, arXiv:2104.01134) supplies the random-chord-diagram probability setting, normal crossings and Poisson simple-chord results, without a genus-conditioned joint law. Chmutov and Pittel (2011, arXiv:1108.5214) establish the genus local limit theorem and use the classical Harer--Zagier genus polynomial; they explicitly motivate understanding individual face sizes, but do not present the adjacent-pair/genus bivariate identity. Young (2020, arXiv:2004.06921) refines short-chord counts in *linear* chord diagrams without weighting by the orientable genus. The exact genus-neutral factorial deletion gives the coupling between these previously separate local and global measurements. Earlier general degree-refined map enumerations may implicitly contain equivalent expressions; a global priority claim is not established.

## Limitations

The result is confined to uniform orientable polygon gluings. It does not cover arbitrary edge weights, other surface constructions, or all face lengths: adjacent pairs correspond only to one-sided faces. Existing genus normality is used, not reproved, for the joint asymptotic limit. The complete finite bivariate law follows from the classical genus polynomials, so its novelty rests on the joint genus-neutral deletion structure and consequences rather than on a new univariate genus enumeration. Historical priority beyond the inspected primary literature remains uncertain, and no independent scientific audit has been performed.

## References

1. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, first public 2021-04-02, https://arxiv.org/abs/2104.01134.
2. S. Chmutov and B. Pittel, *The genus of a random chord diagram is asymptotically normal*, arXiv:1108.5214, 2011, https://arxiv.org/abs/1108.5214.
3. D. Young, *Linear k-Chord Diagrams*, arXiv:2004.06921, first public 2020-04-15, https://arxiv.org/abs/2004.06921.
4. J. Harer and D. Zagier, *The Euler characteristic of the moduli space of curves*, Invent. Math. 85 (1986), 457--485.
