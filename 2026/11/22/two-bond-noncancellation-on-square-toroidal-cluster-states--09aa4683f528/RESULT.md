# Two-bond noncancellation on square toroidal cluster states

## Finding
For every integer \(m\ge2\), let \(G_m=C_{2m}\square C_{2m}\) be the nearest-neighbor square toroidal graph on \(4m^2\) qubits. Prepare its ideal qubit graph state with one controlled-\(Z\) gate per graph edge, and divide the qubits into the equal checkerboard parity classes. For any set \(F\) of **at most two distinct edges**, omit exactly the controlled-\(Z\) gates indexed by \(F\) before preparing the state. Let \(\nu(F)\) be the number of edges in a maximum matching of \(F\), with \(\nu(\varnothing)=0\). The resulting bipartite von Neumann entropy is **exactly**
\[
\boxed{S_m(F)=2m^2-2m+\nu(F)\quad\text{bits},\qquad |F|\le2.}
\]
In particular, either single omitted gate increases entropy by one bit; two omissions with a shared endpoint increase it by one bit; **any two vertex-disjoint omitted gates increase it by two bits**, independent of their relative distance, direction or placement. There is no two-gate entanglement-gain cancellation on any square torus in this family.

For each \(F\), the reduced density matrix has exactly \(2^{S_m(F)}\) equal nonzero eigenvalues, each \(2^{-S_m(F)}\); all positive-order Rényi entropies and the pure-state logarithmic negativity therefore equal \(S_m(F)\) bits.

This rigidity is specific to the square-circumference family. On \(C_4\square C_6\), omitting either edge \(\{(0,0),(0,1)\}\) or \(\{(0,3),(0,4)\}\) increases checkerboard entropy from ten to eleven bits, while omitting both leaves it at ten bits. The two edges have disjoint endpoints.

## Assumptions and scope
Every \(C_{2m}\) is a simple cycle of length at least four, with coordinates modulo \(2m\). The pure stabilizer graph state is prepared from \(|+\rangle^{\otimes4m^2}\) using controlled-\(Z\) gates for precisely the retained graph edges. The fixed parity cut is \(E=\{(x,y):x+y\equiv0\pmod2\}\) versus \(O=\{(x,y):x+y\equiv1\pmod2\}\). All ranks and kernels below are over \(\mathbb F_2\). Omitting a gate means changing the preparation graph; it is not a local operation on an already prepared state. The theorem does not compare other bipartitions or multipartite entanglement measures.

## Proof
**1. Entanglement is binary cut rank.** Write \(B:\mathbb F_2^{E}\to\mathbb F_2^{O}\) for the square binary biadjacency matrix of the intact graph. The standard graph-state character-orthogonality calculation gives \(S_m(F)=\operatorname{rank}_{\mathbb F_2}B_F\), with equal positive Schmidt probabilities, where \(B_F\) is obtained from \(B\) by toggling its entries corresponding to omitted gates. This is the established graph-state bipartite-rank identity, not the new step.

**2. Intact rank.** Identify \(O\) with \(E\) by sending \((x,y)\in E\) to \((x,y+1)\in O\). Then the four neighbors of \((x,y+1)\) in \(E\) are \((x,y)\), \((x+1,y+1)\), \((x-1,y+1)\), and \((x,y+2)\). Consequently, up to the displayed vertex relabeling, \(B=(I+U)(I+V)\), where \(U\) and \(V\) are translations of functions on \(E\) by \((1,1)\) and \((-1,1)\), respectively. Each translation has order \(2m\), and each has exactly \(m\) orbits on the \(2m^2\)-element set \(E\). The two diagonal translations generate the entire group \(E\), and their cyclic subgroups intersect in exactly \(\{0,(m,m)\}\). Thus every \(U\)-orbit intersects every \(V\)-orbit in exactly two sites.

For a cyclic binary shift \(V\), the image of \(I+V\) consists of functions whose sum on each \(V\)-orbit is zero. Each \(U\)-orbit indicator meets each \(V\)-orbit in two points, so \(\ker(I+U)\subseteq\operatorname{im}(I+V)\). The preimage-dimension identity now gives
\[
\dim\ker B=\dim\ker(I+V)+\dim\ker(I+U)=m+m=2m.
\]
Hence \(\operatorname{rank}B=2m^2-2m\).

**3. All distinct coordinate evaluations on the kernel are independent in pairs.** For any site \(a\in E\), evaluation \(\varepsilon_a(f)=f(a)\) is a nonzero linear functional on \(\ker B\), because the constant-one function belongs to \(\ker B\). We show that \(\varepsilon_a\ne\varepsilon_b\) for any distinct \(a,b\in E\). By translation invariance take \(a=0\) and write \(t=b-a\). If \(t\notin\langle U\rangle\), a function constant on \(U\)-orbits separates the sites. If \(t\in\langle U\rangle\setminus\langle V\rangle\), a function constant on \(V\)-orbits separates them. The remaining possible nonzero displacement is \(t=(m,m)=V^m\).

For that displacement, let \(h\) be the indicator of the \(U\)-orbit through zero. The preceding two-intersection observation guarantees a function \(f\) with \((I+V)f=h\); it then satisfies \((I+U)(I+V)f=0\). Along the first \(m\) consecutive \(V\)-steps, one visits all \(m\) distinct \(U\)-orbits exactly once, so
\[
f(0)+f(m,m)=\sum_{j=0}^{m-1}h(V^j0)=1\quad\text{in }\mathbb F_2.
\]
This separates the last pair. Thus evaluations at any two distinct \(E\)-sites are nonzero and distinct, hence linearly independent over \(\mathbb F_2\). Translation by one coordinate step identifies the two parity sides while preserving graph adjacency, so the identical pairwise-independence conclusion applies to coordinate evaluations on \(\ker B^{\mathsf T}\) at distinct \(O\)-sites.

