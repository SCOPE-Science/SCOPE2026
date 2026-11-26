# Joint-rank centralizer census for idempotents of finite directed-path weak endomorphism monoids

## Finding

Let \(M_n\) be the monoid of maps \(g:[n]\to[n]\) with \(g(i+1)-g(i)\in\{0,1\}\) for \(1\le i<n\). Let \(E_n\) denote its idempotents. Define the joint-rank polynomial
\[
H_n(u,z)=\sum_{\substack{e\in E_n,\ g\in M_n\\e\circ g=g\circ e}}
u^{|\operatorname{im}(e)|}z^{|\operatorname{im}(g)|}.
\]
Then the complete, coefficientwise identity in formal power series \(\mathbb Z[u,z][[x]]\) is
\[
\boxed{\sum_{n\ge1}H_n(u,z)x^n=
\frac{xuz(1-x-xuz)^2}{(1-x)^2(1-xuz)(1-x(1+z))^2(1-xu(1+z))^2}.}
\]

More strongly, each idempotent is the unique interval clamp \(e_{a,b}(i)=\min\{b,\max\{a,i\}\}\) for some \(1\le a\le b\le n\). Put \(l=a-1\), \(h=b-a+1\), \(r=n-b\), and \(s=1+z\). The full rank enumerator of its centralizer *inside \(M_n\)* is
\[
\boxed{P_{l,h,r}(z)=z\sum_{0\le i\le j<h}
\binom{h-1}{j-i}z^{j-i}
\bigl(1+\mathbf{1}_{\{i=0\}}(s^l-1)\bigr)
\bigl(1+\mathbf{1}_{\{j=h-1\}}(s^r-1)\bigr).}
\]
For \(h\ge2\), the equivalent closed expression is
\[
P_{l,h,r}(z)=z\Big[(h-2+s^l+s^r)s^{h-1}
-(h-1)zs^{h-2}+z^{h-1}(s^l-1)(s^r-1)\Big].
\]
For \(h=1\), the non-singular endpoint expression is \(P_{l,1,r}(z)=zs^{l+r}\). Every coefficient counts commuting maps of precisely the indicated image size, for every \(n\ge1\) and every clamp interval, including singleton intervals and the whole chain.

Setting \(u=z=1\) gives
\[
\sum_{n\ge1}H_n(1,1)x^n=\frac{x}{(1-x)^3(1-2x)^2},
\qquad H_n(1,1)=(4n-12)2^n+\frac{n^2+9n+24}{2}.
\]
The first values for \(n=1,\ldots,9\) are \(1,7,30,102,303,825,2116,5200,12381\). The proportion of pairs in \(E_n\times M_n\) that commute satisfies \(\Pr(eg=ge)\sim32/n^2\).

## Assumptions and scope

Here \([n]=\{1,\ldots,n\}\), \(n\) is an arbitrary positive integer, all maps are total, and composition is ordinary function composition. Weak endomorphisms of the consistently oriented directed path \(1\to2\to\cdots\to n\) are exactly the maps with increments zero or one; equivalently, order-preserving full contractions or order-preserving transformations with interval image. The two rank variables distinguish the idempotent's image size and the commuting partner's image size. The empty path is not included, so the generating series has zero constant coefficient.

## Proof

**1. Idempotents.** The image of every map \(g\in M_n\) is an interval, since adjacent increments are zero or one. If \(e^2=e\) and \(\operatorname{im}(e)=[a,b]\), then every point in this interval is fixed. For \(i<a\), monotonicity gives \(e(i)\le e(a)=a\), while the image condition gives \(e(i)\ge a\), hence \(e(i)=a\). Similarly \(e(i)=b\) for \(i>b\). Conversely each clamp is idempotent and has adjacent increments zero or one. Thus \(E_n=\{e_{a,b}:1\le a\le b\le n\}\), without repetitions.

