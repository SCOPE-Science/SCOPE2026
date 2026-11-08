# Row-exchange quotients of linear hexagonal-chain independence complexes are spheres

## Finding
For each integer \(n\geq1\), let \(G_n\) be the undirected linear chain of \(n\) hexagons defined below, and let \(h\) exchange its two rows. The **geometric** orbit quotient of its simplicial independence complex has the integral homotopy type
\[
\left|\operatorname{Ind}(G_n)\right|/\langle h\rangle\simeq S^n.
\]
Moreover, the top integral homology of the unquotiented complex is the free rank-one integral permutation lattice
\[
\widetilde H_n\bigl(\operatorname{Ind}(G_n);\mathbb Z\bigr)\cong\mathbb Z[C_2]
\]
under row exchange. In particular, the quotient has \(\widetilde H_n\cong\mathbb Z\) and all other reduced integral homology zero. This is a statement about the geometric orbit space, **not** the Borel homotopy quotient.

## Assumptions and scope
The vertex set of \(G_n\) is
\[
V(G_n)=\{(r,j):r\in\{0,1\},\ 1\leq j\leq 2n+1\}.
\]
For each row, connect consecutive positions \((r,j)\) and \((r,j+1)\), and add a vertical rung between \((0,j)\) and \((1,j)\) precisely for odd \(j\). Thus \(G_1\) is the unfilled six-cycle, and each additional hexagon shares a vertical edge with the previous one. A face of \(\operatorname{Ind}(G_n)\) is a subset of graph vertices with no graph edge. Let \(h(r,j)=(1-r,j)\). Its action on the geometric realization permutes simplex vertices affinely.

We use the published theorem of Chandrakar and Singh [1, Theorem 3.1] that, for all \(n\ge1\),
\[
\operatorname{Ind}(G_n)\simeq S^n\vee S^n.
\]
This nonequivariant homotopy equivalence is a prior input, not a new result. The new assertions concern the integral involution lattice and the geometric quotient homotopy type.

## Proof
**1. The entire fixed-point space is a simplex.** Write \(X_n=|\operatorname{Ind}(G_n)|\) and \(F_n=X_n^h\). A fixed point of the affine simplex action has an \(h\)-invariant supporting face. Since no graph vertex is fixed, such a face is a union of full two-vertex row-exchange orbits. The orbit at column \(j\) is disallowed exactly when \(j\) is odd, because there it is a rung. At even columns, the two vertices are nonadjacent, and unions of distinct even-column pairs are independent: even columns differ by at least two, and graph horizontals join only consecutive columns. There are exactly \(n\) permissible orbit pairs. Their invariant barycentric coordinates form an ordinary simplex on the \(n\) corresponding pair midpoints. Hence
\[
F_n\cong\Delta^{n-1}
\]
for every \(n\ge1\). In particular it is nonempty and contractible.

**2. An integral module lemma.** We prove a finite-dimensional special case suited to this action. Suppose a finite simplicial complex \(X\) has a simplicial involution \(h\), contractible nonempty fixed set \(F\), and homotopy type \(S^n\vee S^n\) for some \(n\ge1\). Then the integral involution module \(M=H_n(X,F;\mathbb Z)\cong\mathbb Z^2\) is isomorphic to the regular module \(\mathbb Z[C_2]\), and the orbit quotient \(Y=X/\langle h\rangle\) satisfies \(\widetilde H_i(Y;\mathbb Z)=\mathbb Z\) for \(i=n\) and zero otherwise.

Indeed, barycentrically subdivide \(X\). An invariant chain of nonempty faces has every member invariant (the dimensions are distinct), so the fixed-point set becomes a subcomplex. Every simplex outside that fixed subcomplex has a two-element orbit. Thus the relative integral cellular chain complex \(C_*(X,F)\) is a *finite complex of free modules* over \(R=\mathbb Z[C_2]=\mathbb Z[h]/(h^2-1)\), and
\[
C_*(Y,F)\cong\mathbb Z\otimes_R C_*(X,F),
\]
where \(h\) acts trivially on the right \(R\)-module \(\mathbb Z\). The relative chain complex has homology only in degree \(n\), where it is \(M\). The derived-tensor hyperhomology spectral sequence has only one nonzero row, and therefore gives natural isomorphisms
\[
H_{n+p}(Y,F;\mathbb Z)\cong\operatorname{Tor}^{R}_{p}(\mathbb Z,M)
\quad(p\ge0),
\]
with the relative homology zero in degrees below \(n\). Since \(Y\) is finite-dimensional, the left side vanishes for all sufficiently large \(p\). The standard explicit two-periodic free resolution of the trivial \(R\)-module \(\mathbb Z\), with alternating maps \(h-1\) and \(1+h\), makes \(\operatorname{Tor}^{R}_{p}(\mathbb Z,M)\) periodic of period two for all \(p\ge1\). It follows that **every positive Tor group vanishes**.

