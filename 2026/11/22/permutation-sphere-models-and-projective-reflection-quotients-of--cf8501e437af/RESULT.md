# Permutation-sphere models and projective reflection quotients of spider independence complexes

## Finding

For integers \(k\geq2\) and \(\ell\geq2\), let \(T_{k,\ell}\) be the tree formed by adjoining \(k\) disjoint paths of \(\ell\) edges to a common hub. Write \(X_{k,\ell}=|\operatorname{Ind}(T_{k,\ell})|\), where \(\operatorname{Ind}\) is the ordinary independent-vertex-set complex. The symmetric group \(S_k\) permutes the arms. It acts on the coordinate permutation representation \(\mathbb R^k\) and trivially on the other displayed factors.

**Equivariant classification.** For every \(m\geq1\),
\[
\begin{aligned}
X_{k,3m}&\simeq_{S_k} *,\\
X_{k,3m+1}&\simeq_{S_k} S\bigl(\mathbb R\oplus(\mathbb R^m\otimes\mathbb R^k)\bigr),\\
X_{k,3m+2}&\simeq_{S_k} S\bigl(\mathbb R^{m+1}\otimes\mathbb R^k\bigr).
\end{aligned}
\]
The last equivalence also holds for \(m=0\) (two-edge arms). Here \(S(V)\) is the unit sphere of a real orthogonal representation \(V\), and equivariant equivalence means a genuine \(S_k\)-homotopy equivalence, not just matching characters.

**Geometric fixed spaces.** If \(H\leq S_k\) has \(o(H)\) orbits on the arms, there is a canonical PL homeomorphism
\[
X_{k,\ell}^{H}\cong_{\mathrm{PL}}|\operatorname{Ind}(T_{o(H),\ell})|.
\]
Consequently the fixed space is contractible when \(3\mid\ell\), is \(S^{m o(H)}\) up to homotopy for \(\ell=3m+1\), and is \(S^{(m+1)o(H)-1}\) up to homotopy for \(\ell=3m+2\). On the unique nonzero reduced integral homology line, an arm permutation \(\sigma\) acts by \(\operatorname{sgn}(\sigma)^m\) in the first sphere case and by \(\operatorname{sgn}(\sigma)^{m+1}\) in the second.

**Exact reflection quotients.** The case \(k=2\) identifies \(T_{2,\ell}\) with the odd path \(P_{2\ell+1}\), and exchanging arms with its reversal \(\tau\). For every \(m\geq1\),
\[
\begin{aligned}
|\operatorname{Ind}(P_{6m+3})|/\langle\tau\rangle&\simeq S^m*\mathbb{RP}^{m-1},\\
|\operatorname{Ind}(P_{6m+5})|/\langle\tau\rangle&\simeq S^m*\mathbb{RP}^{m}.
\end{aligned}
\]
The second formula also holds at \(m=0\), with \(S^0*\mathbb{RP}^0\) contractible. The star denotes the topological join, equivalent to an \((m+1)\)-fold unreduced suspension of the indicated projective space. Paths \(P_{6m+1}\), \(m\geq1\), have contractible independence complexes and contractible reversal quotients. In particular,
\[
\operatorname{Ind}(P_{17})\simeq S^5,\qquad
|\operatorname{Ind}(P_{17})|/\langle\tau\rangle\simeq\Sigma^3\mathbb{RP}^2,\qquad
\widetilde H_4\cong\mathbb Z/2\mathbb Z.
\]
The \(\mathbb Z/2\mathbb Z\) class does not arise from the integral homology of the unquotiented sphere.

## Assumptions and scope

A simple path \(P_j\) has \(j\) vertices. A face of \(\operatorname{Ind}(G)\) is a subset of vertices containing no adjacent pair. The graph \(T_{k,\ell}\) has the hub \(c\) and vertices \(v_{a,j}\), \(1\leq a\leq k\), \(1\leq j\leq\ell\), with edges \(cv_{a,1}\) and \(v_{a,j}v_{a,j+1}\). All actions are the literal simplicial actions induced by permuting \(a\). Fixed spaces and quotients refer to **geometric realizations**, allowing barycenters of setwise invariant faces. No freeness hypothesis is imposed. The claim concerns finite trees and their arm-permutation group; it does not classify arbitrary tree automorphisms.

## Proof