**2. Exact commutation test.** Fix \(e=e_{a,b}\) and \(g\in M_n\). Commutation at the fixed points \(a,b\) forces \(p=g(a)\), \(q=g(b)\) to lie in \([a,b]\); by monotonicity \(a\le p\le q\le b\). For \(t<a\), the equality \(e(g(t))=g(e(t))=p\) requires \(g(t)=p\) when \(p>a\), since also \(g(t)\le p\). When \(p=a\), it imposes no additional condition beyond \(g(t)\le a\). Symmetrically, for \(t>b\), the right tail is forced constant when \(q<b\), and otherwise is arbitrary subject to the adjacent-step rule. For \(a\le t\le b\), \(e(t)=t\) and \(g(t)\in[p,q]\subseteq[a,b]\), so commutation holds automatically. These conditions are therefore both necessary and sufficient.

**3. Centralizer ranks.** Write \(p=a+i\), \(q=a+j\) with \(0\le i\le j<h\). There are exactly \(\binom{h-1}{j-i}\) internal step strings from \(p\) to \(q\). The left tail, when \(i=0\), has \(l\) independent zero-or-one increments, contributing \(s^l\) to the rank generating polynomial; when \(i>0\), it contributes one. Analogously the right tail contributes \(s^r\) when \(j=h-1\) and one otherwise. No boundary violation is possible: the left tail can decrease at most \(l=a-1\) positions from value \(a\), and the right tail can rise at most \(r=n-b\) positions from value \(b\). Since the image is an interval, \(|\operatorname{im}(g)|=1+\) the total number of rising adjacent steps. Multiplying the independent weights and summing \((i,j)\) gives the boxed formula for \(P_{l,h,r}\).

**4. Closed form.** Put \(s=1+z\). The interior base sum over \(i,j\) (ignoring the special tails) equals
\[
\sum_{k=0}^{h-1}(h-k)\binom{h-1}{k}z^k
=h s^{h-1}-(h-1)zs^{h-2}.
\]
For \(h\ge2\), each of the two special tails contributes the correction \((s^l-1)s^{h-1}\) or \((s^r-1)s^{h-1}\). The simultaneous end-to-end case contributes \((s^l-1)(s^r-1)z^{h-1}\). This yields the stated closed form. If \(h=1\), both tail allowances apply to its sole internal value, giving \(zs^{l+r}\), as claimed.

**5. Bivariate generating function.** All triples \((l,h,r)\) with \(l,r\ge0\), \(h\ge1\) represent precisely one clamp interval in a chain of length \(n=l+h+r\). Set \(w=xu\), \(X=(1-x)^{-1}\), and \(Y=(1-xs)^{-1}\). The baseline interior contributions, the two single-tail corrections, and the double-tail correction respectively sum to
\[
\sum_{n\ge1}H_n(u,z)x^n
=zw\left[
X^2\frac{1-zw}{(1-sw)^2}
+2X(Y-X)\frac1{1-sw}
+(Y-X)^2\frac1{1-zw}
\right].
\]
The identities used here are \(\sum_{h\ge1}w^h\bigl(hs^{h-1}-(h-1)zs^{h-2}\bigr)=w(1-zw)/(1-sw)^2\), \(\sum_{h\ge1}w^hs^{h-1}=w/(1-sw)\), and \(\sum_{h\ge1}w^hz^{h-1}=w/(1-zw)\). Bringing the three rational terms to a common denominator gives exactly the boxed rational function. This calculation is formal, valid over \(\mathbb Z[u,z][[x]]\), including \(n=1\).

**6. Unweighted count and probability.** At \(u=z=1\) the rational function reduces to \(x(1-x)^{-3}(1-2x)^{-2}\). Partial fractions, or direct coefficient extraction, yield the displayed exact \(H_n(1,1)\). Since \(|E_n|=n(n+1)/2\) and \(|M_n|=(n+1)2^{n-2}\) for \(n\ge2\), division yields \(\Pr(eg=ge)\sim32/n^2\). The \(n=1\) case is checked separately and satisfies the formulas.

