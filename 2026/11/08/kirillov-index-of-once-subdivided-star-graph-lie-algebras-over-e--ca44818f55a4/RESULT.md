# Kirillov index of once-subdivided star graph Lie algebras over every field

## Finding

Let \(T_m\), \(m\geq1\), be the tree obtained by subdividing every edge of the star \(K_{1,m}\) once. Thus it has one hub, \(m\) middle vertices, and \(m\) terminal leaves. Let \(\mathfrak n_{T_m}\) be the three-step nilpotent graph Lie algebra of Gallo--Videla [GV], whose basis is indexed by vertices, edges and unoriented two-edge paths. For any field \(k\), including characteristic two, define its Kirillov index by
\[
\operatorname{ind}_k(\mathfrak n_{T_m})=\min_{\varphi\in\mathfrak n_{T_m}^{*}}\dim_k\{x\in\mathfrak n_{T_m}:\varphi([x,y])=0\ \text{for all }y\}.
\]
Then
\[
\boxed{\operatorname{ind}_k(\mathfrak n_{T_m})=\frac{m(m+1)}2+2\left\lceil\frac m2\right\rceil-1.}
\]
Equivalently the maximum rank of a Kirillov form is
\[
\boxed{2(m+1)+2\left\lfloor\frac m2\right\rfloor.}
\]
The center has dimension \(m(m+1)/2\). Consequently the excess of the index over the center dimension is exactly \(2\lceil m/2\rceil-1\): it is one for \(m=1,2\) but grows without bound for the first genuinely branching subdivided stars \(m\ge3\). These are exact statements over every field, with no generic-field or large-characteristic assumption.

## Assumptions and scope

The graph \(T_m\) has vertices \(c,u_1,\ldots,u_m,v_1,\ldots,v_m\) and edges \(cu_i,u_iv_i\) for \(1\le i\le m\). There are \(2m+1\) vertices, \(2m\) edges, and \(\binom m2+m=m(m+1)/2\) unoriented paths of length two. The graph Lie algebra is defined exactly as in [GV, Section 2]. Its degree-one basis is the vertices; degree-two basis consists of \(a_i=[c,u_i]\) and \(b_i=[u_i,v_i]\); degree-three central basis consists of \(z_{ij}\) for paths \(u_i-c-u_j\) (\(i<j\)) and \(t_i\) for \(c-u_i-v_i\).

After signs are fixed consistently, the only nonzero brackets other than the edge brackets are
\[
[u_i,a_j]=[u_j,a_i]=z_{ij}\quad(i<j),\qquad [c,b_i]=t_i,\qquad [v_i,a_i]=-t_i.
\]
(The final signs may change with central-basis orientations without changing the result.) Hence the algebra has dimension \(4m+1+m(m+1)/2\). The center equals the span of the degree-three basis by [GV, Lemma 4.4] for the connected tree \(T_m\), and the stated center dimension follows.

## Proof

Write \(V=\langle c,u_1,\ldots,u_m,v_1,\ldots,v_m\rangle\), \(A=\langle a_1,\ldots,a_m,b_1,\ldots,b_m\rangle\), and \(W=\langle z_{ij},t_i\rangle\). For any linear functional \(\varphi\), the radical of its alternating Kirillov form contains \(W\), and its matrix on \(V\oplus A\) has the block form
\[
B_\varphi=\begin{pmatrix}C&D\\-D^{\mathsf T}&0\end{pmatrix},
\]
where \(C\) is an alternating \((2m+1)\times(2m+1)\) matrix and \(D\) is \((2m+1)\times2m\). All brackets in the \(A\times A\) block vanish.

Put \(\tau_i=\varphi(t_i)\), \(\zeta_{ij}=\varphi(z_{ij})\), \(\alpha_i=\varphi(a_i)\), \(\beta_i=\varphi(b_i)\). The column of \(D\) indexed by \(b_i\) has its sole potentially nonzero entry \(\tau_i\) in row \(c\), so all \(b_i\) columns span a space of dimension at most one. There are only \(m\) other columns, indexed by \(a_i\). Thus \(\operatorname{rank}D\le m+1\), over every field. Counting first the \(2m+1\) vertex columns and then the other columns gives
\[
\operatorname{rank}B_\varphi\le(2m+1)+\operatorname{rank}D\le3m+2.
\]
As every alternating matrix has even rank, this yields the uniform bound
\[
\operatorname{rank}B_\varphi\le2(m+1)+2\lfloor m/2\rfloor.
\]

We attain this bound by an explicit functional with values in the prime subfield, so the construction works for every field. Set every \(\tau_i=1\), every \(\alpha_i=0\), and set \(\zeta_{ij}=1\) exactly on the disjoint pairs \((1,2),(3,4),\ldots\), with all other \(\zeta_{ij}=0\). Set \(\beta_{2j}=1\), \(\beta_{2j-1}=0\) on each complete pair, and set \(\beta_m=0\) if \(m\) is odd.

