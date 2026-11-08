# Exact collision protection of two bosons on nonbinary Hamming networks

## Finding

Let \(d\ge 1\) and \(q\ge 3\) be integers. On the Hamming graph \(H(d,q)=K_q^{\square d}\), two identical, noninteracting bosons hop with a uniform nonzero real amplitude \(J\), and an irreversible loss channel of arbitrary positive strength acts on every doubly occupied vertex. Write \(N=q^d\). The maximal permanently loss-free subspace \(\mathcal D\) in the symmetric two-particle Hilbert space has **exact** dimension

\[
\boxed{\dim\mathcal D=\frac{N(N+1)}2-q^{d-1}\bigl((d+1)q+d\bigr)+d.}
\]

For a normalized localized pair at distinct vertices a Hamming distance \(s\in\{1,\ldots,d\}\) apart, the ultimate collision-loss probability \(\eta_{d,q}(s)\) is the following exact rational finite sum. Define the coefficient notation \(g_{w,t}=[T^t]G_w(T)\) and \(f_{b,r,t}=[T^t]F_{b,r}^{(d,s)}(T)\), where

\[
G_w(T)=\bigl(1+(q-1)T^2\bigr)^{d-w}\bigl(2T+(q-2)T^2\bigr)^w,
\]
\[
F_{b,r}^{(d,s)}(T)=\bigl(1+(q-1)T^2\bigr)^{d-s-b}
\bigl(2T+(q-2)T^2\bigr)^b
(1-T^2)^{s-r}(T-T^2)^r.
\]

Then, with all terms having \(g_{b+r,t}=0\) omitted,

\[
\boxed{\eta_{d,q}(s)=\frac{2}{q^{2d}}
\sum_{b=0}^{d-s}\sum_{r=0}^{s}
\binom{d-s}{b}\binom sr(q-1)^b\bigl(2(q-2)\bigr)^r
\sum_{\substack{0\le t\le2d\\g_{b+r,t}>0}}
\frac{f_{b,r,t}^{\,2}}{g_{b+r,t}}.}
\]

For arbitrary initial two-boson density matrix \(\rho\), ultimate collision-loss probability is \(1-\operatorname{Tr}(P_{\mathcal D}\rho)\), where \(P_{\mathcal D}\) is the orthogonal projector onto the subspace characterized in the proof. An initially doubly occupied state is captured with probability one. All these statements are independent of the values of the strictly positive individual loss rates.

For the two-dimensional nonbinary Hamming graph \(H(2,q)=K_q\square K_q\), the distance-resolved law simplifies to

\[
\eta_{2,q}(1)=\frac{q^2+2q-2}{q^2(q-1)},\qquad
\eta_{2,q}(2)=\frac{2}{(q-1)^2}.
\]

For example, \(H(2,3)\) has a fourteen-dimensional protected space with capture probabilities \(13/18\) and \(1/2\), while \(H(2,4)\) has an eighty-two-dimensional protected space with capture probabilities \(11/24\) and \(2/9\) for separations one and two, respectively. These are finite-network responses, not thermodynamic phase transitions.

## Assumptions and scope

Vertices are tuples \(x\in(\mathbb Z/q\mathbb Z)^d\); an edge joins two tuples differing in exactly one coordinate. Although this additive notation is convenient, no prime-power restriction on \(q\) is imposed. Let \(A\) be the ordinary adjacency matrix and \(\mathcal H_+=\operatorname{Sym}^2(\mathbb C^N)\). The loss-free Hamiltonian and effective loss generator on \(\mathcal H_+\) are

\[
H=J(A\otimes I+I\otimes A)|_{\mathcal H_+},\qquad
K=H-i\Gamma,\quad
\Gamma=\sum_{x}\gamma_x|x,x\rangle\langle x,x|,
\]

with \(J\in\mathbb R\setminus\{0\}\) and every \(\gamma_x>0\). The total remaining norm at time \(t\) is \(\|e^{-iKt}\psi\|^2\); for a mixed initial state, it is \(\operatorname{Tr}(e^{-iKt}\rho e^{iK^*t})\). Capture means the limiting norm deficit as \(t\to\infty\). No interaction between the walkers, flux, occupation-dependent hopping, or missing detector is included.

## Proof

