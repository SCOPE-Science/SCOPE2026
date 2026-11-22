# Six-stratum bracket fibers for a one-edge-deleted biclique Lie algebra

## Finding

Let \(G=K_{3,3}-e\) be the six-vertex graph formed by deleting one edge from the complete bipartite graph, and let \(L_G(\mathbb F_q)\) be its graph-defined two-step nilpotent Lie algebra over an arbitrary finite field of cardinality \(q\). The algebra has dimension \(14\), with derived central ideal of dimension \(8\). The number of ordered pairs \((X,Y)\in L_G(\mathbb F_q)^2\) giving **each prescribed** derived element is completely determined by the six strata below; no other fiber sizes occur.

Index the two vertex triplets by \(1,2,3\), and express a prescribed target as an observed \(3\times3\) matrix with position \((3,3)\) omitted:

\[
T=\begin{pmatrix}A&b\\d&*\end{pmatrix},\qquad
A\in M_2(\mathbb F_q),\quad b\in\mathbb F_q^2,\quad d\in(\mathbb F_q^2)^*.
\]

The star represents a *missing coordinate*, not a fixed value. Set
\[
\begin{split}
G_2&=(q^2-1)(q^2-q),\\
N_2&=G_2,\\
N_1&=(q^2-1)q^3+(q+1)G_2,\\
N_0&=q^6+(q^2+q+1)\big((q^2-1)q^3+G_2\big).
\end{split}
\]

For each target, divide the bracket fiber cardinality by \(q^{16}\). The resulting **six distinct** fiber values and their full target multiplicities are:

| Condition on \(A,b,d\) | Fiber divided by \(q^{16}\) | Number of targets |
|---|---:|---:|
| \(\operatorname{rank}A=2\) | \(N_2\) | \(G_2q^4\) |
| \(\operatorname{rank}A=1\), \(b\notin\operatorname{col}A\), \(d\notin\operatorname{row}A\) | \(0\) | \(q^2(q-1)^3(q+1)^2\) |
| \(\operatorname{rank}A=1\), \(b\in\operatorname{col}A\), \(d\in\operatorname{row}A\) | \(N_1+(q-1)N_2\) | \(q^2(q-1)(q+1)^2\) |
| \(\operatorname{rank}A=1\), exactly one of the two inclusions holds | \(qN_2\) | \(2q^2(q-1)^2(q+1)^2\) |
| \(A=0\), \(b\ne0\), \(d\ne0\) | \(qN_2\) | \((q^2-1)^2\) |
| \(A=0\), exactly one of \(b,d\) nonzero | \(qN_1\) | \(2(q^2-1)\) |
| \(A=b=d=0\) | \(N_0+(q-1)N_1\) | \(1\) |

The two rows with \(qN_2\) represent the *same* fiber size, so there are six values, not seven. In particular, the number of unattainable targets is exactly
\[
q^2(q-1)^3(q+1)^2,
\]
and the one-bracket image in the derived algebra has exactly
\[
q^8-q^2(q-1)^3(q+1)^2
\]
elements. This is a generic-surjectivity / singular-obstruction phenomenon: the unattainable proportion is \(q^{-1}+O(q^{-2})\). Every derived element is a sum of at most two brackets, and some are not one bracket, so the bracket width of \(L_G(\mathbb F_q)\) is **exactly two** for all prime powers \(q\), including characteristic two.

## Assumptions and scope

Fix a prime power \(q\ge2\). Take basis \(e_1,e_2,e_3,f_1,f_2,f_3\) for the degree-one space and eight independent central basis vectors \(z_{ij}\) with \(1\le i,j\le3\), \((i,j)\ne(3,3)\). Define the alternating Lie bracket by \([e_i,f_j]=z_{ij}\), the reversed bracket by antisymmetry, and every other basic bracket to be zero. Alternatingity also holds in characteristic two, as \([w,w]=0\) by construction. The center is the eight-dimensional span of the \(z_{ij}\). A target is an element of this derived ideal; targets outside it have no bracket witnesses, by definition.

