# Flux-parity arithmetic of persistent quantum trapping on cycles with two absorbers

## Finding
Consider a coherent quantum particle on an \(n\)-vertex nearest-neighbor cycle with a uniform Peierls flux and two partially absorbing sites. The permanent survival subspace is absent for every flux except zero and half a flux quantum. At either exceptional flux its dimension and the survival from *every* starting vertex are given exactly by elementary congruences; placing the two absorbers a coprime cyclic distance apart is necessary and sufficient for complete absorption at **every** flux.

Precisely, with \(g=\gcd(n,d)\) and \(z=\gcd(n,2d)\),
\[
 m(\phi)=\begin{cases}
\lfloor(z-1)/2\rfloor,&\phi\equiv0\pmod{2\pi},\\
\lfloor g/2\rfloor,&\phi\equiv\pi\pmod{2\pi}\text{ and }n/g\text{ odd},\\
0,&\text{otherwise}.
\end{cases}
\]
For a particle initially at vertex \(j\), the eventual norm squared is
\[
 S_j(0)=\frac2n\sum_{\substack{1\le k\le\lfloor(n-1)/2\rfloor\\ n\mid2kd}}\sin^2\left(\frac{2\pi kj}{n}\right),\qquad
 S_j(\pi)=\frac2n\sum_{\substack{1\le t<n,\;t\text{ odd}\\n\mid td}}\sin^2\left(\frac{\pi tj}{n}\right),
\]
and \(S_j(\phi)=0\) at every other flux.

On even cycles, the exceptional fluxes can act in **opposite directions**. If \(h=n/g\) is odd, the zero-flux and half-flux dark dimensions are \(g/2-1\) and \(g/2\). If \(h\) is even, they are \(g-1\) and \(0\). For example, with \(n=6,d=2\), half flux creates one dark mode and leaves exactly \(1/3\) of an excitation initially at \(j=1\), while zero flux absorbs it completely. In contrast, \(n=8,d=2\) has one zero-flux mode and no half-flux mode.

## Assumptions and scope
Let \(n\ge3\) and \(1\le d<n\) be integers, \(J>0\) a hopping energy, and \(\kappa_0,\kappa_d>0\) local absorption rates. The one-particle Hilbert space has orthonormal basis \(\{|x\rangle: x\in\mathbb Z/n\mathbb Z\}\). Set
\[
 H_0(\phi)=J\sum_{x=0}^{n-1}\left(e^{i\phi/n}|x\rangle\langle x+1|+e^{-i\phi/n}|x+1\rangle\langle x|\right),
\]
where indices are modulo \(n\), and the lossy Hamiltonian is
\[
 H_{\mathrm{eff}}=H_0(\phi)-\frac i2\left(\kappa_0|0\rangle\langle0|+\kappa_d|d\rangle\langle d|\right).
\]
For each unit initial vector \(|\psi\rangle\), define \(S_\psi(\phi)=\lim_{T\to\infty}\|e^{-iH_{\mathrm{eff}}T}|\psi\rangle\|^2\). Rates are time-independent and strictly positive; no dephasing, disorder, gain, extra hopping, or feedback is assumed. A nondecaying mode must be a genuine eigenvector of \(H_0(\phi)\) vanishing at both lossy sites. The claimed formula is independent of the positive rates but does not extend unchanged to a vanishing rate.

## Proof
**1. The dissipative subspace is exactly the common nodal eigenspace.** Put \(W=\kappa_0|0\rangle\langle0|+\kappa_d|d\rangle\langle d|\). For a solution \(|u(T)\rangle=e^{-iH_{\mathrm{eff}}T}|u(0)\rangle\),
\[
\frac{d}{dT}\|u(T)\|^2=-\langle u(T)|W|u(T)\rangle
=-\kappa_0|u_0(T)|^2-\kappa_d|u_d(T)|^2\le0.
\]
If \(H_{\mathrm{eff}}v=\lambda v\) and \(\operatorname{Im}\lambda=0\), this identity forces \(v_0=v_d=0\); hence \(H_0v=\lambda v\). Conversely, every such eigenvector of \(H_0\) has a real eigenvalue of \(H_{\mathrm{eff}}\) and does not decay. Their span \(\mathcal D\) is invariant under \(H_0,H_{\mathrm{eff}}\) and their adjoints; thus \(\mathcal D^\perp\) is invariant. Every eigenvalue of \(H_{\mathrm{eff}}|_{\mathcal D^\perp}\) has strictly negative imaginary part, so the finite-dimensional matrix exponential on this complement tends to zero, even if nontrivial Jordan blocks occur. Consequently \(S_\psi(\phi)=\|P_{\mathcal D}\psi\|^2\).

**2. Identify the only exceptional fluxes.** The plane waves \(v_k(x)=n^{-1/2}e^{2\pi ikx/n}\), \(0\le k<n\), have energies \(2J\cos((2\pi k+\phi)/n)\). Equality of two different cosine energies implies \(2\pi(k+\ell)+2\phi\equiv0\pmod{2\pi n}\), equivalently \(\phi\equiv0\pmod\pi\). Hence for any flux other than zero and half flux (modulo the flux quantum), all eigenvalues are simple. Every plane wave is nonzero at \(0\), so \(\mathcal D=0\).

