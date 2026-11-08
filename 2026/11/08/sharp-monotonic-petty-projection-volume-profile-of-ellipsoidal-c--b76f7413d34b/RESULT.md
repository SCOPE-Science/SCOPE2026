# Sharp monotonic Petty projection-volume profile of ellipsoidal capsules

## Finding

For every integer \(d\ge3\), let \(B_d\) be the Euclidean unit ball and \(\kappa_j=\operatorname{vol}_j(B_j)\). Let \(K_t=B_d+[-t,t]e_d\), \(t\ge0\). Define the (unpolarized) projection body by \(h_{\Pi K}(u)=\operatorname{vol}_{d-1}(\operatorname{proj}_{u^\perp}K)\) for unit \(u\), and its Petty projection-volume quotient by
\[
\mathcal Q_d(K)=\frac{\operatorname{vol}_d(\Pi K)}{\operatorname{vol}_d(K)^{d-1}}.
\]
Then \(\mathcal Q_d(K_t)\) is **strictly increasing** for \(0<t<\infty\), starting with the ball value and approaching a sharp cylindrical degeneration limit:
\[
\boxed{\quad
\frac{\kappa_{d-1}^{d}}{\kappa_d^{d-2}}
<\mathcal Q_d(K_t)<
2\kappa_{d-1}^{2}\left(\frac{\kappa_{d-2}}{\kappa_{d-1}}\right)^{d-1}
\quad(t>0).\quad}
\]
The lower bound is attained at \(t=0\), and the upper bound is never attained for finite \(t\), but is the limit as \(t\to\infty\). The same statement holds for every ellipsoid-plus-segment \(E+[-v,v]\): if \(E=T B_d\), the corresponding parameter is \(t=\|T^{-1}v\|_2\).

The entire profile is a degree-\(d-1\) Bernstein polynomial in
\[
y=\frac{2\kappa_{d-1}t}{\kappa_d+2\kappa_{d-1}t}\in[0,1),
\qquad
\mathcal Q_d(K_t)=\sum_{j=0}^{d-1}\binom{d-1}{j}u_{d,j}y^j(1-y)^{d-1-j},
\]
where, with \(I_m=\int_0^1(1-s^2)^{m/2}\,ds\),
\[
u_{d,j}=\frac{2\kappa_{d-1}^{d-j+1}\kappa_{d-2}^{j} I_{d-1-j}}{\kappa_d^{d-1-j}\kappa_{d-1}^{j}},
\quad 0\le j\le d-1.
\]
Its coefficients satisfy \(u_{d,0}=u_{d,1}<u_{d,2}<\cdots<u_{d,d-1}\). In dimension three the entire formula reduces to
\[
\boxed{\quad
\mathcal Q_3(K_t)=\frac{3\pi^2}{4}+\left(8-\frac{3\pi^2}{4}\right)
\left(\frac{t}{t+2/3}\right)^2.\quad}
\]

## Assumptions and scope

The dimension \(d\) is any integer at least three; \(t\) is any nonnegative real number. All Euclidean balls are centered and of radius one, and the segment is centered and lies along a unit direction. The quotient uses the **volume of the projection body itself**, not the volume of its polar. Euclidean volumes in each dimension use the standard Lebesgue normalization. An affine ellipsoid-plus-segment is \(T(B_d+[-T^{-1}v,T^{-1}v])\), with invertible \(T\).

## Proof

**Step 1: projection-body identity.** An orthogonal projection of \(K_t\) onto a hyperplane \(u^\perp\) is a unit \((d-1)\)-ball swept through the projected segment. Fubini along that segment gives its volume
\[
h_{\Pi K_t}(u)=\kappa_{d-1}+2t\kappa_{d-2}\sqrt{1-\langle u,e_d\rangle^2}.
\]
The last square-root is the support function of the unit \((d-1)\)-disk embedded in \(e_d^\perp\). Therefore, as an equality of convex bodies,
\[
\Pi K_t=aB_d+bB_{d-1}(e_d^\perp),\qquad
 a=\kappa_{d-1},\quad b=2t\kappa_{d-2}.
\]
The volume of \(K_t\) is \(\kappa_d+2t\kappa_{d-1}\).

**Step 2: exact projection-body volume.** At axial height \(z\in[-a,a]\), the \((d-1)\)-dimensional section of \(\Pi K_t\) is a ball of radius \(b+\sqrt{a^2-z^2}\). Thus
\[
\operatorname{vol}_d(\Pi K_t)=
\kappa_{d-1}\int_{-a}^{a}\left(b+\sqrt{a^2-z^2}\right)^{d-1}dz
=2\kappa_{d-1}\sum_{j=0}^{d-1}
\binom{d-1}{j}a^{d-j}b^j I_{d-1-j}.
\]
Expand \((\kappa_d+2t\kappa_{d-1})^{d-1}\) by the binomial theorem. Division gives exactly the Bernstein representation displayed above, using \(y=2t\kappa_{d-1}/(\kappa_d+2t\kappa_{d-1})\).