In the table, \(d\in\operatorname{row}A\) means that the bottom row vector lies in the row span of \(A\), not a dot-product condition. When \(A=0\), the cases are separated by literal zero/nonzero vectors. No field-characteristic restrictions beyond finiteness apply.

## Proof

**Step 1 (wedge products are incomplete matrix factorizations).** Write the degree-one coordinates of \(X\) as \((u,v)\) and of \(Y\) as \((u',v')\), where all four vectors belong to \(\mathbb F_q^3\). The \((i,j)\)-coefficient of \([X,Y]\) for an existing edge is \(u_iv'_j-u'_iv_j\). Thus, with \(U=(u,-u')\in M_{3\times2}(\mathbb F_q)\) and \(V=\binom{v'^\top}{v^\top}\in M_{2\times3}(\mathbb F_q)\), the observed target is the \(3\times3\) matrix product \(UV\) with entry \((3,3)\) forgotten. The mapping from the four vertex vectors to \((U,V)\) is bijective. Each of \(X,Y\) has an arbitrary eight-coordinate central part, multiplying every vertex-level fiber by \(q^{16}\).

**Step 2 (full-matrix product fibers).** Fix a complete \(3\times3\) matrix \(M\) with rank \(r\). It is representable as \(UV\) with \(U\) having two columns if and only if \(r\le2\). If \(\operatorname{rank}U=2\), its image is a plane containing \(\operatorname{col}M\), with \(q^2+q+1\), \(q+1\), or \(1\) choices of plane according as \(r=0\), \(r=1\), or \(r=2\); for each plane there are exactly \(|\operatorname{GL}_2(q)|=G_2\) ordered column bases for \(U\), and \(V\) is unique. If \(\operatorname{rank}U=1\), it can contribute only to \(r=0\) or \(1\). For \(r=1\), its image line must equal \(\operatorname{col}M\), giving \(q^2-1\) choices of \(U\) and \(q^3\) lifts for \(V\). For \(r=0\), any of the \(q^2+q+1\) lines is allowed; the same lift count applies. If \(U=0\), only \(M=0\) is possible and \(V\) is arbitrary, giving \(q^6\) choices. These disjoint cases give precisely \(N_0,N_1,N_2\) above, with no others.

**Step 3 (the one-missing-entry rank census).** Let \(M(c)=\bigl(\begin{smallmatrix}A&b\\d&c\end{smallmatrix}\bigr)\) for \(c\in\mathbb F_q\). If \(\operatorname{rank}A=2\), the Schur complement shows exactly one choice of \(c\) gives \(\operatorname{rank}M(c)=2\); the other \(q-1\) choices give rank three. If \(\operatorname{rank}A=1\), row and column equivalences reduce \(A\) to \(\operatorname{diag}(1,0)\). Writing the residual column and row entries in quotient directions as \(\beta,\delta\), the remaining \(2\times2\) minor has determinant \(-\beta\delta\). Hence: if both \(b\notin\operatorname{col}A\) and \(d\notin\operatorname{row}A\), every completion has rank three; if both inclusions hold, one completion has rank one and the others rank two; if exactly one fails, every completion has rank two. If \(A=0\), both \(b,d\) nonzero imply rank two for every completion, exactly one nonzero implies rank one for all completions, and both zero yield one rank-zero and \(q-1\) rank-one completions. Summing \(N_{\operatorname{rank} M(c)}\) over \(c\) gives all table entries. There is no hidden cancellation in characteristic two because the nonzero obstruction \(-\beta\delta\) remains nonzero.

