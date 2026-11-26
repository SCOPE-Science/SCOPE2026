# Parity-exact reaction probabilities for two quantum walkers on a cycle

## Finding

Consider two distinguishable walkers on the vertices \(\mathbb Z_n\) of a cycle of length \(n\ge3\), with the free single-particle nearest-neighbor hopping matrix \(A_n\) and a nonzero real hopping coefficient \(J\). Both walkers evolve coherently until occupying the same site, where an irreversible reaction may remove their joint state. On the ordered two-particle Hilbert space \(\mathscr H=\mathbb C^n\otimes\mathbb C^n\), put
\[
 H=J(A_n\otimes I+I\otimes A_n),\quad
 Q=\sum_{a=0}^{n-1}\gamma_a|a,a\rangle\langle a,a|,\quad
 K=H-\tfrac i2 Q,
\]
where **every** \(\gamma_a>0\), with no requirement that the rates be equal. The no-reaction state evolves as \(e^{-itK}\rho e^{itK^\dagger}\). The eventual reaction probability is one minus the limit of its trace.

**Theorem.** The total dimension \(R_n\) of the subspace eventually absorbed is
\[
 R_n=\begin{cases}
 n(n+1)/2,&n\text{ odd},\\
 n^2/2,&n\equiv0\pmod4,\\
 n^2/2+1,&n\equiv2\pmod4.
 \end{cases}
\]
For every initial ordered position state \(|x,y\rangle\), set \(d\equiv x-y\pmod n\), with \(0\le d<n\). Its eventual reaction probability is exactly
\[
 C_n(d)=\begin{cases}
 1,&d=0,\\
 1/2,&n\text{ odd},\ d\ne0,\\
 1/2-1/(2n),&n\text{ even},\ d\notin\{0,n/2\},\\
 1/2-1/n,&n\equiv0\pmod4,\ d=n/2,\\
 1/2,&n\equiv2\pmod4,\ d=n/2.
 \end{cases}
\]
Both formulas hold for all prescribed positive reaction rates and all nonzero real \(J\), without taking a weak- or strong-loss limit.

Let \(\mathsf S|x,y\rangle=|y,x\rangle\) be particle exchange and \(P_+=(I+\mathsf S)/2\) the bosonic spatial projector. For distinct sites, the normalized symmetric state \(|x,y\rangle_+=(|x,y\rangle+|y,x\rangle)/\sqrt2\) has eventual reaction probability \(2C_n(d)\). In particular, every such bosonic state reacts with probability one on an **odd** cycle. On an **even** cycle the probability is \(1-1/n\) at non-antipodal distinct sites; at antipodal sites it is \(1-2/n\) if \(4\mid n\) and one if \(n\equiv2\pmod4\). Every antisymmetric spatial state is permanently reaction-free.

## Assumptions and scope

The cycle has distinct left and right neighbors at each vertex; hence \(n\ge3\). The particles may be regarded as distinguishable species with equal coherent hopping, or as identical particles after restricting to the normalized symmetric (bosonic) or antisymmetric (fermionic) spatial subspace. The loss is a no-jump effective Hamiltonian for pair removal at coincident sites, with strictly positive rates \(\gamma_a\) that may vary from site to site. No coherent interparticle potential, hopping asymmetry, magnetic phase, dephasing, or loss outside the coincidence diagonal is assumed.

The claim concerns the limit as \(t\to\infty\) of the no-reaction norm, not a finite-time meeting probability or a discrete-time measurement protocol. All dimensions refer to complex vector spaces. An initial density matrix is any positive semidefinite trace-one matrix on \(\mathscr H\).

## Proof

**1. The eventual-reaction projector.** Let \(\mathcal D\) be the maximal \(H\)-invariant subspace of \(\ker Q\). Since \(H\) is Hermitian, \(\mathcal D\) is a reducing subspace for \(H\). Since \(Q\mathcal D=0\), positivity and self-adjointness of \(Q\) also make \(\mathcal D^\perp\) invariant under \(Q\). On \(\mathcal D\) the no-reaction evolution is unitary. On \(\mathcal D^\perp\), an eigenvector of \(K\) with an eigenvalue of vanishing imaginary part would obey \(\langle v,Qv\rangle=0\), hence \(Qv=0\), and also \(Hv=\lambda v\); this contradicts maximality of \(\mathcal D\). All eigenvalues there have strictly negative imaginary parts, so finite-dimensional Jordan theory gives exponential decay. Therefore
\[
 \lim_{t\to\infty}\operatorname{Tr}(e^{-itK}\rho e^{itK^\dagger})
 =\operatorname{Tr}(P_{\mathcal D}\rho),\qquad
 P_{\mathcal B}=I-P_{\mathcal D}.
\]
Consequently \(P_{\mathcal B}\) projects onto the smallest \(H\)-invariant subspace containing the entire coincidence diagonal \(\operatorname{span}\{|a,a\rangle\}\). This subspace depends on the **support** of the positive rates but not their values.

