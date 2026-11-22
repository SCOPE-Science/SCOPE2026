# One base-field count pair determines both Burkhardt configuration zeta functions

## Finding
Let \(k=\mathbb F_q\) have characteristic at least seven and \(q\equiv1\pmod 3\). For **every** \(k\)-form \(B\) of the split Burkhardt quartic, let \(J_B\) be its reduced finite étale scheme of 40 geometric Jacobi planes, and let \(N_B\) be its reduced finite étale scheme of 45 geometric ordinary double points. Then the two integers
\[
\bigl(\#J_B(k),\#N_B(k)\bigr)
\]
uniquely determine **both complete finite étale zeta functions** \(Z(J_B,T)\) and \(Z(N_B,T)\), including every count over every extension \(\mathbb F_{q^n}\). There are exactly **15** possible pairs and 15 corresponding joint complete zeta spectra among the 20 Frobenius conjugacy classes of \(\operatorname{PSp}_4(\mathbb F_3)\). Exactly five pairs of distinct conjugacy classes are permanently indistinguishable by either configuration scheme, even using all extensions.

In the table supplied as `spectra.csv`, the columns `plane_cycles` and `node_cycles` record multiplicities `d:m` for Frobenius cycles of length \(d\) and multiplicity \(m\). The row indexed by `class_index` identifies a conjugacy class by its element order, class size and both induced cycle types. The two final columns are precisely the base-field counts. In particular, the count pair \((0,0)\) corresponds to the order-five class, with plane cycles \(5^8\) and node cycles \(5^9\); no planes or nodes become rational before extension degree five. The double rows (4,5), (11,12), (13,14), (17,18), (19,20) are the five permanent collisions.

## Assumptions and scope
The base field has prime characteristic \(p\ge7\), with \(q\equiv1\pmod3\); hence it contains a primitive third root of unity. The split Burkhardt quartic is the projective quartic
\[
y_0(y_0^3+y_1^3+y_2^3+y_3^3+y_4^3)+3y_1y_2y_3y_4=0.
\]
A form is a projective variety that becomes isomorphic to this quartic over a separable closure of \(k\). The 40 planes and 45 nodes are intrinsic reduced geometric configurations on the form; their extension-field rational points are Frobenius-fixed geometric objects. The claim does **not** concern rational points of the threefold itself, its full Hasse–Weil zeta function, or twists in excluded characteristics or fields without a cube root of unity.

## Proof
The automorphism group of the split quartic, over a field containing the third roots of unity, is the constant group \(G=\operatorname{PSp}_4(\mathbb F_3)\), of order 25920. Over a finite field, its forms are classified by \(H^1(k,G)\), which here identifies with conjugacy classes of \(G\) because the absolute Galois group is procyclic and acts trivially on \(G\). Therefore all 20 conjugacy classes occur as Frobenius forms.

The classical equivariant geometry identifies the 40 Jacobi planes with the 40 projective points of the four-dimensional symplectic space \(V=\mathbb F_3^4\). It identifies the 45 nodes with unordered orthogonal decompositions \(V=U\perp U^\perp\) into nondegenerate two-dimensional subspaces. There are 90 such subspaces, paired into 45 decompositions. A projective point lies in one of the two summands exactly when its Jacobi plane is incident to the corresponding node. Thus each node is incident to eight planes, each plane to nine nodes, giving 360 flags. These identifications and their equivariance are established geometric inputs, not new claims.

For completeness, the exact finite group certificate is constructed from the form
\[
\langle a,b\rangle=a_0b_1-a_1b_0+a_2b_3-a_3b_2\quad\text{in }\mathbb F_3
\]
and the six explicit symplectic transvections \(x\mapsto x+\langle x,v\rangle v\) in the bundled standard-library program `check.py`. The program enumerates the 40 projective points and 45 decompositions; verifies the 360 incidences and transvection equivariance; constructs 25920 distinct permutations of their 85-point disjoint union; and exhausts all conjugacy classes by closure under conjugation by the generators and their inverses. Since the resulting subgroup has the known order of \(G\) and acts faithfully, this exhausts \(G\), not a sample. Its 20 conjugacy classes have sizes adding to 25920.

For each class, the program follows the complete finite cycles of its representative on the 40 planes and 45 nodes. Its output agrees exactly with the entire bundled `spectra.csv` table. If the plane cycle multiset is \(P=\{(d,m_d)\}\) and the node cycle multiset is \(N=\{(e,n_e)\}\), then
\[
Z(J_B,T)=\prod_{(d,m_d)\in P}(1-T^d)^{-m_d},\qquad
Z(N_B,T)=\prod_{(e,n_e)\in N}(1-T^e)^{-n_e}.
\]
The rational count of each scheme is the multiplicity of its one-cycles; the degree-\(n\) count is the sum of \(d m_d\) over \(d\mid n\) (respectively \(e n_e\) over \(e\mid n\)). The certified table has exactly 15 different pairs of one-cycle multiplicities. Classes with equal one-cycle pairs have the **same two complete cycle multisets**. Thus one base-field pair determines both complete zeta functions. The table also has exactly five unordered pairs of distinct classes with the same complete multisets, proving the precise residual ambiguity.

## Verification
Run `python3 check.py` alongside `spectra.csv` with Python 3.9 or newer. The checker uses only the standard library and reconstructs the full group and every conjugacy-class spectrum from the defined symplectic form; it does not read an external precomputed group or rely on probabilistic testing. Its successful final line is `BURKHARDT_40_PLANES_45_NODES_25920_GROUP_20_CLASSES_15_JOINT_SPECTRA_VERIFIED`. The 20-row CSV specifies all rational count pairs, full cycles, orders and class sizes. The finite enumeration is exhaustive because every one of the 25920 group elements and every class orbit is generated.

## Relationship to prior work
Hoffman–Weintraub describe the 40 projective points and the 45 orthogonal decompositions in their level-three Siegel modular geometry and compute the arithmetic of the untwisted modular compactification. Bruin–Nasserden (2017 preprint) identify the 40 Jacobi planes, their moduli interpretation and the zeta function of the split Burkhardt quartic. Bruin–Filatov (2022 preprint) establish existence and cohomological classification of Burkhardt twists and the invariant 45-node configuration; they do not present a 20-class joint node–plane Frobenius table or the one-extension reconstruction assertion in the inspected text. Cheltsov–Tschinkel–Zhang discuss the equivariant geometry of the 40 planes and 45 nodes. These geometric and twisting inputs are **credited**. The new claim is the arithmetic 20-class calculation and the unexpected exact equivalence between a pair of base-field counts and the full joint zeta spectra.

## Limitations
The result distinguishes 15 joint spectra, **not** all 20 forms. Five pairs remain indistinguishable even over all extensions. It does not determine the full zeta function of a Burkhardt quartic, its rational birational type or the splitting of its exceptional quadrics. The finite group calculation is an exhaustive exact algorithmic proof whose elementary source code and table are supplied, rather than a hand-written classification of 20 conjugacy types. Historical priority is subject to an unindexed equivalent permutation-character/cycle-index calculation, particularly in the classical finite symplectic group literature. The count and geometry assumptions are not asserted in excluded small characteristics.

## References
- J. W. Hoffman and S. H. Weintraub, *The Siegel Modular Variety of Degree Two and Level Three*, freely available author's manuscript, https://www.math.lsu.edu/~hoffman/papers/level3final.pdf . See Sections 1.6 and 3.2 for the 40 points, 45 unordered decompositions, and equivariant incidence.
- N. Bruin and B. Nasserden, *Arithmetic aspects of the Burkhardt quartic threefold*, arXiv:1705.09006, first public 2017-05-25, https://arxiv.org/abs/1705.09006 .
- N. Bruin and E. Filatov, *Twists of the Burkhardt quartic threefold*, arXiv:2207.04393, first public 2022-07-10, https://arxiv.org/abs/2207.04393 .
- I. Cheltsov, Y. Tschinkel and Z. Zhang, *Equivariant geometry of the Segre cubic and the Burkhardt quartic*, arXiv:2308.15271, https://arxiv.org/abs/2308.15271 .
