# A sharp spatial-period cutoff for symmetric Nagumo lattice equilibria

## Finding

For every integer \(n\ge5\), the symmetric Nagumo lattice admits a nonconstant stationary state with **least spatial period exactly \(n\)** if and only if

\[
0<d<d_n^*,\qquad d_n^*=\frac{1}{16\sin^2(\pi/n)}.
\]

If \(d\ge d_n^*\), the only spatially \(n\)-periodic equilibria are the three constant sequences \(0\), \(1/2\) and \(1\). Equality belongs to the nonexistence regime. Below the threshold there is a strictly reflection-odd primitive-period equilibrium: \(u_0=1/2\); for \(1\le j\le\lfloor(n-1)/2\rfloor\), \(1/2<u_j<1\) and \(0<u_{n-j}<1/2\), with \(u_{n-j}=1-u_j\). If \(n\) is even, \(u_{n/2}=1/2\). All components lie in \((0,1)\).

## Assumptions and scope

The bi-infinite, nearest-neighbor lattice has states \(u_j(t)\in\mathbb R\), diffusion \(d>0\), and evolution

\[
\dot u_j=d(u_{j-1}-2u_j+u_{j+1})+u_j(1-u_j)(u_j-1/2),\qquad j\in\mathbb Z.
\]

An \(n\)-periodic equilibrium is an indefinitely repeated vector \((u_0,\ldots,u_{n-1})\) satisfying the stationary equations with cyclic indices. *Least period* means the smallest strictly positive index translation preserving that sequence. No assertion of temporal stability or uniqueness of heterogeneous equilibria is made.

## Proof

**1. Global nonexistence above the cutoff.** Put \(v_j=u_j-1/2\), \(f(v)=v(1/4-v^2)\) and \(\bar v=n^{-1}\sum_j v_j\). Stationarity gives \(d\Delta v_j+f(v_j)=0\). Multiplying by \(v_j-\bar v\), summing cyclically, and using summation by parts yields

\[
d\sum_j(v_{j+1}-v_j)^2
=\sum_j(v_j-\bar v)[f(v_j)-f(\bar v)]
=\frac14\sum_j(v_j-\bar v)^2-\sum_j(v_j-\bar v)^2(v_j^2+v_j\bar v+\bar v^2).
\]

For a nonconstant vector, the last sum is strictly positive: \(v_j^2+v_j\bar v+\bar v^2=(v_j+\bar v/2)^2+3\bar v^2/4\) is nonnegative and can vanish where \(v_j\ne\bar v\) only if both are zero, an impossibility. On the cycle the optimal mean-zero Poincaré constant is \(\lambda_n=4\sin^2(\pi/n)\), by discrete Fourier diagonalization. Hence every nonconstant equilibrium must obey \(d\lambda_n<1/4\), equivalent to \(d<d_n^*\). The constant equilibria solve \(f(v)=0\), giving the stated three.

**2. Variational existence below the cutoff.** For fixed \(n\ge5\), consider the odd-reflection subspace

\[
H_n=\{v\in\mathbb R^n:v_{n-j}=-v_j\text{ for all }j\pmod n\}.
\]

It forces \(v_0=0\), and also \(v_{n/2}=0\) if \(n\) is even. The smooth, coercive energy

\[
\mathcal E_d(v)=\frac d2\sum_j(v_{j+1}-v_j)^2-\frac18\sum_jv_j^2+\frac14\sum_jv_j^4
\]

has a global minimizer on \(H_n\). The vector \(\phi_j=\sin(2\pi j/n)\in H_n\) is an eigenvector with eigenvalue \(\lambda_n\). Consequently,

\[
\mathcal E_d(t\phi)=\frac{t^2}{2}(d\lambda_n-1/4)\sum_j\phi_j^2+\frac{t^4}{4}\sum_j\phi_j^4<0
\]

for sufficiently small nonzero \(t\) whenever \(d<d_n^*\). Thus any minimizer is nonzero.

