# Thirteen Erlang stages preserve quantum purity–overlap order; fourteen can reverse it

## Finding

Let a finite-dimensional quantum system evolve unitarily under a time-independent Hermitian Hamiltonian and be completely reset to a fixed density operator at independent Erlang waiting times with integer shape \(n\). Its stationary ensemble density operator \(\rho_*\) has purity \(P=\operatorname{tr}(\rho_*^2)\) and initial-state Hilbert–Schmidt overlap \(O=\operatorname{tr}(\rho_*\rho_0)\). For every shape \(2\le n\le13\), every stage rate, every Hamiltonian and every reset state,
\[
P\ge O,
\]
with equality if and only if the reset state commutes with the Hamiltonian. Shape \(n=1\) instead gives \(P=O\) for all parameters. At shape \(n=14\), the inequality fails already for an equal-superposition pure qubit: when the Bohr frequency divided by the Erlang stage rate is \(1/\sqrt3\),
\[
P-O=-\frac{40308117}{105226698752}<0.
\]
Hence fourteen stages are the least integer Erlang shape allowing purity to fall below initial-state overlap. For a pure reset state, \(O\) is the standard squared quantum fidelity with the reset vector; for mixed resets it is only a Hilbert–Schmidt overlap, not Uhlmann fidelity.

## Assumptions and scope

Fix a finite dimension \(d\ge2\), Hermitian \(H\), density operator \(\rho_0\), and \(\alpha>0\). Let successive complete resets to \(\rho_0\) be separated by independent sums of \(n\) exponential waiting times of rate \(\alpha\), with integer \(n\ge1\), independent of the quantum evolution. Units retain \(\hbar>0\). The stationary ensemble is the equilibrium renewal-age mixture; no assertion is made about convergence at a synchronized deterministic initial age. Let \(\omega_{jk}=(E_j-E_k)/\hbar\) in any energy eigenbasis; any energy degeneracies are permitted. All claims hold for arbitrary finite \(d\), without a nondegeneracy assumption.

## Proof

Write \(T\) for one Erlang waiting time. Its mean is \(n/\alpha\) and its equilibrium age density is \(w(t)=\Pr(T>t)/(n/\alpha)\), so
\[
\rho_* = \int_0^\infty w(t)e^{-iHt/\hbar}\rho_0e^{iHt/\hbar}\,dt.
\]
For \(z=\omega/\alpha\), Fubini's theorem and the Erlang characteristic function give the Fourier-age multiplier
\[
F_n(z)=\int_0^\infty w(t)e^{i\omega t}\,dt
=\frac{(1-iz)^{-n}-1}{inz},\qquad F_n(0)=1.
\]
The sign convention for the off-diagonal density-matrix factor may conjugate \(F_n\), which leaves the following real expressions unchanged. Directly in an energy eigenbasis,
\[
P-O=\sum_{j<k}2| (\rho_0)_{jk}|^2\bigl(|F_n(z_{jk})|^2-\operatorname{Re}F_n(z_{jk})\bigr).
\]

Define the integer polynomial \(Q_n\) by \(Q_1=0\) and, for \(n\ge2\),
\[
\begin{aligned}
y^2Q_n(y)={}&(1+y)^n+1
-2\sum_{k=0}^{\lfloor n/2\rfloor}(-1)^k{n\choose2k}y^k\\
&-n\sum_{k=0}^{\lfloor(n-1)/2\rfloor}(-1)^k{n\choose2k+1}y^{k+1}.
\end{aligned}
\]
The constant and linear coefficients of the right-hand side vanish identically. Using \((1-iz)^{-n}=(1+iz)^n/(1+z^2)^n\), an exact simplification yields, for \(y=z^2>0\),
\[
|F_n(z)|^2-\operatorname{Re}F_n(z)=\frac{yQ_n(y)}{n^2(1+y)^n}.
\]
For \(n=1\) it is zero, including at \(z=0\) by continuity.

