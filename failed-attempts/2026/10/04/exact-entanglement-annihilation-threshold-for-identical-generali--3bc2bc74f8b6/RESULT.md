# Exact entanglement-annihilation threshold for identical generalized amplitude-damping channels
## Finding
For the generalized amplitude-damping qubit channel \(\mathcal G_{\gamma,n}\) defined below, with \(0\leq\gamma,n\leq1\),
\[
\mathcal G_{\gamma,n}^{\otimes2}\text{ is entanglement-annihilating}
\quad\Longleftrightarrow\quad
2(1+\sqrt2)n(1-n)\gamma^2+\gamma-1\geq0.
\]
Equivalently, the tensor square annihilates every two-qubit entangled input exactly when it makes the singlet \(|\Psi^-\rangle=(|01\rangle-|10\rangle)/\sqrt2\) separable. For \(0<n<1\), the threshold is
\[
\gamma_{\mathrm{EA}}(n)=\frac{2}{1+\sqrt{1+8(1+\sqrt2)n(1-n)}}.
\]
This proves Numerical Conjecture 8 of Masajada, Fellous-Asiani, and Streltsov.

## Assumptions and scope
The channel convention is the one used in arXiv:2506.06089v1:
\[
K_0=\sqrt{1-n}\,\operatorname{diag}(1,\sqrt{1-\gamma}),\qquad
K_1=\sqrt{1-n}\begin{pmatrix}0&\sqrt\gamma\\0&0\end{pmatrix},
\]
\[
K_2=\sqrt n\,\operatorname{diag}(\sqrt{1-\gamma},1),\qquad
K_3=\sqrt n\begin{pmatrix}0&0\\\sqrt\gamma&0\end{pmatrix}.
\]
A two-qubit channel is entanglement-annihilating here if its output is separable across the two output qubits for every two-qubit input state. The theorem concerns two identical copies of this channel. It does not assert an analogous criterion for two different generalized amplitude-damping channels.

## Proof
Put \(q=n(1-n)\). On diagonal density matrices, \(\mathcal G_{\gamma,n}\) acts through the positive transition matrix
\[
M=\begin{pmatrix}
1-n\gamma &(1-n)\gamma\\
n\gamma&1-(1-n)\gamma
\end{pmatrix}.
\]
Assume first \(0<n<1\) and \(0<\gamma<1\). Positive invertible diagonal input and output filters can scale \(M\) to a doubly stochastic matrix. Applying the same filters to the full completely positive map produces a trace-preserving unital qubit channel \(\mathcal U\). Because the input filter is an invertible local map of the positive cone and the output filter is an invertible local filter, separability is preserved in both directions. Hence
\[
\mathcal G_{\gamma,n}^{\otimes2}\text{ is entanglement-annihilating}
\quad\Longleftrightarrow\quad
\mathcal U^{\otimes2}\text{ is entanglement-annihilating}.
\]

Set
\[
R=\sqrt{(1-n\gamma)(1-(1-n)\gamma)}
 =\sqrt{1-\gamma+\gamma^2q}.
\]
The doubly stochastic diagonal action has the form
\[
\begin{pmatrix}u&1-u\\1-u&u\end{pmatrix}.
\]
Diagonal scaling preserves the cross-ratio of the four transition probabilities, so
\[
\frac{u}{1-u}=\frac{R}{\gamma\sqrt q}.
\]
The original channel multiplies both coherences by \(\sqrt{1-\gamma}\). From the product of the two scaled off-diagonal transition entries, the transverse Bloch multiplier of \(\mathcal U\) is
\[
\lambda=\frac{\sqrt{1-\gamma}}{R+\gamma\sqrt q}.
\]
The longitudinal multiplier is
\[
2u-1=\frac{R-\gamma\sqrt q}{R+\gamma\sqrt q}=\lambda^2,
\]
where the last equality uses \(R^2-\gamma^2q=1-\gamma\). Thus the Bloch singular values of \(\mathcal U\) are \((\lambda,\lambda,\lambda^2)\).

