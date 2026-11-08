# Exact center-retention polynomial for vertex-thinned four-cubes

## Finding

Let \(V=\{-1,1\}^4\), and independently retain each of the sixteen vertices with probability \(p\in[0,1]\). Write \(S_p\) for the retained set and \(Q_p=\operatorname{conv}(S_p)\). For an empty retained set, let the event \(0\in Q_p\) be false. Define
\[
(a_0,a_1,\ldots,a_{16})=(1,16,112,448,1096,1584,1312,576,104,0,0,0,0,0,0,0,0).
\]
Then the **exact center-containment reliability polynomial** is
\[
\boxed{\Pr(0\in Q_p)=1-\sum_{k=0}^{8}a_kp^k(1-p)^{16-k}.}
\]
Equivalently, among all \(\binom{16}{k}\) size-\(k\) vertex subsets, exactly \(a_k\) have convex hull *avoiding* the center, for every \(0\le k\le16\). In particular,
\[
\Pr(0\in Q_{1/2})=\frac{60287}{65536},\qquad
\Pr(0\in\operatorname{conv}(S)\mid |S|=8)=\frac{6383}{6435}.
\]
The second probability refers to a uniformly chosen eight-vertex subset. Every subset of at least nine vertices contains the center in its convex hull.

A compact supporting structural census is that the inclusion-minimal nonempty subsets \(C\subseteq V\) with \(0\in\operatorname{conv}(C)\) number exactly 48: eight have two vertices, twenty-four have four, and sixteen have five. No other cardinalities occur. This census gives a second, exact finite proof of the entire polynomial.

## Assumptions and scope

All geometry is Euclidean in \(\mathbb R^4\). The cube is centered and has vertex set \(V\), not a continuously sampled vertex distribution. The retained points are independent Bernoulli choices with a common \(p\). Containment is non-strict: the center may lie on a proper face of the sampled hull. The result is exact for every \(p\in[0,1]\), including the endpoints, and is unchanged by invertible affine transformations of the cube and its center.

Write \(\binom{16}{k}=0\) outside \(0\le k\le16\). The numbers \(a_k\) count center-avoiding subsets rather than maximal separating subsets; the latter are a different classical object.

## Proof

**1. Separation and antipodal transversals.** For a nonempty subset \(S\subseteq V\), the strict separation theorem for a compact convex set gives
\[
0\notin\operatorname{conv}(S)
\quad\Longleftrightarrow\quad
\exists w\in\mathbb R^4\ \forall v\in S:\ \langle w,v\rangle>0.
\]
Perturb \(w\) slightly, preserving its strict positive inequalities on \(S\), so none of the sixteen cube vertices has zero dot product with \(w\). Exactly one vertex from each of the eight antipodal pairs then has positive dot product. Consequently every center-avoiding subset is contained in one of the eight-element *positive transversals* arising from such normals. Conversely, every subset of a positive transversal avoids the center. The empty set is counted as avoiding by convention.

Choose antipodal representatives \(v_{xyz}=(1,x,y,z)\) with \(x,y,z\in\{-1,1\}\). The positive transversals are exactly the sign patterns of the eight linear values \(\langle w,v_{xyz}\rangle\). These are the classical three-variable linear-threshold sign patterns. Their known total, 104, is **not** claimed as new.

**2. Exhaustive determination of the 104 relevant transversals.** The accompanying exact checker finds the signed circuits of the eight representative vectors by rational row reduction on all subsets of sizes two through five. It finds precisely 20 circuits: twelve supported on four representatives and eight on five. If a proposed eight-sign pattern agrees, on an entire circuit support, with either orientation of its unique linear dependence, strict positivity is impossible. Exactly 104 of the 256 patterns survive this obstruction. Independently and constructively, the checker enumerates integer normals \(w\in\{-2,-1,0,1,2\}^4\), and finds **exactly these same 104 patterns**, each attained with all eight dot products nonzero. Hence the twenty circuit obstructions and the displayed small integer witnesses rigorously exhaust the continuum of possible normal directions.

**3. Counting the down-closures.** Encode each of the sixteen vertices by one bit. A mask avoids the center precisely when it is contained in at least one of the 104 positive-transversal masks. Direct exhaustive integer enumeration of the \(2^{16}\) masks, grouped by cardinality, yields
\[
\begin{array}{c|rrrrrrrrr}
k&0&1&2&3&4&5&6&7&8\\\hline
a_k&1&16&112&448&1096&1584&1312&576&104.
\end{array}
\]
No nine-element subset can be contained in an eight-element transversal, so \(a_k=0\) for all \(k\ge9\). A given \(k\)-vertex subset has selection probability \(p^k(1-p)^{16-k}\). Summing over avoiding subsets and taking the complement proves the reliability polynomial and both displayed probabilities.