## Verification

The bundled standalone Python program `check.py` enumerates every total map of the required adjacent-step type, every clamp idempotent, and every pair of actual function compositions for \(1\le n\le9\). It tests **all coefficients** of every individual rank enumerator against the closed combinatorial sum, and compares the aggregated weighted generating function with the rational expression for four independent positive integer evaluations of \((u,z)\) through size nine. It also checks the exact total formula. Execution: `python check.py`. Expected last line: `ALL_EXACT_CHECKS_PASSED`. These finite checks corroborate, but do not replace, the all-\(n\) bijective proof.

## Relationship to prior work

Fernandes and Paulista (first public 2021-12-26) identify these weak path endomorphisms, describe their idempotents and regular elements, and calculate the monoid's size and semigroup rank. Zubairu, Umar, and Aliyu (2022) study rank and combinatorics of order-preserving contractions in an equivalent realization. Fernandes (2024) provides presentations for the order-preserving interval-range monoid. None of these inspected papers presents a rank-refined census of centralizers of its idempotents.

Araújo and Konieczny give general structural criteria for centralizers in the full transformation semigroup; such criteria are broader in ambient maps, but do **not** state the restriction to adjacent-step maps or the displayed closed centralizer and bivariate formulas. Mir and Alali study a different restricted-range transformation setting rather than adjacent-step contractions.

There is a significant **known numerical overlap**: the unweighted sequence \(H_n(1,1)\) coincides with OEIS A045889 with index shifted by one. The OEIS entry already contains its rational generating function \((1-x)^{-3}(1-2x)^{-2}\) as an abstract integer sequence. Thus this work does **not** claim the integer sequence or rational function as a newly discovered sequence. The contribution under review is the exact centralizer interpretation, the individual idempotent-centralizer rank polynomials, and the two-rank generating function. No matching combinatorial centralizer interpretation was found in the inspected OEIS entry.

## Limitations

The claim is restricted to *weak* endomorphisms of consistently oriented finite directed paths, not general digraphs, undirected paths, or unrestricted order-preserving transformations. The result counts commuting pairs with **one idempotent**, not all commuting pairs. It is an exact enumerative theorem, not a classification of the centralizer monoids up to isomorphism. A mathematically equivalent formulation in unindexed transformation-semigroup, contraction, or combinatorial-species literature remains possible. Exhaustive finite checks do not establish the infinite theorem independently of the stated proof. Independent external mathematical assessment has not been performed.

## References

1. V. H. Fernandes and T. Paulista, *On the Rank of Monoids of Endomorphisms of a Finite Directed Path*, arXiv:2112.13427, first public 2021-12-26. https://arxiv.org/abs/2112.13427
2. M. M. Zubairu, A. Umar and M. J. Aliyu, *On the combinatorial and rank properties of certain subsemigroups of full contractions of a finite chain*, arXiv:2205.00438 (2022). https://arxiv.org/abs/2205.00438
3. V. H. Fernandes, *On the monoid of order-preserving transformations of a finite chain whose ranges are intervals*, arXiv:2407.05084 (2024). https://arxiv.org/abs/2407.05084
4. J. Araújo and J. Konieczny, *Centralizers in the Full Transformation Semigroup*, publicly accessible institutional manuscript. https://repositorioaberto.uab.pt/server/api/core/bitstreams/e1505ef6-df71-4791-a964-cd83058b4fc9/content
5. D. J. Mir and A. S. Alali, *On Centralizers of Idempotents with Restricted Range*, *Symmetry* (2024). https://pdfs.semanticscholar.org/418d/e51232cbe6581a876fbcde974ed6e6a8dd67.pdf
6. OEIS Foundation, *A045889: Partial sums of A045618* (entry with closed formula and generating function). https://oeis.org/A045889
