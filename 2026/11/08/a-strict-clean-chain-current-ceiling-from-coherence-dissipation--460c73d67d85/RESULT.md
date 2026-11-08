# A strict clean-chain current ceiling from coherence dissipation in tilted quantum transport

## Finding

A spatial tilt cannot improve the stationary particle current of the boundary-driven, uniformly dephased nearest-neighbor chain **relative to its untilted counterpart at the same dephasing rate**. For every finite chain length and every real tilt, the current deficit obeys an exact nonnegative-coherence identity. This is an all-size, nonperturbative statement, not a tridiagonal approximation.

Define the clean-chain current
\[
 j_0=\left[\frac2\Gamma+\frac{\gamma(N-1)+\Gamma}{2t^2}\right]^{-1}.
\]
If \(X\) is the unit-driving stationary correlation response and \(j=2t\operatorname{Im}X_{k,k+1}\), then
\[
\boxed{j\left(1-\frac j{j_0}\right)=\mathcal E(X)},\qquad
\boxed{0<j\le j_0}.
\]
The excess coherence energy is
\[
\mathcal E(X)=2\sum_{1\le a<b\le N}w_{ab}\left[
(\operatorname{Re}X_{ab})^2+
\mathbf1_{b>a+1}(\operatorname{Im}X_{ab})^2\right],
\]
where \(w_{ab}=\gamma+\frac\Gamma2(\mathbf1_{a\in\{1,N\}}+\mathbf1_{b\in\{1,N\}})>0\).
Equality \(j=j_0\) holds if and only if all onsite energies are equal. Thus for the linear potential \(v_k=v_0+(k-1)U\), it holds precisely at \(U=0\).

## Assumptions and scope

Let \(N\ge2\) be any integer, \(t,\Gamma,\gamma>0\), and \(v_1,\ldots,v_N\in\mathbb R\). Define the Hermitian single-particle Hamiltonian
\[
H=\sum_{k=1}^N v_k|k\rangle\langle k|+
 t\sum_{k=1}^{N-1}(|k\rangle\langle k+1|+|k+1\rangle\langle k|).
\]
Write \(p_k=\mathbf1_{k\in\{1,N\}}\) and define the dissipative response operator entrywise by
\[
\mathcal D(X)_{ab}=\left[\gamma\mathbf1_{a\ne b}+\frac\Gamma2(p_a+p_b)\right]X_{ab}.
\]
The physical boundary occupations are \((1+f)/2\) and \((1-f)/2\), where \(-1\le f\le1\). Their stationary covariance is \(C=I/2+fX\) and \(X=X^\dagger\) is the unique solution of
\[
\mathcal D(X)+i[H,X]=\frac\Gamma2(|1\rangle\langle1|-|N\rangle\langle N|).
\]
Here \(\gamma\) denotes the decay coefficient of **off-diagonal single-particle coherences**. If the physical local Lindblad operator is \(L_k=\sqrt{\gamma_{\rm bath}/2}\,\sigma_k^z\), then \(\gamma=2\gamma_{\rm bath}\); Hamiltonian hopping must also be converted into the same single-particle convention. The right-moving particle current is \(f\,j\) with \(j=2t\operatorname{Im}X_{k,k+1}\). Other spin-current conventions differ by fixed factors. The bound compares tilt strengths **at fixed** \(N,t,\Gamma,\gamma\); it does not compare different dephasing rates.

## Proof

**Step 1: existence and uniqueness of the response.** On Hermitian matrices use the real Hilbert–Schmidt pairing \(\langle A,B\rangle=\operatorname{tr}(AB)\). The commutator contribution \(\langle Z,i[H,Z]\rangle=0\). If the homogeneous response equation holds, then
\[
0=\langle Z,\mathcal D(Z)\rangle=\Gamma(Z_{11}^2+Z_{NN}^2)+2\sum_{a<b}w_{ab}|Z_{ab}|^2.
\]
Strict positivity of all off-diagonal weights forces the off-diagonal entries and both boundary diagonals to vanish. The remaining commutator equations on bonds force all diagonal values equal (since \(t>0\)); the boundary value zero forces \(Z=0\). Thus the finite linear operator is invertible, and a unique Hermitian solution exists.

**Step 2: current conservation and boundary response.** Diagonal entries of the response equation give a bond-independent current
\[
 j=2t\operatorname{Im}X_{k,k+1},\quad
 X_{11}=\frac12-\frac j\Gamma,\quad
 X_{NN}=-\frac12+\frac j\Gamma.
\]
No approximation to the longer-range coherences is involved.

**Step 3: exact dissipation balance.** Pair the inhomogeneous equation with \(X\) to eliminate the Hamiltonian commutator exactly. The source pairing is \(\Gamma/2-j\). The dissipation pairing decomposes as
\[
\langle X,\mathcal D(X)\rangle=
2\Gamma\left(\frac12-\frac j\Gamma\right)^2+
\frac{\gamma(N-1)+\Gamma}{2t^2}j^2+\mathcal E(X),
\]
since every nearest-neighbor imaginary coherence equals \(j/(2t)\), whereas all remaining off-diagonal contributions form \(\mathcal E(X)\). Equating the two sides and simplifying gives
\[
 \mathcal E(X)=j-\left(\frac2\Gamma+\frac{\gamma(N-1)+\Gamma}{2t^2}\right)j^2=j\left(1-\frac j{j_0}\right).
\]

