# Ten Frobenius splitting types of the 165 Eckardt points on binary Frobenius cubic threefolds

## Finding
Let \(A=(a_{ij})\) range over all invertible \(5\times5\) matrices with coefficients in \(\mathbb F_2\), and let
\[
X_A:\quad F_A(x)=\sum_{i,j=0}^{4}a_{ij}x_i^2x_j=0
\subset\mathbb P^4_{\mathbb F_2}.
\]
Every \(X_A\) is geometrically smooth. Its finite geometric scheme of *Eckardt points* (also called tangent-cone centers or star points) has 165 distinct points. The action of arithmetic Frobenius on these points has **exactly ten possible cycle types**, as follows. In the table, an entry \(d^e\) means \(e\) cycles of length \(d\). The matrix code is \(\sum_{i,j}a_{ij}2^{5i+j}\) in row-major order, and the equation-orbit size is the number of distinct equations in the indicated \(\operatorname{GL}_5(\mathbb F_2)\)-congruence class.

| Matrix code | Equation orbit size | Frobenius cycles on Eckardt points |
|---:|---:|---|
| `1118480` | 13,888 | \(1^{15}2^{75}\) |
| `1118482` | 208,320 | \(1^3 2^1 4^{40}\) |
| `1118484` | 104,160 | \(1^7 2^3 4^6 8^{16}\) |
| `1118485` | 104,160 | \(1^7 2^3 4^6 8^{16}\) |
| `1118486` | 624,960 | \(1^3 2^5 4^6 8^{16}\) |
| `1118616` | 1,249,920 | \(1^1 4^1 8^4 16^8\) |
| `1118680` | 1,249,920 | \(1^1 4^1 8^4 16^8\) |
| `1118744` | 555,520 | \(2^3 3^5 6^{24}\) |
| `1118745` | 1,666,560 | \(2^1 3^1 4^1 12^{13}\) |
| `1122448` | 555,520 | \(1^3 2^3 3^4 6^{24}\) |
| `1122450` | 833,280 | \(1^1 3^2 6^1 8^1 12^2 24^5\) |
| `1122451` | 833,280 | \(1^1 3^2 6^1 8^1 12^2 24^5\) |
| `1122820` | 1,999,872 | \(5^3 10^{15}\) |

The orbit sizes total 9,999,360, the full number of invertible binary \(5\times5\) matrices. Consequently the displayed list is exhaustive, and precisely ten distinct cycle multisets occur. For instance, the class `1122820` has no Eckardt point over extensions of degree below five, has fifteen over \(\mathbb F_{32}\), and has all 165 over \(\mathbb F_{1024}\). The classes `1122450` and `1122451` first split all their Eckardt points over degree 24. More generally, if the row associated to \(A\) has \(n_d\) cycles of length \(d\), then for every positive integer \(m\),
\[
\#\mathrm{Eck}(X_A)(\mathbb F_{2^m})
=\sum_{d\mid m}d n_d,
\qquad
Z(\mathrm{Eck}(X_A)/\mathbb F_2,T)=\prod_d(1-T^d)^{-n_d}.
\]
This is an arithmetic classification of a distinguished finite geometric locus, **not** a new classification of the thirteen projective-equivalence classes of cubic threefolds.

## Assumptions and scope
The ground field is exactly \(\mathbb F_2\). The terminology "Eckardt point" means a smooth geometric point \([v]\in X_A\) whose embedded tangent hyperplane section is a cubic cone with vertex \([v]\) over a smooth plane cubic. All geometric points are considered over an algebraic closure, and extension degrees are measured over \(\mathbb F_2\). A matrix code specifies a coefficient-marked cubic; the thirteen code representatives and their congruence orbit sizes occur in the prior complete rational Fano-line classification cited below and are independently re-enumerated by the accompanying orbit checker. No equivalence between distinct rows is asserted; rows with identical cycles remain different rational projective classes.

## Proof
**Smoothness and cone centers.** The derivative vector of \(F_A\) is \(A^{\mathsf T}x^{[2]}\), so it has no projective zero over the algebraic closure exactly when \(A\) is invertible. Let \(v\) be a geometric point on \(X_A\), write \(\beta(u,w)=u^{[2]\mathsf T}Aw\), and expand
\[
F_A(v+t w)=F_A(v)+t\,\beta(v,w)
+t^2\,\beta(w,v)+t^3 F_A(w).
\]
The tangent hyperplane is \(H_v=\{w:\beta(v,w)=0\}\). The restriction is a cone with vertex \([v]\) precisely when \(\beta(w,v)=0\) for every \(w\in H_v\), namely when the two orthogonal hyperplanes of \(v\) coincide. When \(A\) is invertible this condition is equivalent to the existence of a scalar \(\lambda\ne0\) such that \(Av=\lambda A^{\mathsf T}v^{[4]}\). Rescaling \(v\) by a cube root of \(\lambda\) produces a vector obeying the normalized Hermitian equation
\[
Av=A^{\mathsf T}v^{[4]}.
\]
The normalized vector is unique up to multiplication by \(\mathbb F_4^\times\). For a normalized isotropic vector, restriction of \(\beta\) to \(H_v\) has two-sided radical exactly the line spanned by \(v\), because the original \(\beta\) is nondegenerate; hence the quotient is a nonsingular three-dimensional \(2\)-bic form. The cone base is therefore a smooth plane cubic. Conversely every Eckardt point gives such an isotropic normalized Hermitian line. The standard count of isotropic lines of a nondegenerate five-dimensional Hermitian space over \(\mathbb F_4\) is \((2^5+1)(2^4-1)/(2^2-1)=165\); this is also checked exactly in the standalone computations.

