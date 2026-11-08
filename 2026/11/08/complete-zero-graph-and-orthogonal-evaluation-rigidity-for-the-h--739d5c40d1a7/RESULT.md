# Complete zero graph and orthogonal-evaluation rigidity for the half-lattice Hardy kernel

## Finding
For the canonical Hilbert Hardy space \(H^2(\mathbb Z+i\mathbb Z_{\ge0})\) of discrete holomorphic functions, **all** zeros of its Szegő kernel and all orthogonal families of its point-evaluation kernels admit an exact description.

Let \(z=m+in\) and \(w=u+iv\), where \(m,u\in\mathbb Z\) and \(n,v\in\mathbb Z_{\ge0}\). Put \(d=m-u\), \(N=n+v\). The kernel \(K(z,w)\) is zero precisely when
\[
\bigl(N=0\ \text{and}\ d\in 2\mathbb Z\setminus\{0\}\bigr)
\quad\text{or}\quad
\bigl(N\ge1\ \text{is odd and}\ d=0\bigr).
\]
More sharply, for \(N\ge1\), \(K(z,w)\) is strictly positive real if \(d+N\) is even; if \(d+N\) is odd, it is purely imaginary and has the same sign of imaginary part as \(d\), vanishing only when \(d=0\). For \(N=0\), the diagonal value is \(1/2\); for nonzero odd \(d\), it equals \(i/(\pi d)\), and for nonzero even \(d\) it vanishes.

Consequently, any collection of pairwise orthogonal nonzero reproducing kernels containing a point at positive height has at most **two** members. Every such orthogonal pair has equal horizontal coordinate and heights with odd sum. In contrast, any collection of distinct boundary sites of a single parity has pairwise orthogonal kernels, and the normalized kernels on either whole boundary parity class form an orthonormal basis.

## Assumptions and scope
The space and its normalization are those of Dellepiane, Monguzzi and Monti (2026). The boundary Fourier transform is unitary and supported on \([0,\pi]\); the kernel is
\[
K(z,w)=C(d+iN),\qquad
C(d+iN)=\frac1{2\pi}\int_0^\pi e^{idt}
\left(\frac{\cos t}{1+\sin t}\right)^N\,dt
\quad (N\in\mathbb Z_{\ge0}).
\]
Here \(d\in\mathbb Z\) and \(N\in\mathbb Z_{\ge0}\), and \(0^0\) at the isolated midpoint is interpreted by the continuous \(N=0\) integrand. No assertion is made about other discretizations, different Hardy norms or arbitrary kernel combinations.

