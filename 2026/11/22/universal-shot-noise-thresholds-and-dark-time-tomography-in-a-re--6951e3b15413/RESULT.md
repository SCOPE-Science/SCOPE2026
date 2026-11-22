# Universal shot-noise thresholds and dark-time tomography in a reset fluorescent emitter

## Finding

A single regenerative photon emitter with arbitrary finite many dark channels, independently interrupted by Poisson ground-state re-preparation, admits an exact, distribution-free **one-crossing theorem** for its long-time photon-count Fano factor. The transition is controlled only by a Laplace transform of dark-state survival, is independent of the radiative decay rate, and provides a nonparametric inverse measurement of the *aggregate* dark-time survival function. At the shot-noise equality the normalized third count cumulant is strictly below its Poisson value. A heavy-tailed dark channel produces a nonanalytic weak-pump transition scale.

Let the positive pump rate be \(p\), radiative emission rate \(\gamma\), and independent complete ground-state reset rate \(r\). Let \(m\ge1\) dark channels be entered from the excited state at rates \(s_1,\ldots,s_m>0\), with corresponding independent dark dwell times \(U_i>0\), finite almost surely but with otherwise arbitrary laws. Put
\[
K(r)=\sum_{i=1}^{m}s_i\int_0^\infty t e^{-rt}\Pr(U_i>t)\,dt.
\]
For every \(r>0\), the asymptotic Fano factor \(F(r)=\lim_{t\to\infty}\operatorname{Var}(N_t)/\mathbb E N_t\) exists and obeys
\[
\operatorname{sgn}(F(r)-1)=\operatorname{sgn}(pK(r)-1).
\]
The function \(K\) is continuous and strictly decreasing from \(K(0+)=\tfrac12\sum_i s_i\mathbb E U_i^2\in(0,\infty]\) to \(0\). Therefore, for fixed pump \(p\), an exactly one positive sub-Poissonian/super-Poissonian reset threshold exists **if and only if** \(pK(0+)>1\). The Fano factor is strictly above one below that rate and strictly below one above it. Otherwise it is strictly below one at every positive reset rate. This statement does not require finite unreset dark-time variance.

For each fixed \(r>0\), pumping across the unique threshold \(p_c(r)=1/K(r)\) reverses the Fano sign. Perfect knowledge of \(p_c(r)\) for every \(r>0\) uniquely identifies the aggregate \(h(t)=\sum_i s_i\Pr(U_i>t)\) for all \(t>0\) through Laplace inversion of \(t h(t)=\mathcal L^{-1}[1/p_c](t)\). Individual dark channels are **not** separately identified.

At every parameter point where \(F=1\), the normalized third long-time count cumulant satisfies \(c_3/c_1<1\): exact second-order Poisson statistics do not imply Poisson emission.

For a single Pareto dark law \(\Pr(U>t)=(1+t/\tau)^{-\alpha}\) with \(\tau>0\), \(0<\alpha<2\), and entrance rate \(s>0\), the positive threshold exists for all pump rates and obeys
\[
r_*(p)\sim\big[p s\tau^\alpha\Gamma(2-\alpha)\big]^{1/(2-\alpha)}\qquad(p\downarrow0).
\]

## Assumptions and scope

The stochastic state begins in ground state G. It undergoes excitation \(G\to E\) at rate \(p>0\), counted spontaneous emission \(E\to G\) at rate \(\gamma>0\), and independent shelving events \(E\to D_i\) at rate \(s_i>0\). Once in \(D_i\), it stays a fresh independent duration distributed as \(U_i\), then returns to G if no reset intervenes. Every reset, according to a state-independent Poisson clock with rate \(r>0\), returns the entire emitter and its dark-state age to G. Resets are never counted as photons. The dark durations are independent of everything else and redrawn at each dark entry. The physical observation is the total number \(N_t\) of radiative events up to \(t\). The model is an idealized classical semi-Markov photon-jump model: no coherent excitation or measurement backaction beyond the specified jumps. The number of channels is finite; no finite unreset moments are required.

At every photon event the process returns to G with independent future randomness; hence the interphoton times \(T\) are independent and identically distributed. All positive-order moments of \(T\) are finite at \(r>0\), because each failed pre-emission attempt is geometrically interrupted and dark dwell times are exponentially truncated. Long-time cumulant growth rates \(c_k=\lim_{t\to\infty}\kappa_k(N_t)/t\) are considered for \(k=1,2,3\).

## Proof

