# Thirty Frobenius chamber spectra for seven-point degree-two del Pezzo surfaces and their Geiser twists

## Finding

**Theorem.** Let \(k=\mathbb F_q\) be a finite field of **odd** cardinality, and let \(Z\subset\mathbb P^2_k\) be a reduced finite étale subscheme of degree seven such that its seven geometric points are in del Pezzo general position (no three collinear and no six on one conic). Put \(S=\operatorname{Bl}_Z\mathbb P^2_k\). Let \(S^\gamma\) denote the nontrivial quadratic twist of its anticanonical double-plane structure by the central Geiser involution \(\gamma\).

The \(33\,645\) geometric Zariski chambers on each surface form finite Frobenius sets. The full permutation cycle spectrum is given, **for every one of the fifteen partitions of seven** describing Frobenius on \(Z(\bar k)\), by the following thirty-case table. Here \(\ell^{a}\) means exactly \(a\) cycles of length \(\ell\), and a *rational chamber* means a geometrically defined chamber admitting an interior \(k\)-rational divisor class (equivalently a Frobenius-stable negative support).

| Seven-point cycle partition | Untwisted rational chambers | Geiser-twist rational chambers | Untwisted chamber cycle lengths | Geiser-twist cycle lengths |
|---|---:|---:|---|---|
| \((7)\) | 3 | 1 | \(1^{3}\, 7^{4806}\) | \(1\, 2\, 14^{2403}\) |
| \((6,1)\) | 11 | 3 | \(1^{11}\, 2^{23}\, 3^{82}\, 6^{5557}\) | \(1^{3}\, 2^{27}\, 3^{14}\, 6^{5591}\) |
| \((5,1,1)\) | 45 | 1 | \(1^{45}\, 5^{6720}\) | \(1\, 2^{22}\, 10^{3360}\) |
| \((5,2)\) | 13 | 1 | \(1^{13}\, 2^{16}\, 5^{1296}\, 10^{2712}\) | \(1\, 2^{22}\, 10^{3360}\) |
| \((4,1,1,1)\) | 203 | 3 | \(1^{203}\, 2^{551}\, 4^{8085}\) | \(1^{3}\, 2^{651}\, 4^{8085}\) |
| \((4,2,1)\) | 51 | 11 | \(1^{51}\, 2^{627}\, 4^{8085}\) | \(1^{11}\, 2^{647}\, 4^{8085}\) |
| \((4,3)\) | 11 | 3 | \(1^{11}\, 2^{23}\, 3^{64}\, 4^{279}\, 6^{176}\, 12^{2602}\) | \(1^{3}\, 2^{27}\, 4^{279}\, 6^{208}\, 12^{2602}\) |
| \((3,1,1,1,1)\) | 1,173 | 1 | \(1^{1173}\, 3^{10824}\) | \(1\, 2^{586}\, 6^{5412}\) |
| \((3,2,1,1)\) | 265 | 1 | \(1^{265}\, 2^{454}\, 3^{2076}\, 6^{4374}\) | \(1\, 2^{586}\, 6^{5412}\) |
| \((3,2,2)\) | 57 | 5 | \(1^{57}\, 2^{558}\, 3^{416}\, 6^{5204}\) | \(1^{5}\, 2^{584}\, 6^{5412}\) |
| \((3,3,1)\) | 57 | 1 | \(1^{57}\, 3^{11196}\) | \(1\, 2^{28}\, 6^{5598}\) |
| \((2,1,1,1,1,1)\) | 6,493 | 1 | \(1^{6493}\, 2^{13576}\) | \(1\, 2^{16822}\) |
| \((2,2,1,1,1)\) | 1,305 | 5 | \(1^{1305}\, 2^{16170}\) | \(1^{5}\, 2^{16820}\) |
| \((2,2,2,1)\) | 257 | 45 | \(1^{257}\, 2^{16694}\) | \(1^{45}\, 2^{16800}\) |
| \((1,1,1,1,1,1,1)\) | 33,645 | 1 | \(1^{33645}\) | \(1\, 2^{16822}\) |

