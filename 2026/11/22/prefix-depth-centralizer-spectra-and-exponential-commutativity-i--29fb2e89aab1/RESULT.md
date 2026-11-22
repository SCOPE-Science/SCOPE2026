# Prefix-depth centralizer spectra and exponential commutativity in finite polycyclic inverse monoids

## Finding
Fix an integer \(r\ge 2\), an \(r\)-letter alphabet \(A\), and an integer \(N\ge0\). In the polycyclic inverse monoid \(P_r\), write its nonzero elements uniquely as \(uv^{-1}\), for \(u,v\in A^*\). Define the finite, inverse-closed degree-zero truncation
\[
S_{r,N}=\{0\}\cup\{uv^{-1}:\ |u|=|v|\le N\}.
\]
It is an inverse submonoid, of order \(B_{r,N}=1+\sum_{j=0}^N r^{2j}\). For a nonzero element \(x=uv^{-1}\), let \(m=|u|=|v|\) and \(d=\operatorname{lcp}(u,v)\), the length of the longest common prefix. Its centralizer cardinality in \(S_{r,N}\) is exactly
\[
Z_{r,N}(m,d)=1+\sum_{j=0}^{m}\left((r^j-1)^2+\mathbf{1}_{j\le d}\right)+\sum_{j=m+1}^{N}\left(r^{2j}-2r^{2j-m}+(1+\mathbf{1}_{d=m})r^{2(j-m)}\right).
\]
The zero element has centralizer size \(B_{r,N}\). For each \(0\le m\le N\), the centralizer size \(Z_{r,N}(m,d)\) occurs with a *parameter multiplicity* of \(r^m\) when \(d=m\), and of \((r-1)r^{2m-d-1}\) when \(0\le d<m\). If numerical sizes coincide across distinct \((m,d)\), add their multiplicities. Thus the formula specifies the entire centralizer-size multiset.

For fixed levels \(m,n\), put \(h=\max(m,n)\) and \(\ell=\min(m,n)\). The exact number of ordered commuting pairs \((x,y)\) with \(x\ne0\), \(y\ne0\), and these respective levels is
\[
C_r(m,n)=r^{2h}(r^{\ell}-1)^2+r^{2h-\ell}.
\]
The full ordered commuting-pair count is
\[
K_{r,N}=2B_{r,N}-1+\sum_{m=0}^{N} C_r(m,m)+2\sum_{0\le m<n\le N}C_r(m,n).
\]
Consequently, for independent uniform \(X,Y\in S_{r,N}\), at every fixed \(r\ge2\),
\[
\Pr(XY=YX)=1-\frac{2(r-1)(r+1)^3}{r(r^3-1)}r^{-N}+o(r^{-N})\quad(N\to\infty).
\]
In particular, the commuting probability tends to one, and its noncommuting deficit has an explicit, strictly positive sharp first-order coefficient.

## Assumptions and scope
All statements concern ordinary associative multiplication and equality in the finite inverse submonoid \(S_{r,N}\), **not** commuting in a quotient or in its orthogonal completion. The degree-zero restriction \(|u|=|v|\) and depth cutoff \(N\) are both essential to the finite object. The alphabet size \(r\) is any integer at least two; the length cutoff \(N\) may be zero. The empty word is admitted, and the element \(\varepsilon\varepsilon^{-1}\) is the identity. The longest-common-prefix length is in \(\{0,\ldots,m\}\). Every sum with an empty index range is zero.

We use the standard polycyclic multiplication: for \(uv^{-1}\) and \(st^{-1}\), the product is zero if \(v,s\) are not prefix-comparable; if \(s=vw\), the product is \((uw)t^{-1}\); if \(v=sw\), it is \(u(tw)^{-1}\). When the two cases overlap (equal words), they agree. This shows directly that products of balanced pairs have equal resulting word lengths, at most the larger input level; inverses swap \(u\) and \(v\). Hence the stated finite set is an inverse submonoid.

## Proof
**1. Commutation at a fixed element and shorter level.** Fix \(x=uv^{-1}\) at level \(m\), and consider \(y=st^{-1}\) at level \(j\le m\). Since \(|s|=|t|=j\), the product \(xy\) is nonzero precisely when \(s\) is the length-\(j\) prefix of \(v\), while \(yx\) is nonzero precisely when \(t\) is the length-\(j\) prefix of \(u\). There are \(r^j\) pairs in each event and one in the intersection, so exactly \((r^j-1)^2\) pairs make *both* products zero and therefore commute. For the unique pair for which both products are nonzero, the product normal forms are equal precisely when the length-\(j\) prefixes of \(u\) and \(v\) agree, or equivalently \(j\le d\). All remaining pairs have exactly one nonzero product and do not commute. This proves the summand at levels \(j\le m\).

**2. Commutation at a longer level.** For \(j>m\), the products \(xy\) and \(yx\) are nonzero precisely when, respectively, \(s\) extends \(v\) and \(t\) extends \(u\). Each event has \(r^{2j-m}\) choices, with intersection of cardinality \(r^{2(j-m)}\). Both products are zero for
\[
r^{2j}-2r^{2j-m}+r^{2(j-m)}
\]
choices. Write the pairs in the intersection as \(s=va\), \(t=ub\) with \(|a|=|b|=j-m\). The two products are \((ua)(ub)^{-1}\) and \((va)(vb)^{-1}\), equal exactly when \(u=v\), i.e. \(d=m\). This contributes the additional \(\mathbf{1}_{d=m}r^{2(j-m)}\) pairs. Together with the commuting zero element, parts 1 and 2 prove the centralizer formula.

