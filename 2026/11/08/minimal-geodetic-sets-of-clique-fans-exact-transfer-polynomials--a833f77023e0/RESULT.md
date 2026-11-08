# Minimal geodetic sets of clique fans: exact transfer polynomials and purity

## Finding

For all integers \(n\ge3\) and \(m\ge2\), the clique fan \(G_{n,m}=K_1\vee(P_n[K_m])\) has a complete classification of its inclusion-minimal geodetic vertex sets by three-state words, an explicit finite transfer matrix for their cardinality polynomial, and a sharp purity classification.

Let \(F,Z,P\) denote, respectively, a full layer of \(m\) chosen vertices, an empty layer, and a layer with exactly one chosen vertex. A word \(w_1\cdots w_n\) represents an inclusion-minimal geodetic set precisely when \(w_1=w_n=F\) and, for each \(2\le i\le n-1\), the adjacent triple \((w_{i-1},w_i,w_{i+1})\) obeys:

* \(w_i=Z\) exactly requires \(w_{i-1}=w_{i+1}=F\);
* \(w_i=F\) exactly requires at least one neighbor to be \(Z\);
* \(w_i=P\) exactly requires both neighbors not to be \(Z\) and at least one neighbor to be \(P\).

For each \(P\) there are \(m\) independent choices of the selected vertex. Thus the polynomial \(M_{n,m}(z)\) counting all labelled inclusion-minimal geodetic sets by size is
\[
M_{n,m}(z)=\sum_{\substack{w\in\{F,Z,P\}^n\\w_1=w_n=F\\w\ \text{satisfies the triples}}}m^{\#P(w)}z^{m\#F(w)+\#P(w)}.
\]
This has an exact \(9\times9\) transfer-matrix expression. In particular, the simplicial complex of complements of geodetic sets is pure if and only if
\[
n=3\quad\text{or}\quad (m=2\ \text{and}\ n\in\{4,6\}).
\]
In the exceptional cases \(M_{3,m}(z)=z^{2m}\), \(M_{4,2}(z)=6z^6\), and \(M_{6,2}(z)=27z^8\).

## Assumptions and scope

All graphs are finite, undirected, and simple. In \(P_n[K_m]\), the vertices form \(n\) ordered cliques \(L_1,\dots,L_n\) of size \(m\); consecutive cliques are completely joined, and no other inter-layer edges occur. A separate universal vertex \(h\) is adjacent to every layer vertex. A set \(S\) is *geodetic* if every graph vertex belongs to at least one shortest path between two vertices of \(S\) (allowing endpoints). A geodetic set is inclusion-minimal if none of its proper subsets is geodetic. The polynomial counts labelled subsets, not isomorphism classes. The complementary simplicial complex consists of \(V(G_{n,m})\setminus S\) for geodetic \(S\); its facets are complements of inclusion-minimal geodetic sets.

## Proof

**1. Exact feasibility criterion.** Every vertex of \(L_1\cup L_n\) is simplicial: its open neighborhood is a clique. Such a vertex cannot be an internal vertex of any geodesic, hence every geodetic set contains all of \(L_1\cup L_n\). As \(n\ge3\), any two vertices in the two end layers are nonadjacent; the two-edge path through \(h\) is shortest. Therefore these mandatory vertices cover \(h\) geodetically, and \(h\) cannot belong to an inclusion-minimal geodetic set.

For each interior layer \(L_i\), a vertex outside \(S\) can be an internal vertex of a shortest path between selected vertices only when its endpoints belong to \(L_{i-1}\) and \(L_{i+1}\). Indeed, \(G_{n,m}\) has diameter two, and the only nonadjacent neighbors of such a vertex lie in those two layers. Conversely, a selected endpoint in each neighboring layer makes every vertex of \(L_i\) internal to a shortest path. Writing \(s_i=|S\cap L_i|\), a subset of layer vertices is geodetic exactly if
\[
s_1=s_n=m,\qquad s_i=m\ \text{or}\ (s_{i-1}>0\ \text{and}\ s_{i+1}>0)\quad(2\le i\le n-1).
\tag{1}
\]
Adding \(h\) does not change whether any non-hub vertex is covered.

**2. Minimality, without lost configurations.** Geodeticity is upward closed, so it suffices to test deletion of each selected vertex. For an interior full layer \(s_i=m\ge2\), deletion makes \(s_i=m-1>0\) and changes no other occupancy; equation (1) fails precisely when an adjacent layer is empty. For \(2\le s_i<m\), deleting a vertex leaves the layer partially occupied and does not affect equation (1), so such a layer is impossible in a minimal set. A singleton partially occupied layer \(s_i=1<m\) has both neighbors occupied by (1). Removing its selected vertex leaves this layer empty, whose own requirement still holds, and makes (1) fail precisely when at least one neighboring layer is also partially occupied. Finally, an empty layer must have two occupied neighbors, which must be full rather than partial (otherwise their equation (1) would fail). These four observations are equivalent to the three local word rules in the statement. End layers remain full. Conversely, each chosen vertex in any word obeying the rules is essential by the same deletion tests, so the conditions are sufficient. Each singleton layer has exactly \(m\) choices, giving the stated polynomial.

**3. Exact transfer matrix.** Index rows and columns by the nine ordered pairs in \(\{F,Z,P\}^2\), and define \(v(F)=z^m\), \(v(Z)=1\), \(v(P)=mz\). Define \(Q(a,b,c)\) to be one when the central state \(b\) satisfies its displayed local rule with neighbors \(a,c\), and zero otherwise. Put
\[
\alpha_{(a,b)}=\mathbf1_{a=F}v(F)v(b),\qquad
T_{(a,b),(b',c)}=\mathbf1_{b=b'}Q(a,b,c)v(c),\qquad
\beta_{(a,b)}=\mathbf1_{b=F}.
\]
Multiplication extends a word by a new right-hand letter, checking the previous center state and multiplying by the new letter's labelled weight. Hence, for every \(n\ge3\),
\[
\boxed{M_{n,m}(z)=\alpha^{\mathsf T}T^{n-2}\beta.}
\]
This is an explicit exact computation of all coefficients, with constant-size matrix for each \(m\).

**4. Purity, all parameters.** The word \(FP^{n-2}F\) is valid for \(n\ge4\) and has size \(2m+n-2\). For even \(n=2k\ge4\), the word \(F(ZF)^{k-1}F\) is valid and has size \((k+1)m\). These two sizes coincide only at \(m=2\). For odd \(n=2k+1\ge5\), the word \(F(ZF)^k\) is valid and has size \((k+1)m\). Its size equals \(2m+2k-1\) only if \((k-1)m=2k-1\); for \(k\ge3\) no integer \(m\ge2\) satisfies this. At \(n=5\), the words \(FPPPF\) and \(FFZFF\) have sizes \(2m+3\) and \(4m\), which differ for \(m\ge3\); when \(m=2\), compare \(FPPPF\) with \(FZFZF\), of sizes seven and six.

For \(m=2\) and every even \(n\ge8\), the valid word \(FF(ZF)^{(n-6)/2}PPPF\) has size \(n+3\), whereas \(FP^{n-2}F\) has size \(n+2\). Thus all unlisted parameters are nonpure. Directly applying the local rules at \(n=3\) gives only \(FZF\). At \(n=4,m=2\) the only words are \(FZFF,FFZF,FPPF\), all of size six, with labelled multiplicities \(1,1,4\). At \(n=6,m=2\) the only words are \(FFZFZF,FZFFZF,FZFZFF,FZFPPF,FPPFZF,FPPPPF\); all have size eight, with multiplicities \(1,1,1,4,4,16\). Their total is \(27\). Therefore the complement complex is pure exactly in the claimed cases. \(\square\)

## Verification

The standalone script `verify.py` constructs each tested graph directly, performs breadth-first searches to obtain every graph distance, and independently evaluates all geodesic vertex covers and their inclusion-minimal subsets. It compares the results with the three-state formulas and transfer-matrix coefficients for 11 parameter profiles: \(3\le n\le8\) at \(m=2\), \(3\le n\le5\) at \(m=3\), and \(3\le n\le4\) at \(m=4\). This examines 388736 starting subsets and 293 minimal geodetic sets. The transfer matrix and claimed purity classification are also checked for \(3\le n\le35\) and \(2\le m\le6\). The unbounded theorem and the sharp purity statement follow from the proof; enumeration is finite corroboration, not a substitute for it.

## Relationship to prior work

Bergougnoux, Defrain, and Mc Inerney (arXiv:2309.17419, first posted September 29, 2023) study the enumeration of minimal geodetic sets and prove general equivalences with hypergraph transversal enumeration, including results on split graphs and graph classes excluding induced paths. This does not specify a cardinality polynomial or purity criterion for the clique fans here. Dafini and Vijayan (2023) study geodetic sets and polynomials of ordinary fans \(K_1\vee P_n\), the \(m=1\) model; that case is expressly outside this theorem and has a different minimality mechanism. Brešar, Kraner Šumenjak, and Tepeh (2011) investigate *minimum geodetic number* in lexicographic products, particularly with noncomplete second factors, rather than this universal-vertex-joined complete-layer family and its full inclusion-minimal spectrum. Existing generalized-geodetic algorithms do not themselves state the closed three-state characterization.

## Limitations

The theorem concerns ordinary geodetic sets, not strong geodetic sets, and assumes \(m\ge2,n\ge3\). It is not a classification for arbitrary graph substitutions, arbitrary clique-path joins, or the case \(m=1\). The derived transfer formula may be specialized for particular \(m,n\) but no asymptotic coefficient theorem is asserted. Equivalent unindexed prior formulations remain a publication-priority risk; finite verification does not certify novelty or prove the infinite statement independently.

## References

1. B. Bergougnoux, O. Defrain, and F. Mc Inerney, *Enumerating minimal solution sets for metric graph problems*, arXiv:2309.17419 (posted 2023-09-29), https://arxiv.org/abs/2309.17419 .
2. K. Vijila Dafini and A. Vijayan, *On Geodetic Sets and Geodetic Polynomials of Fan Graphs*, Journal of Research in Applied Mathematics 9(1), 1–8 (2023), https://www.questjournals.org/jram/papers/v9-i1/09010108.pdf .
3. B. Brešar, T. Kraner Šumenjak, and A. Tepeh, *The geodetic number of the lexicographic product of graphs*, Discrete Mathematics 311 (2011), 1693–1698, DOI 10.1016/j.disc.2011.04.004.
4. K. Raja Chandrasekar, *Geodetic numbers of tensor product and lexicographic product of graphs*, online November 11, 2024, DOI 10.1080/09728600.2024.2422535 (scalar values for other products).