For this functional, the \(a_i\) columns of \(D\) are linearly independent because they have respective nonzero coefficients \(-1\) in the distinct rows \(v_i\); the \(b_i\) columns span the additional independent row direction \(c\). Hence \(\operatorname{rank}D=m+1\). A vector \(x\in\ker(D^{\mathsf T})\subseteq V\) has \(x_c=0\) and, with \(x_{u_i}=s_i\), the equations
\[
x_{v_j}=\sum_{i\ne j}\zeta_{ij}s_i.
\]
Therefore \(\ker(D^{\mathsf T})\) has dimension \(m\). The restriction of \(C\) to this kernel comes solely from the brackets \([u_i,v_i]=b_i\). On every paired coordinate plane \(\langle s_{2j-1},s_{2j}\rangle\), its alternating matrix is, up to sign,
\[
\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
No cross-pair entry is nonzero, and the one remaining coordinate when \(m\) is odd lies in its radical. Thus the restriction has rank exactly \(2\lfloor m/2\rfloor\), including in characteristic two.

The elementary block-elimination identity
\[
\operatorname{rank}\begin{pmatrix}C&D\\-D^{\mathsf T}&0\end{pmatrix}
=2\operatorname{rank}D+\operatorname{rank}\left(C\big|_{\ker D^{\mathsf T}}\right)
\]
now gives \(\operatorname{rank}B_\varphi=2(m+1)+2\lfloor m/2\rfloor\). This matches the upper bound. Finally, subtracting this rank from \(\dim\mathfrak n_{T_m}=4m+1+m(m+1)/2\) yields the index formula. Every step is valid in characteristic two because the forms are alternating and no division by two is used. This proves the theorem.

## Verification

The standalone standard-library program `check_index.py` builds each subdivided-star graph independently from its vertex and edge lists, constructs all unoriented two-path basis vectors, and computes brackets using the path-incidence rule of [GV]. It does not use the reduced block matrix from the proof as its matrix-generation routine. It computes ranks by exact finite-field elimination and checks the explicit functional for \(m=1,\ldots,10\) over the prime fields of orders \(2,3,5,7\). It also exhaustively checks every possible functional coefficient vector for \(m=1,2,3\) over \(\mathbb F_2\), totaling \(4{,}232\) functionals, to independently confirm the maximum rank in those cases.

Run: `python3 check_index.py`. Expected output is stored in `check_output.txt`: `VERIFY_OK witness_cases=40 exhaustive_binary_functionals=4232 m_range=1..10 prime_fields=2,3,5,7`.

The numerical checks are finite corroboration only. They do not prove the unbounded formula; the proof above does.

## Relationship to prior work

Gallo and Videla [GV] introduce \(\mathfrak n_G\), give its precise brackets, center and lower-central dimensions, and analyze paths, stars, cycles, and other graph families. Their proofs include arbitrary characteristic for the construction and center. The new statement determines the Kirillov index (equivalently, maximal Kirillov-form rank) for the once-subdivided-star family, which does not follow from center dimension or lower-central dimensions alone. The source does not compute this rank for this tree family. The cases \(m=1,2\) coincide with paths and serve as boundary checks; the nontrivial growing index defect occurs for \(m\ge3\).

Earlier index theory of Lie algebras establishes the invariant and standard alternating-form methods; it does not itself evaluate this family. Two-step graphical Lie algebras and their character-degree/matching enumerations concern distinct Lie brackets from the three-step construction of [GV]. General results about sparse alternating matrices provide tools, not an identified previous instance of the displayed index formula. Any as-yet-unlocated specialized index computation for these graph Lie algebras would affect historical priority.

## Limitations

The theorem is restricted to the exact graph family obtained by subdividing every edge of a star once. It does not determine the index for arbitrary trees or other three-step graph Lie algebras; indeed general trees can have other block-support patterns. It gives the maximum rank, not the full distribution of functional ranks or the number of index-realizing functionals over a finite field. The paper is not independently mathematically audited, and priority is conditional on the accessible comparisons described in the accompanying review.

## References

[GV] Andrea L. Gallo and Denis E. Videla, *Nilpotent Lie algebras of nilpotence class at most three via graphs*, arXiv:2610.33963v1, first public 2026-10-25; Sections 2--4 and 5, https://arxiv.org/abs/2610.33963.

[DK] J. Dixmier, work introducing the index of a Lie algebra (1974), cited only for the standard invariant definition; no specialized family result is attributed here.

[DM] S. G. Dani and M. G. Mainkar, *Anosov automorphisms on compact nilmanifolds associated with graphs*, Transactions of the AMS (2005), the earlier two-step graphical construction, distinguished from [GV] in [GV, Section 2].