Every table entry has total geometric size \(\sum_\ell \ell a_\ell=33\,645\). In particular, when the seven base points form one Frobenius orbit, the untwisted surface has chamber cycles \(1^3 7^{4806}\), whereas its Geiser twist has \(1^1 2^1 14^{2403}\). Thus only **three** versus **one** chambers are rational over \(k\). An ordinary blowup with base-point partitions \((6,1)\) and \((5,2)\) has the same arithmetic Picard rank three but respectively eleven and thirteen rational Zariski chambers.

The geometric support polynomial, independently checked, is
\[
1+56t+756t^2+4032t^3+10080t^4+12096t^5+6048t^6+576t^7.
\]
For every integer \(n\ge1\), the number of chambers rational over \(\mathbb F_{q^n}\) is exactly \(\sum_{\ell\mid n}\ell a_\ell\), with the spectrum taken from the corresponding row.

## Assumptions and scope

The base point scheme must be Frobenius stable, reduced of geometric degree seven and in the above general position. This assumption makes \(-K_S\) ample, \(K_S^2=2\), and ensures exactly 56 geometric exceptional curves. The nontrivial Geiser quadratic twist is defined because \(q\) is odd: the anticanonical morphism is a separable double cover \(w^2=f(x,y,z)\), and a nonsquare scalar gives the other quadratic form. The twist's geometric Picard action is \(\gamma\sigma\), where \(\sigma\) permutes the seven point labels and \(\gamma\) is central. We do not assert that each partition is realizable for each small finite field; the formula is conditional on existence of a septuple of the stated kind.

A chamber is indexed by the support of the negative part of the Zariski decomposition on the geometric big cone, including the nef chamber for the empty support. Its arithmetic rationality means that an interior rational divisor class exists on the given surface over \(k\), not simply that a particular negative curve descends individually. The chamber's *geometric Frobenius cycle* is computed on this finite support set, and this is the finite object classified here.

## Proof

