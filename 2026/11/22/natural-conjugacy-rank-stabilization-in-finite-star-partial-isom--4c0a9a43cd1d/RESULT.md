# Natural-conjugacy rank stabilization in finite star partial-isometry monoids

## Finding
Let \(m\ge2\), let \(K_{1,m}\) be the metric star with hub \(0\) and \(m\) leaves, and let \(S_m\) be its inverse monoid of all distance-preserving partial bijections. Define \(c_{m,r}\) to be the number of \(i\)-conjugacy classes of domain rank \(r\), where \(a\sim_i b\) means that there is \(g\in S_m\) satisfying \(g^{-1}ag=b\) and \(gbg^{-1}=a\). The complete class-rank polynomial is

\[
C_m(z)=\sum_{r=0}^{m+1}c_{m,r}z^r=(1+z)\sum_{s=0}^{m}[u^s]F(u,z)+2z^2,
\]
\[
F(u,z)=\prod_{j\ge1}(1-u^jz^j)^{-1}\prod_{j\ge2}(1-u^jz^{j-1})^{-1}.
\]
The expressions are formal series; only support degrees at most \(m\) are used. In particular, if \(p_2(m)\) counts ordered pairs of integer partitions of total size \(m\), then
\[
\#(S_m/\!\sim_i)=C_m(1)=2p_2(m)+2,
\quad p_2(m)=[u^m]\prod_{j\ge1}(1-u^j)^{-2}.
\]
For every fixed rank \(r\ge1\), the class count stabilizes **sharply** when the number of leaves reaches \(2r\):
\[
 c_{m,r}=[z^r]\left((1+z)\prod_{j\ge1}(1-z^j)^{-2}+2z^2\right)
 \quad(m\ge2r),
\]
\[
 c_{2r,r}-c_{2r-1,r}=1.
\]
At \(m=1\) the polynomial is \(1+2z+2z^2\) (the symmetric inverse monoid on two points).

The theorem also classifies and sizes *every* conjugacy class. Write a leaf partial injection as a disjoint union of \(a_j\) directed cycles on \(j\) vertices (\(j\ge1\)) and \(b_j\) directed paths on \(j\) vertices (\(j\ge2\)); a path includes its two endpoints and has \(j-1\) arrows. Let
\[
s=\sum_{j\ge1}ja_j+\sum_{j\ge2}jb_j,
\qquad r=\sum_{j\ge1}ja_j+\sum_{j\ge2}(j-1)b_j,
\]
\[
N_m(\boldsymbol a,\boldsymbol b)=
\frac{m!}{(m-s)!\prod_{j\ge1}j^{a_j}a_j!\prod_{j\ge2}b_j!},\qquad s\le m.
\]
The following is the disjoint class taxonomy. Every leaf-only cycle/path profile is one class, with size \(N_m\), **except** the single one-cycle profile: that class also contains the hub singleton identity and has size \(m+1\). Every **nonempty** leaf profile has another class obtained by adjoining a fixed hub, with size \(N_m\). Besides these there are exactly three hub-moving classes: the one-arrow hub–leaf partial maps, of size \(2m\) and rank one; the hub–leaf transpositions, of size \(m\) and rank two; and the directed three-vertex paths through the hub, of size \(m(m-1)\) and rank two. The empty leaf-only profile represents the zero map.

## Assumptions and scope
The graph metric is \(d(x,x)=0\), \(d(0,i)=1\) for any leaf \(i\), and \(d(i,j)=2\) for distinct leaves. Partial maps may have empty domain. Rank means domain cardinality, not support cardinality. Natural conjugacy here means the explicitly symmetric inverse-semigroup \(i\)-conjugacy, not merely conjugacy by the unit group, primary conjugacy, or agreement of cycle types in the ambient symmetric inverse monoid. Every equality of formal series is coefficientwise, and the stabilization statement concerns ranks \(r\ge1\).

## Proof
**1. Metric-span conjugacy lemma.** For a partial bijection \(a\), let \(\operatorname{sp}(a)=\operatorname{dom}(a)\cup\operatorname{im}(a)\). The two conjugacy identities imply that the conjugator and its inverse are defined on the relevant spans and restrict to a bijective isometry \(\operatorname{sp}(b)\to\operatorname{sp}(a)\) intertwining all directed arrows. Conversely, an isometry of spans that intertwines the arrows, regarded as a partial isometry with exactly this domain, satisfies both conjugacy identities. Thus \(i\)-classes are exactly *isometric directed cycle/path diagrams on their spans*. In particular, the zero map has its own class, and unused vertices outside the span do not enter the type.

**2. Star-specific admissible diagrams.** If the hub is absent from the span, every partial injection on leaves is an isometry, because all distinct leaves are at distance two. If the hub is a fixed point, its union with any leaf partial injection is an isometry. For a map moving the hub, distinguish rank one, giving an arrow in either direction between the hub and one leaf, from rank two. At rank two, an isometry with hub in both domain and image that moves the hub has either a hub–leaf transposition (same leaf) or a path from one leaf through the hub to a different leaf. A moving hub cannot occur at rank at least three: a domain containing the hub and at least two leaves has a uniquely distinguished hub, as does its image, so every isometry fixes the hub. A rank-two map with the hub appearing at only one end of an arrow cannot have another arrow, since the two domain vertices would have distance one but two leaf images would have distance two (or the inverse contradiction). Hence the listed families exhaust all possibilities.

