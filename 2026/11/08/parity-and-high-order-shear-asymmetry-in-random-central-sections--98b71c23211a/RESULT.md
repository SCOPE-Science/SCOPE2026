# Parity and high-order shear asymmetry in random central sections of skew bipyramids

## Finding

For every integer \(n\ge3\), let \(P_n\) be the unit-circumradius regular planar \(n\)-gon with one vertex at \((1,0)\). Fix \(0<s<\cos(\pi/n)\), \(h>0\), and form the convex bipyramid \(K_{n,s,h}\) with ring vertices
\[
v_j=(\cos(2\pi j/n),\sin(2\pi j/n),0),\qquad 0\le j<n,
\]
and apices \(a_+=(s,0,h)\), \(a_-=(s,0,-h)\). Choose an unoriented plane through the origin by Haar-uniform normal direction. Write \(N\) for the number of section vertices and \(\lambda=s/h\).

**Even-order rigidity.** For every even \(n\ge4\), \(N=n+2\) almost surely, for every admissible \(s,h\).

**Odd-order law.** For every odd \(n=2q+1\ge3\) and \(\lambda>0\), exactly the three values \(n+1,n+2,n+3\) have positive probability. Put
\[
k=\frac{\lambda}{\sqrt{1+\lambda^2}},\quad
F_\lambda(t)=\arcsin(k\sin t),\quad
 t_j=\frac{(j+\tfrac12)\pi}{n}\ (0\le j\le q),
\]
\[
\Delta_n(\lambda)=\frac{2(-1)^q}{\pi}\left[F_\lambda(t_0)+\sum_{j=1}^q(-1)^j\bigl(F_\lambda(t_j)-F_\lambda(t_{j-1})\bigr)\right].
\]
Then the *complete* distribution is
\[
\begin{aligned}
\Pr\{N=n+1\}&=\frac{\arctan\lambda}{\pi}+\frac{\Delta_n(\lambda)}2,\\
\Pr\{N=n+2\}&=1-\frac{2\arctan\lambda}{\pi},\\
\Pr\{N=n+3\}&=\frac{\arctan\lambda}{\pi}-\frac{\Delta_n(\lambda)}2.
\end{aligned}
\]
Moreover \(\Delta_n(\lambda)>0\) for every \(\lambda>0\); the smaller of the two exceptional vertex counts is always strictly more probable. For fixed odd \(n=2q+1\), the cancellation order is sharp:
\[
\Delta_n(\lambda)=\frac{2}{\pi}\frac{\binom{2q}{q}}{16^q}\lambda^n+O_n(\lambda^{n+2})\qquad(\lambda\downarrow0).
\]
Both exceptional probabilities increase strictly with \(\lambda\), whereas the middle probability decreases strictly. As \(\lambda\to\infty\), the probabilities for \(n+1,n+2,n+3\) tend respectively to
\[
\frac{n+1}{2n},\quad 0,\quad \frac{n-1}{2n}.
\]
In particular, the section-type probability at \(n+2\) determines the shear-to-height ratio by \(\lambda=\cot\bigl(\pi\Pr\{N=n+2\}/2\bigr)\). Neither this inverse law nor the exceptional probabilities depend on \(s,h\) separately.

## Assumptions and scope

The plane passes through the origin, which lies in the interior of \(K_{n,s,h}\). This is **not** the isotropic-translation-invariant random affine-plane model. The lateral displacement is along a base **vertex** direction. The condition \(s<\cos(\pi/n)\) places the apices' common vertical projection strictly inside the base polygon, ensuring that the \(3n\) genuine polyhedral edges are the \(n\) ring edges and the \(2n\) apex-to-ring edges. The normal is distributed uniformly on the unit sphere modulo sign; exceptional planes containing a vertex have measure zero. We assert no distribution for general apex orientations, nonregular bases, or translated planes.

## Proof

