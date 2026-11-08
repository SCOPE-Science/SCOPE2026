# The \(-1\)-root multiplicity of independence polynomials of cycle-bouquet line graphs

## Finding
Let \(r\ge1\), let \(\ell_1,\ldots,\ell_r\ge3\) be integers, and form a **cycle bouquet** \(B(\ell_1,\ldots,\ell_r)\) by identifying one vertex of each of \(r\) otherwise vertex-disjoint simple cycles of the indicated lengths. Let \(L(B)\) be its line graph, and let \(I_{L(B)}(z)=\sum_{j\ge0}i_j(L(B))z^j\) be its independence polynomial. Set
\[
c=\#\{i:3\mid\ell_i\},\qquad b=\#\{i:\ell_i\equiv2\pmod3\}.
\]
The **exact multiplicity** of the root \(z=-1\) is
\[
\boxed{\operatorname{ord}_{z=-1}I_{L(B)}(z)=\max\{c-1,0\}.}
\]
Thus only cycles with length divisible by three contribute to the multiplicity, and the common vertex causes exactly one unit of cancellation when at least one such cycle is present. In particular, these connected line graphs have arbitrarily large \(-1\)-root multiplicities.

More precisely, define the path-matching polynomials \(p_0(z)=p_1(z)=1\) and \(p_m(z)=p_{m-1}(z)+zp_{m-2}(z)\) for \(m\ge2\). Then **every coefficient** of the independence polynomial is given by
\[
\boxed{I_{L(B)}(z)=\prod_{i=1}^r p_{\ell_i-1}(z)+2z\sum_{i=1}^r p_{\ell_i-2}(z)\prod_{j\ne i}p_{\ell_j-1}(z).}
\]
When \(c=0\), the exact signed evaluation is
\[
I_{L(B)}(-1)=(1-2b)\prod_{i=1}^r p_{\ell_i-1}(-1),
\]
which is a nonzero odd integer. When \(c\ge1\), put \(J=\{i:3\mid\ell_i\}\) and \(k_i=\ell_i/3\) for \(i\in J\). The first nonzero Taylor coefficient is the explicit nonzero integer
\[
\boxed{\left.\frac{I_{L(B)}(z)}{(z+1)^{c-1}}\right|_{z=-1}
=-2\left(\prod_{i\in J}(-1)^{k_i-1}k_i\right)
\left(\prod_{j\notin J}p_{\ell_j-1}(-1)\right)
\left(\sum_{i\in J}\frac1{k_i}\right).}
\]
Products over empty index sets are \(1\). The displayed quotient is evaluated after cancelling the proven polynomial factor.

## Assumptions and scope
All graphs are finite, simple and undirected. The shared bouquet vertex is the only intersection of distinct cycle blocks; no bridges, additional edges or pendant decorations are allowed. There are no restrictions on repetition of lengths, nor on the number \(r\) beyond positivity. Vertex labels are irrelevant: the identities hold for each labelled realization as well as its isomorphism class. Root multiplicity is the order of vanishing of the polynomial at the indicated complex point.

## Proof
**1. Matchings and independence sets.** By definition of a line graph, independent vertex subsets of \(L(B)\) are in bijection with sets of pairwise nonincident edges of \(B\). Therefore \(I_{L(B)}(z)\) is the generating polynomial for matchings of \(B\), with an edge receiving weight \(z\).

**2. Exact polynomial by the shared vertex.** Let \(v\) denote the common vertex. If a matching leaves \(v\) unmatched, on each cycle of length \(\ell_i\) it is an arbitrary matching of the path on its \(\ell_i-1\) remaining vertices; its polynomial is \(p_{\ell_i-1}(z)\). If \(v\) is matched, exactly one of the two incident edges from one cycle \(i\) is used. Either choice leaves a path on \(\ell_i-2\) vertices in that cycle, and the other cycles contribute their paths on \(\ell_j-1\) vertices. The resulting exhaustive, disjoint cases yield the stated complete polynomial. The path recurrence follows by inspecting whether the last path edge is selected.

**3. Residues and simple zeros of the path factors.** With \(t\) a formal variable, the recurrence gives
\[
\sum_{m\ge0}p_m(z)t^m=\frac1{1-t-zt^2}.
\]
At \(z=-1\), and on differentiating with respect to \(z\), respectively, this becomes
\[
\sum_{m\ge0}p_m(-1)t^m=\frac{1+t}{1+t^3},\qquad
\sum_{m\ge0}p'_m(-1)t^m=\frac{t^2(1+t)^2}{(1+t^3)^2}.
\]
Consequently \(p_{\ell-1}(-1)=0\) precisely for \(3\mid\ell\). If \(\ell=3k\), then
\[
p'_{\ell-1}(-1)=(-1)^{k-1}k,\qquad p_{\ell-2}(-1)=(-1)^{k-1};
\]
the zero is simple and the ratio of the latter value to the derivative is \(1/k\). For \(3\nmid\ell\), the value \(p_{\ell-1}(-1)\) is \(1\) or \(-1\), and
\[
\frac{p_{\ell-2}(-1)}{p_{\ell-1}(-1)}=
\begin{cases}0,&\ell\equiv1\pmod3,\\1,&\ell\equiv2\pmod3.\end{cases}
\]

