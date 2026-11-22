# Density-reversing sixth-order directional growth in a six-polarity active lattice gas

## Finding

In the six-polarity active lattice-gas hydrodynamics of Bhowmick and Mohanty [1], the density eigenmode near zero spatial wave number is isotropic through fourth order, but its first allowed sixfold angular harmonic has an **exact, density-dependent and sign-reversing coefficient**. For each \(0<r<1\) and \(p>0\), where \(r\) is uniform total occupancy and \(p=\mathrm{Pe}\), one has

\[
s(k,\theta)=a_2k^2+a_4k^4+\bigl(a_6+b_6\cos(6\theta)\bigr)k^6+O(k^8),
\qquad b_6=\frac{p^6(1-r)^5(2r-1)}{1152}.
\]

Here \(a_4\) and \(a_6\) are real angle-independent functions of \(r,p\), and
\[
a_2=-1-\frac{p^2}{2}(1-r)(1-2r).
\]

In particular, with \(\theta=0\) aligned with a microscopic propulsion heading and \(\theta=\pi/6\) halfway between adjacent headings,
\[
s(k,0)-s(k,\pi/6)=\frac{p^6(1-r)^5(2r-1)}{576}k^6+O(k^8).
\]
The small-wave-number directional preference is toward headings if \(r>1/2\) and toward bisectors if \(r<1/2\). At exactly half filling the cancellation is stronger: \(s(k,\theta)=-k^2\) holds **exactly**, not merely through order six, for the eigenvalue carried by the uniform-orientation vector at every wavevector.

## Assumptions and scope

Let \(n\in\mathbb Z/6\mathbb Z\), \(e_n=(\cos(n\pi/3),\sin(n\pi/3))\), and let \(\rho=\sum_n\rho^n\). Take the dimensionless deterministic six-component PDE [1, Eq. (3)] exactly as stated:
\[
\partial_t\rho^n=(1-\rho)\Delta\rho^n+\rho^n\Delta\rho
-p\, e_n\cdot\nabla\bigl[(1-\rho)\rho^n\bigr]
+\rho^{n-1}+\rho^{n+1}-2\rho^n.
\]
The theorem is for its linearization at \(\rho^n=r/6\), for every fixed \(r\in(0,1)\) and \(p>0\). Let \(k\ge0\) be the magnitude of a spatial Fourier wavevector and \(\theta\in\mathbb R\) its angle relative to \(e_0\). The notation \(s(k,\theta)\) specifies the branch whose eigenvalue at \(k=0\) is zero; this branch is real and analytic for sufficiently small real \(k\). The remainder is uniform over \(\theta\) for fixed \(r,p\). The theorem makes no assertion that this branch dominates every finite wave number or that its directional sign selects the ultimate nonlinear morphology. It is not a theorem about finite-size microscopic particle trajectories.

## Proof

**Linearized symbol.** Write \(I\) for the six-dimensional identity, \(J=\mathbf1\mathbf1^{\mathsf T}/6\), \(E_\theta=\mathrm{diag}(\cos(\theta-n\pi/3))\), and \(L=S+S^{-1}-2I\), where \(S\) cyclically shifts the heading index. Substituting \(\rho^n=r/6+\delta\rho^n e^{st+ik(x\cos\theta+y\sin\theta)}\) gives exactly
\[
M(k,\theta)=L-ikpE_\theta\bigl[(1-r)I-rJ\bigr]-k^2\bigl[(1-r)I+rJ\bigr].
\]
The eigenvalues of \(L\) on angular characters indexed by \(m=0,1,2,3,4,5\) are \(-\Gamma_m\), where \((\Gamma_0,\ldots,\Gamma_5)=(0,1,3,4,3,1)\). Hence zero is simple and separated from all other eigenvalues; analytic perturbation theory applies. Inverting the six headings, \(n\mapsto n+3\), maps \(k\) to \(-k\). The density branch is therefore even in \(k\) and real for all sufficiently small real \(k\).

