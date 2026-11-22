# One-field bitangent and conic-bundle reconstruction for seven-point del Pezzo blowups

## Finding

Let \(S\) be the blowup of a Frobenius-stable set of seven geometric points of \(\mathbb P^2\) in general position over an odd finite field. The rational counts of its 28 branch-quartic bitangents and its 126 conic-bundle pencils, taken **only over the base field**, uniquely recover the Frobenius permutation partition on the blown-up points. Consequently, the pair determines the finite-etale zeta functions of both configuration schemes and the surface's Hasse–Weil zeta function. It is essential that the seven-point blowdown be defined over the ground field; the theorem does not classify all unmarked degree-two del Pezzo surfaces.

## Assumptions and scope

Set \(k=\mathbb F_q\) with \(q\) odd. Let \(Z\subset\mathbb P^2_k\) be a reduced closed subscheme of length seven, geometrically in general position (no three collinear and no six on any conic). Write \(S=\operatorname{Bl}_Z\mathbb P^2\). It is a smooth degree-two del Pezzo surface. Its anticanonical map \(S\to\mathbb P^2\) is a separable double cover with smooth quartic branch curve.

The geometric bitangent set \(\mathcal B\) consists of all 28 bitangent lines of that quartic, including hyperflex tangents if present. Let \(\mathcal R\) be the finite set of **numerical fibre classes** of morphisms \(S_{\bar k}\to\mathbb P^1_{\bar k}\) with generic smooth geometrically rational fibre, equivalent to genus-zero nef classes of square zero and anticanonical degree two. Its size is 126. Rationality of a class means Frobenius-invariance. Over a finite field, the complete pencil of an invariant class descends and its genus-zero base is \(\mathbb P^1_k\), so the same number counts rational pencils up to automorphisms of their targets; this does not count different parameterizations of one pencil.

