# Exact split-quadric genus-four census over \(\mathbf F_2\)

## Finding
Let \(S=\mathbf P^1_{\mathbf F_2}\times\mathbf P^1_{\mathbf F_2}\), and let \(V=H^0(S,\mathcal O_S(3,3))\). Exactly **16,020** of the \(2^{16}-1=65,535\) nonzero binary sections define geometrically smooth curves. They fall into **252** orbits under the full 72-element \(\mathbf F_2\)-automorphism group of the split quadric. By the canonical genus-four embedding and uniqueness of its containing quadric, these orbits are precisely the \(\mathbf F_2\)-isomorphism classes of smooth genus-four curves whose canonical quadric is split and smooth.

The exact joint distribution by number \(r\) of rational points is as follows. The first column counts sections, not equally weighted abstract curves.

| \(r\) | Sections | Isomorphism classes |
|---:|---:|---:|
| 0 | 84 | 3 |
| 1 | 846 | 14 |
| 2 | 2,232 | 34 |
| 3 | 3,438 | 55 |
| 4 | 3,924 | 57 |
| 5 | 3,150 | 49 |
| 6 | 1,752 | 28 |
| 7 | 558 | 11 |
| 8 | 36 | 1 |
| **Total** | **16,020** | **252** |

There are exactly **25** equivalence types of rational-point subsets of the \(3\)-by-\(3\) grid actually realized by smooth sections. Their 25 complete equation-level counts and representatives are reproduced in `artifacts/census_output.txt` and `artifacts/stats.txt`; the orbit representatives of curves are in `artifacts/orbit_representatives.tsv`. The 252 isomorphism classes have automorphism-group orders distributed as follows: 199 of order one, 40 of order two, seven of order three, three of order four, two of order six, and one of order twelve (for the automorphisms preserving the canonical split quadric). The 36 maximal-eight-point equations form a single orbit with stabilizer order two. The already-known genus-four upper bound of eight rational points is **not** asserted as new.

## Assumptions and scope
Write \([X_0:X_1]\) and \([Y_0:Y_1]\) for homogeneous coordinates on the two factors. Coefficient mask \(m\), an integer between \(1\) and \(65,535\), represents the section
\[
F_m=\sum_{i,j=0}^3 \epsilon_{ij} X_0^{3-i}X_1^iY_0^{3-j}Y_1^j,\qquad \epsilon_{ij}=\left\lfloor\frac{m}{2^{4i+j}}\right\rfloor\bmod 2.
\]
Geometric smoothness means nonsingularity at **every** point over an algebraic closure of \(\mathbf F_2\); finite-extension tests alone are not used as certificates of smoothness. Each smooth member has genus \((3-1)(3-1)=4\), and adjunction gives its canonical sheaf \(\mathcal O_S(1,1)|_C\). The acting group is \((\operatorname{PGL}_2(\mathbf F_2)\times\operatorname{PGL}_2(\mathbf F_2))\rtimes C_2\), with the involution exchanging the factors.

## Proof
**Step 1 (exhaustive negative filter).** In each field \(\mathbf F_{2^k}\), for \(1\le k\le6\), and at every point of \(\mathbf P^1(\mathbf F_{2^k})\times\mathbf P^1(\mathbf F_{2^k})\), the conditions \(F_m=\partial_u F_m=\partial_v F_m=0\) give explicit binary linear equations in the 16 coefficients. The script `artifacts/sieve.py` computes their kernels by exact binary elimination, verifies all returned kernel basis vectors satisfy every original equation, and flags the union of all coefficient kernels. It flags **49,515 distinct nonzero masks**, each with a genuine singularity witness in one of those fields. Their exclusion is sound without assuming any bound on the degree of a geometric singular point. The unflagged set has **16,020** masks.

**Step 2 (positive certificate).** `artifacts/census.py` constructs all 72 coordinate transformations, checks that the 16,020 survivors are invariant under every transformation, and partitions them into **252** exact group orbits. For every orbit representative, `artifacts/verify.py` performs an exact Gröbner-basis test of the Jacobian ideal \((f,\partial_u f,\partial_v f)\) on **all four** standard affine charts. Each of the 252 ideals on each chart is the unit ideal. By the affine Jacobian criterion over the algebraic closure, all representatives are geometrically smooth. Projective automorphisms preserve smoothness, so every survivor is smooth. Together, Steps 1 and 2 prove completeness.

**Step 3 (arithmetic and classification).** Evaluating each of the 16,020 sections at the nine rational grid points gives the displayed nine-bin table. Taking orbit representatives under the 72-element group gives the 252 isomorphism classes and stabilizer distribution. Applying the same group to nine-bit rational-point incidence masks gives the 25 pattern classes; the explicit incidence-pattern table is emitted by `artifacts/census.py`. A smooth \((3,3)\)-curve is canonically embedded under the Segre map because \(K_C=\mathcal O_C(1,1)\). The containing quadric is unique for a nonhyperelliptic canonical genus-four curve, so an abstract \(\mathbf F_2\)-isomorphism between any two members extends to a projective automorphism preserving the split quadric. Consequently the group-orbit census is also an isomorphism-class census.

## Verification
Run `python3 artifacts/sieve.py`, then `python3 artifacts/census.py`, then `python3 artifacts/verify.py` from the package root; the first two scripts use only Python's standard library, while the positive geometric smoothness checker needs SymPy. Each script reads/writes data relative to its own directory. Representative lists and saved outputs are in `artifacts/`. These commands executed successfully; the embedded output text was reproduced. Reproduction must evaluate all four charts and must not mistake absence of rational singularities for geometric smoothness.

## Relationship to prior work
Faber and Grantham, *Binary curves of small fixed genus and gonality with many rational points*, arXiv:2005.07054 (first posted 2020-05-14), prove the maximum \(N_2(4,3)=8\) and exhibit a genus-four trigonal curve attaining it. Their Section 5 classifies which quadrics can contain canonical genus-four curves, but does not state the equation-level 16,020 count, the 252 split-quadric isomorphism classes, or the nine-bin and 25-pattern spectra. Faber, Grantham and Howe, *On the Maximum Gonality of a Curve over a Finite Field*, arXiv:2207.14307 (first posted 2022-07-28), settle maximal gonality exceptions, not this split-quadric incidence census. Asgarli and Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169 (first posted 2022-03-14), motivates precise geometric smoothness conditions over small fields but considers a different class of linear systems. See `REVIEW.md` and `AUDIT.json` for novelty comparisons and limitations.

## Limitations
This is a complete classification only for canonical genus-four curves on the **split smooth quadric** over \(\mathbf F_2\), not for all genus-four curves. It excludes smooth non-split quadrics, quadric cones, and hyperelliptic curves. The 25 incidence-pattern counts are counts of equations on one fixed Segre surface, not frequencies of unweighted isomorphism classes. The group orders are relative to the canonical split model (and therefore give abstract automorphism orders in this setting); an independent external audit has not been performed. A previously unindexed exhaustive census of the same fixed family could preempt priority.

## References
1. X. Faber and J. Grantham, *Binary Curves of Small Fixed Genus and Gonality with Many Rational Points*, arXiv:2005.07054, 2020, §5, especially Theorem 5.2. https://arxiv.org/abs/2005.07054
2. X. Faber, J. Grantham and E. W. Howe, *On the Maximum Gonality of a Curve over a Finite Field*, arXiv:2207.14307, 2022. https://arxiv.org/html/2207.14307v2
3. S. Asgarli and D. Ghioca, *Smoothness in Pencils of Hypersurfaces over Finite Fields*, arXiv:2203.07169, 2022. https://arxiv.org/abs/2203.07169
