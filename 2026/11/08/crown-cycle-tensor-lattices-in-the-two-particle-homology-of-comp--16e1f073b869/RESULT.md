# Crown-cycle tensor lattices in the two-particle homology of complete bipartite graphs

## Finding
For integers \(p,q\geq3\), let \(G=K_{p,q}\) be the geometric realization of the complete bipartite graph, and let
\[
F_2(G)=\{(x,y)\in G\times G:x\neq y\}
\]
be its **ordered, collision-free** two-point configuration space. Define the crown graph \(\operatorname{Cr}_k=K_{k,k}\setminus\{\{i_L,i_R\}:1\leq i\leq k\}\), and its integral cycle lattice \(L_k=H_1(\operatorname{Cr}_k;\mathbb Z)\). Both copies of \(\{1,\dots,k\}\) in this definition are labeled.

There is an explicit integral isomorphism, natural for independent permutations of the two parts,
\[
\boxed{H_2(F_2(K_{p,q});\mathbb Z)\;\cong\;L_p\otimes_{\mathbb Z}L_q.}
\]
It is an isomorphism of **integral lattices**, not merely of rational characters. Each \(L_k\) has rank \(r_k=k^2-3k+1\), hence \(H_2\) is free of rank \(r_pr_q\).

Let \(T_k:L_k\to L_k\) transpose the endpoints of every ordered crown edge \((i,j)\mapsto(j,i)\), expressed in the common orientation from its left to its right copy. (This is the negative of the geometric copy-switch on oriented crown edges.) The particle exchange \(\tau(x,y)=(y,x)\) acts under the displayed isomorphism by
\[
\boxed{\tau_*=-T_p\otimes T_q.}
\]
For \(p=q=n\), the graph automorphism exchanging the two bipartition classes acts by swapping the two lattice factors, with no extra sign, after using the matching labels on both classes. These formulas, together with independent vertex relabelings, determine the entire natural integral action of \(\operatorname{Aut}(K_{p,q})\) and particle exchange.

In particular, for \(a\in S_p,b\in S_q\), write \(f_a,f_b\) for their fixed-point counts and \(t_a,t_b\) for their two-cycle counts. The complete rational character on second homology is
\[
\chi_2(a,b)= (f_a^2-3f_a+1)(f_b^2-3f_b+1),\qquad
\chi_2((a,b)\tau)=-(2t_a-1)(2t_b-1).
\]
In the balanced case, choose a part-exchanger \(s\) that maps the two classes by the common label identity. Then, for \(a,b\in S_n\), \(\chi_2((a,b)s\tau^e)=(-1)^e(f_{ab}^2-3f_{ab}+1)\), where \(e\in\{0,1\}\). Thus the result also covers the additional class-exchanging symmetries that occur when \(p=q\).

## Assumptions and scope
All graphs are finite one-dimensional simplicial complexes, with each edge a closed interval and configurations disallowing collisions **anywhere**, including vertices. The number of particles is exactly two and they are ordered. The domain \(p,q\ge3\) is essential: for smaller parts the crown graphs are disconnected, and the stated lattice identification is not asserted. Graph automorphisms are induced by permutations of vertices respecting the adjacency relation; when \(p=q\), interchanging the two classes is included. The tensor factors and their signs refer to the orientation of every original graph edge from the first bipartition class to the second, and every crown edge from its left to its right copy.

The result identifies degree-two integral homology and its symmetry action. Farber and Hanbury already determined the ordinary integral Betti ranks for these spaces. In particular their mature-graph theorem gives \(H_1(F_2(G);\mathbb Z)\cong H_1(G;\mathbb Z)\oplus H_1(G;\mathbb Z)\) via the inclusion into \(G\times G\); this earlier fact is not claimed as new.

## Proof
**1. Discretization and chains.** For a graph with at least three edges in each noncontractible embedded cycle, the standard two-point deleted-product cubical complex is a deformation retract of its two-point configuration space. Here \(K_{p,q}\) has girth four, and all paths connecting essential vertices have positive length, so this applies. Its cells are precisely \(\sigma\times\eta\), where the closed simplices \(\sigma,\eta\) of \(G\) are vertex-disjoint. It has dimension two, so \(H_2\) is literally the integral kernel of its second cellular boundary, with no quotient by three-cell boundaries.

