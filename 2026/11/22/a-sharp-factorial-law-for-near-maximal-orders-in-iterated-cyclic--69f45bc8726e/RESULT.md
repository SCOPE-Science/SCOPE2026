# A sharp factorial law for near-maximal orders in iterated cyclic wreath groups

## Finding
For every prime \(p\), let \(W_{0,p}=1\) and \(W_{h,p}=W_{h-1,p}^{\,p}\rtimes C_p\) for integers \(h\ge1\), where the cyclic group regularly permutes the \(p\) factors. Equivalently, \(W_{h,p}\) is a Sylow \(p\)-subgroup of the symmetric group on \(p^h\) points. Let \(G_h\) be uniformly distributed in \(W_{h,p}\), and write \(\operatorname{ord}(G_h)=p^{M_h}\). Put \(\alpha=(p-1)/p\).

**Sharp fixed-defect extreme-order law.** For every **fixed** nonnegative integer \(r\), as \(h\to\infty\) through integers with \(h>r\),
\[
\Pr(M_h\ge h-r)=\frac{h^r}{r!}\alpha^{h-r}\left(1+O_{p,r}(h^{-1})\right),
\qquad
\Pr(M_h=h-r)=\frac{h^r}{r!}\alpha^{h-r}\left(1+O_{p,r}(h^{-1})\right).
\]
For \(r=0\), both probabilities are **exactly** \(\alpha^h\), without an error term. Thus the count of elements of order \(p^{h-r}\) is asymptotic to
\[
\frac{h^r}{r!}\alpha^{h-r}p^{(p^h-1)/(p-1)}.
\]
The factor \(h^r/r!\) gives a sharp polynomial hierarchy in the far-right tail, beyond the typical-order asymptotic. In particular, for the binary case the first extreme tail is exactly
\[
\Pr(M_h\ge h-1)=\frac{2h-1}{2^h}+2^{1-2h}\quad (p=2,\ h\ge1).
\]

## Assumptions and scope
The group uses the **permutational** wreath product with a regular cyclic top action, not an unrestricted direct or regular wreath product. Element sampling is uniform on group elements, not uniform on conjugacy classes. The prime \(p\) and defect \(r\) are held fixed in the limit. No estimate uniform over \(r\to\infty\) or \(p\to\infty\) is claimed. The exponent of \(W_{h,p}\) is \(p^h\). The order of the group is \(p^{(p^h-1)/(p-1)}\).

## Proof
**1. Exact order recursion.** Define \(F_h(j)=\Pr(M_h\le j)\), taking \(F_h(j)=0\) for \(j<0\) and \(F_0(j)=1\) for \(j\ge0\). Write a wreath element as \((g_0,\ldots,g_{p-1};\sigma)\), with the \(g_i\) independent uniform elements of \(W_{h-1,p}\) and \(\sigma\) uniform in \(C_p\). If \(\sigma\) is the identity, the order is the least common multiple of the component orders, so \(M_h\le j\) has probability \(F_{h-1}(j)^p\). If \(\sigma\ne1\), it is a \(p\)-cycle. Its \(p\)-th power has, in each coordinate, a cyclically ordered product of the \(g_i\); those products are conjugate, and a product of independent uniform group elements is uniform. Consequently its order is \(p\) times the order of that cycle product, and the corresponding probability is \(F_{h-1}(j-1)\). Weighting by the two top-action probabilities gives, for \(h\ge1\), \(j\ge0\),
\[
F_h(j)=\frac1p F_{h-1}(j)^p+\alpha F_{h-1}(j-1).\tag{1}
\]
The exponent and cardinality assertions follow inductively from the same wreath decomposition; elements with nonidentity top action and a maximal-order cycle product attain exponent \(p^h\).

**2. Near-exponent tail recursion.** For integers \(h\ge0\) and \(r\ge0\), define \(T_{h,r}=\Pr(M_h\ge h-r)\), so \(T_{h,r}=1\) whenever \(r\ge h\). For \(r=0\) and \(h\ge1\), the branch with identity top action cannot attain \(M_h=h\), while the nonidentity branch does so exactly if its cycle product has maximal order. Hence
\[
T_{h,0}=\alpha T_{h-1,0}=\alpha^h.\tag{2}
\]
For every \(r\ge1\), \(h\ge r+1\), taking complements in (1) yields
\[
T_{h,r}=\alpha T_{h-1,r}+B_p(T_{h-1,r-1}),
\qquad B_p(x)=\frac{1-(1-x)^p}{p}.\tag{3}
\]
This is an exact finite-depth recursion, including the boundary \(T_{r,r}=1\).

