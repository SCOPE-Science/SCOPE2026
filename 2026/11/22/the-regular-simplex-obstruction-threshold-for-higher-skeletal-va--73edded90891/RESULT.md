# The regular-simplex obstruction threshold for higher skeletal Vaaler inequalities

## Finding
Let \(S_n\) be a regular \(n\)-simplex with inradius one and centroid at the origin, for each integer \(n\ge2\). Write \(Q_n=[-1,1]^n\) and \(\Phi_j(P)=\sum_{F\in\mathcal F_j(P)}\mathcal H^j(F)\), where \(\Phi_0\) counts vertices and \(\mathcal F_n(P)=\{P\}\). Then
\[
R_{n,j}:=\frac{\Phi_j(S_n)}{\Phi_j(Q_n)}=
\frac{n+1}{2^n}\frac{[n(n+1)]^{j/2}}{j!\sqrt{j+1}},\qquad 0\le j\le n.
\]
There is exactly one first nonnegative comparison dimension
\[
j_*(n)=\min\{j\in\{0,\dots,n\}:R_{n,j}\ge1\}\in\{1,\dots,n-1\}.
\]
Precisely the dimensions \(j<j_*(n)\) violate the cubical skeletal bound within the regular-simplex family; all \(j\ge j_*(n)\) satisfy it within this family.

Let \(\alpha\) be the unique solution in \((0,1)\) of
\[
\alpha(1-\log\alpha)=\log2,\qquad
\alpha=0.3275624139775169\ldots.
\]
With
\[
\beta=-\frac{-\log\alpha+\alpha/2-(1/2)\log(2\pi)}{-\log\alpha}
=-0.3233822103134059\ldots,
\]
the positive real crossing of the gamma-interpolated ratio near \(\alpha n\) has location
\[
\xi_n=\alpha n+\beta+O(n^{-1}),
\qquad j_*(n)=\lceil\xi_n\rceil\quad\text{for all sufficiently large }n.
\]
In particular \(j_*(n)=\alpha n+O(1)\). If \(k_{\max}(n)\) denotes the maximal initial range of codimensions for which the proposed cubical lower bounds hold for *every* polytope obeying all face-distance constraints, then
\[
k_{\max}(n)\le n-j_*(n)=(1-\alpha)n+O(1),
\qquad 1-\alpha=0.6724375860224831\ldots.
\]
This is an obstruction from the specified family, **not** a determination of the unrestricted valid range.

## Assumptions and scope
The ambient metric is Euclidean. The face-distance hypothesis is that every nonempty proper codimension-\(k\) face \(F\) satisfies \(\operatorname{dist}(0,\operatorname{aff} F)\ge\sqrt{k}\) for \(1\le k\le n\). The regular simplex above obeys every condition. The comparison is with the cube's exact total face measures \(\Phi_j(Q_n)=2^n\binom nj\). No assertion concerns arbitrary nonsimplex polytopes except the resulting *upper bound* on possible universal validity.

## Proof
**1. Distances from all face affine hulls.** Choose simplex vertices \(v_0,\ldots,v_n\) with \(\sum v_i=0\), \(v_i\cdot v_i=n^2\), and \(v_i\cdot v_l=-n\) for distinct vertices. The affine hull of a face spanned by \(m=n-k+1\) vertices has its origin-nearest point at their centroid, by symmetry; the squared norm of this centroid is
\[
\frac{mn^2-m(m-1)n}{m^2}=\frac{nk}{n-k+1}\ge k.
\]
For \(k=1\) the distance equals one, confirming the normalization. Thus every face-distance condition is satisfied. The edge length is \(\ell=\sqrt{2n(n+1)}\).

**2. Exact skeletal ratio.** A regular Euclidean \(j\)-simplex of edge length \(\ell\) has \(j\)-volume \(\ell^j\sqrt{j+1}/(j!\sqrt{2^j})\), including \(j=0\) under the usual zero-dimensional measure convention. There are \(\binom{n+1}{j+1}\) such \(j\)-faces. Therefore
\[
\Phi_j(S_n)=\binom{n+1}{j+1}\frac{[n(n+1)]^{j/2}\sqrt{j+1}}{j!}.
\]
Since \(\Phi_j(Q_n)=2^n\binom nj\) and \(\binom{n+1}{j+1}/\binom nj=(n+1)/(j+1)\), this gives the stated ratio.

