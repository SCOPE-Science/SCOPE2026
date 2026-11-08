# All-power distance optimization for fixed-volume solid circular cylinders

## Finding
Let \(C_{R,h}=\{(x,z)\in\mathbb R^2\times[0,h]:\lVert x\rVert\le R\}\), with \(R,h>0\) and fixed volume \(V=\pi R^2h\). Sample \(X,Y\) independently and uniformly by **three-dimensional volume** and put \(D=\lVert X-Y\rVert_2\). Let \(q=h/R\), and let \(q_p\) minimize \(\mathbb E[D^p]\) subject to the volume constraint.

**Theorem.** For every real \(p>0\), the minimizer \(q_p\in(0,\infty)\) exists and is unique. The first two nontrivial even powers have distinct exact optimizers,
\[
q_2=\sqrt3,\qquad q_4=\sqrt{\frac{5(\sqrt{33}-1)}8}.
\]
The high-power optimizer tends to the diameter-optimal cylinder, with a sharp first correction:
\[
\boxed{q_p=\sqrt2+\frac{9\sqrt2}{4p}+O(p^{-2})\quad(p\to\infty).}
\]
Thus the volume-normalized second and fourth distance moments are minimized by different cylinder shapes, and the optimal aspect ratio approaches \(\sqrt2\) *from above* as the distance power diverges. The theorem is about ambient Euclidean distances within the **solid** cylinder, not intrinsic distances on its lateral surface.

## Assumptions and scope
The cylinder is a solid, with full end disks, positive \(R,h\), and its volume is fixed at an arbitrary \(V>0\). Points are independent, exactly volume-uniform, and distance means ambient Euclidean distance. No integer restriction on \(p\) is imposed. All minimizations range over **every positive aspect ratio** \(q=h/R\), not over a sampled mesh or a compact interval. Denote the dimensionless planar separation by \(T=\lVert X_{\perp}-Y_{\perp}\rVert/R\) and the dimensionless vertical separation by \(U=|X_z-Y_z|/h\). Their supports are \([0,2]\) and \([0,1]\), and they are independent.

The exact densities are
\[
f_T(t)=\frac{4t}{\pi}\left[\arccos\left(\frac t2\right)-\frac t2\sqrt{1-\frac{t^2}4}\right],\quad 0<t<2;\qquad
f_U(u)=2(1-u),\quad0<u<1.
\]
In particular, \(\mathbb E[T^2]=1\), \(\mathbb E[T^4]=5/3\), \(\mathbb E[U^2]=1/6\), \(\mathbb E[U^4]=1/15\). Writing \(q=h/R\), volume conservation yields \(R=(V/(\pi q))^{1/3}\), and hence
\[
\frac{\mathbb E[D^p]}{(V/\pi)^{p/3}}
=q^{-p/3}\int_0^2\!\int_0^1(t^2+q^2u^2)^{p/2}f_T(t)f_U(u)\,du\,dt.\tag{1}
\]

## Proof
**1. Exact reduction.** Cross-sectional and height coordinates of a volume-uniform point are independent. The difference of two uniform disk points has vector density equal to the disk overlap area divided by \(\pi^2\). The overlap lens at separation \(t\) has area \(2\arccos(t/2)-(t/2)\sqrt{4-t^2}\). Multiplying by the polar Jacobian \(2\pi t\) gives the stated \(f_T\). Two independent uniform height coordinates have absolute difference density \(2(1-u)\). This proves (1), including independence and normalization.

