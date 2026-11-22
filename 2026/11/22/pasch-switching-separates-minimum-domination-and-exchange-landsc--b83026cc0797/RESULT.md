# Pasch switching separates minimum domination and exchange landscapes of the two thirteen-point Steiner designs

## Finding

The two nonisomorphic Steiner triple systems on thirteen points have incidence (Levi) graphs with the **same domination number nine**, as previously known, yet markedly different sets of minimum dominating configurations. For the cyclic system there are **1,456** minimum dominating sets, forming a one-vertex-replacement graph with **2,652 edges** and component-size multiset \(\{676^1,17^{39},1^{117}\}\): one component of size 676, 39 components of size 17, and 117 isolated configurations. No further component isomorphism type is asserted.

For the noncyclic system obtained by one specified Pasch switch, there are **1,511** minimum dominating sets and **3,192** exchange edges. Its component-size multiset is
\[
\{936^1,51^1,48^3,24^6,17^3,13^1,10^9,1^{82}\}.
\]
Consequently the two systems have respectively 157 and 106 exchange components and respectively 117 and 82 isolated optima. The difference between the counts is 55, even though their minimum sizes agree.

In fact, write a minimum dominating set as \(P\cup Q\), where \(P\) is selected point vertices and \(Q\) selected block vertices. Call it **canonical** when \(Q\) consists of exactly the blocks disjoint from \(P\). The complete occupancy census is:

| Point vertices \(|P|\) | Canonical? | Cyclic | Noncyclic |
|---|---|---:|---:|
| 5 | Yes | 195 | 195 |
| 6 | Yes | 624 | 574 |
| 6 | No | 507 | 612 |
| 7 | Yes | 130 | 130 |

All minimum dominating sets fall into these four classes. Thus the difference is concentrated in the six-point sector.

## Assumptions and scope

Fix the labelled ground set \(X=\mathbb Z/13\mathbb Z\). Define the cyclic Steiner system \(\mathcal S_c\) to consist of the 26 cyclic translates of the starter blocks \(\{1,3,9\}\) and \(\{2,5,6\}\). Define \(\mathcal S_n\) by removing the four triples
\[
\{2,4,10\},\;\{2,5,6\},\;\{4,6,12\},\;\{5,10,12\}
\]
and inserting
\[
\{2,4,6\},\;\{2,5,10\},\;\{4,10,12\},\;\{5,6,12\}.
\]
These two designs represent the two isomorphism classes of Steiner triple systems of order thirteen. The explicit families and the Pasch trade are described by Pavone (2023). Each contains exactly 26 blocks, each point lies on six blocks and each unordered pair occurs in one block. The incidence graph \(G(\mathcal S)\) has one vertex for each point or block, and an edge for membership; it has 39 vertices.

A *dominating set* contains or neighbors every vertex. A *minimum* dominating set has the least possible cardinality. The one-vertex-replacement graph \(\mathcal R(\mathcal S)\) has minimum dominating sets as vertices and joins two when their symmetric difference consists of two vertices (one removed, one added). These graphs are undirected; no vertex names or color classes are quotient out by symmetries. All asserted numbers concern this precise finite domain and these explicit definitions.

## Proof

**1. A sharp size bound and forced point range.** Suppose \(D=P\cup Q\) dominates, with \(|P|=p\) and \(|Q|=q\). Each unselected point must belong to a selected block, so \(13-p\le 3q\). For a point set \(P\), write \(t(P)\) for the number of blocks wholly contained in it. By inclusion–exclusion and uniqueness of the block through each pair, the number of blocks meeting \(P\) is exactly
\[
 h(P)=6p-\binom p2+t(P).
\]
Every block disjoint from \(P\) must itself be in \(Q\), so \(26-h(P)\le q\).

There is no dominating set of size at most eight. It is enough to rule out size eight, since any smaller dominating set can be extended to an eight-set. If \(p+q=8\), the point coverage inequality implies \(p\le5\). For \(p\le3\), at most \(6p+q\le 23\) blocks are covered; for \(p=4\), at most \(6p-\binom42+1=19\) blocks meet \(P\), leaving at least seven and hence exceeding \(q=4\). For \(p=5\), at most two distinct blocks can lie fully in \(P\) (two such blocks, if present, intersect in one point); therefore \(h(P)\le30-10+2=22\), leaving at least four disjoint blocks, but \(q=3\). Thus \(\gamma\ge9\).

For the upper bound, take two blocks meeting in exactly one point. Their union \(P\) has five points and contains exactly two full blocks, so exactly four blocks are disjoint from \(P\). Take these four as \(Q\). All block vertices are then dominated. Each point outside \(P\) has six incident blocks and at most five of those can meet \(P\), since every selected point determines at most one such block through the outside point. Hence it meets a block of \(Q\), making \(P\cup Q\) dominating of size nine. Thus \(\gamma=9\). Applying the two coverage inequalities to a size-nine solution yields \(5\le p\le7\).

