# Exact random-unitary threshold for tetrahedral phase damping

## Finding

Consider the Hermitian matrix
\[
K=\begin{pmatrix}
0&1&1&1\\
1&0&i&-i\\
1&-i&0&i\\
1&i&-i&0
\end{pmatrix},
\qquad K^2=3I_4.
\]
For \(0\le t\le1\), define \(C_t=I_4+(1-t)K/\sqrt3\) and the quantum channel \(\Phi_t:M_4(\mathbb C)\to M_4(\mathbb C)\) by \(\Phi_t(X)=C_t\circ X\), where \(\circ\) is entrywise multiplication. Then
\[
\boxed{\ \Phi_t\text{ is random unitary}\quad\Longleftrightarrow\quad
 t\ge t_*=1-\frac{\sqrt3}{2}.\ }
\]
In particular, the smallest admixture of complete computational-basis dephasing that converts \(\Phi_0\) into a mixture of unitary channels is exactly \(1-\sqrt3/2\), approximately \(0.133974596\).

At the boundary the classical unitary realization is unique up to reordering and irrelevant global phases. It uses precisely four diagonal unitaries with equal weights \(1/4\), with diagonals
\[
\begin{aligned}
z_1&=(1,1,1,1),&z_2&=(1,1,-i,i),\\
z_3&=(1,i,1,-i),&z_4&=(1,-i,i,1).
\end{aligned}
\]
Thus \(\Phi_{t_*}(X)=\frac14\sum_{j=1}^4 U_j XU_j^\dagger\), where \(U_j=\operatorname{diag}(z_j)\). Four is the minimum possible number of terms in a random-unitary representation at the boundary.

## Assumptions and scope

The system is a four-dimensional Hilbert space, equivalently two qubits when a computational basis is fixed. The parameter \(t\) is restricted to the closed interval \([0,1]\). A random-unitary channel means a finite convex combination of conjugations \(X\mapsto UXU^\dagger\) by arbitrary \(4\times4\) unitary matrices; diagonality is not imposed a priori. Complete basis dephasing means \(\Delta(X)=I_4\circ X\); this is **not** the completely depolarizing channel \(X\mapsto\operatorname{Tr}(X)I_4/4\).

The identity \(K^2=3I_4\) shows that \(K\) has eigenvalues \(+\sqrt3\) and \(-\sqrt3\), each twice, since \(\operatorname{Tr}K=0\). Thus \(C_0=I_4+K/\sqrt3\) is positive semidefinite, of rank two, with diagonal entries one; \(C_t=(1-t)C_0+tI_4\) is a correlation matrix for every allowed \(t\), hence defines a completely positive unital trace-preserving channel. Its off-diagonal overlap moduli are \(1/\sqrt3\) at \(t=0\). A rank-two Gram factorization supplies four pure environmental-qubit vectors with Bloch vectors having pairwise dot product \(-1/3\), namely a regular tetrahedron. This explains the canonical geometry of the channel family.

## Proof

**1. All unitary summands must be diagonal.** The map \(\Phi_t\) fixes every computational-basis rank-one projector \(P_k=|k\rangle\langle k|\). Suppose \(\Phi_t(X)=\sum_a p_aV_a XV_a^\dagger\) with \(p_a>0\), \(\sum_a p_a=1\), and unitary \(V_a\). Then \(P_k=\sum_a p_aV_aP_kV_a^\dagger\). The expectation of this equation in a basis vector orthogonal to \(|k\rangle\) is a sum of nonnegative terms equal to zero. Consequently every \(V_a|k\rangle\) is proportional to \(|k\rangle\). This holds for every \(k\), so every \(V_a\) is diagonal. Therefore \(\Phi_t\) is random unitary exactly when its correlation matrix belongs to the convex hull of \(zz^\dagger\) with \(|z_k|=1\).

**2. An exact unimodular witness bound.** We prove
\[
\max_{|z_1|=\cdots=|z_4|=1}z^\dagger Kz=6.
\]
An irrelevant common phase lets us set \(z=(1,e^{i\theta},e^{i(\phi+h)},e^{i(\phi-h)})\). Direct expansion of the six upper-triangle entries of \(K\) gives
\[
\frac12z^\dagger Kz
=\cos\theta+\sin(2h)
 +2\operatorname{Re}\!\left[e^{i\phi}\left(\cos h-e^{-i\theta}\sin h\right)\right].
\]
Put \(x=\cos\theta\) and \(y=\sin(2h)\); both lie in \([-1,1]\). Optimizing the last phase yields
\[
\frac12z^\dagger Kz\le x+y+2\sqrt{1-xy}\le3.
\]
The second inequality follows because \(3-x-y>0\) and
\[
(3-x-y)^2-4(1-xy)
=(x+y-1)^2+4(1-x)(1-y)\ge0.
\]
Equality requires \((x,y)=(1,0)\) or \((x,y)=(0,1)\), as well as alignment of \(\phi\) with the displayed complex coefficient. In the first case the two resulting projective vectors are \(z_1,z_2\); in the second they are \(z_3,z_4\), as listed above. Hence **exactly four** rank-one phase Gram matrices saturate the bound.

