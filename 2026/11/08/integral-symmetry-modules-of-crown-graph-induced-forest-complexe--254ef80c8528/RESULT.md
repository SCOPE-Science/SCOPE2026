# Integral symmetry modules of crown-graph induced-forest complexes

## Finding
For every integer \(n\geq 3\), let \(C_n\) be the crown graph with vertices \(a_1,\ldots,a_n,b_1,\ldots,b_n\) and edges \(a_i b_j\) precisely when \(i\ne j\). Let \(\mathcal F(C_n)\) consist of those vertex subsets inducing an acyclic graph. The group \(G_n=S_n\times C_2\) acts by simultaneous permutations of the labels and by exchanging the two vertex layers. Define \(W_n=\ker(\mathbb Z^n\xrightarrow{\sum}\mathbb Z)\), let \(P_{n,3}=\mathbb Z[\binom{[n]}{3}]\) be the permutation lattice on three-element label sets, and write \(\varepsilon\) for the one-dimensional lattice on which the layer-exchange involution acts by \(-1\) and \(S_n\) acts trivially. Then there are isomorphisms of **integral** \(G_n\)-modules
\[
\widetilde H_4(\mathcal F(C_n);\mathbb Z)\cong P_{n,3}\otimes\varepsilon,\qquad
\widetilde H_3(\mathcal F(C_n);\mathbb Z)\cong\bigwedge^3 W_n\otimes\varepsilon.
\]
All other reduced integral homology groups vanish. In degree four, an explicit basis is formed by the oriented fundamental cycles of the boundaries of the five-simplices on \(\{a_i,a_j,a_k,b_i,b_j,b_k\}\), one for each unordered label triple \(\{i,j,k\}\).

For \(\sigma\in S_n\), write \(f,t,u\) for its numbers of cycles of lengths one, two, and three, respectively. If \(s\in\{0,1\}\) denotes whether layers are exchanged, the complete character formulas are
\[
\chi_4(\sigma,s)=(-1)^s\left(\binom f3+ft+u\right),\qquad
\chi_3(\sigma,s)=(-1)^s\left(\binom{f-1}{3}-(f-1)t+u\right).
\]
Here \(\binom{x}{3}=x(x-1)(x-2)/6\) is the polynomial binomial coefficient (including \(x=-1\)). In particular, layer exchange negates both homology groups; these modules cannot be recovered from nonequivariant Betti numbers alone.

## Assumptions and scope
All graphs are finite, simple and undirected; chains and homology are reduced integral simplicial chains unless otherwise stated. The crown graph is the **categorical** graph product \(K_2\times K_n\), not a Cartesian product. The group action is the canonical faithful action for \(n\geq3\). The subcomplex \(\mathcal F_2(C_n)\) consists of acyclic induced subsets of maximum induced degree at most two; its inclusion into \(\mathcal F(C_n)\) is equivariant and induces an isomorphism on integral homology, by the established filtration result [2, Lemma 40]. Its nonequivariant homotopy groups are not claimed as new: [2, Proposition 41] already gives \(\bigvee^{\binom n3}S^4\vee\bigvee^{\binom{n-1}3}S^3\). The new assertion concerns the complete **integral group actions**, including both degrees and the side-exchange signs.

## Proof
**1. A natural cover.** Let \(K=\mathcal F_2(C_n)\). For each triple \(T\subset[n]\), let \(X_T\) be the full subcomplex on the six vertices with labels in \(T\); since the induced graph is a six-cycle, \(X_T\) is the boundary of the five-simplex and is homeomorphic to \(S^4\). Let \(A\) and \(B\) be the full simplices on the respective vertex layers. Then
\[
K=A\cup B\cup\bigcup_{|T|=3}X_T.
\]
For completeness: a forest face that uses both sides either uses at most one vertex from one side, or has layer sizes \((2,2),(2,3),(3,2)\). The \((2,2)\) case needs at least one repeated label; each \((2,3)\) or \((3,2)\) case needs both labels from the smaller side repeated. The degree-at-most-two condition rules out \((1,b)\) or \((a,1)\) when the larger side has at least four vertices, and permits a three-vertex larger side only when its repeated label is present. Every such mixed face belongs to some \(X_T\), and single-layer faces belong to \(A\) or \(B\).

For distinct triples \(T_1,\ldots,T_r\), their common intersection consists of the full simplex on both copies of the common labels if their label intersection is nonempty (it has at most two labels), and is empty otherwise. Intersections with \(A\) or \(B\) are pure-layer simplices. Since \(A\cap B=\varnothing\), every nonempty multiple intersection of distinct members of this cover is contractible. All intersections and the cover are permuted naturally by \(G_n\).

**2. The integral homology cover spectral sequence.** The homological Mayer–Vietoris (or Cech double-chain) spectral sequence of this finite cover has a bottom row equal to the ordinary simplicial chain complex of its nerve \(U\), with trivial \(H_0\) coefficients on nonempty intersections. Its only other nonzero entry on the first page is
\[
E^1_{0,4}=\bigoplus_{|T|=3}H_4(X_T;\mathbb Z).
\]
Indeed \(A\) and \(B\) are contractible, each \(X_T\) has only positive homology in degree four, and every intersection of at least two distinct cover members is contractible. All these statements hold integrally and functorially for \(G_n\). The nerve \(U\) is the simplicial suspension of \(N\), the nerve of the cover of \(\operatorname{sk}_2\Delta^{n-1}\) by its triangular faces. The three-element subsets are the nerve vertices, and a collection spans a simplex precisely when the label triples have a nonempty common intersection. The two suspension apices correspond to \(A\) and \(B\), which are exchanged by the layer involution.

