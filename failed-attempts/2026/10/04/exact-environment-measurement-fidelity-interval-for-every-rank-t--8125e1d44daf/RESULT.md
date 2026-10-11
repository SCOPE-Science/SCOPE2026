# Exact environment-measurement fidelity interval for every rank-two qubit channel

## Finding

Let \(\Phi:M_2\to M_2\) be a trace-preserving qubit channel of Kraus rank exactly \(2\). Choose a minimal Kraus pair
\[
A_0,\quad A_1.
\]
For \(z=(z_0,z_1)^{\mathsf T}\in\mathbb C^2\), define
\[
q_\Phi(z_0,z_1)=\det(z_0A_0+z_1A_1)=z^{\mathsf T}Mz,
\]
where \(M\) is complex symmetric. Let
\[
s_1\ge s_2\ge0
\]
be its Takagi singular values. A different minimal Kraus pair changes \(M\) by unitary congruence, so \(s_1,s_2\) are channel invariants.

For any finite Kraus representation
\[
\Phi(\rho)=\sum_k B_k\rho B_k^\dagger
\]
and the optimal outcome-dependent unitary correction of Gregoratti--Werner,
\[
F_{\mathrm{corr}}(\{B_k\})
=
\frac12+\frac12\sum_k|\det B_k|.
\]
As the finite Kraus representation varies, the complete attainable fidelity set is
\[
\boxed{
\left[
\frac{1+s_1-s_2}{2},
\frac{1+s_1+s_2}{2}
\right].
}
\]
Both endpoints are attained with two outcomes, and every intermediate value is attained by a continuous two-outcome family.

Consequently, the optimally corrected fidelity is independent of the finite rank-one environment measurement exactly when
\[
\boxed{s_2=0,}
\]
equivalently when the determinant quadratic form has rank at most one.

For amplitude damping with damping probability \(p\in[0,1)\), take
\[
A_0=
\begin{pmatrix}
1&0\\
0&\sqrt{1-p}
\end{pmatrix},
\qquad
A_1=
\begin{pmatrix}
0&\sqrt p\\
0&0
\end{pmatrix}.
\]
Then
\[
q_\Phi(z_0,z_1)=\sqrt{1-p}\,z_0^2,
\]
so every finite rank-one environment measurement has the same optimal corrected fidelity
\[
F_{\mathrm{corr}}=\frac{1+\sqrt{1-p}}{2}.
\]

For the rank-two dephasing channel
\[
A_0=\sqrt p\,I,
\qquad
A_1=\sqrt{1-p}\,Z,
\qquad
0<p<1,
\]
the determinant form is
\[
q_\Phi(z_0,z_1)=p z_0^2-(1-p)z_1^2.
\]
Thus
\[
s_1=\max(p,1-p),
\qquad
s_2=\min(p,1-p),
\]
and the complete attainable interval is
\[
\boxed{[\max(p,1-p),1].}
\]
The canonical random-unitary decomposition attains perfect correction, while a different two-outcome environment basis attains the lower endpoint.

## Assumptions and scope

The system is a single qubit and the channel has minimal Kraus rank exactly \(2\). The figure of merit is the channel fidelity used by Gregoratti and Werner, equivalently entanglement fidelity for the maximally mixed qubit input. After each environment outcome, an outcome-dependent unitary is chosen optimally for that fixed Kraus branch.

A finite Kraus representation is equivalent, after a finite Naimark dilation when needed, to a finite rank-one measurement on a Stinespring environment. The theorem concerns this refined measurement class. Deliberate coarse-graining that discards an available environment label is outside the parametrization unless it is refined to its Kraus outcomes.

Higher Kraus rank, higher system dimension, nonunitary conditional recovery maps, and other fidelity objectives are outside the claim.

## Proof

For a fixed Kraus representation \(\{B_k\}\), Gregoratti and Werner show that the optimal conditional correction is obtained from the polar decomposition of each \(B_k\), with
\[
F_{\mathrm{corr}}(\{B_k\})
=
\frac14\sum_k\left(\operatorname{tr}|B_k|\right)^2.
\]
For every \(2\times2\) matrix \(B\),
\[
\left(\operatorname{tr}|B|\right)^2
=
\operatorname{tr}(B^\dagger B)+2|\det B|.
\]
Trace preservation gives
\[
\sum_kB_k^\dagger B_k=I,
\]
hence
\[
F_{\mathrm{corr}}(\{B_k\})
=
\frac12+\frac12\sum_k|\det B_k|.
\]

Fix a minimal Kraus pair \(A_0,A_1\). Every finite Kraus representation can be written
\[
B_k=v_{k0}A_0+v_{k1}A_1,
\]
where \(V=(v_{kj})\) is an isometry:
\[
V^\dagger V=I_2.
\]
The determinant is a homogeneous quadratic form
\[
\det(z_0A_0+z_1A_1)=z^{\mathsf T}Mz.
\]
By Takagi factorization, after a unitary change of minimal Kraus basis,
\[
M=
\begin{pmatrix}
s_1&0\\
0&s_2
\end{pmatrix}.
\]
Write the two orthonormal columns of \(V\) as
\[
x=(x_k)_k,\qquad y=(y_k)_k.
\]
Then
\[
\det B_k=s_1x_k^2+s_2y_k^2,
\]
with
\[
\sum_k|x_k|^2=\sum_k|y_k|^2=1.
\]

