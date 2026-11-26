# Four arithmetic classes of minimum-degree smooth filling curves on \(\mathbb P^1\times\mathbb P^1\) over \(\mathbb F_2\)

## Finding

Let \(S=\mathbb P^1_{\mathbb F_2}\times\mathbb P^1_{\mathbb F_2}\). There are exactly **66** distinct geometrically smooth divisors \(C\) of bidegree \((4,3)\) satisfying \(C(\mathbb F_2)=S(\mathbb F_2)\). Under the order-36 group \(\operatorname{PGL}_2(\mathbb F_2)^2\), acting independently on the two rulings, these form exactly **four** orbits of sizes \(6,18,36,6\). Their respective stabilizers in this group are \(C_6,C_2,\{1\},S_3\).

They have **four distinct Hasse–Weil numerators** over \(\mathbb F_2\). Their genus-six Jacobians are therefore pairwise nonisogenous over \(\mathbb F_2\). The four classes are represented by the coefficient masks and extension-field point counts below; every entry is exactly reproducible by the accompanying scripts.

| Coefficient mask | Orbit size | Ruling-preserving stabilizer | \((N_1,N_2,N_3,N_4,N_5,N_6)\) | \((c_1,c_2,c_3,c_4,c_5,c_6)\) |
| ---: | ---: | :--- | :--- | :--- |
| `396246` | 6 | \(C_6\) | \((9,9,9,9,69,51)\) | \((6,20,48,90,144,211)\) |
| `399606` | 18 | \(C_2\) | \((9,9,9,21,39,39)\) | \((6,20,48,93,156,233)\) |
| `404886` | 36 | trivial | \((9,9,12,17,24,78)\) | \((6,20,49,98,167,250)\) |
| `420790` | 6 | \(S_3\) | \((9,11,9,23,9,53)\) | \((6,21,54,114,204,313)\) |