1. **Exceptional classes.** In the divisor basis \(H,E_1,\ldots,E_7\), write \(D=dH-\sum_{i=1}^7m_iE_i\), with intersection \(D\cdot D'=dd'-\sum_i m_i m_i'\) and \(-K=3H-\sum_iE_i\). The complete 56-element list is: seven exceptional divisors \(E_i\); twenty-one strict transforms \(H-E_i-E_j\); twenty-one conic transforms \(2H-\sum_{i\in I}E_i\) with \(|I|=5\); and seven cubic transforms \(3H-2E_i-\sum_{j\ne i}E_j\). Each has self-intersection \(-1\) and \((-K)\)-degree one. The stated general position ensures that this is the complete geometric negative-curve list; it also makes every intersection between distinct effective irreducible curves nonnegative.

2. **Chamber supports.** A symmetric matrix with diagonal \(-1\) and off-diagonal nonnegative integers is negative definite only if all its off-diagonal entries vanish: a positive off-diagonal entry would give a two-by-two principal submatrix with determinant at most zero. Conversely, a subset of pairwise disjoint negative-one curves has intersection matrix \(-I\), hence is negative definite. The negative-support criterion for Zariski chambers therefore identifies them *bijectively* with the pairwise-disjoint subsets of these 56 curves. An explicit complete recursive enumeration gives the support polynomial displayed in the theorem. Summing its coefficients yields \(33\,645\), the established geometric chamber count.

3. **Rational descent.** If a support \(T\) is Frobenius stable, both \(-K\) and \(\sum_{C\in T}C\) are \(k\)-rational divisor classes. The effective \(k\)-rational divisor class
\[
D_T=-K+2\sum_{C\in T}C
\]
has Zariski decomposition \(D_T=P_T+N_T\) with \(N_T=\sum_{C\in T}C\) and \(P_T=-K+\sum_{C\in T}C\). For each \(C\in T\), \(P_T\cdot C=1-1=0\); for every other irreducible curve \(B\), ampleness of \(-K\) and nonnegativity of intersections of distinct curves show \(P_T\cdot B>0\). Thus \(P_T\) is nef, and \(P_T^2=2+|T|>0\) makes it big. In particular \(D_T\) lies in the interior of its geometric chamber. Conversely, the uniqueness of a Zariski decomposition forces the negative support of a rational divisor to be Frobenius stable. Therefore rational chambers are precisely Frobenius-fixed supports. This argument applies verbatim to \(S^\gamma\).

4. **Arithmetic action.** Frobenius on the ordinary blown-up surface permutes the seven labels according to a partition \(\lambda\vdash7\). The Geiser involution on a negative-one class is \(\gamma(C)=-K-C\); in coordinates this sends \((d;m_i)\) to \((3-d;1-m_i)\), exchanging the exceptional and cubic classes and pairing lines with complementary conics. The Geiser twist consequently acts by \(\gamma\sigma\). The two maps commute and preserve disjointness, so they permute every chamber support.

5. **Exhaustive finite calculation, with independent reconstruction.** The first verifier builds the entire 56-curve intersection table, recursively enumerates every pairwise-disjoint support exactly once by increasing vertex index, and follows Frobenius and twisted-Frobenius cycles on all \(33\,645\) supports, for each of the fifteen partitions. The second verifier does **not** use the list of \(33\,645\) supports. It first decomposes the 56 curves into orbits under each Frobenius power, discards curve orbits containing intersections, and enumerates mutually compatible remaining orbits to count fixed supports. Möbius inversion
\[
a_\ell=\frac1\ell\sum_{d\mid\ell}\mu(\ell/d)F(d)
\]
then recovers the exact count of length-\(\ell\) support cycles from the fixed counts \(F(d)\). The two independently reconstructed cycle profiles and rational support-size distributions agree with the complete tabulation in `CHAMBER_SPECTRA.json` in all thirty cases. Every resulting cycle profile has total weight \(33\,645\). This completes the finite classification.

## Verification

The accompanying self-contained files are `CHAMBER_SPECTRA.json`, `verify_chamber_cycles.py`, and `verify_orbit_blocks.py`. In the same directory, execute `python3 verify_chamber_cycles.py` followed by `python3 verify_orbit_blocks.py`. They use only the Python standard library, enumerate **all fifteen integer partitions of seven**, and compare exact integer cycle counts with every entry of the JSON certificate. The first succeeds only after the terminal marker `DIRECT_33645_SUPPORT_PERMUTATION_30_CASES_OK`; the second only after `INDEPENDENT_ORBIT_BLOCK_AND_MOBIUS_30_CASES_OK`. No numerical approximation, random sampling, uninspected remote dependency, or timeout inference is involved. The structural geometric and descent arguments above are essential and are not inferred solely from a table.

## Relationship to prior work

Bauer–Funke–Neumann (2009) give the negative-definite support criterion and the **geometric** total \(33\,645\) for a degree-two del Pezzo surface. Bauer–Schmitz (2012) study nonequivariant chamber-count algorithms on surfaces with larger Picard rank. Rieken (2016) records the explicit 56 classes and the central Geiser pairing. Bergvall (2022) studies Frobenius/Weyl types for degree-two del Pezzo surfaces. Those results supply geometric and arithmetic context, but none of the inspected relevant portions states the thirty support-cycle distributions given above. The present result restricts to the natural subgroup generated by seven-label permutations and Geiser twisting; it is not a classification of all elements of \(W(E_7)\). Related published chamber-count results for weak degree-two and lower-degree del Pezzo surfaces concern different configurations or Weyl actions and do not imply this table.

## Limitations

All conclusions are conditional on a smooth degree-two del Pezzo surface arising as the blowup of a reduced Frobenius-stable **seven-point scheme in general position**, or its Geiser quadratic twist, over a finite field of **odd** order. Other Frobenius conjugacy classes in the full Weyl group, bad point configurations, characteristic two, existence frequencies of marked septuples, and the geometry of the chambers' walls are not classified. The novelty comparison is best-knowledge rather than an independently certified exhaustive priority search; a previously unindexed equivariant table may exist. The mathematical proof and integer outputs have received self-review, but not independent mathematical validation.

## References

- T. Bauer, M. Funke, and S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958v1 (first public 2009-12-04), https://arxiv.org/abs/0912.0958.
- T. Bauer and D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373v1 (2012), https://arxiv.org/abs/1204.4373.
- S. Rieken, *Moduli of real pointed quartic curves*, Geometriae Dedicata 185 (2016), Section 3.3, https://doi.org/10.1007/s10711-016-0174-0.
- O. Bergvall, *Frobenius actions on Del Pezzo surfaces of degree 2*, arXiv:2211.12855 (2022), https://arxiv.org/abs/2211.12855.
