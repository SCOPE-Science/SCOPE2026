# Cyclotomic rigidity and exact diameter-preserving ascent of even regular small polygons

## Finding

Let \(n=2m\ge4\) and let \(v_j=\frac12\exp(2\pi i j/n)\), with indices modulo \(n\), be a regular convex polygon of diameter one. Consider ordered configurations
\[
p_j=v_j+c_{j\bmod m},\qquad c_0,\ldots,c_{m-1}\in\mathbb C.
\]
Every original antipodal diameter vector is preserved **exactly**: \(p_{j+m}-p_j=v_{j+m}-v_j\). The full classification of configurations in this class whose \(n\) side lengths are equal is as follows. Either all \(c_j\) coincide, or there are \(t>0\) and signs \(\sigma_0,\ldots,\sigma_{m-1}\in\{-1,1\}\) satisfying
\[
\sum_{j=0}^{m-1}\sigma_j\exp(2\pi i j/n)=0,
\]
and, writing \(\zeta=\exp(2\pi i/n)\), their successive pair shifts obey
\[
c_{j+1}-c_j=t\sigma_j w\zeta^j\quad(0\le j<m),
\qquad w=\frac{i(v_1-v_0)}{|v_1-v_0|},\quad c_m=c_0.
\]
Conversely every such choice gives equal side lengths, exactly
\[
\ell(t)=\sqrt{\sin^2(\pi/n)+t^2},\qquad L(t)=n\ell(t).
\]
There is a nonconstant configuration in this class **if and only if \(n\) is not a power of two**. For each such \(n\), nonconstant configurations exist for every sufficiently small \(t>0\) as strictly convex equilateral polygons of diameter exactly one. Their perimeter strictly exceeds that of the regular polygon by
\[
L(t)-L(0)=\frac{n}{2\sin(\pi/n)}t^2+O_n(t^4).
\]
If \(n\) is a power of two, the only equal-side-length configurations in this diameter-*vector*-preserving class are common translations of the regular polygon. The latter assertion is not a statement about all nearby equilateral small polygons.

## Assumptions and scope

The Euclidean plane is identified with \(\mathbb C\). The original polygon is regular, centered at zero, with circumradius \(1/2\); this is possible because \(n\) is even and its diameters join opposite vertices. A *paired translation* applies a common arbitrary displacement \(c_j\) to the original antipodal pair of vertices indexed by \(j\) and \(j+m\). The displacement class is defined by vector equality, not only by preservation of diameter lengths. There is no a priori convexity or diameter bound in the algebraic classification; these are separately established for small nonzero \(t\) in the construction.

## Proof

**1. Pairing opposite edges.** Let \(a_j=v_{j+1}-v_j\), \(0\le j<m\). Since \(v_{j+m}=-v_j\), the opposite edge vector is \(-a_j\). Put \(d_j=c_{j+1}-c_j\) and impose the periodic convention \(c_m=c_0\). The two edge vectors in the corresponding antipodal positions are \(a_j+d_j\) and \(-a_j+d_j\). Equality of their lengths implies
\[
|a_j+d_j|^2-|-a_j+d_j|^2=4\operatorname{Re}(\overline{a_j}d_j)=0.
\]
Thus \(d_j\) is perpendicular to \(a_j\). All \(|a_j|=\ell_0=\sin(\pi/n)\). Since the entire polygon is equilateral, \(|a_j+d_j|^2=\ell_0^2+|d_j|^2\) is independent of \(j\), forcing a common \(|d_j|=t\ge0\). If \(t=0\), the \(c_j\) are all identical. If \(t>0\), because \(a_j=a_0\zeta^j\), perpendicularity gives exactly \(d_j=t\sigma_j w\zeta^j\) with \(w=i a_0/|a_0|\) and \(\sigma_j\in\{-1,1\}\). Conversely, all these displacements make both sides of every antipodal edge pair have length \(\sqrt{\ell_0^2+t^2}\).

**2. Cyclotomic closure.** The displacements derive from cyclic \(c_0,\ldots,c_{m-1}\) precisely when \(\sum_{j=0}^{m-1}d_j=0\). Dividing by \(tw\), this is
\[
Q(\zeta)=0,\qquad Q(x)=\sum_{j=0}^{m-1}\sigma_j x^j.
\]
When \(m=2^s\), \(\zeta\) is a primitive \(2^{s+1}\)-st root of unity, with irreducible minimal polynomial \(\Phi_{2^{s+1}}(x)=x^m+1\). Every nonzero \(Q\) above has degree \(m-1\); it cannot vanish at \(\zeta\). This proves rigidity for all powers of two, including \(n=4\).