**2. Strict uniqueness for every power.** Set \(s=\log q\), \(A=T^2\), \(B=U^2\). Except on a null set, \(A,B>0\). After removing the fixed volume factor, the integrand in the objective is
\[
\bigl(Ae^{-2s/3}+Be^{4s/3}\bigr)^{p/2}.
\]
For fixed \(A,B>0\), the logarithm of this expression has strictly positive second derivative in \(s\) (it is a positive multiple of a two-term log-sum-exp with different slopes). Its integral is strictly log-convex in \(s\): Hölder's inequality transfers log-convexity, and strict pointwise convexity yields strictness. As \(s\to-\infty\), the first positive term diverges in expectation, while as \(s\to+\infty\), the second diverges. Thus a global minimizer exists, is interior, and is unique for **every** \(p>0\). Differentiation under the integral also gives the exact characterization
\[
\frac{\mathbb E\left[(T^2+q_p^2U^2)^{p/2}\frac{q_p^2U^2}{T^2+q_p^2U^2}\right]}
{\mathbb E[(T^2+q_p^2U^2)^{p/2}]}=\frac13.\tag{2}
\]
There are no other positive stationary aspect ratios.

**3. Algebraic benchmarks.** Integrating the second and fourth powers in (1), using independence, gives
\[
M_2(q)=q^{-2/3}\left(1+\frac{q^2}6\right),\qquad
M_4(q)=q^{-4/3}\left(\frac53+\frac{q^2}3+\frac{q^4}{15}\right),\tag{3}
\]
where \(M_p=\mathbb E[D^p]/(V/\pi)^{p/3}\). For \(p=2\), differentiation gives \(q^2=3\). For \(p=4\), writing \(x=q^2\) gives \(4x^2+5x-50=0\). The unique positive root is \(x=5(\sqrt{33}-1)/8\). Strict convexity in step 2 proves these are the global minimizers, not merely stationary points.

**4. High-power limit.** On the support of \((T,U)\), the essential supremum of \(\sqrt{T^2+q^2U^2}\) is \(\sqrt{4+q^2}\), so the \(L^p\)-to-\(L^\infty\) limit gives
\[
\lim_{p\to\infty}M_p(q)^{1/p}=q^{-1/3}\sqrt{4+q^2}=:L(q).
\]
The function \(L(q)\) diverges at zero and infinity, and has its unique minimum at \(q_\infty=\sqrt2\). For \(p\ge1\), the \(L^p\) norms dominate the first moment, which diverges at both aspect-ratio endpoints, uniformly in \(p\). This bounds the optimizing \(q_p\) away from the endpoints. Monotonicity of \(L^p\) norms, plus compactness and uniqueness of the minimizer of \(L\), proves \(q_p\to\sqrt2\).

**5. First high-power correction.** The two separation densities have the following exact endpoint behavior, uniformly with one differentiable remainder on fixed endpoint neighborhoods:
\[
f_T(2-v)=\frac{16}{3\pi}v^{3/2}\bigl(1+O(v)\bigr),\qquad f_U(1-w)=2w,\qquad(v,w\downarrow0).
\]
For \(q\) in any compact subinterval of \((0,\infty)\), inserting \(t=2-v\), \(u=1-w\) into the double integral in (1) gives the boundary Laplace integral with exponent
\[
\frac p2\log\frac{t^2+q^2u^2}{4+q^2}
=-p\frac{2v+q^2w}{4+q^2}+O\bigl(p(v+w)^2\bigr).
\]
The leading two independent gamma integrals (indices \(5/2\) and \(2\)) give, uniformly in \(q\) on such compact sets,
\[
\mathbb E[(T^2+q^2U^2)^{p/2}]
=(4+q^2)^{p/2}p^{-9/2}
\frac{\sqrt{2/\pi}(4+q^2)^{9/2}}{q^4}
\bigl(1+O(p^{-1})\bigr).\tag{4}
\]
Here the expansion and its first \(q\)-derivative are uniform: split the square into a fixed small endpoint neighborhood and its exponentially negligible complement, then use \(v,w=O(p^{-1})\), the analytic endpoint expansions, and gamma domination. Consequently
\[
\log M_p(q)=p\left[\frac12\log(4+q^2)-\frac13\log q\right]
-\frac92\log p+\log\left(\frac{\sqrt{2/\pi}(4+q^2)^{9/2}}{q^4}\right)+O(p^{-1})
\]
with a uniform first derivative near \(q=\sqrt2\). The first bracket's derivative vanishes at \(\sqrt2\), and its second derivative there equals \(2/9\). The derivative of the remaining \(q\)-dependent logarithm at \(\sqrt2\) equals \(-\sqrt2/2\). The unique stationary point therefore satisfies
\[
q_p-\sqrt2=-\frac{-\sqrt2/2}{p(2/9)}+O(p^{-2})
=\frac{9\sqrt2}{4p}+O(p^{-2}),
\]
as claimed. Smooth higher-order endpoint expansions justify the displayed \(O(p^{-2})\) remainder.