**1. Asymptotic capture equals orthogonal removal of invariant dark states.** For every state \(\psi(t)\),
\[\frac{d}{dt}\|\psi(t)\|^2=-2\langle\psi(t),\Gamma\psi(t)\rangle\le0.\]
Any eigenvector of \(K\) with real eigenvalue must be annihilated by \(\Gamma\) and be an eigenvector of the Hermitian operator \(H\). Conversely every \(H\)-eigenvector in \(\ker\Gamma\) evolves unitarily. A Jordan block on the real axis would create polynomial growth, contradicting the contraction property. Every remaining eigenmode of \(K\) decays, because its eigenvalue has strictly negative imaginary part. Moreover the sum \(\mathcal D\) of the dark eigenspaces reduces both \(H\) and \(\Gamma\), so its orthogonal complement is invariant. Thus the surviving squared norm is precisely the initial weight in \(\mathcal D\), and it depends only on \(\ker\Gamma=\operatorname{span}\{|x,x\rangle\}^{\perp}\), not the positive rates.

**2. Exactly one bright direction per nonempty momentum-energy sector.** Choose Fourier states \(|u\rangle=N^{-1/2}\sum_x e^{2\pi i\langle u,x\rangle/q}|x\rangle\). Their one-particle adjacency eigenvalues are \(d(q-1)-q\operatorname{wt}(u)\). In the ordered two-particle space, for a total momentum \(p\) and an integer \(0\le t\le2d\), the energy \(J(2d(q-1)-qt)\) sector consists of pairs \(|u,p-u\rangle\) satisfying
\[\operatorname{wt}(u)+\operatorname{wt}(p-u)=t.\]
The Fourier collision vector for total momentum \(p\) is \(|D_p\rangle=N^{-1/2}\sum_x e^{2\pi i\langle p,x\rangle/q}|x,x\rangle\). Up to an irrelevant sign convention, its spectral projection is proportional to the symmetric sum of all \(|u,p-u\rangle\) in the sector. Every term has the same nonzero coefficient, so the projected collision vector is nonzero if and only if at least one such \(u\) exists. There is exactly **one** bright direction in each nonempty pair \((p,t)\); its orthogonal complement is dark. Distinct pairs of total momentum and energy are mutually orthogonal.

**3. Counting nonempty sectors.** If \(p\) has \(w\) nonzero coordinates, a coordinate with \(p_i=0\) contributes either zero or two to \(t\), while a coordinate with \(p_i\ne0\) contributes one or two. The latter second possibility requires \(q\ge3\). Hence for \(w=0\) there are exactly \(d+1\) possible energies \(t=0,2,\ldots,2d\); for \(1\le w\le d\) every integer \(t=w,w+1,\ldots,2d\) occurs, giving \(2d-w+1\) energies. Since the number of momenta of weight \(w\) is \(\binom dw(q-1)^w\), the total bright rank is

\[
R=(d+1)+\sum_{w=1}^{d}\binom dw(q-1)^w(2d-w+1)
=q^{d-1}\bigl((d+1)q+d\bigr)-d.
\]

The symmetric two-particle dimension is \(N(N+1)/2\); subtraction proves the dimension formula. This also constructs an explicit orthogonal projector: from \(\mathcal H_+\), subtract the rank-one projector onto the normalized symmetric Fourier sum in every nonempty \((p,t)\) sector.

**4. Distance-resolved capture and a root-of-unity reduction.** For distinct positions \(x,y\), the normalized bosonic pair is \(|x,y\rangle_+=(|x,y\rangle+|y,x\rangle)/\sqrt2\). For fixed \((p,t)\), let \(m_{p,t}\) be the number of admissible ordered Fourier indices \(u\). The corresponding bright weight of a localized pair is

\[
\frac{2}{N^2m_{p,t}}\left|\sum_{\substack{u:\operatorname{wt}(u)+\operatorname{wt}(p-u)=t}}
 e^{2\pi i\langle u,x-y\rangle/q}\right|^2.
\]

