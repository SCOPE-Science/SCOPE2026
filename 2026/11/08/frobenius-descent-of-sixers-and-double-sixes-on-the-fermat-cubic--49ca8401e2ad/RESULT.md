# Frobenius descent of sixers and double-sixes on the Fermat cubic surface

## Finding
For every prime power \(q\) of characteristic different from \(3\), let \(X/\mathbb F_q\) be the smooth Fermat cubic surface
\[
X:\quad x_0^3+x_1^3+x_2^3+x_3^3=0.
\]
A **sixer** is an unordered set of six distinct, pairwise skew *geometric* lines on \(X\). A **double-six** is an unordered pair of complementary sixers: their twelve lines have the classical double-six incidence, each line meeting five lines of the other sixer and missing one, with the six omissions forming a bijection. A marking is **rational** if its underlying geometric set is Frobenius-invariant, without requiring its individual lines to be rational.

The complete arithmetic census is

| Ground field | Rational sixers | Rational unordered double-sixes | Double-sixes with two individually rational sixer halves | Double-sixes with Frobenius-exchanged halves |
|---|---:|---:|---:|---:|
| \(q\equiv1\pmod3\) | 72 | 36 | 36 | 0 |
| \(q\equiv2\pmod3\) | 2 | 4 | 1 | 3 |

In the nonsplit case exactly three geometric lines are individually rational, one in each coordinate-pairing family, but neither of the rational sixers contains any of them. Each of the two rational sixers consists of three Frobenius-conjugate pairs of lines, and together the two rational sixers are the halves of the unique rational split-half double-six. The three other rational double-sixes have *no* rational sixer half.

Writing \(\mathcal S_X\) for the finite étale scheme of unordered sixers and \(\mathcal D_X\) for the scheme of unordered double-sixes, when \(q\equiv2\pmod3\) their zeta functions are
\[
Z(\mathcal S_X,T)=\frac1{(1-T)^2(1-T^2)^{35}},\qquad
Z(\mathcal D_X,T)=\frac1{(1-T)^4(1-T^2)^{16}}.
\]
When \(q\equiv1\pmod3\), they are respectively \((1-T)^{-72}\) and \((1-T)^{-36}\). These formulas determine the marking counts over every finite extension. The number of \(\mathbb F_q\)-defined blow-down morphisms \(X\to\mathbb P^2\), modulo projective changes of target, is 72 in the split case and 2 in the nonsplit case.

## Assumptions and scope
Choose \(\omega\in\overline{\mathbb F}_q\) with \(\omega^2+\omega+1=0\). The three pairings of the four coordinates are \((01\mid23)\), \((02\mid13)\), and \((03\mid12)\). For each pairing \(((i,j),(k,l))\) and exponents \(a,b\in\{0,1,2\}\), let \(L_{f,a,b}\) be the line cut out by \(x_i+\omega^a x_j=x_k+\omega^b x_l=0\). These are the 27 distinct geometric lines on the smooth cubic. In characteristic \(2\) these equations and all conclusions remain valid; characteristic \(3\) is excluded because the surface is not smooth.

A rational sixer is not the same thing as a set of six rational lines. A rational double-six may have its two sixer halves exchanged by Frobenius. The zeta functions concern finite étale *marking schemes*, not the cubic surface itself.

## Proof
**1. Exact incidence and independence of the characteristic.** Work in \(\mathbb Z[\omega]\), with \(\omega^2+\omega+1=0\). Each line is given by two displayed linear forms. Two distinct lines meet if and only if the determinant of their four linear forms vanishes. For all \(\binom{27}{2}=351\) unordered pairs, the exact norms of these determinants are distributed as follows:
\[
\begin{array}{c|ccc}\text{determinant norm}&0&3&9\\\hline
\text{number of pairs}&135&162&54\end{array}
\]
The ring norm is \(N(a+b\omega)=a^2-ab+b^2\). In particular every nonzero determinant is a unit up to powers of \(1-\omega\), and it cannot vanish after reduction in any characteristic other than \(3\). Thus this single exact incidence computation applies to *every* ground field in the theorem. Every geometric line meets ten of the other 26.

