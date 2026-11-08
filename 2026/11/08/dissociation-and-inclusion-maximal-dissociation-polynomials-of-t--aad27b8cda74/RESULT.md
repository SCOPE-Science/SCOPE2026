# Dissociation and inclusion-maximal dissociation polynomials of triangular graphs

## Finding

For every integer \(n\ge3\), let \(T_n=J(n,2)=L(K_n)\) be the triangular graph. Its vertices are the two-element subsets of \([n]\), and two distinct vertices are adjacent exactly when their subsets intersect. A *dissociation set* is a vertex subset whose induced subgraph has maximum degree at most one. Let \(D_n(z)\) count all dissociation sets by cardinality, including the empty set, and let \(M_n(z)\) count the inclusion-maximal dissociation sets.

The complete polynomials are

\[
D_n(z)=n![x^n]\exp\!\left(x+\frac{zx^2}{2}+\frac{z^2x^3}{2}\right),
\]

\[
M_n(z)=n![x^n]\left[\exp\!\left(\frac{zx^2}{2}+\frac{z^2x^3}{2}\right)+x\exp\!\left(\frac{z^2x^3}{2}\right)\right].
\]

The attainable cardinalities of inclusion-maximal dissociation sets are exactly all integers in the interval

\[
\left\{\left\lceil\frac n2\right\rceil,\left\lceil\frac n2\right\rceil+1,\ldots,\left\lfloor\frac{2n}{3}\right\rfloor\right\}.
\]

Consequently the minimum cardinality among inclusion-maximal dissociation sets is \(\lceil n/2\rceil\), whereas the maximum dissociation number is \(\lfloor 2n/3\rfloor\). The two generating functions provide exact multiplicities at every cardinality, not just extrema.

## Assumptions and scope

All graphs are finite, simple and labeled. The coefficient operator \([x^n]\) extracts the coefficient of \(x^n\) in an exponential formal power series. The integer \(n\) is unrestricted apart from \(n\ge3\). Here *maximal* always means inclusion-maximal, not maximum-cardinality. No assertion is made about other Johnson parameters \(J(n,k)\) with \(k>2\), or arbitrary line graphs.

Associate a selected vertex of \(T_n\), namely a two-subset of \([n]\), with an edge of \(K_n\). For a selected edge set \(F\subseteq E(K_n)\), let \(H_F=([n],F)\). We regard isolated vertices of \(H_F\) as components.

## Proof

**Component lemma.** A set \(F\) corresponds to a dissociation set in \(T_n\) if and only if every component of \(H_F\) is an isolated vertex, a single edge \(K_2\), or a two-edge path \(P_3\).

Indeed, the degree of an edge \(uv\in F\) as a vertex of \(L(K_n)[F]\) equals \(\deg_{H_F}(u)+\deg_{H_F}(v)-2\), because \(K_n\) is simple. If this is at most one for every selected edge, then every vertex incident with a selected edge has degree at most two. A vertex of degree two must be joined only to degree-one vertices: any edge incident to a second vertex of degree at least two would have line-graph degree at least two. Thus each nontrivial component is \(K_2\) or \(P_3\). Conversely these components plainly give line-graph degree at most one.

Write \(a\) for the number of \(P_3\) components, \(b\) for the number of \(K_2\) components, and \(c\) for the number of isolated vertices. Then \(3a+2b+c=n\), and the corresponding dissociation set has size \(2a+b\). Partitioning the \(n\) labeled ground vertices into unordered components gives exactly

\[
N(n;a,b,c)=\frac{n!}{2^a a!\,2^b b!\,c!}
\]

such sets: each triple has three possible central vertices, hence the division by \(2\) after assigning its labels; each pair has one edge. Distinct partitions give distinct edge sets. Therefore

\[
D_n(z)=\sum_{\substack{a,b,c\ge0\\3a+2b+c=n}}\frac{n!z^{2a+b}}{2^{a+b}a!b!c!},
\]

which is equivalent to the first coefficient formula.

**Maximality lemma.** Such a dissociation set is inclusion-maximal if and only if either \(c=0\), or \(c=1\) and \(b=0\).

For necessity, if \(c\ge2\), the edge joining two isolated vertices can be added, preserving the component condition. If \(c=1\) and \(b\ge1\), an edge joining the lone isolated vertex to an endpoint of one existing \(K_2\) extends that \(K_2\) to a \(P_3\), again preserving the condition. Hence neither situation is maximal.

For sufficiency, suppose \(c=0\). Any unselected edge either meets a vertex of a \(P_3\), in which case the new edge meets both selected edges when it touches the middle, or an already selected edge gains a second line-graph neighbor when it touches an endpoint; or it joins two different \(K_2\) components, in which case the new edge itself has two distinct selected neighbors. There is no unselected edge with both endpoints inside a single \(K_2\). Thus no edge can be added. If \(c=1,b=0\), every unselected edge either lies between nonisolated components, to which the preceding argument applies, or meets the sole isolated vertex and a \(P_3\); in the latter case an existing selected edge acquires a second line-graph neighbor. Thus no edge can be added in this case either.

