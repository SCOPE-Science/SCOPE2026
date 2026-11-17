# Two cut-locus exponents make the distance histogram rigid for flat Klein bottles

## Finding

Consider the two-parameter family of standard flat Klein bottles \(K_{a,b}\) in the next section. Their global intrinsic two-point distance distribution \(F_{a,b}(r)\) uniquely determines the **ordered** pair \((a,b)\), and thus the metric quotient up to isometry. Only the small-distance coefficient and the first singular transition of the distribution are needed.

Writing \(A=ab\), \(t=\min(a,b)/2\), and \(J(r)=\pi r^2-AF_{a,b}(r)\), one has \(J(r)=0\) for all \(0\le r\le t\), and \(J(r)>0\) for all sufficiently close \(r>t\). As \(\varepsilon\downarrow0\),

\[
J(t+\varepsilon)=
\begin{cases}
\dfrac{8\sqrt a}{3}\varepsilon^{3/2}+O(\varepsilon^{5/2}),&a<b,\\[5pt]
\dfrac{2\pi b}{a}\varepsilon^2+O(\varepsilon^{3}),&b<a,\\[5pt]
\dfrac{8\sqrt a}{3}\varepsilon^{3/2}+\dfrac{2\pi b}{a}\varepsilon^2+O(\varepsilon^{5/2}),&a=b.
\end{cases}
\]

The distinct \(3/2\) versus \(2\) exponents distinguish whether the first geodesic identifications arise along a translation or a glide. In the equal-length case the parameters are already fixed by \(A\) and \(t\). This is an injectivity theorem *within the rectangular flat Klein-bottle family*; it is not a claim about arbitrary flat surfaces.

## Assumptions and scope

For arbitrary \(a,b>0\), define Euclidean isometries
\[
T(x,y)=(x+a,y),\qquad G(x,y)=(-x,y+b).
\]
Their group acts freely and properly discontinuously. The compact quotient \(K_{a,b}=\mathbb R^2/\langle T,G\rangle\) has a fundamental rectangle of width \(a\), height \(b\), and Riemannian area \(A=ab\). The vertical generator is a glide reflection and the horizontal generator a pure translation. Use intrinsic shortest-path distance from the quotient Euclidean metric and its normalized area measure. Choose \(X,Y\) independently from this measure. In particular, the distribution is not a Euclidean embedding distance, and the two points are not sampled from a boundary.

The exact local statement below applies for each *fixed* \(a,b>0\), with a potentially parameter-dependent interval after the first cutoff. No uniform remainder bound over degenerating aspect ratios is claimed.

## Proof

**Step 1: local volume coefficient and first cut radius.** If \(p\) is a lift of a point on the quotient, its orbit has nonidentity vectors from the even subgroup \(T^mG^{2k}\), whose lengths are \(\sqrt{m^2a^2+4k^2b^2}\), and from the odd subgroup \(T^mG^{2k+1}\). For \(p=(x,y)\), the latter vectors are
\[
(ma-2x,(2k+1)b),\qquad m,k\in\mathbb Z.
\]
All nonzero orbit displacements are at least \(\min(a,b)\), and this lower bound is attained by the horizontal translation for all \(p\) when \(a\le b\), or by glide displacements at \(2x\in a\mathbb Z\) when \(b\le a\). Thus every intrinsic disk of radius \(r\le t=\min(a,b)/2\) has area \(\pi r^2\) (possible boundary identifications have zero area), and \(F(r)=\pi r^2/A\). For \(r>t\), at least one overlap has positive area on a positive-measure set of basepoints, so the averaged area is strictly less than \(\pi r^2\) as soon as \(r>t\) sufficiently close.

**Step 2: exact local overlap formula.** For two Euclidean radius-\(r\) disks whose centers have separation \(d<2r\), write their common lens area
\[
\Lambda_r(d)=2r^2\arccos\!\left(\frac d{2r}\right)-\frac d2\sqrt{4r^2-d^2},
\]
and set \(\Lambda_r(d)=0\) when \(d\ge2r\). Each competing orbit point cuts a *half-lens* out of the lifted disk centered at \(p\). For fixed \(a,b\), choose \(\eta>0\) so that, for \(t<r<t+\eta\), only the shortest horizontal shifts and/or shortest glide shifts reach distance \(<2r\). Their half-lens regions are pairwise disjoint: opposite shifts point in opposite directions; glide versus horizontal contact directions are orthogonal; and two distinct glide horizontal translates cannot simultaneously be near-tangent for a single basepoint when \(r-t\) is sufficiently small. All remaining orbit points stay a positive distance beyond \(2t\). Accordingly the quotient disk area is \(\pi r^2\) minus the sums of these half-lens areas, *without inclusion–exclusion remainders* for such radii.

The two horizontal neighbors \(p\pm(a,0)\) contribute one full \(\Lambda_r(a)\). For each integer \(m\), the two nearest glide images have displacement vectors \((ma-2x,\pm b)\); together they contribute \(\Lambda_r(\sqrt{b^2+(ma-2x)^2})\). Averaging over a fundamental rectangle removes dependence on \(y\). Periodization gives
\[
\frac1a\int_0^a\sum_{m\in\mathbb Z}
\Lambda_r\!\left(\sqrt{b^2+(ma-2x)^2}\right)dx
=\frac1a\int_{\mathbb R}\Lambda_r(\sqrt{b^2+u^2})\,du.
\]
Since \(AF(r)\) is the mean quotient disk area, for all \(t<r<t+\eta\) we obtain the exact identity
\[
\boxed{J(r)=\Lambda_r(a)+\frac1a\int_{\mathbb R}
\Lambda_r\!\left(\sqrt{b^2+u^2}\right)du.}
\]
The second term vanishes for \(2r\le b\); the first vanishes for \(2r\le a\). Equivalently, the integral can be restricted to \(\lvert u\rvert<\sqrt{4r^2-b^2}\) whenever \(2r>b\).

