# Minimal forts and the complete zero forcing spectrum of crown graphs

## Finding

For every integer \(n\ge 3\), let \(H_n=K_{n,n}-M_n\) be the crown graph with vertex classes \(A=\{A_i:i\in[n]\}\) and \(B=\{B_i:i\in[n]\}\), where \(A_iB_j\) is an edge precisely when \(i\ne j\). The complete family of inclusion-minimal forts is
\[
\mathscr F_n=\big\{\{A_i,A_j,A_k\},\{B_i,B_j,B_k\}:i<j<k\big\}\,\cup\,
\big\{\{A_i,A_j,B_i,B_j\}:i<j\big\}.
\]
In particular, \(|\mathscr F_n|=2\binom n3+\binom n2\), and all its members have size three or four.

A set \(S\subseteq V(H_n)\) is standard zero forcing if and only if its complement contains at most two vertices of each bipartition class and, when two vertices of each class are omitted, the two omitted index-pairs are distinct. The full zero forcing polynomial is consequently
\[
\begin{aligned}
\mathcal Z_n(z)&=\sum_{\substack{S\subseteq V(H_n)\\S\text{ zero forcing}}}z^{|S|}\\
&=\binom n2\!\left(\binom n2-1\right)z^{2n-4}
+n^2(n-1)z^{2n-3}+n(2n-1)z^{2n-2}+2nz^{2n-1}+z^{2n}.
\end{aligned}
\]
Thus \(Z(H_n)=2n-4\), and there are exactly \(\binom n2(\binom n2-1)\) minimum forcing sets. The inclusion-maximal failed forcing sets are exactly the complements of the members of \(\mathscr F_n\): exactly \(2\binom n3\) have size \(2n-3\), and \(\binom n2\) have size \(2n-4\).

The maximum number of pairwise disjoint forts and the fractional zero forcing number satisfy
\[
\operatorname{ft}(H_n)=\left\lfloor\frac{2n}{3}\right\rfloor,
\qquad Z^*(H_n)=\frac{2n}{3}.
\]
For \(n\ge4\), the unique optimal fractional fort-transversal weighting assigns \(1/3\) to every vertex. The zero-forcing-to-fractional integrality ratio is \(Z(H_n)/Z^*(H_n)=3-6/n\), tending to three.

## Assumptions and scope

Graphs are finite, undirected and simple. The result concerns only the standard zero forcing rule: a blue vertex with exactly one white neighbor may color that neighbor blue. A nonempty vertex set \(F\) is a *fort* if every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A fort is *minimal* under set inclusion when it has no proper nonempty subset that is a fort. A *failed* initial blue set cannot force the entire graph.

The fort number \(\operatorname{ft}(G)\) is the largest number of pairwise disjoint nonempty forts. Fractional zero forcing \(Z^*(G)\) is the minimum sum \(\sum_{v\in V(G)}w_v\) over nonnegative real weights obeying \(\sum_{v\in F}w_v\ge1\) for each inclusion-minimal fort \(F\). It is the fractional transversal number of the minimal-fort hypergraph, not the similarly named fractional parameter defined through a three-color forcing game.

## Proof

**1. Fort classification.** Write \(X=\{i:A_i\in F\}\), \(Y=\{i:B_i\in F\}\). For every \(i\notin X\) and \(j\notin Y\), the corresponding numbers of neighbors in \(F\) are exactly
\[
|N(A_i)\cap F|=|Y|-\mathbf1_{i\in Y},\qquad
|N(B_j)\cap F|=|X|-\mathbf1_{j\in X}.
\]
Every triple from a single vertex class is a fort, since each external vertex of the other class sees at least two members of that triple. Therefore a minimal fort containing at least three vertices from one class must be precisely a pure triple, because that triple is already a fort.

Now suppose \(|X|,|Y|\le2\). If \(|Y|=2\), then any index \(i\in Y\setminus X\) would provide a vertex \(A_i\notin F\) with exactly one neighbor in \(F\). Hence \(Y\subseteq X\). Symmetrically, \(|X|=2\) entails \(X\subseteq Y\). Consequently, if either class contributes two vertices to such a fort, both must contribute two and \(X=Y\). These configurations are forts: each external vertex sees exactly two members, and no proper subset can be a fort by the just-derived restrictions and the singleton cases below.

It remains to rule out \(|X|,|Y|\le1\). A nonempty configuration with only one class represented gives some external opposite-class vertex exactly one neighbor, because \(n\ge3\). If both classes contribute one vertex, then an index outside \(X\cup Y\) exists and the corresponding external vertex of either class sees exactly one member of \(F\). The empty configuration is excluded by definition. This proves the list and its minimality.

