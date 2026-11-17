# Multiplicity-free rational symmetry homology of the \(3\times3\times4\) Hamming Rips complex

## Finding

Give \(A=[3]\times[3]\times[4]\) the Hamming distance, and let
\[
X=\operatorname{VR}_{\leq2}(A).
\]
The full natural coordinate/letter symmetry group preserving the two three-letter coordinates is
\[
G=((S_3\times S_3)\rtimes S_2)\times S_4=W\times S_4,
\qquad |G|=1728.
\]
Its action on the 96-dimensional rational group \(\widetilde H_3(X;\mathbb Q)\) is **multiplicity-free with exactly fourteen constituents**. Write \(\rho_0,\rho_1,\rho_2\) for the trivial, sign, and two-dimensional standard representations of \(S_3\), respectively. For \(i<j\) write
\[
M_{ij}=\operatorname{Ind}_{S_3\times S_3}^{W}(\rho_i\boxtimes\rho_j),
\]
and for \(i=0,1,2\) let \(M_i^-\) be the negative-flip extension of \(\rho_i\boxtimes\rho_i\) to \(W\). With \(S^{\lambda}\) denoting the rational Specht representation for the partition \(\lambda\vdash4\), the decomposition is
\[
\begin{aligned}
\widetilde H_3(X;\mathbb Q)\cong {}&
M_{02}\boxtimes\left(S^{(4)}\oplus S^{(3,1)}\oplus S^{(2,2)}\right)\\
&\oplus M_{12}\boxtimes\left(S^{(3,1)}\oplus S^{(2,1,1)}\right)\\
&\oplus M_0^-\boxtimes\left(S^{(4)}\oplus S^{(3,1)}\oplus S^{(2,2)}\right)\\
&\oplus M_1^-\boxtimes\left(S^{(3,1)}\oplus S^{(2,1,1)}\right)\\
&\oplus M_2^-\boxtimes\left(S^{(4)}\oplus S^{(3,1)}\oplus S^{(2,2)}\oplus S^{(2,1,1)}\right).
\end{aligned}
\]
The five summands above have dimensions \(24,24,6,6,36\), respectively, and contain \(3+2+3+2+4=14\) irreducible constituents. In particular the trivial representation does not occur. Since \(X\simeq\bigvee^{96}S^3\), the actual finite topological quotient satisfies
\[
\widetilde H_k(|X|/G;\mathbb Q)=0\qquad\text{for every }k\ge0.
\]
This last statement is rational homological acyclicity, not contractibility or integral acyclicity.

The complete \(45\)-class character is tabulated below. Rows are conjugacy classes of \(W\) and columns are conjugacy classes of \(S_4\), with the cycle types \((1^4),(2,1^2),(2^2),(3,1),(4)\) in that order. The class of an unswapped \(W\)-element is the unordered pair of cycle types of its two \(S_3\) factors; the class of a swapped element is the cycle type of their product. Let \(e,t,c\) denote identity, transposition and three-cycle types in \(S_3\).

| \(W\)-class | Class size in \(W\) | \((1^4)\) | \((2,1^2)\) | \((2^2)\) | \((3,1)\) | \((4)\) |
|---|---:|---:|---:|---:|---:|---:|
| \((e,e)\), unswapped | 1 | 96 | 14 | 4 | 0 | 4 |
| \((e,t)\), unswapped | 6 | 0 | 6 | 12 | 0 | 0 |
| \((e,c)\), unswapped | 4 | 6 | 2 | -2 | 0 | -2 |
| \((t,t)\), unswapped | 9 | 12 | 2 | 0 | 0 | 0 |
| \((t,c)\), unswapped | 12 | 0 | 0 | 0 | 0 | 0 |
| \((c,c)\), unswapped | 4 | -3 | -1 | 1 | 0 | 1 |
| \(e\), swapped | 6 | -30 | -4 | -2 | 0 | -2 |
| \(t\), swapped | 18 | 0 | -2 | -4 | 0 | 0 |
| \(c\), swapped | 12 | -3 | -1 | 1 | 0 | 1 |

## Assumptions and scope