**1. Crossing-edge count.** For a plane containing no polyhedral vertex, the vertices of a planar section of a three-dimensional convex polyhedron are exactly its intersections with edges whose endpoint signs are opposite. Since the origin lies strictly inside the planar ring polygon, the line cut out by the section plane on the ring plane crosses precisely two ring edges. Let \(r\) ring vertices lie on the positive side, leaving \(n-r\) negative.

If the two apices have opposite signs, each ring vertex contributes exactly one crossing of an apex edge, so \(N=n+2\). If both apices are positive, then \(N=2+2(n-r)\); if both are negative, \(N=2+2r\). For regular even \(n\), the ring vertices come in antipodal pairs and \(r=n/2\), proving rigidity. For odd \(n=2q+1\), a generic open semicircle contains exactly \(q\) or \(q+1\) ring vertices, so the only possible vertex numbers are \(n+1,n+2,n+3\).

**2. Distribution of opposite apex signs.** Parameterize a Haar-uniform unit normal as \(u=(\sqrt{1-z^2}\cos\psi,\sqrt{1-z^2}\sin\psi,z)\). The variables \(z\) and \(\psi\) are independent, with \(z\) uniform on \([-1,1]\) and \(\psi\) uniform on \([0,2\pi)\). The apex dot products are \(s\sqrt{1-z^2}\cos\psi\pm hz\). They have the same sign exactly when
\[
|z|<\frac{\lambda|\cos\psi|}{\sqrt{1+\lambda^2\cos^2\psi}}.
\]
Consequently the conditional same-sign probability at azimuth \(\psi\) is \(f_\lambda(\psi)=\lambda|\cos\psi|/\sqrt{1+\lambda^2\cos^2\psi}\). Integrating over azimuth gives \(\Pr\{\text{same apex sign}\}=2\arctan\lambda/\pi\); the complementary event yields \(N=n+2\).

**3. Two exceptional counts.** Restrict azimuth to \([-\pi/2,\pi/2]\), using its symmetry under \(\psi\mapsto\psi+\pi\). The apex common sign, when present, agrees with the sign of \(\cos\psi\). The \(n\) successive intervals
\[
I_j=\left(\frac{(j-\tfrac12)\pi}{n},\frac{(j+\tfrac12)\pi}{n}\right),\qquad -q\le j\le q,
\]
alternate between a majority of ring vertex signs agreeing and disagreeing with the apex sign. Directly counting at \(\psi=0\) and crossing one ring-vertex orthogonality direction at a time shows that agreement occurs precisely when \((-1)^{q+j}=+1\). Agreement corresponds to \(N=n+1\); disagreement to \(N=n+3\). The antiderivative of \(\lambda\cos\psi/\sqrt{1+\lambda^2\cos^2\psi}\) on this interval is \(F_\lambda(\psi)\). Integrating the alternating intervals gives the displayed finite formula for \(\Delta_n=\Pr\{N=n+1\}-\Pr\{N=n+3\}\), and hence all three probabilities.

