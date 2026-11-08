# Singular false-twin quotients and the real graph evolution-algebra isomorphism criterion

## Finding

**Theorem (singular twin quotient; all isomorphisms).** Let \(G\) be a finite connected simple graph with at least two vertices. Partition its vertex set into the classes \(C_i\) of equality of open neighborhoods (false twins); write \(m_i=|C_i|\), and form the quotient graph \(H\) with one vertex per class. Assume that the adjacency matrix of \(H\) is **singular over \(\mathbb R\)**. Let \(A(G)\) be the real evolution algebra with natural basis \(e_v\), \(e_v e_w=0\) for distinct vertices, and \(e_v^2=\sum_{w\sim v}e_w\). Let \(A_{\mathrm{RW}}(G)\) replace each nonzero square by its division by \(\deg_G(v)\). Then

\[
A(G)\cong_{\mathbb R} A_{\mathrm{RW}}(G)
\quad\Longleftrightarrow\quad
G\text{ is regular or bipartite biregular}.
\]

More precisely, put \(V_i=\operatorname{span}_{\mathbb R}\{e_v:v\in C_i\}\) and \(d_i=\deg_G(v)\) for \(v\in C_i\). Every algebra isomorphism \(\Phi:A(G)\to A_{\mathrm{RW}}(G)\) permutes these subspaces by an automorphism \(\pi\) of the weighted quotient \((H,(m_i))\). On \(V_i\to V_{\pi(i)}\), it is given, in the natural ordered bases, by

\[
\Phi|_{V_i}=t_i U_i,\qquad U_i^{\mathsf T}U_i=I_{m_i},\quad U_i\mathbf1_{m_i}=\mathbf1_{m_i},\quad t_i>0.
\]

For a regular graph of degree \(d\), all \(t_i=d\). For a nonregular bipartite biregular graph, if degrees on the two sides are \(a\) and \(b\), respectively, the scalars on those sides are \((a^2b)^{1/3}\) and \((ab^2)^{1/3}\). Conversely, every such weighted-quotient automorphism, every choice of such orthogonal matrices and the prescribed scalars produce an algebra isomorphism.

The proof of the necessity and the full normal form actually uses no assumption about the determinant of \(H\). The singular-quotient formulation isolates the class not covered by the nonsingular-quotient result. Combined with that already established case, it gives the same criterion for **all** finite connected simple graphs over \(\mathbb R\). This is a statement about **isomorphisms**; it does not classify noninvertible homomorphisms.

## Assumptions and scope

All graphs here are finite, connected, undirected, loopless and nonempty, with at least one edge. The coefficient field is \(\mathbb R\), and all maps are \(\mathbb R\)-linear. The false-twin classes are intrinsic to the graph and may have any positive sizes; the graph \(H\) is connected and false-twin-free, and each \(C_i\) is an independent set. Distinct classes are either completely adjacent or completely nonadjacent. The weighted quotient automorphism preserves adjacency and the list of sizes: \(m_{\pi(i)}=m_i\). The degree formula is \(d_i=\sum_{j\sim_H i}m_j>0\). Biregular means bipartite with a constant degree on each side; the two constants need not differ.

## Proof

**1. An intrinsic rank-one partition.** For each class write \(s_i=\sum_{j\sim_H i}\mathbf1_{C_j}\), where \(\mathbf1_{C_j}=\sum_{v\in C_j}e_v\). Thus every natural-basis element in \(V_i\) has square \(s_i\) in \(A(G)\), while it has square \(s_i/d_i\) in \(A_{\mathrm{RW}}(G)\). No \(s_i\) vanishes, since the graph is connected. For distinct \(i,j\), the vectors \(s_i,s_j\) are linearly independent: their entries are zero or one, neither vector is zero, and proportionality over \(\mathbb R\) would force equality of neighborhoods, contrary to distinctness of the classes.