Each \([m]\) denotes \(\{0,\ldots,m-1\}\). A subset is a simplex exactly when no two triples disagree in all three coordinates. Thus \(X\) is also \(\operatorname{Ind}(K_3\times K_3\times K_4)\), where the graph product is **categorical**, not Cartesian. The group \(W=S_3\wr S_2\) permutes letters independently in the two \([3]\)-coordinates and can interchange those two coordinates; the independent \(S_4\)-factor permutes the \([4]\)-alphabet. We use the induced action on oriented simplicial chains over \(\mathbb Q\). The first and second \(S_3\) factors are distinguished only before adjoining the coordinate swap. There is no action interchanging a three-letter coordinate with the four-letter coordinate. All character formulas use rational homology. The classification concerns this exact finite 36-vertex complex and its specified order-1728 action.

## Proof

**1. Entire face poset and homology.** Order the 36 triples lexicographically and assign bit positions \(0,\ldots,35\). Recursively enumerate every clique of the at-most-two Hamming-distance compatibility graph, choosing vertices in ascending order and intersecting candidate sets with compatibility masks. This produces the following complete augmented face vector by cardinality \(0,\ldots,12\):

`(1,36,414,2028,4869,6804,6816,5184,3042,1324,396,72,6)`.

On these 30,992 distinct faces, at stage \(i=0,\ldots,35\), simultaneously pair every still-unmatched face not containing \(i\) with the still-unmatched face obtained by inserting \(i\), whenever both are available. Exactly 15,448 augmented face pairs occur, including the empty face paired with the first vertex. The unmatched faces comprise exactly 96 simplices of cardinality four. To prove this is a valid discrete-Morse matching rather than a formal count, orient every Hasse cover downward except for matched covers oriented upward. Enumerate all 178,704 Hasse covers, and perform a full topological sort: all 30,992 face nodes are removed, proving acyclicity exactly. Removing the empty face and its matching pair leaves an ordinary acyclic matching with one critical vertex and 96 critical three-simplices. Forman's theorem therefore gives a CW model with one zero-cell and 96 three-cells, hence
\[
X\simeq\bigvee^{96}S^3.
\]
The checker performs every stated finite operation using only exact integer and bitset arithmetic. This reconstructs the needed topology rather than assuming a prior homotopy computation.

**2. Character from fixed oriented faces.** For each \(g\in G\), a simplex contributes to the trace of its simplicial chain action if and only if \(g\) preserves its vertex set; its contribution is the sign of the induced vertex permutation. The alternating chain-trace identity and the fact that reduced homology is concentrated in degree three give
\[
\chi_{H_3}(g)=\sum_{F\in X\cup\{\varnothing\}\,;\,gF=F}
(-1)^{|F|}\operatorname{sgn}(g|_F).
\]
The empty-face contribution is one. Partition the 36 vertices into the cycles of \(g\). Every invariant simplex is a union of complete vertex cycles. For a union of \(j\) compatible cycles, the preceding signed term is \((-1)^j\). Hence an **independent exact formula** is
\[
\chi_{H_3}(g)=
\sum_{\substack{\mathcal A\text{ a collection of vertex cycles}\\
\bigcup\mathcal A\in X}}(-1)^{|\mathcal A|},
\]
including the empty collection. Both formulas are evaluated directly from the metric for each of 45 conjugacy representatives (nine in \(W\), five in \(S_4\)); the independently computed results agree entrywise and are precisely the displayed table. In particular the table at the identity gives 96, independently corroborating the Morse count.

**3. Exact irreducible inner products.** The conjugacy classes of \(W\) comprise six classes of unswapped pairs of \(S_3\) cycle types and three classes of swapped products. Their sizes are \((1,6,4,9,12,4,6,18,12)\), which sum to 72. The five \(S_4\) cycle-type class sizes are \((1,6,3,8,6)\), summing to 24. Irreducible \(W\) representations are the three induced \(M_{ij}\) (distinct \(i,j\)) together with the six positive/negative flip extensions \(M_i^{\pm}\) of identical tensor factors. Their characters are explicitly
\[
\begin{aligned}
\chi_{M_{ij}}(a,b;0)&=\chi_i(a)\chi_j(b)+\chi_j(a)\chi_i(b),&
\chi_{M_{ij}}(a,b;1)&=0,\\
\chi_{M_i^{\pm}}(a,b;0)&=\chi_i(a)\chi_i(b),&
\chi_{M_i^{\pm}}(a,b;1)&=\pm\chi_i(ab).
\end{aligned}
\]
Here \(0/1\) records whether coordinates are swapped; the semicolon is not an additional group factor. Using standard rational character tables of \(S_3\) and \(S_4\), calculate for each of the 45 external-product irreducibles
\[
\left\langle\chi_{H_3},\chi_U\chi_{S^\lambda}\right\rangle
=\frac{1}{1728}\sum_{C_W,C_4}|C_W||C_4|
\chi_{H_3}(C_W,C_4)\chi_U(C_W)\chi_{S^\lambda}(C_4).
\]
The exact integer sums divided by 1728 give 1 for the fourteen listed summands and 0 for all other 31 irreducibles. Their dimensions sum to 96, confirming that no character component is missing. In particular the trivial \(M_0^+\boxtimes S^{(4)}\) has multiplicity zero, as claimed.

