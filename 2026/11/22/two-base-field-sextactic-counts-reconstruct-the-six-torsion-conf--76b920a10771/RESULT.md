# Two base-field sextactic counts reconstruct the six-torsion configuration zeta functions of a plane cubic

## Finding
Let \(C\subset\mathbb P^2_{\mathbb F_q}\) be a smooth plane cubic in characteristic at least five **with a rational flex**. Let \(S\) be the finite étale scheme of its 27 geometric sextactic points (points of genuine conic contact six, excluding flexes), \(L\) the 81 geometric lines incident with three distinct points of \(S\), and \(K\) the 8,244 geometric conics incident with six distinct points of \(S\). Write \(K_{\mathrm{red}}\) and \(K_{\mathrm{sm}}\) for the 2,268 geometrically reducible and 5,976 geometrically smooth members of \(K\).

**Theorem.** The known residue \(q\bmod3\), together with just the two base-field integers
\[
 s=\#S(\mathbb F_q),\qquad c=\#K(\mathbb F_q),
\]
uniquely determines the complete Frobenius cycle decompositions, hence the zeta functions and all finite-extension point counts, of each of \(S,L,K,K_{\mathrm{red}},K_{\mathrm{sm}}\). The 24 conjugacy-class pairs of \(\mathrm{GL}_2(\mathbb F_2)\times\mathrm{GL}_2(\mathbb F_3)\) give precisely 19 distinct joint spectra, all distinguished by \((q\bmod3,s,c)\). These 19 are group-theoretic spectra; it is not asserted that every class arises for a fixed field.

The complete lookup table and cycle decompositions for all 24 class pairs, including the collisions of classes with identical joint spectra, are supplied in `class_table.csv`. For example, at determinant \(2\) and counts \((s,c)=(3,76)\), the entire scheme \(K\) has Frobenius cycles \(1^{76}2^{4084}\), with \(54\) rational geometrically reducible conics and \(22\) rational geometrically smooth conics. A single count of \(s\) or \(c\) alone does not distinguish every joint spectrum.

## Assumptions and scope
The ground field is finite of characteristic at least five. The plane cubic is geometrically smooth and has a flex defined over the ground field. Fixing that flex as identity identifies its plane hyperplane class with three times the origin; this is a mathematical assumption, not an assertion that every plane cubic has a rational flex. All finite configuration schemes count **geometric objects defined over the indicated field**; a rational conic may contain no individually rational sextactic points. Geometric smoothness of a conic is distinguished from having a smooth rational equation.

## Proof
1. Let the chosen flex be \(O\), and let \(E=(C,O)\). Under the plane embedding, the hyperplane divisor has class \(3O\). A point supports a conic meeting \(C\) with divisor \(6P\) exactly when \(6(P-O)=0\); the nine flexes are \(E[3]\). Since the characteristic is prime to six, the reduced genuine sextactic set is
\[
S=E[6]\setminus E[3]\simeq\{(u,v)\in\mathbb F_2^2\times\mathbb F_3^2:u\ne0\}.
\]
It has \(3\cdot9=27\) points. Abel's divisor criterion gives: a triple of distinct points in \(S\) lies on a line exactly when its sum in \(E[6]\) is zero; a six-element subset lies on a unique conic exactly when its sum is zero. Each such conic is reduced: it intersects the smooth cubic in six distinct points. It is geometrically reducible precisely when those six points split into two disjoint zero-sum triples, in which case it is the union of their two lines. This establishes canonical, Galois-equivariant identifications of all five finite sets with subsets of the torsion group.

2. Enumerate the \(27\) vectors with nonzero \(\mathbb F_2^2\) coordinate. The standalone exact enumeration visits all \(\binom{27}{3}\) and \(\binom{27}{6}\) subsets and tests coordinate sums modulo two and three, giving exactly \(81\) lines and \(8244\) conics. Independently constructing all unordered disjoint pairs of the \(81\) lines yields \(2268\) distinct six-subsets, all in the conic set, leaving \(5976\) geometrically smooth conics. These are **exhaustive finite-set counts** following the divisor criterion, not statistical tests.

3. Arithmetic Frobenius on \(E[6]\) splits by the Chinese remainder theorem as a pair \((A,B)\in\mathrm{GL}_2(\mathbb F_2)\times\mathrm{GL}_2(\mathbb F_3)\). The Weil pairing forces \(\det(B)\equiv q\pmod3\). In dimension two, \(\mathrm{Sp}_2(\mathbb F_2)=\mathrm{GL}_2(\mathbb F_2)\), so there is no further determinant constraint modulo two. The two groups have orders six and 48, and exactly three and eight conjugacy classes, respectively. Conjugation preserves all induced permutation cycle decompositions; hence all possible arithmetic cases reduce to 24 class-representative pairs, with no unexamined infinite family.