**1. Path recurrence and the inclusion needed at multiples of three.** Write \(I_j=|\operatorname{Ind}(P_j)|\). The standard independence-complex folding lemma states: if distinct nonadjacent vertices \(u,v\) have \(N(u)\subseteq N(v)\), then deleting \(v\) preserves homotopy type. For \(P_j\), \(j\geq3\), take \(u=j\) and \(v=j-2\). After removing \(j-2\), the remaining graph is \(P_{j-3}\) disjoint from the edge joining \(j-1\) and \(j\). Hence
\[
I_j\simeq I_{j-3}*S^0\simeq\Sigma I_{j-3}.
\]
From \(I_1\simeq *\), \(I_2\simeq S^0\), and \(I_3\simeq S^0\), this gives \(I_{3m+1}\simeq *\), \(I_{3m+2}\simeq S^m\), and \(I_{3m}\simeq S^{m-1}\) for \(m\geq1\). Moreover, the inclusion \(I_{3m-1}\hookrightarrow I_{3m}\) is a homotopy equivalence: deletion of the last path vertex yields \(I_{3m-1}\) and its attaching link is \(I_{3m-2}\), contractible by the same recurrence. This last statement is about the **inclusion**, not merely two abstract spaces having the same homotopy type.

For completeness, the folding lemma follows from the elementary acyclic matching pairing every independent face that contains \(v\) and omits \(u\) with the face obtained by adding \(u\). The neighborhood inclusion ensures the latter is a face; the pairs form a valid cone matching on the star of \(v\), leaving precisely the deletion of \(v\). No quantitative finite experiment is needed for this step.

**2. An equivariant hub pushout.** Deleting the hub \(c\) leaves \(k\) disjoint copies of \(P_\ell\), whereas the hub link is the independence complex of \(k\) disjoint copies of \(P_{\ell-1}\). Thus, with \(B=I_\ell^{*k}\) and \(A=I_{\ell-1}^{*k}\),
\[
X_{k,\ell}=B\cup_A(c*A).
\]
This is an exact invariant simplicial pushout, and the group permutes the \(k\) factors and fixes the cone apex. All inclusions are equivariant cofibrations after realization. If \(Y\) is an ordinary nonempty contractible finite complex, the \(k\)-fold join \(Y^{*k}\), under factor permutation, contracts \(S_k\)-equivariantly: use the same contraction of \(Y\) onto a selected point in every factor, then contract the resulting permutation simplex onto its invariant barycenter. In particular, every subgroup fixed space is contractible.

If \(\ell=3m+2\), the link \(A\) is equivariantly contractible, so the inclusion \(B\hookrightarrow X_{k,\ell}\) is an equivariant homotopy equivalence by the equivariant cofibration gluing lemma. Applying the *same* path sphere equivalence \(I_{3m+2}\simeq S^m\) to each join factor yields an equivariant equivalence
\[
B\simeq_{S_k}(S^m)^{*k}\cong_{S_k}S(\mathbb R^{m+1}\otimes\mathbb R^k).
\]
The join-to-unit-sphere map is natural under permutations of equal-dimensional factors.

If \(\ell=3m+1\), \(B\) is equivariantly contractible. Collapsing this equivariantly contractible invariant subcomplex to a point induces an equivariant homotopy equivalence \(X_{k,\ell}\simeq_{S_k}\Sigma A\): on every subgroup-fixed space the contracted subspace is nonempty and contractible, and the fixed-space inclusions are cofibrations. Hence
\[
X_{k,3m+1}\simeq_{S_k}\Sigma(S^{m-1})^{*k}
\cong_{S_k}S(\mathbb R\oplus(\mathbb R^m\otimes\mathbb R^k)),
\]
where the new suspension coordinate is invariant. Finally, if \(\ell=3m\), the path inclusion \(I_{\ell-1}\hookrightarrow I_\ell\) is a homotopy equivalence; its \(k\)-fold join is equivariant (the same inclusion in every factor) and is a fixed-pointwise equivalence for every subgroup. Coning off this equivariant equivalence gives an equivariantly contractible space. This proves the three cases.

**3. An exact model of all fixed points.** Under \(H\le S_k\), every vertex orbit lies at a fixed arm depth. No such orbit contains adjacent vertices. A point of the geometric realization is \(H\)-fixed if and only if it gives equal barycentric weights to the vertices of each \(H\)-orbit, so it is a convex combination of barycenters of independent vertex orbits. The allowed orbit combinations are precisely independent sets of the spider with one arm per orbit of \(H\). The affine orbit-barycenter correspondence produces the asserted PL homeomorphism. Restricting the representation models of Step 2 to the \(H\)-fixed subspaces gives the sphere dimensions. The determinant of a permutation on \(\mathbb R^q\otimes\mathbb R^k\) is \(\operatorname{sgn}(\sigma)^q\); the degree of the induced sphere map equals this determinant, proving the integral orientation statements.

