# Two chord moments identify every regular Reuleaux odd-gon

## Finding

Fix an odd integer \(n\ge 3\) and a width \(w>0\). Let \(K_n(w)\) be the regular Reuleaux \(n\)-gon of width \(w\), and let \(X,Y\) be independent points chosen uniformly by **Euclidean boundary arclength**. Define \(D=\|X-Y\|_2\), \(M_2=\mathbb E D^2\), and \(M_4=\mathbb E D^4\). With
\[
t=\frac{\pi}{2n},\qquad q=\sec^2 t,\qquad z=\frac{\tan t}{t},\qquad m=1+\frac q4-z,
\]
the exact even chord moments are
\[
\boxed{M_2=2w^2m,\qquad
M_4=w^4\left[2\left(1+q+\frac{q^2}{16}-\frac{3+q}{2}z\right)+4m^2\right].}
\]
In particular, the scale-free statistic
\[
\boxed{H_n=\frac{M_4}{M_2^2}-\frac32=\frac{q+z-2z^2}{4m^2}}
\]
is **strictly positive** and **strictly decreasing** as the odd integer \(n\) increases. Consequently the two moments determine \(n\) uniquely within the entire class of regular Reuleaux odd-gons, regardless of unknown width; after identifying \(n\), their width is uniquely recovered by \(w=\sqrt{M_2/(2m)}\). The limiting circle has \(H_\infty=0\), different from every finite odd-gon.

The sharp near-circle moment separation has the two-term expansion
\[
\boxed{H_n=\frac{\pi^4}{90n^4}+\frac{4\pi^6}{945n^6}+O(n^{-8})\qquad(n\to\infty\text{ through odd integers}).}
\]
The order \(n^{-4}\) expresses a quartic loss of conditioning for distinguishing many-sided nearly circular Reuleaux bodies from a circle using these low moments.

## Assumptions and scope

A regular Reuleaux odd-gon is constructed from a regular Euclidean \(n\)-gon of circumradius \(R=w/(2\cos t)\), replacing each straight side by the minor radius-\(w\) circular arc centered at its opposite vertex. There are \(n\) congruent arcs, each of angular span \(2t=\pi/n\); thus its perimeter is \(\pi w\). Sampling is with normalized Euclidean arclength on this piecewise-circular boundary, **not** uniform interior area, uniform normal direction, or random invariant lines. The result holds for every real \(w>0\) and every odd integer \(n\ge3\), with no finite-n cutoff.

## Proof

**1. Single-point radial moments.** Similarity reduces the computation to \(w=1\). Write \(v_j=R(\cos(2\pi j/n),\sin(2\pi j/n))\) for the construction vertices. The arc centered at \(v_j\) has the parametrization
\[
x_j(\phi)=v_j-(\cos(2\pi j/n+\phi),\sin(2\pi j/n+\phi)),\quad -t\le\phi\le t.
\]
Each arc has equal Euclidean length \(2t\), so a uniformly sampled boundary point is obtained by choosing \(j\) uniformly and \(\phi\) uniformly on \([-t,t]\). Its squared distance to the rotational center is
\[
\|x_j(\phi)\|^2=1+R^2-2R\cos\phi,\qquad R=\frac{\sec t}{2}.
\]
Using \(\mathbb E\cos\phi=\sin t/t\) and \(\mathbb E\cos^2\phi=1/2+\sin(2t)/(4t)\) yields
\[
m_2:=\mathbb E\|X\|^2=1+\frac q4-z=m,
\]
\[
m_4:=\mathbb E\|X\|^4=1+q+\frac{q^2}{16}-\frac{3+q}{2}z,
\]
and therefore
\[
\operatorname{Var}(\|X\|^2)=m_4-m_2^2=\frac{q+z-2z^2}{2}.
\]

**2. Independent-pair identities.** Rotational symmetry of order \(n\ge3\) gives \(\mathbb EX=0\) and \(\mathbb E(XX^\mathsf T)=\frac12m_2I_2\). By expanding \(\|X-Y\|^2\) and \(\|X-Y\|^4\) and using independence,
\[
\mathbb E\|X-Y\|^2=2m_2,\qquad
\mathbb E\|X-Y\|^4=2m_4+4m_2^2.
\]
The cross terms containing \(\mathbb EY\) vanish, and \(\mathbb E(X\cdot Y)^2=\operatorname{tr}((m_2I_2/2)^2)=m_2^2/2\). Scaling by \(w\) proves both displayed chord formulas. In particular,
\[
H_n=\frac{m_4-m_2^2}{2m_2^2}>0,
\]
because the radial distance varies nontrivially over each arc.

