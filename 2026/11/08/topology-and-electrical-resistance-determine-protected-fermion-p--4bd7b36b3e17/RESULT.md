# Topology and electrical resistance determine protected fermion pairs on complete networks

## Finding

Two noninteracting spinless fermions on a uniformly coupled complete hopping network need not be captured even after arbitrarily long exposure to a collection of pair-annihilation channels. For any monitored-pair graph \(F\), the entire permanently protected sector has a graph-topological decomposition:

\[
\mathcal D\cong \widetilde H_0(F;\mathbb C)\oplus H_1(\overline F;\mathbb C),
\qquad
\dim\mathcal D=c(F)-1+\beta_1(\overline F).
\]

The two summands occupy distinct hopping energies, \((n-2)J\) and \(-2J\), respectively. These are vector-space identifications, not assertions about a canonical spatial homology of the many-body configuration graph.

For localized initial pair \(|ab\rangle\), write \(S_{ab}\) for the probability that both fermions remain forever rather than suffer an eventual pair-annihilation jump. Then

\[
S_{ab}=\begin{cases}
0,&ab\in E(F),\\
1-R_{\overline F}(a,b)+\displaystyle\frac{\mathbf1_{C_F(a)\ne C_F(b)}}n
\left(\frac1{|C_F(a)|}+\frac1{|C_F(b)|}\right),&ab\in E(\overline F).
\end{cases}
\]

Here every edge of \(\overline F\) has unit electrical resistance, and \(R\) is evaluated in the connected component containing its endpoints. For general initial density operator \(\rho\), the survival probability is \(\operatorname{Tr}(P_\mathcal D\rho)\), with the complete projector given below.

In particular, all inputs are eventually absorbed if and only if \(F\) is connected and \(\overline F\) contains no cycles. For \(n\ge4\), the fewest monitored edges that can achieve this is \(\binom n2-n+1\), attained by making \(\overline F\) a spanning path. For even \(n\ge4\), when \(F\) is a perfect matching, \(\dim\mathcal D=\binom n2-n\), an initially monitored pair is captured with certainty, and an initially unmonitored pair survives with probability \(1-1/(n-2)\).

## Assumptions and scope

Fix any integer \(n\ge3\), set \(V=\{1,\ldots,n\}\), and let \(F=(V,E_F)\) be any finite simple undirected graph. The one-particle hopping operator is \(h=J(\mathbf1\mathbf1^\mathsf T-I)\) for a nonzero real \(J\). The exactly-two-particle Hilbert space is \(\mathcal H=\bigwedge^2\mathbb C^n\), with orthonormal occupation vectors \(|ab\rangle=e_a\wedge e_b\) for \(a<b\). The coherent Hamiltonian is \(H=h\otimes I+I\otimes h\) restricted to the antisymmetric sector. For each \(ab\in E_F\), an independent two-body loss jump has form \(L_{ab}=\sqrt{\gamma_{ab}}c_ac_b\), where \(\gamma_{ab}>0\). The jump removes both particles into the vacuum. No single-particle loss, dephasing, interactions, complex Peierls phases, or additional level shifts are assumed.

The no-jump two-particle evolution has generator \(H_{\mathrm{eff}}=H-\tfrac i2\sum_{ab\in E_F}\gamma_{ab}|ab\rangle\langle ab|\). Indefinite survival is the limit \(\lim_{t\to\infty}\|e^{-itH_{\mathrm{eff}}}\psi\|^2\); the unconditional two-particle population has the same limit. All results concern this asymptotic probability, not a finite-time lifetime. A component is counted even if it consists of one isolated vertex. Let \(\overline F=(V,\binom V2\setminus E_F)\).

## Proof

**1. Two hopping energies.** Set \(u=n^{-1/2}\mathbf1\). The one-particle operator \(h\) acts by \((n-1)J\) on \(u\), and by \(-J\) on \(u^\perp\). Consequently the antisymmetric two-particle space splits orthogonally as

\[
\mathcal H=(u\wedge u^\perp)\oplus\bigwedge^2u^\perp,
\qquad
H=(n-2)J\,P_+-2J\,P_-.
\]