The cover of \(\operatorname{sk}_2\Delta^{n-1}\) by its triangles has contractible nonempty intersections. The natural, equivariant integral-homology comparison from the cover double-chain complex gives
\[
\widetilde H_3(U;\mathbb Z)\cong\widetilde H_2(\operatorname{sk}_2\Delta^{n-1};\mathbb Z)\otimes\varepsilon.
\]
The same skeleton has no reduced homology other than degree two, where its homology is free of rank \(\binom{n-1}{3}\). Thus the only positive-degree entries on the second page are \(E^2_{3,0}\) and \(E^2_{0,4}\). No differential can enter or leave either: the sole potentially relevant higher differential would start from \(E^5_{5,0}=0\). The spectral sequence therefore gives canonical integral \(G_n\)-module identifications
\[
\widetilde H_3(K;\mathbb Z)\cong\widetilde H_3(U;\mathbb Z),\quad
\widetilde H_4(K;\mathbb Z)\cong\bigoplus_{|T|=3}\widetilde H_4(X_T;\mathbb Z).
\]
There are no extension problems, since each total degree has only one surviving filtration summand.

**3. Explicit module structures.** Put \(V=\mathbb Z^n\) with the standard label-permutation action and let \(\alpha:V\to\mathbb Z\) send every standard basis vector to one. The augmented simplicial boundary on the complete simplex is the contraction \(\iota_\alpha\) on \(\bigwedge^\bullet V\). Since \(V=W_n\oplus \mathbb Z e_1\) as abelian groups, \(\ker(\iota_\alpha:\bigwedge^3V\to\bigwedge^2V)=\bigwedge^3W_n\); the identification is independent of that non-equivariant splitting and is \(S_n\)-natural. This kernel equals \(\widetilde H_2(\operatorname{sk}_2\Delta^{n-1};\mathbb Z)\). Exchange of the suspension apices changes orientation by \(-1\), giving the \(\varepsilon\) tensor factor in degree three.

For degree four, orient the fundamental cycle of \(X_T\) as \(\partial[a_i,a_j,a_k,b_i,b_j,b_k]\) for \(i<j<k\). Relabeling by any \(\sigma\in S_n\) induces the **same** permutation on each three-vertex block, hence an even permutation on all six vertices, and sends this cycle with **positive** coefficient to the cycle for \(\sigma(T)\). Exchanging the layers transposes two blocks of size three and has sign \((-1)^9=-1\). Thus the basis of \(\bigoplus_TH_4(X_T)\) affords exactly \(P_{n,3}\otimes\varepsilon\). The inclusion into \(\mathcal F(C_n)\), by the canonical homology isomorphism in [2, Lemma 40], transfers both integral representations to the unrestricted forest complex.

**4. Character calculation.** In degree four, the trace of \(\sigma\) is the number of its invariant triples, namely \(\binom f3+ft+u\). In degree three, the standard determinant identity
\[
\det(1+z\sigma\mid W_n)=\frac{\prod_{c\in\operatorname{Cycles}(\sigma)}(1-(-z)^{|c|})}{1+z}
\]
shows that the coefficient of \(z^3\) is \(\binom{f-1}{3}-(f-1)t+u\). The common layer-exchange sign gives the displayed character formulas. No inference from finite experiments is used in the proof.

## Verification
Run `python3 verify_crown_forest.py` from this directory. This standalone script enumerates all vertex subsets independently by depth-first-search acyclicity for \(3\leq n\leq7\), checks the closed face criterion, and computes mod-two boundary ranks. It verifies the distinguished six-cycle sphere chains have zero integral boundary. For every element of \(S_n\times C_2\) with \(3\leq n\leq6\) (1,740 actions in total), it reconstructs vertex orbits and independently compares the signed simplicial Lefschetz trace with the module character. The saved run is in `verification_output.txt`. These computations corroborate, but do not replace, the uniform integral-cover proof above.

## Relationship to prior work
The archival framework is Taylan's graph-devoid complex [1], which permits any forbidden family of cycles and hence the induced-forest complex. Carnero Bravo [2] explicitly defines the forest filtration and **already proves** the nonequivariant crown-graph homotopy type for all \(n\) in Proposition 41. Its proof uses the sphere-and-simplex cover that is refined here. The distinction is mathematical, not terminological: the original proposition identifies abstract sphere multiplicities but does not state the natural \(S_n\times C_2\) **integral representations**, the augmentation-lattice exterior cube, or the layer-involution signs. The present proof tracks the group action through that cover, its nerve and the integral spectral sequence, rather than claiming a new sphere count. This is a relatively close natural refinement of [2], and possible implicit equivariant consequences of its spectral-sequence construction remain a priority caveat.

## Limitations
The result concerns ordinary reduced integral homology representations, not equivariant homotopy types or a canonical equivariant wedge splitting. It uses the nonequivariant sphere-wedge and filtration theorems from [2], with new equivariant bookkeeping and identification. Neither independence from unpublished work nor independent validation is claimed. For \(n=3\), the exterior-cube term is zero; the formulas still apply. The case \(n=2\) is excluded.

## References
[1] D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754, first public arXiv submission 2015-01-27, https://arxiv.org/abs/1501.06754; definitions and matching-tree framework, Section 3.

[2] A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first public submission 2023-07-25, https://arxiv.org/abs/2307.13271; Lemma 40 and Proposition 41, PDF pp. 27–29 (nonequivariant crown-graph homotopy classification).