**3. Necessity.** If \(\Phi_t\) is random unitary, Step 1 and Step 2 give \(\operatorname{Tr}(KC_t)\le6\). But \(\operatorname{Tr}K=0\) and \(K^2=3I_4\), so
\[
\operatorname{Tr}(KC_t)=\frac{1-t}{\sqrt3}\operatorname{Tr}(K^2)
=4\sqrt3(1-t).
\]
Therefore \(4\sqrt3(1-t)\le6\), equivalently \(t\ge1-\sqrt3/2\). This is a necessary condition for a mixture of **arbitrary** unitaries, not only diagonal ones.

**4. Sufficiency and the boundary construction.** An entry-by-entry computation yields
\[
\frac14\sum_{a=1}^4z_az_a^\dagger=I_4+\frac12K=C_{t_*}.
\]
The four diagonal unitaries therefore realize \(\Phi_{t_*}\). Also \(\Delta\) is random unitary: writing \(f_k=(1,i^k,i^{2k},i^{3k})\) for \(k=0,1,2,3\), one has \(\frac14\sum_{k=0}^3f_kf_k^\dagger=I_4\). For \(t\in[t_*,1]\), set \(\lambda=(1-t)/(1-t_*)\in[0,1]\). Then
\[
\Phi_t=\lambda\Phi_{t_*}+(1-\lambda)\Delta,
\]
a convex combination of random-unitary channels. This establishes sufficiency, including both endpoints.

**5. Unique boundary realization and minimality.** If a random-unitary representation realizes \(C_{t_*}\), the witness is saturated. By the equality characterization in Step 2, all its projective vectors lie among the four \(z_a\). Write their total weights as \(w_1,\ldots,w_4\). The imaginary parts of the first-row off-diagonal entries imply \(w_2=w_3=w_4\), while the first off-diagonal entry gives \(w_1+w_2=1/2\); together with \(\sum_a w_a=1\), this forces \(w_a=1/4\) for all \(a\). Thus the convex representation is unique after merging repeated summands. Independently \(C_{t_*}=I_4+K/2\) has eigenvalues \(1\pm\sqrt3/2\), each with multiplicity two, and is full rank four. A sum of fewer than four rank-one correlation matrices cannot equal it, proving the minimum term count.

## Verification

The attached standard-library script `verify.py` performs exact Gaussian-integer checks of all sixteen entries of \(K^2=3I_4\), all sixteen entries of \(\frac14\sum_a z_az_a^\dagger=I_4+K/2\), saturation \(z_a^\dagger Kz_a=6\), the four Fourier twirl identities, and the four special saturators on the \(4^3\) fourth-root-of-unity phase grid. The continuum witness inequality, exhaustive equality analysis, and impossibility statement are **proved above**; finite-grid enumeration is merely a reproducibility check and is not treated as exhaustive phase optimization. Run with `python3 verify.py` in a standard Python 3 environment.

## Relationship to prior work

Helm and Strunz (2009) exhibited genuinely non-random-unitary two-qubit phase damping using a qubit environment, with an extremality criterion governed by the volume of four environmental Bloch vectors; their full text reports qualitative and numerical distance from random-unitary dynamics but does not classify admixtures of complete computational-basis dephasing. The exact channel family here specializes this environmental geometry to a regular tetrahedron.

Harris, Levene, Paulsen, Plosker, and Rahaman (2018), Theorem 2.2 (recalled from O'Meara and Pereira), characterize random-unitary Schur multipliers by convex combinations of phase rank-one correlation matrices; this gives a useful equivalent formulation but not the sharp threshold for the displayed \(K\). Kribs, Levick, Pereira, and Rahaman (2023), Corollary 34, guarantee random-unitary mixing once a rank-two correlation matrix has been diluted by at least one-half complete basis dephasing. Their Remark 35 explicitly notes that such bounds need not be sharp in low dimensions. The present exact threshold \(1-\sqrt3/2<1/2\) is a sharper specialized value together with its optimal witness and unique boundary decomposition.

## Limitations

The theorem concerns exactly the specified four-dimensional tetrahedral channel path; it does not classify every rank-two correlation matrix, calculate diamond-norm distance to the random-unitary set, or determine minimal unitary length for all intermediate parameter values. It is not a statement about full depolarization, entanglement breaking, or dynamics generated by a fixed time-independent Lindbladian. The presented literature comparison is finite rather than an independent global novelty certification; equivalent specialized results may exist elsewhere.

## References

1. J. Helm and W. T. Strunz, *Quantum Decoherence of Two Qubits*, arXiv:0910.5364v1, first posted 2009-10-28. Full text: https://arxiv.org/html/0910.5364v1
2. S. J. Harris, R. H. Levene, V. I. Paulsen, S. Plosker, and M. Rahaman, *Schur multipliers and mixed unitary maps*, arXiv:1807.06491v2 (2018), especially Theorem 2.2. Full text: https://arxiv.org/html/1807.06491v2
3. D. W. Kribs, J. Levick, R. Pereira, and M. Rahaman, *Operator Algebra Generalization of a Theorem of Watrous and Mixed Unitary Quantum Channels*, arXiv:2306.04077v1 (2023), especially Theorems 25 and 27, Corollary 34, and Remark 35. Full text: https://arxiv.org/html/2306.04077v1
