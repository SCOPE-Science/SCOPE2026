# The exact rank spectrum and half-factorial growth of hub-avoiding wheel partial isometries

## Finding
For each integer \(n\ge 4\), let \(W_n\) be the wheel consisting of a hub and a rim cycle \(C_n\). Let \(\mathcal M_n\) be the inverse monoid of all wheel-distance-preserving partial injections with domain and image entirely on the rim. Its identity is the partial identity on the rim, not the full identity on the wheel. Write \(c_{n,k}\) for the number of its elements having domain rank \(k\). Then
\[
 c_{n,0}=1,\qquad c_{n,n}=2n,
\]
and, for every \(1\le k<n\),
\[
 c_{n,k}=n^2\sum_{r=1}^{\min(k,n-k)}
 \frac{((r-1)!)^2}{r!}
 {n-k-1\choose r-1}^{\!2}
 [x^{k-r}]\left(\frac{1+x}{1-x}\right)^r.
 \tag{1}
\]
Here \([x^j]\) is the ordinary coefficient-extraction operator. Thus \(T_n=|\mathcal M_n|=\sum_{k=0}^n c_{n,k}\) is determined exactly in every dimension. In particular,
\[
 \lim_{n\to\infty}\frac{\log T_n}{n\log n}=\frac12.\tag{2}
\]
Let \(E_n\) count elements of \(\mathcal M_n\) which arise by restricting an automorphism of \(W_n\) to a rim subset. Then
\[
 \lim_{n\to\infty}\frac{\log(E_n/T_n)}{n\log n}=-\frac12.\tag{3}
\]
Equivalently, the proportion admitting an ambient automorphism extension is \(\exp(-(1/2+o(1))n\log n)\). The formulas are for distinct partial maps, not for presentations, generators, isomorphism types, or conjugacy classes.

## Assumptions and scope
The graph \(W_n\) has rim vertex set \(\mathbb Z/n\mathbb Z\), hub \(\ast\), rim edges \(\{i,i+1\}\), and hub edges \(\{\ast,i\}\). An element of \(\mathcal M_n\) is an injective partial map \(f:A\to B\) with \(A,B\subseteq\mathbb Z/n\mathbb Z\) such that \(d_{W_n}(u,v)=d_{W_n}(f(u),f(v))\) for all \(u,v\in A\). Rank means \(|A|\), whereas the rank of a monoid as a generating set is a different invariant. The cycle is a simple graph; the statement concerns \(n\ge4\). Since distinct rim vertices are at wheel distance one precisely when adjacent in the rim cycle and otherwise at distance two, elements of \(\mathcal M_n\) are precisely induced-subgraph isomorphisms between subsets of \(C_n\). The identity belongs to \(\mathcal M_n\) as the identity on all rim vertices.

## Proof
**1. Reduction to induced paths.** Let \(1\le k<n\). Every \(k\)-vertex subset \(A\) of \(C_n\) induces a disjoint union of \(r\) nonempty paths, separated cyclically by \(r\) nonempty gaps of missing vertices, where \(1\le r\le\min(k,n-k)\). Write \(m_j\) for the number of induced paths with \(j\) vertices, so \(\sum_{j\ge1}m_j=r\) and \(\sum_{j\ge1}jm_j=k\).

**2. Count subsets of a given path type.** Distinguish one of the \(r\) path starts and assign it one of the \(n\) rim vertices. There are \(r!/\prod_jm_j!\) possible cyclically ordered sequences of path lengths beginning at the distinguished start, and \({n-k-1\choose r-1}\) positive compositions of the \(n-k\) omitted vertices into the subsequent cyclic gaps. Each underlying subset has exactly \(r\) possible distinguished starts, hence the number of subsets with this path-multiset type is
\[
 s(n,k;(m_j))=\frac{n(r-1)!}{\prod_jm_j!}{n-k-1\choose r-1}.\tag{4}
\]
This count is integral by its direct combinatorial interpretation.

**3. Count partial isomorphisms with this type.** Two such induced subgraphs are isomorphic precisely when their multisets of path lengths agree. For a fixed ordered pair of such subsets, the number of isomorphisms is
\[
 a((m_j))=\left(\prod_jm_j!\right)2^{\sum_{j\ge2}m_j},\tag{5}
\]
because equal-length components may be permuted, every nontrivial path has two orientation choices, and a singleton path has one. Summing \(s^2a\) over all multiplicity vectors yields
\[
 c_{n,k}=n^2\sum_{r=1}^{\min(k,n-k)}((r-1)!)^2{n-k-1\choose r-1}^2
 \sum_{\substack{\sum m_j=r\\\sum jm_j=k}}
 \frac{2^{\sum_{j\ge2}m_j}}{\prod_jm_j!}.\tag{6}
\]
The weighted path-generating series is \(u(x)=x+2x^2/(1-x)=x(1+x)/(1-x)\). By the multinomial theorem, the innermost sum equals \([x^k]u(x)^r/r!=[x^{k-r}]((1+x)/(1-x))^r/r!\), giving (1). For \(k=0\), only the empty map exists. For \(k=n\), automorphisms of the full cycle form the dihedral group of order \(2n\); this is why the full-rank term must not be obtained by extending the path-run formula.

