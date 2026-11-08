# Three-phase shadow minima and a uniquely least-anisotropic triangular bipyramid

## Finding

For each \(h>0\), let \(T_h\subset\mathbb R^3\) be the convex hull of the three points \((\cos(2\pi j/3),\sin(2\pi j/3),0)\), for \(j=0,1,2\), and the two apices \((0,0,\pm h)\). For a unit viewing direction \(u\), let \(B_h(u)\) denote the Euclidean area of the orthogonal projection of \(T_h\) onto \(u^\perp\). Put \(b_-(h)=\min_{\|u\|=1}B_h(u)\) and \(b_+(h)=\max_{\|u\|=1}B_h(u)\). Then

\[
b_-(h)=\begin{cases}
3h/2,&0<h\le1/\sqrt3,\\
\sqrt3 h/\sqrt{1+h^2},&1/\sqrt3\le h\le\sqrt{11/21},\\
9h/(4\sqrt{1+3h^2}),&h\ge\sqrt{11/21},
\end{cases}
\qquad
b_+(h)=\begin{cases}
3\sqrt3/4,&0<h\le3/4,\\
\sqrt3h,&h\ge3/4.
\end{cases}
\]

Consequently the scale-invariant angular-brightness anisotropy satisfies the *sharp* inequality

\[
\frac{b_+(h)}{b_-(h)}\ge\frac{\sqrt{129}}9,
\]

with equality **if and only if** \(h=3/4\). This optimizes over the entire family of centrally aligned equilateral-base triangular bipyramids, with base circumradius normalized to one. The minimum brightness has three distinct active-direction regimes and two exact switching heights.

## Assumptions and scope

Euclidean \(\mathbb R^3\) with its usual scalar product is fixed. The parameter \(h\) is any strictly positive real number. The base lies in \(z=0\), is equilateral, has circumradius one, and its centroid lies on the line of the two apices at signed heights \(\pm h\). The projected planar area is the standard two-dimensional Lebesgue area; \(u\) and \(-u\) define the same projection. All extrema are taken over the full unit sphere, including nongeneric viewing directions. Scale-invariance means that simultaneously scaling all dimensions changes neither \(b_+/b_-\) nor the optimal *height/circumradius ratio*.

Write \(e_j=(\cos(2\pi j/3),\sin(2\pi j/3))\) for \(j=0,1,2\), and \(u=(w,z)\in\mathbb R^2\times\mathbb R\), with \(\|w\|^2+z^2=1\). More explicitly, the complete brightness function is

\[
B_h(w,z)=\frac{\sqrt3}{2}\sum_{j=0}^2\max\bigl(h|e_j\cdot w|,|z|/2\bigr).
\]

The minimizing directions, up to sign and triangular symmetry, are: (I) \(z=0\), \(w\perp e_j\); (II) \(w\parallel e_j\), \(|z|=h\|w\|\); (III) \(w\perp e_j\), \(|z|=\sqrt3 h\|w\|\). Types I, II and III respectively attain the minimum in the three strict open regimes above; at either switch the adjacent types both attain it. The maximizing directions are exactly the vertical axis when \(h<3/4\), exactly the six horizontal directions \(w=\pm e_j\) when \(h>3/4\), and the union at equality.

## Proof

**1. Facets and brightness.** Every facet of \(T_h\) joins one of the three base edges to one apex. The side-edge length of the equilateral base is \(\sqrt3\), its inradius is \(1/2\), and every triangular facet has area \(A_f=(\sqrt3/2)\sqrt{h^2+1/4}\). For a base edge opposite \(e_j\), outward unit normals to the upper and lower facets are respectively \((-h e_j,\,1/2)/\sqrt{h^2+1/4}\) and \((-h e_j,\,-1/2)/\sqrt{h^2+1/4}\). Cauchy's polytope projection identity \(B_h(u)=\frac12\sum_f A_f|\langle u,n_f\rangle|\) therefore gives