**3. Unique crossing.** Direct cancellation yields
\[
\frac{R_{n,j+1}}{R_{n,j}}=\sqrt{\frac{n(n+1)}{(j+1)(j+2)}}.
\]
This is strictly greater than one for \(0\le j\le n-2\), and equals one for \(j=n-1\). At the left endpoint \(R_{n,0}=(n+1)/2^n<1\) for all \(n\ge2\). For the right endpoint, the arithmetic-geometric mean inequality \(n!\le((n+1)/2)^n\) gives
\[
R_{n,n}=\frac{\sqrt{n+1}\,[n(n+1)]^{n/2}}{2^n n!}
\ge\sqrt{n+1}\left(\frac n{n+1}\right)^{n/2}>1.
\]
The final strict inequality is equivalent to \((1+1/n)^n<n+1\), true because \((1+1/n)^n<e<3\le n+1\). Thus the integer transition exists, is unique, and cannot first occur at \(j=n\), since \(R_{n,n-1}=R_{n,n}>1\).

**4. Asymptotic boundary including its constant displacement.** Define the continuous gamma-interpolated logarithmic ratio for \(x\ge0\):
\[
G_n(x)=\log(n+1)-n\log2+\frac{x}{2}\log[n(n+1)]
-\log\Gamma(x+1)-\frac12\log(x+1).
\]
For \(x=sn\) with \(s\) in any fixed compact subset of \((0,1)\), Stirling's formula with a uniform remainder yields
\[
G_n(sn)=n\,[s(1-\log s)-\log2]
-\log s+\frac{s}{2}-\frac12\log(2\pi)+O(n^{-1}).
\]
The function \(f(s)=s(1-\log s)-\log2\) has derivative \(-\log s>0\) for \(0<s<1\), with \(f(0+)=-\log2\) and \(f(1)=1-\log2>0\). Thus it has a unique root \(\alpha\). Substituting \(x=\alpha n+t\), uniformly for bounded \(t\), gives
\[
G_n(\alpha n+t)=(-\log\alpha)t+
\left[-\log\alpha+\frac{\alpha}{2}-\frac12\log(2\pi)\right]+O(n^{-1}).
\]
The derivative of \(G_n\) near \(\alpha n\) approaches \(-\log\alpha>0\), so its local zero is \(\xi_n=\alpha n+\beta+O(n^{-1})\). By the exact discrete single-crossing proved above, the first integer with nonnegative ratio is \(\lceil\xi_n\rceil\) for sufficiently large \(n\), with equality itself allowed.

**5. Universal obstruction.** The proposed codimension-\(k\) inequality has face dimension \(j=n-k\). The admissible simplex violates it whenever \(n-k<j_*(n)\), i.e. \(k>n-j_*(n)\). Therefore no universally valid *initial* codimension range can end above \(n-j_*(n)\). The slope and the explicit shift follow from step 4.

## Verification
The accompanying `skeletal_threshold_check.py` uses exact integer arithmetic to check the signs of the squared ratios for all \(2\le n\le250\), verifies the consecutive-ratio identity, checks selected threshold examples, and compares the Stirling approximation numerically at large dimensions. It reports 63,012 finite arithmetic / asymptotic spot checks passed. The infinite proof is steps 1–5 above, not an inference from that finite sample.

## Relationship to prior work
Zwierzyński's 2026 paper *A Sharp Surface-Area Extension of Vaaler's Theorem* proves the universal facet measure inequality under the same face-distance assumptions and asks in Question 5.5 which higher-skeleton codimensions can satisfy analogous universal bounds. Proposition 5.1 already uses an inradius-one regular four-simplex to violate one low-dimensional bound; its regular-simplex example is not new. The present calculation determines the **entire** skeletal comparison profile of regular simplices in every dimension, gives the unique crossing and its two-term asymptotics, and turns it into a quantitative obstruction for Question 5.5. Published ridge-skeleton results for products of simplices concern codimension two; results on products of planar triangles concern a different family. Their statements do not determine this full regular-simplex profile. The formula for the volume of a regular simplex is classical; the proposed contribution is its organization into the exact all-dimensional obstruction transition and its asymptotic implications for the open range question.

## Limitations
The result provides only the **regular-simplex obstruction**, not a sharp universal theorem for all admissible polytopes. It does not prove validity at any codimension not already covered by independent theory. The quoted decimal values are approximations; the definitions of \(\alpha\) and \(\beta\) are exact. Priority among older isoperimetric and skeletal-measure literature has residual uncertainty, in particular where complete older texts were not accessible.

## References
1. M. Zwierzyński, *A Sharp Surface-Area Extension of Vaaler's Theorem*, arXiv:2609.27798 (public arXiv listing September 24, 2026), especially Proposition 5.1 and Question 5.5. https://arxiv.org/abs/2609.27798
2. R. Karasev, *Rogers's proof of Vaaler's theorem*, Discrete Mathematics 349 (2026), 115088. https://doi.org/10.1016/j.disc.2026.115088
3. L. Dalla and N. K. Tamvakis, *An isoperimetric inequality in the class of simplicial polytopes*, Math. Japonica 44 (1996), 569–572 (related fixed-volume skeletal inequalities).