The triangle inequality gives
\[
\sum_k|\det B_k|
\le s_1+s_2.
\]
The reverse triangle inequality gives
\[
|s_1x_k^2+s_2y_k^2|
\ge s_1|x_k|^2-s_2|y_k|^2,
\]
so after summing,
\[
\sum_k|\det B_k|
\ge s_1-s_2.
\]
Therefore
\[
\frac{1+s_1-s_2}{2}
\le F_{\mathrm{corr}}
\le
\frac{1+s_1+s_2}{2}.
\]

The identity mixing attains the upper endpoint. The unitary
\[
V_{\pi/4}
=
\frac1{\sqrt2}
\begin{pmatrix}
1&i\\
i&1
\end{pmatrix}
\]
in the Takagi Kraus basis gives determinants
\[
\frac{s_1-s_2}{2},
\qquad
\frac{s_2-s_1}{2},
\]
and therefore attains the lower endpoint.

More generally,
\[
V_\theta
=
\begin{pmatrix}
\cos\theta&i\sin\theta\\
i\sin\theta&\cos\theta
\end{pmatrix},
\qquad
0\le\theta\le\frac{\pi}{4},
\]
is unitary. Its determinant sum depends continuously on \(\theta\), starts at \(s_1+s_2\), and ends at \(s_1-s_2\). The sharp bounds exclude values outside this interval, so the intermediate-value theorem gives the full interval.

The interval collapses exactly when \(s_2=0\). The amplitude-damping and dephasing formulas follow by direct determinant calculation.

## Verification

`verify_rank2_feedback.py` uses only the Python standard library. It verifies the amplitude-damping and dephasing specializations, constructs deterministic random rank-two qubit channels from random \(4\times2\) Stinespring isometries, computes the determinant quadratic matrix, and extracts its two singular values from \(M^\dagger M\).

For each sampled channel it verifies invariance of those singular values under random unitary changes of minimal Kraus pair. It then samples finite Kraus refinements with two through six outcomes and checks
\[
s_1-s_2
\le
\sum_k|\det B_k|
\le
s_1+s_2.
\]
The finite checks are supplementary; the all-channel theorem is proved above.

## Relationship to prior work

Gregoratti and Werner formulate environment-assisted correction using an observed Kraus decomposition and solve the optimal recovery problem for a fixed decomposition. Their Proposition 4 gives the polar-decomposition correction, and their qubit discussion uses
\[
(\operatorname{tr}|A|)^2
=
\operatorname{tr}|A|^2+2|\det A|.
\]
The inspected text does not characterize the full range obtained by varying the environment measurement for an arbitrary rank-two qubit channel.

Uhlmann develops determinant and concurrence structures for rank-two channels, including quadratic forms associated with two-dimensional Kraus spaces. That work is close algebraically, but the inspected full text does not state the environment-measurement fidelity interval or the measurement-independence criterion above.

Memarzadeh, Cafaro, and Mancini study environment-measurement choice for the qubit amplitude-damping channel. They prove invariance for all two-Kraus decompositions and report numerical agreement for three- and four-outcome decompositions. The present theorem explains that phenomenon structurally: amplitude damping has
\[
s_2=0,
\]
so every finite rank-one measurement gives the same value. Dephasing shows that such invariance is not generic.

Targeted searches combining rank-two qubit channels, Kraus determinants, environment measurements, feedback correction, Takagi factorization, and entanglement fidelity did not locate the displayed exact interval or iff criterion.

## Limitations

The proof uses a qubit-specific determinant identity. Higher-dimensional corrected fidelity depends on a richer singular-value structure.

The theorem concerns finite rank-one environment measurements. It does not claim that deliberately coarse-graining outcomes cannot lower performance further when the receiver is denied the refinement label.

A residual literature risk remains because determinant quadratic forms and Takagi factorization are standard in rank-two concurrence theory. An equivalent interval statement may exist under concurrence-of-assistance or channel-correction terminology not surfaced by the searches.

## References

1. M. Gregoratti and R. F. Werner, “On quantum error-correction by classical feedback in discrete time,” *Journal of Mathematical Physics* 45 (2004), 2600–2612, arXiv:quant-ph/0403092, DOI: 10.1063/1.1758320.
2. A. Uhlmann, “On Concurrence and Entanglement of Rank Two Channels,” *Open Systems & Information Dynamics* 12 (2005), 397–428, arXiv:quant-ph/0605103, DOI: 10.1007/s11080-005-0490-6.
3. L. Memarzadeh, C. Cafaro, and S. Mancini, “Quantum information reclaiming after amplitude damping,” *Journal of Physics A: Mathematical and Theoretical* 44 (2011), 045304, arXiv:1004.0497, DOI: 10.1088/1751-8113/44/4/045304.
