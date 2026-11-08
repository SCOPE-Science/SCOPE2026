# The affine homology representation of the Paley-\(31\) directed flag complex
## Finding
Let \(P_{31}\) be the tournament on \(\mathbb F_{31}\) with \(u\to v\) precisely when \(v-u\) is a nonzero square. Let \(X=\operatorname{dFl}(P_{31})\) be its transitive-subtournament (acyclic) simplicial complex and let
\[
G=\{x\mapsto ax+b:a\in(\mathbb F_{31}^{\times})^2,\ b\in\mathbb F_{31}\}\cong C_{31}\rtimes C_{15}.
\]
Write \(\mathbb Q[G]\) for the regular representation and \(W=\mathbb Q[\mathbb F_{31}]/\mathbb Q\mathbf1\) for the augmentation quotient of the natural permutation representation, which has dimension \(30\). Then the **entire reduced rational homology representation** is
\[
\widetilde H_i(X;\mathbb Q)=0\ (i\ne4),\qquad
\widetilde H_4(X;\mathbb Q)\cong 2\,\mathbb Q[G]\oplus W
\quad\text{as }\mathbb Q[G]\text{-modules}.
\]
In particular, \(W\) is rationally irreducible, the fixed subspace \(\widetilde H_4(X;\mathbb Q)^G\) has dimension \(2\), and the invariants under the translation subgroup \(C_{31}\) have dimension \(30\). The restriction to any point-stabilizer \(C_{15}\) consists of \(64\) regular representations. The character is \(960\) at the identity, \(-1\) at each nonidentity translation, and \(0\) at the remaining \(434\) affine transformations.

## Assumptions and scope
The nonzero quadratic residues in \(\mathbb F_{31}\) are
\[
Q=\{1,2,4,5,7,8,9,10,14,16,18,19,20,25,28\}.
\]
For each nonempty \(F\subseteq\mathbb F_{31}\), the vertices of \(F\) form a simplex of \(X\) if and only if their induced directed complete graph has no directed cycle. In a tournament, acyclicity is equivalent to the existence of a unique compatible total order, and also equivalent to having the sorted outdegrees \(0,1,\ldots,|F|-1\). The action is claimed for the explicitly defined affine subgroup \(G\); a classification of every automorphism of the tournament is not required. The result is rational and does **not** assert an integral representation-lattice classification, an equivariant homotopy decomposition, or a classification for other Paley primes.

## Proof
**Step 1: exhaustive rational homology calculation.** Enumerate transitive subsets in strictly increasing vertex-label order, extending a set only when the induced tournament remains transitive. Every nonempty transitive subset is generated exactly once, since all its subsets are transitive. The exact resulting simplex counts in dimensions \(0\) through \(6\) are
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6)=(31,465,3255,9765,10695,3255,465).
\]
Their alternating sum minus one is \(960\), the reduced Euler characteristic. Independent cyclic-incidence counting checks the vector by counting faces through vertex \(0\) and using translation transitivity. The ranks of the simplicial boundary maps \(\partial_d:C_d(X;\mathbb F_2)\to C_{d-1}(X;\mathbb F_2)\), for \(d=1,\ldots,6\), are
\[
(30,435,2820,6945,2790,465).
\]
The finite verifier constructs the actual boundary columns, performs complete bit-exact Gaussian elimination, and checks all consecutive boundary compositions vanish. Therefore the unreduced mod-two Betti vector is
\[
(1,0,0,0,960,0,0).
\]
The rational Betti number in any degree cannot exceed its mod-two counterpart (universal coefficients, or reduction of integer matrices). The rational homology thus vanishes outside degrees \(0\) and \(4\); the reduced Euler characteristic forces \(\dim\widetilde H_4(X;\mathbb Q)=960\). This argument does not make any statement about integral torsion.