\[
B_h(w,z)=\frac{\sqrt3}{4}\sum_{j=0}^{2}
\left(\left|h e_j\cdot w+\frac z2\right|+
\left|h e_j\cdot w-\frac z2\right|\right).
\]

Apply \(|a+b|+|a-b|=2\max(|a|,|b|)\) to obtain the announced brightness function. No genericity assumption was used.

**2. Maximum.** Define six vectors \(q_{j,\pm}=(h e_j,\pm1/2)\). Maximizing the finite sum of absolute scalar products can be interchanged with maximizing its signs:

\[
b_+(h)=\frac{\sqrt3}{4}\max_{\varepsilon_{j,\pm}\in\{-1,1\}}
\left\|\sum_{j,\pm}\varepsilon_{j,\pm}q_{j,\pm}\right\|.
\]

For a fixed \(j\), equal signs produce a horizontal vector \(\pm2h e_j\) and zero vertical contribution; opposite signs produce a vertical vector of magnitude one and zero horizontal contribution. If \(k\) of the three pairs have equal signs, the largest possible norm of the total sign sum is, in order \(k=0,1,2,3\),

\[
3,\qquad2\sqrt{1+h^2},\qquad\sqrt{1+12h^2},\qquad4h.
\]

Here \(\|e_i-e_j\|=\sqrt3\) for distinct base vectors and \(\max_{\delta_j\in\{-1,1\}}\|\sum_j\delta_j e_j\|=2\). For \(0<h\le3/4\), the two middle norms are both at most \(3\); for \(h\ge3/4\), both are at most \(4h\). Thus \(b_+(h)=(\sqrt3/4)\max(3,4h)\). At equality of the outer two candidates, the intermediate candidates remain strictly smaller, giving the stated maximizing-direction classification.

**3. A finite-ray principle for minima.** Let \(F(u)=\sum_{a=1}^N|\langle u,q_a\rangle|\) where the \(q_a\) span \(\mathbb R^3\). In each closed sign chamber \(C=\{u:\varepsilon_a\langle u,q_a\rangle\ge0\ \forall a\}\), the function \(F\) is linear and \(C\) is pointed. If \(u=\sum_l t_l r_l\), with \(t_l\ge0\) and unit extreme-ray directions \(r_l\) of \(C\), then

\[
F(u)=\sum_l t_lF(r_l)\ge\bigl(\min_lF(r_l)\bigr)\sum_l t_l\ge\bigl(\min_lF(r_l)\bigr)\|u\|.
\]

Every global minimizing unit direction must therefore be an extreme ray of some chamber. The second inequality is strict for any nontrivial combination of nonparallel rays, so it also proves there are no additional minimizing directions in chamber interiors. Each extreme ray in three dimensions is cut out by two linearly independent equations \(\langle u,q_a\rangle=0\).

**4. Exhaustive ray geometry.** Up to sign, rotation and reflection, there are precisely three ways to choose two different facet-normal planes: choose the two planes associated with the same \(j\) but opposite signs; choose planes associated with different indices but equal signs; choose planes associated with different indices and opposite signs. Their intersection directions are respectively

\[
\begin{array}{ll}
\text{I:}& z=0,\quad w\perp e_j,\\
\text{II:}& w\parallel e_j,\quad |z|=h\|w\|,\\
\text{III:}&w\perp e_j,\quad |z|=\sqrt3h\|w\|.
\end{array}
\]

Direct substitution into the brightness formula gives the three candidate minimum values

\[
c_1=3h/2,\qquad c_2=\sqrt3h/\sqrt{1+h^2},\qquad c_3=9h/(4\sqrt{1+3h^2}).
\]

All three candidate rays exist for every \(h>0\), and they are the exhaustive list. To determine their lower envelope, compare their squares:

\[
\begin{aligned}
c_1^2-c_2^2&=\frac{3h^2(3h^2-1)}{4(1+h^2)},\\
c_1^2-c_3^2&=\frac{9h^2(12h^2-5)}{16(1+3h^2)},\\
c_2^2-c_3^2&=\frac{3h^2(21h^2-11)}{16(1+h^2)(1+3h^2)}.
\end{aligned}
\]

