# Sharp three-cycle coexistence and complete fourth-return census in a border-collision map

## Finding
Consider the two-piece planar border-collision normal form in the next section. Throughout the class of such maps, there are **at most three isolated primitive period-four cycles whose four points all lie strictly away from the switching line**. This bound is attained robustly in the mixed non-invertible, two-saddle parameter regime.

At the exact parameters
\[
(\tau_L,\delta_L,\tau_R,\delta_R)
=\left(1,-\frac74,-\frac74,\frac35\right),
\]
the fourth iterate has **exactly sixteen fixed points** in the entire real plane. Two are fixed points, two belong to one primitive two-cycle, and the other twelve belong to **exactly three primitive four-cycles**. The three strict four-cycle itineraries are \(LLLR\), \(LLRR\), and \(LRRR\). The \(LRRR\) cycle is a hyperbolic attractor, and the other two are hyperbolic saddles, with respectively a negative and a positive expanding multiplier. The entire exact census and these stability types persist on a nonempty open neighborhood of the specified four-dimensional parameter point.

## Assumptions and scope
Let \(F:\mathbb R^2\to\mathbb R^2\) be
\[
F(x,y)=\begin{cases}
(\tau_L x+y+1,-\delta_L x),&x\leq0,\\
(\tau_R x+y+1,-\delta_R x),&x\geq0.
\end{cases}
\]
The formulas coincide when \(x=0\); thus \(F\) is continuous and single-valued. The general isolated-orbit upper bound holds for all real values of the four parameters. It counts only four-cycles with **strict itineraries**, meaning every point has nonzero first coordinate. An *isolated* four-cycle means each of its points is isolated in \(\operatorname{Fix}(F^4)\). The exact complete census and open-neighborhood assertion are for the displayed rational parameter choice.

For comparison with the originating dynamical regime, the two-saddle domain is
\[
\tau_L>|1+\delta_L|,\qquad \tau_R<-|1+\delta_R|,
\qquad \delta_L<0<\delta_R.
\]
Our parameters lie strictly inside this domain: \(1>3/4\) and \(-7/4<-8/5\). The word of an orbit records the signs of successive first coordinates, with \(L\) negative and \(R\) positive.

## Proof
**1. The universal isolated-orbit bound.** Set
\[
A_L=\begin{pmatrix}\tau_L&1\\-\delta_L&0\end{pmatrix},\quad
A_R=\begin{pmatrix}\tau_R&1\\-\delta_R&0\end{pmatrix},\quad b=\binom10.
\]
For each length-four word \(w=w_0w_1w_2w_3\), the fourth iterate on the open set of points realizing the strict word is affine:
\[
F^4(z)=M_w z+c_w,\quad
M_w=A_{w_3}A_{w_2}A_{w_1}A_{w_0},\quad
c_w=\sum_{j=0}^{3}A_{w_3}\cdots A_{w_{j+1}}b,
\]
where an empty product is the identity. The equation \((I-M_w)z=c_w\) has at most one **isolated** solution: if the matrix is singular, any solution lies in an affine space of positive dimension, and the strict itinerary holds on a neighborhood.

If a strict primitive period-four point had a symbolic word of smaller cyclic period \(d\in\{1,2\}\), let \(T\) be the affine return for the repeating \(d\)-letter block. Locally, its fourth return equals \(T^{4/d}\). A periodic point with \(T^{4/d}(z)=z\) but \(T(z)\ne z\) forces \(I-D(T^{4/d})\) to be singular: otherwise the affine equation would have a unique solution, which must be fixed by \(T\), since \(T\) commutes with its own iterate. Hence such a point cannot be isolated. It follows that an isolated strict primitive four-cycle must have an **aperiodic length-four binary necklace**. There are exactly three such necklaces, represented by \(LLLR\), \(LLRR\), and \(LRRR\); cyclic rotations name the same orbit. Since each word supports at most one isolated fixed point, at most three such cycles exist.

**2. Exact parameter witness and complete census.** At the asserted rational parameters,
\[
A_L=\begin{pmatrix}1&1\\7/4&0\end{pmatrix},\qquad
A_R=\begin{pmatrix}-7/4&1\\-3/5&0\end{pmatrix}.
\]
For each of the six length-four necklaces, direct rational solution of \((I-M_w)z=c_w\) gives the following first coordinate of the initial point and nonzero return determinant. The table's stated least periods follow by exact substitution.

| Representative word | Initial \(x\) coordinate | \(\det(I-M_w)\) | Least period |
|---|---:|---:|---:|
| `LLLL` | \(-4/7\) | \(-959/256\) | 1 |
| `RRRR` | \(20/67\) | \(-259089/160000\) | 1 |
| `LRLR` | \(-3/11\) | \(-143/400\) | 2 |
| `LLLR` | \(-440/799\) | \(799/320\) | 4 |
| `LLRR` | \(-1348/2571\) | \(-2571/1600\) | 4 |
| `LRRR` | \(-3867/8396\) | \(2099/2000\) | 4 |

