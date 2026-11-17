# Complete coordinate-symmetry homology of three-factor categorical complete-graph products

## Finding
For integers \(m,n\ge2\), let \(K_k\) denote the simple complete graph, let \(\times\) denote the categorical graph product, and put \(X_{m,n}=\operatorname{Ind}(K_2\times K_m\times K_n)\). For \(k\ge2\), let \(U_k=\ker(\mathbb Q^k\stackrel{\varepsilon}{\longrightarrow}\mathbb Q)\), where \(\varepsilon\) sums coordinates. The natural action of \(S_m\times S_n\) on the second and third graph coordinates induces
\[
\widetilde H_3(X_{m,n};\mathbb Q)\cong
(\operatorname{Sym}^2U_m\otimes\operatorname{Sym}^2U_n)
\oplus(U_m\otimes\bigwedge^2U_n)
\oplus(\bigwedge^2U_m\otimes U_n)
\oplus(\bigwedge^2U_m\otimes\bigwedge^2U_n).
\]
All other reduced rational homology vanishes. If \(f\) and \(h\) count fixed letters and \(s\) and \(t\) count two-cycles of \(\sigma\in S_m\) and \(\tau\in S_n\), respectively, then
\[
\chi_3(\sigma,\tau)=\frac{(f-1)(h-1)(fh-2)}{2}+2st.
\]
In particular the invariant subspace has dimension exactly one for every \(m,n\ge2\), so \(|X_{m,n}|/(S_m\times S_n)\) has the rational homology of \(S^3\).

## Assumptions and scope
The categorical product has two vertices adjacent precisely when they are adjacent in **every** factor; this is not the Cartesian or strong graph product. Each graph is finite, loopless and simple. The theorem concerns rational representations of the specified coordinate-relabeling subgroup, not the full automorphism group (which includes further symmetries). It does not assert an integral module decomposition.

## Proof
**1. A canonical homology suspension.** Denote the two first-coordinate layers by \(A\) and \(B\), each identified with the \(m\)-by-\(n\) cell set \([m]\times[n]\). Both are independent vertex sets. Between layers, \(a_{ij}\sim b_{kl}\) exactly if \(i\ne k\) **and** \(j\ne l\). Let \(\Delta_A\) be the full simplex on \(A\), and let \(Z=\bigcup_{b\in B}\operatorname{st}_{X_{m,n}}(b)\), the union of closed vertex stars. Each nonempty finite intersection of these stars contains the simplex on its indexing subset of \(B\), since all of \(B\) is independent; hence every intersection is contractible. Their nerve is a full simplex, so the ordinary nerve theorem gives contractible \(Z\). Every face belongs to \(\Delta_A\) or \(Z\). The intersection \(Y=\Delta_A\cap Z\) has precisely those subsets of cells that are contained in a *cross* \(R_i\cup C_j\), the union of some row and some column. The Mayer–Vietoris connecting isomorphism \(\widetilde H_3(X_{m,n};\mathbb Q)\simeq\widetilde H_2(Y;\mathbb Q)\) is canonical and \(S_m\times S_n\)-equivariant. The nonequivariant homotopy theorem of Antolín Camarena and Carnero Bravo (Proposition 25, cited below) proves that these are the only nonzero reduced rational homology groups and that their common rank is \((m-1)(n-1)(mn-2)/2\).

**2. Signed fixed-face count.** Fix \(g=(\sigma,\tau)\) and write \(f,h,s,t\) as in the finding. For a set \(E\) of cells stable under \(g\), the signed simplicial trace of its oriented simplex is \((-1)^{|E|-c(E)}\), where \(c(E)\) is the number of \(g\)-orbits contained in \(E\). Including the empty simplex, define \(F_Y(g)=\sum_{E\in Y,\ gE=E}(-1)^{c(E)}\). Since the reduced homology of \(Y\) is concentrated in degree two, the reduced Lefschetz formula gives \(\chi_3(g)=-F_Y(g)\). This includes the augmentation/empty-face contribution and fixes its sign.

**3. Classify cross-covered faces.** A face of \(Y\) is uniquely classified as: empty; a singleton; a subset with at least two cells lying in one row; a subset with at least two cells lying in one column; a two-element *diagonal pair* with different rows and columns; or a face containing at least three cells, not lying in any single row or column. A face of the last type has a **unique** covering cross: the intersection of two distinct crosses is either a single row, a single column or at most two cells. Stable faces with a unique covering cross must have a stable (hence fixed) row index and a stable (hence fixed) column index.

The respective contributions to \(F_Y(g)\) from empty, singleton, row-only and column-only types are \(1\), \(-fh\), \(f(h-1)\) and \(h(f-1)\). For row-only subsets of a fixed row, this follows by subtracting the empty and singleton terms from the zero total over all stable subsets of that row. The same argument applies to columns.