**Step 2: character via fixed faces.** Every affine map \(g(x)=ax+b\) with square multiplier \(a\) preserves the orientation, because \(g(v)-g(u)=a(v-u)\). These \(465=31\cdot15\) distinct maps form \(G\). A nonidentity translation fixes no vertex, while a map with \(a\ne1\) fixes exactly one vertex. A setwise fixed transitive subtournament is fixed pointwise: its unique tournament-compatible total order is preserved by \(g\), and a finite total order has only the identity automorphism. Thus the simplicial chain trace of \(g\) counts precisely the simplices on fixed vertices, with orientation sign \(+1\). The **reduced** Lefschetz number is consequently
\[
\widetilde L(g)=\begin{cases}960,&g=1,\\-1,&a=1,\ b\ne0,\\0,&a\ne1.\end{cases}
\]
By the Hopf trace formula, and since rational reduced homology is concentrated in even degree \(4\), this is exactly the character \(\chi_{\widetilde H_4}(g)\).

**Step 3: representation identification.** The regular module \(\mathbb Q[G]\) has character \(465\) at identity and zero elsewhere. The augmentation module \(W\) has character \(|\operatorname{Fix}_{\mathbb F_{31}}(g)|-1\), giving \((30,-1,0)\) on the three types of group elements. Therefore \(2\mathbb Q[G]\oplus W\) has precisely the character above. Rational semisimplicity identifies the modules. Restricting \(W\) to translations is the degree-\(30\) cyclotomic representation of \(C_{31}\), which is irreducible over \(\mathbb Q\) by irreducibility of \(\Phi_{31}\); hence \(W\) is irreducible for \(G\). The two regular summands give exactly two \(G\)-fixed vectors and \(30\) translation-fixed vectors. Restriction to \(C_{15}\) has character \((960,0,\ldots,0)\), hence is \(64\mathbb Q[C_{15}]\).

## Verification
Run `python3 verify.py` with standard Python 3. The program generates all \(27{,}931\) nonempty simplices, checks the face-incidence cross-count, forms and reduces every mod-two boundary column, verifies \(\partial^2=0\), enumerates all \(465\) affine transformations and their orientation-preserving action, and checks the character and regular-plus-augmentation formula. The exact expected output is `verification_output.txt`. These are exhaustive finite algorithms; no random sampling, timeouts or incomplete ranges are used.

## Relationship to prior work
The archived acyclic-tournament literature develops this simplicial construction, including its relationship to graph coloring [1]. Govc's full-text Proposition 3.4 classifies doubly regular tournament directed-flag homotopy types only through \(27\) vertices [2]. An existing exact calculation establishes the **nonequivariant** wedge \(X\simeq\bigvee^{960}S^4\), but does not determine its affine homology module [3]. A different established computation determines the affine symmetry of the **nineteen-vertex** Paley tournament, whose rational homology occurs in two dimensions; it has neither the same group nor the stated \(31\)-vertex representation [4]. The present claim supplies the complete \(465\)-element character and a rational module decomposition independently supported by a new exhaustive mod-two boundary calculation. The general identity between fixed simplices and fixed vertices is a standard Lefschetz mechanism; the concrete \(960\)-dimensional module, irreducible constituent, and fixed-subspace dimensions are not a restatement of the nonequivariant homotopy type.

## Limitations
The integral torsion, integral \(G\)-lattice and equivariant homotopy type are not determined. The result treats the given affine subgroup, without a separate claim that it equals the full tournament automorphism group. The archived paper [1] was available through publisher abstract and bibliographic information but not full text; and an accessible full-text copy could not be obtained. Consequently its precise uninspected internal statements remain a bibliographic risk, though the later full-text classification [2], the exact same-object prior result [3], and the closely related affine calculation [4] were inspected. Literature searches and prior-record comparisons cannot prove universal publication priority.

## References
[1] Z. Deniz, *Topology of acyclic complexes of tournaments and coloring*, Applicable Algebra in Engineering, Communication and Computing 26 (2015), 213–226. DOI: https://doi.org/10.1007/s00200-014-0245-0. First published online **2014-12-27**.

[2] D. Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333v1 (2020), full text §3.2, Proposition 3.4. https://arxiv.org/abs/2006.05333

[3] *Exact homotopy type of the directed flag complex of the Paley tournament on 31 vertices*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-homotopy-type-of-the-directed-flag-complex-of-the-paley-to--e960fd7ad6c9

[4] *Affine symmetry identifies the Paley-19 directed flag complex and its homology character*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-affine-symmetry-identifies-the-paley-19-directed-flag-complex-an--9f50497a76ce
