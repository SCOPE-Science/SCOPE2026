# Uniform degree-twelve Aronhold-heptad bound and the exceptional Frobenius class

## Finding
Let \(C/\mathbb F_q\) be any smooth geometrically connected plane quartic over an odd finite field. An **Aronhold heptad** is an unordered seven-set of its 28 geometric odd theta characteristics (equivalently bitangents) with the property that the sum of every three, in the affine theta-characteristic torsor, is even. There are 288 heptads. Let \(d_A(C)\) be the smallest positive integer \(d\) for which at least one heptad is invariant under \(q^d\)-Frobenius (not necessarily with its seven members individually rational).

Then
\[
d_A(C)\in\{1,2,3,4,6,8,9,12\},\qquad d_A(C)\le 12.
\]
The following **complete abstract Frobenius spectrum** classifies all elements of \(\operatorname{Sp}_6(\mathbb F_2)\) by the least extension degree fixing one of the 288 Aronhold heptads. The counts classify symplectic elements and classes, **not** plane-quartic isomorphism classes or realizability over a specified finite field.

| Least extension degree | Symplectic elements | Conjugacy classes |
|---:|---:|---:|
| 1 | 694,477 | 15 |
| 2 | 159,075 | 6 |
| 3 | 99,008 | 2 |
| 4 | 15,120 | 2 |
| 6 | 20,160 | 1 |
| 8 | 181,440 | 2 |
| 9 | 161,280 | 1 |
| 12 | 120,960 | 1 |


Exactly one symplectic conjugacy class has minimum 12: the ATLAS class \(12\mathrm{C}\), with \(120960\) elements, each acting on the 288 heptads as \(24\) disjoint cycles of length \(12\). This action nevertheless fixes an odd theta characteristic (a bitangent), and its shortest even-theta/Cayley-octad cycle has length \(6\). Thus existence of a rational bitangent, or of a Cayley octad over a degree-six extension, does **not** force an Aronhold heptad over any proper divisor of degree 12 at the level of abstract Frobenius actions.

The bound is sharp for the abstract symplectic action. **It is not proved here that an odd-characteristic plane quartic with Frobenius class \(12\mathrm{C}\) exists**, so geometric sharpness of the universal degree-twelve bound is open in this statement.

## Assumptions and scope
The base is an odd-characteristic finite field and \(C\) is smooth and canonically embedded as a nonhyperelliptic genus-three quartic. The theta-characteristic torsor has 64 elements, of which 28 are odd and 36 even. The geometric Galois action preserves parity and the Weil pairing, and consequently factors through \(\operatorname{Sp}_6(\mathbb F_2)\). The 288-point heptad action is the transitive coset action with point stabilizer \(S_7\). A heptad is rational when the **set**, not each individual bitangent, descends. We do not assume or assert all abstract Frobenius classes are realized by curves over any particular finite field.

## Proof
Choose the six-dimensional symplectic vector space \(V=\mathbb F_2^6\), with \(x=(u,v)\), \(u,v\in\mathbb F_2^3\), alternating pairing
\[
B((u,v),(u',v'))=u\cdot v'+v\cdot u',\qquad Q_0(u,v)=u\cdot v.
\]
The 64 theta refinements are \(Q_a(x)=Q_0(x)+B(a,x)\); parity is \(Q_0(a)\). Enumerate the 28 odd indices \(a\) with \(Q_0(a)=1\). For each seven-subset \(H\), check \(Q_0(a+b+c)=0\) for every triple of its indices. This is exactly the asyzygetic Aronhold condition because the triple sum of three odd refinements has parameter \(a+b+c\). A direct, exhaustive \(\binom{28}{7}\) seven-subset enumeration gives precisely 288 such subsets. The attached program constructs this enumeration rather than assuming an external heptad list.

Symplectic transvections \(x\mapsto x+B(x,w)w\), for nonzero \(w\in V\), generate \(\operatorname{Sp}_6(\mathbb F_2)\). Breadth-first closure from the identity enumerates exactly \(1451520\) distinct invertible symplectic matrices, matching its known order. For each matrix \(g\), the refinement action is \(Q_a\mapsto Q_a\circ g^{-1}\). Evaluating its six coordinate basis values determines the new parameter; thereby the program obtains the two cycle signatures on 28 odd and 36 even refinements. Exactly 30 distinct **paired** signatures occur.

