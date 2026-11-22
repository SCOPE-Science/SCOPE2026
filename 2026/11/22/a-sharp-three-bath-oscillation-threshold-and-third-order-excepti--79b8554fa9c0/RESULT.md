# A sharp three-bath oscillation threshold and third-order exceptional modes in Glauber rings

## Finding

A ferromagnetically coupled kinetic Ising ring with the repeating three-bath parameters \((g,g,-h)\), where \(0<g,h<1\), has a sharp, nonzero frustration threshold for nonreal one-spin relaxation modes. Put \(u=h/g\). On every ring of length \(3m\) with \(m\ge2\), **all eigenvalues on the linear spin-observable invariant subspace are real for \(0<u<1/8\)**. At \(u=1/8\) the zero-wavenumber Bloch block acquires a nontrivial order-two Jordan block. For \(u>1/8\), its spectrum contains nonreal conjugate eigenvalues and the homogeneous three-sublattice magnetization responds with damped oscillations for suitable initial conditions. In the mixed region \(1/8<u<1/2\), different Bloch wavenumbers may still have either three real or one real and a complex-conjugate pair of eigenvalues. For \(u>1/2\), every Bloch wavenumber has one real and two nonreal eigenvalues.

The exact discriminant of the three-component Bloch eigenproblem is

\[
\mathcal D(k)=\frac{g^6}{16}\left[(1-2u)^3-27u^2\cos^2 k\right],\qquad k=\frac{2\pi j}{m},\quad j=0,\ldots,m-1.
\]

The two-real/complex transition at each wavenumber occurs at \(\mathcal D(k)=0\). Inside the mixed region, its nonreal pair occurs precisely when

\[
|\cos k|>\frac{(1-2u)^{3/2}}{3\sqrt3\,u}.
\]

At the special second threshold \(u=1/2\), if \(4\mid m\), the modes \(k=\pi/2\) and \(k=3\pi/2\) possess an **order-three exceptional point** (one size-three Jordan block) at relaxation eigenvalue \(-1\). Consequently, observables in these invariant Fourier sectors can exhibit a nonzero \(t^2e^{-t}\) term. The order-three degeneracy is absent from finite rings whose Fourier mesh omits these wavenumbers.

For initial mean spins equal to one on the two positive-bath sublattices and zero on the negative-bath sublattice, write their subsequent means as \(a(t)\) and \(b(t)\). For \(u>1/8\) their dynamics is explicitly

\[
\begin{aligned}
a(t)&=e^{(-1+g/4)t}\left(\cos(\omega t)+\frac{g}{4\omega}\sin(\omega t)\right),\\
b(t)&=-\frac{h}{\omega}e^{(-1+g/4)t}\sin(\omega t),\\
\omega&=\frac14\sqrt{g(8h-g)}.
\end{aligned}
\]

Thus the oscillation frequency turns on as the square root of the excess antagonist strength \(h-g/8\), in contrast to alternating two-bath rings in which opposite signs suffice for oscillatory magnetization relaxation.

## Assumptions and scope

Take \(n=3m\), \(m\ge2\), and spin configurations \(\sigma\in\{-1,+1\}^{n}\) on a periodic nearest-neighbor ring. The continuous-time Markov generator is defined by the spin-flip rates

\[
w_i(\sigma)=\frac12\left[1-\frac{\gamma_i}{2}\sigma_i(\sigma_{i-1}+\sigma_{i+1})\right],\quad
(\gamma_{3r},\gamma_{3r+1},\gamma_{3r+2})=(g,g,-h).
\]

Indices are modulo \(n\). Assume \(0<g,h<1\), so all flip rates are strictly positive, and the finite chain is irreducible. A positive bath coefficient corresponds to a positive temperature for a ferromagnetic coupling, and a negative coefficient to the conventional negative-temperature extension of this bounded-energy spin model. We make no thermodynamic claim about realizing such reservoirs. One-spin observables form an invariant subspace of the full Markov generator; **all spectral claims below are confined to this subspace**, not the entire \(2^n\)-state generator. The word exceptional point means a nondiagonalizable eigenvalue of the complexified one-spin generator.