4. For each of the 24 pairs, compute the induced permutations on the five enumerated sets, form their full cycle decompositions, and compare the key \((\det B,\#\mathrm{Fix}_S,\#\mathrm{Fix}_K)\). The `checker.py` algorithm tests all classes and verifies that each key is associated with exactly one full five-scheme cycle spectrum; it finds 19 keys and 19 full spectra. The table contains actual representative matrices, determinant, class sizes, all five cycle decompositions, and first and second extension counts. Because every actual arithmetic Frobenius belongs to exactly one conjugacy class in each factor, the finite exhaustive classification proves the universal reconstruction assertion.

The resulting distinct base-field keys are listed here; the complete orbit decompositions and the five configurations' first-extension counts are in `class_table.csv`.

| \(\det B\) | Distinct \((s,c)\) pairs |
|---|---|
| \(1\) | \((0,0),(0,4),(0,36),(1,0),(1,4),(1,148),(3,0),(3,4),(3,6),(3,220),(9,54),(9,156),(27,8244)\) |
| \(2\) | \((0,0),(0,6),(1,0),(3,0),(3,76),(9,228)\) |

5. If the Frobenius cycles on a finite scheme \(X\) are \(a_d\) cycles of length \(d\), then
\[
\#X(\mathbb F_{q^n})=\sum_{d\mid n}d\,a_d,\qquad
Z(X,T)=\prod_d(1-T^d)^{-a_d}.
\]
Therefore the lookup reconstructs all the claimed zeta functions over all positive extension degrees, not only the first two degrees.

## Verification
From a directory containing `checker.py`, run `python3 checker.py class_table.csv`. The standard-library-only checker enumerates all 296,010 six-element subsets, constructs the exact geometric line and conic sets, independently constructs reducibles as unions of disjoint lines, forms all 24 conjugacy-class representatives, computes complete cycle decompositions and asserts injectivity of the indicated base-field key on spectra. Successful output is `UNIVERSAL_SEXTACTIC_24_CLASS_19_SPECTRUM_RECONSTRUCTION_VERIFIED` followed by geometric and class counts. `class_table.csv` is the actual produced certificate, not a hand-compiled sample. Mathematical validity additionally relies on the standard divisor criterion and torsion identifications proved above; running code alone cannot certify those geometric facts.

## Relationship to prior work
Szemberg and Szpond (arXiv:2211.00494, first public 2022-11-01, Sections 2–4) study the Fermat cubic, explicitly construct its 27 sextactic points, and enumerate its 81 trisecants and 8,244 six-secant conics. Their special geometric computations provide the objects and cardinalities, but do not establish the 24-class, general-cubic arithmetic reconstruction from two base-field counts. Banerjee and Chen (arXiv:2101.03824, first public 2021-01-11, Section 6) explain the torsion construction of sextactic points for arbitrary smooth plane cubics; their principal conclusions concern universal multisections and monodromy, not finite-field conic or trisecant Frobenius zeta functions. A separately located public arithmetic result treats the Fermat cubic's conic and trisecant spectra, including the \(5976,0,22\) smooth-conic trichotomy; those specialized spectra are contained in the present group-theoretic framework, but do not imply the full table for arbitrary elliptic plane cubics without the additional conjugacy calculation. No claim of absolute priority against unindexed group-character tables is made.

## Limitations
The theorem assumes a rational flex; for a cubic whose flex torsor has no rational point, Frobenius acts affinely rather than purely linearly on \(E[6]\), and the current table cannot be applied. Characteristic two or three is excluded. The 19 types classify spectra, not elliptic curves up to isomorphism, mod-six Frobenius conjugacy classes, or Weil polynomials. Group-theoretic classes were enumerated completely, but not individually realized as geometric Frobenius for any prescribed finite field. The originality comparison of the relevant specialized public arithmetic record was based on its accessible summary, not on an accessible complete manuscript; a stronger unindexed general result remains possible.

## References
- T. Szemberg and J. Szpond, *Sextactic points on the Fermat cubic curve and arrangements of conics*, arXiv:2211.00494 (2022), https://arxiv.org/abs/2211.00494.
- I. Banerjee and W. Chen, *Choosing points on cubic plane curves: rigidity and flexibility*, arXiv:2101.03824 (2021), https://arxiv.org/abs/2101.03824.
- Classical Abel divisor-sum criterion on plane cubics, as presented in Banerjee–Chen, Section 6.1.
