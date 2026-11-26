# Sharp central-symmetry phase transition of homothetic frusta

## Finding
Let \(d\ge2\) be an integer, and let \(B=-B\subset\mathbb R^{d-1}\) be any compact convex body with nonempty interior. For \(0\le r\le1\) set
\[
F_r(B)=\operatorname{conv}\bigl(rB\times\{0\},B\times\{1\}\bigr).
\]
The **central-symmetry volume fraction** of any full-dimensional convex body \(K\) is
\[
\beta(K)=\max_{c\in\mathbb R^d}\frac{\operatorname{Vol}_d\bigl(K\cap(2c-K)\bigr)}{\operatorname{Vol}_d(K)}.
\]
Every centrally symmetric convex subset of \(K\) centered at \(c\) is contained in the reflected intersection, so this is the maximum inscribed centrally symmetric volume fraction.

Define
\[
q_d=2^{-1/(d-1)},\qquad
 a_d=\frac1{2-q_d},\qquad
 r_d=\frac{q_d}{2-q_d}=2a_d-1.
\]
Then **the unique optimizing symmetry center** of \(F_r(B)\) is \((0,s_d(r))\), where
\[
s_d(r)=\begin{cases}
\dfrac{a_d-r}{1-r},&0\le r<r_d,\\[3pt]
\dfrac12,&r_d\le r\le1.
\end{cases}
\]
The exact ratio is
\[
\boxed{\beta(F_r(B))=
\begin{cases}
\dfrac{a_d^{d-1}}{1-r^d},&0\le r\le r_d,\\[5pt]
\dfrac{2\bigl(((1+r)/2)^d-r^d\bigr)}{1-r^d},&r_d\le r<1,\\[5pt]
1,&r=1.
\end{cases}}
\]
The two positive-radius formulas agree at \(r=r_d\). For smaller radius ratios the center moves with \(r\); at the sharp threshold it reaches the middle-height plane and remains there for all larger ratios. The formula and threshold are independent of the shape of \(B\). In dimension two the threshold is \(1/3\); in dimension three it is \(1/(2\sqrt2-1)\).

## Assumptions and scope
The horizontal base \(B\) is centrally symmetric about the origin, bounded, full-dimensional, and convex; no smoothness or strict convexity is imposed. The truncated-cone parameter \(r\) includes the cone endpoint \(0\) and symmetric-prism endpoint \(1\). The normalization fixes total height and larger-base scale at one, without loss under invertible affine maps. The same result applies after an arbitrary affine shear, in particular when the homothetic base centers are not vertically aligned. It does not extend by this argument to unrelated nonhomothetic cross-sections or to asymmetric \(B\).

## Proof
**1. Every maximizing center is axial.** Write \(n=d-1\). The slice of \(F_r(B)\) at height \(z\in[0,1]\) is \(w(z)B\), with \(w(z)=r+(1-r)z\). Fix a proposed symmetry center \(c=(u,s)\). A nonempty full-dimensional reflected intersection requires \(0<s<1\). Its slice at \(z\) is
\[
w(z)B\cap\bigl(2u+w(2s-z)B\bigr),
\]
where we used \(B=-B\). Its \(n\)-volume is at most
\[
|B|\min\bigl(w(z),w(2s-z)\bigr)^n.
\]
For \(u=0\), both sets are concentrically nested dilations of \(B\), and equality holds in this bound for every admissible slice. If \(u\ne0\), the slice at \(z=s\) is \(w(s)B\cap(2u+w(s)B)\), which has strictly smaller volume than \(w(s)B\). Indeed, two unequal translates of a bounded full-dimensional convex body cannot agree up to measure zero: otherwise their convex closures would coincide and repeated translation would contradict boundedness. Continuity of slice intersection volume gives strict loss on an interval of heights around \(s\). Therefore \(u=0\) is necessary for global optimality and is optimal for every fixed \(s\).

**2. Exact reflection-volume profile.** Because \(w\) is increasing, the smaller of its arguments at \(z\) and \(2s-z\) is \(w(\min\{z,2s-z\})\). Integrating these nested slices gives, when \(0\le r<1\),
\[
\frac{\operatorname{Vol}_d(F_r(B)\cap(2(0,s)-F_r(B)))}{|B|}
=\frac{2}{d(1-r)}
\begin{cases}
[r+(1-r)s]^d-r^d,&0\le s\le\tfrac12,\\[3pt]
[r+(1-r)s]^d-[r+(1-r)(2s-1)]^d,&\tfrac12\le s\le1.
\end{cases}
\tag{1}
\]
Independently,
\[
\operatorname{Vol}_d(F_r(B))=\frac{|B|}{d(1-r)}(1-r^d).
\tag{2}
\]
Both formulas are direct integrals of \(n\)-dimensional slice volumes, not sample-based approximations.

