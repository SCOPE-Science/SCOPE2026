# Nonreversible return laws give a single sharp Crank–Nicolson positivity window

## Finding
Let \(Q\) be **any** finite real continuous-time Markov generator in row convention, so that \(q_{ij}\ge0\) for \(i\ne j\) and \(Q\mathbf 1=0\); irreducibility and reversibility are **not** assumed. Define the Crank–Nicolson end-step and backward-Euler resolvent by
\[
C_h=(I-hQ/2)^{-1}(I+hQ/2),\qquad R_s=(I-sQ)^{-1},\quad s=h/2.
\]
There exists a unique \(H\in(0,\infty]\) such that
\[
\boxed{\quad C_h\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad 0\le h\le H.\quad}
\]
Here \(H=\infty\) is allowed, and it occurs **if and only if**, after simultaneous permutation of states, \(Q\) is block diagonal with blocks consisting exclusively of one-state zero generators and two-state balanced generators
\[
\begin{pmatrix}-a&a\\a&-a\end{pmatrix},\qquad a>0.
\]
Thus arbitrary directed cycles, nonreversible chains and chains with transient states have no disconnected, later reentrant positivity windows.

A constructive formula uses first return times. Fix any \(\lambda>0\) satisfying \(\lambda\ge\max_i(-q_{ii})\) and set \(P=I+Q/\lambda\), a row-stochastic matrix. Write \(\tau_i=\min\{n\ge1:X_n=i\}\) for the first strictly positive return time to \(i\) in the discrete-time chain \(P\), started at \(i\). Let \(f_{i,n}=\Pr_i(\tau_i=n)\), \(a_i=\Pr_i(\tau_i=\infty)\), and \(z=\lambda s/(1+\lambda s)\). Then
\[
\boxed{\quad (R_s)_{ii}^{-1}=\frac{a_i}{1-z}+\sum_{n\ge1}f_{i,n}\sum_{k=0}^{n-1}z^k.\quad}
\]
For every state with a nonzero exit rate, \((R_s)_{ii}\) is **strictly decreasing** for \(s\ge0\); it is identically one for absorbing states. Define \(\ell_i=\lim_{s\to\infty}(R_s)_{ii}\), which equals the stationary probability of \(i\) within its closed irreducible class when \(i\) is recurrent, and zero when it is transient. For each \(i\) with \(\ell_i<1/2\), there exists a unique \(s_i>0\) for which \((R_{s_i})_{ii}=1/2\). The sharp positivity endpoint is
\[
H=2\min_{\{i:\ell_i<1/2\}}s_i,
\]
with \(H=\infty\) if that set is empty. For \(\lambda_{\max}=\max_i(-q_{ii})>0\), the universal guaranteed window \(0\le h\le2/\lambda_{\max}\) is contained in the sharp window; for irreducible chains with at least two states the inclusion is strict.

For the unit-rate **directed three-cycle** \(Q=P_3-I\), the nonreversible endpoint is explicitly
\[
\boxed{H=1+\sqrt5.}
\]
For a one-way pure-birth chain, the sufficient bound \(2/\lambda_{\max}\) is sharp.

## Assumptions and scope
The finite state set has arbitrary positive cardinality. All rates are fixed, finite, and nonnegative off the diagonal. \(C_h\) acts by right multiplication on row probability distributions, so its entrywise nonnegativity together with \(C_h\mathbf1=\mathbf1\) is precisely preservation of probability for **all** initial distributions. The positivity window is for the exact Crank–Nicolson end-step, not for the separate internal stages of a Runge–Kutta implementation. Reducible and absorbing generators are permitted. At \(h=0\) the map is the identity and is nonnegative.

The cutoff \(H\) is finite when any state is transient, any closed irreducible class has at least three states, or any closed two-state class has unequal transition rates. In the infinite case, the statement \(0\le h\le H\) means every finite \(h\ge0\).

