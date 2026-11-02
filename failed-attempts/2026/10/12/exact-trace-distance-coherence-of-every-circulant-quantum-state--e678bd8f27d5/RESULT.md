# Exact trace-distance coherence of every circulant quantum state

## Finding

For every integer \(d\ge2\), let \(F_d\) be the normalized discrete Fourier transform and let \(p=(p_0,\ldots,p_{d-1})\) be a probability vector. Define
\[
\rho_p=F_d\,\operatorname{diag}(p)\,F_d^\dagger .
\]
Then the trace-distance coherence
\[
C_{\rm tr}(\rho_p):=\min_{\delta\in\mathcal I}\|\rho_p-\delta\|_1
\]
over computational-basis incoherent density matrices satisfies
\[
C_{\rm tr}(\rho_p)=\left\|\rho_p-\frac{I_d}{d}\right\|_1
=\sum_{k=0}^{d-1}\left|p_k-\frac1d\right|.
\]
Thus \(I_d/d\) is a closest incoherent state, and on the complete circulant state simplex trace-distance coherence is exactly twice the classical total-variation distance from the Fourier spectrum \(p\) to the uniform distribution. In dimension three, for
\[
\rho_{r,\theta}=\frac{I_3}{3}
+r\begin{pmatrix}
0&e^{i\theta}&e^{-i\theta}\\
e^{-i\theta}&0&e^{i\theta}\\
e^{i\theta}&e^{-i\theta}&0
\end{pmatrix},
\]
whenever \(1/3+2r\cos(\theta+2\pi k/3)\ge0\) for \(k=0,1,2\),
\[
C_{\rm tr}(\rho_{r,\theta})=4r\max_{k=0,1,2}\left|\cos(\theta+2\pi k/3)\right|.
\]
No uniqueness of the closest incoherent state is claimed.

## Assumptions and scope

The computational basis is fixed. The trace norm is \(\|X\|_1=\operatorname{tr}\sqrt{X^\dagger X}\), without the optional factor \(1/2\) sometimes included in the phrase “trace distance.” The incoherent set \(\mathcal I\) consists of diagonal positive semidefinite matrices of trace one. The normalized Fourier matrix \(F_d\) is unitary. The states \(\rho_p\) are exactly the density matrices invariant under the cyclic basis shift \(S|j\rangle=|j+1\pmod d\rangle\), equivalently the Hermitian circulant density matrices.

## Proof

Let \(\delta=\operatorname{diag}(q_0,\ldots,q_{d-1})\in\mathcal I\). Average its orbit under the cyclic shift:
\[
\bar\delta=\frac1d\sum_{m=0}^{d-1}S^m\delta S^{-m}=\frac{I_d}{d}.
\]
Because \(\rho_p\) is shift invariant, convexity and unitary invariance of the trace norm give
\[
\left\|\rho_p-\frac{I_d}{d}\right\|_1
=
\left\|\frac1d\sum_{m=0}^{d-1}S^m(\rho_p-\delta)S^{-m}\right\|_1
\le
\frac1d\sum_{m=0}^{d-1}\|\rho_p-\delta\|_1
=
\|\rho_p-\delta\|_1.
\]
Thus \(I_d/d\) is a closest incoherent state. Since
\[
\rho_p-\frac{I_d}{d}
=
F_d\,\operatorname{diag}\!\left(p_0-\frac1d,\ldots,p_{d-1}-\frac1d\right)F_d^\dagger,
\]
its singular values are \(\left|p_k-1/d\right|\), proving the formula.

For the qutrit family, the three Fourier eigenvalue deviations are
\[
2r\cos\!\left(\theta+\frac{2\pi k}{3}\right),\qquad k=0,1,2.
\]
They sum to zero. For any three real numbers with zero sum, the sum of their absolute values is twice their largest absolute value. Substitution yields the displayed qutrit formula.

## Verification

The proof is analytic and does not depend on finite sampling. The decisive check is the exact cyclic twirl: every diagonal density matrix is sent to \(I_d/d\), while every \(\rho_p\) is fixed. The trace-norm inequality therefore holds for every admissible \(\delta\), including boundary points with zero diagonal entries. Fourier diagonalization then gives the exact norm. The qutrit corollary follows from the explicit three eigenvalues and the zero-sum identity.

## Relationship to prior work

Shao, Xi, Fan, and Li introduced and analyzed trace-norm coherence and obtained closed formulas for several special qutrit classes, including single-coherence-edge forms; their treatment does not give the full circulant family. Rana, Parashar, and Lewenstein treated qubits, \(X\)-states, pure states, and semidefinite-program formulations for general states, without this circulant reduction. Wang, Wang, and Wang later solved a different qudit class in which all off-diagonal entries are the same real number; that class does not contain general complex circulant states. Later trace-norm resource-theory work gives broad orthogonality criteria, but the unrestricted-diagonal Birkhoff–James condition is different from the trace-one incoherent simplex optimized here.

The new point is the exact all-dimensional symmetry reduction and its classical interpretation:
\[
C_{\rm tr}(\rho_p)=2\,\operatorname{TV}(p,u_d).
\]

## Limitations

This result concerns the complete cyclic-shift-invariant state family, not arbitrary density matrices. It does not prove strong monotonicity of trace-norm coherence, does not classify all closest incoherent states, and does not assert that the displayed closest state is unique. A residual literature risk is that the same cyclic twirling argument may appear as an unstated special case of a later general symmetry-reduction theorem for resource distances.

## References

- Shao, Xi, Fan, and Li, “Fidelity and trace-norm distances for quantifying coherence,” arXiv:1410.8327; DOI:10.1103/PhysRevA.91.042120.
- Rana, Parashar, and Lewenstein, “Trace-distance measure of coherence,” arXiv:1511.01854.
- Wang, Wang, and Wang, “Trace distance measure of coherence for a class of qudit states,” arXiv:1610.07330.
- Johnston et al., “Birkhoff-James Orthogonality in the Trace Norm, with Applications to Quantum Resource Theories,” arXiv:2109.05552.
