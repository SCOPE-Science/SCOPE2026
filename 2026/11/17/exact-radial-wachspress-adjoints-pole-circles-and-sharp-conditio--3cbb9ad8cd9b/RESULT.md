# Exact radial Wachspress adjoints, pole circles, and sharp conditioning for every regular polygon

## Finding

For every integer \(n\ge3\), let \(P_n\subset\mathbb R^2\) be the regular \(n\)-gon of circumradius one centered at the origin. Write \(c_n=\cos(\pi/n)\), \(u_j=(\cos(2\pi j/n),\sin(2\pi j/n))\), and \(\ell_j(x)=c_n-u_j\cdot x\) for \(0\le j<n\), with subscripts modulo \(n\). Define the unscaled Wachspress vertex numerators and denominator by
\[
 W_j(x)=\prod_{k\notin\{j-1,j\}}\ell_k(x),\qquad Q_n(x)=\sum_{j=0}^{n-1}W_j(x).
\]
The exact identity, valid as a polynomial identity on the **whole affine plane**, is
\[
 \boxed{Q_n(x)=n c_n^{n-2}\prod_{k=2}^{\lfloor(n-1)/2\rfloor}
 \left(1-\frac{\cos^2(k\pi/n)}{c_n^2}\|x\|^2\right).}
\]
An empty product equals one (\(n=3,4\)). For every \(n\ge5\), the real zero set consists **exactly** of \(\lfloor(n-3)/2\rfloor\) distinct concentric circles of radii
\[
 \rho_{n,k}=\frac{c_n}{\cos(k\pi/n)},\quad
 k=2,\ldots,\lfloor(n-1)/2\rfloor.
\]
Each circle is a simple factor in the variable \(\|x\|^2\) and a genuine pole component of the rational Wachspress coordinate system \(\lambda_j=W_j/Q_n\) at all but finitely many points. The maximal origin-centered open disk containing no denominator zeros has radius \(\rho_{n,2}>1\); for \(n=3,4\) it is the entire plane. Its sharp large-order deficit is
\[
 \rho_{n,2}-1=\frac{3\pi^2}{2n^2}+O(n^{-4}).
\]
Moreover, \(Q_n\) is strictly radially decreasing on \(0<\|x\|<\rho_{n,2}\) when \(n\ge5\). On \(P_n\), its exact maximum is at the origin, its exact minimum occurs only at the vertices, and
\[
 \boxed{\frac{\max_{x\in P_n}Q_n(x)}{\min_{x\in P_n}Q_n(x)}
 =\frac{2^n c_n^{n-2}\sin^2(\pi/n)}{n}
 \sim\frac{\pi^2 2^n}{n^3}.}
\]
This ratio is one for \(n=3,4\). Finally, the empirical distribution of the \(\lfloor(n-3)/2\rfloor\) distinct zero-circle radii converges, as \(n\to\infty\), to the probability distribution on \([1,\infty)\) with cumulative distribution function \(F(R)=(2/\pi)\arccos(1/R)\) for \(R\ge1\), and \(F(R)=0\) for \(R<1\). The farthest zero circle has radius asymptotic to \(2n/\pi\) for odd \(n\) and \(n/\pi\) for even \(n\).

## Assumptions and scope

All products are over the normalized supporting forms \(\ell_j=c_n-u_j\cdot x\) of the regular convex polygon. The vertex indexed by \(j\) is \(v_j=(\cos((2j-1)\pi/n),\sin((2j-1)\pi/n))\), the common intersection of \(\ell_{j-1}=0\) and \(\ell_j=0\). Because adjacent outward-normal determinants have equal nonzero absolute value, the usual Wachspress numerators have the same constant factor and the normalized coordinate system is exactly \(\lambda_j=W_j/Q_n\). All claims refer to these explicitly defined polynomials, not to arbitrary rational barycentric systems. The pole assertion means generic poles along the real zero circles, not singularities at every single point. The distribution concerns each distinct circle once, not a distribution of points on its circumference.

