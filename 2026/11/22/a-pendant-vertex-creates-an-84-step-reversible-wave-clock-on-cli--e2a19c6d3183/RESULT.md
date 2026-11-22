# A pendant vertex creates an 84-step reversible wave clock on cliques

## Finding

For every integer \(n\geq3\), let \(P_n\) consist of the complete graph \(K_n\) on labelled vertices \(0,\ldots,n-1\) and one additional leaf \(\ell\), adjacent only to vertex \(0\). Let \(q=3^f\), \(f\geq1\), and let \(A_n\) be the adjacency matrix of \(P_n\) over \(\mathbb F_q\). The reversible wave on pairs of vertex fields is
\[
T_n(u,v)=(A_nu-v,u),\qquad (u,v)\in\mathbb F_q^{n+1}\times\mathbb F_q^{n+1}.
\]

**Theorem.** Every state is periodic from time zero, and the sharp global order is
\[
L_n=\operatorname{ord}(T_n)=
\begin{cases}
84,&n\equiv0\pmod3,\\
18,&n\equiv1\pmod3,\\
24,&n\equiv2\pmod3.
\end{cases}
\]
For every integer \(k\geq1\), define \(d_n(k)\) as follows. If \(n\equiv0\pmod3\), then
\[
d_n(k)=(n-2)(1+\mathbf1_{3\mid k})+6\mathbf1_{28\mid k}.
\]
If \(n\equiv2\pmod3\), then
\[
d_n(k)=(n-2)(1+\mathbf1_{3\mid k})+2\mathbf1_{4\mid k}+4\mathbf1_{8\mid k}.
\]
If \(n\equiv1\pmod3\), put \(s=3^{\nu_3(k)}\), and then
\[
d_n(k)=\min(s,6)+(n-3)\min(s,2)+\mathbf1_{2\mid k}\min(s,2).
\]
The exact fixed-iterate count is
\[
\#\operatorname{Fix}(T_n^k)=q^{d_n(k)}.
\]
For every divisor \(r\) of \(L_n\), the number of **primitive temporal orbits** of period \(r\) equals
\[
\frac1r\sum_{e\mid r}\mu(r/e)q^{d_n(e)};
\]
there are no other primitive periods. By contrast, for the same rule on the unmodified \(K_n\), the global period is respectively \(9,12,6\) in the same three residue classes. Thus adding one leaf produces a primitive order-28 spectral mode when \(3\mid n\), enlarging the global clock from \(9\) to \(84\).

## Assumptions and scope

Graphs are finite, simple and undirected, with the specified vertex labels and no self-loops. The field has characteristic exactly three and may have any finite extension degree. All sums in the update are computed in that field; the full time state consists of both rows \((u,v)\). The fixed-iterate count is for labelled field-valued pairs, not graph-isomorphism classes. The statement is for every \(n\ge3\), every \(f\ge1\), and every positive update count \(k\). The graph family is also called the one-leaf pineapple or clique-with-leaf family; its ordinary adjacency characteristic polynomial is previously known, and is used here as a starting point rather than claimed as a new spectral formula.

## Proof

First, \(T_n^{-1}(u,v)=(v,A_nv-u)\), so all orbits on the finite state set are periodic immediately. Put \(m=n+1\). Let \(t\) denote an indeterminate. By eliminating the all-but-one identical core rows (or by the equitable partition into the root, the other \(n-1\) clique vertices, and the leaf),
\[
\det(tI_m-A_n)=(t+1)^{n-2}g_n(t),\qquad
 g_n(t)=t^3+(2-n)t^2-nt+n-2.
\]
Over \(\mathbb F_3\), the cubic factors by the residue of \(n\):
\[
\begin{array}{c|c}
n\bmod3&g_n(t)\\\hline
0&t^3-t^2+1\\
1&(t-1)(t+1)^2\\
2&t(t^2+1).
\end{array}
\]
Write \(W\) for the \((n-2)\)-dimensional space supported on the non-root clique vertices with their coordinate sum zero. Every vector in \(W\) is an eigenvector of \(A_n\) of eigenvalue \(-1\). For \(n\not\equiv1\pmod3\), the constant non-root vector supplements \(W\), giving a direct invariant decomposition into \(W\) and the three-dimensional root/constant/leaf sector. This last sector has adjacency characteristic polynomial \(g_n\). Both cubics for residues zero and two are square-free: the residue-zero cubic is irreducible over \(\mathbb F_3\), and the residue-two cubic has distinct factors. The wave matrix for an adjacency scalar \(a\) has characteristic polynomial \(z^2-az+1\). Consequently, the \(W\)-sector comprises \(n-2\) identical two-by-two unipotent blocks at temporal eigenvalue \(+1\), each with order three and with fixed-space dimension \(1+\mathbf1_{3\mid k}\) at update \(k\).

When \(n\equiv0\pmod3\), the remaining temporal characteristic polynomial is
\[
h(z)=z^3g_n(z+z^{-1})=z^6-z^5-z^3-z+1.
\]
Over \(\mathbb F_3\),
\[
\Phi_{28}(z)=h(z)(z^6+z^5+z^3+z+1).
\]
The roots of \(h\) are distinct primitive 28th roots (since three is coprime to 28). Their whole six-dimensional sector is fixed by the \(k\)-th update if and only if \(28\mid k\), and otherwise contributes no fixed vectors. This proves the first formula for \(d_n(k)\) and the global order \(\operatorname{lcm}(3,28)=84\).

When \(n\equiv2\pmod3\), the remaining temporal polynomial factors as
\[
 z^3g_n(z+z^{-1})=(z^2+1)(z^2-z-1)(z^2+z-1).
\]
The first quadratic has two primitive fourth roots; the last two quadratics multiply to \(z^4+1\) in characteristic three, and hence contribute four primitive eighth roots. All factors are square-free. This proves the residue-two fixed-space formula and global order \(\operatorname{lcm}(3,8)=24\).