The energies differ by \(nJ\ne0\). A vector stays outside all monitored occupation states under coherent evolution exactly when each of its two spectral components has zero coefficient on every edge of \(F\).

**2. Higher-energy protected states.** The amplitude of \(u\wedge v\), with \(v\perp u\), at \(a<b\) is \((v_b-v_a)/\sqrt n\). This vanishes on every edge of \(F\) precisely when \(v\) is constant on every connected component of \(F\). Orthogonality to \(u\) removes the one global constant direction. There are exactly \(c(F)-1\) independent protected vectors at energy \((n-2)J\).

**3. Lower-energy protected states.** Regard \(\bigwedge^2\mathbb C^n\) as the oriented edge space of \(K_n\). For its oriented incidence matrix \(B\), contraction with \(u\) equals \(B/\sqrt n\), up to orientation convention. Thus \(\bigwedge^2u^\perp=\ker B\), the ordinary divergence-free real or complex flow space. Eliminating amplitudes on all edges of \(F\) leaves exactly \(\ker B_{\overline F}\), the cycle-flow space of \(\overline F\), embedded by zero extension. Its dimension is \(|E(\overline F)|-n+c(\overline F)=\beta_1(\overline F)\). The two protected subspaces are orthogonal because they have different hopping energies. This proves the dimension and identifies an explicit cycle-basis construction.

**4. Full orthogonal projector.** For each component \(C\) of \(F\) let \(\mathbf1_C\) be its vertex-indicator vector. Define the orthogonal projection

\[
Q_F=\sum_{C\in\pi_0(F)}\frac{\mathbf1_C\mathbf1_C^{\mathsf T}}{|C|}-uu^{\mathsf T}
\]

on the component-constant zero-sum vertex vectors. Let \(U:v\mapsto u\wedge v\), \(B_{\overline F}\) be the \(n\)-by-\(|E(\overline F)|\) incidence matrix of the complement, \(L_{\overline F}=B_{\overline F}B_{\overline F}^{\mathsf T}\), and \(E_{\overline F}\) embed its edge space into that of \(K_n\). Then the exact dark projector is

\[
P_{\mathcal D}=UQ_FU^\dagger+
E_{\overline F}\bigl(I-B_{\overline F}^{\mathsf T}
L_{\overline F}^{+}B_{\overline F}\bigr)E_{\overline F}^{\mathsf T}.
\]

Here \(L^+\) means the Moore–Penrose pseudoinverse; the second summand is zero if \(\overline F\) has no edges. The incidence identity yields the orthogonal projection onto the cycle kernel even if \(\overline F\) is disconnected.

**5. Exact localized survival.** Project \(|ab\rangle\) onto the higher-energy protected subspace. If \(a,b\) lie in the same component of \(F\), its squared norm is zero. Otherwise the squared norm is \(n^{-1}(|C_F(a)|^{-1}+|C_F(b)|^{-1})\). On the lower-energy protected subspace, a monitored pair has zero projection. For an unmonitored pair, the cycle-projector diagonal is \(1-d_{ab}^{\mathsf T}L_{\overline F}^+d_{ab}=1-R_{\overline F}(a,b)\), where \(d_{ab}=e_b-e_a\). Adding these orthogonal contributions gives the displayed law.

**6. Why this is eventual survival.** The dark projector commutes with \(H\), and all \(L_{ab}\) annihilate its image. The orthogonal complement is invariant under both \(H\) and the positive loss operator. If a non-dark eigenvector of \(H_{\mathrm{eff}}\) had a purely real eigenvalue, the imaginary part of its expectation would force every monitored-pair amplitude to vanish (because every rate is positive); it would then be a protected eigenvector of \(H\), contradiction. Thus every eigenvalue on the finite-dimensional bright complement has strictly negative imaginary part. Its no-jump propagator tends to zero, including any Jordan-block contributions. The remaining norm is exactly the initial dark projection norm, independently of the actual positive rates.

