# Coordinate-symmetric fixed spheres at the penultimate hypercube Rips scale

## Finding
Let \(Q_n=\{0,1\}^n\) carry Hamming distance, and let \(X_n=\operatorname{VR}_{\le n-2}(Q_n)\) denote the inclusive Vietoris--Rips complex. For every integer \(n\ge2\), let \(S_n\) permute the coordinates and set \(F_n=|X_n|^{S_n}\), the **geometric** fixed-point subspace (not the full invariant subcomplex). Put \(m=\lfloor n/2\rfloor\) and \(t=\lceil m/2\rceil\). Then \(F_n\) is PL-homeomorphic to the realization of a finite simplicial complex that *simplicially collapses* onto the boundary of the \(t\)-dimensional cross-polytope. In particular,
\[
F_n\simeq S^{t-1}=S^{\lfloor(n-2)/4\rfloor},\qquad
\widetilde H_j(F_n;\mathbb Z)\cong
\begin{cases}\mathbb Z,&j=\lfloor(n-2)/4\rfloor,\\0,&j\ne\lfloor(n-2)/4\rfloor.\end{cases}
\]
The simultaneous bit-complement \(\kappa:x\mapsto\mathbf1-x\), which commutes with \(S_n\), acts freely on \(F_n\). On its unique nonzero reduced integral homology group, \(\kappa_*\) is multiplication by \((-1)^t\).

## Assumptions and scope
All simplices are finite sets of vertices whose *pairwise* Hamming distances are at most \(n-2\); the scale inequality is inclusive. Geometric fixed points are taken after realization. When \(n=2,3,4,5\), the homotopy sphere is \(S^0\), with its usual two-point realization; for \(n\ge6\) the sphere is connected. The group \(S_n\) acts on the original \(2^n\) cube vertices by permuting coordinate positions, not by bit complementation. The residual bit-complement map acts on the fixed-point space because the two actions commute.

## Proof
**1. Geometric orbit realization.** For a finite simplicial complex with an acting finite group, the geometric fixed space is PL-homeomorphic to the complex whose vertices are *entire original vertex orbits* \(O\) that individually span simplices, and whose faces are sets of such orbits with simplicial union. Indeed, each fixed barycentric point has equal coefficients at all vertices of the same orbit, and a supported union of orbits spans a simplex precisely when its support is a face. Conversely, normalized orbit barycenters span precisely the fixed simplices. Their disjoint original supports make the affine identification injective.

**2. Exact weight-orbit compatibility.** Under coordinate permutations the orbits are the Hamming-weight layers \(W_a\), \(0\le a\le n\). For two layers (also allowing \(a=b\)), the largest Hamming distance attained between their points is
\[
D(a,b)=\min(a+b,\,2n-a-b).
\]
For disjoint supports the upper bound \(a+b\) is attained whenever \(a+b\le n\). When \(a+b\ge n\), choose the supports with minimal overlap \(a+b-n\), attaining \(2n-a-b\). The same argument applies to two elements in one layer (and gives zero when that layer contains only one element). Thus \(W_a\) is admissible exactly when \(2\min(a,n-a)\le n-2\), which is equivalent to
\[
0\le a\le m-1\quad\text{or}\quad n-m+1\le a\le n.
\]
Call the low-weight orbit \(L_i=W_i\) and the high-weight orbit \(R_j=W_{n-j}\) for \(0\le i,j<m\). All low-weight orbits are mutually compatible, and so are all high-weight orbits: for the low side \(D(a,b)=a+b\le2m-2\le n-2\). Across the sides,
\[
D(i,n-j)=n-|i-j|.
\]
Hence \(L_i\) and \(R_j\) are **incompatible** precisely when \(|i-j|\le1\).

Define the bipartite band graph \(B_m\) on vertices \(L_0,\ldots,L_{m-1},R_0,\ldots,R_{m-1}\), whose only edges are \(L_iR_j\) with \(|i-j|\le1\). Since the Rips condition is pairwise, Step 1 proves the canonical PL identification
\[
F_n\cong_{\mathrm{PL}}|\operatorname{Ind}(B_m)|.
\]
This is exact, including the \(n=2,3\) boundary cases.

**3. Explicit collapses.** The following elementary folding fact is used. If \(u,v\) are nonadjacent graph vertices with open neighborhoods \(N(u)\subseteq N(v)\), then \(\operatorname{Ind}(G)\) simplicially collapses onto \(\operatorname{Ind}(G-v)\): each face containing \(v\) but not \(u\) can be paired with the face obtained by adjoining \(u\), and the cone of the link at \(v\) is eliminated. This is a standard dominated-vertex collapse and also follows by ordering these face pairs from largest to smallest.

Starting with \(B_m\), for each even \(i\) with \(i+1<m\), first delete \(L_{i+1}\) using \(L_i\), then delete \(R_{i+1}\) using \(R_i\). At each step the required open-neighborhood inclusion holds in the graph remaining after earlier deletions. For example, for \(i=0\), \(N(L_0)=\{R_0,R_1\}\subseteq N(L_1)\), and after removing \(L_1\), \(N(R_0)=\{L_0\}\subseteq N(R_1)\). The rest is the identically shifted induction on the induced graph at indexes \(2,\ldots,m-1\). After all deletions the only remaining edges are \(L_{2j}R_{2j}\), for \(0\le j<t\); they are \(t\) vertex-disjoint edges. Therefore
\[
\operatorname{Ind}(B_m)\searrow \operatorname{Ind}(tK_2)
=\underbrace{S^0*\cdots*S^0}_{t\text{ factors}}
\cong_{\mathrm{PL}} S^{t-1}.
\]
The last simplicial complex is precisely the boundary of the \(t\)-cross-polytope. This proves the integral homotopy and homology statements.