## Proof

**Polynomial degree and radiality.** The standard affine-precision identity for Wachspress coordinates is
\[
 \sum_{j=0}^{n-1}v_j W_j(x)=x\sum_{j=0}^{n-1}W_j(x)=x Q_n(x).
\]
It holds on the interior because the normalized Wachspress coordinates are barycentric and hence everywhere as a polynomial identity. Every \(W_j\) has total degree \(n-2\). Comparing the polynomial degrees on the two sides of affine precision shows \(\deg Q_n\le n-3\) (and \(Q_n\not\equiv0\), since \(Q_n(0)=n c_n^{n-2}>0\)). A rotation by \(2\pi/n\) cyclically permutes the \(\ell_j\) and therefore fixes \(Q_n\). In complex variables \(z=x_1+i x_2\) and \(\overline z=x_1-i x_2\), a monomial \(z^a\overline z^b\) of total degree below \(n\) is invariant under that rotation only if \(a-b\equiv0\pmod n\), hence only if \(a=b\). Consequently, \(Q_n(x)=f_n(\|x\|^2)\) for a real one-variable polynomial with \(\deg f_n\le\lfloor(n-3)/2\rfloor\).

**Forcing all factors.** Fix an integer \(k\) with \(2\le k\le\lfloor(n-1)/2\rfloor\). The two nonadjacent supporting lines \(\ell_0=0\) and \(\ell_k=0\) intersect at the point
\[
 x_k=\frac{c_n}{\cos(k\pi/n)}
 (\cos(k\pi/n),\sin(k\pi/n)),
\]
whose norm is \(\rho_{n,k}=c_n/\cos(k\pi/n)\). (Equivalently, \(x_k=(c_n,c_n\tan(k\pi/n))\).) Every numerator \(W_j\) contains at least one of the two factors \(\ell_0,\ell_k\), because a numerator omits only two **adjacent** factors. Thus \(Q_n(x_k)=0\). All these radii are distinct and positive; their number is \(\lfloor(n-3)/2\rfloor\). This exhausts the allowed degree of \(f_n\); its constant term \(Q_n(0)=n c_n^{n-2}\) gives the displayed product. No limiting or numerical argument is used.

**Zero-free radius and genuine pole circles.** For each \(n\ge5\), \(c_n>\cos(2\pi/n)>0\), so the smallest \(\rho_{n,k}\) is \(\rho_{n,2}>1\). The product has no other real zeros. Each circular quadratic factor \(\|x\|^2-\rho_{n,k}^2\) is irreducible over the real polynomial ring in two variables; none can divide any \(W_j\), since each \(W_j\) is a product of affine-linear factors. Hence generic points on every circle are genuine poles of each rational coordinate whose numerator is nonzero there. Taylor expansion of \(\cos(\pi/n)/\cos(2\pi/n)\) yields the stated \(3\pi^2/(2n^2)+O(n^{-4})\) barrier.

**Monotonicity, extrema, and sharp ratio.** For \(0<r<\rho_{n,2}\), all factors \(1-r^2/\rho_{n,k}^2\) are positive and strictly decrease in \(r\). Thus \(Q_n\) is strictly decreasing on this interval if \(n\ge5\). As \(P_n\) lies in the closed unit disk and meets the unit circle only at its vertices, the maximum and minimum are as asserted. At vertex \(v_0\), only \(W_0\) is nonzero, giving
\[
 Q_n(v_0)=\prod_{j=1}^{n-2}
 \bigl[\cos(\pi/n)-\cos((2j+1)\pi/n)\bigr]
 =2^{n-2}\prod_{j=1}^{n-2}\sin(j\pi/n)\sin((j+1)\pi/n).
\]
Using \(\prod_{j=1}^{n-1}\sin(j\pi/n)=n/2^{n-1}\) gives
\[
 Q_n(v_0)=\frac{n^2}{2^n\sin^2(\pi/n)}.
\]
Divide \(Q_n(0)=n c_n^{n-2}\) by this quantity. The large-order asymptotic follows from \(c_n^{n-2}=1+O(n^{-1})\) and \(\sin^2(\pi/n)=\pi^2n^{-2}(1+O(n^{-2}))\).