**Step 3: strict coefficient order.** The ball-slice formula gives
\[
\kappa_m=2\kappa_{m-1}I_{m-1},\qquad
\frac{u_{d,j+1}}{u_{d,j}}=
\frac{\kappa_{d-2}\kappa_d}{\kappa_{d-1}^{2}}
\frac{I_{d-2-j}}{I_{d-1-j}}.
\]
At \(j=0\) the ratio is exactly one. The sequence \(I_m\) is strictly log-convex: by strict Cauchy-Schwarz,
\(I_m^2<I_{m-1}I_{m+1}\) for each integer \(m\ge1\), since \(s\mapsto\sqrt{1-s^2}\) is nonconstant on \((0,1)\). Consequently \(I_{m-1}/I_m\) decreases strictly as \(m\) increases. For every \(j\ge1\), the above ratio is strictly larger than at \(j=0\), and \(u_{d,j+1}>u_{d,j}\).

**Step 4: strict monotonicity and sharp endpoints.** Differentiating the Bernstein form gives
\[
\frac{d\mathcal Q_d}{dy}=(d-1)\sum_{j=0}^{d-2}\binom{d-2}{j}
 (u_{d,j+1}-u_{d,j})y^j(1-y)^{d-2-j}>0
\]
for all \(0<y<1\): the \(j=0\) difference vanishes, but at least the \(j=1\) term is strictly positive because \(d\ge3\). Also \(dy/dt>0\). At \(y=0\) the value is \(u_{d,0}=\kappa_{d-1}^{d}/\kappa_d^{d-2}\); as \(y\uparrow1\), the limit is \(u_{d,d-1}=2\kappa_{d-1}^{2}(\kappa_{d-2}/\kappa_{d-1})^{d-1}\).

**Step 5: the three-dimensional formula and affine extension.** Insert \(\kappa_1=2\), \(\kappa_2=\pi\), \(\kappa_3=4\pi/3\) in the Bernstein polynomial; the degree-two formula follows because \(u_{3,0}=u_{3,1}=3\pi^2/4\), \(u_{3,2}=8\). The coefficient of the squared term is positive, e.g. \(\pi<22/7\) implies \(3\pi^2/4<8\). Under any invertible linear map \(T\), one has \(\Pi(TK)=|\det T|T^{-\mathsf T}\Pi K\), hence the quotient is invariant. Rotate \(T^{-1}v\) to the final coordinate axis to obtain the ellipsoid-plus-segment assertion.

## Verification

Run `python3 check.py` from the same directory as this document. The standard-library script reconstructs the coefficient identities, compares the exact polynomial volume formula with independent direct numerical quadrature in dimensions three through twelve, verifies endpoint ordering and sampled monotonicity, and checks the three-dimensional formula by a rational symbolic polynomial calculation. It completed 214 comparisons without error. These checks are supplementary; the proof for every dimension is the exact coefficient-order argument in Step 3.

## Relationship to prior work

The September 11, 2026 preprint of Mielke-Sulz proves the projection-volume inequality for all bodies of revolution in every dimension at least three, with ellipsoid equality. A separate 2026 paper proves the inequality for general convex bodies in dimensions at least four. Those global inequalities imply the ball's *lower bound*, but neither gives the exact profile for the ball-plus-segment family, its strict path monotonicity, the sharp cylindrical limiting value, or the Bernstein coefficient order. Existing projection-body and mixed-volume identities support the calculation, but the ratio monotonicity requires the strict moment comparison above.

## Limitations

No claim is made for Minkowski sums of general nonspherical bodies and segments, for paths formed by other summands, or for the **polar** Petty quotient. The infinite-length endpoint is a degeneration and is not itself a full-dimensional finite capsule; the limiting inequality is strict for every finite segment. This is not a new proof of the universal Petty conjecture. A broader historical search may uncover an equivalent special-family formula under other terminology; no assertion of independent external validation is made.

## References

1. Florian Mielke-Sulz, *The Petty Conjecture for Convex Bodies of Revolution*, arXiv:2609.13517, first public version September 11, 2026, https://arxiv.org/abs/2609.13517.
2. *Petty's projection-volume conjecture in dimensions at least four*, September 24, 2026; public paper exposition at https://wcook04.github.io/plectis-atlas/papers/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026.html.
3. D. Langharst, M. Roysdon, A. Zvavitch, *General measure extensions of projection bodies*, Proc. London Math. Soc. 125 (2022), 1083–1129, https://doi.org/10.1112/plms.12477 (projection-body context; the paper focuses on a different, polar quotient).