**2. Forcing and enumeration.** An initial blue set \(S\) can never force into a fort disjoint from \(S\): while the entire fort stays white, no external blue vertex sees exactly one white neighbor inside it. Conversely, if a process stops with nonempty white set \(W\), every blue vertex has a number of white neighbors different from one, so \(W\) is a fort. Thus \(S\) is zero forcing exactly when it meets every minimal fort.

Put \(X=A\setminus S\) and \(Y=B\setminus S\), now denoting omitted vertices by their index sets. Meeting all pure triples is exactly \(|X|,|Y|\le2\). Under these restrictions, failing to meet a four-element matched-pair fort is possible exactly when \(X=Y\) and both have size two. Therefore the generating function is
\[
\sum_{a,b=0}^{2}\binom na\binom nb z^{2n-a-b}-\binom n2 z^{2n-4}.
\]
Collecting terms gives the displayed five coefficients. The first nonzero coefficient proves both the minimum and its multiplicity. Complements of minimal forts are precisely inclusion-maximal failed sets: failure is monotone under taking subsets of the initial blue set, and adding any vertex to such a complement hits every fort.

**3. Fractional optimum and uniqueness.** Every three-element subset of \(A\) and \(B\) is a fort. Summing its weight constraint over all triples of \(A\) gives
\[
\binom{n-1}{2}\sum_{i=1}^{n}w(A_i)\ge\binom n3,
\]
whence \(\sum_i w(A_i)\ge n/3\); likewise \(\sum_i w(B_i)\ge n/3\). Uniform weights \(w(v)=1/3\) satisfy every triple constraint with equality and each matched-pair four-set constraint with slack \(1/3\). Hence \(Z^*(H_n)=2n/3\). For \(n\ge4\), equality in the sum of triple inequalities forces every triple's weight sum to equal one. Comparing two triples with the same two other vertices makes any two weights in a class equal; their common weight is \(1/3\). This holds on both classes, proving uniqueness. Uniqueness is not asserted for \(n=3\).

**4. Fort packing.** Every fort contains a minimal fort and hence has at least three vertices. Disjoint forts therefore number at most \(\lfloor2n/3\rfloor\). Write \(n=3q+r\) with \(r\in\{0,1,2\}\). Partition \(3q\) indices into \(q\) triples; take the pure triple fort on both \(A\) and \(B\) for each index triple, giving \(2q\) disjoint forts. When \(r=2\), add the matched-pair four-set from the two unused indices to obtain \(2q+1\) disjoint forts. These realize \(\lfloor2n/3\rfloor\) in every residue class. The integral/fractional ratio follows from the formulas above.

## Verification

The standalone Python 3 program `verify_crown_forts.py` constructs all graph adjacencies explicitly and simulates standard zero forcing on all \(349{,}504\) vertex subsets for \(3\le n\le9\). For \(3\le n\le8\), it checks every nonempty vertex subset for the fort condition and verifies that every fort contains a predicted minimal fort; it separately checks that every predicted minimal fort has no proper fort subset. For \(3\le n\le7\), it performs exact dynamic-programming fort packing. It also checks binomial coefficients and the residue construction through order eighty. Its recorded output is in `verification_output.txt`.

These finite checks are reproducibility evidence and do not replace the proof for arbitrary \(n\ge3\).

## Relationship to prior work

The fort-transversal characterization, fort number and fractional zero forcing framework are established by Cameron et al. [1]. Becker et al. [2] develop minimal-fort counting and the maximal-failed-set correspondence, including formulas for paths, cycles, spiders and constructions for other graph families. Pelayo and Abara [3] study maximal failed zero forcing sets for Cartesian, strong, lexicographic and corona products; their product classes do not include the direct-product representation \(K_2\times K_n\) of the crown graph. None of these inspected statements entails the explicit crown-graph minimal-fort hypergraph, full polynomial or combined integral/fractional formulas here. In particular, a complete bipartite graph is not the matching-deleted crown graph.

## Limitations

The domain is \(n\ge3\); the disconnected graph at \(n=2\) is not included. Neither positive-semidefinite/skew zero forcing nor propagation times are addressed. No general upper bound of three for the integrality ratio is claimed. Priority in unindexed mathematical literature, including equivalent descriptions under bipartite double-cover or direct-product terminology, cannot be ruled out by search alone. The mathematical proofs and finite experiments provided here do not constitute independent external validation.

## References

[1] T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal and H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904 (first version 2023-10-27), https://arxiv.org/abs/2310.17904 .

[2] P. Becker, T. R. Cameron, D. Hanely, B. Ong and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963 (first version 2024-04-09), https://arxiv.org/abs/2404.05963 .

[3] P. A. B. Pelayo and M. N. M. Abara, *Maximal failed zero forcing sets for products of two graphs*, arXiv:2202.04997 (first version 2022-02-10), https://arxiv.org/abs/2202.04997 .
