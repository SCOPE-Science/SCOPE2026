# A valence-four threshold for bosonic collision-dark states on weighted quantum stars

## Finding
Consider two noninteracting identical bosons hopping on a star with one hub and \(q\ge 3\) leaves, with strictly positive but not necessarily equal hub-to-leaf hoppings \(w_1,\ldots,w_q\). At every vertex, doubly occupied states undergo irreversible pair loss with an independently chosen positive rate. The full loss-free subspace has dimension
\[
\dim\mathcal D=\frac{q(q-3)}2.
\]
It is absent for three leaves and appears sharply at four leaves. Every protected state has coherent energy zero, regardless of the positive hopping strengths and loss rates.

For \(1\le i<j\le q\), let \(|ij\rangle_+=(|i\rangle\otimes|j\rangle+|j\rangle\otimes|i\rangle)/\sqrt2\), and let \(\mathcal E\) be the span of these distinct-leaf states. Define the real \(q\)-by-\(\binom q2\) matrix \(B\), with one column indexed by each pair, by
\[
 B_{k,ij}=w_j\mathbf 1_{k=i}+w_i\mathbf 1_{k=j}.
\]
The full long-time survival projector is zero on \(\mathcal E^\perp\), and on \(\mathcal E\) it equals
\[
 P_{\mathrm{dark}}=I-B^\mathsf T(BB^\mathsf T)^{-1}B.
\]
For every normalized initial two-boson density matrix \(\rho\), the eventual probability of a pair-loss event is
\[
 \eta(\rho)=1-\operatorname{Tr}(P_{\mathrm{dark}}\rho).
\]
Here \(P_{\mathrm{dark}}\) is extended by zero on \(\mathcal E^\perp\). In particular, for an initially localized symmetrized distinct-leaf pair \(|ij\rangle_+\), with \(b_{ij}\) the corresponding column of \(B\),
\[
\eta_{ij}=b_{ij}^{\mathsf T}(BB^{\mathsf T})^{-1}b_{ij}.
\]
For uniform hopping this simplifies, for every leaf pair, to \(\eta_{ij}=2/(q-1)\); hence the protected probability is \((q-3)/(q-1)\), tending to one as the star degree increases. For example, the four-leaf uniform star loses exactly \(2/3\) of an initially localized pair's probability. With hoppings \((1,2,3,4)\), its first two leaves instead have exact loss probability \(179/929\).

## Assumptions and scope
The one-particle vertex set is \(\{0,1,\ldots,q\}\), with hub \(0\), leaves \(1,\ldots,q\), and single-particle Hermitian adjacency operator
\[
A=\sum_{i=1}^q w_i(|0\rangle\langle i|+|i\rangle\langle0|),\qquad w_i>0.
\]
The two-boson Hilbert space is \(\operatorname{Sym}^2\mathbb C^{q+1}\), and its coherent Hamiltonian is the restriction of \(A\otimes I+I\otimes A\). There are no extra on-site potentials, particle interactions, or direct leaf-to-leaf hoppings. For each vertex \(v\), use the jump \(L_v=\sqrt{\gamma_v}\,|\mathrm{vac}\rangle\langle vv|\), with \(\gamma_v>0\), into an orthogonal vacuum state. Equivalently, in the two-particle no-jump sector,
\[
H_{\mathrm{eff}}=H-\frac{i}{2}\sum_{v=0}^q \gamma_v|vv\rangle\langle vv|.
\]
The eventual loss probability is one minus the long-time two-particle survival probability. The result applies to every choice of positive real hoppings and positive real rates, every \(q\ge3\), and all initial density matrices in the two-boson sector; it says nothing about finite-time loss rates or stability under additional potentials.

## Proof
**1. Detectable eigenvectors.** Let \(D=\sum_v\gamma_v|vv\rangle\langle vv|\). Since \(H\) is Hermitian and all \(\gamma_v>0\), a real-eigenvalue right eigenvector \(\psi\) of \(H_{\mathrm{eff}}=H-iD/2\) obeys \(\langle\psi,D\psi\rangle=0\). Thus it has zero amplitude at every \(|vv\rangle\) and is an eigenvector of \(H\). Conversely, any eigenvector of \(H\) that vanishes on the entire collision diagonal is an undamped eigenvector. All other eigenvalues of the finite matrix \(H_{\mathrm{eff}}\) lie strictly below the real axis. The span \(\mathcal D\) of the undamped eigenvectors is reducing for both \(H\) and \(D\), so the evolution on its orthogonal complement decays to zero, including possible Jordan blocks. Therefore long-time survival is exactly the initial squared projection onto \(\mathcal D\).

**2. Exhaustion of the dark eigenvectors.** Introduce the normalized symmetric basis \(|0i\rangle_+\), \(|ij\rangle_+\) for distinct leaves, and collision basis \(|vv\rangle\). A dark eigenvector of \(H\), of energy \(\lambda\), can initially be expanded only in \(|0i\rangle_+\) and \(|ij\rangle_+\):
\[
|\psi\rangle=\sum_i a_i|0i\rangle_++\sum_{i<j}c_{ij}|ij\rangle_+.
\]
The eigenvalue equation at \(|ii\rangle\) has right-hand side \(\sqrt2w_i a_i\). Since \(w_i>0\), necessarily \(a_i=0\) for every leaf. The equation at \(|ij\rangle_+\) then reads \(\lambda c_{ij}=0\). A nonzero dark vector must consequently have \(\lambda=0\). Finally, the equations at \(|0i\rangle_+\) are exactly
\[
\sum_{j\ne i}w_jc_{\min(i,j),\max(i,j)}=0\qquad(i=1,\ldots,q),
\]
or \(Bc=0\). Conversely, every such vector is an exact zero-energy eigenvector with no collision amplitude. This proves \(\mathcal D=\ker B\) as an embedded subspace of distinct-leaf pairs, with no other hidden modes.

