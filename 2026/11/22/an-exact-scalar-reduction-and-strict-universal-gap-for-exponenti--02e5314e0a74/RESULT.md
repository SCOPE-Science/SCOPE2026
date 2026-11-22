# An exact scalar reduction and strict universal gap for exponential-cone projection stability

## Finding
Let \(K\subset\mathbb R^3\) be the closed exponential cone
\[
K=\operatorname{cl}\{(x,y,z):y>0,\ z\ge y\exp(x/y)\},
\]
with Euclidean nearest-point projector \(P_K\). All coordinates of both arguments and values are measured in \(\|\cdot\|_\infty\). For every real \(r\), set
\[
p(r)=(r,1,e^r),\qquad v(r)=(e^r,(1-r)e^r,-1),
\]
\[
R(r)=\max_{1\le i\le3}\frac{|p_i(r)|\sum_{j=1}^3|p_j(r)|}{\sum_{j=1}^3p_j(r)^2},
\qquad
H(r)=\max_{1\le i\le3}\left[1+\frac{|v_i(r)|(\sum_{j\ne i}|v_j(r)|-|v_i(r)|)}{\sum_{j=1}^3v_j(r)^2}\right].
\]
Then the **exact global coordinatewise Lipschitz constant** is the following explicit *one-real-variable* extremum:
\[
\boxed{\operatorname{Lip}_{\infty\to\infty}(P_K)
=\max\left\{1,\ \max_{r\in\mathbb R}R(r),\ \max_{r\in\mathbb R}H(r)\right\}.}
\]
The maxima exist. Moreover, writing \(r_0=201/200\),
\[
\boxed{
\frac{e^{r_0}(e^{r_0}+1+r_0)}{e^{2r_0}+1+r_0^2}
\le \operatorname{Lip}_{\infty\to\infty}(P_K)
<\frac{1+\sqrt3}{2}.}
\]
The left-hand expression is about \(1.3660217223\), whereas the right-hand universal positive-contraction ceiling is about \(1.3660254038\). In particular, Euclidean nonexpansivity does not imply coordinatewise nonexpansivity, and this nonpolyhedral cone comes exceptionally close to, but strictly misses, the universal three-coordinate ceiling.

## Assumptions and scope
The projection is the unique Euclidean metric projector onto the *whole closed cone*, including its singular flat face. The Lipschitz constant is the supremum over **all distinct input pairs** in \(\mathbb R^3\), not the modulus of a selected branch. All statements are for ordinary real coordinates and the unweighted maximum norm; the scalar formula is exact but no closed form for its maximizing \(r\) or proof of which of \(R,H\) globally dominates is asserted.

## Proof
**1. Smooth normal geometry.** The positively scaled smooth boundary is \(t p(r)\), where \(t>0\) and \(r\in\mathbb R\). Its outward normal is \(v(r)\), and \(p(r)\cdot v(r)=0\). For every \(t>0\) and \(\lambda>0\), the point
\[
a(t,r,\lambda)=t p(r)+\lambda v(r)
\]
projects exactly to \(t p(r)\), by the normal-cone characterization of Euclidean projection onto a closed convex set. Moreover the normal is unique on this smooth boundary.

