# Parity-split infinitesimal width rigidity of centrally symmetric equilateral polygons

## Finding
Let \(m\ge 2\) be an integer and \(\ell>0\). Every strictly convex, centrally symmetric Euclidean polygon with exactly \(2m\) sides, all of length \(\ell\), has minimum Euclidean width bounded by
\[
 w(P)\le \ell\cot\left(\frac{\pi}{2m}\right).
\]
Equality holds if and only if \(P\) is a regular \(2m\)-gon (up to Euclidean congruence). Moreover, the first-order stability of this unique maximizer has an exact parity dichotomy. Parameterize its \(m\) unoriented side directions by \(\theta_i^0=\theta_0+i\pi/m\), with indices modulo \(m\), and let \(\theta_i(t)=\theta_i^0+t v_i+o(t)\) for any real vector \(v\). The one-sided derivative exists and is
\[
 \left.\frac{d}{dt}\right|_{t=0+}w(P(t))
 =\ell\min_{0\le i<m}(T_m v)_i,\qquad
 (T_m v)_i=\sum_{k=1}^{m-1}\cos\left(\frac{k\pi}{m}\right)(v_{i+k}-v_i).
\]
The right-hand derivative vanishes exactly when \(v\) is constant if \(m\) is odd, and exactly when \(v_i=a+b(-1)^i\) if \(m\) is even. Otherwise the derivative is strictly negative. For even \(m\), the sole nonrotational first-order neutral direction integrates to the explicit strictly convex family
\[
 \theta_i(t)=\theta_0+\frac{i\pi}{m}+t(-1)^i,
 \qquad |t|<\frac{\pi}{2m},
\]
whose minimum width obeys the exact nonlinear identity
\[
 \boxed{w(P(t))=\ell\cot\left(\frac{\pi}{2m}\right)
       -\frac{2\ell\sin^2 t}{\sin(\pi/m)}.}
\]
Thus these neutral directions lose width at the sharp quadratic rate \(2\ell\csc(\pi/m)t^2+O(t^4)\). In particular, \(2m\equiv2\pmod4\) gives first-order rigidity modulo rotation, whereas \(4\mid 2m\) gives a one-dimensional nonrotational neutral tangent.

## Assumptions and scope
Width is the least distance between two parallel supporting lines, over all orientations. Strict convexity means successive edges have distinct, strictly increasing directions, with all \(2m\) sides present. Central symmetry forces opposite sides to be parallel and equal, so every such polygon, up to translation, has the zonogon representation
\[
 P=\sum_{i=0}^{m-1}[0,\ell(\cos\theta_i,\sin\theta_i)],\qquad
 \theta_0<\theta_1<\cdots<\theta_{m-1}<\theta_0+\pi.
\]
Conversely every such choice produces a strictly convex centrally symmetric equilateral \(2m\)-gon. A permitted differentiable deformation varies the ordered side directions with the same fixed side lengths; translation and common rotation are inessential. The derivative formula is one-sided because minimum width need not be differentiable at the regular configuration. No claim is made for arbitrary noncentrally symmetric equilateral polygons.

## Proof
**1. Exact facet-normal width formula.** For any unit vector \(u\), the zonogon width is \(\ell\sum_j|u\cdot(\cos\theta_j,\sin\theta_j)|\). Between consecutive edge-normal orientations the supporting vertices are fixed, so this width is a positive function \(A\cos\phi+B\sin\phi\) satisfying \(w''(\phi)=-w(\phi)<0\). Its minimum in each such interval therefore lies at an endpoint: a normal to an edge. Put \(\theta_{i+m}=\theta_i+\pi\). The \(m\) distinct candidate widths, divided by \(\ell\), are
\[
 f_i=\sum_{k=1}^{m-1}\sin(\theta_{i+k}-\theta_i),\qquad
 \frac{w(P)}\ell=\min_{0\le i<m} f_i.
\]
All sine arguments lie strictly between zero and \(\pi\), which also fixes their signs and eliminates any normalization ambiguity.

**2. Global maximum and equality rigidity.** Let the positive cyclic gaps be \(g_i=\theta_{i+1}-\theta_i\), with \(\sum_{i=0}^{m-1}g_i=\pi\), and put \(s_{i,k}=g_i+\cdots+g_{i+k-1}\). Each fixed-\(k\) family satisfies \(\sum_i s_{i,k}=k\pi\). Strict concavity of \(\sin s\) on \((0,\pi)\) gives
\[
 \frac{w(P)}\ell\le\frac1m\sum_i f_i
 =\sum_{k=1}^{m-1}\frac1m\sum_i\sin s_{i,k}
 \le \sum_{k=1}^{m-1}\sin\left(\frac{k\pi}{m}\right)
 =\cot\left(\frac{\pi}{2m}\right).
\]
The final finite sine sum follows from the geometric-series or sine-sum identity. Equality in the displayed inequalities requires equality in the strictly concave \(k=1\) Jensen term, so all \(g_i=\pi/m\). This is precisely the regular \(2m\)-gon. Conversely that polygon has every \(f_i\) equal to the bound.

**3. First variation.** At equally spaced directions every candidate \(f_i\) is active, so the directional derivative of their finite minimum is the minimum of their derivatives. Differentiating the preceding exact formula yields the stated skew-circulant \(T_m\). Its row sums and column sums vanish: \(\sum_i(T_m v)_i=0\), and hence \(\min_i(T_m v)_i<0\) whenever \(T_m v\ne0\).

