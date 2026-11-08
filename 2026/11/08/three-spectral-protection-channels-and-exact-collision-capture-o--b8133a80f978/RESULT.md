# Three spectral protection channels and exact collision capture on balanced multipartite quantum networks

## Finding

Let \(q\ge3\) and \(m\ge2\) be integers. Two noninteracting identical bosons hop with real nonzero uniform hopping \(J\) on the complete \(q\)-partite graph \(K_{m,\ldots,m}\), with \(m\) vertices in each part. At every vertex, two bosons on that vertex undergo irreversible loss with an arbitrary strictly positive rate. The full collision-dark space has dimension

\[
\dim\mathcal D=\binom{q(m-1)+1}{2}-q r_m+q(q-2)(m-1)+\frac{q(q-3)}2,
\qquad
r_m=\begin{cases}1,&m=2,\\m,&m\ge3.\end{cases}
\]

The three summands are the dimensions of dark spaces at the distinct two-boson hopping energies \(0\), \(-Jm\), and \(-2Jm\), respectively. All other energies support no collision-dark state. In particular, the last channel appears only when \(q\ge4\), and the middle channel has dimension \(q(q-2)(m-1)\) for every \(q\ge3\).

For a normalized initially localized bosonic pair on **distinct** vertices, the eventual collision-loss probabilities are exactly

\[
\eta_{\rm different}=\frac{2}{m(q-1)}
\quad\text{(vertices in different parts)},\qquad
\eta_{\rm same}=\begin{cases}1,&m=2,3,\\\frac{2}{m-1},&m\ge4\end{cases}
\quad\text{(vertices in the same part)}.
\]

For a doubly occupied initial vertex, the capture probability is one. For an arbitrary initial two-boson density matrix \(\rho\), the total eventual loss probability is \(1-\operatorname{Tr}(P_{\mathcal D}\rho)\), where \(P_{\mathcal D}\) is the orthogonal projector onto the three-channel space specified below. Every formula is independent of the positive individual loss rates.

For example, the octahedral network \(K_{2,2,2}\) has six dark dimensions and cross-part loss probability \(1/2\). The eight-vertex network \(K_{2,2,2,2}\) has sixteen dark dimensions and cross-part loss probability \(1/3\); two of its dark dimensions belong to the third, collective channel.

## Assumptions and scope

The graph has \(N=qm\) vertices, partitioned into \(q\) parts of equal size \(m\). Its one-particle adjacency matrix \(A\) has entry one between distinct parts and zero within parts. On \(\mathcal H=\operatorname{Sym}^2(\mathbb C^N)\), the Hamiltonian is \(H=J(A\otimes I+I\otimes A)\). The orthonormal bosonic position states are \(|v,v\rangle\) and \(|v,w\rangle_+=(|v,w\rangle+|w,v\rangle)/\sqrt2\) for \(v\ne w\).

For each vertex \(v\), let \(L_v=\sqrt{\gamma_v}\,|\mathrm{vac}\rangle\langle v,v|\), with \(\gamma_v>0\). In the two-particle no-jump sector the effective Hamiltonian is

\[
H_{\rm eff}=H-\frac{i}{2}\sum_v\gamma_v|v,v\rangle\langle v,v|.
\]

Define \(\Delta:\mathcal H\to\mathbb C^N\) by \((\Delta\psi)_v=\langle v,v|\psi\rangle\). The dark space \(\mathcal D\) is the maximal \(H\)-invariant subspace contained in \(\ker\Delta\); hence \(\mathcal D=\bigoplus_\lambda(\ker(H-\lambda I)\cap\ker\Delta)\). This is a no-interaction, no-detuning, finite-network and asymptotic-loss statement; it makes no assertion about finite-time decay rates.

## Proof