**Angular selection rule and coefficient.** In the angular character basis, the first-order perturbation \(-ipE_\theta[(1-r)I-rJ]\) changes the angular index by \(+1\) or \(-1\), with respective phases \(e^{\pm i\theta}\), while the second-order perturbation preserves the angular index. For a path leaving and returning to the uniform mode, an angular phase survives only if the sum of its index increments is a nonzero multiple of six. Thus no angular dependence occurs below order \(k^6\). At degree six, exactly two contributions can carry the phases \(e^{\pm6i\theta}\): the monotone winding paths
\[
0\to1\to2\to3\to4\to5\to0,
\qquad0\to5\to4\to3\to2\to1\to0.
\]
Other perturbation words have fewer than six index shifts or zero net winding and are angle-independent. Corrections from the spectral parameter in resolvents likewise have fewer shifts at this order. On the first shift out of the uniform mode, the transport vertex has factor \((1-2r)\); every subsequent shift has factor \((1-r)\). Each shift also contributes \(-ip/2\), and the five intermediate resolvent gaps have product
\[
\Gamma_1\Gamma_2\Gamma_3\Gamma_4\Gamma_5=1\cdot3\cdot4\cdot3\cdot1=36.
\]
Summing the two windings gives
\[
\frac{(-ip/2)^6(1-2r)(1-r)^5}{36}
\bigl(e^{6i\theta}+e^{-6i\theta}\bigr)
=\frac{p^6(2r-1)(1-r)^5}{1152}\cos(6\theta).
\]
The first nonzero isotropic term follows from the \(-k^2\) diffusion operator and two-step uniform-to-polarization-to-uniform paths, giving \(a_2=-1-p^2(1-r)(1-2r)/2\).

**Exact half-filling cancellation.** At \(r=1/2\), the first-order term annihilates \(\mathbf1\), since \([(1-r)I-rJ]\mathbf1=(1-2r)\mathbf1=0\). The second-order term has \([(1-r)I+rJ]\mathbf1=\mathbf1\), while \(L\mathbf1=0\). Therefore \(M(k,\theta)\mathbf1=-k^2\mathbf1\) identically. Near \(k=0\), this is the analytically continued density eigenvalue. The proof is complete.

## Verification

The standalone `verify.py` reconstructs the full six-by-six Fourier symbol, checks the two-winding denominator and sign, compares the exact sixth-order prediction with independently computed high-precision eigenvalues along headings and bisectors for four parameter pairs and two small wave numbers, and verifies the exact uniform eigenvector identity at half filling. At the two wave numbers in the check, the relative sixth-order coefficient error decreases as the wave number is halved. The computations corroborate the proof but are not a substitute for the analytic infinite-wave-number-limit argument.

Run `python verify.py`; the checker uses the public Python package `mpmath` and emits measured relative errors.

## Relationship to prior work

Bhowmick and Mohanty [1] give the underlying six-polarity continuum equation and derive its isotropic fourth-gradient-order active-model-B+ reduction, emphasizing why sixfold symmetry first permits a lattice-isotropic fourth-order closure. Those are established inputs, not new contributions here. Their supplemental calculation [2] details the fourth-gradient-order elimination and identifies the higher third-angular-harmonic contribution without presenting a coefficient for the sixth-order angular dependence of the exact small-wave-number density eigenvalue. The result above computes this otherwise missing sixth-order angular term by full time-dependent spectral perturbation, including its sign reversal at half occupancy and the exact cancellation at that density. The slow spectral branch is deliberately distinguished from adiabatic coefficient truncations.

Loewe and Shendruk [3] study anisotropy of turn dynamics in a different four-direction right-angle setting. Their non-isotropy analysis does not imply the occupancy-dependent six-direction coefficient or the exact half-filling identity here. General point-group principles permit a sixth angular harmonic but do not fix its sign and coefficient in this coupled nonlinear mobility model. Comparisons against accessible public mathematical finding summaries did not reveal a statement covering this exact result; this is a scoped best-knowledge comparison, not a proof of priority.

## Limitations

The result establishes a local-in-wave-number linear spectral expansion at each fixed \(r,p\). It does not bound the remainder uniformly in extreme \(p\) or near occupancy endpoints; it does not establish nonlinear pattern selection, finite-wave-number global optimization, or a microscopic fluctuation theorem. The sixth-order signal is small relative to lower-order isotropic growth and may require high-resolution measurements. Broader or unindexed earlier calculations of the same six-component symbol could alter the novelty assessment; independent audit has not been performed.

## References

[1] A. Bhowmick and P. K. Mohanty, *Active model B+ from run-and-tumble particles on a triangular lattice*, arXiv:2611.08296v1 (first public 2026-11-05). https://arxiv.org/html/2611.08296v1

[2] A. Bhowmick and P. K. Mohanty, accompanying supplemental material, `triRTP_supp_arXiv.pdf`, linked from https://arxiv.org/abs/2611.08296.

[3] B. Loewe and T. N. Shendruk, *Anisotropic run-and-tumble-turn dynamics*, arXiv:2305.03663v1 (2023); Soft Matter (2024), DOI: 10.1039/D3SM00589E. https://arxiv.org/html/2305.03663v1
