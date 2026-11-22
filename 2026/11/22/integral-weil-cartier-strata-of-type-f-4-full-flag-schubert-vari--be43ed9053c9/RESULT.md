# Integral Weil–Cartier strata of type-\(F_4\) full-flag Schubert varieties

## Finding
Let \(G\) be a connected, simply connected, complex simple algebraic group of type \(F_4\), \(B\) a Borel subgroup, and \(X_w=\overline{BwB/B}\subset G/B\) for \(w\in W(F_4)\). Let \(\mathrm{Cl}(X_w)\) denote the Weil divisor class group and \(\mathrm{Pic}(X_w)\) the Cartier class group. Among the \(1,152\) Schubert varieties \(X_w\), exactly \(233\) are \(\mathbb Q\)-factorial. Their finite quotients \(\mathrm{Cl}(X_w)/\mathrm{Pic}(X_w)\) have the **complete** distribution

| Quotient group | Number of \(w\) |
|---|---:|
| \(0\) | \(171\) |
| \(\mathbb Z/2\mathbb Z\) | \(49\) |
| \((\mathbb Z/2\mathbb Z)^2\) | \(13\) |

The other \(919\) are not \(\mathbb Q\)-factorial. In particular, every Weil divisor on every \(\mathbb Q\)-factorial \(X_w\) becomes Cartier after multiplication by \(2\); the maximal order of the global Weil–Cartier quotient is \(4\), attained without a cyclic order-four factor. Both nontrivial quotient types occur, first in lengths \(3\) and \(6\), respectively.

## Assumptions and scope
Work over \(\mathbb C\), in the full flag variety \(G/B\); no parabolic or other root systems are included. Number the simple reflections \(s_1,s_2,s_3,s_4\) with Cartan matrix \(A=(\langle\alpha_i^\vee,\alpha_j\rangle)_{i,j}\) equal to
\[
\begin{pmatrix}2&-1&0&0\\-1&2&-2&0\\0&-1&2&-1\\0&0&-1&2\end{pmatrix}.
\]
A \(\mathbb Q\)-factorial normal variety is one for which every Weil divisor has a positive integral multiple that is Cartier. The quotient \(\mathrm{Cl}/\mathrm{Pic}\) here is the global group of Weil classes modulo Cartier classes, not a local class group at a particular point.

## Proof
**Reduction to integral linear algebra.** For any \(w\), let \(I(w)=\{i:s_i\le w\}\) and let \(\mathcal C(w)=\{v<w:\ell(v)=\ell(w)-1\}\) be the set of Bruhat coatoms. Each \(v\in\mathcal C(w)\) determines a unique positive coroot \(\beta_v^\vee\) with \(v=w s_{\beta_v}\). By the Picard-basis and Schubert-divisor formulas of Li–Rietsch–Yang [1, Proposition A, Theorem B and Proposition 5.2], the matrix
\[
M_w=\big(\langle\omega_i,\beta_v^\vee\rangle\big)_{v\in\mathcal C(w),\ i\in I(w)}
\]
represents the injection \(\mathrm{Pic}(X_w)\to\mathrm{Cl}(X_w)\). Thus \(\mathrm{Cl}(X_w)/\mathrm{Pic}(X_w)\cong\mathrm{coker}(M_w)\). The same cited result shows that \(M_w\) has full column rank. It follows that \(X_w\) is \(\mathbb Q\)-factorial precisely when \(|\mathcal C(w)|=|I(w)|\), in which case the finite quotient has the invariant factors of \(M_w\).

**Exhaustive finite reduction.** The attached standalone Python checker implements root reflections on the integral simple-root lattice and their dual action on simple coroots. Its breadth-first enumeration generates exactly \(1,152\) distinct matrices, with maximal Coxeter length \(24\) and the standard rank-four \(F_4\) length distribution. It independently constructs the \(24\) positive root/coroot pairs and verifies every enumerated Coxeter length by counting positive roots carried negative. For each reduced expression \(w=s_{i_1}\cdots s_{i_\ell}\), the strong exchange condition lists all Bruhat coatoms by reduced single-letter deletions. Deleting position \(j\), with suffix \(u=s_{i_{j+1}}\cdots s_{i_\ell}\), gives the positive representative of \(\beta_v^\vee=u^{-1}\alpha_{i_j}^\vee\). For every one of the \(1,152\) elements, an **independent** enumeration using all \(24\) positive root reflections gives exactly the same cover-to-coroot dictionary. In total this checks \(6,168\) covers.

**Integer determinant and Smith invariants.** The checker takes the simple-coroot coordinates of the cover coroots as the rows of \(M_w\). If there are more rows than columns the quotient has positive free rank. In the square case the script computes the gcd of every integral minor of each size. The ratios of consecutive determinantal divisors give the exact Smith invariant factors, without floating-point arithmetic or a black-box algebra system. The exhaustive counts are \(171\) trivial groups, \(49\) groups with invariant factors \((2)\), and \(13\) with invariant factors \((2,2)\); precisely \(919\) matrices are nonsquare. This proves every assertion in the finding.

For explicit witnesses, \(w=s_2s_3s_2\) has \(M_w=\begin{pmatrix}1&0\\1&2\end{pmatrix}\), giving \(\mathbb Z/2\mathbb Z\). For \(w=s_2s_3s_2s_4s_3s_2\), the cover-coroot matrix is
\[
M_w=\begin{pmatrix}1&0&0\\1&2&0\\1&2&2\end{pmatrix},
\]
whose Smith form is \(\mathrm{diag}(1,2,2)\), giving \((\mathbb Z/2\mathbb Z)^2\). Their Coxeter lengths are \(3\) and \(6\). The finite census excludes any earlier occurrence or another finite group type.

## Verification
Run `python3 f4_cartier_check.py` using only the Python standard library. Its machine-independent exact checks include \(|W|=1152\), \(24\) positive roots, \(6,168\) independently matched Bruhat covers, inversion-length consistency for every element, exact signed permutation determinants, and gcds of all square minors. The output ends with `CHECKS PASS: enumeration, inversion lengths, reflection covers, determinants, minors.` The complete code is embedded with this result.

## Relationship to prior work
Li, Rietsch and Yang [1] determine the Picard basis and general matrix criterion, including the difference between \(\mathbb Q\)-factoriality and factoriality outside simply-laced type. Their worked non-simply-laced classification treats type \(G_2\), and their type-\(F_4\) reference concerns possible root coefficients, not a complete census of global Weil–Cartier quotients. The contribution here is the exact all-element **integral classification** for the exceptional \(F_4\) full-flag family, including the order-four elementary abelian cases, not a new general factoriality criterion. Related results on Betti polynomials or type-\(D\) Schubert varieties do not imply these Smith invariants.

## Limitations
This does not classify torsion in the \(919\) positive-rank quotients, local divisor class groups at individual singular points, Schubert varieties in partial flag spaces, or other Weyl types. The exhaustive result is conditional on the established Picard/divisor basis theorem [1], independently stated here rather than reproved. The finite computations are exact and directly replayable, but an independent mathematical audit has not been performed. Possible unindexed equivalent tabulations remain a priority risk.

## References
[1] Changzheng Li, Konstanze Rietsch and Mingzhi Yang, *An anticanonical perspective on \(G/P\) Schubert varieties*, arXiv:2506.18388v1, first submitted 2025-06-23, https://arxiv.org/html/2506.18388v1. See Proposition A, Theorem B, Proposition 5.2, Remark 5.5 and Section 7.