A stable diagonal pair is either fixed cellwise or interchanged. The former occur in \(2\binom f2\binom h2=fh(f-1)(h-1)/2\) ways and contribute \(+1\); the latter occur in exactly \(2st\) ways and contribute \(-1\). Thus the total diagonal-pair contribution is \(fh(f-1)(h-1)/2-2st\).

For each fixed cross \(R_i\cup C_j\), the signed sum over all its stable subsets is zero, since its nonempty orbit set yields a product of factors \((1-1)\). Within this cross subtract the contributions of the empty set, its \(f+h-1\) fixed singleton cells, its \(h-1\) row-only and \(f-1\) column-only contributions, and its \((f-1)(h-1)\) stable diagonal pairs (which must be pointwise fixed because the two arms are separately invariant). The remainder, the signed contribution of faces with at least three cells and unique covering cross, is \(-(f-1)(h-1)\). There are exactly \(fh\) fixed crosses.

Adding the six disjoint classes gives
\[
F_Y(g)=1-fh+f(h-1)+h(f-1)+\frac{fh(f-1)(h-1)}2-2st-fh(f-1)(h-1)
=-\frac{(f-1)(h-1)(fh-2)}2-2st,
\]
proving the character formula, uniformly including zero fixed-point counts and small parameters.

**4. Identify the module.** Let \(\mathcal D\) be the permutation set of unordered diagonal pairs of the \(m\)-by-\(n\) board. Such a pair is fixed by \(g\) precisely when it is fixed cellwise or interchanged; hence its permutation character is \(fh(f-1)(h-1)/2+2st\). The augmentation tensor \(U_m\otimes U_n\) has character \((f-1)(h-1)\). Therefore the proved character is that of the virtual module \(\mathbb Q[\mathcal D]-(U_m\otimes U_n)\). Let \(P_k=\mathbb Q^k=\mathbf1\oplus U_k\). In the rational representation ring,
\[
\mathbb Q[\mathcal D]=\operatorname{Sym}^2(P_m\otimes P_n)-\operatorname{Sym}^2(P_m)\otimes P_n-P_m\otimes\operatorname{Sym}^2(P_n)+P_m\otimes P_n.
\]
Apply \(\operatorname{Sym}^2(V\otimes W)=(\operatorname{Sym}^2V\otimes\operatorname{Sym}^2W)\oplus(\bigwedge^2V\otimes\bigwedge^2W)\), \(\operatorname{Sym}^2(P_k)-P_k=\operatorname{Sym}^2U_k\), and \(\bigwedge^2P_k=U_k\oplus\bigwedge^2U_k\). Subtract \(U_m\otimes U_n\) to obtain exactly the four genuine summands in the finding. Rational character equality for a finite group implies module isomorphism.

**5. Quotient.** The standard augmentation module has no invariant vectors and its second exterior power has no invariant vectors for each \(k\ge2\). Its second symmetric power has exactly one invariant line (the invariant inner product). Thus precisely one copy of the trivial module occurs, in \(\operatorname{Sym}^2U_m\otimes\operatorname{Sym}^2U_n\). The rational transfer/averaging theorem for a finite simplicial group action identifies quotient-space rational homology with invariants, proving the quotient statement.

## Verification
The standalone `verify.py` reconstructs the graph, cross complex, signed Lefschetz traces and predicted characters independently. Its recorded run checks 104 combined cross-character cases, 19 additional direct original-complex Lefschetz cases, and mod-two simplicial boundary ranks for \((m,n)=(2,2),(2,3),(3,3)\). These finite tests corroborate but do not replace the all-parameter argument. See `verify.out` for actual results.

## Relationship to prior work
Antolín Camarena–Carnero Bravo (2023), Proposition 25, gives precisely the nonequivariant wedge of \((m-1)(n-1)(mn-2)/2\) three-spheres for this product. Its accessible proof on pages 27–30 was read; it does not give the coordinate permutation representation or character formula. Goyal–Shukla–Singh (2019), Proposition 3.2, concerns the **two-factor** product \(K_m\times K_n\), a different graph and a one-dimensional wedge. Related published graph-product constructions do not imply the representation here. The proof above independently derives the equivariant refinement from the cross-cover complex.

## Limitations
The statement uses rational coefficients and the specified \(S_m\times S_n\) subgroup. It does not determine the extra first-factor layer-exchange action or the equal-size coordinate-interchange action, integral module structure, equivariant homotopy type, or induced maps between parameter values. Related unindexed or inaccessible mathematical literature could contain an equivalent character formula.

## References
1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first public 2023-07-23), especially Proposition 25. https://arxiv.org/abs/2307.12401
2. S. Goyal, S. Shukla and A. Singh, *Topology of independence complexes of categorical products of complete graphs*, arXiv:1905.06926 (2019), especially Proposition 3.2. https://arxiv.org/abs/1905.06926
