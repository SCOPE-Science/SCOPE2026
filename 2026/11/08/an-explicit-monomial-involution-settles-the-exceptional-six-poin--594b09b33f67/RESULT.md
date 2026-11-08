# An explicit monomial involution settles the exceptional six-point toric-code equivalence over the field of eight elements

## Finding

Let \(k=\mathbb F_8\), and let \(T=(k^*)^2\) be the torus of \(49\) rational points. Define the two lattice polygons from Luo–Yau–Zhang–Zuo, Figure 1.4 in arXiv:1402.0060 (Figure 1 in the published article), by their complete lattice-point sets
\[
P_4\cap\mathbb Z^2=\{(0,0),(1,0),(2,0),(3,0),(0,1),(0,-1)\},
\]
\[
P_5\cap\mathbb Z^2=\{(0,0),(1,0),(2,0),(3,0),(0,1),(-1,-1)\}.
\]
Here \(P_4\) is the polygon denoted \(P_6^{(4)}\), and \(P_5\) is the one denoted \(P_6^{(5)}\), in that paper. Write \(C(P_i)\subseteq k^{49}\) for the evaluation of all six Laurent monomials at \(T\).

**The two evaluation codes are monomially equivalent.** More precisely, the invertible monomial operator
\[
(\mathscr Tf)(x,y)=x^3 f(x^{-1},x^{-3}y),\qquad (x,y)\in T,
\]
interchanges \(C(P_4)\) and \(C(P_5)\) and satisfies \(\mathscr T^2=\mathrm{id}\). This proves Conjecture 1.1 in Luo–Yau–Zhang–Zuo, *On classification of toric surface codes of low dimension* (2014 preprint; 2015 publication), which explicitly left this pair undecided over \(\mathbb F_8\). Together with that work's Theorem 1.2, it removes the sole outstanding monomial-equivalence ambiguity in their dimension-six classification.

The polygons themselves are **not** equivalent under integral affine unimodular transformations: \(P_4\) has four boundary lattice points and \(P_5\) has three. The equivalence is therefore genuinely finite-field and not induced by an integer lattice equivalence.

## Assumptions and scope

The field is exactly \(k=\mathbb F_8\), not a variable characteristic-two field. The length is \((8-1)^2=49\), and both codes have dimension six. A monomial equivalence means an invertible permutation of the \(49\) coordinates combined with multiplication of each coordinate by a nonzero field element. Laurent monomials are well defined because both coordinates of points of \(T\) are nonzero. The same formula considered over an arbitrary field need not map one six-dimensional evaluation space to the other: the crucial identity \(x^6=x^{-1}\) holds on \(k^*\) because \(x^7=1\).

## Proof

**1. Identification of the six sections.** The first polygon has vertices \((0,1),(3,0),(0,-1)\), normalized area \(6\), and precisely the stated six lattice points. The second has vertices \((-1,-1),(0,1),(3,0)\), normalized area \(7\), and precisely its stated six lattice points. Consequently the associated six-dimensional spaces of Laurent functions are
\[
L_4=\{A(x)+b y+c y^{-1}:\deg A\le3,\ b,c\in k\},
\]
\[
L_5=\{B(x)+b y+c x^{-1}y^{-1}:\deg B\le3,\ b,c\in k\}.
\]
The six distinct exponent characters are independent as functions on the \(7\)-torsion torus \(T\), so both evaluation maps have rank six.

**2. Coordinate permutation and weights.** The map
\[
\phi:T\longrightarrow T,\qquad \phi(x,y)=(x^{-1},x^{-3}y)
\]
is bijective and indeed satisfies \(\phi^2=\mathrm{id}\). For every \((x,y)\in T\), the scalar \(x^3\) is nonzero. Therefore \(\mathscr T\), defined by permuting coordinates according to \(\phi\) and multiplying the coordinate indexed by \((x,y)\) by \(x^3\), is an ambient monomial transformation of \(k^{49}\). Also \(x^3(x^{-1})^3=1\), so \(\mathscr T^2=\mathrm{id}\).

