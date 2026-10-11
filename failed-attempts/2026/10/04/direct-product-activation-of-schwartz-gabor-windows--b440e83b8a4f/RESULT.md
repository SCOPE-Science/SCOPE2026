# Direct-product activation of Schwartz Gabor windows

## Finding

Let \(\Lambda\subset\mathbb R^{2d}\) be a symplectically rational full-rank phase-space lattice. Write
\[
\nu=\nu(\Lambda),
\qquad
r=\nu(\Lambda^\circ),
\]
and assume
\[
\nu>r.
\]
By the covolume identity in the cited classification, this is exactly the strict-density condition
\[
\operatorname{covol}(\Lambda)<1.
\]

For \(k\ge1\), let
\[
\Lambda^{\oplus k}\subset\mathbb R^{2kd}
\]
denote the \(k\)-fold symplectic direct product. Then
\[
\nu(\Lambda^{\oplus k})=\nu^k,
\qquad
\nu((\Lambda^{\oplus k})^\circ)=r^k.
\]

Therefore the exact minimum number of Schwartz-class windows needed for a Gabor frame on the product lattice is
\[
q_{\min}^{\mathcal S}(\Lambda^{\oplus k})
=
\left\lceil
\frac{r^k+kd}{\nu^k}
\right\rceil.
\]

In particular, a one-window Schwartz Gabor frame exists on \(\Lambda^{\oplus k}\) if and only if
\[
\nu^k-r^k\ge kd.
\]
Since \(\nu>r\), this inequality holds for every sufficiently large \(k\). Thus every strictly subcritical symplectically rational lattice becomes one-window Schwartz-admissible after finitely many independent direct-product copies, even if one copy is below the one-window regularity threshold.

For the explicit lattice in Example 1.2(ii) of the primary source,
\[
d=2,\qquad \nu=2,\qquad r=1.
\]
The one-window criterion fails for one and two copies but holds for three:
\[
2^1-1^1=1<2,
\]
\[
2^2-1^2=3<4,
\]
and
\[
2^3-1^3=7\ge6.
\]
The exact minimum number of Schwartz windows is correspondingly
\[
2,\ 2,\ 1.
\]

## Assumptions and scope

The direct product is taken with the block-diagonal symplectic form
\[
\sigma^{\oplus k}
=
\sigma\oplus\cdots\oplus\sigma.
\]
Thus \(\Lambda^{\oplus k}\) is a phase-space lattice for signals in
\[
L^2(\mathbb R^{kd}).
\]

The result concerns existence of Schwartz-class Gabor-frame windows. The one-window produced by the classification on the product space need not be a tensor product of windows from the factors. Indeed, the phenomenon is interesting precisely when the individual factor lattice does not admit any Schwartz one-window frame.

No quantitative frame bounds are asserted. The result also does not claim that the first activating power has a tensor-product extremizer or any uniqueness property.

## Proof

Let
\[
\Lambda_1\subset\mathbb R^{2d_1},
\qquad
\Lambda_2\subset\mathbb R^{2d_2}
\]
be full-rank phase-space lattices, with symplectic forms \(\sigma_1\) and \(\sigma_2\). On the direct sum,
\[
\sigma((z_1,z_2),(w_1,w_2))
=
\sigma_1(z_1,w_1)+\sigma_2(z_2,w_2).
\]

By definition of the adjoint lattice,
\[
(\Lambda_1\oplus\Lambda_2)^\circ
=
\Lambda_1^\circ\oplus\Lambda_2^\circ.
\]
Indeed, a pair \((z_1,z_2)\) has integer symplectic pairing with every \((\lambda_1,\lambda_2)\) if and only if \(z_i\) has integer pairing with every element of \(\Lambda_i\) for each factor separately.

Hence
\[
(\Lambda_1\oplus\Lambda_2)_{\mathrm{int}}
=
(\Lambda_1\oplus\Lambda_2)
\cap
(\Lambda_1^\circ\oplus\Lambda_2^\circ)
=
(\Lambda_1\cap\Lambda_1^\circ)
\oplus
(\Lambda_2\cap\Lambda_2^\circ).
\]
Taking finite group indices gives
\[
[\Lambda_1\oplus\Lambda_2:
(\Lambda_1\oplus\Lambda_2)_{\mathrm{int}}]
=
[\Lambda_1:\Lambda_{1,\mathrm{int}}]
[\Lambda_2:\Lambda_{2,\mathrm{int}}].
\]
The symplectic integrality index is the positive square root of this group index, so
\[
\nu(\Lambda_1\oplus\Lambda_2)
=
\nu(\Lambda_1)\nu(\Lambda_2).
\]
Applying the same argument to the adjoint lattices gives
\[
\nu((\Lambda_1\oplus\Lambda_2)^\circ)
=
\nu(\Lambda_1^\circ)\nu(\Lambda_2^\circ).
\]