## Proof
**1. Reduce all entrywise signs to the diagonal.** For \(s\ge0\), \(I-sQ\) is a nonsingular \(M\)-matrix and \(R_s\ge0\). Also \(R_s\mathbf1=\mathbf1\). The algebraic Cayley identity gives
\[
C_h=2R_s-I.
\]
Thus \((C_h)_{ij}=2(R_s)_{ij}\ge0\) whenever \(i\ne j\), whereas \((C_h)_{ii}=2(R_s)_{ii}-1\). Therefore \(C_h\) is entrywise nonnegative exactly when \((R_{h/2})_{ii}\ge1/2\) for every \(i\).

**2. Prove the return formula without reversibility.** The chosen uniformization rate makes \(P=I+Q/\lambda\) stochastic. With \(z=\lambda s/(1+\lambda s)\),
\[
R_s=(1-z)(I-zP)^{-1}.
\]
Let \(u_i(z)=\sum_{m\ge0}(P^m)_{ii}z^m\), and let \(F_i(z)=\sum_{n\ge1}f_{i,n}z^n\). The first-return decomposition of every path that starts at \(i\) and finishes at \(i\) gives \(u_i(z)=1+F_i(z)u_i(z)\), so \(u_i(z)=1/(1-F_i(z))\) for \(0\le z<1\). Hence \((R_s)_{ii}=(1-z)/(1-F_i(z))\).

Since \(a_i+\sum_{n\ge1}f_{i,n}=1\), dividing
\[
1-F_i(z)=a_i+\sum_{n\ge1}f_{i,n}(1-z^n)
\]
by \(1-z\) yields the asserted inverse-diagonal return formula. Each summand on its right is nondecreasing in \(z\). If \(i\) is nonabsorbing, \(P_{ii}<1\); consequently either \(a_i>0\) or some \(f_{i,n}>0\) for \(n\ge2\). The right side is then strictly increasing in \(z\in[0,1)\), which proves strict decrease of \((R_s)_{ii}\) as \(s\) increases. If \(i\) is absorbing, \(f_{i,1}=1\) and the inverse diagonal is identically one.

**3. Identify limits and crossing times.** For a transient state the probability \(a_i\) of never returning is positive, and the return formula implies \((R_s)_{ii}\to0\). For a recurrent state in a finite closed irreducible class, \(a_i=0\) and the mean discrete return time satisfies \(\mathbb E_i\tau_i=1/\pi_i\), where \(\pi\) is that class's normalized stationary law. Monotone convergence in the return formula then gives \((R_s)_{ii}\to\pi_i\). The same is immediate for a one-state absorbing class with \(\pi_i=1\).

Every diagonal starts at one and decreases continuously to \(\ell_i\) if the state is nonabsorbing. It crosses \(1/2\) once and only once when \(\ell_i<1/2\), and otherwise stays above \(1/2\) at every finite step. Combining these independent state thresholds proves that the **entire** positivity set is precisely the single interval \([0,H]\) (or all nonnegative steps).

**4. Classify unconditional positivity, including reducible chains.** For \(H=\infty\), every state must have \(\ell_i\ge1/2\), so no transient states exist. The state space is therefore a disjoint union of closed irreducible classes. A closed class with \(m\ge3\) has some stationary probability below \(1/2\), hence cannot occur. A two-state class has stationary masses both at least \(1/2\) only if they both equal \(1/2\), which requires its two rates to be equal. Singleton classes are absorbing. Conversely, each of these allowed blocks has diagonal resolvent at least \(1/2\) for every finite step; their direct sum does too. This proves necessity and sufficiency.

**5. Show the universal lower bound and exact examples.** The probability of staying at state \(i\) without jumping through time \(t\) is \(e^{-\lambda_i t}\), with \(\lambda_i=-q_{ii}\). Thus \((e^{tQ})_{ii}\ge e^{-\lambda_i t}\), so
\[
(R_s)_{ii}=\int_0^\infty e^{-t}(e^{stQ})_{ii}\,dt\ge\frac1{1+s\lambda_i}.
\]
In particular all diagonals are at least \(1/2\) whenever \(s\le1/\lambda_{\max}\). If the chain is irreducible and has at least two states, every state can depart and return along a positive-rate path, so the inequality is strict for all \(s>0\) and all \(i\); continuity at the common sufficient cutoff gives \(H>2/\lambda_{\max}\).

