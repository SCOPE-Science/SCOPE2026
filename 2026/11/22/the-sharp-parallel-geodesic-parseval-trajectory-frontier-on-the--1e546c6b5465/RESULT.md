# The sharp parallel-geodesic Parseval trajectory frontier on the flat two-torus

## Finding

Let \(N\ge 1\) and \(L\ge 2\) be integers. On the flat torus \(\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2\), let \(\mathcal B_N\) be the space of complex trigonometric polynomials with Fourier indices \((k_1,k_2)\in[-N,N]^2\cap\mathbb Z^2\). Equip it with Haar-probability \(L^2\) norm. Consider \(L\) distinct, parallel, primitive closed geodesics, all of one slope \((p,q)\in\mathbb Z^2\) with \(\gcd(|p|,|q|)=1\). Give each geodesic its normalized arclength measure and average the \(L\) measures with equal weight.

Write \(s=\max(|p|,|q|)\). An isometric sampling (Parseval) family of this slope exists **if and only if**
\[
L\ge 1+\left\lfloor\frac{2N}{s}\right\rfloor.
\]
For every slope meeting this condition, a suitable equal-spacing of the geodesics gives exactly
\[
\frac1L\sum_{j=0}^{L-1}\frac1{2\pi}\int_0^{2\pi}
   f(\gamma_j(t))\overline{g(\gamma_j(t))}\,dt
=\int_{\mathbb T^2} f\overline g\,d\mu
\qquad(f,g\in\mathcal B_N).
\]
If the displayed condition fails, **no choice of offsets** can even give injective sampling on \(\mathcal B_N\).

Define the integer \(s_L=1+\lfloor2N/L\rfloor\). The *minimum total trajectory length* among these Parseval families is exactly
\[
\mathcal L_{N,L}=
\begin{cases}
2\pi L, & s_L=1,\\
2\pi L\sqrt{s_L^2+1},&s_L\ge 2.
\end{cases}
\]
The only length-minimizing slope classes are coordinate directions when \(s_L=1\), and the signed coordinate permutations of \((s_L,1)\) when \(s_L\ge2\). All are attained by equal-spacing. Across **all** \(L\ge2\), the unique optimal number of loops is \(L=2N+1\), and the minimum total length is \(2\pi(2N+1)\); then the loops are parallel coordinate circles.

## Assumptions and scope

A primitive geodesic has one period and length \(2\pi\sqrt{p^2+q^2}\), and a family consists of distinct translates of the same such geodesic. The cost counts the sum of those lengths, not travel between loops, sensor setup cost, or arbitrary connecting arcs. The exactness statement concerns equal-weight normalized arclength; nonparallel, non-geodesic, and unequal-weight designs are outside the minimization. There is no claim of a globally shortest *connected* curve or of a shortest arbitrary mobile-sampling path.

## Proof

The orthonormal Fourier basis is \(e_k(x)=\exp(i(k_1x_1+k_2x_2))\), \(k\in[-N,N]^2\cap\mathbb Z^2\). Fix a primitive slope \((p,q)\). Restricting \(e_k\) to a translated geodesic \(\gamma(t)=(pt,qt)+u\) gives a constant phase times the one-dimensional character of frequency \(m(k)=pk_1+qk_2\). Two indices have the same longitudinal frequency if and only if their difference is an integer multiple of \((q,-p)\). Every fiber of \(m\) inside the square is therefore a consecutive finite interval in that lattice direction.

The longest fiber contains exactly \(1+\lfloor 2N/s\rfloor\) indices. Its size cannot be larger because two fiber indices \(r-1\) steps apart have a coordinate difference \((r-1)s\le2N\). Conversely, if \(h=\lfloor2N/s\rfloor\), the coordinate increments of \(h(q,-p)\) have magnitudes at most \(2N\), so a segment of \(h+1\) consecutive lattice indices fits inside the centered integer square after suitable integral translation in each coordinate. Since its frequencies are the same, its span restricts on each translated geodesic to only one common one-dimensional Fourier character. Thus observing \(L\) geodesics has rank at most \(L\) on a fiber of size \(h+1\), proving noninjectivity whenever \(L<h+1\), irrespective of offsets.