For \(x=\sum_i x_i\), \(x_i\in V_i\), left multiplication in either algebra has the form
\[
L_x(y)=\sum_i \alpha_i\langle x_i,y_i\rangle s_i,
\]
with \(\alpha_i=1\) in the adjacency algebra and \(\alpha_i=1/d_i\) in the random-walk algebra. For \(x_i\ne0\), the coefficient functional of \(y_i\) is nonzero, and the independently selectable \(y_i\)'s show that the image of \(L_x\) is exactly the span of those \(s_i\) for which \(x_i\ne0\). Thus
\[
\operatorname{rank}L_x\le1\quad\Longleftrightarrow\quad x\in\bigcup_i V_i.
\]
Indeed, two nonzero blocks produce two independent images; a single block produces rank one. This union is characterized solely by the multiplication, hence is preserved by an algebra isomorphism. Since a linear subspace contained in this finite union must lie inside one of the \(V_i\), invertibility implies that an isomorphism permutes its maximal linear subspaces, giving \(\Phi(V_i)=V_{\pi(i)}\) and \(m_{\pi(i)}=m_i\).

**2. Orthogonal similitudes on the blocks.** Let \(M_i\) be the invertible \(m_i\)-by-\(m_i\) real matrix of the restriction. Images of two different basis vectors of \(V_i\) multiply to zero in the target algebra. Their target product is their Euclidean inner product times \(s_{\pi(i)}/d_{\pi(i)}\), so distinct columns of \(M_i\) are orthogonal. Their source squares are all the same \(s_i\); hence their target squares are equal, so the squared column norms are all the same positive number \(\lambda_i\). Therefore
\[
M_i^{\mathsf T}M_i=\lambda_iI_{m_i},\qquad \lambda_i>0.
\]
Also \(\Phi(s_i)=\lambda_i s_{\pi(i)}/d_{\pi(i)}\).

**3. Quotient symmetry and the edge equations.** Since \(\Phi(s_i)=\sum_{j\sim_H i}M_j\mathbf1_{m_j}\), its nonzero blocks occur *exactly* at \(\pi(j)\) for \(j\sim_H i\); each block is nonzero because \(M_j\) is invertible. On the other hand, the support of \(s_{\pi(i)}\) comprises the neighbors of \(\pi(i)\). Consequently \(\pi(N_H(i))=N_H(\pi(i))\), so \(\pi\) is an automorphism of \(H\), preserving the sizes and hence the degrees \(d_{\pi(i)}=d_i\). Comparing the blocks in the last identity gives, for every edge \(ij\),
\[
M_j\mathbf1_{m_j}=\frac{\lambda_i}{d_i}\mathbf1_{m_j}
\]
(the ones vector on the right is understood in \(V_{\pi(j)}\)). Thus each \(M_j\mathbf1_{m_j}=t_j\mathbf1_{m_j}\) for a positive scalar \(t_j\). Positivity follows because every vertex has a neighbor and \(\lambda_i/d_i>0\). Taking norms in the last identity and using \(M_j^{\mathsf T}M_j=\lambda_j I\) gives \(t_j^2=\lambda_j\). Hence
\[
t_j=\frac{t_i^2}{d_i}\qquad\text{for every directed edge }i\to j\text{ of }H.
\]
Setting \(U_i=t_i^{-1}M_i\) yields the claimed orthogonality and \(U_i\mathbf1=\mathbf1\).

