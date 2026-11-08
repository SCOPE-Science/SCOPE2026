# Four optimal-latitude regimes for pure cubic spherical harmonics

## Finding

For every integer \(d\ge3\), let \(\mathcal H_3(S^{d-1};\mathbb C)\) be the space of restrictions of complex homogeneous harmonic cubics, with normalized full-sphere \(L^2\) norm. For \(0<z<1\), restrict every harmonic to the latitude
\[
\Sigma_{d,z}=\{(t,y)\in S^{d-1}:t=\sqrt z\}
\]
with normalized latitude probability measure. Let \(G_{d,z}\) denote the positive restriction Gram operator and \(B_d(z)=\lambda_{\min}(G_{d,z})\). This is a continuous-function-value observation norm, not a finite sampling matrix.

Its four eigenvalue sectors, indexed by the harmonic degree \(j\) in the transverse \(d-1\) variables, are
\[
\begin{aligned}
\lambda_0&=\frac{d(d+4)}{6(d-1)}z((d+2)z-3)^2,\\
\lambda_1&=\frac{d(d+4)}{2(d-1)(d+1)}(1-z)((d+2)z-1)^2,\\
\lambda_2&=\frac{d(d+2)(d+4)}{(d-1)(d+1)}z(1-z)^2,\\
\lambda_3&=\frac{d(d+2)(d+4)}{(d-1)(d+1)(d+3)}(1-z)^3.
\end{aligned}
\]
Their respective multiplicities are
\[
1,\quad d-1,\quad\frac{(d-2)(d+1)}2,\quad\frac{(d-1)(d-2)(d+3)}6.
\]
The restriction is injective for \(0<z<1\) except at \(z=1/(d+2)\), with nullity \(d-1\), and at \(z=3/(d+2)\), with nullity \(1\).

Put \(x=(d+2)z\). **The squared latitude maximizing \(B_d(z)\) is unique for every integer \(d\ge3\)**, and its defining equation changes according to four regimes:

1. \(d=3\): \(x_*\in(0,1)\) is the unique root of \(\lambda_1=\lambda_2\).
2. \(d=4\): \(x_*\in(1,3)\) is the unique root of \(\lambda_1=\lambda_3\).
3. \(5\le d\le11\): \(x_*\in(1,3)\) is the unique root of \(\lambda_0=\lambda_1\).
4. \(d\ge12\): \(x_*\in(3,5)\) is the unique root of \(\lambda_0=\lambda_3\).

Here each \(\lambda_j\) is evaluated at \(z=x/(d+2)\). The sharp lower frame bound is the common value of the stated active pair. The opposite signed latitude has the same Gram spectrum, so uniqueness concerns the squared latitude.

For the high-dimensional regime, \(x_*\) tends to the unique \(c\in(3,5)\) satisfying
\[
c(c-3)^2=6,\qquad c=4.195823345445944\ldots,
\]
and \(\max_{0<z<1}B_d(z)\to1\). Thus \(dz_*\to c\), although this is **not** an asymptotically tight frame claim: the other eigenvalue sectors remain larger than one.

## Assumptions and scope

The only free design parameter is one squared latitude \(0<z<1\). Source harmonics have normalized surface-probability \(L^2\) norm; target latitudes have normalized conditional surface-probability norm. All degrees are **pure degree three**, all transverse angular positions are observed continuously and equally weighted, and coefficient fields are complex. Gram eigenvalues are **squared singular values**. The optimization maximizes the minimum squared singular value, not the ratio of extreme singular values.

## Proof

Write \((t,y)\in S^{d-1}\) with \(y=\sqrt{1-t^2}\,\omega\), where \(\omega\in S^{d-2}\). Let \(Y_j(\omega)\) be an arbitrary unit-norm transverse spherical harmonic of degree \(j\). Harmonic extension and separation of variables give, up to nonzero constants independent of \(t\), the four radial factors
\[
\begin{aligned}
R_0(t)&=t((d+2)t^2-3),\\
R_1(t)&=\sqrt{1-t^2}\,((d+2)t^2-1),\\
R_2(t)&=t(1-t^2),\\
R_3(t)&=(1-t^2)^{3/2}.
\end{aligned}
\]
Indeed, their parent homogeneous harmonic polynomials are respectively \(t^3-3t|y|^2/(d-1)\), \((t^2-|y|^2/(d+1))H_1(y)\), \(tH_2(y)\), and \(H_3(y)\). Their dimensions sum to \(d(d-1)(d+4)/6=\dim\mathcal H_3\). Distinct transverse degrees are mutually orthogonal both on the full sphere and on each latitude. For a full-sphere uniform coordinate \(T\),
\[
\mathbb ET^2=\frac1d,\quad
\mathbb ET^4=\frac3{d(d+2)},\quad
\mathbb ET^6=\frac{15}{d(d+2)(d+4)}.
\]
Substitution gives
\[
\begin{aligned}
\mathbb ER_0(T)^2&=\frac{6(d-1)}{d(d+4)},\\
\mathbb ER_1(T)^2&=\frac{2(d-1)(d+1)}{d(d+4)},\\
\mathbb ER_2(T)^2&=\frac{(d-1)(d+1)}{d(d+2)(d+4)},\\
\mathbb ER_3(T)^2&=\frac{(d-1)(d+1)(d+3)}{d(d+2)(d+4)}.
\end{aligned}
\]
Consequently \(\lambda_j=R_j(\sqrt z)^2/\mathbb ER_j(T)^2\), proving the spectrum, multiplicities and rank exceptions.

