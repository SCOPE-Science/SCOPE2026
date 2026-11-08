# Zero-flux mean-capture discontinuity and optimal sink strength in a magnetic quantum square

## Finding

Consider one coherent excitation on the four-cycle \(C_4\), prepared at vertex \(2\), with an irreversible, continuously active single-site sink at the opposite vertex \(0\). Let \(J>0\) be the absolute nearest-neighbour hopping amplitude, \(\kappa>0\) the Lindblad capture rate, and \(\phi\) the total Peierls phase (flux) around the cycle, modulo \(2\pi\). The time \(T\) denotes the random quantum-jump capture time, with \(T=\infty\) if capture never occurs.

The capture probability is \(1\) for all \(\phi\not\equiv\pi\pmod{2\pi}\), but is \(0\) at \(\phi\equiv\pi\pmod{2\pi}\). Whenever \(\phi\not\equiv0,\pi\pmod{2\pi}\), its exact finite mean is

\[
\mathbb E[T]=\frac4\kappa+\frac{\kappa}{4J^2\cos^2(\phi/2)}.
\]

At the exceptional zero-flux point \(\phi\equiv0\pmod{2\pi}\), the mean instead is

\[
\mathbb E[T]=\frac3\kappa+\frac{\kappa}{4J^2}.
\]

Thus the mean has a **finite strict jump** as any nonzero flux is switched on:

\[
\lim_{\phi\to0,\;\phi\ne0}\mathbb E[T]-\mathbb E[T]\big|_{\phi=0}=\frac1\kappa,
\]

although capture remains almost sure. At \(\phi\equiv\pi\), there is no capture, so \(\mathbb E[T]=\infty\). At every other flux, the unique optimal positive sink rate and optimized mean are

\[
\kappa_*(\phi)=
\begin{cases}
2\sqrt3\,J,&\phi\equiv0\pmod{2\pi},\\
4J|\cos(\phi/2)|,&\phi\not\equiv0,\pi\pmod{2\pi},
\end{cases}
\qquad
\inf_{\kappa>0}\mathbb E[T]=
\begin{cases}
\sqrt3/J,&\phi\equiv0\pmod{2\pi},\\
2/(J|\cos(\phi/2)|),&\phi\not\equiv0,\pi\pmod{2\pi}.
\end{cases}
\]

In particular, at fixed \(\kappa\), the mean diverges as \(\kappa/[J^2(\pi-\phi)^2]\) upon approaching half flux, while the optimized mean diverges as \(4/[J|\pi-\phi|]\); the optimal sink rate tends to zero as \(2J|\pi-\phi|\). Here asymptotic equivalence is intended, and flux differences are taken in radians.

## Assumptions and scope

The single-excitation Hilbert space is \(\mathbb C^4\), with site basis \(|0\rangle,\ldots,|3\rangle\). We set \(\hbar=1\) and use the Hermitian Hamiltonian

\[
H_\phi=J\sum_{j=0}^{3}\left(e^{i\phi/4}|j+1\rangle\langle j|+e^{-i\phi/4}|j\rangle\langle j+1|\right),
\]

with indices modulo \(4\). Site energies are equal; there are no additional losses, incoherent hops, dephasing, or interactions. An irreversible Lindblad jump \(L=\sqrt\kappa|\mathrm{vac}\rangle\langle0|\) removes the particle. Initially \(|\psi(0)\rangle=|2\rangle\). The unconditional survival probability is \(S(t)=\|e^{Kt}|2\rangle\|^2\) where \(K=-iH_\phi-(\kappa/2)|0\rangle\langle0|\), and \(\mathbb E[T]=\int_0^\infty S(t)\,dt\), allowing infinite values. These are physical-time absorption statistics for a continuously coupled sink, not the number of projective measurements in a stroboscopic protocol.

## Proof

Choose the representative \(0\le\phi\le2\pi\). In the orthonormal basis \((|e_+\rangle,|o_+\rangle,|e_-\rangle,i|o_-\rangle)\), with \(|e_\pm\rangle=(|0\rangle\pm|2\rangle)/\sqrt2\) and \(|o_\pm\rangle=(|1\rangle\pm|3\rangle)/\sqrt2\), the Hamiltonian is represented by

\[
H=\begin{pmatrix}0&A&0&0\\A&0&0&0\\0&0&0&B\\0&0&B&0\end{pmatrix},\qquad
A=2J\cos(\phi/4),\quad B=2J\sin(\phi/4).
\]

In that same ordered representation the detector and initial state vectors are

\[
w=(1,0,1,0)^\mathsf T/\sqrt2,\qquad
v=(1,0,-1,0)^\mathsf T/\sqrt2.
\]

The phase choice \(i|o_-\rangle\) makes the \(B\)-coupling real. The transformation is unitary; the source and sink have the displayed components. Set \(d=A^2-B^2\), \(s=A^2+B^2\), and \(K=-iH-(\kappa/2)ww^\dagger\).

When \(ABd\ne0\), the eigenvalues of \(H\) are the four distinct numbers \(\pm A,\pm B\). Every eigenvector has nonzero overlap with \(w\); hence no undamped subspace exists and \(e^{Kt}\) decays exponentially. The occupation integral

\[
Y=\int_0^\infty e^{Kt}vv^\dagger e^{K^\dagger t}\,dt
\]

therefore exists and is uniquely determined by the Lyapunov equation \(KY+YK^\dagger=-vv^\dagger\). Direct substitution verifies the following *exact* solution (all entries are expressed in terms of \(A,B,\kappa,d,s\)):