The Lefschetz number of \(h\) on \(X\) is the Euler characteristic of its fixed set, hence equals one. As \(H_0(X;\mathbb Z)\cong\mathbb Z\) and the only nonzero reduced homology is \(H_n(X;\mathbb Z)\cong\mathbb Z^2\), the trace of \(h\) on \(M\otimes\mathbb Q\) is zero. Consequently its positive and negative rational eigenspaces both have dimension one. Choose a primitive fixed vector \(e\) spanning the rank-one integral fixed sublattice and extend it to a \(\mathbb Z\)-basis \(e,f\) of \(M\). Necessarily
\[
h e=e,\qquad h f=a e-f
\]
for some integer \(a\). Changing \(f\) by a multiple of \(e\) changes \(a\) by an even integer. If \(a\) were even, the lattice would split into a trivial and sign line; the explicit periodic resolution would then give \(\operatorname{Tor}^{R}_1(\mathbb Z,M)\cong\mathbb Z/2\), contradicting its vanishing. Hence \(a\) is odd. Choose \(f\) so that \(hf=e-f\). Then \(f,hf\) are an integral basis, exchanged by \(h\), proving \(M\cong R\). It follows that
\[
H_n(Y,F;\mathbb Z)\cong M/(h-1)M\cong\mathbb Z
\]
and all other relative homology vanishes. Since \(F\) is contractible, this is the claimed reduced integral homology of \(Y\). This completes the lemma.

**3. The homotopy type for \(n\ge2\).** Apply the lemma to \(X_n,F_n\) using the known two-sphere wedge in Step 1 and [1]. For \(n\ge2\), \(X_n\) is simply connected. The finite action has a fixed point, so Armstrong's orbit-space fundamental-group theorem [3] gives \(\pi_1(Y_n)=1\). A simply connected CW complex with reduced integral homology concentrated as one copy of \(\mathbb Z\) in degree \(n\ge2\) is homotopy equivalent to \(S^n\): successive Hurewicz arguments produce an \((n-1)\)-connected space, and a map representing the generator of \(\pi_n\) is an integral homology equivalence; homological Whitehead then makes it a homotopy equivalence. Therefore \(Y_n\simeq S^n\) for all \(n\ge2\).

**4. The case \(n=1\).** Here \(G_1=C_6\). The quotient of the barycentric subdivision of \(\operatorname{Ind}(C_6)\) has \(9\) vertices, \(15\) one-cells, and \(6\) two-cells. Each of the six two-cells can be eliminated with a distinct free boundary edge by an explicit sequence of elementary collapses. The residual complex is a connected graph with \(9\) vertices and \(9\) edges, hence has homotopy type \(S^1\). A deterministic algorithm specifying and checking every collapse is supplied in `verify_hex_quotient.py`, function `verify_base_circle`. This completes the all-parameter proof.

## Verification
The standalone standard-library script `verify_hex_quotient.py` reconstructs the exact graph and independent faces. For each \(1\le n\le6\), it exhaustively checks that the invariant faces are precisely the \(2^n\) unions of even-column pairs, verifies the Euler characteristics of the original and fixed complexes, and computes the quotient Euler characteristic. For \(n=1,2\), it constructs all barycentric flags, forms their exact involution orbits, and computes the orbit-cell boundary ranks over \(\mathbb F_2\); these give Betti vectors \((1,1,0)\) and \((1,0,1,0,0)\), respectively. It also explicitly verifies the six free-face collapses in the \(n=1\) quotient. The recorded command is `python3 verify_hex_quotient.py`; successful replay concludes `ALL_VERIFY_OK`. The computations corroborate the proof but do not replace the infinite-parameter argument, especially its integral torsion exclusion.

## Relationship to prior work
Chandrakar and Singh [1] proved the **nonequivariant** \(S^n\vee S^n\) homotopy type. Their Sections 2–3 define these exact graphs and prove the wedge statement, but do not discuss their geometric symmetry quotients or an integral row-exchange module. The independently published mathematical result [2] determines the rational character of row exchange, including trace zero; it expressly does not provide the integral lattice or geometric quotient homotopy type. A trace-zero rank-two rational representation does not distinguish the two possible integral involution lattices (split trivial-plus-sign versus regular), so it cannot alone settle quotient torsion. The contractible fixed simplex and the finite free relative chain argument in Step 2 establish the missing integral structure and the full quotient homotopy classification.

The periodic group-ring resolution, the simplicial Lefschetz formula, Hurewicz, Whitehead, and Armstrong's orbit-space fundamental-group theorem are standard tools; no general novelty is asserted for those tools separately. The contribution is their verified application to the full family of natural hexagonal-chain orbit quotients. Searches for equivalent quotient-sphere classifications, alternative orbit-space formulations, and stronger equivariant models identified no covering result; this does not rule out unindexed or implicit prior work.

## Limitations
The classification concerns the involution exchanging the two rows of the finite planar chain and the **geometric** quotient, not the Borel construction, the end-reversal quotient, the full Klein-four quotient, or wider or periodic hexagonal grids. The proof depends on the established nonequivariant homotopy theorem [1]. The finite verifier samples only \(n\le6\) for face identities and \(n\le2\) for quotient boundary matrices; the all-parameter conclusion is proved separately in Steps 1–4.

## References
[1] Himanshu Chandrakar and Anurag Singh, *Independence Complexes of Hexagonal Grid Graphs*, arXiv:2512.21318v1, first public 2025-12-24, Theorem 3.1 and Sections 2–3. https://arxiv.org/pdf/2512.21318

[2] *Reflection characters of linear hexagonal-chain independence complexes*, public mathematical record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-reflection-characters-of-linear-hexagonal-chain-independence-com--db3e42fb7a57

[3] M. A. Armstrong, *On the fundamental group of an orbit space*, Proceedings of the Cambridge Philosophical Society **61** (1965), 639–646, DOI:10.1017/S0305004100038974.