**3. Zero flux.** At \(\phi=0\), the only degenerate pairs are \(k,n-k\) with \(1\le k\le\lfloor(n-1)/2\rfloor\). The unique (up to scale) vector in each pair vanishing at \(0\) is \(x\mapsto \sin(2\pi kx/n)\). It vanishes at \(d\) precisely when \(n\mid2kd\). Distinct such modes are mutually orthogonal with norm squared \(n/2\); the constant mode and the possible \(k=n/2\) mode are nonzero at \(0\). The eligible integers \(k\) are precisely the positive multiples of \(n/\gcd(n,2d)\) strictly below \(n/2\). Their number is \(\lfloor(\gcd(n,2d)-1)/2\rfloor\). Normalizing their contribution to \(|j\rangle\) proves the stated \(S_j(0)\).

**4. Half flux.** At \(\phi=\pi\), the paired eigenvalues correspond to the odd momenta \(t=2k+1\) with \(1\le t<n\). Up to a constant phase, the vector in each pair vanishing at \(0\) is \(x\mapsto e^{-i\pi x/n}\sin(\pi t x/n)\), with squared norm \(n/2\). A possible unpaired momentum when \(n\) is odd is never dark. Its paired dark candidate vanishes at \(d\) exactly when \(n\mid td\). Writing \(g=\gcd(n,d)\) and \(h=n/g\), this means \(h\mid t\). If \(h\) is even, none of these multiples \(t\) is odd; if \(h\) is odd, the odd multiples of \(h\) strictly below \(n=gh\) are \(h,3h,\ldots\), numbering \(\lfloor g/2\rfloor\). The normalized projection gives \(S_j(\pi)\).

**5. Universal placement and parity.** If \(g=1\), then \(n\mid2kd\) has no eligible \(k\), and \(n\mid td\) no eligible odd \(t<n\); thus no flux has a nondecaying mode. Conversely if \(g>1\), either \(n\) is odd, so \(\lfloor(g-1)/2\rfloor>0\), or \(n\) is even: if \(h\) is odd, \(g\) is even and the half-flux count is positive; if \(h\) is even, \(\gcd(n,2d)=2g\) and the zero-flux count is \(g-1>0\). Finally, for even \(n\), \(h\) odd forces \(g\) even and \(\gcd(n,2d)=g\), giving the claimed half-flux creation. For \(h\) even, the zero-flux count is \(g-1\), and the half-flux count vanishes. This proves the theorem.

## Verification
Run the standalone program `verify.py` with Python, NumPy and SciPy. It builds the actual complex Hermitian hopping matrix, independently computes the kernel of absorber evaluation within each energy eigenspace by singular-value decomposition, and compares the count of real eigenvalues of the non-Hermitian effective operator. For each \(3\le n\le24\), all \(1\le d<n\), three fluxes \(0\), \(\pi\), and \(0.317\pi\), and every initial vertex, it checks the explicit dimension and survival formula. It performs 825 spectrum pairs and all corresponding vertex projections; it also checks the coprime-placement equivalence and concrete opposite-flux examples. These are finite diagnostics; the five-step proof supplies the infinite-domain justification.

## Relationship to prior work
Krapivsky, Luck and Mallick (2013/14), Section 5, already analyzed avoiding modes and arithmetic constraints on **unthreaded** finite rings with multiple traps; the zero-flux methodology and generic projection identity are theirs, not new here. Emary (2007) showed flux-controlled dark-state blocking in a triangular-dot transport setup, so flux suppression or enhancement as a phenomenon is not new. Rudner, Levin and Levitov (2016) studied Bloch/topological dark states in periodically lossy one-dimensional networks, including twisted-boundary probes; those results do not state this finite two-absorber cyclic distance law. Le et al. (2017) investigated methods to suppress dark states in networks; their graph-theoretic results do not yield the two-flux arithmetic trichotomy. The focused contribution here is the **joint all-flux, all-distance, all-initial-site exact finite-cycle classification**, including parity reversal and the iff coprime placement criterion. The inference is conditional on the inspected texts; historical priority has not been independently certified.

## Limitations
The finite-dimensional, uniform-hop, single-particle, purely absorptive model omits disorder, interactions, reservoirs with coherent injection, dephasing, and multiple distributed impurities. Flux values arbitrarily close to, but unequal to, a resonance have zero infinite-time survival even though the decay time can be very long: **no uniform convergence in flux or finite-time robustness** is asserted. The zero-flux part is substantially covered by prior work, and uninspected literature may contain the half-flux arithmetic classification. No independent scientific validation has been performed.

## References
1. C. Emary, *Dark states in the magnetotransport through triple quantum dots*, arXiv:0705.2934, first public 2007-05-21. https://arxiv.org/html/0705.2934v1
2. P. L. Krapivsky, J. M. Luck, K. Mallick, *Survival of classical and quantum particles in the presence of traps*, arXiv:1311.6298, first public 2013-11-25, especially Section 5. https://arxiv.org/html/1311.6298v2
3. M. S. Rudner, M. Levin, L. S. Levitov, *Survival, decay, and topological protection in non-Hermitian quantum transport*, arXiv:1605.07652, first public 2016-05-24. https://arxiv.org/html/1605.07652v1
4. T. P. Le et al., *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482, first public 2017-07-24 (supporting literature, not archive focal). https://arxiv.org/abs/1707.07482
