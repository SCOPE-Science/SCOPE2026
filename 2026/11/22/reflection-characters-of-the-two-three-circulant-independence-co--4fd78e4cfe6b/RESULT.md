# Reflection characters of the two-three circulant independence complexes

## Finding
Let \(G_n\) be the simple Cayley graph on \(\mathbb Z/n\mathbb Z\) with jumps \(\{\pm2,\pm3\}\), let \(X_n=\operatorname{Ind}(G_n)\), and assume \(n\ge6\). For \(k\in\mathbb Z/n\mathbb Z\), write \(R_k(i)=k-i\) and let \(d_n\) denote the unique reduced-homology degree of \(X_n\). Define the integer
\[
L(n,k)=\begin{cases}
(n+1)/2,& n\text{ odd},\\
n/2+1,&n\text{ even and }k\text{ even},\\
n/2,&n\text{ even and }k\text{ odd},
\end{cases}
\qquad
\epsilon(L)=(-1)^{1+\lfloor (L-3)/4\rfloor}.
\]
Then the *complete reflection character* of the unique nonzero reduced rational homology group is
\[
\boxed{\operatorname{tr}\left((R_k)_*\mid\widetilde H_{d_n}(X_n;\mathbb Q)\right)
=(-1)^{d_n+1}\epsilon(L(n,k)).}
\]
The known sphere multiplicity is \(b_n=5\) when \(n\equiv0\pmod8\), \(b_n=3\) when \(n\equiv4\pmod8\), and \(b_n=1\) otherwise. In particular, the reduced rational Betti number in degree \(d_n\) of the genuine geometric quotient \(|X_n|/\langle R_k\rangle\) equals
\[
\frac{b_n+(-1)^{d_n+1}\epsilon(L(n,k))}{2}.
\]
For \(n=8q+4\), the two reflection-axis types have different quotient ranks. They are exactly \(\frac{3+(-1)^q}{2}\) for the vertex-axis and \(\frac{3-(-1)^q}{2}\) for the edge-axis; thus the unordered pair is always \(\{1,2\}\). The character formula, combined with the previously published cyclic translation character, determines the full rational dihedral character; it makes no assertion about integral dihedral module extensions.

## Assumptions and scope
The vertex set is \(\mathbb Z/n\mathbb Z\), and \(\operatorname{Ind}\) denotes the abstract simplicial complex of all independent vertex subsets. The Cayley graph is simple, so repeated jumps modulo small \(n\) count as one edge. All involutions are induced by the explicit permutations \(i\mapsto k-i\) of the original labeled vertex set. Geometric fixed points in the realization, rather than merely fixed original vertices, are used. We use the independently established ordinary homotopy classification of Wang, first deposited August 24, 2026 and reproduced as Corollary 6.3 of Wang–Li (October 15, 2026): for \(n=8q+r\), the nonzero degree and rank are
\[
(d_n,b_n)=\begin{cases}
(2q-1,5),&r=0,\\
(2q-1,1),&r=1,2,3,\\
(2q,3),&r=4,\\
(2q+1,1),&r=5,6,7.
\end{cases}
\]
Only \(n\ge6\) is claimed, and the already published sphere ranks and cyclic character are not claimed as discoveries here.

## Proof
**Reflection fold.** A face fixed setwise by \(R_k\) is a union of orbits of \(R_k\). An orbit containing an internal graph edge cannot appear in an independent face; two permitted orbits are incompatible exactly when a graph edge joins them. Sending a geometric fixed point to its total barycentric mass on each orbit gives a homeomorphism between the fixed space and the independence complex of this looped orbit graph after deleting all internally incompatible orbits. This uses weights divided by orbit size on the inverse map, so fixed one-vertex orbits and paired orbits are treated consistently.

Use consecutive representatives indexed \(0,1,\ldots,L-1\) after folding a reflection axis. When \(n\) is odd all reflections are conjugate and \(L=(n+1)/2\). When \(n\) is even, a reflection through opposite vertices has \(L=n/2+1\), whereas a reflection through opposite edges has \(L=n/2\). In every case \(L\ge3\). Direct comparison of the four jumps against the folded coordinates shows that **precisely** the orbit indices \(1\) and \(L-2\) are internally incompatible; the remaining vertices are joined exactly when their *ordinary index difference* is two or three. Thus the fixed space is \(\operatorname{Ind}(J_L)\), where \(J_L\) has vertex set \(\{0,\ldots,L-1\}\setminus\{1,L-2\}\) and edges of ordinary difference two or three. This is an exact graph identification, not just a homology calculation.

