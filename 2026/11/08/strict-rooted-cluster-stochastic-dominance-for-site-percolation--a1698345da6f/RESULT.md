# Strict rooted-cluster stochastic dominance for site percolation on two cospectral networks

## Finding

Let \(R=K_4\square K_4\) be the sixteen-vertex rook graph and let \(S\) be the Shrikhande graph. Retain each vertex independently with the same probability \(p\in[0,1]\). Fix any vertex \(o\). Write \(X_G\) for the number of retained vertices in the component of \(o\) in the induced retained subgraph of \(G\); set \(X_G=0\) when \(o\) is absent. Then

\[
\Pr(X_S\ge t)\ge\Pr(X_R\ge t)
\quad\text{for every integer }t\text{ and }0\le p\le1.
\]

For \(0<p<1\), the inequality is **strict exactly for** \(t\in\{4,5,6,7,8\}\) and is equality for all other integer thresholds. The stronger fixed-population statement holds: if exactly \(k\) of the sixteen sites are retained uniformly, the Shrikhande rooted-cluster size first-order stochastically dominates the rook rooted-cluster size for every \(0\le k\le16\). Its exact nonzero tail-coefficient differences are recorded below.

As a consequence, the *unconditional* mean rooted-cluster size obeys the exact positive identity (write \(q=1-p\))

\[
\begin{aligned}
\mathbb E X_S-\mathbb E X_R
&=12p^4q^{12}+96p^5q^{11}+234p^6q^{10}\\
&\quad+126p^7q^9+24p^8q^8.
\end{aligned}
\]

Both graphs have the same strongly regular parameters \((16,6,2,2)\) and hence the same adjacency spectrum \(6^1,2^6,(-2)^9\). Thus this strict percolation order is not determined by those common spectral data.

## Assumptions and scope

Write the common vertex set as \(V=\mathbb Z_4\times\mathbb Z_4\), with \(o=(0,0)\). In \(R\), distinct vertices are adjacent when their first or second coordinates coincide. In \(S\), vertices are adjacent when their difference belongs to \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\), with arithmetic modulo four. These definitions fix simple undirected graphs, not edge-percolation networks. The claim covers every independent common site-retention probability \(p\), all integer thresholds, and all choices of root by coordinate-translation symmetry.

We distinguish the *canonical independent-site ensemble* from the *microcanonical ensemble*, in which precisely \(k\in\{0,\ldots,16\}\) retained vertices are sampled uniformly. No infinite-graph critical threshold or thermodynamic limit is asserted.

## Proof

For \(G\in\{R,S\}\), define the nonnegative integer array

\[
H_G(k,s)=\#\{A\subseteq V:|A|=k,\;|C_G(o;A)|=s\},
\quad 0\le k,s\le16,
\]

where \(C_G(o;A)\) is the connected component of \(o\) in \(G[A]\), or empty when \(o\notin A\). In particular \(H_G(k,0)=\binom{15}{k}\). All rows sum to \(\binom{16}{k}\).

For an occupied root component to equal a specified nonempty connected vertex set \(U\ni o\), every vertex of \(U\) must be retained and every vertex of its *external vertex boundary* \(\partial_G U=\{v\in V\setminus U: v\text{ has a neighbor in }U\}\) must be absent. The remaining \(16-|U|-|\partial_GU|\) sites are unrestricted. Consequently, with an out-of-range binomial coefficient interpreted as zero, the exact finite formula is

\[
H_G(k,s)=\sum_{\substack{U\ni o,\ |U|=s\\G[U]\text{ connected}}}
\binom{16-s-|\partial_GU|}{k-s},\quad s\ge1.
\]

Exhaustive evaluation of this finite sum produces the following **complete signed difference** \(\Delta H(k,s)=H_S(k,s)-H_R(k,s)\). Every unlisted entry of the entire \(17\times17\) matrix is exactly zero:

| \(k\) | Nonzero entries \((s,\Delta H(k,s))\) |
|---:|---|
| 4 | \((3,-12),(4,12)\) |
| 5 | \((3,-36),(4,-24),(5,60)\) |
| 6 | \((3,-36),(4,-48),(5,-30),(6,114)\) |
| 7 | \((3,-12),(4,-24),(6,-6),(7,42)\) |
| 8 | \((4,-6),(8,6)\) |

The counts are exact integers, not Monte Carlo estimates. Three standard-library Python files in this package independently enumerate: (i) every one of the \(2^{16}=65536\) retained-site masks by graph traversal; (ii) connected rooted candidate components \(U\) using the displayed boundary formula; and (iii) entry-by-entry equality of the two \(17\times17\) arrays. Both algorithms explicitly generate the two graph adjacency rules and are finite complete enumerations, not sampling.