## Proof

**Step 1: exact closure.** A spin flip at site \(i\) changes \(\sigma_i\) by \(-2\sigma_i\) and leaves other spin coordinates unchanged. Direct generator application gives

\[
L\sigma_i=-\sigma_i+\frac{\gamma_i}{2}(\sigma_{i-1}+\sigma_{i+1}).
\]

Hence all mean magnetizations \(M_i(t)=\mathbb E\sigma_i(t)\) obey a finite, exact, linear system with no higher-moment closure assumption. Group the three sites in cell \(r\) into \(v_r=(M_{3r},M_{3r+1},M_{3r+2})^\mathsf T\). On a Bloch mode \(v_r=z^rv\), \(z=e^{ik}\), \(k=2\pi j/m\), the generator acts by \(-I+B(z)\), where

\[
B(z)=\begin{pmatrix}
0&g/2&g/(2z)\\
g/2&0&g/2\\
-hz/2&-h/2&0
\end{pmatrix}.
\]

**Step 2: characteristic equation and discriminant.** A direct determinant expansion yields

\[
\det(\mu I-B(z))=\mu^3-\frac{g(g-2h)}4\mu+\frac{g^2h}{8}(z+z^{-1})
=\mu^3-\frac{g^2(1-2u)}4\mu+\frac{g^3u}4\cos k.
\]

For a real-coefficient depressed cubic \(x^3+px+q\), the discriminant \(-4p^3-27q^2\) has sign positive for three distinct real roots, zero for repeated roots, and negative for one real root and a nonreal conjugate pair. Substitution gives the asserted \(\mathcal D(k)\). The identity

\[
(1-2u)^3-27u^2=(1+u)^2(1-8u)
\]

implies that \(\mathcal D(k)>0\) for all \(k\) if \(0<u<1/8\); at \(u=1/8\), only \(\cos k=\pm1\) gives equality. For \(1/8<u<1/2\), solve \(\mathcal D(k)<0\) to obtain exactly the stated momentum cutoff; the cutoff lies strictly between zero and one. At \(u=1/2\), the discriminant vanishes only for \(\cos k=0\). For \(u>1/2\) the first term is negative and the second nonpositive, so the discriminant is strictly negative everywhere.

**Step 3: the order-two exceptional threshold.** At \(u=1/8\) and \(k=0\), the characteristic cubic factors as

\[
(\mu-g/4)^2(\mu+g/2).
\]

At \(k=\pi\), when present in the finite ring, it factors as \((\mu+g/4)^2(\mu-g/2)\). The leading principal two-by-two minor of \(\mu I-B\) equals \(\mu^2-g^2/4\); at \(\mu=\pm g/4\) it is nonzero. Therefore the repeated eigenvalue has a one-dimensional eigenspace and a size-two Jordan block. Since \(k=0\) always belongs to the Fourier mesh, this spectral transition is sharp on every admissible ring.

**Step 4: order-three exceptional modes.** Let \(u=1/2\) and \(z=i\), equivalently \(k=\pi/2\). The cubic reduces to \(\mu^3\). Direct matrix multiplication gives \(B(i)^3=0\), \(B(i)^2\ne0\), and \(\operatorname{rank}B(i)=2\). Thus the full three-dimensional Bloch block has precisely one nilpotent Jordan block of length three, and \(e^{(-I+B(i))t}=e^{-t}(I+tB(i)+t^2B(i)^2/2)\). The conjugate mode \(z=-i\) behaves identically. These modes belong to the finite Fourier mesh if and only if \(4\mid m\).

**Step 5: directly observable oscillation and its onset.** For initial spin means constant on each cell and equal on the two positive-bath classes, the symmetry is maintained. Setting these means to \(a(t)\), and the negative-bath-class mean to \(b(t)\), exact closure reads

\[
\binom{a'}{b'}=\begin{pmatrix}-1+g/2&g/2\\-h&-1\end{pmatrix}\binom a b.
\]