**4. Degree rigidity.** All neighbors of a given vertex \(i\) have the same \(t\)-value, namely \(t_i^2/d_i\). Along a path, the \(t\)-values therefore alternate between at most two constants. If \(H\) contains an odd cycle, connectivity forces a single constant \(t\) on the whole graph. The edge equation gives \(d_i=t\) everywhere: \(G\) is regular. If \(H\) is bipartite, the constants \(a'\) and \(b'\) are uniform on its two sides; the edge equations then give \(d_i=(a')^2/b'\) and \(d_j=(b')^2/a'\), so \(G\) is biregular. The bipartition of \(H\) lifts to \(G\).

**5. Converse and uniqueness of scalings.** If \(G\) has constant degree \(d\), put \(t_i=d\). Otherwise, in the biregular case with degrees \(a\) on one side and \(b\) on the other, solve \(t_B=t_A^2/a\) and \(t_A=t_B^2/b\): their unique positive solution is \(t_A=(a^2b)^{1/3}\), \(t_B=(ab^2)^{1/3}\). The respective formulas satisfy every directed edge equation. For any weighted-quotient automorphism \(\pi\) and any real orthogonal blocks \(U_i\) with \(U_i\mathbf1=\mathbf1\), define \(\Phi|_{V_i}=t_iU_i\) into \(V_{\pi(i)}\). Products of distinct source basis elements map to zero (orthogonality inside a block, disjoint support across blocks), and for each source basis element in \(V_i\),
\[
\Phi(e_v^2)=\sum_{j\sim i}t_j\mathbf1_{C_{\pi(j)}}=\frac{t_i^2}{d_i}s_{\pi(i)}=\Phi(e_v)^2.
\]
Thus \(\Phi\) is a bijective homomorphism. Every isomorphism was shown to have this form. This completes the proof. \(\square\)

## Verification

`checker.py` uses exact rational arithmetic for finite graph enumeration and an explicit algebra homomorphism check. It enumerates all labeled connected simple graphs on \(2\) through \(6\) vertices: \(27{,}475\) graphs, of which \(5{,}820\) have singular false-twin quotient. Among these, \(60\) satisfy the regular or bipartite-biregular degree condition, and \(5{,}760\) do not; \(2{,}700\) of the singular-quotient examples have nontrivial twin classes. It also constructs a nonpermutation orthogonal block isomorphism for the triple independent-set blow-up of the eight-cycle and checks the irregular twin-free seven-vertex path as an obstruction. All checks completed without discrepancy. The checker tests structural prerequisites and explicit examples, not all possible real linear maps. The unrestricted conclusion is established by the proof, not by enumeration.

Run from an ordinary Python 3 installation as `python3 checker.py`; its output is included in `checker_output.txt`.

## Relationship to prior work

The 2017 nonsingular-graph classification of Cadavid, Rodiño Montoya and Rodríguez proves the criterion when the adjacency matrix of \(G\) is invertible. Their 2024 paper explicitly identifies the singular case as conjectural, proves selected graph-family cases and suggests exploiting twin partitions. A later paper by Rodiño Montoya, Viana Bedoya and Henao studies automorphisms of each individual evolution algebra but not this cross-algebra isomorphism criterion. The 2026 survey by Kaygorodov, Martín González and Viruel records the open question. The already established nonsingular-twin-quotient theorem proves the criterion when \(H\) is nonsingular; this theorem treats the complementary singular-quotient case, including singular, false-twin-free graphs. Neither the 2017 result nor the earlier quotient theorem implies the singular-quotient statement. The joint conclusion is the complete real-field isomorphism criterion.

## Limitations

The positivity argument uses the real Euclidean inner product and positive squared norms, so no corresponding classification is asserted over arbitrary fields. The result concerns finite connected simple graphs with edges and bijective linear algebra homomorphisms; it does **not** establish the separate conjecture that every homomorphism between nonisomorphic associated algebras must vanish. The finite checker is corroborative, not an exhaustive search over isomorphisms. Historical priority for differently phrased unindexed results cannot be ruled out solely by literature searches; an independent mathematical audit has not been performed.

## References

1. I. Kaygorodov, C. Martín González and M. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first public 2026-10-15), Question 26.
2. P. Cadavid, M. L. Rodiño Montoya, P. M. Rodríguez and S. J. Vidal, *On some singular graphs with non-isomorphic associated evolution algebras*, arXiv:2405.12341v1 (2024), especially Sections 2–3.
3. M. L. Rodiño Montoya, N. A. Viana Bedoya and C. Henao, *Group actions and automorphisms of evolution algebras associated to finite graphs*, arXiv:2505.15604v2 (2025).
4. P. Cadavid, M. L. Rodiño Montoya and P. M. Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks*, arXiv:1710.10516 (2017), nonsingular case.