**2. Resolving total momentum.** Set \(\omega=e^{2\pi i/n}\) and use the normalized one-particle Fourier vectors \(|q\rangle=n^{-1/2}\sum_x\omega^{qx}|x\rangle\), with \(q\in\mathbb Z_n\). In the total-momentum sector \(k\in\mathbb Z_n\), let \(|k;q\rangle=|q,k-q\rangle\). These form an orthonormal basis of an \(n\)-dimensional invariant sector. The corresponding free energies are
\[
 E_{k,q}=2J\cos\frac{2\pi q}{n}+2J\cos\frac{2\pi(k-q)}{n}
 =4J\cos\frac{\pi k}{n}\cos\frac{\pi(2q-k)}n.
\]
The Fourier transforms of the coincidence states are
\[
 |\chi_k\rangle=\frac1{\sqrt n}\sum_{a=0}^{n-1}\omega^{ka}|a,a\rangle
 =\frac1{\sqrt n}\sum_{q=0}^{n-1}|k;q\rangle.
\]
The \(n\) vectors \(\chi_k\) form an orthonormal basis of the coincidence diagonal. Hence the bright subspace in sector \(k\) is the cyclic \(H\)-span of \(\chi_k\). This conclusion uses only \(\ker Q\), so no translation symmetry of the *rates* is needed.

**3. All nonflat sectors have exactly the exchange-symmetric bright space.** Unless \(n\) is even and \(k=n/2\), the prefactor \(\cos(\pi k/n)\) is nonzero. Equality of energies in the same sector then holds precisely for \(q'=q\) or \(q'=k-q\pmod n\). Thus distinct spectral eigenspaces correspond to the orbits of \(q\mapsto k-q\). The projection of \(\chi_k\) onto every orbit is nonzero and spans its one-dimensional symmetric combination; its antisymmetric combination, when present, vanishes at every coincidence site. These symmetric combinations are exactly the \(+1\) eigenspace of particle exchange \(\mathsf S\) in that sector. By the spectral theorem, the bright projector of every nonflat sector is the restriction of \(P_+\).

**4. The exceptional zero-hopping sector.** When \(n\) is even, the single sector \(k=n/2\) has \(E_{k,q}=0\) for **all** \(q\). Its entire Hamiltonian vanishes, so its coincidence-driven bright space is only \(\operatorname{span}\{\chi_{n/2}\}\), independent of the dimension of its exchange-symmetric part. Let \(\Pi_\pi\) be the orthogonal projector onto this total-momentum sector. Altogether, the exact bright projector is
\[
 P_{\mathcal B}=\begin{cases}
 P_+,&n\text{ odd},\\
 P_+-\Pi_\pi P_++|\chi_{n/2}\rangle\langle\chi_{n/2}|,&n\text{ even}.
 \end{cases}
\]
The factors \(\Pi_\pi\) and \(P_+\) commute. Exchange acts inside sector \(k\) by swapping \(q\) and \(k-q\), so the number of fixed Fourier labels is the number of solutions of \(2q=k\pmod n\). In the exceptional sector this count is two if \(4\mid n\) and zero if \(n\equiv2\pmod4\). Consequently its symmetric dimension is \(n/2+1\) or \(n/2\), respectively. Subtracting that dimension from \(\dim P_+=n(n+1)/2\) and adding the single bright vector \(\chi_{n/2}\) gives the three asserted formulas for \(R_n\).