**7. Full-capture threshold and matching case.** Both terms in \(\dim\mathcal D=\beta_1(\overline F)+c(F)-1\) are nonnegative, so \(\mathcal D=0\) precisely when \(F\) is connected and \(\overline F\) is a forest. A forest has at most \(n-1\) edges, giving the stated lower bound on monitored pairs. For \(n\ge4\), taking \(\overline F=P_n\) attains it and leaves \(F=K_n\setminus P_n\) connected. For a perfect matching \(F\) on even \(n\ge4\), \(c(F)=n/2\) and \(\overline F\) is connected, giving dimension \(\binom n2-n\). The complement's Laplacian has eigenvalues \(0\), \(n-2\) on pair-antisymmetric modes, and \(n\) on nonconstant pair-symmetric modes. For an unmonitored cross-pair, its effective resistance is \(1/(n-2)+1/n\), and its higher-energy dark projection has squared norm \(1/n\). Thus the total survival is \(1-1/(n-2)\).

## Verification

The included scripts provide independently organized finite checks. `check_numeric.py` constructs the complete signed fermion hopping Hamiltonian directly, diagonalizes its two energy blocks, and computes the dark projector by nullspaces of the monitored-pair amplitudes. It checks the dimension and every diagonal survival entry against the graph/resistance formulas for 120 fixed and seeded graph selections through eight vertices. An explicit non-Hermitian no-jump evolution with unequal rates converges to the predicted projector probability.

`check_exact.py` uses integer matrices, fundamental cycle bases, component-potential bases, rational orthogonal projection, and exact reduced-Laplacian inversion. It independently tests all monitored-edge graphs on three and four vertices and selected graphs on five through seven vertices, including the separate maximality test from ranks of the two Hamiltonian spectral projections. `check_cutoff.py` exhaustively tests the graph-theoretic full-capture threshold on every graph of up to six vertices. Run the scripts using Python 3 with the packages stated in `requirements.txt`.

These computations check finite examples; the all-size claims follow from the preceding arguments, not from a finite census.

## Relationship to prior work

Krovi and Brun (2006) establish the general existence of non-hitting invariant quantum-walk subspaces. Varbanov, Krovi and Brun (2008) analyze continuous-time absorbing measurements and spectral dark projectors. Gamble and collaborators (2010) treat antisymmetric two-fermion walks, but not graph-patterned two-body absorption. Ates and collaborators (2012) physically motivate nonlocal pair annihilation in hard-core boson lattices, with emphasis on strong-loss-induced complexes. Belovs (2013) relates quantum-walk search complexity to electrical resistance. None of these inspected results states the arbitrary-loss-graph cycle-plus-component classification, the edgewise eventual-survival resistance formula, or the minimal pair-monitoring threshold. The spectral-projection principle and electrical/graph Hodge identities themselves are classical ingredients, not claimed as discoveries.

## Limitations

The coherent hopping graph must be complete with a single uniform nonzero real hopping; the particles must be identical noninteracting spinless fermions, with precisely the specified pair-annihilation losses of strictly positive strength. A rate tending to zero while still positive does not affect asymptotic survival, but setting it exactly to zero changes the monitored graph. No finite-time decay-rate estimate is made. The theorem does not extend automatically to interacting, dephasing, or nonuniform-hopping networks. Bibliographic searches and inspected primary texts are not an exhaustive proof of historical priority; unindexed equivalent applications of standard graph Hodge theory remain a residual risk.

## References

1. H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094v1 (first posted 10 June 2006), https://arxiv.org/html/quant-ph/0606094v1 .
2. M. Varbanov, H. Krovi, and T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446 (first posted 24 March 2008), https://arxiv.org/abs/0803.3446 .
3. J. K. Gamble, M. Friesen, D. Zhou, R. Joynt, and S. N. Coppersmith, *Two-particle quantum walks applied to the graph isomorphism problem*, arXiv:1002.3003 (first posted 16 February 2010), https://arxiv.org/abs/1002.3003 .
4. C. Ates, B. Olmos, W. Li, and I. Lesanovsky, *Dissipative Binding of Lattice Bosons through Distance-Selective Pair Loss*, arXiv:1207.6291 (first posted 26 July 2012), https://arxiv.org/abs/1207.6291 .
5. A. Belovs, *Quantum Walks and Electric Networks*, arXiv:1302.3143 (first posted 13 February 2013), https://arxiv.org/abs/1302.3143 .
