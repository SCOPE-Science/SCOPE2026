# Every indexed Fourier zero of a concentric annulus has exactly one fewer turning point than its index

## Finding

Let \(d\ge2\) be an integer. For every concentric Euclidean annulus with fixed outer radius one and inner radius \(a\in(0,1)\), index the positive radial zeros of its Fourier transform increasingly as \(\tau_k(a)\), for integers \(k\ge1\). **The zero trajectory \(a\mapsto\tau_k(a)\) has exactly \(k-1\) stationary points, all strict local extrema, and no others.** The corresponding inner-scaled frequency \(a\tau_k(a)\) is strictly increasing from zero to the \(k\)-th positive zero of \(J_{d/2-1}\). Thus the first radial null strictly decreases as the central hole grows, the second has exactly one strict maximum, and higher nulls reverse direction increasingly many times.

More precisely, write \(\nu=d/2\), let \(j_{\nu-1,\ell}\) denote the \(\ell\)-th strictly positive zero of the Bessel function \(J_{\nu-1}\), and let
\[
H_\nu(t)=t^\nu J_\nu(t).
\]
The exact \(k-1\) critical inner radii are
\[
a_{k,\ell}=\frac{j_{\nu-1,\ell}}{u_{k,\ell}},\qquad 1\le\ell<k,
\]
where \(u_{k,\ell}\) is the unique solution in \((j_{\nu-1,k},j_{\nu-1,k+1})\) to
\[
H_\nu(u_{k,\ell})=H_\nu(j_{\nu-1,\ell}).
\]
They obey \(0<a_{k,1}<\cdots<a_{k,k-1}<1\). Each critical point is nondegenerate. In the planar case \(d=2\), the second Fourier null has its unique maximum at inner radius approximately \(0.31558546905658\), where its normalized frequency is approximately \(7.62020369595863\); these decimals are numerical approximations, not definitions.

## Assumptions and scope

Use the unnormalized Fourier transform
\[
\widehat{f}(\xi)=\int_{\mathbb R^d}f(x)e^{-i\xi\cdot x}\,dx,
\]
with \(\mathcal A_{d,a}=\{x\in\mathbb R^d:a<\lVert x\rVert<1\}\). Let \(t=\lVert\xi\rVert\) denote radial frequency. The annular Fourier amplitude equals
\[
\widehat{\mathbf1_{\mathcal A_{d,a}}}(\xi)
=(2\pi)^\nu t^{-\nu}\left(J_\nu(t)-a^\nu J_\nu(at)\right)\quad(t>0).
\]
The value at the origin is the positive volume of the annulus. The unique root \(\tau_k(a)\) lies in \((j_{\nu-1,k},j_{\nu-1,k+1})\). Root existence, uniqueness, simplicity, and real-analytic motion were obtained earlier for every \(d\ge2\) in the published annular Fourier-zero interlacing theorem identified in the references. Here they are also reconstructed directly, to make the new turning-point classification independent of numerical experimentation.

## Proof

