# Göpel and Rosenhain tetrad counts determine their joint zeta functions over finite fields

## Finding

Let \(C/\mathbb F_q\) be a smooth geometrically connected genus-two curve over any finite field of **odd** cardinality \(q\). On the singular Jacobian Kummer quartic \(K=\operatorname{Jac}(C)/\{\pm1\}\), let \(G_C\) and \(R_C\) denote the reduced finite étale schemes parametrizing, respectively, its \(60\) Göpel and \(80\) Rosenhain tetrads of nodes. Set \(g_n=\#G_C(\mathbb F_{q^n})\) and \(r_n=\#R_C(\mathbb F_{q^n})\).

**The ordered pair \((g_1,r_1)\) uniquely determines both complete zeta functions \(Z(G_C,T)\) and \(Z(R_C,T)\)**, including all extension-field point counts. Among the \(11\) partitions of six describing Frobenius on the six geometric Weierstrass points, there are exactly \(10\) distinct combined tetrad spectra and exactly \(10\) distinct base-field pairs. The only collision is the branch-partition pair \((1,1,4)\) versus \((2,4)\): both yield Göpel cycle decomposition \(1^2 2^3 4^{13}\) and Rosenhain decomposition \(2^4 4^{18}\). Consequently both tetrad parameter schemes, separately, are isomorphic over the respective finite field. These two branch types occur over **every odd finite field**, so the ambiguity is arithmetic, not just formal group theory.

The complete eleven-type classification is:

| Branch Frobenius partition | Göpel cycles | Rosenhain cycles | \((g_1,r_1)\) |
|:--|:--|:--|:--|
| \((1,1,1,1,1,1)\) | \(1^{60}\) | \(1^{80}\) | \((60,80)\) |
| \((1,1,1,1,2)\) | \(1^{12}2^{24}\) | \(1^{24}2^{28}\) | \((12,24)\) |
| \((1,1,1,3)\) | \(3^{20}\) | \(1^5 3^{25}\) | \((0,5)\) |
| \((1,1,2,2)\) | \(1^8 2^{26}\) | \(1^8 2^{36}\) | \((8,8)\) |
| \((1,1,4)\) | \(1^2 2^3 4^{13}\) | \(2^4 4^{18}\) | \((2,0)\) |
| \((1,2,3)\) | \(3^4 6^8\) | \(1^3 2^1 3^7 6^9\) | \((0,3)\) |
| \((1,5)\) | \(5^{12}\) | \(5^{16}\) | \((0,0)\) |
| \((2,2,2)\) | \(1^{16}2^{22}\) | \(2^{40}\) | \((16,0)\) |
| \((2,4)\) | \(1^2 2^3 4^{13}\) | \(2^4 4^{18}\) | \((2,0)\) |
| \((3,3)\) | \(1^3 3^{19}\) | \(1^2 3^{26}\) | \((3,2)\) |
| \((6)\) | \(1^1 2^1 3^5 6^7\) | \(2^1 6^{13}\) | \((1,0)\) |

Here a cycle monomial \(1^{a_1}2^{a_2}\cdots\) means that the finite étale parameter scheme consists of \(a_d\) Frobenius orbits of length \(d\). Thus each row supplies the exact zeta functions
\[
Z(G_C,T)=\prod_{d\ge1}(1-T^d)^{-a_d},\qquad
Z(R_C,T)=\prod_{d\ge1}(1-T^d)^{-b_d},
\]
where \(a_d,b_d\) are the row's respective cycle multiplicities.

The pair \((1,1,2,2)\) versus \((2,2,2)\) also gives a noteworthy distinction: these two types have identical complete *individual node and trope* Frobenius spectra, but their tetrad counts are \((8,8)\) and \((16,0)\), respectively.

## Assumptions and scope

The Weierstrass branch divisor of a smooth genus-two curve in odd characteristic is finite étale of degree six, even if the curve is described using a quintic polynomial with the point at infinity among the branch points. The associated geometric two-torsion vector space \(V=\operatorname{Jac}(C)[2](\overline{\mathbb F}_q)\) has dimension four over \(\mathbb F_2\), with its nondegenerate Weil pairing. A Göpel (respectively Rosenhain) tetrad is an affine translate of a two-dimensional totally isotropic (respectively non-isotropic) subspace of \(V\). Both types are intrinsically defined from the Kummer node–trope configuration and are stable under arithmetic Frobenius. No rational Weierstrass point, marking, or rational theta structure is assumed.

For a permutation of the six branch points, define the abstract \(V\) as even-cardinality subsets modulo complement, with addition by symmetric difference and \(\langle S,U\rangle=\#(S\cap U)\bmod2\). The two-dimensional affine planes in this space are the two geometric classes of tetrads. A branch permutation determines a Frobenius action on this configuration. The theorem makes no claim that an arbitrary prescribed six-point splitting partition is attained over each *fixed* small field, except the specified collision, whose realizability is proved below.

## Proof

**1. Symplectic identification and counts.** The classical hyperelliptic description identifies \(V\) with even subsets of the six geometric branch points modulo complement, equivariantly for Frobenius. The intersection parity defines the Weil form. There are \(\binom{15}{2}/3=35\) two-dimensional vector subspaces of \(V\): choosing a pair of distinct nonzero vectors counts every subspace exactly three times. Exactly \(15\) of these are totally isotropic (for each nonzero \(u\), there are \(6\) choices of \(v\notin\{0,u\}\) perpendicular to it, and each isotropic plane is counted by \(6\) ordered bases). The other \(20\) are non-isotropic. Every two-dimensional subspace has four cosets; hence exactly \(60\) Göpel and \(80\) Rosenhain tetrads.

**2. General fixed-tetrad formula.** Let \(A\) be any symplectic linear endomorphism of \(V\), here the Frobenius permutation on even-subset classes. An affine plane \(x+H\) is fixed by \(A\) if and only if \(AH=H\) and \((A-I)x\in H\). For each invariant \(H\), the fixed cosets form the kernel of \(A-I\) acting on \(V/H\); their exact number is therefore
\[
\#\ker\bigl(A-I:V/H\longrightarrow V/H\bigr).
\]
Summing over invariant isotropic (respectively non-isotropic) \(H\) gives the two fixed-tetrad counts. Replacing \(A\) by \(A^n\) gives every extension-field count; the formula is valid without any assumption on \(q\) beyond odd characteristic or on the order of Frobenius.

**3. Exact finite classification.** Partitioning the six labels according to their permutation cycles gives precisely \(11\) classes in \(S_6\). For each partition, apply the explicit even-subset action to all \(35\) directions and their cosets. The exact exhaustive classification gives the eleven rows displayed above. The included independent verifier `verify_tetrads.py` separately constructs all affine planes as four-element subsets, testing the vanishing of their sum in \(V\); it agrees with the direction/coset construction on the actual sets of \(60\) and \(80\). It then computes their entire orbit decompositions for **all \(720\) permutations**, verifying conjugacy-class invariance. For each of the eleven classes it independently checks fixed-coset counts using the quotient-space formula. The source code contains no external package dependency and the full table is reproduced in `tetrad_spectra.csv`. Since this is an exhaustive finite computation with explicit membership criteria, it is a complete certificate for the eleven permutation cases, not a sampling of finite fields.

**4. Reconstruction and unique ambiguity.** Direct comparison of the eleven exact ordered base-field count pairs finds precisely one repetition: \((2,0)\) for \((1,1,4)\) and \((2,4)\). Inspection of the exact full cycle decompositions for those two rows shows equality of both, while the remaining nine pairs have different counts. Hence the base-field pair determines the pair of complete spectra, even when it does not uniquely identify the six-point splitting partition. Over a finite field a finite étale scheme is classified up to isomorphism by its multiset of Frobenius orbit lengths, so the collision is equality of isomorphism types of the respective parameter schemes, not merely equality of point counts at finitely many extensions.

**5. Realizability of the collision over every odd finite field.** Every finite field admits monic irreducible polynomials of degrees two and four. Let \(h_2,h_4\) be such polynomials over \(\mathbb F_q\), and choose distinct \(a,b\in\mathbb F_q\), possible because \(q\ge3\). Then the squarefree separable genus-two equations
\[
y^2=(x-a)(x-b)h_4(x),\qquad y^2=h_2(x)h_4(x)
\]
have branch splitting \((1,1,4)\) and \((2,4)\), respectively. Thus both arithmetic types exist for every odd \(q\). There is no assertion these two curves are isomorphic or have the same Hasse–Weil curve zeta function.

**6. Comparison with nodes and tropes.** The sixteen nodes are indexed by \(V\); the sixteen tropes by theta characteristics, consisting of the six odd singleton branch labels and the ten even complementary three-element subsets. Using those actions, the branch types \((1,1,2,2)\) and \((2,2,2)\) have identical complete node and trope orbit decompositions. The Göpel/Rosenhain base-field counts distinguish them: \((8,8)\) against \((16,0)\). The verifier independently implements the node and trope actions to confirm this comparison, which illustrates additional arithmetic information present in the tetrad schemes.

## Verification

Run `python3 verify_tetrads.py tetrad_spectra.csv` with a standard Python 3 interpreter; the program regenerates the CSV from first principles. It checks the \(16\)-node quotient structure, \(35\) directions, both counts of tetrads, full agreement between independent geometric enumerations, stability under all \(720\) branch-label permutations, equality of the stable-plane formula and direct fixed-tetrad counts, all \(11\) orbit spectra, the uniqueness of the \((1,1,4)/(2,4)\) collision, and the node/trope comparison. Its final success marker begins `VERIFIED: 16 nodes, 35 planes, 60 Goepel and 80 Rosenhain tetrads`. The supplied CSV is an exact reproducible derived table, not a database assumed to contain correct results.

## Relationship to prior work

The sixteen Kummer nodes, Göpel and Rosenhain tetrad definitions, the geometric counts \(60\) and \(80\), and their interpretation as isotropic/non-isotropic affine planes are classical, explicitly discussed by Keum (1997, Section 2) and Dolgachev (2023 preprint, Section 5). He (2024, Section 2.4.1) also describes the Göpel node configurations and their geometric constructions. These geometric facts are **not** claimed as new. A published study of the integral \(16\)-by-\(60\) Göpel incidence lattice gives its Smith form and membership congruences but does not classify Frobenius orbits or the Rosenhain scheme. Prior arithmetic classifications of the fifteen rational Richelot kernels and of the ninety-six Kummer node–trope incidence flags study different finite étale schemes and do not state the present pair of tetrad schemes' one-extension reconstruction or unique collision. This finding is specifically the exact joint **arithmetic Frobenius classification** of the two Kummer tetrad schemes and the sharp first-extension observation.

## Limitations

The theorem concerns finite étale **tetrad parameter schemes** of the singular genus-two Jacobian Kummer quartic, not the zeta function of the full Kummer surface, nor its resolved K3 surface, the Jacobian's Weil polynomial, or rational parameters for all individual geometric tetrads. The base-field pair cannot distinguish \((1,1,4)\) from \((2,4)\), even with all extension counts. The table is exhaustive for the abstract \(S_6\)-actions, not a weighted census of curves over a fixed field. The independent evaluation of mathematical priority has not been performed; an identical result may exist in older finite-geometry permutation-character tables not identified by the searches.

## References

1. J. H. Keum, *Automorphisms of Jacobian Kummer surfaces*, Compositio Mathematica (1997), Section 2, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/99E3B77D5A4D01C1F0A5F419204EDDC5/S0010437X97000419a.pdf/automorphisms_of_jacobian_kummer_surfaces.pdf .
2. I. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, arXiv:2302.13101, v1 first public 2023-02-25, Section 5, https://arxiv.org/abs/2302.13101 ; full journal version https://doi.org/10.1112/blms.13033 .
3. Z. He, *Pseudo-automorphisms of rational threefolds and Kummer surfaces*, arXiv:2401.07948, Section 2.4.1, https://arxiv.org/abs/2401.07948 .
4. *The integral Göpel-tetrad lattice of a Kummer quartic*, published-finding corpus public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-integral-g-pel-tetrad-lattice-of-a-kummer-quartic--2fe9c0537bec .
