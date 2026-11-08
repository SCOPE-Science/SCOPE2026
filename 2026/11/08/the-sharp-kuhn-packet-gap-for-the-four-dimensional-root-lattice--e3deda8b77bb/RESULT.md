# The sharp Kuhn-packet gap for the four-dimensional root lattice \(D_4\)

## Finding

Let \(D_4=\{z\in\mathbb Z^4:\sum_{i=1}^4 z_i\in2\mathbb Z\}\) and let \(B_2^4\) be the Euclidean unit ball. For the original common-frame Kuhn-packet invariant defined below,
\[
\boxed{\kappa(B_2^4,D_4)=\sqrt{3/2},\qquad \mu(B_2^4,D_4)=1.}
\]
In particular, the precise penalty for requiring one lattice frame to generate all permutation simplices is \(\sqrt{3/2}\), even though allowing an arbitrary periodic lattice triangulation restores the ordinary covering radius.

A second exact geometric statement underlies the first: every linearly independent quadruple \(b_1,b_2,b_3,b_4\in D_4\) satisfies
\[
\max_{\varnothing\ne I\subseteq\{1,2,3,4\}}\left\|\sum_{i\in I}b_i\right\|_2^2\ge6.
\]
The displayed basis in the proof attains equality. This is a sharp, all-frame subset-sum obstruction, not merely an obstruction among lattice bases.

## Assumptions and scope

For an ordered independent lattice frame \(B=(b_1,b_2,b_3,b_4)\) and a permutation \(\sigma\in S_4\), put
\[
\Delta_\sigma(B)=\operatorname{conv}\left\{0,b_{\sigma(1)},b_{\sigma(1)}+b_{\sigma(2)},\ldots,\sum_{j=1}^4b_j\right\}.
\]
For a finite set or simplex \(A\subset\mathbb R^4\), let \(r(A)\) be its least Euclidean enclosing-ball radius. Following the original Kuhn-packet definition of Xue, set
\[
\kappa(B_2^4,D_4)=\inf_{B\text{ independent in }D_4}\max_{\sigma\in S_4} r(\Delta_\sigma(B)).
\]
Each simplex may have its own ball center, but the *same ordered independent frame* must produce all 24 simplices. The frame may generate a proper sublattice. The ordinary covering radius is \(\mu(B_2^4,D_4)=\sup_{x\in\mathbb R^4}\operatorname{dist}(x,D_4)\). The invariant here is the original \(\kappa\), **not** the later relaxed periodic-triangulation invariant \(\widehat\kappa\).

## Proof

**1. The ordinary covering radius is exactly one.** Given \(x\in\mathbb R^4\), choose a coordinatewise nearest-integer vector \(m\in\mathbb Z^4\), with absolute rounding errors \(\delta_i\in[0,1/2]\), and put \(q=\max_i\delta_i\). If \(\sum_i m_i\) is even, \(m\in D_4\) and \(\|x-m\|_2^2\le4q^2\le1\). If the sum is odd, adjust a coordinate with error \(q\) to the other adjacent integer, changing the parity; the new squared distance is at most \(4q^2+1-2q\le1\), because \(0\le q\le1/2\). Thus \(\mu\le1\). The point \((1,0,0,0)\) is at distance exactly one from \(D_4\), giving \(\mu=1\).

**2. Every frame has a subset sum of squared length at least six.** Every \(z\in D_4\) has even squared Euclidean norm, since \(z_i^2\equiv z_i\pmod2\). If four independent vectors had all 15 nonempty subset sums of squared norm at most four, each generator would belong to the finite set
\[
V=\{z\in D_4:0<\|z\|_2^2\le4\}.
\]
The set \(V\) consists of 24 vectors of squared norm two and 24 of squared norm four: exactly 48 vectors. Exhaustive *exact-integer* recursion over ordered independent partial frames, retaining precisely those for which every existing nonempty subset sum has squared norm at most four, gives the following counts, by frame length \(0,1,2,3,4\):
\[
\boxed{(1,48,816,1728,0).}
\]
Independence is checked by strict positivity of the exact integer Gram determinant, and new subset sums are obtained by adding the candidate generator to each previous subset sum (including zero). The supplied complete standard-library verifier implements this 48-element finite search and independently evaluates all Gram determinants by the permutation determinant formula. These counts are exhaustive because **any** potential counterexample necessarily uses four vectors of \(V\); there are no omitted long generators, orientations or frames. The last count is zero. Hence at least one nonempty subset sum of any independent quadruple has squared norm \(\ge6\).

For each subset \(I\), choose a permutation with the elements of \(I\) first. Both zero and \(\sum_{i\in I}b_i\) are then vertices of that permutation simplex. A ball enclosing it has radius at least half their distance. Consequently every Kuhn packet contains a simplex of radius at least \(\sqrt6/2=\sqrt{3/2}\), proving the lower bound for \(\kappa\).

