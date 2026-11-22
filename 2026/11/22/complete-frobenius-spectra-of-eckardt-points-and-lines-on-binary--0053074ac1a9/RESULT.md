# Complete Frobenius spectra of Eckardt points and lines on binary non-Frobenius-split cubic surfaces

## Finding

Let \(A=(a_{ij})\in \operatorname{GL}_4(\mathbb F_2)\). Set \(S_A\subset\mathbb P^3_{\mathbb F_2}\) by
\[F_A(X)=\sum_{i,j=0}^3 a_{ij}X_i^2X_j=0.\]
The complete arithmetic classification of the reduced schemes of the twenty-seven geometric lines and forty-five geometric Eckardt points is given by the table below. Matrix labels are unsigned 16-bit hexadecimal integers; the nibble in positions \(4i,\ldots,4i+3\) is row \(i\), with the least-significant bit being column zero. Cycle notation `3^4 6^5` means four Frobenius orbits of length three and five of length six, not a polynomial power.

| Matrix | Congruence orbit | Surface points | Rational lines | Rational Eckardt points | 45-point Frobenius cycles | 27-line Frobenius cycles |
|---|---:|---:|---:|---:|---|---|
| `1468` | 1120 | 3 | 0 | 3 | `1^3 3^4 6^5` | `3^5 6^2` |
| `126b` | 420 | 3 | 1 | 3 | `1^3 2^1 4^10` | `1^1 2^3 4^5` |
| `1486` | 4032 | 5 | 0 | 0 | `5^3 10^3` | `2^1 5^3 10^1` |
| `1469` | 3360 | 7 | 0 | 1 | `1^1 2^1 3^2 6^6` | `3^1 6^4` |
| `126c` | 5040 | 7 | 1 | 1 | `1^1 4^3 8^4` | `1^1 2^1 8^3` |
| `1249` | 420 | 7 | 3 | 7 | `1^7 2^19` | `1^3 2^12` |
| `128d` | 3360 | 9 | 1 | 0 | `2^1 3^1 4^1 12^3` | `1^1 4^2 6^1 12^1` |
| `128c` | 1120 | 9 | 3 | 0 | `2^3 3^5 6^4` | `1^3 2^3 3^4 6^1` |
| `124a` | 1260 | 11 | 5 | 3 | `1^3 2^1 4^10` | `1^5 2^1 4^5` |
| `1248` | 28 | 15 | 15 | 15 | `1^15 2^15` | `1^15 2^6` |


All ten matrices are invertible; every invertible binary \(A\) is congruent to exactly one table representative via \(A\mapsto P^{\mathsf T}AP\). The matrix-congruence orbit sizes in the table total \(20160\). If \(e_d(A)\) and \(\ell_d(A)\) count length-\(d\) cycles on Eckardt points and lines, respectively, the reduced zero-dimensional schemes have zeta functions
\[Z_{\mathrm{Eck}}(T)=\prod_{d\ge1}(1-T^d)^{-e_d(A)},\qquad Z_{\mathrm{lines}}(T)=\prod_{d\ge1}(1-T^d)^{-\ell_d(A)}.\]
In particular, matrices `126b` and `124a` share the Eckardt-point cycle type `1^3 2^1 4^10`, but have different line types `1^1 2^3 4^5` and `1^5 2^1 4^5`. Hence their complete Eckardt-point zeta functions agree whereas their line-scheme zeta functions differ. Matrix `128d` has three degree-twelve Eckardt-point places.

## Assumptions and scope

The base field is exactly \(\mathbb F_2\); "non-Frobenius-split" is used in the established sense of Frobenius splitting of cubic hypersurfaces. Its full-rank Frobenius-form cubics \(F_A\) are smooth because \(\nabla F_A=A^{\mathsf T}X^{[2]}\) has no projective zero. We classify the *reduced geometric support* of the finite Eckardt-point scheme and the finite line scheme, not their possibly nonreduced scheme structures and not all smooth binary cubic surfaces. The source equivalence of smooth non-Frobenius-split cubics with full-rank binary Frobenius forms is prior work. The ten marked congruence classes are used for complete bookkeeping; the novelty assertion concerns the joint complete Frobenius cycle data, not the existence of the classes or their rational-line counts.

## Proof

Write \(B=(A^{\mathsf T})^{-1}A\). A tangent plane to \(S_A\) at a point \(u\) has equation \((A^{\mathsf T}u^{[2]})^{\mathsf T}X=0\). On a smooth cubic in characteristic two, the tangent section is three concurrent geometric lines exactly when its quadratic residual in the tangent plane vanishes. For a Frobenius form this condition is that \(A^{\mathsf T}u^{[4]}\) and \(Au\) are proportional; equivalently, the projective point admits a representative satisfying \(u^{[4]}=Bu\). Projective representatives can be rescaled to this normalization by solving a cubic equation over the algebraic closure, and the three normalized representatives are related by \(\mathbb F_4^\times\). The additional surface equation \(F_A(u)=0\) selects the Eckardt points.