**4. Strict asymmetry and its exact vanishing order.** With \(k=\lambda/\sqrt{1+\lambda^2}\in(0,1)\), the globally convergent power series for arcsine and the trigonometric identity for odd powers of sine give the absolutely convergent Fourier expansion
\[
F_\lambda(\psi)=\sum_{r=0}^{\infty}(-1)^r B_r(k)\sin((2r+1)\psi),
\]
\[
B_r(k)=\sum_{j=r}^{\infty}
\frac{\binom{2j}{j}\binom{2j+1}{j-r}}{(2j+1)16^j}\,k^{2j+1}>0.
\]
Write \(b_r=(2r+1)B_r>0\). The odd-cosine Fourier series of \(F_\lambda'\) has coefficients \((-1)^r b_r\). Multiply by the standard square-wave series
\[
\operatorname{sgn}(\cos(n\psi))=\frac4\pi\sum_{m=0}^{\infty}\frac{(-1)^m}{2m+1}\cos((2m+1)n\psi),
\]
and integrate over \([-\pi/2,\pi/2]\). Orthogonality of distinct odd cosine frequencies and \(n=2q+1\) give
\[
\Delta_n(\lambda)=\frac2\pi\sum_{m=0}^{\infty}\frac{b_{q+mn}(k)}{2m+1}>0.
\]
This is strictly positive without numerical assumptions. The first term \(m=0\), \(j=q\) contributes \(\frac2\pi\binom{2q}{q}\lambda^n/16^q\); all other contributions are of higher order, yielding the claimed remainder \(O_n(\lambda^{n+2})\).

**5. Monotonicity and limits.** On the positive-cosine half-circle, the weight \(\lambda\cos\psi/\sqrt{1+\lambda^2\cos^2\psi}\) increases strictly in \(\lambda\). Each exceptional probability is the integral of this weight over a fixed positive-measure union of intervals; both therefore increase strictly. The middle probability has the stated decreasing elementary formula. When \(\lambda\to\infty\), the weight tends to one almost everywhere; among \(n\) equal-width intervals, \(q+1\) give \(n+1\) vertices and \(q\) give \(n+3\), proving the limits. The inverse formula follows algebraically.

## Verification

The reproducible standalone program `check_skew_bipyramid.py` constructs the **three-dimensional convex hull** of the stated vertices, extracts its edges from triangular facets, and for 18 choices of polygon order and shear ratio counts edge intersections for 85,000 independently simulated Haar normal directions per configuration. It separately checks the closed-form law against deterministic numerical quadrature to accuracy \(3\times10^{-13}\), and checks the sharp small-shear coefficient with 70-digit arithmetic for odd orders \(3,5,7,9\). It completed with the three success lines recorded in `VERIFICATION.md`. The deterministic calculations check finite cases and the stated coefficient numerically; the all-order conclusions are supplied by the analytical proof above.

## Relationship to prior work

Padrol and Pfeifle, *Polygons as sections of higher-dimensional polytopes* (first public preprint 2014-04-09), analyze **existence** of polygonal sections and in particular the possibility of a hexagonal section of a triangular bipyramid. This does not assign Haar probabilities to central sections, distinguish parity across all regular base orders, or imply the \(\lambda^n\) imbalance. De Loera, Lopez-Campos and Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope* (2024), investigate maximum attainable section sizes and vertex-count sequences over all affine hyperplanes, not the present shear-dependent central-plane distribution. Voss (1982) addresses frequencies of polygon types in random affine-plane sections of polyhedra; its abstract refers to certain simple polyhedra, but the full source was unavailable for comparison. The latter creates residual historical-priority uncertainty, not mathematical independence. Sukiasyan (1982) is another related archival source on random sections whose complete Russian text was not checked. The claims here are not purported to settle general stereological sampling.

## Limitations

The parameter restriction on \(s\), alignment with a base vertex, and origin-central slicing are essential to the stated theorem. Probabilities under randomly translated affine planes differ. The \(\lambda\to\infty\) limits are limits through nondegenerate polyhedra, not statements about a degenerate height-zero body. The work has not received independent audit. Earlier inaccessible full texts may affect priority; a failed literature search is not proof of novelty.

## References

1. A. Padrol and J. Pfeifle, *Polygons as sections of higher-dimensional polytopes*, arXiv:1404.2443, first submitted 2014-04-09, https://arxiv.org/abs/1404.2443 .
2. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419, first submitted 2024-12-17, https://arxiv.org/abs/2412.12419 .
3. K. Voss, *Frequencies of n-polygons in planar sections of polyhedrons*, Journal of Microscopy 128 (1982), 111–120, DOI 10.1111/j.1365-2818.1982.tb00443.x (abstract accessed; complete text unavailable).
4. G. S. Sukiasyan, *On random sections of polyhedra*, Doklady Akademii Nauk SSSR 263 (1982), 809–812, https://www.mathnet.ru/eng/dan45193 (metadata accessed; complete text not examined).