The two eigenvalues are \(-1+g/4\pm\frac14\sqrt{g(g-8h)}\). Exponentiate this matrix at initial condition \((a(0),b(0))=(1,0)\) to obtain the displayed formula when \(8h>g\), with \(\omega=\sqrt{g(8h-g)}/4\). At \(h=g/8\) one takes the continuous \(\omega\downarrow0\) limit, producing a nonzero \(te^{(-1+g/4)t}\) term. These initial means are realized by taking all first and second sublattice spins \(+1\) and unbiased independent third-sublattice spins. Thus the nonreal eigenvalues reflect an actual admissible spin expectation trajectory, not merely formal spectral roots. Equivalently, \(\omega=(\sqrt{8g}/4)\sqrt{h-g/8}\).

## Verification

The standalone script `verify.py`, using Python, SymPy and NumPy, performs: exact symbolic characteristic/discriminant/exceptional-point checks; 5,016 exact-rational state-by-state applications of the physical spin-flip generator on three finite rings; and 15 comparisons of full one-spin ring spectra against the Bloch-block spectra. Successful replay prints `THREE_BATH_GLAUBER_CHECKS_PASSED symbolic=10 exact_generator=5016 finite_spectra=15`. The finite checks support but do not replace the determinant, discriminant, and Jordan proofs, which hold for all stated continuous parameters and ring lengths.

## Relationship to prior work

Mobilia, Zia, and Schmittmann's 2004 two-temperature kinetic Ising solution derives the same closed magnetization-generator form, and identifies oscillatory relaxation for alternating positive/negative temperature baths. Their focus is two alternating sublattices; the present three-bath \((g,g,-h)\) periodicity produces a nonzero \(h/g=1/8\) onset and momentum-selective cubic degeneracies that are not implied by their two-by-two Bloch problem. Their longer 2004/2005 reaction–diffusion treatment explicitly retains the two-sublattice alternation and maps negative temperatures to competing creation/annihilation rates. Schmittmann and Schmüser's 2002 stationary-correlation analysis likewise treats two alternating baths and does not determine this three-sublattice relaxation spectrum.

The previously indexed period-three Glauber finding on failure of stationary four-spin factorization studies the \((\delta,a,b)\) positive-temperature regime and a stationary connected-moment defect. Its claim does not supply the spectral discriminant, the negative-bath threshold, or the order-three exceptional modes. Nor does the present statement imply that stationary factorization result. The original magnetization closure is a known general method; the claimed contribution is the exact phase diagram and exceptional-mode hierarchy in this natural periodically frustrated specialization.

## Limitations

The theorem concerns the one-spin invariant subspace, not the full spectrum or stationary multispin correlation hierarchy. The result requires the displayed three-periodic bath pattern, strictly positive \(g,h\) below one, and finite rings of length divisible by three; ring-length divisibility by twelve is necessary for the order-three exceptional modes. The mixed-regime momentum mesh is discrete, not a continuum for each finite ring. Oscillatory modes do not imply every initial condition has an oscillatory observable. The result does not establish exhaustive publication priority; more general periodic transfer-matrix or Markov-mode treatments may already imply parts of this classification.

## References

1. M. Mobilia, R. K. P. Zia, and B. Schmittmann, *Complete Solution of the Kinetics in a Far-from-equilibrium Ising Chain*, arXiv:cond-mat/0405375, first posted 2004-05-17, https://arxiv.org/abs/cond-mat/0405375.
2. M. Mobilia, B. Schmittmann, and R. K. P. Zia, *Exact dynamics of a reaction-diffusion model with spatially alternating rates*, arXiv:cond-mat/0412576, first posted 2004-12-21, https://arxiv.org/abs/cond-mat/0412576.
3. B. Schmittmann and F. Schmüser, *Stationary correlations for a far-from-equilibrium spin chain*, arXiv:cond-mat/0212616, first posted 2002-12-27, https://arxiv.org/abs/cond-mat/0212616.
4. *A four-spin obstruction to two-point factorization in a periodic three-temperature Glauber chain*, archived research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-four-spin-obstruction-to-two-point-factorization-in-a-periodic--40ac4bb02a8c.