Let \(R\sim\operatorname{Exp}(r)\) be independent. Set \(V_i=\min(U_i,R)\), \(M_{i,k}=\mathbb E V_i^k\), and \(\psi_i(z)=\mathbb E e^{-zV_i}\). Elementary survival integration gives
\[
M_{i,k}=k\int_0^\infty t^{k-1}e^{-rt}\Pr(U_i>t)\,dt,\qquad k=1,2,3.
\]
Let \(f_G(z)=\mathbb E e^{-zT}\) starting in G and \(f_E(z)\) starting in E. The exponential transition and reset competition yield
\[
f_G(z)=\frac p{p+z}f_E(z),\qquad
f_E(z)=\frac{\gamma+[r+\sum_i s_i\psi_i(z)]f_G(z)}{\gamma+\sum_i s_i+r+z}.
\]
Thus with \(s=\sum_i s_i\),
\[
f_G(z)=\frac{p\gamma}{H(z)},\quad H(z)=(p+z)(\gamma+s+r+z)-p\left[r+\sum_i s_i\psi_i(z)\right].
\]
All equalities are valid in a neighborhood of zero, since \(r>0\) bounds the positive exponential moments of each \(V_i\). We have \(H(0)=p\gamma\), and direct differentiation gives
\[
A=H'(0)=p+\gamma+s+r+p\sum_i s_iM_{i,1},\quad
B=H''(0)=2-p\sum_i s_iM_{i,2},\quad
C=H^{(3)}(0)=p\sum_i s_iM_{i,3}>0.
\]
For the exponentially light-tailed renewal interval, the scaled cumulant generating function \(z(x)\) is the unique analytic small-\(x\) solution of \(H(z(x))=p\gamma e^x\), with \(z(0)=0\). Three differentiations give
\[
c_1=\frac{p\gamma}{A},\qquad
\frac{c_2}{c_1}=1-\frac{p\gamma B}{A^2},\qquad
\frac{c_3}{c_1}=1-3\frac{p\gamma B}{A^2}\frac{c_2}{c_1}-\frac{(p\gamma)^2 C}{A^3}.
\]
Consequently, \(F-1=(p\gamma/A^2)(p\sum_i s_i M_{i,2}-2)\). Since \(\sum_i s_iM_{i,2}=2K(r)\), the claimed Fano-sign equivalence follows. At the crossing \(B=0\), the third ratio is \(1-(p\gamma)^2 C/A^3<1\). The strict inequality follows from positive dark entrance rates and almost-surely positive dark durations.

The derivative
\[
K'(r)=-\sum_i s_i\int_0^\infty t^2e^{-rt}\Pr(U_i>t)\,dt<0
\]
exists at every positive \(r\). As \(r\to\infty\), dominated convergence gives \(K(r)\to0\); as \(r\downarrow0\), monotone convergence gives \(K(0+)=\frac12\sum_i s_i\mathbb E U_i^2\) with the possibility of infinity. Continuity and strict monotonicity prove the exact number of crossings, including the equality case where \(pK(0+)=1\): there is no positive crossing. At fixed \(r>0\), \(p_c(r)=1/K(r)\) is unique and is independent of \(\gamma\).

Since \(K(r)=\int_0^\infty e^{-rt}\,t h(t)\,dt\), uniqueness of Laplace transforms identifies \(t h(t)\) almost everywhere from the full ideal threshold curve. The aggregate survival function \(h\) is right-continuous for \(t>0\); therefore its almost-everywhere determination uniquely fixes it at every positive time. Different decompositions \(h=\sum_i s_i\Pr(U_i>\cdot)\) generally remain observationally equivalent.

For the Pareto case, substitution \(v=rt\) and dominated convergence yield
\[
K(r)\sim s\tau^\alpha\Gamma(2-\alpha)r^{\alpha-2}\quad(r\downarrow0).
\]
Inverting the strictly monotone threshold equation \(pK(r_*)=1\) proves the asymptotic stated above. No finite-dark-time second moment has been invoked.

## Verification

Run \(\texttt{python verification.py}\) with Python 3, SymPy and mpmath. This standalone program checks the exact four-state tilted-generator determinant for two exponentially distributed dark channels, all first three small-count derivatives, the one-channel limiting formula, forty independent two-dark-branch numerical tilted-generator cumulant calculations, the non-exponential deterministic dwell transform, and Pareto heavy-tail threshold scaling. The computations are auxiliary checks; the analytic proof above establishes arbitrary finite channel counts and dwell laws.

## Relationship to prior work

Liu (2023), arXiv:2308.02214, develops general quantum-jump renewal and tilted-matrix counting formulas with resetting, including explicit two-level examples. The current derivation uses that established renewal viewpoint but identifies the exact Fano sign for a broad semi-Markov dark sector, a strict third-cumulant witness, and nonparametric aggregate survival reconstruction from the zero-excess-noise curve. Lachman and collaborators (2024) analyze a single metastable dark branch of an unreset emitter, providing a physically relevant base model but not the arbitrary-law threshold or inverse map. Volkán-Kacsó (2014) studies arbitrary power-law on/off statistics in photon blinking without the Poisson ground-reset control. The single exponentially distributed dark-channel Fano crossing is already obtainable from the familiar three-state Markov model; it is not claimed as a separate novelty here. General counting-formula coverage leaves a residual risk of unrecognized implicit specialization.

## Limitations

The inverse theorem requires ideal knowledge of the critical pump curve at *all* positive reset rates; a finite set of noisy measurements cannot identify an arbitrary unknown survival function. The theorem identifies only the weighted aggregate of dark-channel survival laws, not individual channels. The third-cumulant statement describes long-time renewal counts, not finite-time binned photon statistics. Direct temperature dependence, coherent driving, nonrenewal dark-state memory, reset failures, photon-detection loss, and energetic cost of re-preparation are not included. Numerical checks do not replace the analytic claims, and no independent experimental validation is asserted.

## References

- Fei Liu, *Semi-Markov Processes in Open Quantum Systems. II. Counting Statistics with Resetting*, arXiv:2308.02214, first submitted 2023-08-04, https://arxiv.org/abs/2308.02214.
- Lukáš Lachman et al., *Experimental Certification of Level Dynamics in Single-Photon Emitters*, *Physical Review Research* **6**, 033254 (2024), https://doi.org/10.1103/PhysRevResearch.6.033254.
- Sándor Volkán-Kacsó, *Two-state theory of binned photon statistics for a large class of waiting time distributions and its application to quantum dot blinking*, *Journal of Chemical Physics* **140**, 224110 (2014), https://doi.org/10.1063/1.4881460.