**Single-particle splitting.** Let \(u_a\) be the normalized uniform vector in part \(a\). Write \(T=\operatorname{span}(q^{-1/2}\sum_a u_a)\), \(V=\{\sum_a c_a u_a:\sum_a c_a=0\}\), and \(U=\bigoplus_a W_a\), where \(W_a\) is the dimension-\(m-1\) zero-sum space supported on part \(a\). The decomposition \(\mathbb C^N=T\oplus V\oplus U\) is orthogonal. The adjacency eigenvalues are respectively \(m(q-1)\), \(-m\), and \(0\). Set \(d=q(m-1)=\dim U\).

**Nonoverlapping two-body energies.** On \(\operatorname{Sym}^2\mathbb C^N\), the orthogonal sectors \(\operatorname{Sym}^2 T\), \(T\vee V\), \(T\vee U\), \(\operatorname{Sym}^2 V\), \(V\vee U\), and \(\operatorname{Sym}^2 U\) have energies, in this order,

\[
2Jm(q-1),\quad Jm(q-2),\quad Jm(q-1),\quad -2Jm,\quad-Jm,\quad0.
\]

These six values are pairwise distinct for every \(q\ge3\) and \(J\ne0\), so the dark kernel is calculated separately in each sector.

**Collision ranks.** On \(\operatorname{Sym}^2 U\), cross-part products \(W_a\vee W_b\), for \(a\ne b\), are collision-free. For one part, the diagonal map on \(\operatorname{Sym}^2 W_a\) has rank one when \(m=2\) and rank \(m\) when \(m\ge3\). For the latter case, choosing \(e_i-e_m\) for \(i<m\) shows that diagonal vectors of squares and pairwise products span all \(m\) site coordinates. Thus the zero-energy dark dimension is \(d(d+1)/2-qr_m\).

On \(V\vee U=\bigoplus_a(V\vee W_a)\), collisions in part \(a\) depend only on the \(a\)-th block-uniform coordinate of \(V\). This is one nonzero linear functional on the \((q-1)\)-dimensional \(V\), so the collision map has rank \(m-1\) on each part, leaving \(q(q-2)(m-1)\) dark dimensions at energy \(-Jm\).

On \(\operatorname{Sym}^2 V\), the collision map is the blockwise diagonal map from \(\operatorname{Sym}^2\{c\in\mathbb C^q:\sum c_a=0\}\) to \(\mathbb C^q\). Its rank is \(q\), by the same basis argument for \(q\ge3\), leaving \(q(q-3)/2\) dark dimensions at energy \(-2Jm\). The collision map is injective on each of \(\operatorname{Sym}^2T\), \(T\vee V\), and \(T\vee U\): multiplication by the constant nonzero \(T\)-amplitude cannot annihilate a nonzero factor. These ranks prove the stated dimension, spectral decomposition, and completeness.

**Localized capture.** The following diagonal-kernel identity gives the projection norms needed below. For \(n\ge3\), let \(V_n=\mathbf1^\perp\subset\mathbb C^n\), \(p_i=e_i-\mathbf1/n\), and \(z_{ij}=(p_i\otimes p_j+p_j\otimes p_i)/\sqrt2\) for \(i\ne j\). If \(D_n\) denotes the diagonal map on \(\operatorname{Sym}^2V_n\), then

\[
\|P_{\ker D_n}z_{ij}\|^2=\frac{n-3}{n-1}.
\]

Indeed, \(D_nD_n^*\) is the entrywise square of \(I-\mathbf1\mathbf1^*/n\), with eigenvalues \((n-1)/n\) on constants and \((n-2)/n\) on their orthogonal complement. Direct substitution yields \(\|z_{ij}\|^2=(n^2-2n+2)/n^2\) and \(\langle D_nz_{ij},(D_nD_n^*)^{-1}D_nz_{ij}\rangle=2(2n-1)/[n^2(n-1)]\). Their difference is the claimed norm. For \(n=2\), the corresponding diagonal kernel is zero.

For two vertices in different parts, the squared projections of their normalized bosonic pair onto the three dark sectors \(\operatorname{Sym}^2U\), \(V\vee U\), and \(\operatorname{Sym}^2V\) are respectively

\[
\frac{(m-1)^2}{m^2},\qquad
\frac{2(m-1)(q-2)}{m^2(q-1)},\qquad
\frac{q-3}{m^2(q-1)}.
\]