**3. Which diagrams merge?** The metric on two distinct leaves is two, whereas on a hub–leaf pair it is one. An isometry of a span with at least three points that includes a hub must carry that uniquely central point to the hub; in the two-point hub–leaf case swapping the two points is permitted. Accordingly, leaf-only types cannot merge with hub-fixed types of nonempty leaf support. The two orientations of the rank-one hub–leaf arrow merge; so do all placements of a hub in the two-vertex transposition, and all ordered choices of the two distinct leaves on a length-three path. The singleton fixed point is the unique exception to the leaf-only/hub-fixed separation, because all singleton metric spaces are isometric. The metric-span lemma now proves exactly the claimed taxonomy.

**4. Sizes and generating function.** A cycle on \(j\) labeled leaves has \(j\) cyclic presentations of the same directed cycle; a directed path has no orientation-reversal symmetry. Permuting equal components yields the remaining factorial divisors. Therefore a prescribed leaf profile has precisely \(N_m(\boldsymbol a,\boldsymbol b)\) labeled realizations. The hub-fixed copy has the same size; the special classes have sizes \(2m\), \(m\), and \(m(m-1)\), and the fixed singleton class contains all \(m+1\) singleton identities. Cycles and paths contribute factors \((1-u^jz^j)^{-1}\) and \((1-u^jz^{j-1})^{-1}\), respectively. Summing leaf-only profiles through support size \(m\), duplicating every nonempty profile with a fixed hub, and correcting the singleton and three exceptional hub-moving classes yields
\[
F_m(z)+z(F_m(z)-1)+z+z^2+z^2=(1+z)F_m(z)+2z^2,
\]
where \(F_m(z)=\sum_{s=0}^m[u^s]F(u,z)\). This calculation requires \(m\ge2\), since the three-vertex path requires distinct leaves.

**5. Partition and sharp stability.** Setting \(z=1\) gives
\[
F(u,1)=(1-u)\prod_{j\ge1}(1-u^j)^{-2}.
\]
Hence \(\sum_{s=0}^m[u^s]F(u,1)=p_2(m)\), proving the scalar formula. For a leaf diagram of rank \(r\), every directed path has at least one arrow and at most one more vertex than arrows, so its span contains at most \(2r\) vertices; equality forces exactly \(r\) disjoint one-arrow paths and no cycles. A hub-fixed diagram of rank \(r\) uses a leaf diagram of rank \(r-1\), hence at most \(2r-2\) leaves. The hub-moving classes have stabilized already for \(m\ge2\). Consequently, rank-\(r\) counts are constant once \(m\ge2r\), while exactly one new leaf-only profile enters at \(m=2r\): the union of \(r\) disjoint one-arrow paths. Letting the support bound go to infinity in a fixed rank coefficient replaces the cycle factor and path factor by the same partition product \(\prod_{j\ge1}(1-z^j)^{-1}\). This gives the displayed stable coefficient and proves sharpness, including \(r=1\).

## Verification
The included `verify.py` enumerates the actual partial distance isometries on stars with one through four leaves and computes the symmetric \(i\)-conjugacy relation directly using both conjugation equations, not inferred cycle types. Its observed class-rank distributions are, respectively,

| Leaves | Class counts in increasing rank |
|---:|---|
| 1 | 1, 2, 2 |
| 2 | 1, 3, 6, 2 |
| 3 | 1, 3, 8, 7, 3 |
| 4 | 1, 3, 9, 12, 12, 5 |

The same executable independently checks the full multiset of conjugacy class sizes for those cases, the partition identity through twelve leaves, and sharp rank stabilization for ranks one through five. Run `python3 verify.py` with the Python 3 standard library. These finite checks are corroborative; the preceding proof is uniform in \(m\).

## Relationship to prior work
Fernandes and Paulista, *On the monoid of partial isometries of a finite star graph* (first arXiv posting 2022-03-10, arXiv:2203.05504), give the four-family element decomposition, Green relations, a presentation and cardinality. Araújo, Kinyon and Konieczny, *Conjugacy in inverse semigroups* (first arXiv posting 2018-10-07, arXiv:1810.03208), establish the cycle-chain criterion and the two-partition count for the full symmetric inverse monoid. Araújo et al., *Conjugacy in Semigroups: the Partition and Brauer Diagram Monoids, Conjugacy Growth, and Partial Inner Automorphisms* (2023-01-11, arXiv:2301.04252), establish equality of natural conjugacy and \(i\)-conjugacy for inverse semigroups. The partial-star result uses these structural inputs, but additionally requires a metric-span analysis to determine which classes split or fuse, all three moving-hub class sizes, the rank polynomial, and exact rank-stabilization threshold. No claim is made to originate the source decomposition, general conjugacy notion, or partition theorem.

## Limitations
The formula concerns natural \(i\)-conjugacy, not ordinary unit conjugacy, and the metric is the graph metric of an unweighted star. The exceptional count changes at one leaf. The calculation does not establish analogous formulas for weighted stars, double stars or arbitrary trees. Although targeted searches did not uncover an existing star-specific conjugacy classification with this exact rank polynomial, an equivalent specialization or unpublished formula could exist; independent literature and mathematical review remain outstanding.

## References
1. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a finite star graph*, arXiv:2203.05504 (2022-03-10), https://arxiv.org/abs/2203.05504.
2. J. Araújo, M. Kinyon and J. Konieczny, *Conjugacy in inverse semigroups*, arXiv:1810.03208 (2018-10-07), https://arxiv.org/abs/1810.03208.
3. J. Araújo, W. Bentz, M. Kinyon, J. Konieczny, A. Malheiro and V. Mercier, *Conjugacy in Semigroups: the Partition and Brauer Diagram Monoids, Conjugacy Growth, and Partial Inner Automorphisms*, arXiv:2301.04252 (2023-01-11), https://arxiv.org/abs/2301.04252.