**Signed enumeration.** Let \(P_L=I_{J_L}(-1)=\sum_{S\in\operatorname{Ind}(J_L)}(-1)^{|S|}\), including the empty set. In an invariant face formed from \(a\) reflection orbits, let \(t\) of those orbits be two-cycles. Its number of vertices is \(a+t\) and the induced orientation sign is \((-1)^t\). Its contribution to the *reduced* simplicial Lefschetz sum (with the empty face convention) is therefore \((-1)^{a+t-1+t}=(-1)^{a-1}\). Summing proves
\[
\widetilde{\mathcal L}(R_k;X_n)=-P_{L(n,k)}.
\]
The homology is concentrated in degree \(d_n\), so Hopf's trace identity gives \((-1)^{d_n}\operatorname{tr}((R_k)_*)=-P_{L(n,k)}\).

**Exact finite-state identity.** We show \(P_L=(-1)^{1+\lfloor(L-3)/4\rfloor}\) for *every integer* \(L\ge3\). For \(L\ge5\), process the length-\(L\) binary word left to right, forcing positions \(1\) and \(L-2\) to zero and forbidding pairs of ones separated by two or three positions. Index an eight-state row by the preceding three bits \(s\in\{0,\ldots,7\}\). Let \(T\) have transition \(s\to 2s\bmod8\) of weight \(+1\), and, only if \(s\mathbin{\&}6=0\), transition \(s\to(2s\bmod8)+1\) of weight \(-1\). Let \(F\) retain only the first, zero-appending transition. After reading positions \(0,1,2\), the signed row is exactly
\[
v=(1,-1,0,0,-1,0,0,0).
\]
Writing \(\mathbf1\) for the eight-entry column of ones and \(w=FT\mathbf1=(0,1,1,1,0,1,1,1)^{\mathsf T}\), the exact polynomial evaluation is
\[
P_L=vT^{L-5}w\qquad(L\ge5).
\]
With \(I\) the eight-by-eight identity, direct integer multiplication gives the identities
\[
vT^3(T^4+I)=0,
\qquad vT^j(T^4+I)w=0\quad(j=0,1,2).
\]
Consequently \(P_{L+4}=-P_L\) for every \(L\ge5\). Direct enumeration gives \(P_3=P_4=P_5=P_6=-1\); these four bases plus the recurrence prove the displayed \(P_L\) formula for all \(L\ge3\). Together with the signed enumeration this proves the character formula.

**Quotient.** Over \(\mathbb Q\), finite-group coinvariants agree with invariants, and the rational homology of a finite simplicial group quotient agrees with the invariant rational homology. The invariant dimension under an involution is \((b_n+\operatorname{tr}(R_k))/2\), proving the quotient formula. Substituting \(n=8q+4\) yields vertex-axis trace \((-1)^q\) and edge-axis trace \((-1)^{q+1}\), hence the two explicitly ordered quotient ranks above. The previously published cyclic representation plus these traces specifies the entire rational dihedral character.

## Verification
The accompanying Python 3 standard-library script `check.py` reconstructs the exact transfer matrices, checks both displayed polynomial identities over the integers, independently compares all folded graphs with \(J_L\) for 137 reflection cases with \(6\le n\le96\), and evaluates signed oriented simplicial Lefschetz sums directly in all 20 reflection cases with \(6\le n\le18\). The output must equal `EXPECTED.txt` byte-for-byte. The infinite assertion rests on the transfer proof, not on finite sampling.

## Relationship to prior work
Wang, *A Local Block Criterion for Periodic Morse Reductions of Circulant Independence Complexes* (Zenodo, August 24, 2026), first establishes the family homotopy types and cyclic translation character. Wang and Li, *Integral homology lattices of matching and circulant complexes* (arXiv:2610.22082, first public October 15, 2026), Corollary 6.3, Section 8, and Theorem 10.3, give the ordinary homotopy classification, a **cyclic** subgroup fixed-space profile, and the **cyclic** character. Inspection of those full relevant sections found no all-reflection trace or axis-specific quotient-rank theorem for this family. Results on reflection characters of other graph complexes are not the same objects. The present theorem adds the reflection part of the rational dihedral character while expressly relying on the established homology concentration.

## Limitations
The proof computes rational characters, not integral dihedral lattices, a complete dihedral-equivariant homotopy type, or quotient homotopy types. The first source's full preprint was not independently inspected beyond its public metadata and abstract; the later full preprint's directly relevant sections were inspected. Unindexed equivalents remain a priority risk. No independent mathematical audit is asserted.

## References
1. Q. Wang, *A Local Block Criterion for Periodic Morse Reductions of Circulant Independence Complexes*, Zenodo v1, August 24, 2026, https://zenodo.org/records/22082056, DOI: 10.5281/zenodo.22082056.
2. Q. Wang and W. Li, *Integral homology lattices of matching and circulant complexes*, arXiv:2610.22082v1, October 15, 2026, https://arxiv.org/html/2610.22082v1, especially Corollary 6.3, Theorems 8.2 and 10.3.