**2. Complete characterization of candidates.** For fixed \(P\subseteq X\) and selected block family \(Q\), domination is *equivalent* to
\[
 \{B\in\mathcal S:B\cap P=\varnothing\}\subseteq Q,
 \qquad P\cup\bigcup_{B\in Q}B=X.
\]
The first condition dominates every block vertex, and the second dominates every point vertex. Together with \(|P|+|Q|=9\) and \(5\le|P|\le7\), this is an exhaustive, decidable characterization with no omitted cases.

For \(p=5\), the bound above forces exactly two full blocks in \(P\), hence \(P\) is the union of two intersecting triples; all four disjoint blocks are forced. There are \(13\binom62=195\) possibilities, all valid. For \(p=7\), there are exactly two selected blocks, whose union must contain all six unselected points, so they must be disjoint and \(P\) is their complement. Every other block meets \(P\) because a third triple inside a union of two disjoint triples would meet one of them in at least two points, contradicting pair uniqueness. Exactly \(\binom{26}{2}-13\binom62=130\) disjoint pairs exist, giving precisely 130 canonical seven-point solutions.

**3. The six-point census and exchange graph.** The remaining cases have six selected points and three selected blocks. Both attached standalone programs enumerate them using the equivalence in step 2: `verify_p_first.py` enumerates all \(2^{13}\) point subsets and the required/optional blocks; `verify_q_first.cpp` chooses each two-, three-, or four-block family first, then tests all point subsets of the required size. Neither implementation samples states or treats partial enumeration as exhaustive. Both independently check each design's pair counts, construct all nine-vertex dominating sets and compare full 39-bit state lists. The programs independently establish the displayed four-class counts, edge totals and connected-component sizes by checking all exactly-one-replacement pairs and traversing the resulting finite graphs.

## Verification

Reproduce with standard Python 3 and a C++17 compiler:

```sh
python3 verify_p_first.py
g++ -std=c++17 -O2 verify_q_first.cpp -o verify_q_first
./verify_q_first | grep -v '^@'
```

Both programs assert all stated solution counts, canonical class counts, exchange-edge counts, and component multiplicities. In the full replay, the independently generated state sets were also compared mask by mask and agreed exactly: 1,456 cyclic masks and 1,511 noncyclic masks. The Python verifier reports SHA-256 of the lexicographically sorted mask list (ten lowercase hexadecimal digits per mask, followed by newline):

- Cyclic: `5590a58180c3b68c5907c93ae101fa56d51ec9df91744a5fd777d9e945bf72e1`
- Noncyclic: `6461144eda33c6c59b06632c3d299f17d728381d8264e490ec4ee41fb855e009`

Both verifiers require no external data or third-party libraries. The proof of completeness comes from the domain reduction and the exhaustive loops in those programs, **not** from a test log alone. Independent scholarly verification remains outstanding.

## Relationship to prior work

Goldberg, Rajendraprasad and Mathew (arXiv:1405.3436v1, 14 May 2014, Section 7) reported domination number nine for both thirteen-point Steiner triple systems, and studied the structure of dominating sets. That known scalar invariant is not new. Tang and Zhou (arXiv:1603.07398v1, 24 March 2016) developed general domination-number conditions for block designs, not these complete configuration or exchange counts. Pavone's 2023 graphical presentation specifies the two nonisomorphic designs and the Pasch trade used here; the 2023 work is a structural reference, **not** used as the first qualifying archival date. The current results distinguish the two types at the level of all minimum sets and single-replacement dynamics, rather than their common minimum size.

## Limitations

The findings concern only the two thirteen-point Steiner triple systems, not all Steiner triple systems or arbitrary block designs. Component *sizes* are determined; finer abstract isomorphism types of nontrivial exchange components are not claimed. The exhaustive computations constitute a finite proof for the labelled incidence graphs after checking both systems satisfy the Steiner pair property. Searches and inspected primary articles found no preceding statement implying the exact numbers, but unindexed enumerations and uninspected relevant historical results remain a priority risk. No independent scholarly audit has occurred.

## References

1. F. Goldberg, D. Rajendraprasad and R. Mathew, *Domination in designs*, arXiv:1405.3436v1 (first public 14 May 2014). https://arxiv.org/html/1405.3436v1
2. L. Tang and S. Zhou, *Domination number in block designs*, arXiv:1603.07398v1 (24 March 2016). https://arxiv.org/abs/1603.07398
3. M. Pavone, *A visual representation of the Steiner triple systems of order 13*, 2023, DOI: 10.26493/2590-9770.1564.2b8. https://iris.unipa.it/retrieve/674a8990-dc17-457f-b6b2-f2261c09ebde/Picture%20STS%2813%29_2023_01_05.pdf
