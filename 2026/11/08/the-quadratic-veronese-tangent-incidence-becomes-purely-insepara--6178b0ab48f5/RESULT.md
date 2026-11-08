# The quadratic Veronese tangent incidence becomes purely inseparable in characteristic two

## Finding

Let \(k\) be an algebraically closed field, of arbitrary characteristic, and let \(V=\nu_2(\mathbb P^2_k)\subset\mathbb P^5_k\) be the quadratic Veronese surface, with coordinates \(A,B,C,D,E,F\) corresponding to \(x_0^2,x_1^2,x_2^2,x_0x_1,x_0x_2,x_1x_2\). Write
\[
\Delta=ABC-AF^2-BE^2-CD^2+2DEF.
\]
Then the **reduced** tangential variety \(\tau(V)\) equals the irreducible cubic hypersurface \(V(\Delta)\) over \(k\), in every characteristic. The natural tangent-incidence projection
\[
\pi:\{(x,z)\in V\times\mathbb P^5:z\in\mathbb P(T_xV)\}\longrightarrow \tau(V)
\]
is generically finite of **degree two** in every characteristic. Its function-field extension is separable if \(\operatorname{char} k\ne2\), and purely inseparable of degree two if \(\operatorname{char} k=2\). Thus a general geometric point has two distinct tangent centers in odd/zero characteristic, but only one geometric tangent center (a length-two geometric incidence fiber) in characteristic two. The degree of the image stays three across specialization; only the separability of tangent incidence changes.

## Assumptions and scope

The base field \(k\) is algebraically closed. Projective tangent spaces are embedded tangent planes to the smooth quadratic Veronese surface. The incidence scheme is the projectivization of the rank-three bundle of affine tangent cones, and its image is given the reduced scheme structure. The generic degree refers to the extension of rational function fields, not the number of rational points of a special fiber. Nothing is asserted about all special fibers or the complete branch scheme.

## Proof

**1. Cubic image.** With symmetric matrix
\[
M=\begin{pmatrix}A&D&E\\D&B&F\\E&F&C\end{pmatrix}
\]
the determinant is \(\Delta\). On the chart where the tangent center is \([1:s:t]\), every point of its affine tangent cone can be written (up to overall scaling, on the open chart \(A=1\)) with two velocity parameters \(u,v\):
\[
A=1,\quad B=s^2+2su,\quad C=t^2+2tv,\quad
D=s+u,\quad E=t+v,\quad F=st+tu+sv.
\]
Direct expansion gives \(\Delta=0\). The incidence is irreducible of dimension \(2+2=4\). At \(A=1\), eliminating \(B\) from \(\Delta=0\) gives
\[
B=\frac{CD^2-2DEF+F^2}{C-E^2}
\]
on \(C-E^2\ne0\); hence the cubic has a rational four-dimensional dense chart, is integral there, and its irreducible homogeneous closure is the determinant hypersurface. (It is also primitive and linear in \(B\) with relatively prime coefficient \(AC-E^2\) and constant term \(-AF^2-CD^2+2DEF\); hence \(\Delta\) is irreducible.) The subsequent generic-reconstruction computation shows the incidence image has dimension four, so its closure is exactly \(V(\Delta)\).

**2. Exact generic center equation.** Eliminate velocities using \(u=D-s\) and \(v=E-t\). The first three nonconstant coordinates give
\[
P(s)=s^2-2Ds+B=0,\qquad t^2-2Et+C=0.
\]
The last one gives \(F=Dt+Es-st\), so on \(D-s\ne0\),
\[
t=\frac{F-sE}{D-s}.
\]
Substitute into \(t^2-2Et+C=0\), clear denominators, and reduce modulo \(P(s)\). The remainder is exactly \(-\Delta\). Thus at the generic point of the cubic, every root of \(P\) yields exactly one center (and velocities); conversely every center satisfies \(P\). Consequently
\[
k(\operatorname{Inc})=k(V(\Delta))(s),\quad s^2-2Ds+B=0.
\]