**3. Sharp asymptotic induction.** For fixed \(r\), put \(S_{h,r}=\alpha^{-h}T_{h,r}\). By (2), \(S_{h,0}=1\). For \(0\le x\le1\), the binomial theorem gives \(B_p(x)=x+O_p(x^2)\), with a constant uniform over that interval. Dividing (3) by \(\alpha^h\), we obtain
\[
S_{h,r}-S_{h-1,r}=\alpha^{-1}S_{h-1,r-1}
+O_p\!\left(\alpha^{h-2}S_{h-1,r-1}^{\,2}\right).\tag{4}
\]
Inductively suppose \(S_{t,r-1}=t^{r-1}/((r-1)!\alpha^{r-1})+O_{p,r}(t^{r-2})\) for \(r\ge2\); for \(r=1\), use exactly \(S_{t,0}=1\). In either case \(S_{t,r-1}=O_{p,r}(t^{r-1})\). The errors in (4), summed over \(h\), are uniformly bounded because
\[
\sum_{h\ge r+1}\alpha^{h-2}h^{2r-2}<\infty.
\]
Summing (4) from \(h=r+1\) onward and using the finite initial value \(S_{r,r}=\alpha^{-r}\), and the elementary power sum \(\sum_{t\le h}t^{r-1}=h^r/r+O_r(h^{r-1})\), gives
\[
S_{h,r}=\frac{h^r}{r!\alpha^r}+O_{p,r}(h^{r-1})\quad (r\ge1).\tag{5}
\]
This proves the first stated formula. For the exact-order formula, subtract adjacent tails: \(\Pr(M_h=h-r)=T_{h,r}-T_{h,r-1}\). For fixed \(r\ge1\), (5) shows that the second term is smaller by a factor \(O_{p,r}(1/h)\), completing the proof. For \(r=0\) (2) is exact.

**4. Exact binary next-to-maximum expression.** At \(p=2\), equation (3) for \(r=1\) becomes \(T_{h,1}=\tfrac12T_{h-1,1}+T_{h-1,0}-\tfrac12T_{h-1,0}^2\). Insert \(T_{h-1,0}=2^{-(h-1)}\), multiply by \(2^h\), and sum with \(T_{1,1}=1\). The result is \(2^hT_{h,1}=2h-1+2^{1-h}\), yielding the displayed formula.

## Verification
An independent finite-group checker constructs all wreath permutations and computes orders from their actual cycle decompositions. Exhaustive agreement with exact rational recurrence (1) was obtained for \((p,h)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(5,1),(5,2)\), including every element in the groups of orders \(32768\) and \(15625\). The checker and its captured output accompany this result. Asymptotic ratios at larger \(h\) were also evaluated numerically; this is only a sanity check, not the proof of the asymptotic statement, which is (2)–(5).

## Relationship to prior work
Abért and Virág (first posted December 13, 2002) established the asymptotic **typical** logarithmic order and a branching-random-walk framework for the same groups. Schlage-Puchta (published 2004; arXiv posting 2011) contrasted order sampling by conjugacy classes and cited earlier uniform-element estimates. Pólya's wreath-product cycle-index formula and Renteln's 2024 application determine complete **finite-depth** permutation cycle indices, and hence encode exact element-order counts; no novelty is claimed for this general finite enumeration or for the basic wreath-product decomposition. The assertion treated here is the explicit sharp factorial prefactor in each fixed-defect near-maximal-order tail, a very different scale from typical order and not stated in the primary results inspected. The possibility of an earlier equivalent rare-tail expansion, including an extraction from the general cycle-index theory, remains a priority risk.

## Limitations
This is an asymptotic for each fixed prime and fixed defect, not a uniform moderate-deviation or central-limit theorem. The proof uses known group structure and elementary binomial expansion; finite exhaustive checks are illustrative. No independent external proof audit or historical priority certification has been performed.

## References
1. M. Abért and B. Virág, *Dimension and randomness in groups acting on rooted trees*, arXiv:math/0212191, initial submission 2002-12-13; J. Amer. Math. Soc. 18 (2005), 157–192. https://arxiv.org/abs/math/0212191
2. J.-C. Schlage-Puchta, *The order of elements in Sylow p-subgroups of the symmetric group*, Acta Math. Hungar. 105 (2004), 187–195; arXiv:1105.1610, submitted 2011-05-09. https://arxiv.org/abs/1105.1610
3. P. Renteln, *Counting Sylow double cosets in the symmetric group*, Discrete Mathematics 347 (2024), 114109. https://doi.org/10.1016/j.disc.2024.114109
4. Pólya's classical cycle-index wreath-product composition theorem, used in reference 3, Theorem 7.
