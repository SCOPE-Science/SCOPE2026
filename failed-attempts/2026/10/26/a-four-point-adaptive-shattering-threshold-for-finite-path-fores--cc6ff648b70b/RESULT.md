# A four-point adaptive-shattering threshold for finite path-forest betweenness

## Finding
Let \(V\) be a finite labeled set with a **known** partition \(\mathcal B\), every block having between one and five vertices. For each block, choose a simple undirected path on precisely that block's vertices, and let \(F\) be the disjoint union of these paths. A hypothesis \(h_F\) assigns to a strict ternary query \((a,b,c)\) the bit \(1\) when the three vertices are distinct and \(b\) lies on the unique path in \(F\) between \(a\) and \(c\); otherwise it assigns \(0\). The set of all such hypotheses, with the fixed partition of component vertex sets, is \(\mathcal H(\mathcal B)\).

Write \(m_j\) for the number of blocks of size \(j\). Then, for all such partitions, without a bound on the total number of vertices,
\[
\operatorname{VCdim}(\mathcal H(\mathcal B))=m_3+2m_4+4m_5,
\qquad
\operatorname{Ldim}(\mathcal H(\mathcal B))=m_3+3m_4+5m_5.
\]
Therefore
\[
\operatorname{Ldim}(\mathcal H(\mathcal B))-
\operatorname{VCdim}(\mathcal H(\mathcal B))=m_4+m_5.
\]
In particular, four vertices are the first possible component size giving a strict gap, and \(m\) disjoint four-vertex path components give dimensions \(2m\) and \(3m\), for every \(m\ge1\). This is an unbounded gap for a class of finite, disconnected path-forest betweenness structures with prescribed component supports.

## Assumptions and scope
All graphs are finite, simple, and undirected. A one-vertex block contributes one trivial path, a two-vertex block one edge, and a block of size \(j\ge3\) contributes a labeled undirected path, identified with a linear permutation modulo reversal. The component vertex sets are known in advance but their paths are not; varying the component partition itself defines a different concept class and is **not** addressed here. All ordered triples of pairwise distinct vertices are allowed as queries; reversing the two endpoints does not change the answer. Triples spanning distinct blocks are constantly false. Static shattering means all binary labels on a fixed set of queries are realized. Online (Littlestone) shattering means that a complete binary tree of instances has every labeled root-to-leaf path realized by a hypothesis. Dimensions of a singleton concept class are zero.

## Proof
**1. Local hypotheses and query reduction.** On \(j\) distinct vertices, an undirected path is encoded by a permutation and its reversal, so there are \(j!/2\) distinct hypotheses for \(j\ge2\), and one for \(j=1\). A nonconstant strict-betweenness query is uniquely represented by a triple with a specified middle vertex and an unordered pair of endpoints. Hence there are exactly \(3\binom j3\) nonredundant local binary coordinates. These two enumerations exhaust all possibilities, not merely a sample.

**2. Exact local dimensions for \(1\le j\le5\).** The table below is proved by the complete, standalone certificate `finite_betweenness_certificate.json`, constructed by `generate_certificate.py` and checked by an independently written program `verify_betweenness.py`:

| \(j\) | Number of paths | Number of distinct triple queries | VC dimension | Littlestone dimension |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 |
| 2 | 1 | 0 | 0 | 0 |
| 3 | 3 | 3 | 1 | 1 |
| 4 | 12 | 12 | 2 | 3 |
| 5 | 60 | 30 | 4 | 5 |

For each \(j\), the certificate supplies the fixed set of \(v_j\) VC queries and, for every one of its \(2^{v_j}\) bit strings, a path realizing that string. Its upper-bound verification independently enumerates all \(\binom{3\binom j3}{v_j+1}\) possible sets of \(v_j+1\) nonredundant queries and establishes that none is shattered. For \(j=3,4,5\), these are respectively \(3\), \(220\), and \(142506\) sets. The larger query sets then cannot be shattered by heredity. For \(j=1,2\) there are no nonconstant queries. These checks prove both lower and upper VC bounds.