**A finite Frobenius model.** Set \(C=(A^{\mathsf T})^{-1}A\in\operatorname{GL}_5(\mathbb F_2)\), with finite order \(h\). Normalized Hermitian vectors solve \(v^{[4]}=Cv\). By iteration, each solution is defined over \(\mathbb F_{2^{2h}}\), because \(v^{[4^h]}=C^h v=v\). This equation is linear over \(\mathbb F_4\), and its kernel in \(\mathbb F_{2^{2h}}^5\) has dimension five over \(\mathbb F_4\). Thus there are exactly 1,024 normalized vectors, including zero. Identify nonzero solutions under multiplication by \(\mathbb F_4^\times\), test \(F_A(v)=0\), and obtain exactly 165 isotropic classes. Since \(C\) has entries in \(\mathbb F_2\), coordinate squaring preserves normalized solutions and induces the arithmetic Frobenius permutation. Decomposing its action gives the cycles in the table. This derivation covers all geometric points, not merely a bounded search among points of small extension degree.

**Completeness of the arithmetic cases.** The thirteen displayed binary matrices are invertible and represent disjoint congruence orbits. The accompanying `verify_orbits.c` constructs every orbit under adjacent coordinate transpositions and one elementary transvection; these transformations generate \(\operatorname{GL}_5(\mathbb F_2)\). It obtains the thirteen orbit sizes shown above and total 9,999,360; this is the full number \(\prod_{i=0}^{4}(2^5-2^i)\) of invertible matrices. In particular every smooth binary Frobenius cubic threefold occurs in exactly one of these orbits. The 165-point computation, run on each representative, is congruence invariant, completing the ten-type classification.

## Verification
The self-contained Python script `hermitian_orbits.py` performs arithmetic in explicitly constructed binary extension fields, obtains an exact kernel basis of the semilinear equation, tests every normalized solution, and decomposes the Frobenius permutation. It checks that there are 165 isotropic projective solutions and that every cycle decomposition has total length 165. The separate `verify_orbits.c` re-establishes the thirteen class coverage and orbit weights from elementary \(\operatorname{GL}_5(\mathbb F_2)\) generators; it ends with `ALL_THIRTEEN_GL5_CONGRUENCE_ORBITS_VERIFIED`. As a differential check, `verify_small_fields.py` directly tests the tangent-cone equations on all rational projective points over \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\), agreeing with the cycle-derived fixed-point counts for all thirteen equations. All checkers were executed against the supplied source files. The proofs of the finite algorithms rest on explicit bijections and exhaustive ranges, not statistical testing.

## Relationship to prior work
Raymond Cheng's *\(q\)-bic threefolds and their surface of lines* (2024), §§1.5–1.6 and 2.1–2.2, establishes the smoothness, Hermitian-vector and cone-point framework and its relevance to Fano surfaces. The earlier classification of Frobenius forms in five variables by Kadyrsizova, Page, Singh, Smith, Vraciu and Witt classifies the algebraically closed-field forms; it does not compute the finite-field Frobenius cycles. The published *Rational Fano-line fingerprints of non-Frobenius-split cubic threefolds over \(\mathbf F_2\)* supplies the thirteen arithmetic projective classes, their matrices, orbit sizes, and rational point–line incidence profiles; all are credited here, rather than treated as new. Bockondas and Bossoto analyze Eckardt points of complex cubic threefolds, where the characteristic-two Hermitian arithmetic considered here is not applicable. The contribution of the present finding is specifically the **complete extension-field splitting/Zeta census of all 165 Eckardt centers** across the thirteen arithmetic classes, together with the exact semilinear computation.

## Limitations
Only the smooth Frobenius-form cubic-threefold locus over \(\mathbb F_2\) is classified, not arbitrary cubic threefolds or cubic surfaces. The geometric set of 165 points and the general Hermitian description are known; no novelty is claimed for them or for the thirteen base-field matrix classes. The cycle table describes the finite reduced Eckardt-point locus, not its possible infinitesimal ambient parameter scheme. Geometric splitting degrees do not by themselves determine the zeta function of the cubic threefold or of its Fano surface. An unindexed classical finite-unitary-group computation equivalent to some cycle rows cannot be excluded without independent literature audit.

## References
1. R. Cheng, *\(q\)-bic threefolds and their surface of lines*, arXiv:2402.09884v1, first public 2024-02-15, https://arxiv.org/html/2402.09884v1 .
2. Z. Kadyrsizova, J. Page, J. Singh, K. E. Smith, A. Vraciu and E. E. Witt, *Classification of Frobenius Forms in Five Variables*, arXiv:2104.05635, first public 2021-04-12, https://arxiv.org/abs/2104.05635 .
3. G. G. Bockondas and B. G. R. Bossoto, *Eckardt points on a cubic threefold*, arXiv:2309.08124, first public 2023-09-15, https://arxiv.org/html/2309.08124v2 .
4. *Rational Fano-line fingerprints of non-Frobenius-split cubic threefolds over \(\mathbf F_2\)*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-rational-fano-line-fingerprints-of-non-frobenius-split-cubic-thr--62a143310a01 .