**Full zero-circle distribution.** With \(k/n\) asymptotically uniform on \((0,1/2)\), \(\rho_{n,k}=c_n/\cos(\pi k/n)\) converges in empirical distribution to \(1/\cos(\pi U)\) for \(U\) uniform on \((0,1/2)\). For finite \(R\ge1\), its distribution function is \((2/\pi)\arccos(1/R)\). The largest index \(k=\lfloor(n-1)/2\rfloor\) gives exactly \(c_n/\sin(\pi/(2n))\) for odd \(n\), and \(c_n/\sin(\pi/n)\) for even \(n\), proving the parity-sensitive extreme asymptotics.

## Verification

The accompanying `verify.py` uses only the Python standard library and independently assembles the products of facet forms, checks the full radial factorization and affine precision for every \(3\le n\le35\), tests the residual-line intersection locations, and checks the sharp vertex value. It returned **2556 successful finite assertions**. Additionally, independent 65-digit arithmetic for \(3\le n\le29\) passed **1164 finite checks**. Neither computation proves the all-order theorem; the algebraic proof above supplies the universal quantifiers.

## Relationship to prior work

Baumbach and Winter (2026) develop rational generalized barycentric coordinates and adjoint denominator degrees, which motivate studying explicit denominator geometry. Kohn and Ranestad (2019) establish general adjoint vanishing on residual face intersections and provide a projective-geometric framework. Kohn et al. (2021) characterize the real topology of adjoints for convex polygons; its abstract was accessible, but the full large PDF could not be materially inspected here. A separately indexed 2026 all-polygon theorem already identifies the **minimum possible denominator degree** \(n-3\) in noncentrally symmetric cases and \(n-4\) in centrally symmetric cases. These degree assertions and the generic residual-arrangement theory are prior work, not claimed as new. The specific claim is the explicit all-order *radial factorization*, exact zero/pole circles, sharp continuation barrier, exponential denominator range, and circle-radius distribution. Targeted literature and research-index searches did not identify a statement covering this combined exact classification; unindexed equivalent derivations remain a historical-priority risk.

## Limitations

This is a result only for ordinary Wachspress coordinates of centered regular convex planar polygons (or their trivial affine transports), not for general polygons or arbitrary generalized barycentric systems. The sharp ratio measures variation of a **fixed normalized polynomial denominator**, not numerical conditioning of every possible floating-point implementation. The analytic continuation barrier concerns the common denominator and generic rational poles; cancellation at isolated intersection points is not excluded. Prior art may include an equivalent specialization of classical general adjoint theory, especially in full text not accessible in this review. Independent validation has not been performed.

## References

1. T. Baumbach and M. Winter, *Rational barycentric coordinates and low degree adjoints*, arXiv:2611.02110v1 (first posted 2026-11-01), https://arxiv.org/abs/2611.02110.
2. K. Kohn and K. Ranestad, *Projective geometry of Wachspress coordinates*, arXiv:1904.02123v3 (2019), https://arxiv.org/abs/1904.02123.
3. K. Kohn, R. Piene, K. Ranestad, F. Rydell, B. Shapiro, R. Sinn, M.-S. Sorea, S. Telen, *Adjoints and Canonical Forms of Polypols*, arXiv:2108.11747 (2021), https://arxiv.org/abs/2108.11747.
4. *Wachspress denominators have minimum degree on every convex polygon*, public mathematical research record dated 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-wachspress-denominators-have-minimum-degree-on-every-convex-poly--7b4aad67706d.