On the Fourier vector \(v_j=e^{2\pi\mathrm{i}qj/m}\), \(0\le q<m\), the operator has eigenvalue
\[
 \lambda_q=
 \sum_{k=1}^{m-1}\cos\left(\frac{k\pi}{m}\right)
    \left(e^{2\pi\mathrm{i}qk/m}-1\right)
 =\frac{\mathrm{i}}2\left[
   \cot\left(\frac{(2q-1)\pi}{2m}\right)
  +\cot\left(\frac{(2q+1)\pi}{2m}\right)\right].
\]
To verify the second equality, write \(2\cos a\,e^{2\mathrm{i}qa}=e^{\mathrm{i}(2q+1)a}+e^{\mathrm{i}(2q-1)a}\), sum each finite geometric progression, and use \(\sum_{k=1}^{m-1}\cos(k\pi/m)=0\). The cotangent sum vanishes exactly when \(\sin(2q\pi/m)=0\), because its denominator is nonzero for every integer \(q\). Thus \(\lambda_q=0\) precisely for \(q=0\) and, when \(m\) is even, \(q=m/2\). The corresponding real kernel is respectively the constant vectors or their span with \(((-1)^i)_i\). Every vector outside this kernel has a strictly negative first-order width derivative by the zero-sum property, proving the complete infinitesimal classification.

**4. Exact neutral deformation.** Suppose \(m\) is even. The stated angles have positive cyclic gaps \(\pi/m\pm2t\), so they define the required polygons for \(|t|<\pi/(2m)\). In each facet formula, an even increment \(k\) leaves the angle difference \(k\pi/m\) unchanged, while an odd increment changes it by \(\pm2t\). The odd-\(k\) cosine contributions cancel in pairs under \(k\mapsto m-k\), so all facet widths are equal. Their common decrement is
\[
 \ell(1-\cos 2t)\sum_{\substack{1\le k<m\\k\ \mathrm{odd}}}
 \sin\left(\frac{k\pi}{m}\right)
 =\ell(1-\cos2t)\csc\left(\frac\pi m\right)
 =\frac{2\ell\sin^2t}{\sin(\pi/m)}.
\]
The odd-sine sum identity follows from summing \(\sin((2j+1)\pi/m)\) over \(j=0,\ldots,m/2-1\). This proves the exact formula and its Taylor expansion for all even \(m\), including the four-sided case.

## Verification
Run `python verify_geometry.py` using only Python's standard library. It recomputes the edge-normal width formula from independent absolute projection sums, compares it with sampled arbitrary normals, independently evaluates the Fourier eigenvalues and the cotangent formula, tests finite-difference first variations, and checks the exact alternating-family formula. The deterministic checker passed 9,317 numerical comparisons for \(m=2,\ldots,23\), with random positive cyclic gaps and perturbations. This finite experiment is a diagnostic only; the preceding analytic argument establishes the universal statements.

## Relationship to prior work
The maximum-width problem under a perimeter constraint is classical. Audet, Hansen and Messine (2009) give a sharp general upper bound and identify global unrestricted optimizers for many side counts. Fejes Tóth (2022, especially its width discussion) surveys the remaining polygonal extremal questions, including the equilateral width issue. Our result concerns the naturally narrower class of **simultaneously centrally symmetric and equilateral** polygons; it neither recovers their unrestricted sharp constant nor solves the noncentrally symmetric equilateral problem. The Jensen extremizer step is a standard concavity method. The separate contribution evaluated here is the exact **parity-dependent first variation for the minimum over all support directions**, including the unique nonrotational nullmode and its exact nonlinear loss. Related results on equiangular opposite-parallel polygons control different support-number observables; results on equal-radius angular vertex grids concern an orthogonal constraint and area instead of width. Explicit scientific overlaps and residual literature risks are recorded separately.

## Limitations
The class is planar, strictly convex, centrally symmetric and equilateral, with a fixed even number of sides. The derivative concerns fixed-side-length variations near the regular polygon; it is not a uniform quantitative stability constant for arbitrary nonregular shapes. The second-order identity is specific to the alternating path when \(m\) is even; it does not assert a universal second-order expansion in all perturbation directions. The identified priority is provisional because an older result phrased through zonogon normal-direction perturbations could be equivalent even if not indexed under polygonal width.

## References
1. G. Fejes Tóth, *Finite variations on the isoperimetric problem*, arXiv:2202.09920v1 (first public 2022-02-20), https://arxiv.org/html/2202.09920v1.
2. C. Audet, P. Hansen and F. Messine, *Isoperimetric Polygons of Maximum Width*, Discrete & Computational Geometry 41 (2009), 45–60, DOI:10.1007/s00454-008-9103-9, https://paperity.org/p/11589983/isoperimetric-polygons-of-maximum-width.
3. C. Audet and J. Ninin, *Maximal perimeter, diameter and area of equilateral unit-width convex polygons*, original preprint (2010), https://www.gerad.ca/Charles.Audet/PUB/largeur_GERAD.pdf.
4. *Sharp pointwise width stability for equiangular polygons with parallel opposite sides*, publicly indexed mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-pointwise-width-stability-for-equiangular-polygons-with-pa--dd6fcbc2a54c.
5. *Parity rigidity and sharp area bounds for equilateral polygons on a regular radial grid*, publicly indexed mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-parity-rigidity-and-sharp-area-bounds-for-equilateral-polygons-o--5e01ff137083.