**Step 4 (multiplicities).** There are \(G_2\) invertible \(2\times2\) matrices and \((q-1)(q+1)^2\) rank-one such matrices. For a fixed rank-one \(A\), each of \(\operatorname{col}A\) and \(\operatorname{row}A\) has \(q\) vectors, while each complement has \(q(q-1)\). Multiplying the allowed independent choices for \(b,d\) gives all seven condition-row multiplicities; the two \(qN_2\) rows combine. The unattainable multiplicity is therefore \((q-1)(q+1)^2\cdot q^2(q-1)^2\). The row multiplicities sum to \(q^8\). For \(q\ge2\), the six displayed fiber values are distinct by \(0<N_2<qN_2<N_1+(q-1)N_2<qN_1<N_0+(q-1)N_1\).

**Step 5 (sharp bracket width).** For any observed target, fill the missing entry arbitrarily, producing a matrix of rank at most three. Any rank-three matrix is a sum of a rank-at-most-two and a rank-at-most-one matrix. Each summand factors through a two-dimensional middle space and hence is itself the full matrix of some bracket. After deleting the missing coordinate this is a sum of two brackets. Conversely, the row of unattainable targets has positive multiplicity for every \(q\ge2\), so one bracket never suffices universally. Thus width equals two.

## Verification

The standalone `verification/finite_field_check.py` replays the entire vertex-pair count for all \(q^{12}\) ordered pairs over \(\mathbb F_2\) and over \(\mathbb F_3\), then checks the formula against every one of the \(q^8\) prescribed targets, including all zero-fiber targets. It also checks the unattainable-target count and the sum of all fibers. Exact output is embedded in `verification/check_output.txt`. These exhaustive *finite* checks corroborate but do not replace the field-uniform proof above. The proof establishes all prime powers, including nonprime extension fields.

## Relationship to prior work

Mainkar's graph-defined two-step Lie algebra construction and isomorphism theorem supply the ambient objects; they do not count prescribed bracket witnesses. The determinantal matrix-completion framework of Király, Theran and Tomioka establishes generic completion properties of low-rank matrices, predominantly over the complex field. Its generic theorem does not specify singular-target finite-field completion multiplicities or the multiplicity-weighted bracket fibers of the deleted-edge Lie algebra. Rossmann's graphical-group census concerns conjugacy and centralizer sizes, not fixed nonzero bracket targets. Kishnani and Kulshrestha give qualitative defect obstructions to bracket surjectivity, but not the six-stratum prescribed-fiber distribution of this six-vertex algebra. Classical rank-two matrix factorization and Schur complements are inputs, not claimed as new. The assessed combination is the **complete target-by-target finite-field bracket-fiber and image classification** for this natural boundary graph, including the sharp two-bracket width.

## Limitations

This theorem covers exactly the graph obtained from \(K_{3,3}\) by one edge deletion and its associated Lie algebra. It does not classify arbitrary incomplete bipartite graphs or arbitrary two-step nilpotent Lie algebras. Literature searches cannot prove priority; in particular, an implicit specialization of a more general singular matrix-completion counting theorem could potentially overlap. The relevant published works read here address broader generic-completion, centralizer, or qualitative obstruction questions rather than these full fibers. Independent mathematical validation remains outstanding.

## References

- M. G. Mainkar, *Graphs and and two-step nilpotent Lie algebras*, 2013, arXiv:1310.3414v1, https://arxiv.org/html/1310.3414v1 (graph Lie algebras and graph-isomorphism theorem; inspected introduction and proof framing).
- F. J. Király, L. Theran and R. Tomioka, *The Algebraic Combinatorial Approach for Low-Rank Matrix Completion*, arXiv:1211.4116v1 (first posted 2012-11-17), JMLR 16 (2015), 1391–1436, https://jmlr.org/papers/volume16/kiraly15a/kiraly15a.pdf (generic determinantal completion, especially Theorem 17 and Section 6).
- C. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, Bull. Lond. Math. Soc. 54 (2022), 1923–1943, https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12665 (graphical Lie centralizers and class-counting polynomials).
- H. Kishnani and A. Kulshrestha, *Defects in weighted graphs and Commutators*, arXiv:2505.07965 (2025), https://arxiv.org/abs/2505.07965 (qualitative non-surjectivity obstructions).