For Littlestone dimension, the same certificate supplies full binary adaptive query trees of depths \(0,0,1,3,5\), with one **explicit path witness per leaf**. The independent verifier recomputes each strict-betweenness answer along every root-to-leaf path; there are respectively \(1,1,2,8,32\) leaves. Conversely, any complete depth-\(d\) shattered tree needs \(2^d\) distinct hypotheses. The counts \(1,1,3,12,60\) are strictly less than the next powers of two after the listed depths. Thus these constructed depths attain the information-theoretic upper bound. No finite enumeration is extrapolated to arbitrary component size.

**3. Additivity.** When the component-support partition is fixed, every cross-component triple is constantly false. Every remaining nonconstant query belongs to exactly one block. Every arbitrary choice of local paths occurs as a global hypothesis; hence the local hypothesis spaces combine as a Cartesian product over disjoint nonconstant query domains. For VC dimension, a globally shattered query set restricts to a shattered set in each block, and the union of local shattered query sets is shattered by independent choices of local paths. Thus the VC dimensions add.

For Littlestone dimension, local shattered trees may be concatenated, giving the lower bound by the sum of the depths. For the reverse inequality, consider a nonempty product version space and the sum \(D\) of the Littlestone dimensions of its local factors. A nonconstant query acts in one factor. By the defining maximum-minimum recursion for Littlestone dimension, at least one nonempty answer branch of that local factor has dimension strictly lower than before (otherwise a depth one larger than its dimension would be shattered). Therefore on at least one branch the product potential drops by at least one; induction on \(D\) rules out a complete shattered tree deeper than \(D\). This proves equality and all three displayed formulas.

## Verification
Run `python3 generate_certificate.py` to regenerate `finite_betweenness_certificate.json`; then run `python3 verify_betweenness.py finite_betweenness_certificate.json`. The verifier uses a separately written canonicalization of all labeled paths, checks every VC trace witness, exhausts all candidate query sets of one more than the stated VC dimension, independently evaluates all paths along every adaptive certificate branch, and checks the entropy upper bound from the number of distinct hypotheses. The recorded output is in `verification_output.txt` and finishes with `BETWEENNESS_CERTIFICATES_ALL_PASS`. The logical disjoint-product additivity and unrestricted \(m\)-block assertion are proved above, not inferred from computer runs.

## Relationship to prior work
Courcelle, *Axiomatizations of betweenness in order-theoretic trees* (arXiv:2004.10127; first public posting 2020-04-21), develops axioms, structural classes, and first-order/monadic-second-order definability for ternary tree betweenness. Its line-betweenness definition agrees with the present local relation but its main theorems do not determine VC or Littlestone dimensions. Avdiukhin et al., *Tree Learning: Optimal Sample Complexity and Algorithms* (arXiv:2302.04492; 2023-02-09), study **rooted hierarchical-tree odd-one-out labels**, rather than binary strict-between membership for paths, and prove broad Natarajan/Littlestone learning bounds. Chase, Freitag and Reyzin, *Applications of Littlestone dimension to query learning and to compression* (arXiv:2310.04812; 2023-10-07), prove general query-learning/compression results rather than betweenness component profiles. Distinctness of the query semantics matters: ternary odd-one-out for rooted trees and pairwise permutation comparisons are not automatically interchangeable with path betweenness. The static/online product additivity used here is a general fact and is not claimed as new. A targeted comparison with accessible published records found no statement implying the five local dimension values and the resulting prescribed-component formula; it is not a proof of historical uniqueness.

## Limitations
The exact formula is restricted to **known component supports of sizes at most five**. It does not give the dimension of the class of all path forests when component supports vary, the class of connected paths of arbitrary size, rooted hierarchical-tree triplet labels, or unknown graph topology. The finite certificate is complete only for the explicitly stated local sizes; it is not a universal computation. Literature searches cannot exclude equivalent unindexed results. Independent external scientific review has not been performed.

## References
1. B. Courcelle, *Axiomatizations of betweenness in order-theoretic trees*, arXiv:2004.10127v1 (2020-04-21), https://arxiv.org/html/2004.10127v4 .
2. D. Avdiukhin, G. Yaroslavtsev, D. Vainstein, O. Fischer, S. Das and F. Mirza, *Tree Learning: Optimal Sample Complexity and Algorithms*, arXiv:2302.04492v1 (2023-02-09), https://arxiv.org/pdf/2302.04492 .
3. H. Chase, J. Freitag and L. Reyzin, *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812v1 (2023-10-07), https://arxiv.org/html/2310.04812v1 .