For direct transparency, the successive first coordinates of the three primitive four-cycles are respectively
\[
\begin{aligned}
LLLR:&\quad (-440,-52,-23,685)/799,\\
LLRR:&\quad (-1348,-97,115,2200)/2571,\\
LRRR:&\quad (-3867/8396,485/8396,195/2099,1685/2099).
\end{aligned}
\]
Each tuple has exactly the signs specified by its word. The other three representatives similarly have their required strict signs, as verified directly by their period-one and period-two solutions. Cyclic rotation supplies the remaining ten words. Because all branch matrices here are nonsingular, cyclically rotated return products have the same nonzero determinant \(\det(I-M_w)\). Thus all sixteen words yield exactly one strict solution each. No solutions can lie on the switching line: any such solution could be assigned an arbitrary side at each zero coordinate (the affine formulas agree there), forcing it to equal one of the already enumerated strict candidates. Hence \(\#\operatorname{Fix}(F^4)=16\), consisting of two period-one points, two period-two points, and twelve least-period-four points.

**3. Exact stability and persistence.** For the three primitive four-cycle return matrices, rational multiplication gives
\[
\begin{array}{c|ccc}
 w&\operatorname{tr}M_w&\det M_w&\det(I+M_w)\\\hline
 LLLR&-377/80&-1029/320&-2217/320\\
 LLRR&1187/320&441/400&9299/1600\\
 LRRR&-171/400&-189/500&389/2000
\end{array}
\]
For \(LLLR\), \(\det(I+M_w)<0\) and \(\det M_w<0\), so one real multiplier is below \(-1\) and the other is strictly between \(0\) and \(1\). For \(LLRR\), \(\det(I-M_w)<0\), positive trace, and positive determinant show that one real multiplier exceeds \(1\) and the other is strictly between \(0\) and \(1\). For \(LRRR\), the exact Schur conditions are
\[
\det(I-M_w)=2099/2000>0,\quad
\det(I+M_w)=389/2000>0,\quad
1-\det M_w=689/500>0,
\]
so both multipliers lie strictly inside the unit disk. This establishes two saddles and one attracting four-cycle, all hyperbolic.

Each of the sixteen word solutions varies continuously (in fact rationally) with parameters near the witness because its determinant stays nonzero; all sixteen strict sign inequalities persist. All three return stability classifications also persist. The same sixteen-word exhaustion proves the unchanged total census on some nonempty open four-parameter neighborhood, still within the mixed non-invertible two-saddle domain. No numerical continuation or unproved genericity assumption is needed.

## Verification
The standalone `verify_coexistence.py` uses only Python's exact `fractions.Fraction` arithmetic. It enumerates **all sixteen words**, recomputes every fourth-return affine solution, verifies strict branch inequalities and periodicity, checks pairwise distinctness and the \(2,2,12\) least-period point partition, checks the six necklace representatives and their nonzero return determinants, and reproduces all three stability certificates. Execute `python verify_coexistence.py`. A complete run prints `EXACT_16_WORD_CENSUS_OK`, `PERIODS_2_2_12_OK`, and `MONODROMY_AND_HYPERBOLICITY_OK`. The upper bound and parameter-open persistence follow from the mathematical arguments above; the finite checker alone is not an all-parameter proof.

## Relationship to prior work
Ghosh, McLachlan and Simpson (2024), arXiv:2402.05393v1, §9, identify a stable \(LRRR\) four-cycle parameter region in this same non-invertible two-saddle configuration. They do not state the exact simultaneous \(LLLR\), \(LLRR\), \(LRRR\) census at the present parameters or the sharp three-necklace upper bound. Their earlier work on robust chaos (2023) concerns trapping regions and invariant expanding cones rather than this complete fourth-return census. Fatoyinbo and Simpson (2022) survey the non-invertible normal form and low-period bifurcations but do not give this all-word rational witness.

A separately published result, *No attracting three-left one-right four-cycle in the non-invertible two-saddle border-collision map*, proves a global **stability obstruction for \(LLLR\)** and exhibits a stable \(LRRR\) witness. It does not imply that all three primitive four-cycle necklaces coexist, and it does not supply the present simultaneous complete exact census. The proof here is consistent with that obstruction: the \(LLLR\) cycle is a saddle. Searches for synonyms such as strict symbolic cycles, binary necklaces, monodromy, and border-collision itinerary coexistence identified no stronger covering statement in the material inspected. Search absence is not proof of first discovery.

## Limitations
The universal upper bound counts **isolated** primitive four-cycles with strict itineraries. It does not bound nonisolated families or all possible switching-line cycles at arbitrary parameters. At the explicit rational parameters and throughout a neighborhood, the census is complete even for points on the switching line (there are none among the fourth-return fixed points). The result says nothing about higher periods, global attractors, chaos, or orbit basins beyond the locally attracting \(LRRR\) cycle. Equivalent statements may exist in literature not located by the searches; independent mathematical and priority audits have not been performed.

## References
1. I. Ghosh, R. I. McLachlan and D. J. W. Simpson, *The bifurcation structure within robust chaos for two-dimensional piecewise-linear maps*, arXiv:2402.05393v1, first publicly posted 2024-02-08, especially §9. https://arxiv.org/html/2402.05393v1
2. I. Ghosh, R. I. McLachlan and D. J. W. Simpson, *Robust chaos in orientation-reversing and non-invertible two-dimensional piecewise-linear maps*, arXiv:2307.05144v1, 2023-07-11. https://arxiv.org/abs/2307.05144
3. H. O. Fatoyinbo and D. J. W. Simpson, *A synopsis of the non-invertible, two-dimensional, border-collision normal form with applications to power converters*, arXiv:2210.14445v1, 2022-10-26. https://arxiv.org/abs/2210.14445
4. *No attracting three-left one-right four-cycle in the non-invertible two-saddle border-collision map*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-no-attracting-three-left-one-right-four-cycle-in-the-non-inverti--829828b41a37
