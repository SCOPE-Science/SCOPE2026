# Integral homotopy and component-lattice classification of higher tolerance complexes of graphs

## Finding
Let \(G=(V,E)\) be any finite simple graph with \(n=|V|\ge4\), and let \(K(G)\) be its **unfilled one-dimensional** simplicial complex: the vertices and edges of \(G\), with no higher faces, even where \(G\) has triangles. Let \(2\le t\le n-2\). Put \(c=|\pi_0(G)|\), and let \(i_{t+2}(G)\) count independent vertex sets of cardinality \(t+2\). Define
\[
B_t=\binom{c-1}{t+1},\qquad
B_{t+1}=\binom n{t+2}-i_{t+2}(G)-\binom{n-1}{t+1}+\binom{c-1}{t+1}.
\]
Here \(\binom ab=0\) if \(b>a\). Then \(B_{t+1}\) is a nonnegative integer and the entire *integral homotopy type* is
\[
\left|\mathcal T_t(K(G))\right|\simeq
\bigvee^{B_t}S^t\ \vee\ \bigvee^{B_{t+1}}S^{t+1}.
\]
Moreover, with \(C=\pi_0(G)\) and the component augmentation lattice \(W_C=\ker(\mathbb Z^C\overset{\sum}{\longrightarrow}\mathbb Z)\), there is an isomorphism, natural under all graph automorphisms,
\[
\widetilde H_t(\mathcal T_t(K(G));\mathbb Z)\cong\bigwedge^{t+1}W_C.
\]
All other reduced integral homology groups, except those in dimensions \(t\) and \(t+1\), vanish. For \(t\ge n-1\), the tolerance complex is a simplex and hence contractible.

## Assumptions and scope
The graph is simple, undirected, loopless, and may be disconnected or contain isolated vertices. A face belongs to \(\mathcal T_t(K)\) precisely when deletion of at most \(t\) vertices makes it a face of \(K\). Thus \(X=\mathcal T_t(K(G))\) contains **every** vertex set of size at most \(t+1\); its \((t+1)\)-dimensional simplices are exactly the \((t+2)\)-subsets containing a graph edge; it has no higher simplices. The dimension bound follows from the input complex being one-dimensional, regardless of graph triangles. No convention of filling graph cliques is allowed.

## Proof
**1. Integral chain model.** Set \(L=\mathbb Z^V\) with basis \(e_v\), and let \(\epsilon:L\to\mathbb Z\) send every basis element to \(1\). Write \(W=\ker\epsilon\). Give the oriented simplicial chain complex of the full simplex its usual exterior-algebra model \(\widetilde C_q\cong\bigwedge^{q+1}L\), with boundary the degree-minus-one derivation \(\partial(e_v)=1\). After splitting \(L=\mathbb Z e_o\oplus W\) using any vertex \(o\), its cycle lattice in degree \(t\) is exactly \(\bigwedge^{t+1}W\): indeed \(\partial(e_o\wedge z)=z\) and \(\partial z=0\) for \(z\in\bigwedge W\). Because \(X\) contains the full \(t\)-skeleton, the same assertion holds for its degree-\(t\) cycles.

**2. Top-boundary image, integrally and without torsion.** For distinct \(u,v,a_1,\ldots,a_t\), the boundary of the oriented \((t+1)\)-simplex on these vertices, up to its orientation sign, is
\[
\partial(e_u\wedge e_v\wedge e_{a_1}\wedge\cdots\wedge e_{a_t})
=(e_v-e_u)\wedge(e_{a_1}-e_u)\wedge\cdots\wedge(e_{a_t}-e_u).
\]
For each fixed graph edge \(uv\in E\), the vectors \(e_v-e_u\) together with \(e_a-e_u\) for \(a\notin\{u,v\}\) form an integral basis of \(W\). Consequently the boundaries of all allowed top simplices containing \(uv\) generate exactly \((e_v-e_u)\wedge\bigwedge^t W\). Let
\[
U=\langle e_v-e_u:uv\in E\rangle_{\mathbb Z}\subseteq W.
\]
Summing over graph edges gives, **as an equality of integral sublattices**,
\[
\operatorname{im}\partial_{t+1}=U\wedge\bigwedge^t W.
\]
The component projection \(L\to\mathbb Z^C\), \(e_v\mapsto e_{[v]}\), restricts to a surjection \(W\to W_C\), with kernel precisely \(U\). To see integrality and saturation, take a spanning tree in every graph component: its edge differences form a primitive basis for \(U\), extendible to a basis of \(W\) by differences of component representatives. Therefore \(W/U\cong W_C\) is free of rank \(c-1\). Exterior algebra over the integers now yields
\[
\widetilde H_t(X;\mathbb Z)
=\frac{\bigwedge^{t+1}W}{U\wedge\bigwedge^t W}
\cong\bigwedge^{t+1}(W/U)
\cong\bigwedge^{t+1}W_C.
\]
All maps commute with graph automorphisms, proving the claimed naturality. The boundary image has rank \(\binom{n-1}{t+1}-\binom{c-1}{t+1}\), and its quotient is torsion-free.

