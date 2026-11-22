# Sharp axis–diagonal minimax transition in heat versus product-Poisson smoothing on tori

## Finding

Fix an integer \(d\ge2\). Let \(H_t\) be the heat semigroup and \(Q_s\) the *tensor product of one-dimensional Poisson semigroups* on the flat \(d\)-torus. The optimal small-time \(L^2\)-operator-norm error has a strictly positive, dimension-dependent limit:
\[
\inf_{s>0}\|H_t-Q_s\|_{L^2\to L^2}=E_d+O_d(t),\qquad t\downarrow0.
\]
All minimizing times satisfy \(s=c_d\sqrt t+O_d(t^{3/2})\). The constants \(c_d,E_d\) are specified by one unique crossing of two explicit one-dimensional extrema, and the limiting worst Fourier directions switch sharply between coordinate axes and fully balanced diagonals. As \(d\to\infty\), the optimal error \(E_d\) increases strictly to \(1\).

## Assumptions and scope

The torus is \(\mathbb T^d=(\mathbb R/2\pi\mathbb Z)^d\) with normalized Haar measure. With \(k=(k_1,\ldots,k_d)\in\mathbb Z^d\), \(H_t\) and \(Q_s\) have Fourier multipliers
\[
\widehat{H_tf}(k)=e^{-t\|k\|_2^2}\widehat f(k),\qquad
\widehat{Q_sf}(k)=e^{-s\|k\|_1}\widehat f(k).
\]
The optimization is over all \(s>0\), with \(t>0\), while dimension \(d\ge2\) is fixed before the limit. This \(Q_s\) is not the *isotropic subordinated* Poisson semigroup \(e^{-s\sqrt{-\Delta}}\): the product generator has multiplier \(\|k\|_1\), not \(\|k\|_2\). In particular, the distinction is essential for dimensional dependence.

For \(a>0\) let \(u_-(a)\in(0,a)\) and \(u_+(a)\in(a,\infty)\) be the respective unique roots of
\[
\log(2u/a)+au-u^2=0.
\]
Define
\[
U(a)=e^{-u_-(a)^2}-e^{-a u_-(a)},\qquad
V(a)=e^{-a u_+(a)}-e^{-u_+(a)^2}.
\]
Then \(c_d\) is the **unique** solution of \(U(c\sqrt d)=V(c)\), and \(E_d\) denotes their common value. Both constants are finite, positive, and depend only on \(d\).

## Proof

**1. Exact continuum reduction.** By Plancherel, setting \(s=c\sqrt t\), the operator norm is
\[
E_{d,t}(c):=\sup_{k\in\mathbb Z^d}\left|e^{-t\|k\|_2^2}-e^{-c\sqrt t\|k\|_1}\right|.
\]
On the entire continuum define
\[
F_d(c)=\sup_{x\in\mathbb R^d}\left|e^{-\|x\|_2^2}-e^{-c\|x\|_1}\right|.
\]
For fixed \(u=\|x\|_2>0\), the exact sharp range is \(u\le\|x\|_1\le\sqrt d\,u\). In the positive-error direction the term \(e^{-c\|x\|_1}\) should be minimized, so the maximum is attained at balanced vectors \(x=(\pm u/\sqrt d,\ldots,\pm u/\sqrt d)\). In the negative-error direction it should be maximized, so the maximum is attained at coordinate axes \(x=\pm ue_j\). Both equalities follow from the equality cases of Cauchy–Schwarz and of \(\|x\|_1\ge\|x\|_2\). Therefore the exact whole-space norm is
\[
F_d(c)=\max\{U(c\sqrt d),V(c)\}.
\]
These are the only families of nonzero global maximizers, apart from a possible tie between families. The zero vector has zero error, so is never maximizing.

**2. Exact scalar maximizers.** For \(a>0\), \(e^{-u^2}-e^{-au}>0\) exactly for \(0<u<a\), whereas its negative is positive exactly for \(u>a\). Both functions vanish at the finite endpoint, and approach zero at their other endpoint (including infinity for the negative wing). Their interior critical points solve the displayed logarithmic equation. The function \(h_a(u)=\log(2u/a)+au-u^2\) satisfies \(h_a''(u)=-u^{-2}-2<0\), \(h_a(0+)=-\infty\), \(h_a(a)=\log2>0\), and \(h_a(\infty)=-\infty\). Strict concavity and its monotone-derivative structure yield exactly two positive roots: one in \((0,a)\), the other in \((a,\infty)\); hence \(u_-,u_+\) are unique global maxima in the respective wings. The implicit-function theorem makes them smooth in \(a>0\). From the strict pointwise dependence on \(a\) and attained maxima, \(U\) is strictly increasing from \(0\) to \(1\), and \(V\) strictly decreasing from \(1\) to \(0\). In particular their crossing is unique and transverse. Differentiating at the critical point gives the strictly positive derivative of \(U\) and strictly negative derivative of \(V\):
\[
U'(a)=u_-(a)e^{-a u_-(a)}>0,\qquad
V'(a)=-u_+(a)e^{-a u_+(a)}<0.
\]
Thus \(F_d\) has a sharp V-shaped unique minimizer at \(c_d\), with \(F_d(c)-E_d\ge b_d|c-c_d|\) for \(c\) in some neighborhood of \(c_d\), where \(b_d>0\).