**4. Complement action.** The bit-complement map exchanges \(L_i\leftrightarrow R_i\) on the weight-orbit model. Any simplex setwise fixed by this involution would contain both \(L_i\) and \(R_i\) for some \(i\), which is impossible since \(L_iR_i\) is an edge of the forbidden graph. Thus the involution has no geometric fixed point, and its simplicial Lefschetz number is zero (there are no setwise fixed nonempty simplices). The unreduced degree-zero homology contributes trace \(1\) when \(t\ge2\). Equivalently, for all \(t\ge1\), its reduced Lefschetz number equals \(-1\); because the only reduced homology group is a copy of \(\mathbb Z\) in dimension \(t-1\), its trace is \((-1)^t\), necessarily the multiplication sign on that rank-one integral group. The reduced formulation includes \(t=1\), when the two components are exchanged.

## Verification
The standalone standard-library Python file `verify_penultimate_fixed.py` independently enumerates *all* Hamming-weight layer pairs and their original binary vectors for \(2\le n\le10\), checking the derived orbit compatibility relation without assuming its formula. It then checks every open-neighborhood containment and the residual disjoint-edge graph for \(1\le m\le30\). Separate mod-two boundary calculations on the exact band-graph independence complexes for \(1\le m\le6\) check their sphere homology predictions, and finite complement-pair checks cover \(1\le m\le20\). Run `python3 verify_penultimate_fixed.py` beside this document. The expected terminal line is `PENULTIMATE_COORDINATE_FIXED_SPHERES_OK`; the recorded full output is in `verification_output.txt`. Finite checks are corroboration, not an infinite proof; the argument above is valid for all integers in scope.

## Relationship to prior work
Galetto, Montaño and Wellner (arXiv:2606.20784; first publicly posted 2026-06-18) compute full hyperoctahedral **ordinary rational homology representations** at scales at most three and at scale \(n-1\). Their §7 treats \(n-1\), not the present scale \(n-2\); the ordinary representation is not a computation of the geometric fixed-point space. Bendersky, Elia and Grbić (arXiv:2605.00705; first posted 2026-05-01; later open-access journal article dated 2026-10-22) develop cohomological connectivity bounds and explicit classes for the unrestricted complexes, not this weight-orbit fixed homotopy type.

The publicly available note *A parity reduction of penultimate hypercube Rips complexes* (2026-10-04) identifies the **entire** scale-\(n-2\) complex with independence complexes of folded cubes (in a parity-dependent model), but contains no orbit-fixed-space classification under the *original* coordinate-permutation action and no residual complement degree. The present theorem is not the ordinary homotopy type of that full complex. Feng (arXiv:2305.07084) treats scale three, overlapping the present scale only for \(n=5\). Earlier Adamaszek--Adams work (arXiv:2103.01040) treats small scales and the top cross-polytope boundary. The case \(n=4\) overlaps earlier small-scale fixed-point analyses; the unrestricted penultimate-scale sphere pattern and sign statement in all higher dimensions do not follow from those small-scale calculations.

## Limitations
The result classifies fixed points of the **full** coordinate-permutation group, not all its subgroups or the whole hyperoctahedral group. It gives a simplicial collapse of the orbit-fixed model, hence a homotopy sphere, but does **not** assert that the original fixed space is PL-homeomorphic to a sphere. The ordinary unrestricted homotopy type of \(\operatorname{VR}_{\le n-2}(Q_n)\) is not determined. The complement action is determined on the unique nonzero reduced homology group, not classified up to equivariant homotopy. Literature comparisons are based on identified accessible primary works and research records; an unindexed equivalent classification remains a residual originality risk.

## References
1. Federico Galetto, Jonathan Montaño and Zoe Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, first public date 2026-06-18. https://arxiv.org/abs/2606.20784
2. Martin Bendersky, Salvatore Elia and Jelena Grbić, *Cohomological properties of the Vietoris-Rips Complex of a Hypercube Graph*, arXiv:2605.00705, first public date 2026-05-01; *Proc. Roy. Soc. Edinburgh Sect. A*, online 2026-10-22. https://doi.org/10.1017/prm.2026.10175
3. Ziqin Feng, *Homotopy types of Vietoris-Rips complexes of Hypercube Graphs*, arXiv:2305.07084, first public date 2023-05-11. https://arxiv.org/abs/2305.07084
4. Michał Adamaszek and Henry Adams, *On Vietoris--Rips complexes of hypercube graphs*, arXiv:2103.01040, first public date 2021-03-01. https://arxiv.org/abs/2103.01040
5. *A parity reduction of penultimate hypercube Rips complexes*, published mathematical research note, 2026-10-04. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-parity-reduction-of-penultimate-hypercube-rips-complexes--7b869e8f79d9