Filippov, Rybár, and Ziman proved that a unital qubit channel with Bloch singular values \((\lambda_1,\lambda_2,\lambda_3)\) has an entanglement-annihilating tensor square exactly when
\[
\lambda_1^2+\lambda_2^2+\lambda_3^2\leq1.
\]
For the present representative this becomes
\[
2\lambda^2+\lambda^4\leq1,
\]
which is equivalent to \(\lambda^2\leq\sqrt2-1\). Substituting the expression above and using \(R\geq0\) gives
\[
R\leq(1+\sqrt2)\gamma\sqrt q.
\]
Squaring and using \(R^2=1-\gamma+\gamma^2q\) yields exactly
\[
2(1+\sqrt2)q\gamma^2+\gamma-1\geq0.
\]

It remains to identify this condition with the singlet test. A direct application of \(\mathcal G_{\gamma,n}^{\otimes2}\) to \(|\Psi^-\rangle\langle\Psi^-|\), followed by partial transposition, leaves one potentially negative \(2\times2\) block. Its determinant has the same sign as
\[
\left(q\gamma^2+\frac{\sqrt2-1}{2}(\gamma-1)\right)
\left(q\gamma^2-\frac{\sqrt2+1}{2}\gamma+\frac{\sqrt2+1}{2}\right).
\]
The second factor is nonnegative on \(0\leq q\leq1/4\) and \(0\leq\gamma\leq1\): it decreases in \(\gamma\) there and its value at \(\gamma=1\) is \(q\). Therefore the singlet output is PPT, hence separable for two qubits, exactly when
\[
q\gamma^2+\frac{\sqrt2-1}{2}(\gamma-1)\geq0,
\]
which is the same inequality as above after multiplication by \(2(1+\sqrt2)\).

For \(n=0\) or \(n=1\), the criterion reduces to \(\gamma=1\), agreeing with the limiting argument and with the fact that only complete amplitude damping annihilates all two-qubit entanglement in that zero-temperature endpoint. At \(\gamma=0\) the channel is the identity and is not entanglement-annihilating; at \(\gamma=1\) it is a constant-output thermal channel and is entanglement-annihilating. Solving the quadratic for \(0<n<1\) gives the stated closed form for \(\gamma_{\mathrm{EA}}(n)\).

## Verification
The proof has two independent exact routes to the same boundary: diagonal Sinkhorn reduction followed by the unital tensor-square criterion, and a direct two-qubit PPT calculation on the singlet. The algebraic identity
\[
(R-\gamma\sqrt q)(R+\gamma\sqrt q)=1-\gamma
\]
is the critical consistency check linking the transverse and longitudinal multipliers. The endpoint cases \(n\in\{0,1\}\), \(n=1/2\), \(\gamma=0\), and \(\gamma=1\) agree with the known amplitude-damping and unital limits. No finite sampling or numerical optimizer is used to establish the universal quantifiers.

## Relationship to prior work
Masajada, Fellous-Asiani, and Streltsov formulated the singlet criterion as Numerical Conjecture 8 and supported it with a fine parameter scan and semidefinite optimization. Filippov, Rybár, and Ziman had earlier found the generalized amplitude-damping boundary numerically and proved the exact tensor-square criterion for unital qubit channels, but did not analytically bridge the nonunital generalized amplitude-damping family to that criterion. Gonzalez later proved a general implication from parallel entanglement annihilation to entanglement breaking of a sequential composition; that implication does not supply the converse needed here. The present diagonal-filter reduction supplies the missing analytic bridge and gives the exact closed form.

## Limitations
The result is restricted to two identical generalized amplitude-damping qubit channels and two-qubit inputs. It does not characterize asymmetric products \(\mathcal G_{\gamma_1,n_1}\otimes\mathcal G_{\gamma_2,n_2}\), higher local dimensions, or multipartite entanglement annihilation. The originality comparison cannot exclude an equivalent formulation buried under remote quantum-Sinkhorn or cone-preserver terminology, although the directly relevant sources inspected do not state this theorem.

## References
1. P. Masajada, M. Fellous-Asiani, and A. Streltsov, “Optimizing entanglement distribution via noisy quantum channels,” arXiv:2506.06089v1 (2025).
2. S. N. Filippov, T. Rybár, and M. Ziman, “Local two-qubit entanglement-annihilating channels,” arXiv:1110.3757v1; Phys. Rev. A 85, 012303 (2012), DOI:10.1103/PhysRevA.85.012303.
3. D. Gonzalez, “Feasibility Ordering of Entanglement-Source Placement for Qubit Channels,” arXiv:2609.18803v1 (2026).
4. V. Sargolzahi, “Entanglement increase from local interactions which lead to non-positive local reduced dynamics,” arXiv:2605.08923v1 (2026).
