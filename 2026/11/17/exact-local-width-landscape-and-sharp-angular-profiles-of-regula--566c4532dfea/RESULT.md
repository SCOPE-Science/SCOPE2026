# Exact local-width landscape and sharp angular profiles of regular simplices

## Finding
Let \(N\ge3\), let \(H_N=\{u\in\mathbb R^N:\sum_i u_i=0\}\), and let \(D_{N-1}=\operatorname{conv}\{e_1,\ldots,e_N\}\), regarded as a Euclidean \((N-1)\)-simplex in its affine hull. Its directional width for \(u\in H_N\) of norm one is
\[
W(u)=\max_{1\le i\le N}u_i-\min_{1\le i\le N}u_i.
\]
For each nonempty proper \(S\subset[N]\), write \(t=|S|\), \(s=N-t\), and set
\[
 u^S_i=\begin{cases}-\sqrt{\dfrac{s}{Nt}},&i\in S,\\[2mm]
 +\sqrt{\dfrac{t}{Ns}},&i\notin S.
 \end{cases}
\]
Then **all and only** the strict local minimizers of \(W\) on the unit sphere of \(H_N\) are the \(2^N-2\) vectors \(u^S\). There are no other (even non-strict) local minima. Their widths are
\[
 W(u^S)=w_{N,t}:=\sqrt{\frac{N}{t(N-t)}}.
\]
Thus all local minima are global precisely for the balanced splits \(t\in\{\lfloor N/2\rfloor,\lceil N/2\rceil\}\); when \(N\ge4\) the remaining minima are genuine suboptimal traps.

There is an additional **exact finite-angle local profile**. Put
\[
 \gamma_{N,t}:=\frac{1}{\sqrt{\max\{t(t-1),s(s-1)\}}},\qquad
 \Theta_{N,t}:=\arctan\!\frac{w_{N,t}}{\sqrt2}.
\]
For every \(0<\theta<\Theta_{N,t}\), using the intrinsic spherical angle in \(H_N\),
\[
 \boxed{\min_{\substack{u\in H_N,\ \|u\|=1\\
                    \langle u,u^S\rangle=\cos\theta}}W(u)
       =w_{N,t}\cos\theta+\gamma_{N,t}\sin\theta.}
\]
Every asserted minimum is attained. In particular, the exact sharp one-sided local growth modulus is
\[
 \lim_{\theta\downarrow0}\frac{\min_{\angle(u,u^S)=\theta}W(u)-W(u^S)}{\theta}=\gamma_{N,t}>0.
\]
For a regular simplex of **unit** edge length, divide every width and its angular growth modulus by \(\sqrt2\); the angular range is unchanged.

## Assumptions and scope
The direction sphere is \(\mathbb S(H_N)=\{u\in H_N:\|u\|_2=1\}\), with the intrinsic metric \(\angle(u,v)=\arccos\langle u,v\rangle\). The vectors \(u\) and \(-u\) are regarded as distinct oriented directions; they encode the same unoriented line. Therefore there are \(2^{N-1}-1\) unoriented local-minimum lines. This statement concerns the *directional projection-width function*, not the inradius of the simplex, its section volume, or a width computed with an arbitrary norm.

The finite-angle formula is established on the **stated sufficient open interval**, not claimed to hold up to the first possible global crossover. No assertion is made about the full width profile beyond that interval. At a fixed \(t\), the vectors indexed by the subsets of size \(t\) have identical local geometry by coordinate permutation.

## Proof
**1. A rescaling equivalence.** For any nonconstant \(z\in H_N\), write \(R=\max z_i-\min z_i>0\) and \(y_i=(z_i-\min z)/R\). Then \(0\le y_i\le1\), its minimum is zero and maximum is one, and centering \(y\) gives \(z=R(y-\bar y\mathbf1)\). Consequently for the unit normalization of \(z\),
\[
 W\left(\frac z{\|z\|}\right)=\left[\sum_{i=1}^N(y_i-\bar y)^2\right]^{-1/2}.
\]
Let \(E(y)=\sum_i(y_i-\bar y)^2\). It has the elementary variation formula
\[
 E(y+\varepsilon e_j)-E(y)
 =2\varepsilon(y_j-\bar y)+\varepsilon^2(1-1/N).
\]
If a coordinate lies strictly between zero and one, one can move it slightly outward relative to \(\bar y\) while retaining the extreme coordinates \(0\) and \(1\); when it equals \(\bar y\), either small change increases \(E\). The displayed formula gives a strictly larger \(E\), hence a strictly *smaller* normalized width, arbitrarily nearby. Therefore every local minimum of \(W\) must have exactly two coordinate values, and after unit norm and zero-sum normalization is one of the displayed \(u^S\). Each such vector has the asserted \(w_{N,t}\) by direct substitution.

**2. Spherical directions tangent to a candidate.** Fix \(u^S\), with low block \(L=S\) of size \(t\) and high block \(U=S^c\) of size \(s\). The tangent unit sphere at \(u^S\) consists exactly of the vectors \(v\) satisfying
\[
 \|v\|=1,\quad \sum_{i\in L}v_i=0,\quad\sum_{i\in U}v_i=0.
\]
Indeed, \(v\perp\mathbf1\) and \(v\perp u^S\) are equivalent to the two block-sum constraints because the two values of \(u^S\) differ. Every nearby spherical direction is uniquely \(u=\cos\theta\,u^S+\sin\theta\,v\) for \(\theta\in(0,\pi)\) and unit tangent \(v\).