**4. Half-factorial growth.** Put \(s=\lfloor n/2\rfloor\). A fixed independent subset of \(C_n\) of size \(s\) has no edges, so every one of its \(s!\) self-bijections lies in \(\mathcal M_n\):
\[
 T_n\ge s!.\tag{7}
\]
For each proper subset, its induced graph has at most \(s\) path components; its automorphism group has order at most \(2^s s!\), since at most \(s\) components may be permuted and each path has at most two automorphisms. For every ordered pair of subsets there are either zero isomorphisms or at most \(2^s s!\). There are \(4^n\) ordered pairs of subsets in total. Adding the \(2n\) full-domain automorphisms gives the harmless bound
\[
 T_n\le 4^n2^s s!+2n.\tag{8}
\]
Stirling's formula shows that the logarithms of both sides of (7)--(8), divided by \(n\log n\), tend to \(1/2\), proving (2).

**5. Nonextendibility.** For \(n\ge4\), each automorphism of \(W_n\) fixes its unique high-degree hub and acts on the rim by one of the \(2n\) dihedral symmetries. Its restriction to any of the \(2^n\) rim subsets belongs to \(\mathcal M_n\). Conversely, the \(2n\) distinct full-rim automorphisms each occur once, so
\[
 2n\le E_n\le 2n\,2^n.\tag{9}
\]
Consequently \(\log E_n=O(n)\). Combining this with \(\log T_n/(n\log n)\to1/2\) proves (3). The argument does not assert that all smaller-rank isomorphisms fail to extend; it quantifies their proportion across the full monoid.

## Verification
The included standard-library script `verify.py` independently enumerates all partial injections preserving cycle adjacency, through \(n=7\), and compares their rank distributions with (1). It also directly counts source-subset path multisets through \(n=12\), compares the exact rational coefficient formula for every rank through \(n=12\), and enumerates distinct dihedral restrictions for \(4\le n\le10\). Successful execution prints `VERIFY_OK`. The first values \(T_4,\dots,T_{10}\) are \(97,286,955,3396,12753,50482,208251\). Finite tests corroborate (1); they do not substitute for the all-\(n\) proof. The growth limits follow from the displayed inequalities, not numerical extrapolation.

## Relationship to prior work
V. H. Fernandes (arXiv:2307.16257, first publicly posted 2023-07-30) introduced and studied the hub-avoiding wheel partial-isometry monoid, characterizing its Green relations, generators, and minimal generating-set rank. Its \(\mathscr J\)-types already use induced component lengths, a starting point explicitly credited here. The checked paper does not give the element-count rank spectrum (1) or asymptotic claims (2)--(3). R. Jajcay, T. Jajcayova, N. Szakács, and M. B. Szendrei (arXiv:1809.04422) develop the general theory of inverse monoids of partial graph automorphisms; their results provide conceptual context but no cited enumerator for the rim cycles. I. Dimitrova and collaborators (arXiv:2101.12468) enumerate partial automorphisms of *paths*, whose boundary decomposition differs from the cyclic path-run count. V. H. Fernandes and T. Paulista (arXiv:2205.02196) determine the cardinality of the cycle-*geodesic* partial-isometry monoid, which consists of restrictions of dihedral permutations. That is not \(\mathcal M_n\): the wheel metric contracts nonadjacent rim distances to two. Formula (3) makes the distinction quantitatively sharp. The absence of a matching result in these inspected works is not a universal claim of publication priority.

## Limitations
The theorem concerns the hub-avoiding inverse monoid with its *rim identity* and not the full wheel partial-isometry monoid (whose identity acts on the hub too). It counts labeled partial maps and uses the full wheel metric, rather than the intrinsic geodesic metric of the bare cycle. It proves logarithmic growth exponents and a logarithmic extension-rate exponent; no sharp multiplicative asymptotic for \(T_n\) or \(E_n\) is claimed. Coverage of nonindexed or inaccessible literature cannot be ruled out, and an independent mathematical audit has not been performed.

## References
1. V. H. Fernandes, *On the monoid of partial isometries of a wheel graph*, arXiv:2307.16257 (2023), https://arxiv.org/abs/2307.16257.
2. R. Jajcay, T. Jajcayova, N. Szakács and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422 (2018), https://arxiv.org/abs/1809.04422.
3. I. Dimitrova, V. H. Fernandes, J. Koppitz and T. M. Quinteiro, *Partial Automorphisms and Injective Partial Endomorphisms of a Finite Undirected Path*, arXiv:2101.12468 (2021), https://arxiv.org/abs/2101.12468.
4. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196 (2022), https://arxiv.org/abs/2205.02196.