**3. Strict ordering in the number of arcs.** Treat \(t\) as a continuous variable on \((0,\pi/6]\) and denote \(m_2(t)=1+\sec^2(t)/4-\tan(t)/t\). A direct derivative calculation shows that \(m_2'(t)<0\) is equivalent to
\[
2t\cot t>2\cos^2t+t^2.
\]
Here is a uniform elementary bound rather than a numerical derivative argument. On this interval the alternating Taylor bounds for sine and cosine give
\[
\frac{t}{\sin t}\ge1+\frac{t^2}{6},\qquad
\cos t\ge1-\frac{t^2}{2},\qquad
\cos^2t\le1-t^2+\frac{t^4}{3}.
\]
For the first inequality, combine \(\sin t/t\le1-t^2/6+t^4/120\) with \((1+t^2/6)^{-1}=1-t^2/6+t^4/[36(1+t^2/6)]\), whose final coefficient is at least \(1/120\) on this interval. Thus
\[
2t\cot t-(2\cos^2t+t^2)
\ge\frac{t^2}{3}-\frac{5t^4}{6}>0,
\]
since \(t^2\le\pi^2/36<2/5\). Therefore \(m_2(t)\) is strictly decreasing.

On the other hand, with \(U\) uniform on \([-1,1]\), the radial variance is
\[
V(t):=\operatorname{Var}(\|X\|^2)=\sec^2t\,\operatorname{Var}(\cos(tU)).
\]
For independent \(U,U'\), the variance on the right is half the expected squared difference \((\cos(tU)-\cos(tU'))^2\). Whenever \(|U|\ne|U'|\), that absolute difference strictly increases with \(t\in(0,\pi/6]\): its derivative is the positive difference of \(u\sin(tu)\) at the larger and smaller absolute values, and \(u\mapsto u\sin(tu)\) is strictly increasing on \([0,1]\). Hence \(V(t)\) strictly increases, as does \(H(t)=V(t)/(2m_2(t)^2)\). Because \(t=\pi/(2n)\) decreases with \(n\), \(H_n\) strictly decreases. The formula for recovering \(w\) follows from \(M_2\).

**4. Precise near-circle expansion.** Standard convergent Taylor expansions at the origin give
\[
m_2(t)=\frac14-\frac{t^2}{12}+\frac{t^4}{30}+O(t^6),
\]
\[
V(t)=\frac{t^4}{45}+\frac{2t^6}{105}+O(t^8),
\]
and consequently
\[
H(t)=\frac{8t^4}{45}+\frac{256t^6}{945}+O(t^8).
\]
Substituting \(t=\pi/(2n)\) produces the stated two coefficients. This is a proved analytic expansion, not an empirical extrapolation.

## Verification

Running `python3 verify.py` uses only the standard Python library and constructs the actual circular boundary arcs. It compares all ordered-point squared and fourth distances under independent midpoint quadrature against the closed formulas for six odd side counts; it checks positivity and discrete strict ordering for 100 consecutive odd orders and the leading asymptotic coefficient at three orders. The verifier reports 121 passed assertions. These finite checks are supplementary: all positive integers and strict inequalities are established by the analytic argument above.

## Relationship to prior work

Basit and Lángi, *Dowker-type theorems for disk-polygons in normed planes* (arXiv:2307.04026, first public version July 8, 2023), place circular-arc disk-polygons in the context of geometric approximation and provide area/perimeter extremal theorems, but their main statements do not concern independent arclength boundary-distance moments. Earlier Reuleaux-polygon results such as Firey's and Sallee's concern area and isoperimetric behavior. A published boundary-chord tail result for regular Reuleaux odd-gons determines the number of arcs from the leading near-diameter probability tail, not from two low even moments; a separate published polar-moment calculation uses uniform **interior area**, not boundary arclength. Neither implication recovers the present two-moment formula or its monotonicity without an additional argument. The present result is therefore a distinct low-moment inverse observation within this natural one-parameter shape family, with residual priority uncertainty in unindexed classical metric-geometry literature.

## Limitations

The theorem assumes in advance that the body is either a regular Reuleaux odd-gon or, when discussing the limit, a circle. It does **not** characterize arbitrary constant-width curves from two moments, nor distinguish regular Reuleaux odd-gons from unrelated shapes outside this family. The inverse is exact but increasingly ill-conditioned: the scale-free gap vanishes to fourth order in reciprocal side count. The proof uses ideal exact moments; finite-sample statistical accuracy is not analyzed. No independent mathematical audit has been performed.

## References

- B. Basit and Z. Lángi, *Dowker-type theorems for disk-polygons in normed planes*, arXiv:2307.04026, first version 2023-07-08, https://arxiv.org/abs/2307.04026.
- G. T. Sallee, *Maximal Areas of Reuleaux Polygons*, Canadian Mathematical Bulletin **13** (1970), 175–179, DOI:10.4153/CMB-1970-037-1; with reference to W. J. Firey, *Isoperimetric ratios of Reuleaux polygons*, Pacific Journal of Mathematics **10** (1960), 823–830.
- *Two-term diameter tails and logarithmic endpoint marks for regular Reuleaux odd-gons*, publicly available finding dated 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-two-term-diameter-tails-and-logarithmic-endpoint-marks-for-regul--c7dc1d087471.
- *Polar moment and isotropic constant of regular Reuleaux odd-gons*, publicly available finding dated 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-polar-moment-and-isotropic-constant-of-regular-reuleaux-odd-gons--43279757dfc9.