**3. Full row rank and the explicit projector.** Suppose \(B^\mathsf T u=0\). The column corresponding to \(i<j\) gives \(w_j u_i+w_i u_j=0\). Dividing by \(w_iw_j\) gives \(u_i/w_i+u_j/w_j=0\) for every leaf pair. A triangle of leaf indices forces each ratio to vanish, since \(q\ge3\). Thus \(\operatorname{rank}B=q\) and \(G=BB^\mathsf T\) is positive definite. Its entries are
\[
G_{ii}=\sum_{j\ne i}w_j^2,\qquad G_{ij}=w_iw_j\quad(i\ne j).
\]
The standard orthogonal kernel projector is \(I-B^\mathsf T G^{-1}B\); its rank is \(\binom q2-q=q(q-3)/2\). Applying the complementary projector to \(|ij\rangle_+\) gives the displayed formula for \(\eta_{ij}\).

**4. Uniform-hopping specialization.** If \(w_i=w>0\) for every leaf, then \(G=w^2((q-2)I+\mathbf 1\mathbf 1^\mathsf T)\). Since \(b_{ij}=w(e_i+e_j)\), direct inversion yields
\[
b_{ij}^\mathsf T G^{-1}b_{ij}=\frac2{q-1}.
\]
The rank and projector are unaffected by the magnitudes of the strictly positive collision rates, completing the argument.

## Verification
The accompanying `verify_star.py` constructs the independent two-particle hopping matrix using integer symmetric coordinate amplitudes, not the incidence projector. It computes the exact collision-observability rank from powers of the two-body Hamiltonian. The star's one-particle spectrum consists of \(0\) and \(\pm\sqrt{\sum_iw_i^2}\), so its two-particle Hamiltonian has at most five distinct eigenvalues; powers zero through four suffice exactly. It independently constructs the weighted incidence projector and checks its rank, idempotence, symmetry, null condition, and the uniform-hopping diagonal formula. Twelve exactly evaluated weighted cases with three through eight leaves, plus the two-leaf boundary case, pass. For a replay, use `python3 verify_star.py` with Python 3 and SymPy; the final line is `STAR_EXACT_ALL_OK`. The finite checks corroborate but do not replace the all-size proof.

## Relationship to prior work
Krovi and Brun (2006) established a general connection between dark invariant subspaces and incomplete quantum detection, but not the present two-boson weighted-star collision projector. Gamble et al. (2010) formulated two-boson walks on arbitrary graphs and the corresponding Hubbard collision operator; this supplies established modeling machinery, not the all-leaf irreversible loss classification. Gräfe et al. (2013) studied non-Hermitian lattice correlations with independent site losses, which differ from pair loss conditional on co-occupation. Qin et al. (2014) treated coherent interacting two-particle walks on one-dimensional lattices, not irreversible collision absorption on stars. Later general one-excitation graph trapping results, including Le et al. (2017), do not yield this two-particle leaf-pair projector without new analysis. The 2022 study of attractive two-exciton localization on extended stars concerns a different, coherent bound-state model; its complete text could not be inspected, so any additional overlap remains a historical-priority limitation.

The theorem's new component as assessed here is the sharp four-leaf onset and complete weighted, arbitrary-rate pair-loss projector, not the general principles of dark-state projection or the second-quantized two-body Hamiltonian. No claim of an exhaustive historical novelty search or independent scientific audit is made.

## Limitations
All hopping weights and collision rates must be strictly positive; zero couplings or zero rates can enlarge the dark space. On-site disorder, direct leaf-to-leaf hopping, interactions between the two walkers, and nonbosonic exchange sectors are outside the theorem. The result determines eventual capture, not the time required to approach it. Priority remains provisional, particularly regarding obscure collision-loss calculations and inaccessible full texts. The computational examples are finite and are not proofs of the infinite-family statement.

## References
- H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094v1 (first submitted 2006-06-10), https://arxiv.org/html/quant-ph/0606094v1.
- J. K. Gamble, M. Friesen, D. Zhou, R. Joynt, and S. N. Coppersmith, *Two-particle quantum walks applied to the graph isomorphism problem*, arXiv:1002.3003v1 (first submitted 2010-02-16), https://arxiv.org/abs/1002.3003.
- M. Gräfe et al., *Correlations of indistinguishable particles in non-Hermitian lattices*, New Journal of Physics 15, 033008 (2013), https://doi.org/10.1088/1367-2630/15/3/033008.
- X. Qin et al., *Quantum Walks of Two Interacting Particles in One Dimension*, arXiv:1402.3349v1 (first submitted 2014-02-14), https://arxiv.org/abs/1402.3349.
- T. P. Le, L. Donati, S. Severini, and F. Caruso, *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482v1 (2017), https://arxiv.org/abs/1707.07482.
- V. Pouthier, *Two-exciton bound state quantum self-trapping in an extended star graph*, Journal of Chemical Physics 156, 155101 (2022), https://doi.org/10.1063/5.0087200 (abstract examined; full text unavailable).