**2. Exhaustive sixer and double-six construction.** Enumerate the \(\binom{27}{6}=296010\) unordered six-element subsets, retaining exactly those whose 15 pairs have nonzero determinant. This produces exactly \(72\) sixers. For every sixer \(S\), take the six lines outside \(S\) that meet exactly five elements of \(S\). Direct incidence calculation shows that they form another sixer \(S'\), that the unique missed element of \(S\) is different for the six lines of \(S'\), and that the operation \(S\mapsto S'\) is a fixed-point-free involution. Hence exactly \(36\) unordered double-sixes are obtained. Both algorithms are explicitly reproduced with exact arithmetic in `verify.py`; every possible sixer is tested, with no pruning assumption or numerical approximation.

**3. Frobenius.** Frobenius fixes each coordinate-pairing family and maps \(L_{f,a,b}\) to \(L_{f,qa,qb}\), with exponents modulo \(3\). If \(q\equiv1\pmod3\), the action is trivial, proving the first row. If \(q\equiv2\pmod3\), it is the involution \((f,a,b)\mapsto(f,-a,-b)\). Applying this explicit involution to all 72 sixers finds exactly two fixed sixers; applying it to all 36 unordered double-sixes finds exactly four fixed double-sixes, one with two fixed halves and three with exchanged halves. The two fixed sixers are, in zero-based lexicographic indexing of \((f,a,b)\),
\[
\{4,8,14,16,22,26\}\quad\text{and}\quad\{5,7,13,17,23,25\}.
\]
Each is a union of three two-cycles of the line involution; the only individually fixed lines under this involution are \(L_{f,0,0}\), and neither of the two Frobenius-fixed sixers contains one of them. The explicit fixed/swap census is therefore uniform in \(q\), including characteristic \(2\).

**4. Zeta functions and contractions.** An involution on 72 objects with two fixed objects has 35 remaining two-cycles; similarly 36 double-sixes with four fixed ones have 16 two-cycles. For a finite étale scheme, the zeta function is the product of \((1-T^d)^{-1}\) over Frobenius orbits of size \(d\), proving the formulas. The contraction of a Frobenius-invariant disjoint sixer descends to a smooth degree-nine del Pezzo surface, a Severi–Brauer surface over \(\mathbb F_q\). Because the Brauer group of a finite field is zero, the target is \(\mathbb P^2_{\mathbb F_q}\). Conversely any such contraction gives exactly its exceptional sixer, so the count of contractions modulo target automorphism equals the count of rational sixers.

## Verification
`python3 verify.py` performs the complete 351-pair determinant-norm census in exact Eisenstein integers, all 296010 six-subsets, involutive complementary-sixer test with bijective omissions, and the complete Frobenius fixed-point and half-swap census. Successful output includes `VERIFY_FERMAT_DOUBLE_SIX_OK sixers=72 double_sixes=36 fixed_sixers=2 fixed_double_sixes=4`.

`python3 verify_fields.py` independently reconstructs the line incidence over \(\mathbb F_4\) (on a model over \(\mathbb F_2\)) and \(\mathbb F_7\) using elementary finite-field row reduction, without the integral norm arithmetic, and reproduces the split/nonsplit counts. Its finite tests are cross-checks, not substitutes for the characteristic-uniform integral determinant argument.

## Relationship to prior work
Ronno Das, *Arithmetic statistics on cubic surfaces* (first publicly posted February 25, 2020), develops a general framework for counting Frobenius-stable line-incidence markings and gives distributions of some markings across all cubic surfaces. That general framework does not state the specific Fermat-surface sixer and unordered double-six fixed-point numbers, nor their split-versus-exchanged halves. Elsenhans and Jahnel develop general arithmetic of Galois-invariant double-sixes, but do not give the present Fermat fixed-point classification. Favacchio and Malara classify the 72 geometric sixers of the Fermat cubic into automorphism orbits of sizes 18 and 54; the publicly available companion source was also examined. A published refinement identifies coordinate-pairing profiles and a prism decomposition of the 18-orbit. These geometric classifications by themselves do not supply the Frobenius fixed-set/half-swap enumeration. In particular, the present contribution is not the previously known geometric number 72 or 36, but the complete arithmetic descent comparison and its zeta functions.

## Limitations
The conclusion is specific to the standard Fermat cubic and its finite-field twists only as explicitly defined by this equation; it is not a general table for every cubic surface with the same Weyl group conjugacy type. The calculation is finite but exhaustive because the 27 geometric lines and all candidate six-subsets have been proved to be the complete universe. Equivalent older computations under Weyl-group language could exist. The complete text of the 2026 Favacchio--Malara paper could not be accessed; its abstract and public companion computation were inspected, leaving a specific priority risk. No independent mathematical audit is asserted.

## References
1. Ronno Das, *Arithmetic statistics on cubic surfaces*, arXiv:2002.11183, first posted 2020-02-25, https://arxiv.org/abs/2002.11183.
2. Andreas-Stephan Elsenhans and Jörg Jahnel, *Cubic surfaces with a Galois invariant double-six*, 2010, https://doi.org/10.2478/s11533-010-0036-1.
3. Stephen McKean, *Rational lines on smooth cubic surfaces*, arXiv:2101.08217, first posted 2021-01-20.
4. Giuseppe Favacchio and Grzegorz Malara, *On the Geometry of Sixers on the Fermat Cubic Surface*, arXiv:2608.23716, first posted 2026-08-24; public computational companion: https://github.com/GrzMal/sixers-on-the-fermat-cubic-surface.
5. *Pairing-profile classification and prism blocks for the 18-sixer orbit on the Fermat cubic surface*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-pairing-profile-classification-and-prism-blocks-for-the-18-sixer--815a6195e439.
