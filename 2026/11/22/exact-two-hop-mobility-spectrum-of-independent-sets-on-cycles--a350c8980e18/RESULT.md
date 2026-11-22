# Exact two-hop mobility spectrum of independent sets on cycles

## Finding

For every integer \(n\ge5\), let \(G_n\) be the undirected reconfiguration graph whose vertices are all **indexed independent sets** of the simple cycle \(C_n\). Two states are adjacent exactly when one occupied vertex is relocated by two steps clockwise or counterclockwise on the cycle, and the resulting state remains independent. Moves by one step are **not** allowed, and neither are arbitrary jumps.

If \(I\ne\varnothing\), enumerate its occupied sites in clockwise order and write \(g_1,\ldots,g_k\) for the successive clockwise distances (positive gaps), so \(k=|I|\), every \(g_i\ge2\), and \(\sum_i g_i=n\). Define \(t(I)=|\{i:g_i\ge4\}|\). Then
\[
\boxed{\deg_{G_n}(I)=2t(I),\qquad \deg_{G_n}(\varnothing)=0.}
\]

More strongly, the **entire degree distribution** is determined at every ring size by the rational bivariate gap series
\[
W(z,u)=z^2+z^3+\frac{uz^4}{1-z},\qquad
\boxed{D_n(u)=\sum_{I\in V(G_n)}u^{\deg(I)/2}
=1+[z^n]\frac{z\,\partial_z W(z,u)}{1-W(z,u)}}.
\]
For each occupancy count \(k\ge1\) and half-degree \(t\), the coefficient is the exact nonnegative integer
\[
\boxed{N_{n,k,t}=\frac{n}{k}\binom{k}{t}
[z^{n-2k-2t}]\frac{(1+z)^{k-t}}{(1-z)^t},}
\]
with zero coefficients when the exponent is negative; when \(t=0\), the denominator is one. Thus \(D_n(u)=1+\sum_{k,t}N_{n,k,t}u^t\).

All even degrees from zero through \(2\lfloor n/4\rfloor\) occur. Writing \(n=4h+r\) with \(0\le r\le3\), the number of independent sets achieving the largest degree is
\[
\boxed{M_n=\begin{cases}
4,&r=0,\\
n,&r=1,\\
n(h+3)/2,&r=2,\\
n(h+1)(h+8)/6,&r=3.
\end{cases}}
\]
The total number of undirected reconfiguration edges is
\[
\boxed{|E(G_n)|=nF_{n-3}},
\]
where \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\). The degree-zero coefficient is \(1+P_n\), where \(P_0=3,P_1=0,P_2=2,P_j=P_{j-2}+P_{j-3}\) is the classical Perrin sequence; this **known frozen-state count is not itself claimed as new**.

For example, \(D_{12}(u)=30+180u+108u^2+4u^3\), whereas \(D_{20}(u)=278+3000u+7120u^2+4220u^3+505u^4+4u^5\).

## Assumptions and scope

The ring consists of \(n\ge5\) separately labelled vertices modulo \(n\). An independent set never contains adjacent vertices modulo \(n\). States are *not* identified under rotations, reversal, or particle permutations: each occupied subset is one vertex. A legal step removes exactly one occupied site and occupies exactly one previously empty site differing from the removed site by \(+2\) or \(-2\) modulo \(n\). The intermediate state after removal need not be separately counted. The power \(u^{\deg/2}\) is an integer exponent because every degree is even. Empty-state conventions are explicit. No statement is made for cycles with fewer than five vertices.

## Proof

**1. Exact local moves.** Let two consecutive occupied sites be \(a,b\), separated clockwise by \(g\). The clockwise move \(a\mapsto a+2\) is legal exactly when \(g\ge4\): its new site lies at clockwise distance \(g-2\) from \(b\), so independence requires \(g-2\ge2\). The preceding occupied-site distance is increased by two, so it causes no other collision. Similarly, \(b\mapsto b-2\) is legal exactly when \(g\ge4\). When there is a single particle, the unique circular gap is \(n\ge5\), and these two moves are legal. For \(n\ge5\) the two destinations of one particle are distinct; moving different occupied particles also produces distinct output sets, since the removed site identifies the move. Consequently every long gap produces exactly two distinct neighbors and no other move is legal, proving the degree law.

**2. Anchored circular-gap count.** For a configuration with \(k\ge1\), distinguish one occupied vertex as an anchor and list the \(k\) clockwise gaps starting there. Every gap is either two, three, or at least four. With \(u\) marking long gaps, the generating polynomial for one gap is precisely \(W(z,u)\). For \(k\) ordered gaps the series is \(W(z,u)^k\). Every actual indexed independent set is represented by exactly \(k\) choices of anchor, while a fixed anchored gap list has \(n\) choices of anchor position. Thus its contribution at length \(n\) has factor \(n/k\), including configurations with rotational symmetry, because anchor positions are indexed. Summing over \(k\),
\[
D_n(u)-1=\sum_{k\ge1}\frac nk[z^n]W(z,u)^k
=[z^n]z\frac{\partial}{\partial z}\sum_{k\ge1}\frac{W(z,u)^k}{k}
=[z^n]\frac{zW_z(z,u)}{1-W(z,u)}.
\]
To obtain occupancy and degree coefficients, choose \(t\) among \(k\) gaps to be long. Short gaps contribute \(z^{2(k-t)}(1+z)^{k-t}\), and long gaps contribute \(z^{4t}(1-z)^{-t}\), yielding the stated formula for \(N_{n,k,t}\).