For the unit-rate directed three-cycle, direct inversion yields
\[
(R_s)_{ii}=\frac{(1+s)^2}{1+3s+3s^2},\qquad (C_{2s})_{ii}=\frac{1+s-s^2}{1+3s+3s^2}.
\]
All off-diagonal entries are nonnegative, and the diagonal is nonnegative exactly when \(s\le(1+\sqrt5)/2\), giving \(H=1+\sqrt5\). Finally, on a one-way pure-birth chain, no departed state returns, so each nonabsorbing state's resolvent diagonal equals \((1+s\lambda_i)^{-1}\); thus \(H=2/\lambda_{\max}\), as asserted.

## Verification
`verify.py` (Python 3 with SymPy 1.14) uses exact rational/symbolic arithmetic on directed cycles, balanced blocks, pure-birth and path generators, and independently generated nonreversible rate matrices. It checks row-sum preservation, the Cayley identity, nonnegativity off diagonal, the sharp diagonal cutoff criterion, and strict diagonal monotonicity at rational step pairs. It also symbolically derives the directed-three-cycle diagonal formula and its derivative and tests the two-state and birth-chain boundaries. Running `python verify.py` on the attached code produced **5,754 passing assertions**, recorded in `verification_output.txt`. These finite tests do **not** establish the all-generator theorem; the general proof is the first-return argument above.

## Relationship to prior work
Blanes, Iserles and Macnamara (2021, arXiv:2102.08242v1; full-text 2022 version) motivate positivity for nonsymmetric graph-Laplacian ODE models and distinguish structure-preserving integration methods from ordinary Runge–Kutta updates. Their analysis does not give the one-interval Crank–Nicolson cutoff for arbitrary reducible or nonreversible finite chains.

Fallat and Tsatsomeros (2002) study general Cayley transforms of \(M\)-matrices; their Lemma 2.2 supplies the algebraic transform identity. Their matrix-class results do not imply the monotonicity of Markov return diagonals, the single-interval step law, or the reducible classification. Horváth (1998) provides worst-problem-class Runge–Kutta positivity radii, rather than a sharp, chain-dependent frontier.

The closest published chain-specific analysis, *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* (2026), already establishes the general resolvent diagonal test, the reversible irreducible single-cutoff law, the irreducible unconditional two-state classification, and some explicit symmetric examples. **None of those is claimed as new here.** Its reversible monotonicity proof uses a positive spectral mixture, and its stated scope leaves open possible disconnected positivity sets for nonreversible chains, as well as the reducible unconditional case. The new contribution is the first-return argument establishing the universal nonreversible single-cutoff theorem; the full reducible classification and the sharp explicitly nonreversible directed-three-cycle endpoint are concrete consequences, not separately asserted to require new methods. General Markov renewal identities are classical; their use here is part of the proof, not claimed as a new probabilistic theorem.

## Limitations
The theorem concerns finite, time-homogeneous Markov generators and exact-arithmetic Crank–Nicolson end-step matrices. It does not cover general matrix-valued non-Markov ODEs, nonlinear or time-varying generators, stage positivity, nor higher-order Padé or Runge–Kutta maps. The return generating function is a mathematical characterization, not a claim that exact first-return distributions are computationally inexpensive to obtain for large state spaces. Literature on stochastic-matrix Cayley transforms, semi-Markov renewal theory and other terminology is broad; an unlocated implication-equivalent earlier formula remains the principal precedence risk.

## References
1. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for population models*, arXiv:2102.08242v1, first submitted 2021-02-16; revised as *Positivity-preserving methods for ordinary differential equations*, arXiv:2102.08242v2 (2022). https://arxiv.org/abs/2102.08242 and https://arxiv.org/html/2102.08242v2.
2. S. M. Fallat and M. J. Tsatsomeros, *On the Cayley Transform of Positivity Classes of Matrices*, Electronic Journal of Linear Algebra 9 (2002), 190–196. https://doi.org/10.13001/1081-3810.1086.
3. Z. Horváth, *Positivity of Runge–Kutta and Diagonally Split Runge–Kutta Methods*, Applied Numerical Mathematics 28 (1998), 309–326. https://doi.org/10.1016/S0168-9274(98)00050-6.
4. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* (2026), public research record: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