**5. Localized and exchange-symmetric probabilities.** For \(x\ne y\), \(\langle x,y|P_+|x,y\rangle=1/2\). In the even case the exceptional-sector overlap is
\[
 \langle x,y|\Pi_\pi P_+|x,y\rangle
 =\frac1{2n}\left[1+\mathbf1_{\{2d\equiv0\pmod n\}}(-1)^d\right].
\]
This follows by Fourier summation over common translations: the exchanged coordinates lie on the same translation orbit only when \(2d\equiv0\pmod n\). Moreover \(\langle x,y|\chi_{n/2}\rangle=0\) for \(x\ne y\). Therefore the second bright-projector formula yields \(1/2-1/(2n)\) away from the antipode, and either \(1/2-1/n\) or \(1/2\) at the antipode according to the parity of \(n/2\). For \(x=y\), the state itself is in the coincidence diagonal, so \(C_n(0)=1\). For odd \(n\), \(P_{\mathcal B}=P_+\), giving \(1/2\) at any distinct sites.

Finally \(P_{\mathcal B}\mathsf S=P_{\mathcal B}\); for distinct sites the two cross terms of the normalized symmetric state equal the two diagonal terms. Hence its bright expectation is twice the distinguishable-state probability. For every antisymmetric state \(P_{\mathcal B}=0\), proving all remaining assertions.

## Verification

Run the supplied standalone script with `python verify.py` after installing the dependencies in `requirements.txt`. It constructs the two-particle Hermitian Hamiltonian independently, resolves numerically degenerate energy eigenspaces, computes the exact detector-visible bright projection by singular-value decomposition, and compares its rank and every localized matrix element with the closed formulas. It also checks every distinct-site symmetric input and compares finite-time no-jump evolution with predicted limiting survival for several nonuniform positive rate arrays. The completed run reported:

`VERIFY_OK spectral_dimensions=8 exact_sitewise=380 bosonic_states=328 lossy_evolutions=24`

The finite computations cover \(3\le n\le10\) and are corroboration only; the proof above supplies the infinite-family conclusion. The finite-time check is sensitive to slow decay and does not establish any rate-uniform convergence bound.

## Relationship to prior work

Štefaňák, Kiss, Jex and Mohring studied the meeting probability for two discrete-time coined walkers on an infinite line, including bosonic and fermionic statistics. The present continuous-time, finite periodic, continuously absorbing model asks for eventual reaction, rather than the probability of simultaneous occupancy at discrete observation times. Foss-Feig, Daley, Thompson and Rey developed the physical mechanism by which two-body reactions preserve antisymmetric orbital states; that general protection is assumed and credited, not claimed as new. Qin and collaborators studied periodic two-particle lattice motion and bound-state co-walking, without a complete coincidence-loss spectral rank and exact sitewise eventual reaction law. Razzoli, Paris and Bordone developed the spectral transport-subspace method on one-particle graphs, on which the bright-projector viewpoint builds.

A related earlier finite-path classification gives only exchange-antisymmetric collision-dark states for nonzero nearest-neighbor path hoppings. The closing edge of the present **cycle** is not covered by that path result. The relevant new distinction is the exceptional flat total-momentum sector on every even cycle and its dimension- and position-dependent effect on *symmetric* reaction-free states; in odd cycles the familiar antisymmetric-only behavior persists. The theorem is an explicit evaluation of a physically motivated geometry, not a claim to invent the underlying spectral or exchange-symmetry principles.

## Limitations

The formulas concern finite periodic nearest-neighbor cycles with identical hopping for the two particles, strictly positive coincidence-loss rates, and no coherent two-body potential. They do not assert the same probability under magnetic flux, unequal walker hoppings, additional dephasing, interactions, or incomplete coverage of the coincidence diagonal. Nor do they address a discrete-time detection protocol, finite-time reaction rates, non-Markovian losses, or a uniform bound on the time required to approach the limit. No independent audit or exhaustive worldwide publication-priority certification is claimed.

## References

1. M. Štefaňák, T. Kiss, I. Jex and B. Mohring, *The meeting problem in the quantum random walk*, arXiv:0705.1985v1 (14 May 2007), https://arxiv.org/abs/0705.1985.
2. M. Foss-Feig, A. J. Daley, J. K. Thompson and A. M. Rey, *Steady-state many-body entanglement of hot reactive fermions*, arXiv:1207.4741v1 (19 July 2012), https://arxiv.org/abs/1207.4741.
3. X. Qin, Y. Ke, X. Guan, Z. Li, N. Andrei and C. Lee, *Quantum Walks of Two Interacting Particles in One Dimension*, arXiv:1402.3349v1 (14 February 2014), https://arxiv.org/abs/1402.3349.
4. L. Razzoli, M. G. A. Paris and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794v2 (2021), https://arxiv.org/abs/2011.13794.