**4. The projective-space orbit models.** When \(k=2\), decompose the permutation representation as \(\mathbb R^2\cong\mathbf1\oplus\varepsilon\), where \(\varepsilon\) is the one-dimensional sign representation. For \(\ell=3m+1\) the representation in Step 2 is \(\mathbf1^{m+1}\oplus\varepsilon^m\). For \(\ell=3m+2\) it is \(\mathbf1^{m+1}\oplus\varepsilon^{m+1}\). For any \(u,v\geq1\), the unit sphere of \(\mathbb R^u\oplus\varepsilon^v\) modulo the sign involution is homeomorphic to
\[
S^{u-1}*(S^{v-1}/(x\sim-x))=S^{u-1}*\mathbb{RP}^{v-1}.
\]
This follows directly by expressing a unit vector as a pair of vectors with squared norms adding to one: the ratio of norms is the join parameter, with the expected endpoint collapses. Equivariant homotopy equivalences descend to homotopy equivalences on orbit spaces. Setting \(u=m+1\), \(v=m\) or \(m+1\) proves both formulas. Reduced integral homology of \(\mathbb{RP}^{2}\) is \(\mathbb Z/2\mathbb Z\) in degree one; a triple suspension shifts it to degree four, proving the \(P_{17}\) instance.

## Verification

Run `python3 checks/verify_spider.py` using Python 3 and only its standard library. The checker directly enumerates all independent faces and geometric orbit-closed faces for \(32\) permutation/arm-length configurations (two- and three-arm spiders with lengths \(2\) through \(5\)), verifies equality with the one-arm-per-orbit simplicial model, checks Euler characteristics and orientation signs, and independently checks reversal-quotient Euler characteristics for \(58\) odd path widths. It outputs `VERIFY_OK`. These are bounded corroborations, **not** proofs of arbitrary lengths, equivariant homotopy types, or projective-space torsion; those follow from the preceding path recurrence, gluing and representation arguments.

## Relationship to prior work

The nonequivariant forest sphere-or-contractible theorem and the path trichotomy are established by Ehrenborg and Hetyei [1, Corollaries 6.1 and 6.3]; neither is claimed new. Kawamura [2] gives an independent inductive method for forest independence homotopy, not an identified classification of the geometric quotients above. Previously published path-reversal work [3, 4] determines the integral orientation sign and geometric fixed-space homotopy types for broader path independence parameters. Those fixed-space and character calculations **do not imply** the homotopy type or integral torsion of the ordinary orbit space. The added claim is a simultaneous equivariant representation-sphere model for uniform-arm spiders, giving exact projective-space joins for all the displayed odd-path reversal quotients. Work on projective suspensions for a bounded-independence *cycle* complex [5] concerns a different object and group action; its quotient theorem does not specialize to path independence complexes.

## Limitations

All equivariant equivalences are homotopy equivalences, not asserted PL homeomorphisms; only the fixed-orbit simplicial model is a PL homeomorphism. The result does not extend without further work to mixed-length arms or arbitrary tree symmetries. Finite checks do not establish infinite assertions. The available full text of the closest 2005 forest paper was inspected, and relevant published path-symmetry results were compared at the statement and proof levels; an equivalent unindexed treatment of the path quotient may still exist. The full text of Kawamura [2] was not obtained, so publication priority remains subject to that residual source-access risk.

## References

[1] R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923, available online 2005-11-28, Corollaries 6.1 and 6.3 and Proposition 6.2, https://www.ms.uky.edu/~jrge/Papers/Independence.pdf .

[2] K. Kawamura, *Homotopy types of independence complexes of forests*, Contributions to Discrete Mathematics 5 (2010), published 2010-09-28, https://cdm.ucalgary.ca/article/view/62064 .

[3] *Path-reversal orientation of all higher-independence spheres* (2026), published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-path-reversal-orientation-of-all-higher-independence-spheres--d1cebdb99d99 .

[4] *Reflection-fixed homotopy types of higher path-independence complexes* (2026), published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-reflection-fixed-homotopy-types-of-higher-path-independence-comp--6730d982e3bb .

[5] *Projective suspensions in half-turn quotients of bounded-independence cycle spheres* (2026), published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-projective-suspensions-in-half-turn-quotients-of-bounded-indepen--4fbd7de8d13d .