For \(2\le n\le13\), positivity of \(Q_n\) on the entire nonnegative half-line follows from exact rational Bernstein certificates, not sampling. Set \(c_n=1/2\) for \(n\in\{2,3,4,5,6,12,13\}\), and \(c_n=1\) for \(7\le n\le11\). On each consecutive quarter-interval \([j/4,(j+1)/4]\subseteq[0,c_n]\), expand \(Q_n(j/4+t/4)\) in the degree \(n-2\) Bernstein basis for \(0\le t\le1\). Every Bernstein coefficient is strictly positive. On the remaining ray, every ordinary monomial coefficient of \(Q_n(c_n+u)\) is strictly positive for \(u\ge0\). A standalone exact-fraction checker constructs both sets of coefficients for every \(n=2,\ldots,13\) from the displayed binomial formula. Its complete minima of quarter-interval Bernstein coefficients, for ascending \(n=2,\ldots,13\), are
\[
1,\ 6,\ 20,\ 50,\ \frac{6533}{64},\ \frac{401267}{2560},\ \frac{393355}{2048},\ \frac{5695317}{28672},\ \frac{5138977}{28672},\ \frac{1351795}{9216},\ \frac{10749791}{122880},\ \frac{89725453}{5046272}.
\]
The minimum monomial coefficient of every shifted tail is \(1\). The Bernstein-basis partition-of-unity property therefore proves \(Q_n(y)>0\) for all \(y\ge0\). Each nonzero energy-gap coherence contributes strictly positively to \(P-O\), so equality is equivalent to \([H,\rho_0]=0\).

For shape \(14\), direct binomial expansion instead gives
\[
Q_{14}(y)=3185-21658y+43043y^2-24024y^3+7917y^4+3238y^5+3003y^6+2002y^7+1001y^8+364y^9+91y^{10}+14y^{11}+y^{12}.
\]
At \(y=1/3\), \(Q_{14}(1/3)=-13436039/531441\). Therefore the single positive gap of a two-level Hamiltonian with \(\omega/\alpha=1/\sqrt3\), and initial \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt2\), produces exactly
\[
P-O=\tfrac12\bigl(|F_{14}(1/\sqrt3)|^2-\operatorname{Re}F_{14}(1/\sqrt3)\bigr)=-\frac{40308117}{105226698752}.
\]
This exhibits the first possible shape reversal and completes the proof.

## Verification

Run \(\texttt{python3 checker.py}\) with standard Python 3; no external packages are required. The checker reconstructs \(Q_n\) from the binomial identities, checks all rational Bernstein coefficients and all positive shifted-tail coefficients for \(2\le n\le13\), tests the exact shape-14 polynomial and negative rational witness, and independently recomputes the transform identity in exact complex rational arithmetic for 42 shape–frequency pairs. The script reports 356 coefficient and transform checks passing. The integer-stage classification is an exact finite symbolic certificate, not an inference from numerical interpolation or a time-limited search.

## Relationship to prior work

Sevilla and Valdés-Hernández [1] provide a general renewal-time quantum-resetting formalism, explicit gamma-distributed stationary coherence multipliers, and stationary purity and fidelity formulas (especially their equations 27, 34, 42 and 47). Those general formulas determine individual values in this theorem but do not state the exact all-Hamiltonian sign bound for shapes 2 through 13 or the first counterexample at shape 14. Kulkarni and Majumdar [2] study Poisson quantum resetting and fidelity in a two-spin system; the identity at shape one is consistent with their framework and is **not** claimed to be new. The contribution assessed here is precisely the all-dimension, sharp finite-stage positivity threshold and its rational qubit counterexample.

## Limitations

The result only classifies universal order for integer shapes 1 through 14, not all larger shapes or noninteger gamma shapes. It says nothing about a measurement implementation, actual operational advantage, or independence from all unindexed prior literature. Full earlier general renewal formulas make pointwise instances derivable, so the originality claim is restricted to the globally sharp threshold and its nontrivial positivity certificate.

## References

[1] F. J. Sevilla and A. Valdés-Hernández, "Dynamics of closed quantum systems under stochastic resetting," arXiv:2209.05643v1 (12 September 2022), https://arxiv.org/html/2209.05643v1.
[2] M. Kulkarni and S. N. Majumdar, "Generating Entanglement by Quantum Resetting," arXiv:2307.07485v1 (14 July 2023), https://arxiv.org/abs/2307.07485.