**3. All degrees and sharp maximizers.** Each long gap consumes at least four sites; hence \(t\le h=\lfloor n/4\rfloor\). Every \(1\le t\le h\) occurs by taking \(t\) gaps of lengths \(4,\ldots,4,n-4(t-1)\); this gives a legal independent set. Degree zero occurs because every \(n\ge5\) is expressible as a sum of twos and threes (choose adjacent occupied gaps accordingly). To count maximum-degree states take exactly \(h\) long gaps. If \(r=0\), only the \(h\) gaps of length four occur and the anchored gap identity yields \(n/h=4\). If \(r=1\), exactly one unit of slack is distributed among the \(h\) long gaps, giving \(n\) states. If \(r=2\), either \(h\) long gaps share two excess units, or \(h\) long gaps coexist with one short gap of length two; the respective counts are \(n(h+1)/2\) and \(n\). If \(r=3\), the \(h\)-gap case contributes \(n(h+1)(h+2)/6\); the \(h+1\)-gap case (one short gap of length two or three) contributes \(n(h+1)\). Adding these disjoint cases gives the four residue formulas. Their integrality follows from the anchored-gap count, not an external numerical observation.

**4. Total edge count.** Fix a site \(i\) holding a particle, and consider the clockwise move \(i\mapsto i+2\). The five-site block \((i-1,i,i+1,i+2,i+3)\) must equal `01000`. The other \(n-5\) consecutively arranged sites constitute an independent set of a path; their number is \(F_{n-3}\), including the empty path for \(n=5\). There are \(n\) choices of \(i\). Every undirected two-hop edge has exactly one clockwise-oriented representation, since its reverse is counterclockwise for \(n\ge5\). Therefore \(|E(G_n)|=nF_{n-3}\).

**5. Degree-zero coefficient.** A nonempty state has degree zero exactly when all cyclic gaps are two or three. This is equivalent to an inclusion-maximal independent set of the cycle, whose classical Perrin count is \(P_n\). Adding the empty state gives \(D_n(0)=1+P_n\). This identification is a check against established combinatorics, not an originality claim for the Perrin sequence.

## Verification

Run `python3 check.py` with standard Python. It enumerates the actual legal two-hop reconfiguration neighbors directly for every independent set of \(C_n\) with \(5\le n\le20\), and independently constructs the predicted multiplicities from anchored-gap coefficients, checking all individual degrees, total vertices, total edges, degree extrema, and extremal populations. It processed 39,585 independent sets. The same checker numerically tests coefficient, edge and sharp-extremizer identities at sizes through \(n=75\), but these larger tests use the same gap-count formula rather than a separate graph enumeration. Finite verification supports but does not replace the all-length proof above.

## Relationship to prior work

Hatano, Kitamura, Izumi, Ito and Masuzawa (first public version July 16, 2024) study *distance-at-most-two* jumps, allowing one-site moves as well, and investigate decision complexity on graph classes rather than the exact-degree polynomial of the strictly two-site ring model. Avis and Hoang study ordinary *distance-one token sliding*, not the exact two-site rule. The published published-finding corpus finding *Connected maximal-independent-set exchange sectors and exact degree laws on cycles* examines only inclusion-maximal independent sets, with one-delete/one-insert exchanges necessarily equivalent to one-site slides. Its objects have gaps only two or three and therefore lie entirely in the degree-zero sector of the present strictly two-site graph; its nonzero exchange degrees cannot be substituted into this distribution. Other published records on bounded-gap token sliding or minimum isolating sets likewise impose different state restrictions or move rules. The classical Perrin frozen count, Fibonacci cycle-independent-set total, and ordinary circular gap enumeration are explicitly credited as known ingredients.

The new claim is the complete *strictly two-site* degree polynomial across **all** independent sets, the sharp four-residue maximum-degree multiplicities, and the total edge formula. A stronger, unindexed formula for the same exact-hop model may still exist; no claim of historical priority or independent review is made.

## Limitations

The theorem requires \(n\ge5\), labelled simple cycles, nearest-neighbor exclusion, and relocations by exactly two positions. It does not classify connected components, shortest reconfiguration routes, stochastic rates, or any model that permits one-step moves. The formulas are proved by elementary combinatorial argument. Computational checks are finite. A complete historical novelty guarantee cannot be inferred from the searches, and bibliographic coverage of unindexed exact-hop papers remains a risk.

## References

1. H. Hatano, N. Kitamura, T. Izumi, T. Ito, T. Masuzawa, *Independent Set Reconfiguration Under Bounded-Hop Token*, arXiv:2407.11768, first publicly posted 2024-07-16, https://arxiv.org/abs/2407.11768.
2. D. Avis, D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861, first publicly posted 2022-03-31, https://arxiv.org/abs/2203.16861.
3. N. Bousquet, A. E. Mouawad, N. Nishimura, S. Siebertz, *A survey on the parameterized complexity of the independent set and (connected) dominating set reconfiguration problems*, arXiv:2204.10526, https://arxiv.org/abs/2204.10526.
4. *Connected maximal-independent-set exchange sectors and exact degree laws on cycles*, published research record, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-connected-maximal-independent-set-exchange-sectors-and-exact-deg--a5fcb188f118/RESULT.md.