**3. Quadratic polynomial is irreducible.** The affine generic-function field is
\[
K=k(C,D,E,F)
\]
because \(B\) is expressed rationally above. In \(K\),
\[
D^2-B=-\frac{(F-DE)^2}{C-E^2}.
\]
The element \(C-E^2\) is not a square in \(K\): it has valuation one at the irreducible prime divisor \(C-E^2=0\) in the polynomial UFD \(k[C,D,E,F]\). The numerator is a nonzero square and the denominator has odd valuation, also in characteristic two. Hence \(P(s)\) is irreducible, since for characteristic not two the square class of its discriminant is that of \(D^2-B\); in characteristic two it is \(s^2+B\) and \(B\) has the same nonsquare class as \(D^2-B\). The field-extension degree is exactly two.

**4. Separability transition.** If \(\operatorname{char} k\ne2\), then \(P'(s)=2(s-D)\) is not zero in the degree-two extension; \(P\) is separable. If \(\operatorname{char} k=2\), then \(P=s^2+B\) with derivative zero and \(B\) nonsquare in \(K\), so the extension is purely inseparable of degree two. Over an algebraic closure of the function field its unique geometric root is double, explaining the length-two tangent-center fiber. The generic incidence is a field extension, so this length is scheme-theoretic.

**5. Independent intersection-theoretic cross-check.** The rank-three bundle \(\mathcal E\) of affine tangent cones to the Veronese embedding fits in
\[
0\to\mathcal O_{\mathbb P^2}(-2)\to \mathcal E\to T_{\mathbb P^2}(-2)\to0.
\]
Using \(c(T_{\mathbb P^2}(-2))=1-h+h^2\), one gets \(c_1(\mathcal E)=-3h\), \(c_2(\mathcal E)=3h^2\), and its top Segre number is \(\int_{\mathbb P^2}(c_1^2-c_2)=6\). Since the image is cubic, this independently gives \(\deg\pi=6/3=2\).

## Verification

The attached `verify.py` checks the determinant under tangent parametrization, polynomial elimination, the exact nonsquare identity and Segre-degree calculation using symbolic integer algebra. It enumerates every rank-two matrix in the chart \(A=1\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), and counts their rational tangent centers; it gives 12 matrices with one center over \(\mathbb F_2\), 72 matrices with zero or two over \(\mathbb F_3\), and 600 matrices with zero or two over \(\mathbb F_5\). The saved `verify.out` ends `ALL_CHECKS_PASSED`. Finite field checks corroborate the infinite-field proof but are not substituted for it.

## Relationship to prior work

The equality between the tangential variety of the quadratic Veronese surface and its rank-at-most-two symmetric determinantal secant cubic is classical; it is **not** claimed here as original. Oeding–Raicu, *Tangential Varieties of Segre–Veronese Varieties* (arXiv:1111.6202, 2011), work in characteristic zero and explicitly discuss this secant–tangent coincidence; their statements do not imply the characteristic-two inseparability transition. Ballico, *On the dual variety in characteristic 2* (1990), concerns duality and conormal morphisms, not this specific tangent-incidence extension. Kaji, *Higher Gauss Maps of Veronese Varieties* (arXiv:1509.04935), addresses higher Gauss maps, distinct from this incidence projection; only its abstract was inspected, so possible indirect implications are a residual priority risk. The new content is the exact characteristic-dependent generic degree/separability statement with rational function-field certificate.

## Limitations

The proof controls the generic incidence field extension and its generic geometric fiber, not the global ramification or every special incidence fiber. Historical priority remains provisional because an exhaustive inspection of older positive-characteristic Veronese geometry is unavailable; absence from searches is not proof of novelty. No independent validation has been performed.

## References

1. L. Oeding and C. Raicu, *Tangential Varieties of Segre–Veronese Varieties*, arXiv:1111.6202 (first public version 2011-11-26), https://arxiv.org/abs/1111.6202.
2. E. Ballico, *On the dual variety in characteristic 2*, 1990 (full text inspected).
3. H. Kaji, *Higher Gauss Maps of Veronese Varieties*, arXiv:1509.04935 (abstract inspected only).