Orient original edges \(e_{ij}\) from left vertex \(i\) to right vertex \(j\). Two-cells are \(e_{ij}\times e_{k\ell}\) with \(i\ne k\), \(j\ne\ell\), oriented by this ordered product. Their coefficient group is exactly \(A_p\otimes A_q\), where
\[
A_m=\mathbb Z\langle(i,k):1\le i,k\le m,\ i\ne k\rangle,
\]
and \((i,k)\otimes(j,\ell)\) represents \(e_{ij}\times e_{k\ell}\).

**2. Exact boundary constraints.** The product boundary is
\[
\partial(e_{ij}\times e_{k\ell})=
(v_j,e_{k\ell})-(u_i,e_{k\ell})-(e_{ij},v_\ell)+(e_{ij},u_k).
\]
Its four families of coefficients are, respectively, sums of the two-cell coefficients over \(i\), over \(j\), over \(k\), and over \(\ell\), with the other three indices fixed. Hence \(\partial z=0\) **if and only if** all first- and second-endpoint sums in each of the two ordered-pair factors vanish. Explicitly, define
\[
d_m:A_m\longrightarrow\mathbb Z^m\oplus\mathbb Z^m,
\qquad d_m(i,k)=(e_i,e_k).
\]
The equations are exactly \((d_p\otimes1)z=0\) and \((1\otimes d_q)z=0\). In \(\operatorname{Cr}_m\), identifying a directed edge from \(i_L\) to \(k_R\) with \((i,k)\) identifies \(\ker(d_m)\) with the ordinary graph cycle lattice: using all-positive rather than signed incidence merely multiplies the left vertex rows by \(-1\).

**3. Integral intersection, not a field argument.** For \(m\ge3\), \(\operatorname{Cr}_m\) is connected. Its incidence-image quotient is \(\mathbb Z\), so \(\operatorname{im}(d_m)\) is free and \(A_m/\ker(d_m)\) is free. Therefore \(\ker(d_m)\) is a direct summand of the free abelian group \(A_m\). Choose (noncanonical) complements \(A_p=L_p\oplus B_p\) and \(A_q=L_q\oplus B_q\). Then the simultaneous kernel of \(d_p\otimes1\) and \(1\otimes d_q\) is **exactly** \(L_p\otimes L_q\); the other three direct summands have a nonzero image under at least one map. This identification itself is canonical because it is the inclusion of the common kernel. Since a connected crown has \(m(m-1)\) edges and \(2m\) vertices, its first Betti rank is \(m(m-1)-2m+1=m^2-3m+1\). This proves the integral theorem, with no torsion or unproved finite-to-infinite extrapolation.

**4. Actions and orientations.** A pair \((a,b)\in S_p\times S_q\) sends \((i,k)\otimes(j,\ell)\) to \((a(i),a(k))\otimes(b(j),b(\ell))\), preserving both edge orientations. Exchanging the two particles sends \(e_{ij}\times e_{k\ell}\) to \(-e_{k\ell}\times e_{ij}\), because exchanging the two one-dimensional factors changes the product orientation by \(-1\). Thus the map on the tensor coefficients is \(-T_p\otimes T_q\). When \(p=q\), switching graph parts reverses each of the two edge orientations, whose signs cancel, and interchanges the crown factors. All these maps preserve the common kernel, establishing the integral symmetry statements.

**5. Character calculation.** On \(A_m\), an ordinary label permutation \(a\) has trace \(f_a(f_a-1)\), while it has trace \(2f_a\) on the target of \(d_m\). The rank-one cokernel has trace one, hence \(\operatorname{tr}(a\mid L_m)=f_a^2-3f_a+1\). On \(A_m\), transpose followed by \(a\) fixes precisely the two directed edges associated to each two-cycle, for trace \(2t_a\). On the target of \(d_m\), transpose swaps its two \(m\)-dimensional summands, giving trace zero; on the one-dimensional cokernel it acts by \(-1\), so the trace on the image of \(d_m\) is one. Therefore \(\operatorname{tr}(aT_m\mid L_m)=2t_a-1\). The tensor-product and particle-exchange formulas follow. Finally, the trace of a flip composed with \(a\otimes b\) on \(L_n\otimes L_n\) equals \(\operatorname{tr}(ab\mid L_n)\). Because the transpose commutes with all label permutations and satisfies \(T_n^2=1\), adding particle exchange changes this trace by a factor of \(-1\). This proves the balanced formulas.