\[
Y=\begin{pmatrix}
\frac1\kappa+\frac{\kappa s}{4d^2}&0&-\frac{\kappa s}{4d^2}&\frac{iB}{d}\\
0&\frac1\kappa+\frac{\kappa A^2}{2d^2}&\frac{iA}{d}&-\frac{\kappa AB}{2d^2}\\
-\frac{\kappa s}{4d^2}&-\frac{iA}{d}&\frac1\kappa+\frac{\kappa s}{4d^2}&0\\
-\frac{iB}{d}&-\frac{\kappa AB}{2d^2}&0&\frac1\kappa+\frac{\kappa B^2}{2d^2}
\end{pmatrix}.
\]

Taking the trace gives \(4/\kappa+\kappa s/d^2\). Since \(s=4J^2\) and \(d=4J^2\cos(\phi/2)\), this is the claimed generic expression.

At zero flux, \(B=0\), the mode \(i|o_-\rangle\) is decoupled from both the initial state and the other three modes. The physical occupation integral is obtained by setting \(B=0\) in the displayed matrix and replacing its last diagonal entry \(1/\kappa\) by zero. This modified matrix satisfies the same Lyapunov equation, is supported on the reachable three-dimensional subspace, and has trace \(3/\kappa+\kappa/A^2=3/\kappa+\kappa/(4J^2)\). At \(\phi=2\pi\), the analogous decoupled mode is \(|o_+\rangle\), giving the same mean. This establishes the one-sided jump, and explains why the generic Lyapunov solution cannot simply be specialized to the exact zero-flux point.

At half flux \(A=B\), the two-dimensional space spanned by \(v\) and \((0,1,0,-1)^\mathsf T/\sqrt2\) is invariant under \(H\) and entirely orthogonal to \(w\). The source lies in this dark space, so the sink amplitude vanishes at every time: \(S(t)=1\) and the capture probability is zero. At every other flux, the preceding spectral argument, or its reachable-subspace version at zero flux, proves capture probability one.

Finally, strict convexity in \(\kappa>0\) of each finite expression follows from its positive \(c/\kappa\) term: the second derivative is \(2c/\kappa^3>0\). Derivative zero yields the unique optimal rate and the displayed optimized means. Taylor expansion of \(\cos(\phi/2)\) around \(\phi=\pi\) proves the two critical asymptotic statements. All conclusions hold for every \(J,\kappa>0\) and every real flux, modulo \(2\pi\).

## Verification

The included `verify.py` uses exact SymPy simplification to establish the full \(4\times4\) Lyapunov matrix certificate, both zero-flux endpoint certificates, the half-flux dark-state identities and the optimizer identities. It independently builds the original complex Peierls Hamiltonian in the physical site basis and checks the mean against a numerical Lyapunov solver for 11 flux values and four sink rates, with 88 numerical comparison/residual assertions. Run `python verify.py` with SymPy, NumPy and SciPy installed. These computations replay finite-dimensional algebra; the analytic reachability and optimization arguments above prove the infinite-time statements.

## Relationship to prior work

L. Jin (2016, arXiv:1611.10015) establishes magnetic-flux-induced transmission zeros in an open two-arm resonator interferometer, including destructive interference at half a flux quantum. That is scattering into output leads, not an exponentially absorbing single-site sink with a jump-time expectation. Le et al. (2017, arXiv:1707.07482) analyze dark subspaces and Lindblad sinks in quantum networks; their general framework motivates the absorption question but does not supply the complete square-ring flux-dependent mean, the finite zero-flux jump, or its sink-rate optimizer. Friedman, Kessler and Barkai (2016, arXiv:1611.05676) and Liu et al. (2020, arXiv:2001.00231) study repeated projective first detection on rings and at degeneracies, with a different measurement protocol and observable. Holzinger et al. (2023, arXiv:2309.11376) investigate ring-emitter trapping and transfer in long-range radiative networks, without the present Peierls-flux and single opposite-site capture-time classification.

The new claim is specifically the exact trichotomy for continuous absorption in this minimal magnetic ring and the discontinuity and optimized singular scaling. It does not claim the underlying Peierls model, sink formalism, interference mechanism, or the general existence of dark states as new.

## Limitations

The result assumes exact equal arms, uniform Hermitian nearest-neighbour hoppings, an initially localized opposite-site excitation, and no other loss or decoherence. Static disorder, dephasing, additional traps, other initial states and general even rings are not covered. Its priority relative to unpublished work or implicitly equivalent specialized formulas is not established by the finite literature search; independent review is outstanding. The zero-flux jump concerns an infinite-time mean and is not a discontinuity of finite-time survival probability.

## References

- H. Friedman, D. A. Kessler, E. Barkai, *Quantum walks: the first detected passage time problem* (first public preprint 2016-11-17), https://arxiv.org/abs/1611.05676.
- L. Jin, *Quantum transport in coupled resonators enclosed synthetic magnetic flux* (first public preprint 2016-11-30), https://arxiv.org/abs/1611.10015.
- T. P. Le, L. Donati, S. Severini, F. Caruso, *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures* (first public preprint 2017-07-24), https://arxiv.org/abs/1707.07482.
- Q. Liu, R. Yin, K. Ziegler, E. Barkai, *Quantum walks: the first detected transition time* (first public preprint 2020-01-01), https://arxiv.org/abs/2001.00231.
- R. Holzinger, J. S. Peter, S. Ostermann, H. Ritsch, S. F. Yelin, *Harnessing quantum emitter rings for efficient energy transport and trapping* (first public preprint 2023-09-20), https://arxiv.org/abs/2309.11376.