**3. Lattice approximation at quadratic accuracy.** Always \(E_{d,t}(c)\le F_d(c)\), since \(\sqrt t\,\mathbb Z^d\subset\mathbb R^d\). Fix a compact interval \(I\subset(0,\infty)\) of calibrations. The critical radii \(u_-(c\sqrt d)\) and \(u_+(c)\) vary smoothly and remain in a compact subset of \((0,\infty)\) as \(c\in I\). Round the axial continuum maximizer's one nonzero coordinate, and each equal-magnitude coordinate of the diagonal maximizer, to the nearest point of \(\sqrt t\,\mathbb Z\). The two one-dimensional radial objective functions have zero first derivative at their respective maxima; uniform boundedness of the second derivatives on this compact set and Taylor's theorem imply
\[
0\le F_d(c)-E_{d,t}(c)\le C_{d,I}t\quad\text{for every }c\in I\text{ and all sufficiently small }t.
\]
The choice of frequency signs is immaterial; only the actual integer lattice was used in the lower bound.

**4. Minimization over every positive time, not only calibrated candidates.** For fixed \(t>0\), \(E_{d,t}(c)\) is continuous in \(c>0\) (the multiplier tails are uniformly small on any compact \(c\)-interval). As \(c\downarrow0\), its supremum tends to \(1\), by taking arbitrarily high frequency. As \(c\to\infty\), it tends to \(e^{-t}\), since the nonzero Fourier frequencies have \(\|k\|_1\ge1\) and the least nonzero heat exponent is \(t\). Choose fixed \(a<c_d<b\) such that both continuum branch barriers, \(V(a)\) and \(U(b\sqrt d)\), are strictly larger than \(E_d\). For sufficiently small \(t\), the lattice estimates at \(a,b\) also exceed \(E_d\). The negative-wing expression at its fixed axial lattice witness is decreasing in \(c\) as long as it is negative, so the norm remains above that barrier for all \(c\le a\); analogously the positive-wing lattice witness at \(b\) gives the same barrier for all \(c\ge b\), since its signed error grows with \(c\). Hence all global minimizers lie inside \([a,b]\), where continuity ensures existence. Apply the uniform lattice bound of Step 3 and \(F_d(c)\ge E_d\) to conclude
\[
E_d-C_dt\le\inf_{c>0}E_{d,t}(c)\le E_{d,t}(c_d)\le E_d.
\]
For any minimizing \(c_t\), the same bound gives \(F_d(c_t)\le E_d+C_dt\). The unique cusp and compactness imply \(|c_t-c_d|=O_d(t)\), so \(s_t=\sqrt t\,c_t=c_d\sqrt t+O_d(t^{3/2})\) for every minimizer.

**5. Axis–diagonal transition and dimension.** Since \(U(c\sqrt d)\) increases and \(V(c)\) decreases, the maximizing set of \(F_d(c)\) consists precisely of the axial negative-error points \(\pm u_+(c)e_j\) when \(c<c_d\), and precisely of the balanced positive-error points \(x=(\pm u_-(c\sqrt d)/\sqrt d,\ldots,\pm u_-(c\sqrt d)/\sqrt d)\) when \(c>c_d\). At equality both families and no others maximize. Increasing \(d\) strictly raises the first wing for every \(c>0\), hence strictly lowers the crossing \(c_d\) and strictly raises \(E_d\). The decreasing sequence \(c_d\) must tend to zero, since otherwise \(U(c_d\sqrt d)\to1\) while \(V(c_d)\) stays bounded below one. Consequently \(E_d=V(c_d)\to1\). This proves the claims.

## Verification

The included standalone `check.py` uses only the Python standard library. It computes the unique scalar critical points by bisection, checks critical-equation residuals and matching wings, verifies the strictly ordered constants for six dimensions, and compares the continuum formula against nine finite Fourier lattice calculations in dimensions two and three. It passed all assertions. The script's finite grids are diagnostics, not proofs of the continuum supremum, lattice approximation, uniqueness, or uniform all-frequency statement. The latter are established in Steps 1–5 above.

Illustrative numerical values (not definitions) are \(c_2\approx0.78155787578\), \(E_2\approx0.20968189592\), \(c_3\approx0.71242187012\), and \(E_3\approx0.24296641228\).

## Relationship to prior work

Quanhua Xu, *Holomorphic functional calculus and vector-valued Littlewood–Paley–Stein theory for semigroups* (arXiv:2105.12175v1; first public 25 May 2021), studies heat and **isotropically subordinated** Poisson semigroups through square-function and martingale type/cotype estimates, not the sharp operator-norm minimax distance for the tensor-product generator. Duong–Hu–Li (2019) treat tensor-product semigroups in weighted product Hardy-space square/area function equivalences; their definitions and main theorems do not supply a sharp heat/product-Poisson difference norm or an axis-versus-diagonal optimization. Those sources motivate the comparison of distinct smoothing geometries rather than imply this theorem. A literature and indexed-result comparison found no equivalent sharp multi-dimensional result. This is a best-knowledge priority assessment, not proof of historical uniqueness.

## Limitations

The \(O_d(t)\) error and the optimizer \(O_d(t^{3/2})\) displacement are for each fixed dimension, not uniform as \(d\to\infty\). The theorem concerns \(L^2\)-operator norm, not \(L^p\) norms with \(p\ne2\), nor spatial-density discrepancies, nor the isotropic Poisson semigroup. No exact finite-time formula for the optimal parameter is claimed. The constants are specified implicitly, with reproducible numerical approximations. A formal independent mathematical audit and exhaustive historical-priority verification have not been performed.

## References

1. Q. Xu, *Holomorphic functional calculus and vector-valued Littlewood–Paley–Stein theory for semigroups*, arXiv:2105.12175v1 (2021), https://arxiv.org/abs/2105.12175; journal DOI: https://doi.org/10.4171/JEMS/1430.
2. X. T. Duong, G. Hu, J. Li, *Equivalence of Littlewood–Paley square function and area function characterizations of weighted product Hardy spaces associated to operators*, J. Math. Soc. Japan 71 (2019), 91–115; https://doi.org/10.2969/jmsj/78287828.