**4. Quotient rational homology.** For a finite simplicial group action and rational coefficients, barycentric subdivision makes the quotient an honest finite simplicial/CW quotient and averaging chain maps identifies its rational homology with the invariant part of the original rational homology (equivalently use the rational transfer/coinvariant complex). By Maschke's theorem this is the invariant subspace. Since \(X\) is connected and its only positive-degree reduced rational homology is \(\widetilde H_3\), which contains no trivial constituent, \(|X|/G\) has no positive-degree rational homology and remains connected. This proves the reduced rational acyclicity stated above.

## Verification

The complete, standalone Python 3 standard-library program `verify_equivariant_334.py` is supplied. Execute `python3 verify_equivariant_334.py` from its directory. It enumerates all faces, verifies the entire acyclic discrete-Morse Hasse digraph, computes the 45 traces by **both** signed simplicial chains and compatible vertex-orbit inclusion–exclusion, uses exact group-class sizes and ordinary symmetric-group character tables, performs all 45 irreducible inner products, and asserts every expected decomposition multiplicity. Its terminal line is `VERIFIED_FULL_334_SYMMETRY_CHARACTER`. The package also includes the expected character table and dimensional constituents in `CHARACTER_TABLE.json`. No floating-point arithmetic, unspecified software package or downloaded external data is required. This is a complete finite exhaustive certificate for this exact 36-vertex object, not an extrapolation to larger alphabets. The scientific review is same-model only; no independent audit is asserted.

## Relationship to prior work

Antolín Camarena and Carnero Bravo (2023) prove a three-factor categorical-product homotopy statement when one complete-graph factor is \(K_2\). Their result does not address the present all-nonbinary mixed alphabet, let alone its symmetry character. Bendersky, Elia and Grbić (2026) study binary hypercube Rips cohomology. Galetto, Montaño and Wellner (2026) determine rational hyperoctahedral representations for binary hypercubes; their group and metric vertex set are not the present \(3\)-by-\(3\)-by-\(4\) box. A publicly accessible 2026 calculation already proves \(\operatorname{VR}_{\le2}([3]\times[3]\times[4])\simeq\bigvee^{96}S^3\). This homotopy type is **prior work**, not a novelty assertion here; its full result was inspected and explicitly states that equivariant homology modules are outside its scope. A further full-text 2026 calculation gives the 22-class rational character for the *uniform ternary* cube \([3]^3\) under its different 1,296-element group; this does not imply the mixed 36-vertex, 1,728-element character. Likewise character computations for \([2]\times[4]\times[4]\) concern another complex. The new contribution is the complete explicit mixed-box rational character and its fourteen-piece multiplicity-free decomposition, together with the quotient's rational acyclicity. These comparisons concern actual statements and group actions, not superficial title differences.

## Limitations

Only the rational representation of the specified group on \(\widetilde H_3\) is classified; neither integral equivariant lattices nor integral quotient torsion is determined. The quotient is shown rationally acyclic, not contractible. There is no general theorem for arbitrary mixed alphabet sizes or for other Rips scales. The finite checker is a reproducible exact computation, not an independent external mathematical validation. Some earlier equivalent computation might be unindexed; no exhaustive publication-priority certification is claimed.

## References

1. M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705, first public 2026-05-01, https://arxiv.org/abs/2605.00705.
2. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, first public 2026-06-18, https://arxiv.org/abs/2606.20784.
3. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, first public 2023-07-23, https://arxiv.org/abs/2307.12401.
4. *A 96-three-sphere stage in the mixed ternary–quaternary Hamming box*, 2026-10-25, public result, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-a-96-three-sphere-stage-in-the-mixed-ternary-quaternary-hamming--98bfe9517ebf/RESULT.md.
5. *The complete \(S_3\wr S_3\) homology character of the ternary three-cube Rips complex*, 2026-11-08, public result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-complete-s-3-wr-s-3-homology-character-of-the-ternary-three--e25864e97f44/RESULT.md.