The group has exactly 30 conjugacy classes, as verified against the ATLAS class table. The paired signature is constant under conjugacy; since 30 different signatures occur, each is precisely one full conjugacy class. Hence taking one representative of each signature, computing its induced permutation of all 288 enumerated heptads, and weighting by the number of group elements with that signature exhaustively evaluates the Aronhold action of **every** symplectic element. Cycle decomposition yields the displayed eight minimum values and the element/class totals; the standalone calculation and its human-readable 30-profile table reproduce the complete certificate.

For the unique class with least heptad cycle 12, the program gives 24 cycles each of length 12 and group-element count 120960. Its centralizer size is \(1451520/120960=12\); the ATLAS table contains a single order-twelve class with centralizer 12, labelled \(12\mathrm{C}\). Its odd-refinement permutation has a fixed point while its even-refinement permutation has minimum cycle length six. These conclusions are exact finite group statements, not extrapolations from finite-field samples.

Finally, geometric Frobenius for any \(C\) is an element of this symplectic group. Its heptad orbit lengths determine the fields of definition of rational heptads, hence the least degree must be among the eight computed minima and at most twelve.

## Verification
Run `c++ -O2 -std=c++17 verify_aronhold.cpp -o verify_aronhold && ./verify_aronhold` (with a C++17 compiler). The program reconstructs all 288 seven-sets, enumerates the entire symplectic group using 63 transvections, verifies 30 distinct paired odd/even signatures, reconstructs the full 288-heptad permutation for each class, and prints 30 class profiles and eight degree totals. Compare the summary with `minimum_degrees.csv` and the class profiles with `class_profiles.csv`, embedded alongside the verifier. The computation provides a finite exhaustive certificate, not a probabilistic experiment. It does not prove geometric realizability of any listed abstract class.

## Relationship to prior work
Elsenhans–Jahnel (2017, first posted 2017-10-19) study Galois actions on bitangents and prescribed invariant Cayley octads. Bergvall (first posted 2021-06-24) explains the 288 Aronhold heptads, their role in marked plane-quartic moduli, and their symplectic actions. The ATLAS of finite group representations already gives the 288-point permutation action and all 30 conjugacy classes of \(\operatorname{Sp}_6(\mathbb F_2)\). These basic objects, group orders, conjugacy classes, and permutation representations are **prior work**, not new results. The new claim is specifically the evaluated least rational-heptad extension-degree spectrum with exact group multiplicities and the class-\(12\mathrm{C}\) cross-comparison with odd/even theta fields. The ATLAS representation permits this computation in principle, so the result should be regarded as a refined arithmetic evaluation of classical group data, rather than a new group action.

## Limitations
The eight-value list is a set of necessary possibilities for arbitrary curves, not an assertion that all eight occur over each finite field. In particular, the group-theoretic witness \(12\mathrm{C}\) is not constructed as a Frobenius action of an actual plane quartic. An equivalent older 288-point permutation-cycle or subgroup-covering table could imply this finite statement; its absence from accessible searched literature cannot rule that out. No characteristic-two assertion is made. No geometry of rational points on the quartic or all seven individually rational bitangents is inferred.

## References
1. A.-S. Elsenhans and J. Jahnel, *On plane quartics with a Galois invariant Cayley octad*, arXiv:1710.07279, first posted 19 October 2017, especially introduction and §2; https://arxiv.org/abs/1710.07279.
2. O. Bergvall, *Arithmetic and topology of classical structures associated to plane quartics*, arXiv:2106.13072, first posted 24 June 2021; https://arxiv.org/abs/2106.13072.
3. ATLAS of Finite Group Representations, *Symplectic group S6(2)*, group order and 30 conjugacy classes; https://brauer.maths.qmul.ac.uk/Atlas/v3/clas/S62/.
4. ATLAS, *S6(2) permutation representation on 288 points*, stabilizer S7, https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/S62G1-p288B0.