**3. Full stationarity and strict sign profile.** Because the energy is invariant under \((Rv)_j=-v_{n-j}\), its gradient at an \(R\)-fixed vector lies in \(H_n\). Thus the restricted minimizer is a critical point in the full \(n\)-dimensional space and obeys every stationary equation. On the independent positions \(1,\ldots,m\), where \(m=\lfloor(n-1)/2\rfloor\), replace the free coordinates by their absolute values and retain their negative reflected partners. This preserves the on-site energy and cannot increase any nearest-neighbor squared difference, including the reflected midpoint edge for odd \(n\). Hence there is a nonzero minimizing equilibrium with \(v_j\ge0\) on these positions. If one such coordinate were zero, its stationary equation would force its nonnegative neighbors to be zero; propagation along the half-cycle would force all coordinates to vanish. Thus \(v_j>0\) for every \(1\le j\le m\), with \(v_{n-j}<0\).

At the global positive maximum, \(\Delta v\le0\), so stationarity rules out \(v>1/2\); equality \(v=1/2\) would force both neighbors to equal it and then force a constant sequence, contradicting odd reflection. Hence \(0<\max_jv_j<1/2\), with the analogous bound below. Therefore every original coordinate lies in \((0,1)\).

**4. Least period.** For odd \(n\), the odd-reflection profile has precisely one zero among the \(v_j\), namely \(j=0\), and thus cannot have any proper spatial subperiod. For even \(n\), the only zero positions are \(0,n/2\). A proper period would have to translate the zero set into itself, and hence would have to equal \(n/2\); but translation by \(n/2\) changes the positive half into the negative half. Thus the least period is exactly \(n\). Both directions of the stated criterion are proved.

## Verification

An accompanying standalone Python checker verifies the exact period-three and period-four identities as calibrations, and representative variational stationary patterns for \(n=5,6,7,9\) below the respective thresholds. The universal conclusion follows from the Fourier, energy, symmetry, and maximum-principle arguments above; finite samples are not a proof. A reproducible run yields `VERIFY_OK exact_3_4=4 variational_examples=8 spectral_thresholds=4`.

## Relationship to prior work

Hesoun–Stehlík–Volek (2026) study spatial topological chaos for this bistable lattice in the **small-diffusion** regime. Hupkes–Morelli–Stehlík–Švígler (2019) treat multichromatic waves and compute the symmetric three-site threshold \(d=1/12\), which is therefore **not claimed as new** here. Their study considers three- and four-site patterns rather than the sharp necessary-and-sufficient cutoff for every \(n\ge5\). Švígler (2020) studies existence regions, spatial-period labelling and their enumeration; it explicitly notes the difficulty of determining the boundaries. The present theorem concerns the entire positive diffusion axis, the *presence of at least one primitive-period equilibrium*, and the precise spectral cutoff. It does not classify all existing equilibrium branches. General Fourier, variational, and maximum-principle methods are classical; the asserted contribution is their sharp primitive-period synthesis for this lattice.

## Limitations

This result is specific to the symmetric cubic parameter \(a=1/2\) and nearest-neighbor coupling on a one-dimensional periodic lattice, with periods at least five. It does not establish the number, dynamical stability, or bifurcation histories of all steady patterns. The sharp cutoff concerns existence of at least one primitive spatial period, not all other bifurcation thresholds. Complete inspection of the 2026 primary manuscript was unavailable, so historical priority is subject to that stated limitation and independent review remains outstanding.

## References

1. J. Hesoun, P. Stehlík, J. Volek, *Characterization of spatial topological chaos for bistable lattice equation*, arXiv:2609.25868, first public 2026-09-22, https://arxiv.org/abs/2609.25868.
2. V. Švígler, *Periodic stationary solutions of the Nagumo lattice differential equation: existence regions and their number*, arXiv:2003.14070, first public 2020-03-31, https://arxiv.org/abs/2003.14070.
3. H. J. Hupkes, L. Morelli, P. Stehlík, V. Švígler, *Multichromatic travelling waves for lattice Nagumo equations*, arXiv:1901.07227, first public 2019-01-22, https://arxiv.org/abs/1901.07227.
4. H. J. Hupkes, L. Morelli, P. Stehlík, *Bichromatic travelling waves for lattice Nagumo equations*, arXiv:1805.10977, first public 2018-05-28, https://arxiv.org/abs/1805.10977.