**3. Top homology and exact multiplicities.** The number of allowed \((t+1)\)-simplices is \(F=\binom n{t+2}-i_{t+2}(G)\). Since there are no simplices of dimension \(t+2\), the top homology is \(\ker\partial_{t+1}\), a free abelian group of rank
\[
F-\operatorname{rank}\operatorname{im}\partial_{t+1}
=F-\binom{n-1}{t+1}+\binom{c-1}{t+1}=B_{t+1}.
\]
This proves its nonnegativity. The full \(t\)-skeleton is \((t-1)\)-connected, so \(X\) is \((t-1)\)-connected. Thus all other reduced homology vanishes.

**4. Homotopy, not just homology.** The full \(t\)-skeleton of an \((n-1)\)-simplex has homotopy type \(\bigvee^{\binom{n-1}{t+1}}S^t\), as follows by collapsing the closed star of a chosen vertex and using the standard relative CW description. The \((t+1)\)-simplices of \(X\) attach \((t+1)\)-cells to this wedge. For \(t\ge2\), Hurewicz identifies the attaching groups \(\pi_t\) with integral \(H_t\), so their attaching maps are determined by their integral cellular-boundary columns. Step 2 proves that their image is a primitive direct summand. Apply unimodular changes of basis to diagonalize the matrix to a block \(I_r\) and zeros; changes of \(t\)-sphere basis are realized by homotopy self-equivalences, and changes of \((t+1)\)-cell basis by standard cell slides. Each unit pair cancels, while zero columns attach nullhomotopically. The resulting CW complex is exactly a wedge of \(B_t\) spheres in dimension \(t\) and \(B_{t+1}\) spheres in dimension \(t+1\). This establishes the claimed integral homotopy equivalence. The argument explicitly uses \(t\ge2\); it does not infer the fundamental group of the \(t=1\) case from homology.

## Verification
Run `python3 verify.py` with Python's standard library only. The checker constructs every allowed top simplex, independently forms its simplicial boundary over \(\mathbb F_2\), and compares exact ranks with the component formula. It exhaustively checks every labelled graph on \(4,5,6\) vertices (32,960 graphs, 100,416 graph-tolerance pairs) and 1,000 deterministic seven-vertex graphs across four tolerance values (4,000 more pairs). Total: **104,416 passed finite instances**. This finite testing does not establish integral saturation or general homotopy, which instead follow from the proof above.

As informative examples, for the unfilled cycle on six vertices at tolerance two one gets \(\bigvee^5S^3\); the eight-cycle yields \(\bigvee^{33}S^3\). With six vertices and only the two disjoint edges \(01\) and \(23\) (plus two isolated vertices), tolerance two gives the mixed-dimensional type \(S^2\vee S^3\vee S^3\). In contrast, a connected graph always has \(B_t=0\), while a graph with at least \(t+2\) components can carry nonzero lower-degree homology.

## Relationship to prior work
Kim and Lew introduced tolerance complexes and established general Leray-number bounds (arXiv:2109.03030, first public 2021-09-07). Selvaraja's 2026 study establishes collapsibility and Leray bounds in chordal and related settings and works at arbitrary tolerance (arXiv:2611.14384, first public 2026-11-10). These bounds do not supply the integral homotopy decomposition or the natural component exterior-power lattice above. Kim and Lew's bounded-independence graph complexes (arXiv:1912.12605) concern a different, generally higher-dimensional simplicial complex; its degree-\(t+1\) truncation is not in general this tolerance complex. Previously available exact one-tolerance classifications are the \(t=1\) boundary case and do not give the higher-tolerance exterior-power calculation or the proof of nullhomotopic higher attachments.

## Limitations
The input is strictly an unfilled one-dimensional graph complex, not a clique complex. The theorem covers integers \(t\ge2\) and gives no general statement for tolerance complexes of higher-dimensional inputs. The decomposition is nonequivariant; only the displayed integral lower-degree lattice is asserted naturally. The theorem does not classify the integral module carried by top homology. The finite tests use characteristic two and are not substitutes for the integral proof. No independent mathematical audit or exhaustive priority certification has been performed.

## References
- S. Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers*, arXiv:2611.14384, 2026-11-10. https://arxiv.org/abs/2611.14384
- M. Kim and A. Lew, *Leray numbers of tolerance complexes*, arXiv:2109.03030, 2021-09-07. https://arxiv.org/abs/2109.03030
- M. Kim and A. Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605, 2019-12-29. https://arxiv.org/abs/1912.12605
- R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145. Standard CW-cell cancellation context; the proof here uses only elementary chain and CW-homotopy arguments.