Here \(N_n=\#C(\mathbb F_{2^n})\) and \(L_C(T)=\sum_{i=0}^{12}c_iT^i\), with \(c_0=1\) and \(c_{12-i}=2^{6-i}c_i\) for \(0\le i\le5\). Thus the table uniquely specifies all four degree-12 numerators.

The unique opposite bidegree \((3,4)\) version is obtained by interchanging the factors. Consequently there are also 66 such smooth curves of bidegree \((3,4)\), and four orbits when both bidegrees are considered under the full automorphism group of \(S\).

## Assumptions and scope

Everything is over \(\mathbb F_2\). Coordinates are \(([X_0:X_1],[Y_0:Y_1])\) on \(S\). For \(0\le i\le4\) and \(0\le j\le3\), let

\[
M_{i,j}=X_0^{4-i}X_1^iY_0^{3-j}Y_1^j.
\]

Any bidegree-\((4,3)\) equation is \(F=\sum_{i,j}a_{i,j}M_{i,j}\), with \(a_{i,j}\in\mathbb F_2\). Its **coefficient mask** is the integer \(m(F)=\sum_{i,j}a_{i,j}2^{4i+j}\). This convention is part of the theorem and the verifier, not an unspecified encoding. Distinct nonzero forms give distinct divisors, because \(\mathbb F_2^\times\) is trivial. Smooth means smooth **over an algebraic closure**, not merely at the nine rational points.

The bidegrees are ordered: the first factor has degree four and the second degree three. Projective orbit equivalence means equivalence by automorphisms preserving both rulings. No assertion is made about the full abstract automorphism groups of the curves.

## Proof

**1. Exhaustive parameter space.** There are \(5\cdot4=20\) monomials \(M_{i,j}\). The condition that their linear combination vanish at every one of the \(3\cdot3=9\) rational points is a linear system of rank nine: row reduction of the explicit nine-by-twenty evaluation matrix produces eleven free columns. Therefore precisely \(2^{11}=2048\) sections, including zero, vanish at all nine points. With the mask convention above, a binary basis of the kernel is `6,96,272,544,1056,2176,4112,8224,16416,32896,393216`. The first verifier recomputes the entire evaluation matrix and a basis of the kernel, independently verifying every row against every section. This is all possible equations, with no sampling.

**2. All projective-equivalence orbits.** Each ruling has \(\operatorname{PGL}_2(\mathbb F_2)\cong S_3\), of order six. For every one of the 36 ordered pairs of invertible binary two-by-two matrices, explicit polynomial substitution yields a linear action on all twenty coefficients. Applying all 36 transformations to each of the 2047 nonzero filling forms partitions them into exactly 99 disjoint orbits. The complete orbit-size histogram (size:count) is `1:1, 3:6, 6:12, 9:8, 12:4, 18:34, 36:34`, whose weighted sum is 2047. The group action preserves the nine-point vanishing condition and geometric smoothness.

**3. Geometric smoothness.** On each of the four standard affine charts \(X_a\ne0\), \(Y_b\ne0\), put the nonzero homogeneous coordinates equal to one and denote the two remaining affine coordinates by \(u,v\). If \(f_{a,b}(u,v)\) is the dehomogenized equation, the curve is smooth on this chart over \(\overline{\mathbb F}_2\) precisely when

\[
(f_{a,b},\partial_u f_{a,b},\partial_v f_{a,b})=(1)
\quad\text{in }\mathbb F_2[u,v].
\]

The equivalence is the Jacobian criterion and the Nullstellensatz: the ideal has no common zero over the algebraic closure if and only if it contains one. For each of the 99 orbit representatives, the first verifier computes an exact Gröbner basis in all four charts, using graded reverse-lexicographic order. Only the four mask representatives in the table have the unit ideal in every chart. Their orbit sizes add up to \(6+18+36+6=66\); the other 95 orbits have a singularity over the algebraic closure.

As an independent check of the census, a second verifier constructs all \(2^{20}\) binary coefficient vectors, filters the nine rational-point equations directly, and tests **all 2047 nonzero filling forms** (without orbit reduction) using lexicographic Gröbner elimination with the variables reversed. It finds exactly 66 smooth forms, including the four representatives. Hence no orbit has been lost through a symmetry reduction.

**4. Geometric irreducibility, genus, and stabilizers.** A smooth effective divisor of bidegree \((4,3)\) on \(\mathbb P^1\times\mathbb P^1\) is geometrically irreducible: any decomposition into two nonzero effective parts of total bidegree \((4,3)\) forces positive intersection between some components from different parts, contradicting smoothness. Adjunction gives

\[
g=(4-1)(3-1)=6.
\]

The 36-element transformation table gives stabilizer orders \(6,2,1,6\). The element-order histograms are respectively \((1:1,2:1,3:2,6:2)\), \((1:1,2:1)\), \((1:1)\), and \((1:1,2:3,3:2)\). They distinguish cyclic \(C_6\) from nonabelian \(S_3\) in the two order-six cases.

**5. Arithmetic distinction.** For each representative, enumerate the \((2^n+1)^2\) pairs of points of \(\mathbb P^1(\mathbb F_{2^n})^2\) for \(1\le n\le6\), evaluating its bihomogeneous form with exact finite-field multiplication. The first verifier uses irreducible binary polynomials of degrees one through six given by integers \((3,7,11,19,37,67)\); the second independently uses \((3,7,13,25,41,73)\). The two programs agree on every \(N_n\) in the table.

The coefficients are then reconstructed from

\[
nc_n=\sum_{i=1}^n\bigl(N_i-(1+2^i)\bigr)c_{n-i}\qquad(1\le n\le6),
\]

and the genus-six functional equation \(c_{12-i}=2^{6-i}c_i\). Because the four six-tuples of coefficients differ, their Weil polynomials differ. Tate's isogeny theorem therefore implies that the four Jacobians are pairwise nonisogenous over \(\mathbb F_2\). This completes the classification and arithmetic distinction.

## Verification

The package includes two complete, self-contained Python programs requiring only Python and SymPy. They implement exact binary linear algebra, projective substitutions, Jacobian-ideal Gröbner tests, and finite-field counting. Run:

```text
python verify_filling_43_orbits.py
python verify_filling_43_independent.py
```

Their successful terminal markers are:

```text
BIDEGREE43_FILLING_PASS 2048 99 66 4
BIDEGREE43_INDEPENDENT_PASS 2048 66 4
```

The first program additionally verifies that the explicit example constructed by Homma and Kim has mask `429846` and belongs to the orbit represented by `399606` (size 18). The second program is independent of the first and does not import its enumeration or polynomial-arithmetic routines. Both are exact finite computations, not evidence for claims about other fields or degrees.

## Relationship to prior work

Homma and Kim, *Filling curves for \(\mathbb P^1\times\mathbb P^1\)* (arXiv:2203.11595, initial version March 22, 2022), proved that bidegrees \((4,3)\) and \((3,4)\) are minimum for irreducible filling curves over \(\mathbb F_2\) and constructed one geometrically smooth example; their Section 4 supplies an explicit equation. The present classification includes that example in the size-18 orbit, but goes further by classifying **all** smooth forms, their four ambient orbits, stabilizers and full Weil numerators. Thus the minimum-degree bound and existence statement are prior results, not part of the claimed novelty.

Ahammed, Campbell and Moon, *Minimal algebraic space filling curves on the product of projective lines* (arXiv:2512.02796, December 2025), study the corresponding form and smoothness criteria, proving results for odd field sizes and giving computational statistics for \(q=3,5\). Their inspected sections do not enumerate or classify the exceptional \(q=2\), bidegree-\((4,3)\) smooth locus. Asgarli and Ghioca (arXiv:2307.03072) study plane-filling curves in \(\mathbb P^2\), a different ambient surface and bidegree problem.

## Limitations

The theorem is confined to geometrically smooth divisors of bidegree \((4,3)\) on the **split** quadric surface over \(\mathbb F_2\) and its factor-swapped version. Ruling-preserving stabilizers need not equal abstract curve automorphism groups. Pairwise nonisogenous refers to Jacobians over \(\mathbb F_2\), not after base extension. Exact Gröbner and point-count computation is essential to the exhaustive classification; the scripts supply the full reproducible finite proof, but no independent external audit has been performed. A previously unindexed equivalent enumeration remains a priority risk.

## References

1. M. Homma and S. J. Kim, *Filling curves for \(\mathbb P^1\times\mathbb P^1\)*, arXiv:2203.11595, first publicly posted March 22, 2022, Section 4 and Lemma 2.1. https://arxiv.org/abs/2203.11595
2. M. Ahammed, M. Campbell and H.-B. Moon, *Minimal algebraic space filling curves on the product of projective lines*, arXiv:2512.02796, December 2025, Sections 3–5. https://arxiv.org/abs/2512.02796
3. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072, July 2023. https://arxiv.org/abs/2307.03072
