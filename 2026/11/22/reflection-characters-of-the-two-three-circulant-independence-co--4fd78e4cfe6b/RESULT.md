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

Conjugating by a translation changes \(k\) by an even residue. Thus we can use \(k=-\delta\), with \(\delta=0\) in the odd and even vertex-axis cases, and \(\delta=1\) in the even edge-axis case. The orbits have representatives \(0\le i<L\), with mates \(-i-\delta\pmod n\), and \(L=\lfloor n/2\rfloor+1-\delta\). The ordinary differences between representatives give exactly the jumps at distance two or three: the only possible wraparound at distance at most three is \(n=6\) and ordinary difference three, already included.

For edges between representatives and mates the residue to check is \(s=i+j+\delta\). At the left endpoint, \(s=2,3\) gives, for \(\delta=0\), the loop at \(i=j=1\) and the distinct pairs \((0,2),(0,3),(1,2)\); for \(\delta=1\) it gives the same loop and the distinct pairs \((0,1),(0,2)\). Only pairs within the index range are considered. After removal of index 1, the remaining pairs on either list have ordinary distance two or three. At the right endpoint write \(i'=L-1-i\), \(j'=L-1-j\); then \(n-s=i'+j'+n-2(L-1)-\delta\), with the last three terms combining to 0 in the even vertex-axis case and 1 in the other cases. The same lists now give the loop at index \(L-2\) and no new edges on the permitted indices. A loop here comes from an edge between the distinct members of one orbit; a singleton has residue 0 modulo \(n\) and contributes no loop. Hence **precisely** indices \(1,L-2\) are internally incompatible (they may coincide), and the fixed space is \(\operatorname{Ind}(J_L)\), where \(J_L\) is the graph on the remaining indices with edges of ordinary difference two or three.

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
Consequently \(P_{L+4}=-P_L\) for every \(L\ge5\). The values \(vT^jw\) for \(j=0,1,2,3\) are \(-1,-1,1,1\), respectively, giving the four starting values \(P_5,P_6,P_7,P_8\) for this recurrence. For \(L=3,4\) the permitted graph is a single edge, so \(P_3=P_4=-1\). These six values, with the recurrence starting at \(L=5\), prove the formula for every \(L\ge3\). Together with the signed enumeration this proves the character formula.

**Quotient.** After barycentric subdivision the vertices of each simplex correspond to faces of distinct dimensions. A simplex stabilizer therefore fixes its simplex pointwise, and the geometric quotient has one open cell per simplex orbit. Its rational cellular chains are the coinvariants of the subdivided simplicial chains, with orientations given by ordering the face dimensions. Over \(\mathbb Q\), averaging identifies finite-group coinvariants with invariants and makes the functor exact. Hence the quotient homology is the invariant homology. The invariant dimension under an involution is \((b_n+\operatorname{tr}(R_k))/2\), proving the quotient formula. Substituting \(n=8q+4\) yields vertex-axis trace \((-1)^q\) and edge-axis trace \((-1)^{q+1}\), hence the two explicitly ordered quotient ranks above. The previously published cyclic representation plus these traces specifies the entire rational dihedral character.

## Verification
The accompanying Python 3 standard-library script `check.py` reconstructs the exact transfer matrices, checks both displayed polynomial identities over the integers, independently compares all folded graphs with \(J_L\) for 137 reflection cases with \(6\le n\le96\), and evaluates signed oriented simplicial Lefschetz sums directly in all 20 reflection cases with \(6\le n\le18\). The output must equal `EXPECTED.txt` byte-for-byte. The infinite assertion rests on the transfer proof, not on finite sampling.

## Relationship to prior work
Wang, *A Local Block Criterion for Periodic Morse Reductions of Circulant Independence Complexes* (Zenodo, August 24, 2026), first establishes the family homotopy types and cyclic translation character. Wang and Li, *Integral homology lattices of matching and circulant complexes* (arXiv:2610.22082, first public October 15, 2026), Corollary 6.3, Section 8, and Theorem 10.3, give the ordinary homotopy classification, a **cyclic** subgroup fixed-space profile, and the **cyclic** character. Inspection of those full relevant sections found no all-reflection trace or axis-specific quotient-rank theorem for this family. Results on reflection characters of other graph complexes are not the same objects. The present theorem adds the reflection part of the rational dihedral character while expressly relying on the established homology concentration.

## Limitations
The proof computes rational characters, not integral dihedral lattices, a complete dihedral-equivariant homotopy type, or quotient homotopy types. The first source's full preprint was not independently inspected beyond its public metadata and abstract; the later full preprint's directly relevant sections were inspected. Unindexed equivalents remain a priority risk. No independent mathematical audit is asserted.

## References
1. Q. Wang, *A Local Block Criterion for Periodic Morse Reductions of Circulant Independence Complexes*, Zenodo v1, August 24, 2026, https://zenodo.org/records/22082056, DOI: 10.5281/zenodo.22082056.
2. Q. Wang and W. Li, *Integral homology lattices of matching and circulant complexes*, arXiv:2610.22082v1, October 15, 2026, https://arxiv.org/html/2610.22082v1, especially Corollary 6.3, Theorems 8.2 and 10.3.