**Step 3: the competing exponents.** The elementary circular-segment expansion, as \(\delta\downarrow0\) with \(r\) in a compact positive interval, is
\[
\Lambda_r(2r-\delta)=\frac43\sqrt r\,\delta^{3/2}
+O(\delta^{5/2}).
\]
For \(r=a/2+\varepsilon\), this yields
\[
\Lambda_r(a)=\frac{8\sqrt a}{3}\varepsilon^{3/2}
+O(\varepsilon^{5/2}).
\]
For \(r=b/2+\varepsilon\), substitute \(u=2\sqrt{b\varepsilon}\,v\) in the glide integral. The expression \(2r-\sqrt{b^2+u^2}\) equals \(2\varepsilon(1-v^2)+O(\varepsilon^2)\) on its shrinking support. Using dominated convergence after factoring out \(\varepsilon^2\), and
\[
\int_{-1}^1(1-v^2)^{3/2}\,dv=\frac{3\pi}{8},
\]
we obtain the exact leading coefficient
\[
\frac1a\int_{\mathbb R}\Lambda_r(\sqrt{b^2+u^2})\,du
=\frac{2\pi b}{a}\varepsilon^2+O(\varepsilon^3).
\]
These formulas prove all three cases, including addition of the distinct-order terms when \(a=b\).

**Step 4: reconstruction and uniqueness.** The distribution determines
\[
A=\left(\lim_{r\downarrow0}\frac{F(r)}{\pi r^2}\right)^{-1},\qquad
 t=\sup\{s>0:\ F(r)=\pi r^2/A\ \text{for every }0\le r\le s\}.
\]
Set \(m=2t\) and \(M=A/m\). The unordered pair of parameters is \(\{m,M\}\). If \(m=M\), then \(a=b=m\). If \(m<M\), the deficit has order \(\varepsilon^{3/2}\) if \(a=m\), but order \(\varepsilon^2\) if \(b=m\). Thus the observed exponent specifies the ordering. In either case \((a,b)\) is uniquely reconstructed. \(\square\)

## Verification

The accompanying standalone `verify_klein.py` computes the exact local lens and one-dimensional glide integral; it compares their predicted distance CDF values against an independent pair-of-points simulation which minimizes Euclidean distances over nearby even and odd deck transformations. Cases with \(a<b\), \(b<a\), and \(a=b\) are included. It also tests normalized asymptotic coefficients for six positive cutoff offsets in each regime. The recorded run was:

`VERIFICATION_OK distance_pair_sampling=6 local_coefficients=18 small_epsilon_ratios= [(2.0, 3.0, 1.00174842), (3.0, 2.0, 1.00249922), (2.0, 2.0, 1.00204285)]`

For the equal-length case the predicted \(O(\varepsilon^2)\) glide contribution is subtracted before the last ratio is compared to the leading horizontal coefficient. This is a numerical check only; analytic proof establishes the infinite statements.

## Relationship to prior work

El Mir and Yassine [1] work with flat Klein-bottle covering models and prove conformal length and area inequalities; they do not give this global two-point histogram reconstruction. Mémoli and Needham [2] frame inverse problems using distance distributions, including nonuniqueness in broad classes; their broader framework does not imply the specific injectivity of the Klein family. Hubard and collaborators [3] investigate shortest-path embeddings for flat Klein-bottle metrics; their object is graph embedding, not random-pair distance laws. Davis and Recio-Mitter [4] investigate geodesic complexity and cut loci on Klein bottles, not the area-averaged two-point distance distribution. The new claim uses their common metric-geometric setting but its local exponent comparison is not contained in the identified statements. This originality assessment remains provisional pending independent scholarly review.

## Limitations

This theorem assumes the exact continuous global distance CDF, known to arise from a standard flat Klein bottle with two orthogonal metric parameters. It does not assert recognition of the Klein-bottle topology among *all* compact metric spaces, stability under noisy finite samples, a classification of nonflat Klein metrics, or any property of an extrinsic embedding. The local asymptotics are pointwise in fixed \(a,b>0\), not uniform as one parameter tends to zero. The auxiliary script is diagnostic, not a formal proof certificate.

## References

[1] C. El Mir and Z. Yassine, *Conformal Geometric Inequalities on the Klein Bottle*, arXiv:1209.6202v1 (first public 2012-09-27). https://arxiv.org/abs/1209.6202

[2] F. Mémoli and T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646 (first public 2018-10-23; published 2022). https://arxiv.org/abs/1810.09646

[3] A. Hubard, V. Kaluža, A. de Mesmay, and M. Tancer, *Shortest path embeddings of graphs on surfaces*, arXiv:1602.06778v1 (first public 2016-02-22). https://arxiv.org/abs/1602.06778

[4] D. M. Davis and D. Recio-Mitter, *The geodesic complexity of n-dimensional Klein bottles*, arXiv:1912.07411 (first public 2019-12-16). https://arxiv.org/abs/1912.07411