It remains to optimize the lower envelope. In the coordinate \(x=(d+2)z\), split the full open design interval into \((0,1)\), \((1,3)\), and \((3,d+2)\). On the first interval \(\lambda_1\) strictly decreases and \(\lambda_2\) strictly increases, so their minimum has a unique maximum at their crossing. On the middle interval \(\lambda_1\) strictly increases, while \(\lambda_0\) and \(\lambda_3\) strictly decrease, so the relevant two-branch envelopes have unique crossings. On the last interval \(\lambda_0\) strictly increases and \(\lambda_3\) strictly decreases, so their minimum has a unique maximum at their crossing. These derivative claims follow directly by differentiating the displayed polynomials; the first and last interval crossing signs hold at their endpoints.

For the finitely many dimensions \(3\le d\le11\), the following **exact rational separation certificate** completes the global comparison. Every coordinate in the final four columns is an integer divided by \(100000\). The barrier \(K_d\) is strictly below the actual minimum of all four eigenvalues at the winning witness \(w_d\); in every *other* interval, the maximum of the two indicated envelope branches at its split point is strictly below \(K_d\). Blank cells mean the winning interval. For the first interval the upper-envelope pair is \((\lambda_1,\lambda_2)\); for the middle, \((\lambda_1,\lambda_3)\) when \(d\le4\) and \((\lambda_0,\lambda_1)\) otherwise; for the last, \((\lambda_0,\lambda_3)\). The monotonicities above turn each split-point inequality into a **global** upper bound on its interval.

| \(d\) | \(K_d\) | \(w_d\) | first split | middle split | last split |
|---:|:---:|---:|---:|---:|---:|
| 3 | \(61/100\) | 27682 | — | 182085 | 327884 |
| 4 | \(14/25\) | 189564 | 27526 | — | 338774 |
| 5 | \(53/100\) | 193236 | 27416 | — | 347455 |
| 6 | \(1/2\) | 192458 | 27335 | — | 354493 |
| 7 | \(12/25\) | 191898 | 27273 | — | 360299 |
| 8 | \(9/20\) | 191475 | 27223 | — | 365164 |
| 9 | \(9/20\) | 191144 | 27183 | — | 369297 |
| 10 | \(23/50\) | 190877 | 27150 | — | 372850 |
| 11 | \(47/100\) | 190659 | 27122 | — | 375936 |

At each winning pair's unique crossing, its other two eigenvalues are **strictly larger**. This last statement is checked using exact rational bisection of the crossing and rational interval arithmetic on all four eigenvalue expressions in the companion checker. The existence, uniqueness and location of each crossing are analytic, and the finite comparisons establish the stated first three dimension regimes without decimal approximations.

For every \(d\ge12\), use the common rational barrier \(K=12/25\). On the first interval, split at \(x=7/20\). The coefficient \(C_d=d(d+4)/((d-1)(d+1))\) decreases in \(d\), so \(C_d\le192/143\); hence both \(\lambda_1(7/20)<12/25\) and \(\lambda_2(7/20)<12/25\). The first-interval envelope is therefore everywhere below \(K\). On the middle interval, split at \(x=19/10\). After clearing positive denominators, the differences \(K-\lambda_0(19/10)\) and \(K-\lambda_1(19/10)\) have, in \(u=d-12\ge0\), respectively the strictly positive numerator polynomials
\[
581u^2+7628u+2112,
\qquad150u^3+3999u^2+29892u+40128.
\]
Thus the entire middle interval is below \(K\).

