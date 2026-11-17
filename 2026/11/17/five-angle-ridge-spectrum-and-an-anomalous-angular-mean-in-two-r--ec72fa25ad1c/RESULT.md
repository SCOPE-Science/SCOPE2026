# Five-angle ridge spectrum and an anomalous angular mean in two-row Monge polytopes

## Finding

For every integer \(q\ge2\), define the standard two-row normalized Monge polytope
\[
\mathcal M_q=\left\{(a,b)\in\mathbb R_{\ge0}^{2q}:\ \sum_{i=1}^q(a_i+b_i)=1,\quad a_i-b_i\le a_{i+1}-b_{i+1}\ (1\le i<q)\right\}.
\]
All distances and dihedral angles are intrinsic to its affine hyperplane, with the Euclidean metric inherited from \(\mathbb R^{2q}\). Let a ridge mean a face of dimension \(2q-3\), and count each ridge once. Put
\[
\alpha_q=\arccos\frac1{2q-1},\qquad
\beta_q=\arccos\sqrt{\frac{q}{2(2q-1)}}.
\]
The complete spectrum of **interior** dihedral angles, including multiplicities, is

| Interior angle | Exact number of ridges |
|:--|--:|
| \(\beta_q\) | \(2(q-1)\) |
| \(\pi/3\) | \(q-2\) |
| \(\alpha_q\) | \((3q^2-q)/2\) |
| \(\pi/2\) | \((q-2)(q-3)/2+2(q-1)(q-2)\) |
| \(\pi-\beta_q\) | \(2(q-1)\) |