The automorphism group of the Hamming graph is transitive on ordered pairs at any fixed distance \(s\), so take \(x-y\) to have \(s\) coordinates equal to one and \(d-s\) equal to zero. In a coordinate with \(p_i=0\), the generating polynomial for the Fourier character sum is \(1+(q-1)T^2\) when \(x_i=y_i\), and \(1-T^2\) otherwise. When \(p_i\ne0\), it is \(2T+(q-2)T^2\) when \(x_i=y_i\), and \((1+\zeta^{p_i})(T-T^2)\) otherwise, where \(\zeta=e^{2\pi i/q}\).

Fix \(b\) as the number of nonzero coordinates of \(p\) among the \(d-s\) equal-position coordinates, and \(r\) among the \(s\) unequal-position coordinates. The Fourier coefficient apart from the product of \((1+\zeta^{p_i})\) is \(f_{b,r,t}\), while the number of Fourier terms is \(g_{b+r,t}\). The sum over each nonzero momentum coordinate in the unequal-position group simplifies using

\[
\sum_{a=1}^{q-1}|1+\zeta^a|^2=2(q-2).
\]

There are \(\binom{d-s}{b}\binom sr\) choices of coordinate positions and \((q-1)^b\) choices of the remaining momentum values. Summing the resulting squared projections yields the stated exact rational formula. If a denominator vanishes, the corresponding Fourier sector is empty and its numerator coefficient also vanishes; omission is mathematically necessary, not a numerical convention. Substituting \(d=2\) and collecting rational terms yields the two displayed expressions.

## Verification

`formula_replay.py` evaluates the coefficient formula with exact integer polynomial arithmetic and rational fractions, checks six independently stated finite cases, and checks both \(d=2\) specializations for thirteen different nonbinary alphabet sizes. `matrix_replay.py` constructs the complete symmetric two-particle Hamiltonian directly from Hamming adjacency, diagonalizes each spectral sector, projects the collision-diagonal basis, and independently reproduces dark dimensions and localized capture for six small cases. The two programs share no code and compare independent constructions. They are finite corroborations: the proof above, not the sample calculations, covers all integers \(d\ge1\) and \(q\ge3\).

Replay with `python formula_replay.py` and `OPENBLAS_NUM_THREADS=1 python matrix_replay.py`. The second script requires `numpy` and the first requires only Python's standard library. Both scripts are included with this result.

## Relationship to prior work

Krovi and Brun [1] established the symmetry-induced infinite-hitting-time and dark-subspace mechanism for quantum walks, including continuous-time walks; that mechanism is antecedent, not a new claim here. Gamble and collaborators [2] wrote the noninteracting two-boson graph Hamiltonian as a symmetrized Kronecker sum, studying graph isomorphism and on-site Hubbard interactions rather than irreversible Hamming collision capture. Bernard, Crampé and Vinet [3] studied free **fermions** and entanglement on the same family of nonbinary Hamming graphs; their Hamming adjacency decomposition is relevant, but their calculated quantities are not the bosonic collision-dark ranks or loss probabilities here.

The binary hypercube \(q=2\) has a different total-momentum energy-support pattern: for a fixed nonzero momentum, parity gaps persist, whereas the present \(q\ge3\) sectors fill every integer energy index from momentum weight to maximum. In the binary case the bright rank is \(2^{d-1}(d+2)\), not the formula of this finding. The present claim is restricted to nonbinary alphabets and does not reassert the binary result as new.

## Limitations

All graph edges have one common real nonzero hopping amplitude. The particles do not interact coherently; losses occur on **all** collision vertices with strictly positive rates. The result gives asymptotic survival, not finite-time decay rates or protection under disorder, flux, missing detectors, correlated baths, particle-number changes before collision, or coherent on-site interactions. Exact priority over unindexed equivalent treatments is not established by finite searches, and no independent scientific audit is claimed.

## References

1. H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094v1 (public 2006-06-10), https://arxiv.org/abs/quant-ph/0606094.
2. J. K. Gamble, M. Friesen, D. Zhou, R. Joynt, and S. N. Coppersmith, *Two-particle quantum walks applied to the graph isomorphism problem*, arXiv:1002.3003v1 (public 2010-02-16), https://arxiv.org/abs/1002.3003.
3. P.-A. Bernard, N. Crampé, and L. Vinet, *Entanglement of free fermions on Hamming graphs*, *Nuclear Physics B* **986** (2023), 116061, https://doi.org/10.1016/j.nuclphysb.2022.116061.
