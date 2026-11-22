# Exact bipartition-dependent PPT windows for a reset-noisy four-qubit Dicke state

## Finding

A continuously depolarized four-qubit two-excitation Dicke state, replenished by complete Poisson resetting to the same pure state, exhibits a sharp cut-dependent stationary partial-transpose transition. In units \(x=r/\gamma\), put \(Q=(x+2)(x+4)\). For every positive \(x\), the negativity (sum of the moduli of strictly negative partial-transpose eigenvalues) is
\[
\begin{aligned}
\mathcal N_{1|3}(x)&=\left[\frac{2x-1}{4(x+4)}\right]_++2\left[\frac{x-6}{12Q}\right]_+,\\
\mathcal N_{2|2}(x)&=2\left[\frac{4x^2+7x-6}{12Q}\right]_++\left[\frac{(x-1)(x+3)}{6Q}\right]_+.
\end{aligned}
\]
The operation \([a]_+\) denotes \(\max\{a,0\}\). Accordingly, every one-versus-three cut is NPT exactly for \(x>1/2\), and every two-versus-two cut is NPT exactly for
\[
x>\beta=\frac{\sqrt{145}-7}{8}.
\]
Since \(\beta>1/2\), the entire interval \(1/2<x\le\beta\) has NPT on every one-versus-three cut while retaining PPT on every two-versus-two cut. The respective counts of strictly negative partial-transpose eigenvalues change from \(0\) to \(1\) at \(x=1/2\) and to \(3\) at \(x=6\), and from \(0\) to \(2\) at \(x=\beta\) and to \(3\) at \(x=1\).

## Assumptions and scope

Use distinguishable qubits and the computational basis. The initial pure state is
\[
|D_4^{(2)}\rangle=\frac{|0011\rangle+|0101\rangle+|0110\rangle+|1001\rangle+|1010\rangle+|1100\rangle}{\sqrt6}.
\]
Each qubit evolves independently under the isotropic, unital depolarizing semigroup \(\mathcal D_t(A)=e^{-\gamma t}A+(1-e^{-\gamma t})\operatorname{tr}(A)I/2\), at the same \(\gamma>0\). A Poisson clock of rate \(r>0\) replaces *all four* qubits by the pure initial state, independent of the state immediately before resetting. There are no Hamiltonian terms, correlations between noise channels, measurement selection, or imperfect reset. The unique stationary density operator is
\[
\rho_x=r\int_0^\infty e^{-rt}\mathcal D_t^{\otimes4}(|D_4^{(2)}\rangle\langle D_4^{(2)}|)\,dt,
\qquad x=r/\gamma>0.
\]
Partial transpose is defined in the computational basis on a specified subset of qubits. Positivity of partial transpose (PPT) is a spectral property, not a sufficient separability characterization in these bipartite dimensions. Permutation invariance gives identical results for each partition of the same size.

## Proof

**1. Stationary reduction.** On every traceless one-qubit Pauli operator, the local channel multiplies by \(e^{-\gamma t}\). Thus a four-qubit Pauli string with \(j\) nonidentity factors is multiplied by \(e^{-j\gamma t}\). The renewal-age integral multiplies this coefficient by \(x/(x+j)\), while preserving the identity coefficient. In particular, the resolvent state solves the stationary generator equation
\[
\sum_{k=1}^4\gamma\big(\operatorname{tr}_k\rho_x\otimes I_k/2-\rho_x\big)+r\big(|D\rangle\langle D|-\rho_x\big)=0.
\]
The positive reset rate makes the stationary solution unique by contraction of the associated quantum Markov semigroup. The integral also proves state positivity and trace normalization. Expanding the four local channels as degree-four polynomials in \(z=e^{-\gamma t}\) and integrating their coefficients with weights \(x/(x+j)\) produces an explicit rational \(16\times16\) matrix. The provided code evaluates it exactly by interpolation and verifies the generator equation symbolically.

**2. Full one-versus-three transpose spectrum.** Define \(a=\sqrt{9x^2+60x+112}\). Direct exact characteristic-polynomial factorization on its five invariant coordinate blocks yields the following entire multiset of eigenvalues; each superscript in parentheses is the eigenvalue multiplicity:
\[
\begin{gathered}
\left(\frac{x+3}{6Q}\right)^{(4)},\quad
\left(\frac{3x^2+10x+6-xa}{12Q}\right)^{(2)},\quad
\left(\frac{3x^2+10x+6+xa}{12Q}\right)^{(2)},\\
\left(\frac{1-2x}{4(x+4)}\right)^{(1)},\quad
\left(\frac{1}{4(x+4)}\right)^{(4)},\quad
\left(\frac{6x^2+23x+6}{12Q}\right)^{(1)},\quad
\left(\frac{6-x}{12Q}\right)^{(2)}.
\end{gathered}
\]
All terms except possibly the last and the \(1-2x\) term are strictly positive because all denominators are positive and
\[
(3x^2+10x+6)^2-x^2(9x^2+60x+112)=12(2x^2+10x+3)>0.
\]
Therefore exactly the two displayed rational branches can become negative, at \(x=1/2\) and \(x=6\) respectively.