**3. Unique height optimum and transition.** On the first interval in (1), differentiation gives the strictly positive derivative \(2[r+(1-r)s]^{d-1}\) for \(s>0\). Thus every optimum has \(s\ge1/2\). On the second interval put \(a=r+(1-r)s\), so the reflected smaller radius is \(2a-1\); here \(a\in[(1+r)/2,1]\). The sign of the derivative in \(s\) is the sign of
\[
H_d(a)=a^{d-1}-2(2a-1)^{d-1}.
\]
For \(a>1/2\), the ratio \(a/(2a-1)\) decreases strictly, hence \(H_d\) changes sign exactly once, from positive to negative, at \(a=a_d=1/(2-2^{-1/(d-1)})\). This stationary point lies in the interval if and only if \((1+r)/2\le a_d\), equivalently \(r\le r_d\). If \(r<r_d\), its unique maximizing height solves \(r+(1-r)s=a_d\), giving \(s=(a_d-r)/(1-r)>1/2\). If \(r\ge r_d\), the unique maximum occurs at \(s=1/2\); at equality of the threshold the stationary point coincides with this boundary. This proves the unique-center statement for every \(r<1\).

At the interior stationary point, \(2a_d-1=q_da_d\) and \(2q_d^{d-1}=1\), hence
\[
2\bigl(a_d^d-(2a_d-1)^d\bigr)=a_d^{d-1}.
\]
Divide (1) by (2) to obtain the stated first branch. Substituting \(s=1/2\) yields the stated second branch, including equality at the threshold. For \(r=1\) the body is the centrally symmetric prism \(B\times[0,1]\), whose unique center of symmetry is \((0,1/2)\). Its maximum ratio equals one. This proves all statements.

## Verification
The standalone, standard-library-only script `verify.py` re-evaluates the reflection-volume integrals and exact optimizer formula for dimensions 2 through 30 and several parameter values including both sides of every transition. It compares the predicted optimum with 101 independent height-grid values per case, and in dimension two numerically integrates the actual intersections of translated horizontal intervals, including nonaxial centers. Running `python3 verify.py` prints `VERIFY_OK` (29,430 tested inequalities/comparisons); the largest numerical integration discrepancy observed was approximately \(1.4\cdot10^{-15}\). These finite checks are only regression tests: the universal assertions are proved by the exact slice integration and derivative arguments above.

## Relationship to prior work
Saroglou's *On the equivalence between two problems of asymmetry on convex bodies* (first public version 20 November 2013) studies the maximum inscribed centrally symmetric fraction in the context of asymmetry extremizers and its relation to the Blaschke body. That general extremal-equivalence theorem does not supply the reflection-intersection formula or the complete homothetic-frustum phase diagram. Goenka, Moore, Sun and White's *On Axial Symmetry in Convex Bodies* (2023) studies related symmetry measures and a dimension-dependent conical bound. The \(r=0\) triangle/rounded-cone benchmark and its appearance in earlier symmetry studies are **not** claimed as new: the new contribution is the exact ratio, universal optimizing-center classification, and sharp \(r_d\) transition over \(0<r<1\).

A separate published result, *Universal Santaló and volume-product laws for homothetic frusta*, studies precisely these homothetic bodies for a different invariant: the location of the Santaló center and the Mahler product. Its polar-volume formula and monotonicity do not determine the maximum reflected-intersection volume or its maximizing reflection center. Another published result, *Exact Kovner–Besicovitch area ratio of regular Reuleaux odd-gons*, studies the same symmetry invariant on different planar circular-arc bodies, not frusta. Full mathematical statements and proofs of both relevant published results were compared. General facts that a symmetric subset is contained in its corresponding reflected intersection, or that reflection-overlap is concave after taking a volume root, also do not by themselves yield the displayed threshold and all-dimensional formula.

## Limitations
The base must be centrally symmetric, and the two end slices must be positive homothetic copies, with the degenerate point-base and equal-base limits included. The proof does not characterize the symmetry measure for asymmetric-base frusta or nonhomothetic prismatoids. The cone endpoint, the planar triangle ratio \(2/3\), and the general definition of central-symmetry measure are classical; no historical novelty is asserted for them. Searchable full-text comparison cannot exclude an older unindexed elementary treatment of the planar trapezoid specialization or an equivalent higher-dimensional frustum formula; this remains a priority risk. No independent scientific audit is asserted.

## References
1. C. Saroglou, *On the equivalence between two problems of asymmetry on convex bodies*, arXiv:1311.4955v1, first posted 20 November 2013, subsequently *Discrete & Computational Geometry* 54 (2015), 573–585.
2. R. Goenka, K. Moore, W. R. Sun, E. P. White, *On Axial Symmetry in Convex Bodies*, arXiv:2309.12597v1, first posted 22 September 2023, especially the conical symmetry bound and related definitions.
3. *Universal Santaló and volume-product laws for homothetic frusta*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-santal-and-volume-product-laws-for-homothetic-frusta--3dbfdaf0b359 .
4. *Exact Kovner–Besicovitch area ratio of regular Reuleaux odd-gons*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-kovner-besicovitch-area-ratio-of-regular-reuleaux-odd-gons--71273748c58f .
