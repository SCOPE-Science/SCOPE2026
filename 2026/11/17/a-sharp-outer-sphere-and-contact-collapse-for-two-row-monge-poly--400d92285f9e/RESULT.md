# A sharp outer-sphere and contact collapse for two-row Monge polytopes

## Finding

For an integer \(q\ge2\), let \(\mathcal M_{2,q}\) be the polytope of nonnegative real \(2\times q\) arrays \(x=(a_1,\ldots,a_q;b_1,\ldots,b_q)\) satisfying
\[
\sum_{j=1}^q(a_j+b_j)=1,\qquad a_j+b_{j+1}\le a_{j+1}+b_j\quad(1\le j<q).
\]
Distances are Frobenius/ambient Euclidean distances on these \(2q\) coordinates. Then its **unique smallest enclosing Euclidean ball** has squared radius
\[
\boxed{R_q^2=\frac{5q-6}{8(q-1)}}
\]
and center \(c\) specified by
\[
a_1(c)=b_q(c)=0,\quad a_q(c)=b_1(c)=\frac{q}{4(q-1)},\quad a_j(c)=b_j(c)=\frac1{4(q-1)}\ (2\le j\le q-1).
\]
For \(q=2\), all six vertices touch its sphere. For every \(q\ge3\), **exactly \(q\) vertices touch**: the singleton at the final position of the top row, the singleton at the initial position of the bottom row, and the \(q-2\) arrays with entries \(1/2\) in both rows at one interior column. No other points of the polytope touch. The polytope has Euclidean diameter \(\sqrt2\) and one unordered diametral vertex pair. In particular, \(R_q/\operatorname{diam}(\mathcal M_{2,q})\to\sqrt5/4\).

## Assumptions and scope

The inequalities use the ordinary, nonsymmetric Monge convention. The affine dimension is \(2q-1\), and all radii are intrinsic to its sum-one affine span (equivalently ambient Euclidean radii, because the stated center lies in the span). This theorem concerns the smallest **ball**, not the minimum-volume ellipsoid and not the largest inscribed ball. All integer \(q\ge2\) are covered without asymptotic assumptions.

Let \(A_k\) have \(1/k\) in the last \(k\) positions of the first row and zero elsewhere; let \(B_k\) have \(1/k\) in the first \(k\) positions of the second row and zero elsewhere (\(1\le k\le q\)). Let \(C_j\) have \(1/2\) in both rows at column \(j\), zero elsewhere (\(1\le j\le q\)). All are members of \(\mathcal M_{2,q}\).

## Proof

**1. Complete vertex description.** Put \(y_j=a_j-b_j\). The Monge condition is \(y_1\le\cdots\le y_q\). Write
\[
a_j=t_j+y_j^+,\qquad b_j=t_j+y_j^-,\qquad t_j=\min(a_j,b_j)\ge0,
\]
where \(y_j^+=\max(y_j,0)\) is nondecreasing and \(y_j^-=\max(-y_j,0)\) is nonincreasing. Every nonnegative nondecreasing sequence is a nonnegative linear combination of terminal-interval indicators, and every nonnegative nonincreasing sequence is a combination of initial-interval indicators. Hence every nonnegative Monge array is a nonnegative combination of the unnormalized forms of \(A_k,B_k,C_j\). Normalize by total entry sum to obtain
\[
\mathcal M_{2,q}=\operatorname{conv}\{A_1,\ldots,A_q,B_1,\ldots,B_q,C_1,\ldots,C_q\}.
\]
Each generator is extreme: a nonnegative combination supported in just one row on an exact terminal (respectively initial) interval can use only its corresponding ray; a combination supported in both rows of one column can use no nonzero terminal-first-row and initial-second-row rays simultaneously when \(q\ge2\), so it can only use that column's \(C_j\) ray. Thus these \(3q\) generators are exactly the vertices. An all-positive matrix with strictly increasing row differences shows full dimension in the sum-one affine hyperplane.