**2. Full Jacobian.** Write \(p'=\frac{d}{dr}p\), \(v'=\frac{d}{dr}v\), and let
\[
q=p'-\frac{p'\cdot p}{p\cdot p}p.
\]
Since \(v'\cdot p=0\) and \(v'\cdot q=v'\cdot p'=e^r>0\), the differential of input \(a\) in the orthogonal directions spanned by \(p,q,v\) is diagonal after removing the radial contribution to \(p'\). Differentiating the input and projection parametrizations gives
\[
DP_K(a)=P_{\mathrm{rad}}(r)+\rho(t,r,\lambda)
\big(P_{\mathrm{tan}}(r)-P_{\mathrm{rad}}(r)\big),
\]
where
\[
P_{\mathrm{rad}}(r)=\frac{p(r)p(r)^{\mathsf T}}{\|p(r)\|_2^2},\qquad
P_{\mathrm{tan}}(r)=I-\frac{v(r)v(r)^{\mathsf T}}{\|v(r)\|_2^2},
\]
\[
\rho(t,r,\lambda)=\left(1+\frac{\lambda e^r}{t\|q(r)\|_2^2}\right)^{-1}\in(0,1).
\]
Here \(P_{\mathrm{rad}}\) is the rank-one projection onto the cone generator and \(P_{\mathrm{tan}}\) is the projection onto the boundary tangent plane. The identity may also be verified directly by multiplying the derivative matrices \([p,\ tp'+\lambda v',\ v]\) for the input and \([p,\ tp',\ 0]\) for the output.

**3. All possible projection branches.** On the interior of \(K\), the projector is the identity; on the interior of its polar, it is zero. On the flat-face branch with source \(x\le0,y\le0\), the projector is \((x,0,\max\{z,0\})\), whose local maximum-norm Lipschitz coefficient is at most one. The remaining open branch has a smooth boundary projection and is covered by step 2. These cases also follow from the exact projection classification of Friberg (2021, Sections 3–4). Boundaries of these branches cannot increase the global constant: the projector is globally Euclidean-Lipschitz and hence locally absolutely continuous; an almost-everywhere Jacobian bound extends to the whole map by standard mollification (or integrating along almost every line).

**4. Exact maximization reduction.** The induced maximum norm is convex as a function of the matrix. Step 2 therefore gives
\[
\|DP_K(a)\|_{\infty\to\infty}\le
\max\{\|P_{\mathrm{rad}}(r)\|_{\infty\to\infty},
\|P_{\mathrm{tan}}(r)\|_{\infty\to\infty}\}.
\]
The first matrix has maximum absolute row sum exactly \(R(r)\), and the second exactly \(H(r)\). This proves the global upper bound, together with the other branches. Conversely, keeping \(t,r\) fixed and sending \(\lambda\to\infty\) makes \(\rho\to0\), so local Jacobian norms approach \(R(r)\); sending \(\lambda\downarrow0\) makes them approach \(H(r)\). These local Jacobians provide genuine arbitrarily close distinct input pairs. An interior point supplies coefficient one. Thus the upper bound is sharp.

**5. Strict universal ceiling.** For any Euclidean unit vector \(w\in\mathbb R^3\), Cauchy–Schwarz bounds the absolute row sums of each of the rank-one projections \(ww^{\mathsf T}\) and its complement \(I-ww^{\mathsf T}\) by \((1+\sqrt3)/2\). Equality for the rank-one projection requires the two *other* absolute coordinates to agree and the distinguished absolute coordinate to be \(1+\sqrt3\) times each other coordinate. Equality for the complement requires the same equality of the other coordinates but distinguished-to-other ratio \(\sqrt3-1\).

For \(p(r)=(r,1,e^r)\), equality in the first condition is impossible: distinguished coordinate \(r\) would require \(r=0\) and hence vanish; distinguished coordinate \(1\) would require \(-r=e^r=1/(1+\sqrt3)\), contradicted by \(e^{-c}>c\) for \(c=1/(1+\sqrt3)<1/2\); distinguished coordinate \(e^r\) requires \(r=\pm1\) and neither \(e\) nor \(e^{-1}\) equals \(1+\sqrt3\). For \(v(r)=(e^r,(1-r)e^r,-1)\), equality in the complement condition is likewise impossible: if the first coordinate is distinguished, equality of the other two forces either \(r=0\) or \(r>1\), giving a distinguished ratio at least one rather than \(\sqrt3-1\); if the second is distinguished, equality of the others forces \(r=0\), giving ratio one; if the third is distinguished, equality of the others forces \(r=0\) or \(r=2\), giving ratio one or \(e^{-2}\), neither equal to \(\sqrt3-1\).

Finally, both \(R(r)\) and \(H(r)\) tend to one as \(r\to\pm\infty\), hence achieve maxima at finite \(r\) and, by the preceding strict equality obstruction, both maxima fall strictly below the ceiling. The explicit lower bound is the third row sum of \(P_{\mathrm{rad}}(r_0)\) from step 4, and it is greater than one. This proves both boxed statements.

## Verification
The included `check.py` independently differentiates the smooth KKT parametrization using a direct \(3\times3\) matrix inverse and compares it against the convex-combination Jacobian formula on 350 deterministic sample points. It also checks the two scalar row-norm formulas and the explicit numerical lower bound, and performs a separate exploratory scalar grid. Run using `python3 check.py` with only the Python standard library. These numerical checks are **supplementary**; the real-line maximum and strict ceiling are proved analytically above, not by a finite grid.

## Relationship to prior work
Friberg (January 12, 2021) provides a complete scalar-root characterization and closed-form branches of exponential-cone projection. Friedlander–Goodwin–Hoheisel (February 12, 2021) develop general epigraphical projection sensitivity and proximal parametrization. Agrawal–Barratt–Boyd–Busseti–Moursi (initial arXiv April 2019, revised May 2020) differentiate solutions of cone programs via projection derivatives. None of the inspected material states the above sharp maximum-norm scalar extremum or the strict, near-saturated three-dimensional ceiling for exponential-cone projection. The proof deliberately builds on their projection framework rather than claiming the underlying projector or differentiability formulas as new. Related results for Lorentz cones and planar cones concern other geometries and do not imply this exponential-cone exact coefficient.

## Limitations
No closed form for the maximizing scalar argument, proof of which scalar branch dominates, or independently audited novelty certificate is supplied. Values around \(1.3660217\) from scalar numerical optimization are exploratory; the certified theorem is the exact extremal formula and the explicit analytic bounds. Literature searches can miss older results under equivalent descriptions. The statement does not address weighted coordinates, non-Euclidean metric projectors, or algorithmic floating-point errors.

## References
- H. A. Friberg, *Projection onto the exponential cone: a univariate root-finding problem*, Optimization Online, first public January 12, 2021. https://optimization-online.org/2021/01/8204/ ; full preprint https://optimization-online.org/wp-content/uploads/2021/01/8204.pdf
- M. P. Friedlander, A. Goodwin, T. Hoheisel, *From perspective maps to epigraphical projections*, arXiv:2102.06809, first public February 12, 2021. https://arxiv.org/pdf/2102.06809
- A. Agrawal, S. Barratt, S. Boyd, E. Busseti, W. M. Moursi, *Differentiating Through a Cone Program*, arXiv:1904.09043 (2019; revised 2020). https://arxiv.org/pdf/1904.09043