**1. Bessel energy and zero brackets.** Define
\[
E_\nu(t)=t^{2\nu}\big(J_{\nu-1}(t)^2+J_\nu(t)^2\big).
\]
The standard recurrences \(J_\nu'=J_{\nu-1}-\nu J_\nu/t\) and \(J_{\nu-1}'=(\nu-1)J_{\nu-1}/t-J_\nu\) give
\[
E_\nu'(t)=(4\nu-2)t^{2\nu-1}J_{\nu-1}(t)^2.
\]
Since \(\nu\ge1\), the energy strictly increases for positive \(t\) (integrate the nonnegative derivative, whose zeros are isolated). Furthermore \(H_\nu'(t)=t^\nu J_{\nu-1}(t)\). Thus \(H_\nu\) is strictly monotone between successive zeros of \(J_{\nu-1}\), and its absolute successive extremal values strictly increase. For \(0<a<1\), the equation for a radial Fourier zero is exactly
\[
H_\nu(t)=H_\nu(at).
\]
At \(t=j_{\nu-1,k}\), strict energy increase forces the difference to have the sign of \(H_\nu(j_{\nu-1,k})\), alternating with \(k\). There is therefore at least one root in every interval \((j_{\nu-1,k},j_{\nu-1,k+1})\). At any such root \(t\), strict energy inequality and equality of the \(H_\nu\)-values imply
\[
|J_{\nu-1}(t)|>a^\nu|J_{\nu-1}(at)|.
\]
Consequently
\[
D=J_{\nu-1}(t)-a^{\nu+1}J_{\nu-1}(at)
\]
has the nonzero sign of \(J_{\nu-1}(t)\). Differentiating the Bessel root equation shows the root crosses with that same sign; all roots in a given interval would cross in the same direction, so exactly one exists there. No root occurs before the first \(J_{\nu-1}\) zero by the same sign argument and positivity of the small-frequency amplitude. The implicit function theorem now gives real-analytic \(\tau_k\).

**2. Endpoint limits and strict rescaled motion.** Standard contiguous-order Bessel interlacing and local uniform convergence give
\[
\lim_{a\downarrow0}\tau_k(a)=j_{\nu,k},\qquad
\lim_{a\uparrow1}\tau_k(a)=j_{\nu-1,k}.
\]
Indeed the root equation converges to \(J_\nu(t)=0\) as \(a\downarrow0\); upon division by \(1-a\), it converges on compact positive-frequency intervals to \(tJ_{\nu-1}(t)=0\) as \(a\uparrow1\). Both limit roots are simple, and uniqueness in the Bessel brackets fixes the indexed limits.

Let \(T=\tau_k(a)\), \(s=aT\), and evaluate \(D\) at \(t=T\). Implicit differentiation of \(H_\nu(T)=H_\nu(s)\), using \(H_\nu'(u)=u^\nu J_{\nu-1}(u)\), yields the **exact differential identities**
\[
\frac{dT}{da}=\frac{a^\nu T J_{\nu-1}(s)}{D},
\qquad
\frac{ds}{da}=\frac{T J_{\nu-1}(T)}{D}>0.
\]
The inequality follows because \(D\) and \(J_{\nu-1}(T)\) have the same sign. The strictly increasing function \(s(a)\) starts at zero and ends at \(j_{\nu-1,k}\).

**3. Complete stationary-point census.** The first identity and \(D\ne0\) show
\[
T'(a)=0\quad\Longleftrightarrow\quad
J_{\nu-1}(aT)=0.
\]
Since \(s(a)\) is strictly increasing through precisely the interval \((0,j_{\nu-1,k})\), it crosses each of \(j_{\nu-1,1},\ldots,j_{\nu-1,k-1}\) exactly once. These give exactly \(k-1\) distinct stationary points, ordered as claimed. At such a point \(J_{\nu-1}'(s)\ne0\) by simplicity of Bessel zeros, while \(s'(a)>0\). Hence \(T'\) changes sign at every stationary point, and its derivative there is nonzero: the extrema are strict and nondegenerate. No additional stationary point exists.

**4. Exact critical-radius formulas.** At the critical radius with \(s=j_{\nu-1,\ell}\), equality of the two \(H_\nu\)-values gives \(H_\nu(T)=H_\nu(j_{\nu-1,\ell})\). As \(H_\nu\) is strictly monotone on the \(k\)-th bracket, and the earlier Bessel extremal magnitude is smaller than both endpoint magnitudes of that bracket, this scalar equation has exactly one solution \(u_{k,\ell}\) there. The condition \(aT=j_{\nu-1,\ell}\) gives the advertised ratio. In particular, \(k=1\) has no stationary radii and derivative negative throughout; \(k=2\) has exactly one maximum. This proves the theorem for all integer dimensions at least two and all positive root indices.

## Verification

`checker_all.py` independently locates Bessel brackets and the nonlinear annular Fourier zeros over six dimensions (2, 3, 4, 5, 6, 8), the first eleven indexed roots, and 53 inner radii per root. It checks the root residual, Bessel-bracket membership, strict sign identities, monotonicity of the inner-scaled roots, and all predicted turning-point radii through the tenth index. Its recorded output contains 18,216 successful finite checks and the planar second-null numerical extremizer quoted above. Run `python checker_all.py` with Python 3, NumPy, and SciPy. The unlimited-dimensional and unlimited-index conclusions follow from the preceding analytic proof, not from the finite computation.

## Relationship to prior work

The 2021 photonics study of Khachaturian, Fatemi, Darbinian and Hajimiri discusses Fourier–Bessel diffraction of circular and annular-ring apertures, with circular and thin-ring Bessel profiles. The NIST Digital Library of Mathematical Functions provides classical Bessel recurrences and interlacing for *individual* orders. Most closely, the published result **Rigidity and Bessel interlacing of Fourier zeros of concentric annuli** establishes the all-dimensional zero census, simplicity, and analytic endpoint continuation of each annular zero. Those statements are explicitly treated here as established antecedents, not rediscovered claims. They do **not** classify the critical inner radii or imply a direction of travel from analytic continuation alone. The new content is the strict monotonicity of the inner-scaled branch, its exact derivative identities, the full \(k-1\) stationary-point classification, and the explicit Bessel-level characterization of every stationary radius.

## Limitations

The theorem concerns fixed outer radius, concentric *sharp-edged* uniform annuli, real radial Fourier zeros, and Euclidean dimensions \(d\ge2\). It does not claim the same turning-point count for nonradial masks, arbitrary apodizations, complex-frequency zeros, moving outer boundaries, or dimension one. It does not claim the stationary radii are elementary numbers. The finite checks only corroborate the universal proof. Historical priority beyond the inspected sources remains provisional, including possible unindexed Bessel-root perturbation results.

## References

- A. Khachaturian, R. Fatemi, A. Darbinian and A. Hajimiri, *Discretization of Annular-Ring Diffraction Pattern for Large-Scale Photonics Beamforming*, arXiv:2109.05118v1, public September 10, 2021. The full arXiv HTML was inspected, especially Sections 1–2 and the circular/annular Bessel diffraction models.
- *Rigidity and Bessel interlacing of Fourier zeros of concentric annuli*, published October 25, 2026, identifier `2026/10/25/SCOPE-rigidity-and-bessel-interlacing-of-fourier-zeros-of-concentric-a--08d6dce0baa0`. Full `RESULT.md` inspected, including proof of uniqueness, simplicity and endpoint limits.
- NIST Digital Library of Mathematical Functions, §§10.6, 10.21, especially contiguous-order interlacing in §10.21(i), equation 10.21.2: https://dlmf.nist.gov/10.21.
- G. Urcid and A. Padilla, *Far-field diffraction patterns of circular sectors and related apertures*, Applied Optics 44 (2005), 7677–7696, DOI 10.1364/AO.44.007677 (related annular Fourier–Bessel diffraction formulas; accessible bibliographic and abstract material reviewed).