**4. Low-rank update lemma.** Let \(M:V\to W\) be any linear map over a field of rank \(r\). If \(u_1,u_2\in W\) have linearly independent images in \(W/\operatorname{im}M\) and the restrictions of \(v_1^{\mathsf T},v_2^{\mathsf T}\) to \(\ker M\) are linearly independent, then
\[
\operatorname{rank}(M+u_1v_1^{\mathsf T}+u_2v_2^{\mathsf T})=r+2.
\]
To prove this, choose domain and codomain bases putting \(M\) in the block form \(\operatorname{diag}(I_r,0)\). Independence of the two projected \(u\)'s and restricted \(v\)'s permits invertible row and column changes fixing this block while sending the update into a nonsingular two-by-two block in the lower-right null block. The rank is therefore \(r+2\). The analogous rank-one statement holds for a nonzero quotient vector and a functional nonzero on the kernel.

**5. Apply to any pair of missing gates.** For an omitted edge \(e=\{u,v\}\), with \(u\in O\), \(v\in E\), toggling its \(1\)-entry adds \(e_u e_v^{\mathsf T}\) to \(B\) over \(\mathbb F_2\). The coordinate evaluation at every individual endpoint is nonzero on the appropriate kernel. Two vertex-disjoint edges have distinct endpoints on both shores, so Step 3 and the rank-two lemma give an exact two-rank increase. If the two edges share their \(O\)-endpoint, the update is instead \(e_u(e_v+e_w)^{\mathsf T}\), and the two distinct input evaluations have nonzero sum on \(\ker B\); the rank-one lemma gives an exact one-rank increase. The analogous argument applies if they share their \(E\)-endpoint. A single edge is the rank-one case. Since a simple graph's two distinct edges cannot share both endpoints, these are all possibilities. Step 1 converts the rank formula to the claimed entropy and flat spectrum.

**6. Sharp nonsquare boundary.** For the stated \(C_4\square C_6\) pair, direct binary elimination gives intact cut rank ten, single-deletion ranks eleven, and joint-deletion rank ten. The accompanying fully specified finite calculation reproduces this boundary example independently; the all-size square result did not rely on that computation.

## Verification
Run `python checker.py` using the standard Python library. The checker builds each actual even-to-odd biadjacency matrix from four distinct neighbors and computes exact binary ranks by integer-bit elimination, independently of the diagonal-orbit argument. It checks every single edge for torus sizes \(C_{2m}\square C_{2m}\) with \(2\le m\le8\). For \(2\le m\le5\), it exhausts **every unordered pair** of edges, including intersecting and disjoint pairs; for \(6\le m\le8\), it samples 1,800 distinct pairs per size with a fixed seed. Altogether 36,480 exact pair comparisons pass. It also reproduces the nonsquare \(C_4\square C_6\) contrast. `checker-output.txt` gives the actual recorded output. These finite tests corroborate, but do not replace, Steps 1–5 for all integers \(m\ge2\).

## Relationship to prior work
The graph-state binary bipartition-rank identity, flat Schmidt-spectrum property, and general single-edge rank bounds are classical; see Hein, Eisert and Briegel (2003) and Hein et al. (2006). The separately published *Commensurability deficit and single-bond entanglement gain in periodic square cluster states* already proves the intact rectangular-torus formula and an exact one-bit gain for **one** omitted gate. Both facts are used here and are not claimed as new. The separately published *Paired omitted-bond cancellation in three-dimensional toroidal cluster states* proves that **two disjoint** missing bonds can cancel each other's individual entanglement gains on a particular three-dimensional torus family; its construction does not imply this two-dimensional, all-location **noncancellation** theorem. The new result is the complete two-distinct-edge law on every square torus, proved by pairwise separation of nullspace-coordinate functionals. Unlike an isolated one-edge bound, it supplies a global two-error classification and a sharp nonsquare counterexample.

## Limitations
This is an ideal, pure, binary qubit graph-state statement for square periodic grids of even circumference at least four. It does not cover three or more omitted gates, general rectangles, arbitrary bipartitions, composite qudits, or noisy gates. The word “noncancellation” concerns checkerboard bipartite entanglement change only; no fault tolerance, computational advantage, or statement about already-prepared states follows. Historical priority for the exact two-edge statement is not independently certified, particularly against unindexed binary-grid rank literature.

## References
1. M. Hein, J. Eisert, H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (first publicly submitted 2003-07-18). https://arxiv.org/abs/quant-ph/0307130
2. M. Hein, W. Dür, J. Eisert, R. Raussendorf, M. Van den Nest, H.-J. Briegel, *Entanglement in Graph States and its Applications*, arXiv:quant-ph/0602096 (first publicly submitted 2006-02-11). https://arxiv.org/abs/quant-ph/0602096
3. *Commensurability deficit and single-bond entanglement gain in periodic square cluster states*, publicly accessible research record, 2026-11-02. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-commensurability-deficit-and-single-bond-entanglement-gain-in-pe--bcc73b58c68a/RESULT.md
4. *Paired omitted-bond cancellation in three-dimensional toroidal cluster states*, publicly accessible research record, 2026-11-02. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-paired-omitted-bond-cancellation-in-three-dimensional-toroidal-c--06ff2b1986a2/RESULT.md
