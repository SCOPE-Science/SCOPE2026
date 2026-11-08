# Complete phase-retrieval fibers for resonant three-tap cyclic windows

## Finding
Let \(N=2m\ge6\) be even. A three-tap cyclic window \(g=(a,b,c,0,\ldots,0)\) has nonzero taps, balanced endpoints \(|a|=|c|>0\), and a nonsingular zero-lag circulant:
\[
W(\xi)=|a|^2+|b|^2\xi+|c|^2\xi^2\ne0\quad(\xi^N=1).
\]
In particular, the last condition follows if \(|b|^2>2|a|^2\). Put
\[
\kappa=\frac{\overline b c}{\overline a b}\in\mathbb T,
\qquad \tau=\kappa^2,
\qquad \omega=e^{2\pi i/N}.
\]
For any nowhere-zero signal \(f\in(\mathbb C^\times)^N\), consider all \(N^2\) intensities
\[
I_f(t,k)=\left|\overline a f_t+\overline b\omega^k f_{t+1}+\overline c\omega^{2k} f_{t+2}\right|^2,
\qquad t,k\in\mathbb Z_N.
\]
Every fiber, including competitors not assumed nowhere-zero, has at most two global-phase equivalence classes. If \(\kappa^N\ne1\), each fiber is a singleton. If \(\kappa^N=1\), two classes occur exactly for signals of the form
\[
f_{2j}=A\rho^j\tau^{j(j-1)},\qquad
f_{2j+1}=AR\rho^j\tau^{j^2},\qquad 0\le j<m,
\]
where \(A,R\in\mathbb C^\times\), \(\rho^m=1\), and
\[
\delta=\kappa\frac{R}{\overline R}\overline\rho\ne1.
\]
The sole other global-phase class is represented by
\[
h_{2j}=\delta f_{2j},\qquad h_{2j+1}=f_{2j+1}.
\]
The classification includes genuinely quadratic interlaced chirps for every even \(N\ge6\): take \(g=(1,3,\omega,0,\ldots,0)\), \(A=1\), \(R=2\), \(\rho=1\). Then \(\delta=\omega\ne1\), so the complete spectrogram has two distinct full-support solutions in every such dimension.

## Assumptions and scope
All indices are cyclic modulo \(N\). The data include every time shift and all \(N\) frequencies. A fiber consists of all complex vectors with the same data; global unimodular scalar multiples are identified. No amplitude assumption is made on a competing vector. The circulant condition is equivalent to invertibility of the convolution \(x\mapsto |a|^2x_t+|b|^2x_{t+1}+|c|^2x_{t+2}\). It excludes possible amplitude ambiguities from that convolution. Endpoint balance implies \(|\kappa|=1\). The nontrivial phase-twisted case \(\kappa\ne1\) is particularly relevant: it creates a missing lag-one Fourier mode precisely at the resonance \(\kappa^N=1\).

## Proof
For a fixed time \(t\), write \(P_t(z)=u_t+v_tz+w_tz^2\), with \(u_t=\overline a f_t\), \(v_t=\overline b f_{t+1}\), \(w_t=\overline c f_{t+2}\). Since \(N\ge6\), the frequencies \(0,\pm1,\pm2\) are distinct modulo \(N\). The discrete Fourier transform of \(|P_t(\omega^k)|^2\) in \(k\) therefore recovers exactly the three correlations
\[
Z_t=|a|^2|f_t|^2+|b|^2|f_{t+1}|^2+|c|^2|f_{t+2}|^2,
\]
\[
B_t=\overline a b\,f_t\overline{f_{t+1}}+\overline b c\,f_{t+1}\overline{f_{t+2}},
\qquad C_t=\overline a c\,f_t\overline{f_{t+2}}.
\]
Suppose \(h\) has identical intensities. Fourier diagonalization and the assumption \(W(\xi)\ne0\) show that the equal zero-lag vectors give \(|h_t|^2=|f_t|^2\) for every \(t\). Thus \(h_t=\lambda_t f_t\) with \(|\lambda_t|=1\). Equality of \(C_t\ne0\) yields \(\lambda_{t+2}=\lambda_t\). Because \(N\) is even, these multipliers are constant on each parity class. After a global-phase normalization, \(\lambda_{2j}=\delta\in\mathbb T\) and \(\lambda_{2j+1}=1\).

