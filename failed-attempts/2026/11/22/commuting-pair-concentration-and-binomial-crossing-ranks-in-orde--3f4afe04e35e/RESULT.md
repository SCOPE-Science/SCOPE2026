# Commuting-pair concentration and binomial crossing ranks in order-decreasing partial-isometry monoids

## Finding

For each integer \(n\ge1\), let \(M_n\) be the monoid of all order-preserving, order-decreasing partial isometries of the chain \([n]=\{1,\ldots,n\}\), including the empty map. Denote by \(C_n\) the number of ordered commuting pairs in \(M_n^2\). Then

\[
|M_n|=2^{n+1}-n-1,\qquad
\frac{C_n}{|M_n|^2}=\frac14+O(e^{-\sqrt n/4}).
\]

More precisely, the commuting pairs with two idempotent factors number exactly \(4^n\); hence the conditional probability that *both* factors are idempotent, given that they commute, tends to \(1\), with error \(O(e^{-\sqrt n/4})\). For each \(1\le r\le n-1\), the number of ordered commuting pairs with exactly one idempotent factor and with the other factor of map rank \(r\) is exactly

\[
B_{n,r}=2^{n-r+1}\binom{n}{r+1}.
\]

The full crossing count is \(\sum_{r=1}^{n-1}B_{n,r}=4\cdot3^n-(2n+4)2^n\). For \(n\ge2\), conditional on such a crossing pair, the rank of the nonidempotent factor has the distribution \(J-1\), where \(J\) has the \(\mathrm{Bin}(n,1/3)\) law conditioned on \(J\ge2\).

## Assumptions and scope

All maps are partial injections of the finite chain, with semigroup multiplication given by ordinary composition. Map rank is the cardinality of the domain (equivalently, the image). No field or characteristic is involved. The asymptotic variable is the chain size \(n\to\infty\). The \(O\)-constant is absolute and the explicit exponent \(1/4\) is a conservative, not necessarily optimal, decay rate. No complete finite-\(n\) formula for all commuting pairs is asserted.

Every nonempty element of \(M_n\) is uniquely a left translation \(x\mapsto x-k\) on a nonempty subset \(S\subseteq\{k+1,\ldots,n\}\), with \(0\le k\le n-1\). Write this element as \((k,S)\). The unique empty transformation is represented by \((0,\varnothing)\). The idempotents are precisely the partial identities \((0,S)\), one for each subset \(S\subseteq[n]\).

## Proof

**Size and the idempotent core.** The nonempty shift-\(k\) stratum contains \(2^{n-k}-1\) maps. Including the empty map once gives
\[
|M_n|=1+\sum_{k=0}^{n-1}(2^{n-k}-1)=2^{n+1}-n-1.
\]
The \(2^n\) idempotents commute pairwise, supplying exactly \(4^n\) ordered pairs.

**Exact crossing rank polynomial.** Fix a positive shift \(1\le d\le n-1\) and an idempotent \(1_S=(0,S)\). A shifted map \((d,T)\), with \(\varnothing\ne T\subseteq\{d+1,\ldots,n\}\), commutes with \(1_S\) exactly when
\[
 x\in T\implies \mathbf1_S(x)=\mathbf1_S(x-d).
\]
Allow the empty \(T\) temporarily and mark its size by \(z\). The set of positions \([n]\) separates into \(d\) residue-class chains for edges \(x-d\to x\). For a chain of length \(L\), summing over all binary membership labels of \(S\) gives
\[
 \sum_{\text{binary labels}}\prod_{\text{edges}}(1+z\,\mathbf1_{\text{equal endpoints}})
 =2(2+z)^{L-1}.
\]
Indeed the two-state transfer matrix has both row sums \(2+z\), with two initial labels. Multiplying over the \(d\) chains yields \(2^d(2+z)^{n-d}\). For \(r\ge1\), the coefficient of \(z^r\) is \(2^{n-r}\binom{n-d}{r}\). Summing over \(d=1,\ldots,n-1\), using \(\sum_{t=r}^{n-1}\binom tr=\binom n{r+1}\), and doubling for the two factor orders proves the expression for \(B_{n,r}\). Summing its coefficients yields the stated crossing count. The conditioned binomial law follows on substituting \(j=r+1\) into \(\Pr\{\mathrm{Bin}(n,1/3)=j\}=\binom nj2^{n-j}/3^n\).