**4. Multiplicity with no three-divisible cycle.** If \(c=0\), factor the nonzero product \(\prod_i p_{\ell_i-1}(-1)\) out of the matching polynomial at \(-1\). By the last displayed ratio, the remaining factor is \(1-2b\), an odd nonzero integer. Hence the multiplicity is zero.

**5. Multiplicity with at least one three-divisible cycle.** Suppose \(c\ge1\). Exactly \(c\) of the factors \(p_{\ell_i-1}(z)\) have simple zeros at \(-1\); the other factors are nonzero. The first product in the matching polynomial has order \(c\). A summand indexed by \(i\notin J\) also has order \(c\). Every summand indexed by \(i\in J\) has order exactly \(c-1\). Factoring out \((z+1)^{c-1}\) and substituting \(z=-1\) gives the stated first Taylor coefficient, because \(p_{\ell_i-2}(-1)/p'_{\ell_i-1}(-1)=1/k_i\). Its sign factors are nonzero, and its remaining sum is strictly positive. Therefore cancellation at that order is impossible, proving that the multiplicity is exactly \(c-1\). Combining the cases proves all assertions. \(\square\)

## Verification
The accompanying standalone \(\texttt{verify.py}\) enumerates matchings of independently constructed cycle bouquets by edge-include/edge-exclude recursion. On \(126\) mixed-length or repeated-length bouquets (up to four cycles and at most nineteen total cycle edges), it compares the **entire** brute-force matching polynomial coefficientwise with the displayed product formula, then checks both the root multiplicity and signed first nonzero coefficient. It separately checks another \(336\) equal-length parameter cases (up to twelve cycles, lengths through thirty) using the symbolic formula and divisibility identities. Successful execution prints \(\texttt{VERIFY_OK}\). These finite tests are corroborative; the unrestricted proof is the algebraic argument above.

## Relationship to prior work
Bhardwaj, Chau, Ikram, Lather, Nanjangud and Venugopal (first public version July 9, 2026) introduced a systematic treatment of the multiplicity of \(-1\) as an independence-polynomial root. Their Section 6 uses matching and characteristic polynomials to study **line graphs of forests**, while the present result treats connected line graphs of a nonforest family with arbitrarily many cycles. The line-graph/matching-polynomial identity used in Step 1 is classical and is not claimed as new. Xu (2025) gave sharp general upper bounds for multiplicities of nonzero matching-polynomial roots and classified extremizers; those bounds do not determine the root order for arbitrary mixtures of cycle lengths. Ghorbani (2012, arXiv preprint initially published 2010) determined, among other results, the matching polynomials of friendship graphs (bouquets of triangles); that homogeneous subfamily is also prior work. The contribution here is the arbitrary mixed-cycle full polynomial and exact root-order/leading-coefficient classification, which is not a corollary of the few-distinct-matching-roots classification for general cycle lengths. Mphako-Banda's 2007 'flower' graphs share petals with a central cycle along **edges** and address chromatic and flow polynomials, not bouquets sharing one vertex or matching roots.

## Limitations
The theorem does not classify line graphs of arbitrary cacti or their homological invariants; it applies only to the specified one-point union of cycles. The verification program does not independently certify the general proof. Literature searches cannot establish global historical priority; unindexed sources or other equivalent formulations may exist. Independent mathematical assessment has not been performed.

## References
1. O. P. Bhardwaj, T. Chau, S. Ikram, G. Lather, V. Nanjangud, C. Venugopal, *Multiplicity of negative one of independence polynomials of graphs*, arXiv:2607.08480v1 (first publicly available July 9, 2026), https://arxiv.org/abs/2607.08480.
2. E. Ghorbani, *Graphs with few matching roots*, arXiv:1011.0284v3 (2012; first publicly available November 1, 2010), https://arxiv.org/html/1011.0284v3.
3. L. Xu, *On the multiplicity of matching polynomial roots and \(\theta\)-critical graphs*, arXiv:2509.23842v1 (September 28, 2025), https://arxiv.org/abs/2509.23842.
4. E. Mphako-Banda, *Some Polynomials of Flower Graphs*, International Mathematical Forum 2 (2007), 2511–2518, https://paperzz.com/doc/8275221/some-polynomials-of-flower-graphs.