**3. Exact multiplicities and level-pair counts.** There are \(r^m\) pairs \((u,v)\) of length \(m\) with \(u=v\). For \(d<m\), choose their common \(d\)-letter prefix, then a pair of different letters, then independent remaining suffixes. This gives \(r^d r(r-1)r^{2(m-d-1)}=(r-1)r^{2m-d-1}\) elements. Now fix levels \(\ell\le h\), and sum the commuting-pair counts over the \(r^{2\ell}\) shorter elements. For each shorter element, the both-zero contributions number \(r^{2h}(r^{\ell}-1)^2\) after summing, and the both-nonzero contributions occur only for the \(r^{\ell}\) idempotents, with \(r^{2(h-\ell)}\) longer partners each. Thus the latter total is \(r^{2h-\ell}\). The level-pair and total formulas follow; the term \(2B_{r,N}-1\) counts pairs with at least one zero.

**4. Sharp asymptotic.** Let \(D_{r,N}=B_{r,N}^2-K_{r,N}\). Directly from the level-pair formula, the noncommuting pairs at levels \(\ell\le h\) number
\[
D_r(\ell,h)=2r^{\ell+2h}-r^{2h}-r^{2h-\ell}.
\]
The leading contribution as \(N\to\infty\) comes from levels near \(N\). Writing \(\ell=N-j\), \(h=N-k\) with \(j\ge k\ge0\), dividing by \(r^{3N}\), and summing diagonal terms once and off-diagonal terms twice yields, by convergent geometric sums,
\[
\lim_{N\to\infty}\frac{D_{r,N}}{r^{3N}}
=\frac{2}{1-r^{-3}}+\frac{4}{(r-1)(1-r^{-3})}
=\frac{2(r+1)}{(r-1)(1-r^{-3})}.
\]
The terms \(-r^{2h}-r^{2h-\ell}\) contribute at most order \(Nr^{2N}\) to the whole sum, negligible after dividing by \(r^{3N}\); the above geometric convergence may also be justified by uniformly summable bounds on the main terms. Since \(B_{r,N}/r^{2N}\to r^2/(r^2-1)\), division gives precisely the claimed coefficient of \(r^{-N}\) in \(D_{r,N}/B_{r,N}^2\). Its positivity proves sharpness.

## Verification
The standalone exact checker `check.py` implements the polycyclic multiplication directly using finite words and enumerates every pair and element-centralizer. Its saved output `check-output.txt` records exhaustive passes for \((r,N)=(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2)\), including all level-pair counts and centralizer-size multiplicities. For example, \((r,N)=(2,3)\) has \(86\) elements and exactly \(5062\) commuting ordered pairs; \((r,N)=(3,2)\) has \(92\) elements and \(6298\) commuting ordered pairs. The same checker verifies the asymptotic constant numerically at several cutoffs. These finite checks corroborate but do not replace the symbolic proof for arbitrary \(r,N\).

## Relationship to prior work
Jones and Lawson (2011) supply the graph inverse semigroup and polycyclic normal form, placing this family in MSC 20M18; their concern is abstract characterization and completion, not a finite-depth element-centralizer or commuting-pair spectrum. Lawson (2006 preprint, 2007 journal) studies orthogonal completion and right-ideal isomorphisms; its prefix multiplication is precisely the structural ingredient used here, but its inspected Sections 2–3 do not state the finite centralizer formulas. Existing results for the ordinary bicyclic monoid concern a one-letter limit with a different normal form and do not imply the present multi-letter zero-product census. A single fixed positive level \(m\), together with zero, is a Brandt matrix-unit inverse subsemigroup of order \(1+r^{2m}\); its elementary commuting count does not determine **cross-level** interactions or the longest-common-prefix centralizer stratification of their union.

## Limitations
The result is limited to balanced word pairs with a finite depth cutoff, not the full polycyclic monoid, arbitrary graph inverse monoids, or its orthogonal completion. Different parameter pairs \((m,d)\) can yield coincident centralizer sizes; multiplicities must be combined as specified. The asymptotic is at fixed \(r\), not joint growth of alphabet size and cutoff. An equivalent formula may exist in older literature on rooted-tree partial bijections, Brandt semigroups or prefix transformations not located in the inspected sources; this remains a priority risk. No claim of independent mathematical validation is made.

## References
1. D. G. Jones and M. V. Lawson, *Graph inverse semigroups: their characterization and completion*, first preprint 18 June 2011, arXiv:1106.3644, https://arxiv.org/abs/1106.3644. Primary MSC 20M18.
2. M. V. Lawson, *Orthogonal completions of the polycyclic monoids*, author preprint dated 27 March 2006; *Communications in Algebra* **35** (2007), 1651–1660, https://doi.org/10.1080/00927870601169317. Publicly accessible text at https://www.researchgate.net/publication/228667518_Orthogonal_Completions_of_the_Polycyclic_Monoids.
3. D. G. Jones and M. V. Lawson, Section 1.1 and Section 2.4 of reference 1, for the polycyclic presentation, prefix cancellation and inverse-monoid context; no result of that work is re-labeled as new here.