## Verification
A standalone reproducibility script `verify.py` performs Gauss--Legendre integration of the independent disk/interval densities, checks normalization and all four required even moments, solves (2) for powers \(2,4,100,200,400\), checks the asymptotic coefficient, and separately samples 350,000 independent **volume-uniform** point pairs using Cartesian-coordinate geometry. On the current package, it prints `CYLINDER_VOLUME_DISTANCE_UNIQUENESS_ASYMPTOTICS_OK 350000`. This is numerical corroboration of the explicit proof, **not** proof of uniqueness for infinitely many powers or of the Laplace remainder. The proof uses no empirical hypothesis.

## Relationship to prior work
Hammersley's 1951 and 1952 papers develop distance-function integration over solid right circular cylinders; these are direct antecedents for the **integral**, not claimed as new here. The present statement concerns a different operation: optimizing the complete positive-power moment family over **every aspect ratio at fixed volume**, including its unique optimizer and the explicit high-power shift. Hammersley's full papers were inaccessible in this review; this is a substantive historical-priority limitation, and the novelty assessment is provisional. Tu and Fischbach (arXiv:math-ph/0201046, full HTML §§II,V.1 inspected) supply the unit-disk distance density and ball moment methods, but treat spherical objects of fixed shape, not optimized product cylinders. Mathai--Moschopoulos--Pederzoli treat the cube and its distance moments, not variable solid cylinders. García-Pelayo's general even-moment identities may recover the two low-order polynomials, but cannot alone supply positive noninteger powers, strict all-power aspect-ratio optimization or the asymptotic correction without additional analysis. Results on **intrinsic lateral-surface** cylinder distances are not statements about independent three-dimensional volume-uniform samples.

## Limitations
The asymptotic expansion concerns \(p\to+\infty\), not a claim that \(q_p\) is monotone in \(p\); no monotonicity over all positive powers is proved. No optimality over noncircular solids, arbitrary three-dimensional convex bodies, or cylinders with fixed surface area is asserted. This has not undergone independent mathematical validation. Historical uniqueness is not certified because complete full text of the two highly relevant Hammersley papers was unavailable.

## References
1. J. M. Hammersley, *On a certain type of integral associated with circular cylinders*, Proc. Royal Soc. A **210** (1951), 98--110. DOI: 10.1098/rspa.1951.0233. First published 1951-12-07.
2. J. M. Hammersley, *Lagrangian integration coefficients for distance functions taken over right circular cylinders*, J. Math. Phys. (MIT) **31** (1952), 139--150. DOI: 10.1002/sapm1952311139.
3. Shu-Ju Tu and E. Fischbach, *Random Distance Distribution for Spherical Objects: General Theory and Applications to n-Dimensional Physics*, arXiv:math-ph/0201046 (first submitted 2002-01-22), especially §§II,V.1.
4. A. M. Mathai, P. Moschopoulos and G. Pederzoli, *Distance between random points in a cube*, Statistica **59** (1999), 61--81. DOI: 10.6092/issn.1973-2201/1104.
5. R. García-Pelayo, *Moments of the distribution of distance*, J. Math. Phys. **52** (2011), 033505; erratum **54** (2013), 099901. DOI: 10.1063/1.3559719.