**4. Independent exact certificate from positive dependencies.** There is a second proof that does not generate positive transversals. By Carathéodory's theorem, if \(0\in\operatorname{conv}(S)\), then this holds for some subset of size at most five. Every *inclusion-minimal* such subset carries a unique linear dependence, all of whose coefficients are strictly positive (up to common scaling). Conversely, every such dependence witnesses inclusion of the center. Rational row reduction on all vertex subsets of sizes two through five finds precisely 8, 0, 24, 16 such minimal positive dependencies at cardinalities two, three, four, five. The independently enumerated \(2^{16}\) masks that contain at least one of these 48 supports have cardinality histogram
\[
(0,0,8,112,724,2784,6696,10864,12766,11440,8008,4368,1820,560,120,16,1).
\]
Subtracting from \(\binom{16}{k}\) yields exactly the \(a_k\) above. All computations are over rational numbers or integers, not floating point. The attached `verify_cube_center.py` is a complete standalone finite certificate for both routes.

## Verification

Run `python3 verify_cube_center.py` (Python 3 standard library only). It checks: all signed linear dependencies by exact rational elimination; twenty obstructing circuits on antipodal representatives; realization of all 104 allowed sign patterns by bounded integer normals; eight/twenty-four/sixteen minimal positive supports; both independent complete subset histograms; the reliability coefficients and exact probabilities. Its final success line is `CUBE4_EXACT_RELIABILITY_TWO_CERTIFICATES_PASSED`.

The finite enumeration is logically exhaustive because (i) strict separation reduces all potential avoiding sets to eight-element sign patterns and (ii) Carathéodory bounds the size of every minimal center-containing support by five. Thus there is no extrapolation from a finite experiment to an unbounded domain: the relevant domain itself is finite and fully tested with exact arithmetic. The rational linear-dependence routine and both enumeration loops are included in full.

## Relationship to prior work

Newman (2020) considers vertex thinning of polytopes and related random polytope models, motivating the retention observable; his published analysis emphasizes geometric approximation, facet growth and the complexity of randomly generated ambient polytopes, not this exact center-retention polynomial for a fixed Boolean cube. Dyer, Füredi and McDiarmid (1992) investigate expected volume of high-dimensional random Boolean polytopes, a different observable.

Classical threshold-logic literature already supplies the number 104 of three-variable threshold functions. Emamy and Meléndez Ríos (2024) study cut-complexes and a classification of separable four-cube vertex sets. Their published geometric classification is closely related, and the 104 count is explicitly acknowledged as prior. The precise **cardinality-resolved down-closure of these transversals**, equivalently the center-containment reliability polynomial and 48 minimal positive-support certificate, is the claimed result here, not the known threshold-function count or a new general separation theorem.

The structural comparison is important: a count of maximal separable transversals alone does not determine how their subfamilies overlap. The present polynomial measures the union of those down-closures, which requires a separate exact combinatorial analysis. Likewise, a result on random central hyperplane *sections* of a four-cube does not answer a center-containment problem for random *vertex subsets*.

## Limitations

The coefficient formula concerns dimension four only. It does not establish an analogous closed formula for arbitrary dimension, a sharp high-dimensional probabilistic threshold, or the probability that the center belongs to the interior of the sampled hull. The statement is non-strict containment. The exact enumeration is independently reproducible but has not undergone independent mathematical audit. Older cut-complex and partial-threshold-function enumeration literature could encode an equivalent cardinality distribution; historical priority is provisional. The complete 2011 cut-complex article was not available for full-text comparison; the accessible 2024 treatment was inspected in the relevant sections.

## References

1. A. Newman, *Doubly random polytopes*, arXiv:2006.07000v1, first public 12 June 2020, https://arxiv.org/abs/2006.07000; *Random Structures & Algorithms* 61 (2022), 364–382, doi:10.1002/rsa.21059.
2. M. E. Dyer, Z. Füredi, C. McDiarmid, *Volumes Spanned by Random Points in the Hypercube*, *Random Structures & Algorithms* 3 (1992), 91–106, doi:10.1002/rsa.3240030107.
3. M. R. Emamy-Khansary, *A geometric connection to threshold logic via cubical lattices*, *Annals of Operations Research* 188 (2011), 141–153, doi:10.1007/s10479-009-0593-5 (accessible abstract only).
4. M. R. Emamy-Khansary and G. A. Meléndez Ríos, *On a Convex Geometric Connection to Threshold Logic*, 2024, doi:10.1007/978-3-031-52969-6_9 (relevant Sections 6–7 inspected in the accessible author manuscript).
5. OEIS A000609, *Number of threshold functions of \(n\) or fewer variables*, https://oeis.org/A000609 (the classical 104 value).
