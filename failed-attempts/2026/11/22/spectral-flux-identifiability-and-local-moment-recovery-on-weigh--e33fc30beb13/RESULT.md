# Spectral flux identifiability and local-moment recovery on weighted triangular quantum networks

## Finding

A discrete magnetic quantum network can lose the ability to distinguish its individual plaquette fluxes solely because two or more triangle bonds have the same hopping magnitude. Exact bond-strength splitting restores that information in the *global energy spectrum*, while one local third spectral moment at each petal resolves it even in the equal-strength case.

**Theorem.** For every integer \(m\ge2\), define the single-excitation Hamiltonian \(H\) on \(2m+1\) vertices as in the next section. Let \(\tau_1,\ldots,\tau_g\) be the distinct positive internal-edge strengths, let \(J_r=\{j:t_j=\tau_r\}\), let \(n_r=|J_r|\), and put \(C_r=\sum_{j\in J_r}\cos\phi_j\). Then the monic characteristic polynomial \(P(z)=\det(zI-H)\) is

\[
P(z)=\prod_{r=1}^{g}(z^2-\tau_r^2)^{n_r-1}\,Q(z),
\]
\[
Q(z)=z\prod_{r=1}^{g}(z^2-\tau_r^2)-\sum_{r=1}^{g}(2n_rz+2\tau_r C_r)\prod_{s\ne r}(z^2-\tau_s^2).
\]

For fixed known strengths, \(P\) determines every \(C_r\) by the explicit formula

\[
\boxed{C_r=-n_r-\frac{Q(\tau_r)}{2\tau_r\prod_{s\ne r}(\tau_r^2-\tau_s^2)}.}
\]

Consequently two phase assignments are isospectral **if and only if** each equal-strength class has the same sum of flux cosines. In particular, distinct bond strengths make every \(\cos\phi_j\) identifiable from the full global spectrum. For *all* strengths, every individual cosine is recoverable from one site-resolved third spectral moment:

\[
\boxed{\langle a_j,H^3a_j\rangle=\langle b_j,H^3b_j\rangle=2t_j\cos\phi_j.}
\]

The sign of each flux angle is not claimed to be spectrally identifiable: reversing one triangle's vertex labels changes its flux orientation but not its cosine.

## Assumptions and scope

The vertex set is \(\{o,a_1,b_1,\ldots,a_m,b_m\}\). With the standard orthonormal site basis, the only nonzero matrix entries are

\[
H_{o,a_j}=H_{a_j,o}=H_{o,b_j}=H_{b_j,o}=1,\qquad
H_{a_j,b_j}=t_je^{i\phi_j},\quad H_{b_j,a_j}=t_je^{-i\phi_j}.
\]

Here \(t_j>0\) is a **known**, real bond magnitude and \(\phi_j\in\mathbb R\) is a gauge-invariant signed flux angle modulo \(2\pi\), in a gauge where the two hub bonds on each triangle are real and positive. No onsite potentials, interpetal links or multiple excitations are included. Spectra are multisets including multiplicities. The weights and their assignment to triangle sites are known when interpreting the inverse result. The local moment uses a labelled peripheral site, so it assumes site-resolved measurements rather than only global eigenvalues.

## Proof

**1. Exact forward characteristic polynomial.** Order the hub first and the two peripheral sites in each petal next. Write the peripheral block as \(B=\bigoplus_j B_j\), where

\[
B_j=\begin{pmatrix}0&t_je^{i\phi_j}\\t_je^{-i\phi_j}&0\end{pmatrix},\quad
\det(zI_2-B_j)=z^2-t_j^2.
\]

The hub-to-periphery row is the concatenation of \((1,1)\) on every petal. For \(z\ne\pm t_j\), the Schur complement gives

\[
\begin{aligned}
P(z)&=\prod_{j=1}^{m}(z^2-t_j^2)\\
&\quad\times\left[z-\sum_{j=1}^{m}\frac{2z+2t_j\cos\phi_j}{z^2-t_j^2}\right].
\end{aligned}
\]

Both sides are polynomials after cancellation, so the identity extends to **all** complex \(z\). Group the terms having \(t_j=\tau_r\) and cancel the common multiplicities. This yields the stated factorization, with \(Q\) monic of degree \(2g+1\) and \(\prod_r(z^2-\tau_r^2)^{n_r-1}\) of degree \(2m-2g\); hence the total degree is exactly \(2m+1\).

**2. Invertibility by separated spectral evaluation.** For each \(r\), evaluate the polynomial \(Q\) at \(z=\tau_r>0\). All summands except the \(r\)-th contain a vanishing factor. Thus

\[
Q(\tau_r)=-2\tau_r(n_r+C_r)\prod_{s\ne r}(\tau_r^2-\tau_s^2).
\]