Put \(D_{k,t}=\sum_{s\ge t}\Delta H(k,s)\). The table of all nonzero rows or columns of \(D\) is

| \(t\) | \(D_{4,t}\) | \(D_{5,t}\) | \(D_{6,t}\) | \(D_{7,t}\) | \(D_{8,t}\) |
|---:|---:|---:|---:|---:|---:|
| 4 | 12 | 36 | 36 | 12 | 0 |
| 5 | 0 | 60 | 84 | 36 | 6 |
| 6 | 0 | 0 | 114 | 36 | 6 |
| 7 | 0 | 0 | 0 | 42 | 6 |
| 8 | 0 | 0 | 0 | 0 | 6 |

All other \(D_{k,t}\) vanish. Therefore \(D_{k,t}\ge0\) for all \(k,t\), proving the microcanonical stochastic order after division by \(\binom{16}{k}\). In the Bernoulli-site ensemble,

\[
\Pr(X_S\ge t)-\Pr(X_R\ge t)
=\sum_{k=0}^{16}D_{k,t}p^k(1-p)^{16-k}.
\]

Every summand is nonnegative on \([0,1]\); for \(0<p<1\), a positive term exists exactly for the five thresholds in the table. At \(p=0\) or \(p=1\) both induced retained graphs have identical root-component size (respectively zero or sixteen), giving equality. This proves the stated strictness and endpoint cases.

Finally, \(\mathbb E X_G=\sum_{k,s}sH_G(k,s)p^kq^{16-k}\). Weighting the five signed rows by \(s\) gives precisely \(12,96,234,126,24\), proving the stated mean difference. The common strongly regular parameters follow directly by checking each of the sixteen neighborhoods has six vertices and any two distinct neighborhoods intersect in exactly two vertices; the adjacency identity \(A^2=4I+2\mathbf1\mathbf1^{\mathsf T}\) gives the quoted shared spectrum.

## Verification

Run `python3 verify_all.py` from a directory containing the three files `verify_all.py`, `verify_masks.py`, and `verify_boundaries.py`; all use only the Python standard library. The complete integer matrices used by both methods are also in `microcanonical_histograms.json`. The two individual checkers may be run separately. The scripts verify the strongly regular parameters, every row sum \(\binom{16}{k}\), the entire signed histogram, every integer tail coefficient, and the complete agreement of independent traversals and boundary sums. At \(p=1/2\), the exact difference of means is \(492/65536=123/16384\), a direct check using all equally likely site masks.

## Relationship to prior work

Newman and Ziff, *A fast Monte Carlo algorithm for site or bond percolation* (arXiv:cond-mat/0101295, first posted 2001-01-18), explain the fixed-number-of-occupied-sites to independent-site binomial mixing and a practical cluster-tracking method. They do not evaluate the two present sixteen-site graphs or compare their root-component size distributions. Diskin and Krivelevich, *Site Percolation on Pseudo-Random Graphs* (arXiv:2107.13326), establish large-network percolation estimates; their asymptotic hypotheses and conclusions do not imply the finite exact uniform order established here. Huang et al., *Going Deeper into Permutation-Sensitive Graph Neural Networks* (arXiv:2205.14368), explicitly distinguish the rook and Shrikhande graphs by their number of four-cliques; this graph-theoretic separation does not by itself evaluate their site-percolation laws or prove all-parameter first-order stochastic dominance. The basic graph pair and spectrum were already known and are not claimed as new.

## Limitations

The result concerns these two specified sixteen-vertex graphs under independent *site* percolation, not bond percolation, arbitrary nonuniform site probabilities, large-system limits, nor a general extremal principle over all cospectral graphs. Only the explicit signed coefficients and the resulting stochastic order are proposed as a new finding. A prior unindexed table of rooted connected-subset boundary counts or exact percolation data could contain an equivalent evaluated claim; exhaustive novelty is not provable by searching. No independent scientific review has yet been performed.

## References

- M. E. J. Newman and R. M. Ziff, *A fast Monte Carlo algorithm for site or bond percolation*, arXiv:cond-mat/0101295 (v1, 2001-01-18). https://arxiv.org/html/cond-mat/0101295v2
- S. Diskin and M. Krivelevich, *Site Percolation on Pseudo-Random Graphs*, arXiv:2107.13326 (v1, 2021-07-28). https://arxiv.org/abs/2107.13326
- Z. Huang, Y. Wang, C. Li, and H. He, *Going Deeper into Permutation-Sensitive Graph Neural Networks*, arXiv:2205.14368 (v1, 2022-05-28), Appendix I. https://arxiv.org/abs/2205.14368
- A. E. Brouwer, *Shrikhande* (graph data and spectral parameters, referencing S. S. Shrikhande's 1959 classification). https://aeb.win.tue.nl/drg/graphs/Shrikhande.html