**3. Separation of the two blocks.** Since \(\|v\|=1\), any coordinate difference satisfies \(|v_i-v_j|\le\sqrt2\). For \(0<\theta<\Theta_{N,t}\),
\[
 \cos\theta\,w_{N,t}-\sqrt2\sin\theta>0.
\]
Thus *every* coordinate in \(U\) remains larger than *every* coordinate in \(L\). Therefore, identically for every tangent unit vector,
\[
 W(\cos\theta\,u^S+\sin\theta\,v)
 =w_{N,t}\cos\theta+\sin\theta\big(\max_{U}v_i-\min_Lv_i\big).
\]
This exact identity reduces the angular optimization to a homogeneous finite-dimensional one.

**4. Sharp block inequality.** If \(x_1,\ldots,x_r\) have zero sum and maximum \(a\ge0\), then \(a-x_i\ge0\), \(\sum_i(a-x_i)=ra\), and
\[
 \sum_i x_i^2=\sum_i(a-x_i)^2-ra^2
 \le (ra)^2-ra^2=r(r-1)a^2.
\]
The same result holds with \(a\) replaced by minus the minimum. Equality for \(r\ge2\) occurs, after permutation, at \((-(r-1)a,a,\ldots,a)\) or its negative. For tangent \(v\), define \(a=\max_Uv_i\ge0\), \(b=-\min_Lv_i\ge0\), and \(M=\max\{s(s-1),t(t-1)\}\). Summing the block inequalities gives
\[
 1=\|v\|^2\le s(s-1)a^2+t(t-1)b^2
 \le M(a+b)^2.
\]
Hence \(\max_Uv_i-\min_Lv_i=a+b\ge M^{-1/2}=\gamma_{N,t}\). Equality is achievable: if \(s\ge t\), set the entire low block to zero and the high block to the permutation of \((-(s-1)\gamma,\gamma,\ldots,\gamma)\); if \(t>s\), interchange the blocks and reverse signs. These vectors have tangent norm one and attain \(a+b=\gamma\), including singleton blocks.

**5. Conclusion and strictness.** Minimizing the exact expression of Step 3 with the attained bound of Step 4 gives the boxed finite-angle formula. Since \(\gamma_{N,t}>0\), the right derivative at zero is strictly positive. By the exact formula the difference from \(w_{N,t}\) is positive throughout some punctured spherical neighborhood, so every \(u^S\) is a strict local minimizer. Step 1 excludes any others. The widths are minimized when \(t(N-t)\) is maximized, giving the balanced global minima and the existence of nonglobal ones for \(N\ge4\). Each nonempty proper \(S\) gives a distinct oriented vector, giving exactly \(2^N-2\) of them.

## Verification
An independently implemented finite checker is included as `check_width_landscape.py`. Execute `python3 check_width_landscape.py` using Python 3 with its standard library. It checks all \(135\) nontrivial partition sizes over \(3\le N\le17\), the exact norm/width normalizations and combinatorial counts, \(10{,}797\) exact-integer tangent inequalities, the analytic equality constructions, and \(5{,}400\) additional finite-angle comparisons. It printed:

`SIMPLEX_WIDTH_LANDSCAPE_CHECKS_PASSED dimensions=15 orbit_ranks=135 exact_inequalities=10797 sharp_geodesics=135 angular_tests=5400`

These bounded checks do not prove the infinite-dimensional family. Steps 1–5 prove the claims for all specified integers and all real angles in the stated range. The checker is not an independent review or certification.

## Relationship to prior work
The width of a regular simplex and its globally minimizing balanced directions are classical. Gritzmann and Klee (1992, §4, especially (4.1)) enumerate complementary-face supporting-hyperplane separations as *candidates* for the global simplex width; their formulas already contain all the heights \(w_{N,t}\). Alexander (1977) also gave complementary-face separation formulas, as quoted explicitly by Lacoste-Julien and Jaggi (2015, Appendix B.1). Har-Peled and Robson (arXiv:2301.02616, §1, first publicly posted January 6, 2023) give a direct proof of the *global* width and identify its minimizing directions.

The present contribution is not a new formula for those supporting-face distances or the overall minimum width. It is the **full strict local-minimum landscape** and, crucially, the **attained sharp finite-angle angular envelope and linear growth modulus at every complementary partition**, including all suboptimal partitions. The cited global formulas alone do not provide these spherical-neighborhood minimizations or their sharp conical constants. Related general work on width Lipschitz bounds gives upper, not these lower stability moduli. A broader earlier equivalent derivation cannot be excluded without further archival inspection.

## Limitations
The interval \((0,\Theta_{N,t})\) is a certified domain of validity for the exact profile, not a claim of maximal extension. The formulas use the standard Euclidean realization with edge length \(\sqrt2\), and rescale linearly with edge length. The source-priority comparison is necessarily provisional: the full text of Alexander's 1977 paper was not accessible through the checked open routes. This work has received self-review only; there has been no independent audit.

## References
- S. Har-Peled and E. W. Robson, *On the Width of the Regular \(n\)-Simplex*, arXiv:2301.02616 (first public version January 6, 2023), https://arxiv.org/abs/2301.02616.
- P. Gritzmann and V. Klee, *Inner and Outer \(j\)-Radii of Convex Bodies in Finite-Dimensional Normed Spaces*, Discrete & Computational Geometry 7 (1992), 255–280, https://doi.org/10.1007/BF02187841.
- R. Alexander, *The Width and Diameter of a Simplex*, Geometriae Dedicata 6 (1977), 87–94, https://doi.org/10.1007/BF00181583.
- S. Lacoste-Julien and M. Jaggi, *On the Global Linear Convergence of Frank-Wolfe Optimization Variants*, arXiv:1511.05932 (2015), Appendix B.1, https://arxiv.org/abs/1511.05932.