On the last interval use the explicit witness
\[
x_d=\frac{7(3d+2)}{5(d+2)}\in[19/5,21/5).
\]
At this witness \(\lambda_1>1\) and \(\lambda_2>1\), by \(d+2\ge14\), \(x_d\ge19/5\), \(x_d\le21/5\), and the positive prefactors in their formulas. The other two satisfy \(\lambda_0(x_d)>K\) and \(\lambda_3(x_d)>K\). To certify these universal inequalities, let \(u=d-12\). After clearing the positive denominators \(375(d-1)(d+2)^4\) and \(125(d-1)(d+1)(d+2)^5(d+3)\), their numerators \(\lambda_0-K\) and \(\lambda_3-K\) have, in increasing powers of \(u\), coefficient lists
\[
(4017216,6513472,1811488,203952,10368,198)
\]
and
\[
(668965248,4183074336,2165026584,496258476,63704774,
4920659,228285,5885,65),
\]
all strictly positive. The checker independently verifies the polynomial identities by exact rational arithmetic and degree-bounded polynomial identity testing. Hence the final interval strictly dominates the first two for every integer \(d\ge12\).

The last-interval crossing \(\lambda_0=\lambda_3\) lies in \((3,5)\): at \(x=3\) the first member vanishes, whereas at \(x=5\) it exceeds the second. At the crossing \(\lambda_1>1\) and \(\lambda_2>1\), using \(x\in(3,5)\) and \(d+2\ge14\); meanwhile \(\lambda_3<1\), since \(\lambda_3(3/(d+2))<1\) and \(\lambda_3\) strictly decreases. Thus neither inactive sector interferes and the crossing is the unique global maximizer. Finally uniform convergence of the four rational eigenvalue functions on compact \(x\)-intervals and strict crossing monotonicity give the stated limiting equation and lower-bound limit.

## Verification

Run `python3 check_cubic_latitude.py` with standard Python 3. The script uses exact fractions, interval arithmetic and polynomial identities, with no numerical tolerances and no external package. It prints `CUBIC_LATITUDE_RATIONAL_CERTIFICATE_PASS 201` when all assertions succeed. Exact finite comparisons prove the finitely many dimension exceptions; coefficient-positivity proofs, not finite enumeration, prove the infinite dimension range. The analytical sector decomposition and monotonicity arguments are given above rather than inferred from tests.

## Relationship to prior work

General spherical-harmonic branching and Gegenbauer normalization are classical. Nafees, Khalid, Kennedy and McEwen (arXiv:1709.02497, 8 September 2017) optimize positions of **multiple finite iso-latitude rings** for an iterative full-band spherical harmonic transform, by reducing condition numbers of associated Legendre systems. That is not the continuous **single-latitude pure-degree-three minimum-eigenvalue** problem considered here. Zandieh, Han and Avron (arXiv:2202.12995, 25 February 2022) prove near-optimal randomized **whole-sphere** reconstruction, again not a sharp single-latitude E-optimality classification.

Classical latitude factors and the four spectral branches are not asserted to be intrinsically new. An existing pure-cubic **antipodal-cap concentration** analysis gives integrated beta-moment sector formulas; formally differentiating the cap parameter recovers the latitude densities and therefore much of the sector algebra. The added statement here is the **global sharp optimization with its four distinct dimensional regimes**, which does not follow merely from the cap sector ordering. Bellet, Brachet and Croisille's 2022 cubed-sphere interpolation paper has a different node geometry; only its accessible abstract and references were checked, not a full comparison. The exact four-regime optimization has not been located in the inspected literature or the consulted semantic index; this is not a proof of historical priority.

## Limitations

The result does not cover mixed spherical harmonic degrees, spatially discrete sensors, nonuniform latitude weighting, arbitrary observation distributions or minimum spectral condition number. The dimensional partition and uniqueness are mathematically established under the stated normalization, but independent validation and a comprehensive historical-priority determination have not occurred. Previously known general representation formulas are used as ingredients, not claimed as novel results.

## References

1. W. Nafees, Z. Khalid, R. A. Kennedy and J. D. McEwen, *Optimal-Dimensionality Sampling on the Sphere: Improvements and Variations*, arXiv:1709.02497v1 (first public 2017-09-08), https://arxiv.org/abs/1709.02497.
2. A. Zandieh, I. Han and H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995v1 (first public 2022-02-25), https://arxiv.org/abs/2202.12995.
3. J.-B. Bellet, M. Brachet and J.-P. Croisille, *Interpolation on the cubed sphere with spherical harmonics*, Numerische Mathematik 153 (2023), first online 2022-12-28, https://doi.org/10.1007/s00211-022-01340-w.
4. Standard spherical-harmonic addition and branching formulas, including the harmonic-polynomial construction reproduced in the proof above.