The first maximal family has \(c=0\) and is counted by \(\exp(zx^2/2+z^2x^3/2)\). The second has \(c=1,b=0\) and is counted by \(x\exp(z^2x^3/2)\). These are disjoint; their sum proves the second coefficient formula. Equivalently,

\[
M_n(z)=\sum_{\substack{a,b\ge0\\3a+2b=n}}\frac{n!}{2^{a+b}a!b!}z^{2a+b}+\mathbf 1_{n\equiv1\;\mathrm{mod}\;3}\frac{n!}{2^{(n-1)/3}((n-1)/3)!}z^{2(n-1)/3}.
\]

Finally, the \(c=0\) configurations have \(2a+b=(n+a)/2\), where \(a\) runs through all nonnegative integers satisfying \(3a\le n\) and \(a\equiv n\pmod2\). Incrementing \(a\) by two increments cardinality by one. Their minimum is \(\lceil n/2\rceil\). Their largest size is always \(\lfloor2n/3\rfloor\). In the congruence class \(n\equiv1\pmod3\), the \(c=1,b=0\) family contributes additional sets of that same upper size \(2(n-1)/3=\lfloor2n/3\rfloor\), but introduces no new size. This establishes the exact, gap-free maximal-cardinality spectrum and both extrema. \(\square\)

## Verification

Running `python3 verify_triangular_dissociation.py` checks all vertex subsets of \(T_n\) for \(3\le n\le7\), testing the induced maximum-degree-one condition directly from triangular-graph adjacency. Each valid set is tested for inclusion-maximality by all single-vertex additions; the resulting coefficient tables are compared with the component formulas. The executable check completed with:

`VERIFY_OK n=3..7 subsets=2131016 dissociation_sets=2433 maximal_sets=1098 full_polynomial=PASS maximal_polynomial=PASS interval_spectrum=PASS`

These finite computations do not prove the theorem for unbounded \(n\); the unrestricted proof is the component and maximality arguments above.

## Relationship to prior work

Tu, Li and Du (2021) give sharp general-graph and triangle-free-graph upper bounds for the number of maximal dissociation sets, not exact counts on this graph family. Duginov, Kuskova, Malyshev and Shur (2022) study structural and algorithmic properties of maximal dissociating sets and hard subclasses; their general results frame the minimal-maximal and maximum size questions. Tu, Xiao and Lang (2023) study the dissociation polynomial on cubic graphs, obtaining a sharp extremal inequality. The triangular graph \(T_n\) has degree \(2n-4\) and is not cubic for any integer \(n\ge3\), so the latter theorem does not imply this enumerator.

Orlovich, Dolgui, Finke, Gordon and Werner (2011) investigate dissociation complexity and algorithms for certain line graphs; general maximum-size algorithms do not determine all coefficients of the dissociation or inclusion-maximal dissociation polynomials. The present statement is the explicit labeled-component decomposition and both polynomials for \(L(K_n)\), including the maximal cardinality spectrum. No assertion of absolute publication priority is made.

## Limitations

The claim concerns only \(J(n,2)\) for \(n\ge3\). The finite verifier covers \(n\le7\) and does not exhaust larger instances. Some relevant published sources were examined through text/selected sections rather than every page, and a related older publisher-hosted full text was not fully accessible. A differently indexed exact triangular-graph enumerator might exist; independent review and further literature comparison would be required before a publication-priority assertion.

## References

- J. Tu, Y. Li and J. Du, *Maximal and maximum dissociation sets in general and triangle-free graphs*, arXiv:`2103.01402` (2021), subsequently Applied Mathematics and Computation 426 (2022), 127107; earliest public arXiv posting 2021-03-02.
- O. I. Duginov, B. M. Kuskova, D. S. Malyshev and N. A. Shur, *Structural and algorithmic properties of maximal dissociating sets in graphs*, Trudy Inst. Mat. Mekh. UrO RAN 28(2) (2022), 114–142. DOI: `10.21538/0134-4889-2022-28-2-114-142`; first verified public journal posting 2022-05-24.
- J. Tu, J. Xiao and R. Lang, *Counting the number of dissociation sets in cubic graphs*, AIMS Mathematics 8(5) (2023), 10021–10032. DOI: `10.3934/math.2023507`; publication date 2023-02-23.
- Y. Orlovich, A. Dolgui, G. Finke, V. Gordon and F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics 159 (2011), 1352–1366. DOI: `10.1016/j.dam.2011.04.023`.