If \(\delta=1\), then \(h\) is equivalent to \(f\). Otherwise, write
\[
U_t=\overline a b\,f_t\overline{f_{t+1}},\qquad
V_t=\overline b c\,f_{t+1}\overline{f_{t+2}}.
\]
For even \(t\), equality of the lag-one coefficients is \(\delta U_t+\delta^{-1}V_t=U_t+V_t\), giving \(V_t/U_t=\delta\). For odd \(t\) the roles reverse, giving \(V_t/U_t=\delta^{-1}\). Introducing \(r_t=f_{t+1}/f_t\), we obtain
\[
\kappa r_t\overline{r_{t+1}}=
\begin{cases}\delta,&t\text{ even},\\\delta^{-1},&t\text{ odd}.
\end{cases}
\]
Each right-hand side has modulus one, so \(|r_t|\,|r_{t+1}|=1\); taking conjugates of two successive equations then gives \(r_{t+2}=\kappa^2r_t=\tau r_t\). Periodicity of \(r\) forces \(\tau^m=1\), equivalently \(\kappa^N=1\). Hence \(r_{2j}=R\tau^j\), \(r_{2j+1}=S\tau^j\), for nonzero \(R,S\). Put \(\rho=RS\). Periodicity of \(f\) yields \(\rho^m=1\) and summing consecutive ratios gives the displayed formulas for \(f_{2j}\) and \(f_{2j+1}\). The even lag-one equation then fixes
\[
\delta=\kappa R\overline S=\kappa(R/\overline R)\overline\rho.
\]
There is at most one possible nonidentity \(\delta\), so there are at most two classes. Conversely, under the displayed conditions, the ratios satisfy the alternating lag-one equations, while the proposed \(h\) preserves \(Z_t\) and \(C_t\) automatically; thus all intensities agree. The condition \(\delta\ne1\) makes \(h\) inequivalent to \(f\). This establishes both necessity and sufficiency.

For the explicit family, \(\kappa=\omega\), \(\tau=\omega^2\), \(\rho=1\), and \(R=2\), so \(\delta=\omega\ne1\). The middle window power is \(9>2\), guaranteeing the assumed circulant invertibility.

## Verification
The standalone `verify_chirp.py` uses only integer coefficients in the group ring of the cyclic phase character to compare, without floating-point approximation, the exact zero-, first-, and second-lag Fourier coefficients of the intensity for the explicit two-solution family. It covers each even \(N\) from \(6\) through \(40\), totaling \(18\) dimensions and \(1242\) correlation entries. The expected output is `CHIRPED_THREE_TAP_PASS dimensions=18 exact_correlation_rows=1242`. The finite checks are independent consistency checks; the preceding argument is the proof for arbitrary even order and continuous window parameters.

## Relationship to prior work
Bartusel (first publicly posted 14 June 2022) develops ambiguity-function and connectedness criteria and studies short windows. His fixed-window all-signal criteria require stronger nonvanishing assumptions, while his short-window classification treats separated supports; these do not determine the full-support two-class chirp fibers at a missing lag-one mode. His later 2026 treatment establishes sufficiently rich ambiguity-support sampling conditions rather than the present sparse three-tap fiber. Bendory, Cheng, and Edidin establish generic recovery; generic injectivity does not classify all exceptional signals. Two-point cyclic-window fiber classifications involve a different support and alternating amplitude swaps rather than the present chirped parity-phase ambiguity. A known equal-tap, odd-half-length special case corresponds to \(\kappa=1\) and does not cover the phase-twisted family with arbitrary even \(N\) and strictly dominant middle coefficient.

## Limitations
The statement assumes a nowhere-zero reference signal, a balanced-endpoint three-tap window, complete time-frequency data, and invertibility of the zero-lag circulant. It does not classify signals with zeros, unbalanced endpoints, or singular zero-lag convolution, and gives no stability bound under noise. An earlier specialist treatment of phase-chirped exceptional fibers could conceivably exist under different terminology; originality is supported by the specific comparisons stated here rather than by absence from searches alone.

## References
1. D. Bartusel, *Injectivity Conditions for STFT Phase Retrieval on \(\mathbb Z\), \(\mathbb Z_d\) and \(\mathbb R^d\)*, arXiv:2206.06729, first posted 2022-06-14; *J. Fourier Anal. Appl.* 29 (2023), 53, DOI:10.1007/s00041-023-10026-2.
2. T. Bendory, C. Cheng, and D. Edidin, *Near-optimal bounds for signal recovery from blind phaseless periodic short-time Fourier transform*, arXiv:2112.02836, first posted 2021-12-06.
3. D. Bartusel, *Uncertainty Principles as a Tool for STFT Phase Retrieval*, arXiv:2605.31507, first posted 2026-05-29.
4. *Endpoint-lag recovery for nonvanishing cyclic STFT phase retrieval*, published-finding corpus record `2026/10/4/SCOPE-endpoint-lag-recovery-for-nonvanishing-cyclic-stft-phase-retriev--5ab5cece2e03`.
5. *Exact nonvanishing phase-retrieval fibers for an even two-point cyclic STFT window*, published-finding corpus record `2026/10/4/SCOPE-exact-nonvanishing-phase-retrieval-fibers-for-an-even-two-point--29afd3fc909d`.