Iteration yields
\[
\nu(\Lambda^{\oplus k})=\nu^k,
\qquad
\nu((\Lambda^{\oplus k})^\circ)=r^k.
\]
The signal-space dimension of the \(k\)-fold product is \(kd\).

The sharp multiwindow theorem of Caragea and Pfander states that for a symplectically rational lattice \(\Gamma\subset\mathbb R^{2D}\),
\[
q_{\min}^{\mathcal S}(\Gamma)
=
\left\lceil
\frac{\nu(\Gamma^\circ)+D}
{\nu(\Gamma)}
\right\rceil.
\]
Applying this with
\[
\Gamma=\Lambda^{\oplus k},
\qquad
D=kd,
\]
gives
\[
q_{\min}^{\mathcal S}(\Lambda^{\oplus k})
=
\left\lceil
\frac{r^k+kd}{\nu^k}
\right\rceil.
\]

The one-window criterion is therefore
\[
\frac{r^k+kd}{\nu^k}\le1,
\]
equivalently
\[
\nu^k-r^k\ge kd.
\]

Finally, because \(\nu>r\ge1\),
\[
\nu^k-r^k
=
(\nu-r)
\sum_{j=0}^{k-1}
\nu^{k-1-j}r^j
\ge
(\nu-r)\nu^{k-1}.
\]
The right side grows exponentially in \(k\), while \(kd\) grows linearly. Hence the one-window criterion is eventually satisfied.

For the source lattice with
\[
d=2,\qquad \nu=2,\qquad r=1,
\]
the displayed arithmetic check gives activation at exactly the third direct power.

## Verification

The proof uses only the definitions of adjoint lattice, integral symplectic subgroup, and symplectic integrality index, followed by the exact one-window and multiwindow classification in the primary source.

The direct-product identities are exact group identities:
\[
(\Lambda_1\oplus\Lambda_2)^\circ
=
\Lambda_1^\circ\oplus\Lambda_2^\circ
\]
and
\[
(\Lambda_1\oplus\Lambda_2)_{\mathrm{int}}
=
\Lambda_{1,\mathrm{int}}
\oplus
\Lambda_{2,\mathrm{int}}.
\]
Thus the finite indices multiply before taking square roots.

For the concrete source example,
\[
q_{\min}^{\mathcal S}(\Lambda^{\oplus k})
=
\left\lceil
\frac{1+2k}{2^k}
\right\rceil,
\]
so
\[
q_{\min}^{\mathcal S}(\Lambda)=2,\qquad
q_{\min}^{\mathcal S}(\Lambda^{\oplus2})=2,\qquad
q_{\min}^{\mathcal S}(\Lambda^{\oplus3})=1.
\]

No numerical experiment is used for the general theorem.

## Relationship to prior work

Caragea and Pfander introduce the symplectic integrality index and symplectic index gap and prove the exact one-window and multiwindow regularity classifications. Their one-window theorem says that a symplectically rational lattice admits a Schwartz Gabor-frame window exactly when the gap is at least the signal-space dimension. Their multiwindow theorem gives the exact minimum number of Schwartz windows from the two integrality indices separately.

The primary paper does not state a direct-product law for these indices, does not discuss repeated product powers, and does not identify the resulting finite-power activation phenomenon. The new observation uses the exact classification together with multiplicativity of the integral-subgroup index under symplectic direct products.

Enstad, Thiel, and Vilalta previously gave a sufficient criterion for Schwartz Gabor frames over rational lattices and an upper bound for multiwindow systems. Their paper uses tensor products of noncommutative tori in the structural analysis, but does not state a direct-product activation theorem for Gabor lattices or an exact power law for the minimum number of Schwartz windows.

Gjertsen and Luef study structural equivalences of multivariate Gabor systems and tensor-product frame background. Their full article does not state the symplectic-index product-power criterion above.

Targeted searches for direct-product lattices, tensor powers, symplectic integrality indices, minimum Schwartz-window counts, and regularity activation found no statement equivalent to the present result.

## Limitations

The theorem is an existence statement. It does not construct the activating Schwartz window explicitly.

The activation result assumes symplectic rationality and strict density of the factor lattice. Symplectically irrational lattices are governed by a different branch of the source classification and already admit Schwartz windows at strict density.

The exact first activating power depends on the arithmetic pair
\[
(\nu(\Lambda),\nu(\Lambda^\circ))
\]
and the signal dimension \(d\). No universal bound depending only on covolume is asserted here.

## References

1. A. Caragea and G. Pfander, *Schwartz-Class Gabor Windows and the Balian-Low Classification*, arXiv:2609.06255v2, 2026.
2. U. Enstad, H. Thiel, and E. Vilalta, *Criteria for the Existence of Schwartz Gabor Frames Over Rational Lattices*, International Mathematics Research Notices 2025, no. 5, rnaf038.
3. M. Gjertsen and F. Luef, *On the Structure of Multivariate Gabor Systems and a Result on Gaussian Gabor Frames*, Journal of Fourier Analysis and Applications 30 (2024), Article 73.