All denominators are positive; checking these three exact signs gives the announced three-branch minimum, with switches \(1/\sqrt3\) and \(\sqrt{11/21}\). The strict triangle-inequality clause in the finite-ray principle yields exactly the stated minimizing directions.

**5. Optimal anisotropy.** Each of \(c_1,c_2,c_3\) is strictly increasing on \((0,\infty)\), hence their minimum \(b_-(h)\) is strictly increasing. On \(0<h\le3/4\), \(b_+(h)=3\sqrt3/4\) is constant, so \(b_+(h)/b_-(h)\) strictly decreases. Because \(3/4>\sqrt{11/21}\), on \(h\ge3/4\) the minimum is \(c_3\), yielding

\[
\frac{b_+(h)}{b_-(h)}=
\frac{4\sqrt3}{9}\sqrt{1+3h^2},
\]

which strictly increases. The unique minimizer is therefore \(h=3/4\). At this height \(b_+=3\sqrt3/4\) and \(b_-=27/(4\sqrt{43})\), producing the exact ratio \(\sqrt{129}/9\). This completes the proof.

## Verification

The standalone reproducibility file `verify_brightness.py` contains two independent finite reconstructions and deterministic sampling checks. It constructs two-dimensional orthogonal projections of the actual five vertices and computes their convex-hull areas directly, comparing them with the Cauchy-derived formula. Separately it enumerates all fifteen facet-normal-plane pairs and all sixty-four sign sums, checking the lower and upper envelopes at ten heights, including the two transitions and the unique optimizer. It also samples many deterministic pseudorandom directions across ten heights and tests the claimed global bounds. Execute `python3 verify_brightness.py` using only the Python standard library. The checker returns `BIPYRAMID_SHADOW_BOUNDS_CHECKS_PASSED` and `FULL_FACET_PAIR_AND_SIGN_VECTOR_CERTIFICATES_PASSED` on success. The proof above, not finite sampling, covers every real \(h>0\) and every viewing direction.

## Relationship to prior work

Cauchy's projection formula gives the brightness of any polytope from its facets; that identity and its polyhedral specialization are established background, not newly claimed. Black and Criado (arXiv:2406.06936, first posted June 11, 2024) analyze expected **vertex counts** of random planar polytope shadows and upper/lower bounds in terms of geometric parameters, rather than extrema of projected **areas** for the triangular bipyramid. Their accessible full-text publication was checked, including its main theorems and the absence of a triangular-bipyramid brightness classification. The triangular bipyramid itself is classical. The claim here is specifically the *exact three-phase lower brightness envelope*, *full upper envelope*, and *unique minimizer of their ratio* across its natural height family; no general projection formula alone states those optimized constants or equality cases.

## Limitations

Only symmetric right bipyramids over an equilateral base are classified; no claim is made for unequal upper and lower heights, arbitrary triangular bases, other bipyramids, or other brightness anisotropy functionals. The result concerns extreme shadow areas, not the full probability distribution of shadow area or the random shadow's vertex count. A historically earlier equivalent optimization under different terminology cannot be excluded without a comprehensive bibliographic review; mathematical priority remains provisional. Numerical checks alone are not used to assert a continuous-parameter theorem. No independent expert audit has been performed.

## References

1. A. E. Black and F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936 (first posted 2024-06-11); open full text published *Discrete & Computational Geometry* (2026), https://doi.org/10.1007/s00454-026-00880-4.
2. E. W. Weisstein, *Cauchy's Projection Formula*, MathWorld, https://mathworld.wolfram.com/CauchysProjectionFormula.html (classical formula and references).
3. *The Triangular Bipyramid*, polyhedral geometry reference, https://www.qfbox.info/4d/J12 (geometric model and illustrative projections; not a source for the optimization claim).