**2. Candidate center and exact distances.** Let \(c\) be as in the theorem. Its squared norm is
\[
\|c\|_2^2=\frac{q+2}{8(q-1)}.
\]
Direct dot products give
\[
\|A_1-c\|_2^2=\|B_1-c\|_2^2=R_q^2.
\]
For all remaining row-block vertices, by the symmetry exchanging the two rows and reversing the columns,
\[
R_q^2-\|A_k-c\|_2^2=R_q^2-\|B_k-c\|_2^2=
\begin{cases}
\dfrac{k-1}{2k},&2\le k<q,\\
\dfrac{q-2}{2(q-1)},&k=q.
\end{cases}
\]
For the column vertices,
\[
R_q^2-\|C_j-c\|_2^2=
\begin{cases}
\dfrac{q-2}{4(q-1)},&j=1\text{ or }j=q,\\
0,&2\le j\le q-1.
\end{cases}
\]
These are nonnegative for every \(q\ge2\). At \(q=2\), every gap vanishes; at \(q\ge3\), the zero-gap list is exactly \(A_1,B_1,C_2,\ldots,C_{q-1}\). By convexity of the squared distance, the proposed ball contains the whole convex hull. Since the squared norm is strictly convex, no nonvertex point of a face spanned by multiple distinct vertices at the same radius can touch: any strict convex combination of distinct points within the ball has squared norm from \(c\) strictly below \(R_q^2\).

**3. Optimality and uniqueness.** Set
\[
\alpha=\frac q{4(q-1)},\qquad\beta=\frac1{2(q-1)}.
\]
The center has the positive contact-vertex representation
\[
 c=\alpha A_1+\alpha B_1+\beta\sum_{j=2}^{q-1}C_j,
 \qquad 2\alpha+(q-2)\beta=1.
\]
The sum is empty when \(q=2\). For any alternative center \(z\in\mathbb R^{2q}\), the weighted squared-distance identity gives
\[
\sum_{v\in\{A_1,B_1,C_2,\ldots,C_{q-1}\}}\lambda_v\|v-z\|_2^2
=R_q^2+\|z-c\|_2^2,
\]
where the positive weights are \(\alpha,\alpha,\beta,\ldots,\beta\). Hence every ball enclosing these contacts, and therefore the polytope, has radius squared at least \(R_q^2+\|z-c\|_2^2\). The proposed ball is smallest and its center is unique.

**4. Diameter.** Every member of the polytope is a nonnegative sum-one vector, so its squared norm is at most one, and any pair has squared distance at most two. Equality requires two distinct coordinate unit vectors with disjoint support. Among the listed vertices, exactly \(A_1\) and \(B_1\) are unit coordinate vectors, proving the diameter and uniqueness of its vertex pair. Finally, dividing \(R_q^2\) by \(2\) and sending \(q\to\infty\) yields the stated limit.

## Verification

The standalone `VERIFY.py` uses only the Python standard library and exact rational arithmetic. It checks the center's contact convex combination, radius and all gap formulas for every \(2\le q\le32\), then independently enumerates vertices from the original defining inequalities (without using the proposed convex-hull decomposition) for \(q=2,3,4\). It reports **6,286 exact checks**, all passed. These finite tests are corroboration: the proof above establishes the assertions for all \(q\ge2\).

## Relationship to prior work

Erickson and Kretschmann (2023) describe the vertices, edges and facets of general normalized Monge polytopes; their vertex description is acknowledged here rather than claimed as new. Erickson and Jones (September 8, 2026) develop new formulas for Monge-polytope volume and Ehrhart series, motivating exact geometric invariants beyond counting and volume. Recent related calculations treat Euclidean **inradii**, centroids and directional mean widths of Monge polytopes. Those are different optimization problems: an inball maximizes a contained ball, a centroid is a volume mean, and a mean width averages support over directions; none supplies the outer-sphere formula and complete contact classification by direct statement. Historical priority remains provisional because relevant complete manuscripts could not all be examined.

## Limitations

The result covers only the two-row normalized nonsymmetric Monge family with its canonical coordinate metric. It makes no assertion about smallest enclosing ellipsoids, higher row counts, or affine-invariant optimality. The motivating 2026 and 2023 manuscripts were identifiable and their abstracts and bibliographic descriptions were checked, but complete text could not be obtained through the available arXiv/open-access routes; an equivalent theorem hidden in their full text or older literature cannot be ruled out. No independent mathematical validation is claimed.

## References

1. W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522 (first public November 13, 2023), https://arxiv.org/abs/2311.07522.
2. W. Q. Erickson and N. B. Jones, *A lattice path model for the volume of the Monge polytope*, arXiv:2609.09508 (first public September 8, 2026), https://arxiv.org/abs/2609.09508.