If \(m\) is not a power of two, choose any odd divisor \(d\ge3\) of \(m\), write \(m=qd\), and set \(\sigma_{r+qs}=(-1)^s\) for \(0\le r<q\), \(0\le s<d\). Then
\[
Q(\zeta)=\left(\sum_{r=0}^{q-1}\zeta^r\right)
\left(\sum_{s=0}^{d-1}(-\zeta^q)^s\right)=0,
\]
because \((-\zeta^q)^d=1\) for odd \(d\) and \(-\zeta^q\ne1\) for \(d\ge3\). This gives all the claimed explicit constructive sign patterns. The classification itself allows any sign pattern annihilated by \(\Phi_n\), not only this block construction.

**3. Exact small-polygon feasibility.** Fix one successful sign pattern and take \(c_0=0\), then accumulate the successive \(d_j\). These shifts are bounded in absolute value by \((m-1)t\), hence \(p_j\to v_j\) uniformly as \(t\downarrow0\). The original regular polygon is strictly convex: all its successive signed turning determinants are strictly positive. By continuity, the new polygon remains strictly convex for sufficiently small \(t>0\). Every nonopposite vertex pair of the original regular polygon has distance at most \(\cos(\pi/n)<1\). The corresponding perturbed distance is at most \(\cos(\pi/n)+2(m-1)t\), strictly less than one for sufficiently small \(t\). Opposite pairs remain at distance exactly one by construction. The polygon therefore has Euclidean diameter one. In a convex polygon its diameter is attained at vertices, so the vertex-pair check suffices. All its edge lengths are the exact common value found in step 1; the perimeter and its Taylor expansion follow immediately.

This completes the unrestricted algebraic classification in the paired-translation class and the local geometric existence and rigidity assertions.

## Verification

A standalone script `checker.py` reconstructs the constructive sign polynomials, verifies symbolic divisibility by the relevant cyclotomic polynomial for 24 non-dyadic sample orders, and tests cyclic closure, exact edge-length predictions, strict convexity, pairwise diameter bounds, and strict perimeter gain in floating-point geometry. It additionally checks the dyadic minimal-polynomial identity for five powers of two. The symbolic algebra and numerical tests check particular orders only; the preceding proof supplies the uniform statements for every even \(n\ge4\).

Run with Python 3 and SymPy: `python checker.py`.

## Relationship to prior work

Hoffmann and Coppola [1] develop a first-order geometry for arbitrary equilateral small polygons and prove sufficient conditions for strict local maximality of particular nonregular constructions. The present result instead gives an exact nonlinear classification for the natural restricted class in which every original antipodal **diameter vector**, not merely its first derivative or length, remains fixed, and locates a power-of-two obstruction. Their local-optimality criterion does not supply this classification.

Reinhardt's classical theorem, as presented by Bingane and Audet [2], already shows that if \(n\) has an odd divisor, there are globally perimeter-optimal nonregular equilateral small polygons. That does not establish that one can ascend arbitrarily close to the regular polygon while fixing *all* original antipodal diameter vectors. We do not claim the global odd-factor dichotomy as new. Hare and Mossinghoff [3] use alternating-sign cyclotomic divisibility to encode globally extremal Reinhardt polygons, with a different polynomial and geometric realization. The vanishing signed half-period polynomial and the accompanying exact local paired-translation geometry here are distinct; the general cyclotomic concept is established background.

## Limitations

The dyadic rigidity statement applies only to the paired-translation class and cannot exclude improvements by configurations that change original diameter directions. In particular, it does not assert that regular dyadic polygons are local or global perimeter maxima. The construction is guaranteed to be diameter-one and strictly convex only for sufficiently small positive \(t\); outside that neighborhood additional vertex pairs may become diametral, and no unrestricted feasibility statement is made. Historical-priority verification cannot rule out unindexed geometric constructions or an equivalent treatment of paired-translation flexes.

## References

[1] J. Ayala Hoffmann and T. Ayala Coppola, *First Order Geometry of Equilateral Small Polygons*, arXiv:2611.23066v1, first public 17 November 2026. https://arxiv.org/html/2611.23066v1

[2] C. Bingane and C. Audet, *Tight Bounds on the Maximal Perimeter of Convex Equilateral Small Polygons*, arXiv:2105.10618, 2021. https://optimization-online.org/wp-content/uploads/2021/05/8408-1.pdf

[3] K. G. Hare and M. J. Mossinghoff, *Sporadic Reinhardt Polygons*, arXiv:1203.4107, 2012. https://arxiv.org/pdf/1203.4107