Distinctness and positivity of the \(\tau_r\) ensure that every factor in the denominator is nonzero. The displayed recovery formula follows without taking limits at a pole. For fixed strengths, the forward factorization depends on phases only via the \(C_r\), while the inversion shows those sums are unique. This proves the if-and-only-if classification even when \(n_r+C_r=0\) or spectral levels \(\pm\tau_r\) have higher multiplicity than their displayed base powers. No genericity assumption on the phases is used.

**3. Local observability.** The diagonal matrix element \((H^3)_{a_j,a_j}\) is the sum of length-three closed quantum-walk amplitudes from \(a_j\). Because the triangles share only the hub, the only length-three closed paths from \(a_j\) are \(a_j\to o\to b_j\to a_j\) and \(a_j\to b_j\to o\to a_j\). Their amplitudes sum to \(t_je^{i\phi_j}+t_je^{-i\phi_j}=2t_j\cos\phi_j\). The same argument holds for \(b_j\). Thus local moments identify each cosine regardless of equal-strength degeneracy.

**4. Genuine global spectral ambiguity at repeated strengths.** Take two petals with \(t_1=t_2=1\). Assign phase gains \((3+4i)/5\) and \((-3+4i)/5\); alternatively assign \(i\) and \(-i\). Both have \(C_1=0\), so they have precisely the same characteristic polynomial

\[
P(z)=z(z^2-1)(z^2-5).
\]

Yet the first petal's local third moment is respectively \(6/5\) and \(0\). These phase sets are not related by separate orientation reversals or permutations, because their multisets of flux cosines differ. If the strengths are changed to \((1,2)\), the recovery formula separates the two individual cosines and the two displayed assignments cease to be isospectral. Repeating this construction within any larger equal-strength group creates continuous isospectral families whenever the fixed cosine sum admits an interior perturbation.

## Verification

`verify_exact.py` builds \(H\) independently and compares its exact symbolic characteristic polynomial to the factored formula, recovers all class sums by polynomial division and evaluation, and checks each diagonal third moment. It covers six nontrivial rational-phase cases with two to four petals and includes the explicit isospectral, locally distinguishable pair, and the contrasting distinct-weight test. Every assertion passed.

`verify_numerical.py` independently implements a dense complex Hermitian matrix and tests 30 seeded random assignments for every size \(m=2,\ldots,9\), comparing determinant products at four nonreal/real test energies, recovering class sums from the eigenspectrum and checking the third moments. All 240 assignments passed. These finite tests corroborate, but do not replace, the all-size Schur-complement proof.

Run from this directory with `python verify_exact.py` and `python verify_numerical.py`. Requirements: Python 3, SymPy, NumPy. No other files are needed.

## Relationship to prior work

Reff's 2011 gain-graph analysis formalizes Hermitian unit-modulus magnetic edge gains and switching equivalence [1]. Cioabă, Haemers, Vermette and Wong's 2013 classification gives the ordinary unweighted friendship-graph spectrum, without flux-dependent couplings or inverse reconstruction [2]. Cavaleri and Donno's cospectrality theorem characterizes gain-graph spectra abstractly through character-weighted closed walks [3]; it does not state the sharp **equal-strength class** identifiability criterion, the finite spectral evaluation inverse, or the local-moment repair in this weighted model. Earlier tight-binding triangular-bouquet transport results concern common fluxes and scattering rather than independently unknown plaquette fluxes with heterogeneous known bond strengths. The present claim is confined to the specific family and data regime above; general closed-walk and Schur-complement methods are acknowledged rather than claimed as new.

## Limitations

A global spectrum gives cosines but not oriented signs, and fails to separate individual cosines on equal-strength classes. Local moment recovery requires petal-specific site resolution. All hub bonds are fixed at one, onsite energies vanish, and the network is a one-vertex bouquet of triangles. Known positive peripheral strengths are essential to the inverse formula; unknown weights, disorder on hub bonds, decoherence, open leads, and higher-excitation interacting dynamics are not addressed. The result is a self-contained exact finite-network family theorem, not a general inverse theorem for all quantum graphs. Independent external audit and an exhaustive worldwide priority determination have not been performed.

## References

[1] Nathan Reff, *Spectral Properties of Complex Unit Gain Graphs*, first public preprint 20 October 2011, arXiv:1110.4554, https://arxiv.org/abs/1110.4554 (definitions and switching, and adjacency spectral bounds).

[2] Sebastian M. Cioabă, Willem H. Haemers, Jason Vermette and Wiseley Wong, *The graphs with all but two eigenvalues equal to \(\pm1\)*, first public preprint 24 October 2013, arXiv:1310.6529, https://arxiv.org/abs/1310.6529 (the unweighted friendship adjacency spectrum).

[3] Angelot L. Cavaleri and Alfredo Donno, *On cospectrality of gain graphs*, 2022, DOI:10.1515/spma-2022-0169, https://doi.org/10.1515/spma-2022-0169 (especially Theorem 4.12 on character-weighted closed walks).