**Step 4: strict positivity.** Since \(\mathcal E(X)\ge0\) and \(j_0>0\), the identity forces \(j(1-j/j_0)\ge0\), which is equivalent to \(0\le j\le j_0\). If \(j=0\), then \(\mathcal E(X)=0\), all off-diagonal entries vanish, and the bond equations force all site diagonals equal, contradicting \(X_{11}=1/2\) and \(X_{NN}=-1/2\). Therefore \(j>0\).

**Step 5: characterize equality.** Equality \(j=j_0\) is equivalent to \(\mathcal E(X)=0\). Then every nearest-neighbor coherence is purely imaginary and every longer-range coherence vanishes. Taking the *real part* of the nearest-neighbor response equation gives
\[
 (v_k-v_{k+1})\,\operatorname{Im}X_{k,k+1}=0
\]
(the other real terms vanish by the just-stated coherence restrictions). Since \(\operatorname{Im}X_{k,k+1}=j/(2t)>0\), all \(v_k\) must coincide.

**Step 6: attainability for constant potentials.** For any constant \(v_k=v_0\), construct a Hermitian matrix by setting \(X_{11}=1/2-j_0/\Gamma\), \(X_{NN}=-1/2+j_0/\Gamma\), \(X_{k,k+1}=ij_0/(2t)\), and all longer-range entries to zero. Set the interior diagonal sequence by
\[
X_{k+1,k+1}-X_{kk}=-\frac{w_{k,k+1}}{2t^2}j_0.
\]
The definition of \(j_0\) makes the right-end diagonal consistent. The diagonal, adjacent, and more-distant stationary equations now all hold; the more-distant commutator terms cancel between the two equal imaginary bond coherences. Uniqueness identifies this with the stationary solution, giving \(j=j_0\). For a linear potential, constancy means \(U=0\), and the theorem follows.

## Verification

Run `python checks/coherence_current.py` with Python, NumPy, and SymPy. The program builds the complete \(N^2\)-dimensional Hermitian linear equation independently from the formulas above, solves nine exact rational small-chain systems (all algebraic residual identities exact) and checks 120 additional randomized finite-matrix cases at sizes two through seven. Expected output: `PASS 9 exact rational identities and 120 randomized matrix diagnostics; total 129`.

As a small exact example, for \(N=3\), \(t=\Gamma=\gamma=1\), and onsite energies \((0,1,2)\), the response gives \(j=6/25<j_0=2/7\) and \(\mathcal E=24/625\). For \(N=4\) with the same rates and energies \((0,1,2,3)\), the exact response has \(j=3262/16791<j_0=1/4\) and a nonzero next-nearest-neighbor element \(X_{13}=(-80+94i)/16791\), demonstrating that the all-size statement retains coherences discarded by the tridiagonal approximation.

The code checks current continuity, the exact dissipation identity, positivity and the sharp clean bound. These are finite reproducibility diagnostics, **not** the proof for arbitrary chain length or real parameters, which is provided above by the Hilbert–Schmidt argument.

## Relationship to prior work

Jacob et al., arXiv:2407.21715, define the same tilted boundary-driven XX setting, report exact current expressions for chains of length two and three, and derive a tridiagonal approximation and numerical comparisons for larger lengths (Sections 4–5 and Supplementary Section 7). The exact zero-tilt baseline is already known there; it is **not claimed as new**. The result here is the global all-size strict comparison at *fixed dephasing*, with the exact positive excess-coherence certificate, for which no matching proof was identified in that full text.

Žnidarič and Horvat, arXiv:1207.5952, already give the general onsite-disorder correlation-matrix equations and disorder/dephasing transport phenomenology. Their equations are the starting point of this deduction; the equation system is **not** new. The current upper-bound/equality theorem and decomposition into a nonnegative weighted coherence sum were not identified as conclusions of their article. Žnidarič, arXiv:1005.1271, supplies the exact dephased clean-chain steady current, also credited here. A previously published equivalent general energy inequality would supersede the claimed novelty even without matching this wording; publication priority still needs independent literature assessment.

## Limitations

This is a finite-chain, noninteracting, nearest-neighbor, two-reservoir, equal-boundary-coupling and strictly positive uniform-dephasing theorem. It does **not** assert that increasing dephasing at fixed nonzero tilt always decreases current; noise-assisted recovery from Wannier–Stark localization can occur without crossing the no-tilt ceiling. It does not cover zero dephasing, interactions, coherent long-range hopping, unequal boundary couplings or externally different source-and-sink protocols. The stronger arbitrary-onsite-profile lemma is used to prove and contextualize the linear-tilt claim. No independence or formal external certification is asserted.

## References

1. S. L. Jacob, L. P. Bettmann, A. M. Lacerda, K. Zawadzki, S. R. Clark, J. Goold, J. J. Mendoza-Arenas, *Dephasing-assisted transport in a tight-binding chain with a linear potential*, arXiv:2407.21715, first posted 2024-07-31. https://arxiv.org/abs/2407.21715
2. M. Žnidarič and M. Horvat, *Transport in a disordered tight-binding chain with dephasing*, arXiv:1207.5952, first posted 2012-07-25. https://arxiv.org/abs/1207.5952
3. M. Žnidarič, *Exact solution for a diffusive nonequilibrium steady state of an open quantum chain*, arXiv:1005.1271, first posted 2010-05-07. https://arxiv.org/abs/1005.1271