## Verification
The standalone standard-library program `verify.py` constructs every cellular product boundary independently for \((p,q)\in\{(3,3),(3,4),(4,4),(3,5)\}\). It builds integral fundamental-cycle bases of each crown, checks that every tensor generator has zero actual two-cell boundary, and checks the rank of the full two-cell boundary over \(\mathbb F_{101}\). The uniform proof handles the integral saturation; finite rank checks are supporting experiments only. The program also enumerates all \(4,176\) indicated side-preserving, part-exchanging (where available), and particle-exchanging symmetry actions, computes the full cellular signed Lefschetz traces independently, and compares them with the claimed formulas. The program and exact output are included; run `python3 verify.py` in the directory containing the files. See `VERIFICATION.md` for scope and limits.

## Relationship to prior work
Farber–Hanbury (2010), Proposition 22 and Corollary 24, prove that the complete bipartite graphs in this range are mature and give \(b_2=(p^2-3p+1)(q^2-3q+1)\) and \(b_1=2(p-1)(q-1)\). Their Proposition 2 gives a general kernel description through an intersection form. The present result identifies that particular **integral kernel as a tensor of crown-graph cycle lattices**, compatible with every graph automorphism and the particle involution; the Betti rank itself is not new.

Ramos–Yun (first preprint June 11, 2026), Theorem 3.16 and Table 3, give the **rational diagonal-\(S_n\)** and particle-label representation of the ordinary two-particle \(K_{n,n}\) configuration for \(n\ge8\) (with finite tables for smaller sizes). Their work already covers this restriction of the present rational character. It does not identify the integral crown-cycle tensor lattice, the independent \(S_p\times S_q\) factors for all unequal part sizes, or the bipartition-exchanging automorphisms. These are the claimed refinements, not a reannouncement of the diagonal rational representation.

An indexed result on two-particle **sink** configurations of \(K_{p,q}\) permits collisions at original vertices and computes different homology modules. It is not the ordinary collision-free configuration space considered here; the difference is essential already at \(K_{3,3}\), where the sink space has rank seven in second homology and the ordinary space rank one.

## Limitations
No equivariant homotopy classification, cup-product computation, higher-particle theorem, or statement for \(p<3\) or \(q<3\) is asserted. The classification of ordinary Betti ranks and the diagonal rational representation have been previously published and are not new. A mathematically equivalent integral identification in unindexed earlier literature cannot be excluded by targeted searches, and independent verification has not been carried out.

## References
1. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, first preprint May 13, 2010, arXiv:1005.2300, *Algebraic & Geometric Topology* **10** (2010), 2203–2227; especially Proposition 2, Proposition 22 and Corollary 24. https://arxiv.org/abs/1005.2300 and https://msp.org/agt/2010/10-4/agt-v10-n4-p11-p.pdf
2. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, first preprint March 12, 2009, arXiv:0903.2180, *Algebraic & Geometric Topology* **9** (2009), 593–624. https://arxiv.org/abs/0903.2180
3. E. Ramos and C. He Yun, *Computing stable homology representations of graph configuration spaces*, first preprint June 11, 2026, arXiv:2606.13813; section 3.3, Theorem 3.16, Table 3. https://arxiv.org/html/2606.13813v1
4. *Integral homology and particle-swap modules of two-point sink configurations on complete bipartite graphs*, published published-finding corpus record `2026/10/11/SCOPE-integral-homology-and-particle-swap-modules-of-two-point-sink-co--54bc5453d692`, especially Finding, Proof and Relationship to prior work. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-homology-and-particle-swap-modules-of-two-point-sink-co--54bc5453d692