**3. A sharp explicit lattice basis and 24 enclosing balls.** Consider the ordered frame
\[
\begin{aligned}
b_1&=(-1,-1,0,0),&b_2&=(-1,0,-1,0),\\
b_3&=(0,1,1,0),&b_4&=(1,0,0,-1).
\end{aligned}
\]
Its row determinant is \(2\), the covolume of \(D_4\), so it is in fact a lattice basis. For each permutation, write \(p_0=0\) and \(p_j=\sum_{h=1}^j b_{\sigma(h)}\) for \(1\le j\le4\). The following **complete list of all 24 permutations** exhibits two indices \(i<j\) and the ball center \(c=(p_i+p_j)/2\). In each row, \(d^2=\|p_i-p_j\|_2^2\) is the squared simplex diameter and \(4r^2_{\rm shown}=\max_{0\le h\le4}\|2p_h-p_i-p_j\|_2^2\); the equality of the last two columns proves the enclosing ball is exact. Permutation digits refer to the subscripted basis vectors.

| Permutation | \(d^2\) | Center pair \(i,j\) | \(4r^2_{\rm shown}\) |
| --- | ---: | :---: | ---: |
| 1234 | 6 | 0--2 | 6 |
| 1243 | 6 | 0--2 | 6 |
| 1324 | 4 | 0--3 | 4 |
| 1342 | 4 | 1--3 | 4 |
| 1423 | 4 | 0--3 | 4 |
| 1432 | 4 | 1--3 | 4 |
| 2134 | 6 | 0--2 | 6 |
| 2143 | 6 | 0--2 | 6 |
| 2314 | 4 | 0--3 | 4 |
| 2341 | 4 | 1--3 | 4 |
| 2413 | 4 | 0--3 | 4 |
| 2431 | 4 | 1--3 | 4 |
| 3124 | 6 | 1--3 | 6 |
| 3142 | 4 | 1--4 | 4 |
| 3214 | 6 | 1--3 | 6 |
| 3241 | 4 | 1--4 | 4 |
| 3412 | 6 | 2--4 | 6 |
| 3421 | 6 | 2--4 | 6 |
| 4123 | 6 | 1--3 | 6 |
| 4132 | 4 | 1--4 | 4 |
| 4213 | 6 | 1--3 | 6 |
| 4231 | 4 | 1--4 | 4 |
| 4312 | 6 | 2--4 | 6 |
| 4321 | 6 | 2--4 | 6 |

Twelve permutations have squared enclosing radius \(1\), and the other twelve have squared enclosing radius \(3/2\). Because all vertices lie in their stated midpoint balls and each displayed pair is diametral, these are the **exact** minimum enclosing-ball radii for the 24 simplices. Their maximum is \(\sqrt{3/2}\). Combined with step 2, this proves the claimed exact \(\kappa\) and the sharp subset-sum bound (the frame has a subset sum of squared length six).

## Verification

The standalone `verify.py` uses only Python's standard library, performs exact integer calculations, and prints `EXACT_OK` on success. Reproduce with `python3 verify.py`. It enumerates all 48 eligible vectors; checks the complete recursion counts \((1,48,816,1728,0)\); proves the basis determinant is \(2\); and verifies all 24 simplex midpoint certificates, split \(12+12\) between squared diameters four and six. The finite exhaustive computation is used only *after* the mathematical cutoff \(\|b_i\|_2^2\le4\) has been proved; it therefore completes a universal argument over all possible lattice frames rather than extrapolating from finite samples.

## Relationship to prior work

Xue introduced the original common-frame packet minimum and proved general comparisons with the classical covering radius, including equality in indices one and two, and asymptotically growing Euclidean separation in high dimension. In particular, the subset-sum diameter observation in step 2 is already present in Xue's Section 5; only its sharp \(D_4\) specialization, finite obstruction, and matching exact frame are the proposed contributions. The same paper defines a **different relaxed** periodic-triangulation invariant and proves that it equals the classical radius for ellipsoids. Our strict inequality concerns only the original invariant, not that relaxation.

Lian and Xue previously studied common-frame Kuhn triangulations for lattice coverings, notably in dimension three, but the inspected source description does not determine this four-dimensional exact Euclidean value. Classical descriptions of the \(D_4\) root lattice, its determinant, and its Voronoi geometry do not by themselves specify the optimum over the 24-simplex packets for independent frames.

## Limitations

The proof evaluates one explicitly normalized four-dimensional root lattice with the Euclidean unit ball. It does not classify the minimizers among all frames, determine the indexed lower-dimensional projection minima, or establish a sharp dimension-four worst-case ratio over every lattice. The finite search and all its arithmetic are reproducible in the embedded verifier; definitive historical priority and independent proof review remain open. A thematically related earlier three-dimensional Kuhn-triangulation paper was available in abstract/secondary citation only, not fully inspected, so it remains an explicit priority-access risk.

## References

1. Fei Xue, *On κ-covering minima*, arXiv:2610.39034v1 (first posted 2026-10-28), Sections 1, 2, 5, 6. https://arxiv.org/abs/2610.39034 .
2. Yanlu Lian and Fei Xue, *Minimal Covering Bodies and a Minkowski-Type Criterion for Lattice Coverings*, arXiv:2606.14584 (first posted 2026-06-12), especially the three-dimensional Kuhn triangulation criterion. https://arxiv.org/abs/2606.14584 .
3. Gabriele Nebe and Neil J. A. Sloane, *The Lattice D4*, Catalogue of Lattices (catalogue entry; standard D4 structure). https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/D4.html .