The first follows by applying the within-part zero-sum projector independently. For the middle term, each zero-sum factor has squared norm \((m-1)/m\); the other factor's projection onto \(\{c\in V:c_a=0\}\) has squared norm \((q-2)/[m(q-1)]\). The final term follows from the displayed diagonal-kernel identity with \(n=q\) and the two block-uniform amplitudes \(1/\sqrt m\). Summing gives dark survival \(1-2/[m(q-1)]\).

For a pair of distinct vertices in the same part, the two sectors involving \(V\) have zero dark projection: their block-vector components are proportional to the evaluation functional of that part and hence orthogonal to its kernel. The remaining projection is the same-part diagonal-kernel projection, of squared norm \((m-3)/(m-1)\) if \(m\ge3\), and zero if \(m=2\). This proves the second capture formula. Every doublon is orthogonal to \(\ker\Delta\).

**Asymptotic loss.** Since the rates are strictly positive, a no-jump eigenvector with real eigenvalue must have vanishing collision amplitudes. Thus the real spectral part of \(H_{\rm eff}\) is exactly \(\mathcal D\). Its orthogonal complement is invariant and has strictly decaying no-jump evolution in finite dimension. The long-time survival is therefore \(\operatorname{Tr}(P_{\mathcal D}\rho)\). Positive unequal rates cannot change this projector.

## Verification

The supplied \(\texttt{verify\_exact.py}\) constructs the integer symmetric-two-particle hopping matrix in an unnormalized pair basis. Finite-field Gaussian elimination checks the six collision-constrained energy-sector ranks for \((q,m)=(3,2),(4,2),(3,3),(4,3),(5,2)\). Its arithmetic is exact modulo a fixed prime; these finite cases do not replace the infinite-family proof.

The independent \(\texttt{verify\_numeric.py}\) uses an orthonormal pair basis, directly computes each collision-dark spectral kernel, and checks projector idempotence, Hamiltonian invariance, collision annihilation, dimension, and both localized capture probabilities at \((3,2),(4,2),(3,3),(4,3),(5,2),(3,4),(4,4)\). The checks were replayed successfully in Python 3 with NumPy.

## Relationship to prior work

Krovi and Brun established the general connection between quantum-walk symmetry, degeneracy, and non-detection; the mechanism is antecedent, not claimed here. Gamble, Friesen, Zhou, Joynt, and Coppersmith formulated the noninteracting two-boson graph Hamiltonian and developed matrix-element identities, especially for strongly regular graphs. These foundations do not explicitly state the present three-energy collision-dark decomposition or the two localized-loss laws. Everest, Hush, and Lesanovsky studied a different hard-core, nonlocal-loss model and the resulting slow Zeno dynamics, not the on-site two-boson loss on balanced multipartite networks. The established two-part complete-bipartite collision-loss case does not contain the three-or-more-part symmetry channels studied here.

## Limitations

The graph is balanced and complete multipartite, with \(q\ge3\), \(m\ge2\), and exactly uniform nonzero hopping. Unequal part sizes, arbitrary edge weights, on-site detuning, coherent two-body interactions, finite-time loss exponents, and thermodynamic-limit behavior are not addressed. Historical priority against an unindexed equivalent treatment cannot be conclusively excluded by the literature search. The finite calculations validate examples, not the infinitely many parameter pairs.

## References

1. H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094, first public 2006-06-10. https://arxiv.org/abs/quant-ph/0606094
2. J. K. Gamble, M. Friesen, D. Zhou, R. Joynt, and S. N. Coppersmith, *Two-particle quantum walks applied to the graph isomorphism problem*, arXiv:1002.3003, first public 2010-02-16. https://arxiv.org/abs/1002.3003
3. B. Everest, M. R. Hush, and I. Lesanovsky, *Many-body out-of-equilibrium dynamics of hard-core lattice bosons with non-local loss*, arXiv:1406.6097, first public 2014-06-23. https://arxiv.org/abs/1406.6097