Omit zero-multiplicity entries: three angle levels occur for \(q=2\), and five distinct levels for every \(q\ge3\). In particular,
\[
\boxed{\#\{\text{ridges of }\mathcal M_q\}=(2q-1)^2.}
\]
If \(\Theta_q\) is the interior dihedral angle of a uniformly selected ridge, then
\[
\boxed{\ q\left(\Theta_q-\frac\pi2\right)\ \Longrightarrow\ \frac58\delta_0+\frac38\delta_{-1/2}.\ }
\]
Nevertheless, the first moment has a distinct, sharp limit:
\[
\boxed{\lim_{q\to\infty}q\left(\mathbb E\Theta_q-\frac\pi2\right)=-\frac3{16}-\frac\pi{24},}
\]
whereas the limiting distribution has mean \(-3/16\). The extra negative contribution \(-\pi/24\) comes from the vanishing proportion of acute ridges between adjacent Monge-comparison facets. More precisely,
\[
\mathbb E\Theta_q=\frac\pi2-
\frac{(q-2)\pi/6+((3q^2-q)/2)\arcsin(1/(2q-1))}{(2q-1)^2}.
\]

## Assumptions and scope

The polytope has \(q\ge2\) columns, two rows, nonnegative real entries and exactly unit total entry sum. The order direction is nondecreasing for \(d_j=a_j-b_j\), as in the defining inequalities. The ambient metric is the *unweighted Frobenius* metric restricted to \(\sum(a_j+b_j)=1\). The stated spectrum is invariant under the appropriate row reversal but does not claim a formula for arbitrary row count or altered diagonal metrics. An interior dihedral angle is the supplement of the angle between outward unit facet normals in the intrinsic hyperplane. No probability distribution on points of the polytope is used; the random ridge is chosen uniformly among distinct codimension-two faces.

## Proof

**1. Facets and their inward/outward normals.** Write \(H=\{x\in\mathbb R^{2q}:\sum x_i=1\}\), and let \(\mathbf1\) be the ambient all-ones vector. The irredundant facets are precisely the \(q-1\) comparison faces
\[
F_j:\ d_j=d_{j+1}\quad(1\le j<q)
\]
and the \(2q\) coordinate faces
\[
G_{1,k}:a_k=0,\quad G_{2,k}:b_k=0\quad(1\le k\le q).
\]
This facet description is established by Erickson and Kretschmann (Theorem 5.3) and also follows directly by positive-slack constructions. Intrinsic outward normals, in ambient coordinates ordered \((a_1,\ldots,a_q,b_1,\ldots,b_q)\), are
\[
u_j=e_{a_j}-e_{a_{j+1}}-e_{b_j}+e_{b_{j+1}},\qquad
v_{r,k}=-e_{r,k}+\frac1{2q}\mathbf1.
\]
Consequently \(\|u_j\|=2\), \(\|v_{r,k}\|^2=1-1/(2q)\), and \(u_j\cdot v_{r,k}=-(u_j)_{r,k}\). Distinct coordinate normals have dot product \(-1/(2q)\), while \(u_j\cdot u_{j+1}=-2\) and \(u_j\cdot u_\ell=0\) when \(|j-\ell|\ge2\).

**2. Which pairs define ridges.** Every pair of distinct comparison facets meets in a ridge, as does every comparison/coordinate pair. To see this directly, choose a strictly increasing list \((d_1,\ldots,d_q)\) with only the designated comparison equalities, then set \(a_j=(t_j+d_j)/2\), \(b_j=(t_j-d_j)/2\) with \(t_j>|d_j|\), except at one designated zero coordinate where set \(t_j=|d_j|\). A common positive rescaling gives total sum one. This produces a point in the relative interior of the desired two-facet intersection, with exactly those two inequalities tight. For two comparisons use two assigned equalities; no coordinate zeros are needed.

Two distinct coordinate facets within the **same row** also always meet in a ridge: choose a strictly increasing sequence of negative differences for zeros in the first row, or positive differences for zeros in the second row, and otherwise use strictly positive entries. The remaining mixed pairs \(G_{1,i},G_{2,k}\) meet in a ridge exactly when \(i\le k\). For \(i<k\), choose strictly increasing differences with \(d_i<0<d_k\), using \(t_i=-d_i\), \(t_k=d_k\) and large other totals. For \(i=k\), choose \(d_i=0\), \(t_i=0\) and strict differences elsewhere. All such points have precisely the intended two facets tight. If \(i>k\), monotonicity and the two zeros give
\[
0\le d_k=a_k\le d_i=-b_i\le0.
\]
Thus \(a_k=b_i=0\) and both opposite entries also vanish. When \(q=2\), all four coordinates would be zero, so the intersection is empty; when \(q\ge3\), any nonempty intersection lies in four independent coordinate-zero hyperplanes in \(H\) and has codimension at least four. In either case it is not a ridge. Every accepted two-facet pair has independent facet normals and a point on no other facet; hence its intersection has exactly codimension two and no ridge is counted twice.

**3. Angle enumeration.** For distinct comparison facets there are \(q-2\) adjacent pairs, with outward unit-normal inner product \(-1/2\), giving interior angle \(\pi/3\). The other \((q-2)(q-3)/2\) pairs are orthogonal. Among the \(2q(q-1)\) comparison/coordinate pairs, exactly \(2(q-1)\) have outward-normal inner product \(-1/[2\sqrt{1-1/(2q)}]\), exactly \(2(q-1)\) have its opposite, and the other \(2(q-1)(q-2)\) are orthogonal. These produce respectively \(\beta_q\), \(\pi-\beta_q\), and \(\pi/2\).

For coordinate/coordinate pairs, the two same-row classes contribute \(2\binom q2\); the allowed cross-row pairs contribute \(q(q+1)/2\). Thus exactly \((3q^2-q)/2\) ridges have exterior cosine \(-1/(2q-1)\), or interior angle \(\alpha_q\). Adding all multiplicities and simplifying yields \((2q-1)^2\). For \(q\ge3\), direct comparisons of the positive cosines show \(\beta_q<\pi/3<\alpha_q<\pi/2<\pi-\beta_q\), so there are five distinct positive-multiplicity levels.

**4. Angular weak limit and moment defect.** Divide every multiplicity by \((2q-1)^2\). The orthogonal-ridge proportion tends to \(5/8\); the coordinate/coordinate proportion tends to \(3/8\); and every other class has proportion \(O(1/q)\). Since \(q(\alpha_q-\pi/2)=-q\arcsin(1/(2q-1))\to-1/2\), the claimed weak convergence follows. The two comparison/coordinate nonright-angle classes have the same size and their angles sum to \(\pi\), so their contributions to the mean cancel around \(\pi/2\). Adjacent comparison pairs contribute \(-\pi/6\) per ridge, and coordinate/coordinate pairs contribute \(-\arcsin(1/(2q-1))\) per ridge. These give the displayed exact mean. Scaling and taking the limit produces \(-\pi/24-3/16\). This is not the mean of the weak limit because the sequence of rescaled angles is not uniformly integrable: the \(\pi/3\) class is rare, with probability of order \(1/q\), but each corresponding rescaled deviation is of order \(q\).

## Verification

`verify_monge_ridges.py` independently generates the exact \(3q\) vertices from the published rectangle/row/column classification, then tests every unordered pair of facets with exact rational affine-rank elimination, for each \(2\le q\le7\). It checks that an intersection is a ridge precisely under the classification in Step 2, that all six facet-pair classes have the stated counts, and that the total is \((2q-1)^2\). The test emits `MONGE_RIDGE_CLASSIFICATION_PASS dimensions=2..7 all_facet_pairs=checked_exactly`. This is a finite cross-check, not a proof for all dimensions; the preceding inequalities, positive-slack constructions, and normal calculations establish the general claim. The mean identity was also independently evaluated numerically at \(q=2,3,4,5,25,1000\) against the exact expression, and the observed scaled means converge to \(-3/16-\pi/24\).

## Relationship to prior work

Erickson and Kretschmann, *The structure and normalized volume of Monge polytopes* (arXiv:2311.07522, first made public November 13, 2023), define these polytopes and prove their vertex/facet descriptions, edge census and volume normalization. Those results, especially Theorem 5.3, are prior work and are not claimed here. Existing work on the same two-row polytope derives its exact Euclidean surface-area profile and separately its mean width, centroids and Euclidean inball; those concern different-dimensional face measures and directional functionals. The present claim is the full **codimension-two Euclidean interior-angle spectrum**, plus the angular weak limit and the nonuniform-integrability correction to its scaled first moment. The incident facet-pair counts follow naturally from the prior face-lattice setup, but the paired metric spectrum and moment anomaly are not asserted in the primary paper's inspected statements or in the compared results. Priority remains provisional against unindexed equivalent work.

## Limitations

Only normalized nonsymmetric **two-row** Monge matrices with the standard inherited Euclidean metric are covered. The argument does not determine weighted ridge areas, other row counts, Euclidean solid angles of vertices, or angles under anisotropic coordinate scalings. The weak convergence is distributional and the rescaled means do not converge to the weak-limit mean. The proof uses the published exhaustive facet and vertex descriptions; an equivalent dihedral-angle analysis in unindexed work could affect historical novelty. Self-review is not an independent audit.

## References

1. William Q. Erickson and Jan Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522, first public November 13, 2023, Theorem 5.3 and Proposition 5.1. https://arxiv.org/abs/2311.07522 .
2. *Sharp binomial boundary layers and exact surface area of two-row Monge polytopes*, separate scientific treatment of boundary area (not dihedral angles).
3. *A sharp rare-vertex mean-width correction for two-row Monge polytopes*, published October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-rare-vertex-mean-width-correction-for-two-row-monge-poly--bf1db1bc9d42 .
4. *Exact centroids and logarithmic edge profiles of two-row Monge polytopes*, published November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-centroids-and-logarithmic-edge-profiles-of-two-row-monge-p--20e8b8de7493 .