## Proof
**1. Phase splitting.** Set \(\rho(t)=\cos t/(1+\sin t)\) on \([0,\pi/2]\). Then \(\rho(0)=1\), \(\rho(\pi/2)=0\), and \(\rho'(t)=-\rho(t)\sec t<0\) on the interior. Reflection about \(\pi/2\) gives \(\rho(\pi-t)=-\rho(t)\) before restriction to the half-interval. Thus, for every \(N\ge1\),
\[
C(d+iN)=\frac1{2\pi}\int_0^{\pi/2}
\rho(t)^N\left[e^{idt}+(-1)^{d+N}e^{-idt}\right]dt.
\]
When \(d+N\) is even, this reduces to the real quantity
\[
C(d+iN)=\frac1\pi\int_0^{\pi/2}\rho(t)^N\cos(dt)\,dt
=\tfrac12 P_N(d),
\]
where \(P_N(d)=2\operatorname{Re}C(d+iN)\) is the discrete Poisson kernel.

**2. Strictness of the real branch.** The nonnegativity \(P_N(d)\ge0\), diagonal harmonicity for all interior vertices and the boundary condition \(P_0(d)=\mathbf 1_{\{d=0\}}\) are established in the motivating source. The diagonal-lattice nearest-neighbor graph on \(\{(d,N):N\ge0,\ d+N\text{ even}\}\) is connected to \((0,0)\). If \(P_N(d)=0\) at an interior vertex of that graph, nonnegativity and its four-neighbor averaging equation force all four neighbors to vanish. Iterating along a path to \((0,0)\) contradicts \(P_0(0)=1\). Therefore \(P_N(d)>0\) whenever \(N\ge1\) and \(d+N\) is even. The boundary case \(N=0\) is treated in step 4.

**3. Strictness of the imaginary branch.** If \(d+N\) is odd, then
\[
C(d+iN)=\frac i\pi\int_0^{\pi/2}g_N(t)\sin(dt)\,dt,
\quad g_N(t)=\rho(t)^N.
\]
For \(N\ge1\), \(g_N\) is absolutely continuous, decreases strictly from \(1\) to \(0\), and \(-g_N'(t)=N\sec(t)g_N(t)>0\) on \((0,\pi/2)\). Integrating by parts or applying Fubini yields, for every integer \(d>0\),
\[
\int_0^{\pi/2}g_N(t)\sin(dt)\,dt
=\frac1d\int_0^{\pi/2}(-g_N'(s))(1-\cos(ds))\,ds>0.
\]
The integral is strictly positive because the integrand is nonnegative and strictly positive on a set of positive measure. Oddness in \(d\) treats \(d<0\); at \(d=0\), the imaginary branch is exactly zero, which requires odd \(N\).

**4. Boundary cases.** When \(N=0\), direct integration gives
\[
C(d)=\frac{1}{2\pi}\int_0^\pi e^{idt}dt
=\begin{cases}
1/2,&d=0,\\
0,&d\ne0\ \text{even},\\
i/(\pi d),&d\ \text{odd}.
\end{cases}
\]
Steps 2–4 prove the full kernel zero and phase description, without treating numerical nonvanishing as a proof.

**5. Orthogonal interpolation geometry.** In a reproducing-kernel Hilbert space, distinct point-evaluation kernels are orthogonal exactly when their kernel value vanishes. If an orthogonal pair contains an interior point, the first part forces their horizontal coordinates to agree and their height sum to be odd. A third kernel orthogonal to both would also need the same horizontal coordinate; it would have to have height parity opposite to each of two already opposite parities, an impossibility. Thus the sharp maximum is two. Existence is witnessed by \(z=i\), \(w=0\). If all points lie on the boundary, orthogonality is equivalent to same parity and distinctness. Completeness of each entire boundary parity family follows from the already known Paley–Wiener orthonormal-basis theorem; it is not claimed as novel.

## Verification
The standalone `CHECK.py` numerically integrates the **actual full kernel** at 792 integer parameter combinations and symmetry tests, including all four zero/phase branches. It runs with Python 3 and `mpmath>=1.3.0` and should print `PASS 792 finite numerical classifications and symmetry checks`. The proof covers every integer offset and every pair of nonnegative heights; the finite numerical tests are supplementary only. In particular, the strict positivity of the real branch requires a strong minimum-principle step not supplied by numerical computations.

## Relationship to prior work
The full primary source is E. Dellepiane, A. Monguzzi and M. Monti, *Hardy spaces of discrete holomorphic functions on the upper half-lattice*, arXiv:2607.17726v1 (2026-07-20). Their formulas (24)–(25) give the real/imaginary phase decomposition, Lemma 3.5 proves **nonnegative** Poisson values, Lemma 2.5 notes that the Cauchy kernel vanishes on two parity subsets, and Proposition 4.4 supplies the boundary orthonormal bases. These are used as explicit inputs, not reproved or attributed as new. The present result adds the converse zero statement by establishing strictness on every other lattice site and deduces a sharp complete classification of pairwise orthogonal kernel families containing interior evaluations. The primary source's statements do not give this full phase/orthogonality classification. Duffin's 1956 discrete analytic kernel theory is an acknowledged historical precursor; an equivalent zero-locus or strict-sign theorem might be present in older terminology.

## Limitations
The theorem concerns exactly the canonical upper-half-lattice Hilbert Hardy kernel; it does not resolve zeros of the separately introduced discrete Bergman kernel or of general discrete analytic functions. No publication-priority claim beyond the inspected material is made. No independent mathematical audit has been performed.

## References
Dellepiane, E., Monguzzi, A., and Monti, M., *Hardy spaces of discrete holomorphic functions on the upper half-lattice*, arXiv:2607.17726v1, 2026-07-20. https://arxiv.org/abs/2607.17726. Open full manuscript: https://www.researchgate.net/publication/410636387_Hardy_spaces_of_discrete_holomorphic_functions_on_the_upper_half-lattice.

Duffin, R. J., *Basic properties of discrete analytic functions*, Duke Mathematical Journal 23 (1956), 335–363, DOI:10.1215/S0012-7094-56-02332-8. Historical kernel formula; completeness of exact zero classification not verified from this source.