**3. Full two-versus-two transpose spectrum.** Let \(b=\sqrt{3x^2+20x+44}\). The corresponding five coordinate blocks have eigenvalue multiset
\[
\begin{gathered}
\left(\frac{1}{2Q}\right)^{(1)},\quad
\left(\frac{(1-x)(x+3)}{6Q}\right)^{(1)},\quad
\left(\frac{2x+3}{6Q}\right)^{(2)},\\
\left(\frac{5x^2+14x+6-\sqrt3 xb}{12Q}\right)^{(1)},\quad
\left(\frac{5x^2+14x+6+\sqrt3 xb}{12Q}\right)^{(1)},\\
\left(\frac{4x^2+17x+6}{12Q}\right)^{(2)},\quad
\left(\frac{6-7x-4x^2}{12Q}\right)^{(2)},\quad
\left(\frac{x+6}{12Q}\right)^{(4)},\quad
\left(\frac{(x+1)(x+3)}{6Q}\right)^{(2)}.
\end{gathered}
\]
The radicand pair remains positive because
\[
(5x^2+14x+6)^2-3x^2(3x^2+20x+44)=4(4x^4+20x^3+31x^2+42x+9)>0.
\]
Hence only \((1-x)(x+3)/(6Q)\) and \((6-7x-4x^2)/(12Q)\) may be negative. The latter has the unique positive zero \(\beta=(\sqrt{145}-7)/8\), with \(1/2<\beta<1\). Multiplicities yield exactly the two stated negativity formulas and inertia transitions.

**4. Reproducibility and physical limits.** When \(x\downarrow0\), the semigroup equilibrates to the maximally mixed state and both negativities vanish. As \(x\to\infty\), the stationary state converges to the pure Dicke projector, and the exact formulas give the known Schmidt-pure-state negativities \(1/2\) and \(5/6\). These checks fix the convention for negativity and guard against factor-of-two normalization errors.

## Verification

Run `python3 checker.py` with Python 3, SymPy and NumPy. The code constructs the noisy state afresh from the six computational-basis Dicke components, applies independent local depolarizing maps, interpolates the exact degree-four channel polynomial, integrates each coefficient, and verifies the stationary generator equation exactly. It computes characteristic polynomials of all ten noninteracting partial-transpose coordinate blocks and checks equality with the displayed exact eigenvalue factors. Independent numerical Hermitian eigenspectra at thirteen positive rational reset-to-noise ratios reproduce every eigenvalue with the indicated multiplicity. The checker reports 429 finite component checks and ten symbolic block factorizations; those finite numerical checks are not substitutes for the exact all-rate algebraic inequalities.

## Relationship to prior work

Chen and Jiang (2020), *Noise tolerance of Dicke states*, primarily derive entanglement-witness and separation criteria for Dicke states mixed with white noise and discuss amplitude-damped/dephased Dicke states and locally depolarized W states. Their publisher abstract is available, but the full paper could not be accessed during this comparison; implicit coverage by its more general four-qubit criteria is a residual risk. The 2009 work of Campbell, Tame, and Paternostro develops multipartite Dicke entanglement witnesses under local noise, including depolarizing channels, but does not in the material inspected treat the exponential-reset-age stationary mixture or the complete cut-specific partial-transpose spectra. The full publisher and archived open text of Nawareg (2025), on noisy Dicke states, treat a *single white-noise admixture parameter* rather than the four independently attenuated Pauli-weight sectors produced by the present resetting protocol. Kulkarni and Majumdar (2023) provide the general exponential Poisson-reset resolvent for quantum systems and a two-qubit coherently evolving example; the resetting formalism itself is not new. A separately published two-excitation Dicke Pauli-spectrum result treats static Pauli magnitudes and Rényi crossover without noisy-reset stationary PPT cuts. An independently published global-reset two-qubit bit-flip result concerns interacting pairs reset to a product state, not a balanced Dicke state. Neither implies the present specific cut-resolved inertia thresholds merely by changing parameters.

## Limitations

PPT of a balanced cut is not a separability guarantee, and the theorem makes no assertion of genuine multipartite entanglement classification or distillability from the PPT data alone. It applies only to the four-qubit balanced Dicke state with identical local isotropic depolarization and simultaneous perfect Poisson re-preparation; it does not cover arbitrary Dicke sizes, correlated noise, partial resetting, other Lindblad generators, or experimental finite-sample thresholds. Numerical replication supplements, rather than proves, the symbolic spectra. Independent publication-priority evaluation and independent scientific audit have not been performed; highly relevant full text from Chen and Jiang was not accessible, and stronger general results may implicitly contain the classification.

## References

1. X.-Y. Chen and L.-Z. Jiang, *Noise tolerance of Dicke states*, Physical Review A 101, 012308 (2020), DOI: https://doi.org/10.1103/PhysRevA.101.012308 (published 2020-01-09).
2. M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, arXiv:2307.07485 (first posted 2023-07-14), https://arxiv.org/html/2307.07485v2.
3. M. Nawareg, *Entropic analysis of non-separability in noisy Dicke states*, Quantum Information Processing (2025), DOI: https://doi.org/10.1007/s11128-025-04994-1.
4. S. Campbell, M. S. Tame, and M. Paternostro, *Characterizing multipartite symmetric Dicke states under the effects of noise*, New Journal of Physics 11, 073039 (2009), https://arxiv.org/abs/0903.3939.
5. *Three-sector Rényi crossover in the two-excitation Dicke Pauli spectrum*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-three-sector-r-nyi-crossover-in-the-two-excitation-dicke-pauli-s--867c58f80465.
6. *A sharp geometric-mean noise threshold for entanglement under global quantum resetting*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-geometric-mean-noise-threshold-for-entanglement-under-gl--25a4a404999e.