For each matrix representative, the equation \(u^{[4]}=Bu\) is additive and \(\mathbb F_4\)-linear. Its nonzero solutions modulo \(\mathbb F_4^\times\) form the projective candidates. The accompanying exact verifier constructs the full kernel by binary linear algebra over an explicitly specified extension field \(\mathbb F_{2^n}\), with \(n\) twice the order of \(B\). This gives a kernel of exactly \(256\) vectors for every representative, i.e., \(85\) candidate projective points. Evaluating \(F_A\) on all candidates gives exactly \(45\) actual Eckardt points, in agreement with the geometric count for a smooth characteristic-two Hermitian cubic. Squaring their normalized coordinates yields the Frobenius permutation and the Eckardt cycle column.

For two distinct Eckardt points \(u,v\), the line they span lies on \(S_A\) if and only if both mixed cubic coefficients vanish:
\[u^{[2]\mathsf T}Av=0,\qquad v^{[2]\mathsf T}Au=0.\]
Every resulting geometric line contains exactly five of the computed Eckardt points; exhaustive pair testing yields exactly \(27\) distinct five-point subsets. Applying coordinate-wise squaring to those subsets produces precisely the line cycles displayed. Finally, a breadth-first congruence-orbit enumeration among all \(2^{16}\) binary matrices of rank four, using adjacent basis swaps and an elementary basis addition, partitions the \(20160\) invertible matrices into exactly the ten representative orbits with the displayed sizes. Thus the table exhausts the specified family and determines every extension-field rational count and both complete zeta functions.

## Verification

`verify_cubic_spectra.py` is a standalone Python standard-library checker for the binary matrix enumeration, all ten extension-field kernels, the selection of forty-five star points, all twenty-seven lines, both Frobenius cycle decompositions and orbit sizes. Run `python verify_cubic_spectra.py`; expected final text: `TEN_BINARY_EXTREMAL_CUBIC_FROBENIUS_SPECTRA_VERIFIED`. The independent direct finite-field check `verify_small_fields.py` brute-forces every projective \(\mathbb F_{2^n}\)-point for \(1\le n\le5\) and verifies the predicted Eckardt fixed-point counts in all ten cases. Run `python verify_small_fields.py`; expected final text: `DIRECT_FROBENIUS_STAR_POINT_ENUMERATION_VERIFIED`. Both have been executed against the distributed source files, not a prior log.

## Relationship to prior work

Kadyrsizova et al., *Cubic Surfaces of Characteristic Two* (2020), provide the Frobenius form and smoothness framework. Brosowsky–Page–Ryan–Smith, *Geometry of Smooth Extremal Surfaces* (2021), give the Hermitian geometry and star-point count. Karaoğlu, *Nonsingular Cubic Surfaces over finite fields of characteristic two* (2021), already tabulates numerous rational line and Eckardt-point counts for finitely many extensions and the classification of the small-field cubic surfaces; those prior results are not claimed as new here. Betten–Karaoğlu (2022) provides broader Eckardt-configuration parametrizations. The additional classification here distinguishes the complete cycle types and gives both zeta functions over *all* extensions for each of the ten Frobenius-form classes. The exact pair with equal Eckardt zeta but unequal line zeta is a consequence of the joint table, not an assertion of novel existence of nonisomorphic cubic surfaces.

## Limitations

Historical priority is qualified: a full-text comparison with Betten–Karaoğlu (2022) was unavailable; abstract-level comparison cannot exclude an unpublished or unindexed equivalent orbit table. Karaoğlu's online finite-field data and appendices may contain related explicit computations. This is a complete finite calculation with executable certificates, not a general theorem for arbitrary smooth cubic surfaces or a scheme-theoretic nonreduced analysis. No independent external mathematical audit has been performed.

## References

1. Kadyrsizova et al., *Cubic Surfaces of Characteristic Two* (2020), https://arxiv.org/abs/2007.12018 (first public 2020-07-23).
2. Brosowsky, Page, Ryan, Smith, *Geometry of Smooth Extremal Surfaces* (2021), https://arxiv.org/abs/2110.15908.
3. F. Karaoğlu, *Nonsingular cubic surfaces over finite fields of characteristic two* (2021), Turkish Journal of Mathematics 45, 2492–2510, https://doi.org/10.3906/mat-2102-10.
4. A. Betten and F. Karaoğlu, *The Eckardt Point Configuration of Cubic Surfaces Revisited* (2022), Designs, Codes and Cryptography 90, 2159–2180, https://doi.org/10.1007/s10623-021-00999-w.