**Commuting concentration.** Let \(p_n=C_n/|M_n|^2\). For each pair of nonempty translations \((k,S),(l,T)\), commutation is equivalent, for every \(x\in[n]\), to
\[
\mathbf1_S(x)\mathbf1_T(x-k)=\mathbf1_T(x)\mathbf1_S(x-l),
\]
where indicators outside the chain or the respective permissible domains are zero. Fix \(K\ge1\) with \(n>2K+1\), and restrict to shifts \(k,l\le K\), not both zero. Choose indices
\[
x_j=k+l+1+j(K+1)\le n\quad(j=0,1,\ldots,m-1),
\]
where \(m\ge\lfloor(n-2K)/(K+1)\rfloor\). All indicator variables used in distinct selected equations are disjoint. Under independent fair binary choices for *all* permitted membership bits, each selected equation holds with probability \(3/4\) if exactly one shift is zero, and \(5/8\) if both shifts are positive. Thus the number of commuting assignments with those fixed shifts, even allowing empty domains and hence overcounting, is at most
\[
2^{2n-k-l}(3/4)^m.
\]
Sum over the small shifts and divide by \(|M_n|^2\ge4^n\). Their total contribution is at most \(4(3/4)^m\). The proportion of an element having shift greater than \(K\) is at most \(2^{n-K}/|M_n|\le2^{-K}\), so the two-factor tail is at most \(2^{1-K}\). The idempotent-idempotent pairs have already been counted, giving the explicit nonnegative error bound
\[
0\le p_n-\left(\frac{2^n}{2^{n+1}-n-1}\right)^2
\le 4\left(\frac34\right)^{\lfloor(n-2K)/(K+1)\rfloor}+2^{1-K}.
\]
Taking \(K=\lfloor\sqrt n/2\rfloor\) proves the claimed \(O(e^{-\sqrt n/4})\) rate, since the first summand decays faster and \(2^{-K}=O(e^{-(\log2)\sqrt n/2})\). Finally
\[
\left(\frac{2^n}{2^{n+1}-n-1}\right)^2=\frac14+O(n2^{-n}),
\]
so \(p_n=1/4+O(e^{-\sqrt n/4})\). The fraction of commuting pairs with two idempotent factors is \(4^n/C_n\), tending to one with the same error rate.

## Verification

A composition-level implementation enumerates the actual partial maps, rather than the translation-transfer formula, for \(1\le n\le8\). It independently tests their commutators, all \(2^n\) idempotent pairs, the crossing rank coefficients, and the identity \(\sum_S2^{\#\{x>d:\mathbf1_S(x)=\mathbf1_S(x-d)\}}=2^d3^{n-d}\) for every \(1\le d<n\). The checked full commuting-pair totals for \(n=1,\ldots,8\) are \(4,21,102,449,1820,7033,26420,98245\), respectively. Run \(\texttt{python3 checker.py}\) in a directory containing the delivered checker. The program prints \(\texttt{ORDER_DECREASING_PARTIAL_ISOMETRY_COMMUTING_OK}\) when all checks pass. The all-size theorem is established by the preceding proof, not by finite enumeration.

## Relationship to prior work

The motivating paper by Ayık, Ayık and Fernandes determines minimal generators, ideal ranks, and monoid presentations of these order-decreasing partial-isometry monoids, rather than their commuting-pair probabilities or rank-refined idempotent/nonidempotent crossings. Al-Kharousi, Kehinde and Umar previously enumerated several related cardinality statistics and idempotents for the same monoids. Work on *interval-domain* translation rook monoids gives a different asymptotic commuting probability of \(3/10\); interval restrictions change the object and do not imply the \(1/4\) law here. Separate calculations for unconstrained partial translations address product ranks, not commutation or this rank-conditioned crossing law.

## Limitations

The full finite-\(n\) count \(C_n\) is not expressed as a closed formula; only the idempotent core, the exactly-one-idempotent crossing spectrum, and the asymptotic total are determined. The decay bound is not proved optimal. This is an algebraic asymptotic for order-preserving **and** order-decreasing maps only; it is not extended to order-reversing maps or to the full symmetric inverse monoid. Historical novelty remains conditional on indexing and accessibility of older specialist results; no independent verification is claimed.

## References

1. G. Ayık, H. Ayık, V. H. Fernandes, *On semigroups of order-decreasing partial isometries: presentations and ranks of certain ideals*, arXiv:2611.12150v1 (first public 2026-11-09), https://arxiv.org/html/2611.12150v1.
2. F. Al-Kharousi, R. Kehinde, A. Umar, *Combinatorial results for certain semigroups of order-decreasing partial isometries of a finite chain*, arXiv:1702.04485 (2017), https://arxiv.org/abs/1702.04485.