It remains to handle the modular degeneracy when \(n\equiv1\pmod3\), which cannot be inferred from the characteristic polynomial alone. Write a core-root entry \(a\), a vector of other core entries \(b=(b_i)\), its sum \(S=\sum b_i\), and leaf entry \(c\). If \(B=A_n+I\), then
\[
 B(a,b,c)=(a+S+c,\;(a+S)\mathbf1,\;a+c).
\]
Since \(n-1=0\) in the field, \(\ker B\) has conditions \(a=c=S=0\), so \(\dim\ker B=n-2\). Also
\[
 B^2(a,b,c)=(2a+S+2c,\;(a+S+c)\mathbf1,\;2a+S+2c),
\]
whose kernel has the independent conditions \(S=0\) and \(a+c=0\), so \(\dim\ker B^2=n-1\). Together with \(\det(tI-A_n)=(t+1)^n(t-1)\), the Jordan blocks of \(A_n\) are exactly one block of size three at \(-1\), \(n-3\) blocks of size one at \(-1\), and one block of size one at \(+1\). This argument uses ranks over the actual characteristic-three field, rather than importing a characteristic-zero diagonalization.

For one adjacency Jordan block of size \(j\) at \(-1\), the temporal companion has one Jordan block of size \(2j\) at \(+1\). To see this, eliminate one row of the block companion pencil \(zI-T\) to get \((z^2+z+1)I-zN=(z-1)^2I-zN\), where \(N\) is the standard nilpotent block of length \(j\). Since \(z\) is a unit in the localization at \(z=1\), the Smith form has precisely one nonunit diagonal entry, \((z-1)^{2j}\). Similarly, the single adjacency eigenvalue \(+1\) yields one temporal Jordan block of size two at \(-1\). The complete temporal Jordan inventory is therefore one \(J_6(1)\), \(n-3\) copies of \(J_2(1)\), and one \(J_2(-1)\).

For a Jordan block \(J_j(1)\) in characteristic three, the kernel dimension of \(J_j(1)^k-I\) is \(\min(j,3^{\nu_3(k)})\). At eigenvalue \(-1\), there are no fixed vectors for odd \(k\), while for even \(k\) the same kernel formula applies. This proves the residue-one formula. The largest unipotent block has order nine, while the negative block has order six; together they give the sharp global order \(\operatorname{lcm}(9,6)=18\).

Finally, for any finite permutation, the fixed points of its \(k\)-th power count all primitive-period configurations with period dividing \(k\). Möbius inversion yields the stated orbit formula. The orders are sharp because each described primary block occurs for every permitted \(n\), and a direct sum of component states realizes the least common multiple of their orders. The corresponding intact-clique orders follow from \(A(K_n)=J-I\) and \(J^2=nJ\) over characteristic three, obtaining respectively a length-four temporal unipotent block, a primitive-four component, or a negative length-two block alongside the other modes.

## Verification

The included dependency-free program `verify_kite_wave.py` builds the full labelled wave matrix over \(\mathbb F_3\), computes matrix powers and ranks independently of the formulas, and verifies the predicted fixed-space dimensions for every \(1\le k\le L_n\) and \(3\le n\le18\). It tests both \(T_n^{L_n}=I\) and the failure of every prime-divisor order reduction. Separately, it follows the direct vertex update across all \(3^{2(n+1)}\) configurations for \(n=3,4,5\), independently of the matrix-rank implementation, and checks the entire temporal orbit histogram against the formulas. Output is in `verification_run.txt`. These computations check finite cases; the algebraic proof above, not finite testing, establishes all sizes and field extensions.

For example, over \(\mathbb F_3\) at \(n=3\), the orbit counts by primitive length are \(3\) fixed points, \(2\) three-cycles, \(78\) 28-cycles, and \(52\) 84-cycles; these account for all \(6561\) states. At \(n=4\), there are \(2808\) primitive 18-cycles among the \(59049\) configurations. At \(n=5\), there are \(21060\) primitive 24-cycles among the \(531441\) configurations.

## Relationship to prior work

Vlasov's 2013 paper gives the general reversible second-order construction, including the update \((u,v)\mapsto(f(u)-v,u)\), but does not calculate this graph family's periods or orbit counts. Topcu, Sorgun and Haemers (2015, Proposition 1.1) give the ordinary characteristic polynomial for all pineapple graphs; its single-leaf case is exactly the polynomial used as an input above. Their article concerns spectral determination over characteristic zero and does not give the characteristic-three Jordan structure or reversible-wave census. The central additional steps here are the defective-characteristic Jordan analysis, the primitive order-28 mode, and the exact temporal fixed-iterate/orbit counts. Exact prior equivalent results cannot be excluded outside the inspected literature and indexed records.

## Limitations

The statement does not concern irreversible first-order neighbor sums, continuous waves, other field characteristics, arbitrary numbers or placements of leaves, or orbit-attraction basins (there are none because the update is invertible). It does not claim the characteristic polynomial of pineapple graphs is new. Finite checks are corroborative, not a substitute for the infinite-family proof. Priority cannot be guaranteed against unindexed or inaccessible literature; independent audit has not been performed.

## References

1. Alexander Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first submitted 2013-11-18. https://arxiv.org/abs/1311.4297
2. Hatice Topcu, Sezer Sorgun and Willem H. Haemers, *On the spectral characterization of pineapple graphs*, arXiv:1511.08674, first submitted 2015-11-27; in particular Proposition 1.1. https://arxiv.org/abs/1511.08674
