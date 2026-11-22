# The first finite field for strict realizations of Schroeter configuration V

## Finding

Let \(\mathscr L_{\mathrm V}\) be the ten-triple incidence structure on the labeled set \(\{0,1,\ldots,9\}\) defined by
\[
\mathscr L_{\mathrm V}=\{124,138,179,237,259,350,456,480,678,690\}.
\]
Here, for example, \(124\) denotes \(\{1,2,4\}\). A **strict realization** over a field \(k\) is an ordered ten-tuple of distinct points in \(\mathbb P^2(k)\), whose collinear three-subsets are *exactly* the ten displayed triples. Projective equivalence means equivalence under \(\operatorname{PGL}_3(k)\) acting on the coordinates while preserving the labels.

**Theorem.** Among all finite fields, the least field cardinality for which a strict realization of \(\mathscr L_{\mathrm V}\) exists is \(7\). Over \(\mathbb F_7\), there is exactly **one** projective-equivalence class of labeled strict realizations. The numbers of such classes over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\) are respectively \(0,0,0,0,1\).

A representative of the unique \(\mathbb F_7\)-class has point coordinates (entries indexed in order from zero through nine):
\[
\begin{array}{c|cccccccccc}
i&0&1&2&3&4&5&6&7&8&9\\\hline
P_i&(1,1,5)&(1,0,0)&(0,1,0)&(0,0,1)&(1,3,0)&(1,1,1)&(1,5,6)&(0,1,6)&(1,0,4)&(1,6,1)
\end{array}
\]
with all coordinates interpreted modulo \(7\). The statement concerns these specific *strict* point configurations, not weak realizations that admit collisions or additional collinear triples.

## Assumptions and scope

A field is finite and has prime-power cardinality. The only cardinalities below \(7\) are \(2,3,4,5\), with \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\). The incidence structure is the labeled configuration \(\mathscr L_{\mathrm V}\) above, the same object studied by Sturmfels and Sink. Each projective transformation acts on all ten labeled points simultaneously. The incidence convention is the exact if-and-only-if condition, rather than only the ten required vanishing determinants.

## Proof

**1. Canonical frame.** No three among vertices \(1,2,3,5\) belong to one required triple. A strict realization therefore makes these four points a projective frame, with a unique projectivity sending them to
\[
P_1=(1,0,0),\quad P_2=(0,1,0),\quad P_3=(0,0,1),\quad P_5=(1,1,1).
\]
The incidence \(237\) forces \(P_7=(0,1,t)\) with \(t\ne0\); distinctness excludes \(P_2\) and \(P_3\). The incidence data forbid \(P_6\) from lying on the line \(P_2P_3\), so uniquely \(P_6=(1,a,b)\). The remaining four points are forced by intersection:
\[
\begin{aligned}
P_4&=(P_1P_2)\cap(P_5P_6),&
P_8&=(P_1P_3)\cap(P_6P_7),\\
P_9&=(P_1P_7)\cap(P_2P_5),&
P_0&=(P_3P_5)\cap(P_4P_8).
\end{aligned}
\]
Here \(AB\) denotes the projective line spanned by two points. The only remaining prescribed collinearity is \(P_0,P_6,P_9\). Hence the assignment \((a,b,t)\mapsto(P_0,\ldots,P_9)\), wherever defined and strict, parametrizes all projective classes **injectively and surjectively**.

**2. Single cubic equation.** Writing the final determinant condition in these coordinates gives
\[
\begin{aligned}
E(a,b,t)={}& b-tb-t^2a^3+ta^2b+t^2a^2\\
&-tab+tb^2-b^2=0.
\end{aligned}
\]
This is the affine chart of Sturmfels' bidegree-\((2,3)\) realization-surface equation, as displayed by Sink. The expression can also be obtained directly by taking cross products in the preceding four intersection rules. Nonzero intersections, pairwise distinctness and all \(\binom{10}{3}=120\) incidence determinants must still be checked: a point on the equation alone need not be a strict realization.

**3. Exhaustive finite certificate.** The attached standalone `CHECKER.py` implements exact finite-field arithmetic, including the irreducible quadratic model of \(\mathbb F_4\), and two independently organized enumerations: (i) all normalized projective pairs \((P_6,P_7)\) with \(P_7\in P_2P_3\), followed by construction and all 120 incidence checks; and (ii) all \(q^2(q-1)\) parameter triples \((a,b,t)\) tested against \(E\), followed by the distinctness and exact-incidence conditions. The two procedures agree on every surviving ordered configuration. Their fully exhausted counts are:

| \(q\) | Roots of \(E\) | Distinct constructed ten-tuples | Strict classes |
|---:|---:|---:|---:|
| 2 | 4 | 0 | 0 |
| 3 | 13 | 0 | 0 |
| 4 | 22 | 0 | 0 |
| 5 | 31 | 0 | 0 |
| 7 | 50 | 1 | 1 |

In particular, for the four smaller fields, every root of the necessary equation has a collision or undefined forced intersection. For cardinality \(7\), exactly one parameter survives distinctness, namely \((a,b,t)=(5,6,6)\), and its ten points have precisely the required ten collinear triples. Since all smaller prime powers were exhausted and the normalization has no residual projective stabilizer, the minimum and uniqueness follow. \(\square\)

## Verification

Execute `python3 CHECKER.py` in a directory containing the attached `CHECKER.py`. Its only dependency is the standard Python library. It writes `CENSUS.csv` and checks, by assertions, the exact five-row table and the unique ten-coordinate witness. The provided `CENSUS.csv` was produced by this checker. Independent projective-pair and polynomial-root enumeration agree. This is a finite exhaustive proof over the five listed finite fields, not an extrapolation from sampled random configurations.

## Relationship to prior work

Cohen and Liu (2022) investigate one-line extensions of all ten \((10_3)\) configurations over the complex numbers. Sink (2023 preprint, with later versions) provides the exact strict-realization definition, the \(\mathscr L_{\mathrm V}\) incidence list, the projective-frame construction, the surface equation and characteristic-zero K3 geometry. Isham et al. (2025) classify ten-point realization spaces birationally over characteristic zero and explicitly identify finite-field enumeration as a motivation whose general counts are not furnished by their birational results. The new assertion is the sharp **least finite-field order and uniqueness at that order for this specific strict realization moduli space**, neither an assertion about the K3 compactification in characteristic \(7\) nor a general classification of all ten configurations.

## Limitations

The census covers exactly the five finite-field orders up to \(7\); it does not compute realization counts for arbitrary larger \(q\). It does not assert smoothness or unchanged Picard lattice of the associated characteristic-zero K3 model after reduction. Strict point configurations are deliberately distinguished from weak incidence-variety points, which can be abundant even in smaller fields. An equivalent unpublished finite-matroid realization table is a residual priority risk. Independent mathematical validation has not been carried out.

## References

- M. Cohen and B. Liu, *Moduli Spaces of One-Line Extensions of \((10_3)\) Configurations*, arXiv:2208.12293, first submitted 2022-08-25, https://arxiv.org/abs/2208.12293.
- E. Sink, *Line configurations and K3 surfaces*, arXiv:2312.07542, https://arxiv.org/abs/2312.07542, especially Introduction and Section 2, equation (2.1).
- K. Isham, N. Kaplan, S. Kimport, R. Lawrence, L. Peilen, and M. Weinreich, *Configurations of 10 points and their incidence varieties*, arXiv:2507.09829, https://arxiv.org/abs/2507.09829, especially Sections 1 and 4.
- B. Sturmfels, *Computational algebraic geometry of projective configurations*, 1991; original construction cited in Sink, Section 2.