Write \(B_n=\#\mathcal B(\mathbb F_{q^n})\) and \(R_n=\#\mathcal R(\mathbb F_{q^n})\). The theorem concerns \((B_1,R_1)\). Both finite schemes are reduced finite étale schemes by construction as discrete geometric configurations with Galois actions, rather than potentially nonreduced Hilbert schemes in special characteristic.

## Proof

Use the classes \(H,E_1,\ldots,E_7\) after geometric base change, with \(-K_S=3H-\sum_iE_i\), \(H^2=1\), \(E_i^2=-1\), and all other pairings zero. Frobenius fixes \(H\) and permutes the seven \(E_i\) according to its action on \(Z\).

**Bitangents.** The 56 exceptional curves have divisor classes in four disjoint families: \(E_i\) (7), \(H-E_i-E_j\) (21), \(2H-\sum_{m\notin\{i,j\}}E_m\) (21), and \(3H-2E_i-\sum_{m\ne i}E_m\) (7). The Geiser involution pairs each class \(D\) with \(-K_S-D\); the unordered pairs give the 28 geometric bitangents. Thus the bitangent Galois set is equivariantly the disjoint union of the seven singletons and the 21 two-element subsets of the original point set. If \(f,t,u\) count Frobenius cycles of lengths one, two and three, respectively, the number of invariant two-subsets is \(\binom f2+t\). Therefore

\[B_1=f+\binom f2+t.\]

**Conic bundles.** Write a fibre class \(D=aH-\sum_i b_iE_i\). Nefness gives \(b_i=D\cdot E_i\ge0\) and, by intersection with the cubic exceptional class centered doubly at the \(i\)-th point, \(D\cdot(3H-2E_i-\sum_{j\ne i}E_j)=2-b_i\ge0\), hence \(0\le b_i\le2\). The equalities \(D^2=0\) and \((-K_S)\cdot D=2\) become \(a^2=\sum b_i^2\) and \(3a-\sum b_i=2\). They imply \(1\le a\le5\) and yield precisely the following five families, described by the multiplicities of \(0,1,2\) among the seven \(b_i\):

| \(a\) | \((\#0,\#1,\#2)\) | Number of classes | Combinatorial indices |
|---:|:---:|---:|:---|
| 1 | \((6,1,0)\) | 7 | singleton |
| 2 | \((3,4,0)\) | 35 | four-subset |
| 3 | \((1,5,1)\) | 42 | ordered pair of distinct indices |
| 4 | \((0,4,3)\) | 35 | three-subset |
| 5 | \((0,1,6)\) | 7 | singleton |

The list of conic pencils and the existence of their geometric maps follow from the standard seven-point Cremona classification, explicitly displayed as Theorem 4.1 in Ray (2018). Every displayed numerical class intersects all 56 exceptional classes nonnegatively (also directly checked in the attached checker), and the corresponding pencil is basepoint free. Thus the list is exhaustive in odd characteristic.

A fixed three-subset is either three fixed points, a fixed point plus a 2-cycle, or one 3-cycle, contributing \(\binom f3+ft+u\). Fixed ordered pairs of distinct indices contribute \(f(f-1)\). Therefore

\[R_1=2f+2\left(\binom f3+ft+u\right)+f(f-1).\]

**Inversion and arithmetic consequence.** There are exactly 15 partitions \(\lambda\vdash7\). The two expressions above give 15 different ordered pairs, as listed in the exhaustive table below and recomputed independently from the explicit 126 conic classes and 28 bitangent indices. The proof is a finite exhaustive classification, not a sampling of curves. For each \(n\), replacing Frobenius by its \(n\)-th power gives \(B_n\) and \(R_n\) from the recovered partition, proving the finite-étale zeta assertions. On \(\operatorname{Pic}(S_{\bar k})\), Frobenius fixes \(H\) and permutes the seven exceptional basis elements; hence \(\det(1-tF\mid\operatorname{Pic})= (1-t)\prod_{\ell\in\lambda}(1-t^\ell)\). The rational-surface cohomological trace formula yields

\[Z(S,T)=\frac1{(1-T)(1-q^2T)(1-qT)\prod_{\ell\in\lambda}(1-(qT)^\ell)}.\]

**Complete classification (ground-field pair).**

| Frobenius partition | Rational bitangents | Rational conic-bundle classes | Rational blowup points |
|:---|---:|---:|---:|
| \(1+1+1+1+1+1+1\) | 28 | 126 | 7 |
| \(1+1+1+1+1+2\) | 16 | 60 | 5 |
| \(1+1+1+1+3\) | 10 | 30 | 4 |
| \(1+1+1+2+2\) | 8 | 26 | 3 |
| \(1+1+1+4\) | 6 | 14 | 3 |
| \(1+1+2+3\) | 4 | 12 | 2 |
| \(1+1+5\) | 3 | 6 | 2 |
| \(1+2+2+2\) | 4 | 8 | 1 |
| \(1+2+4\) | 2 | 4 | 1 |
| \(1+3+3\) | 1 | 6 | 1 |
| \(1+6\) | 1 | 2 | 1 |
| \(2+2+3\) | 2 | 2 | 0 |
| \(2+5\) | 1 | 0 | 0 |
| \(3+4\) | 0 | 2 | 0 |
| \(7\) | 0 | 0 | 0 |

Neither individual statistic is enough: \(B_1\) alone gives ten different values and \(R_1\) alone eleven, whereas their pair gives fifteen. For instance, \((1,3,3)\) and \((1,6)\) have a common bitangent count one but ruling counts six and two. Similarly, \((3,4)\) and \((7)\) both have zero rational bitangents but ruling counts two and zero.

## Verification

Run `python3 checker.py classification.csv` using Python 3 standard library only. The program directly constructs all 56 exceptional-curve classes, all 126 nef conic-bundle classes and the 28 Geiser-paired bitangent indices. It verifies intersection inequalities, compares direct fixed-class enumeration with both closed counting formulas for all 15 cycle partitions and for the first 21 powers, checks uniqueness of the fifteen ordered pairs, and regenerates the CSV. This checks the finite calculation; the geometric identification and descent arguments are mathematical arguments above and do not follow from the computation alone.

## Relationship to prior work

Ray, *Geometry of \(\mathbb P^2\) blown up at seven points* (arXiv:1805.04064, 2018), Theorem 4.1, lists all five geometric conic-bundle families, and Section 6 lists the 56 exceptional curves. The numerical \(126\) and the orbit decomposition are applications of these known geometric classes, not claimed as new. Bergvall, *Frobenius actions on Del Pezzo surfaces of degree 2* (arXiv:2211.12855, 2022), counts surfaces realizing specified Weyl-group Frobenius classes, rather than reconstructing a specified seven-point cycle partition from bitangent and conic-pencil counts. Bergvall's *Arithmetic and topology of classical structures associated to plane quartics* (arXiv:2106.13072, 2021) studies quartic structures and finite-field arithmetic, but not this joint reconstruction statistic. Gugiatti–Rota (arXiv:2205.00553, 2022) analyzes exceptional curves and special Eckardt configurations. The assessed increment is the one-base-field simultaneous invariant and its exact arithmetic inversion, not the classical seven-point geometry or the full Weyl-group classification.

## Limitations

The theorem applies to surfaces equipped with a ground-field blowdown to a reduced general-position septuple, i.e. to the permutation subgroup arising from the specified seven points. It does **not** assert that the same two counts distinguish all \(W(E_7)\) Frobenius classes or that every partition occurs over every small field. Geometric conic-bundle classes are counted, not rational conic fibres or the number of possible parameterizations of a pencil. The proof does not reconstruct the isomorphism class of \(S\), the quartic, or the moduli coordinates. Literature searches and primary-text checks do not eliminate all risk of an implicit older permutation-character identity.

## References

1. N. Ray, *Geometry of \(\mathbb P^2\) blown up at seven points*, first arXiv posting 10 May 2018, https://arxiv.org/abs/1805.04064, especially Theorem 4.1 and Section 6.
2. O. Bergvall, *Frobenius actions on Del Pezzo surfaces of degree 2*, first arXiv posting 23 November 2022, https://arxiv.org/abs/2211.12855, especially Sections 1–4.
3. O. Bergvall, *Arithmetic and topology of classical structures associated to plane quartics*, first arXiv posting 24 June 2021, https://arxiv.org/abs/2106.13072, especially Sections 1–2.
4. G. Gugiatti and F. Rota, *Full exceptional collections for anticanonical log del Pezzo surfaces*, first arXiv posting 1 May 2022, https://arxiv.org/abs/2205.00553, especially Section 4.4.