For sufficiency choose integers \(a,b\) with \(pb-qa=1\), and set
\[
\gamma_j(t)=\big(pt+2\pi ja/L,\;qt+2\pi jb/L\big)\pmod{2\pi},
\quad 0\le j<L,\quad0\le t<2\pi.
\]
These are \(L\) distinct parallel primitive geodesics. The Gram entry for two Fourier characters is zero if their longitudinal frequencies differ. Otherwise their index difference equals \(r(q,-p)\) for an integer \(r\), and their transverse integer frequencies \(ak_1+bk_2\) differ by \(-r\). The average over \(j\) of \(\exp(-2\pi i jr/L)\) vanishes unless \(L\mid r\). A fiber of size at most \(L\) has \(0<|r|<L\) for distinct indices. Every off-diagonal Gram entry therefore vanishes; all diagonal entries equal one. This proves the asserted Parseval identity.

The criterion becomes \(s>2N/L\), hence the least possible integer \(s\) is \(s_L\). For \(s_L\ge2\), a primitive integer vector of maximal coordinate magnitude \(s\) must have its other coordinate nonzero, so squared length is at least \(s^2+1\), with equality precisely for signed permutations of \((s,1)\). For \(s_L=1\), unit coordinate vectors are uniquely shortest. This proves the fixed-\(L\) cost and classification. Finally, if \(L\le2N\), then \(s_L\ge2\) and the integer \(Ls_L\ge2N+1\) implies
\(L\sqrt{s_L^2+1}>2N+1\). For \(L\ge2N+1\), the cost is \(2\pi L\ge2\pi(2N+1)\), with equality only at \(L=2N+1\). The final statement follows.

## Verification

The standalone Python checker `check_torus.py` enumerates every primitive slope in \([-9,9]^2\), \(N=1,\ldots,7\), and verifies the exact maximum fiber formula and the root-of-unity Gram injectivity/orthogonality test for \(L=1,\ldots,8\). It also checks the minimizing squared winding length exhaustively over a larger square for each \(N=1,\ldots,7\) and \(L=1,\ldots,2N+5\). It reports 12,544 passed integer cases. These finite checks corroborate the symbolic proof; they do not replace the all-parameter argument above.

## Relationship to prior work

Rashkovskii, Ulanovskii, and Zlotnikov (first public version 2020) give general sampling criteria for planar **Euclidean** parallel-line families in Bernstein/Paley–Wiener spaces, not a finite compact-torus length-and-loop frontier. Gröchenig et al. (2015) establish minimal path density for Euclidean mobile sampling. Ehler and Gröchenig (2023) study design curves on spheres. More directly, Kunis (2026, Section 4.1) treats a single primitive winding curve on the two-torus, and Ehler (2026, Theorem 2.1) proves its sharp shortest-curve bound even among arbitrary connected design curves. **The known single-curve result is not claimed as new.** The finding here is the exact \(L\ge2\) disconnected parallel-trajectory Parseval existence criterion, fixed-loop-count Pareto frontier, and its global minimum. The connected-curve lower bound does not cover disconnected unions: for \(L=2N+1\) the total length \(2\pi(2N+1)\) is strictly less than the minimum connected-curve length \(2\pi\sqrt{(2N+1)^2+1}\).

## Limitations

This is a restricted but natural geometry-of-acquisition optimization, not a lower bound for arbitrary mixed slopes, curved trajectories, or unequal weights. The method is elementary Fourier aliasing, and relevant unindexed prior work on periodic mobile sampling could contain an equivalent fixed-loop-count formula. The claim proves exact equal-weight energy reconstruction, not efficient acquisition when transitions between loops incur cost.

## References

1. A. Rashkovskii, A. Ulanovskii, I. Zlotnikov, *On 2-dimensional mobile sampling*, first posted 2020-05-22, https://arxiv.org/abs/2005.11193.
2. K. Gröchenig, J. L. Romero, J. Unnikrishnan, M. Vetterli, *On minimal trajectories for mobile sampling of bandlimited fields*, Applied and Computational Harmonic Analysis 39 (2015), https://doi.org/10.1016/j.acha.2014.11.002.
3. M. Ehler, K. Gröchenig, *t-Design Curves and Mobile Sampling on the Sphere*, first posted 2023-06-19, https://arxiv.org/abs/2306.13152.
4. S. Kunis, *Positive quadrature and mobile sampling of multivariate trigonometric polynomials*, first posted 2026-08-12, https://arxiv.org/abs/2608.11915.
5. M. Ehler, *Optimal bounds for design curves on the torus*, first posted 2026-11-02, https://arxiv.org/abs/2611.03362.