**3. Transformation of the section spaces.** For an arbitrary \(A(x)=a_0+a_1x+a_2x^2+a_3x^3\), direct substitution yields
\[
\begin{aligned}
\mathscr T\big(A(x)+b y+c y^{-1}\big)
&=x^3 A(x^{-1})+b y+c x^6y^{-1}\\
&=a_3+a_2x+a_1x^2+a_0x^3+b y+c x^{-1}y^{-1}.
\end{aligned}
\]
The last equality holds for every \(x\in k^*\), since \(x^7=1\). The right side belongs to \(L_5\). Reversal of the four coefficients \((a_0,a_1,a_2,a_3)\mapsto(a_3,a_2,a_1,a_0)\) is invertible, leaving \(b,c\) fixed. Hence \(\mathscr T(L_4)=L_5\) as evaluation spaces. In generator-matrix language, the explicit row matrix is the reversal permutation in the first four rows, direct sum the \(2\times2\) identity, and the coordinate matrix is the permutation \(\phi\) times \(\operatorname{diag}(x^3)\).

**4. Why this does not contradict lattice inequivalence.** On characters \(x^a y^b\), the same substitution sends the exponent \((a,b)\) to \((3-a-3b,b)\). Thus the source point \((0,-1)\) is sent to \((6,-1)\). On \(T\) its character equals \(x^{-1}y^{-1}\), because exponents agree modulo \(7\). The special wraparound \(6\equiv-1\pmod 7\) is exactly why the equivalence holds on \(\mathbb F_8^*\) without an integral affine equivalence between the polygons. Their differing boundary-point numbers \(4\) and \(3\) prove that no integral affine unimodular map carries \(P_4\) onto \(P_5\).

## Verification

The standalone exact-arithmetic script `verify_equivalence.py` constructs \(\mathbb F_8=\mathbb F_2[\alpha]/(\alpha^3+\alpha+1)\), evaluates both six-section matrices on all \(49\) torus points, verifies both ranks are six, checks the proposed coordinate permutation is bijective, and verifies each of the \(49\) column identities, with the indicated row reversal. Run `python3 verify_equivalence.py` from the extracted directory. The recorded output in `verification_output.txt` ends with `VERIFY_OK`. The symbolic substitution in the proof, rather than enumeration, establishes the result for all codewords.

## Relationship to prior work

Luo, Yau, Zhang and Zuo (arXiv:1402.0060, first posted 2014-02-01; published in *Finite Fields and Their Applications* 33 (2015), 90–102) displayed the two six-point polygons, proved non-equivalence of all other relevant pairs apart from the published exceptions, found equal weight enumerators for the present pair over \(\mathbb F_8\), and **stated their monomial equivalence as Conjecture 1.1**. They explicitly reported that the pair was not settled by their available Magma method. Their \(\mathbb F_7\) equivalence for a different pair is prior art and not part of the new statement.

Hussain, Luo, Yau, Zhang and Zuo (*Communications in Analysis and Geometry*, 28 (2020), 263–319) revisit low-dimensional toric code classification while concentrating on dimension seven. Their Theorem 1.2 concerns dimension-seven pairs, not the explicit dimension-six transformation proved here. Their general introductory remark that dimension-six codes were classified is not an explicit matrix or statement settling Conjecture 1.1 of the 2015 paper. The new proof supplies exactly that missing direct equivalence certificate.

## Limitations

The result settles precisely the named \(\mathbb F_8\) equivalence and, by combination with the 2015 classification, the sole ambiguity there. It does not settle the new dimension-seven equivalence questions raised in the 2020 paper, and does not assert the same equivalence for other fields. The historical priority claim is qualified by the literature inspected; the elementary involution could potentially have been noticed in an unlocated source. Independent scientific audit has not been performed.

## References

1. X. Luo, S. S.-T. Yau, M. Zhang, and H. Zuo, *On classification of toric surface codes of low dimension*, arXiv:1402.0060, first version 2014-02-01; see Theorem 1.2, Conjecture 1.1 and Figure 1.4. https://arxiv.org/abs/1402.0060 .
2. The same authors, *On classification of toric surface codes of low dimension*, *Finite Fields and Their Applications* **33** (2015), 90–102, DOI:10.1016/j.ffa.2014.11.007; Figure 1, Theorem 1.2, Conjecture 1.1. https://archive.ymsc.tsinghua.edu.cn/pacm_download/89/4646-On_classification_of_toric_surface_codes_of_low_dimension.pdf .
3. N. Hussain, X. Luo, S. S.-T. Yau, M. Zhang, and H. Zuo, *On classification of toric surface codes of dimension seven*, *Communications in Analysis and Geometry* **28** (2020), 263–319; Sections 1 and 3 and Theorem 1.2. https://intlpress.com/site/pub/files/_fulltext/journals/cag/2020/0028/0002/CAG-2020-0028-0002-a003.pdf .
