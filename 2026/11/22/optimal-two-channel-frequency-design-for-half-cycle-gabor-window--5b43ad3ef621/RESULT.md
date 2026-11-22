# Optimal two-channel frequency design for half-cycle Gabor windows

## Finding

Let \(m\ge2\), \(N=2m\), and let \(g\in\mathbb C^N\) be the unit-norm indicator of \(m\) consecutive cyclic coordinates. Consider every cyclic translation of \(g\) in each of two distinct modulation channels, with arbitrary strictly positive channel powers having sum two. The **unique optimal channel-power allocation is equal power**. Among frequency gaps, the complete list of minimizers of the squared-analysis condition number \(\kappa=B/A\) is
\[
\boxed{
\begin{array}{c|c|c}
\text{half-window length}&\text{optimal modulation gap }s\pmod{2m}&\min\kappa\\ \hline
m=2&s=2&1\\
m\ge3\text{ odd}&s=m&(m^2+1)\cos^2(\pi/m)\\
m\ge4\text{ even}&s=m-1\text{ or }m+1&m^2\cos^2(\pi/(2m))+1
\end{array}}
\]
where the gap is considered modulo \(N\); either modulation label may be translated without changing the answer. For \(m\ge3\), the system spans if and only if the gap is odd. For \(m=2\), every nonzero gap spans; the gap two is the only tight two-channel design. For every \(m\ge3\), no such two-channel design is tight.

The optimal sharp bounds at equal power are
\[
(A_*,B_*)=
\begin{cases}
(2,2),&m=2,\\
\left(m^{-1}\sec^2(\pi/m),\ m+m^{-1}\right),&m\ge3\text{ odd},\\
\left(m^{-1}\sec^2(\pi/(2m)),\ m+m^{-1}\sec^2(\pi/(2m))\right),&m\ge4\text{ even}.
\end{cases}
\]
In particular \(\kappa_*/m^2\to1\), with the two distinct parity-dependent second terms
\[
\kappa_*=
\begin{cases}
m^2+1-\pi^2+O(m^{-2}),&m\to\infty\text{ through odd integers},\\
m^2+1-\pi^2/4+O(m^{-2}),&m\to\infty\text{ through even integers}.
\end{cases}
\]

## Assumptions and scope

Identify the cyclic indices with \(\mathbb Z_N\) and use the standard Euclidean norm. The signal is arbitrary in \(\mathbb C^N\). Define
\[
g(j)=m^{-1/2}\mathbf1_{\{0,\ldots,m-1\}}(j),\quad
(T_kf)(j)=f(j-k),\quad
(M_\ell f)(j)=e^{2\pi i\ell j/N}f(j).
\]
For distinct \(\ell_0,\ell_1\in\mathbb Z_N\), choose \(w_0,w_1>0\) with \(w_0+w_1=2\), and take the \(2N\) Gabor atoms
\[
\mathcal G=\{\sqrt{w_r}\,M_{\ell_r}T_kg:\ 0\le k<N,\ r\in\{0,1\}\}.
\]
The frame operator is \(S=\sum_{h\in\mathcal G}hh^*\). Its smallest and largest eigenvalues are \(A\) and \(B\); set \(\kappa=+\infty\) when \(A=0\). All claims include *every* positive power allocation, every pair of distinct modulation channels, and every integer \(m\ge2\). A unitary translation or modulation of the window does not affect the extremal quantities.

## Proof

**1. Exact frequency response.** Let \(\widehat g(j)=N^{-1/2}\sum_{x\in\mathbb Z_N}g(x)e^{-2\pi ijx/N}\) be the unitary Fourier transform. Full translation makes \(S\) diagonal in the Fourier basis, with eigenvalues
\[
\lambda_j=w_0R_m(j-\ell_0)+w_1R_m(j-\ell_1),\qquad
R_m(k)=N|\widehat g(k)|^2.
\]
The geometric-sum identity at \(N=2m\) gives the exact nonnegative response
\[
\boxed{R_m(k)=
\begin{cases}
m,&k\equiv0\pmod{2m},\\
0,&k\not\equiv0\pmod{2m}\text{ even},\\
\displaystyle\frac1{m\sin^2(\pi k/(2m))},&k\text{ odd}.
\end{cases}}
\]
The power constraint ensures \(\operatorname{tr}S=2N\) and the mean eigenvalue equals two. We may subtract the common modulation label and write the frequency gap as \(s\in\{1,\ldots,2m-1\}\).

**2. Exact spanning conditions.** If \(s\) is odd, each nonexceptional Fourier index has exactly one positive odd-frequency response; the two exceptional indices \(0\) and \(s\) have an additional positive zero-frequency response. Hence all eigenvalues are positive for all positive powers. If \(s\) is even and \(m\ge3\), choose an even index distinct from both \(0\) and \(s\). Both response terms vanish there, so the system is singular. For \(m=2\), the only nonzero even gap is \(s=2\); then the spectrum at equal power is identically two, so it spans. All other nonzero gaps are odd and span.

**3. Equal powers uniquely minimize conditioning for each gap.** Let \(R=R_m\); it is real and even. For weights \((w_0,w_1)\), the eigenvalue multiset coincides with the one for swapped weights \((w_1,w_0)\), by the bijection \(j\mapsto s-j\). As a maximum of linear functions of the weights, \(B\) is convex; as a minimum, \(A\) is concave. Combining with exchange symmetry shows
\[
B(w_0,w_1)\ge B(1,1),\qquad A(w_0,w_1)\le A(1,1).
\]
For an odd gap, the eigenvalues at indices \(0,s\) are \(w_0m+w_1R(s)\) and \(w_0R(s)+w_1m\). Since \(R(s)<m\), their maximum equals
\[
m+R(s)+\tfrac12|w_0-w_1|\bigl(m-R(s)\bigr),
\]
which is strictly larger than the equal-power upper bound when the weights are unequal. This establishes strict optimality for every admissible odd gap. When \(m=2,s=2\), the eigenvalues are \(2w_0,2w_1,2,2\), so unequal weights strictly worsen the ratio as well.

**4. Sharp lower and upper bounds for odd gaps.** At equal weights, the two exceptional frequency indices \(0,s\) each have eigenvalue \(m+R_m(s)\); every other index has a single odd response, at most \(m\), so
\[
B_s=m+R_m(s).
\]
The odd residues contributing at nonexceptional indices form two copies of all odd residues except that one copy omits \(s\) and the other omits \(-s\). If \(m\) is odd, \(R_m(k)\) has its unique minimum at the odd residue \(k=m\), where \(R_m(m)=1/m\). That value remains among the nonexceptional eigenvalues unless \(s\equiv m\pmod{2m}\). Thus, for odd \(m\ge3\),
\[
A_s=\begin{cases}
\displaystyle m^{-1}\sec^2(\pi/m),&s=m,\\
1/m,&s\ne m\text{ odd}.
\end{cases}
\]
For even \(m\ge4\), the smallest odd responses occur at the two residues \(m-1,m+1\), and at least one copy always survives the exclusions. Hence for every odd gap
\[
A_s=m^{-1}\sec^2\bigl(\pi/(2m)\bigr).
\]

**5. Optimize the frequency gap and establish uniqueness.** Because \(R_m(s)=[m\sin^2(\pi s/(2m))]^{-1}\) for odd \(s\), the quantity \(B_s\) is smallest when \(s\) is an odd integer closest to \(m\). For odd \(m\), this is uniquely \(s=m\), which also strictly increases the lower bound. For even \(m\), the only closest odd choices are \(s=m-1,m+1\); the lower bound does not depend on the odd gap, so these and only these gaps minimize the ratio. The special \(m=2\) gap \(s=2\) has the tight eigenvalue list \(2,2,2,2\), while odd gaps have a larger condition number. The formulas for \(\kappa_*\), \((A_*,B_*)\) and their Taylor expansions follow by substitution. The lower bound is positive in every displayed optimal case; all uniqueness assertions include the arbitrary positive weights.

## Verification

The self-contained `CHECK.py` (Python 3.10+, standard library only) reconstructs the Fourier response directly, enumerates all nonzero gaps and exact predicted spectral extrema for \(2\le m\le98\), and checks the global winners. It also constructs actual complex Gabor frame-operator matrices independently for \(2\le m\le8\) and compares all Fourier matrix entries against the proposed diagonalization, then tests non-equal power allocations and exchange symmetry. Its execution produced 85,546 passing finite assertions. This is corroborating finite evidence, not the proof for unbounded \(m\); the proof is Steps 1–5 above.

## Relationship to prior work

Asipchuk, De Carli and Rodriguez's 2026 block-equivalence theorem establishes general Fourier and block reductions for finite Gabor frames. Its reduction implies the diagonalization used in Step 1, but it does not identify the minimax power allocation, classify the optimal pair of frequency channels for every half-window length, or quantify the parity-dependent sharp condition numbers here. Earlier work on noise and erasures in finite Gabor frames supplies stability context without this constrained frequency-design classification. Published studies of critically sampled overlapping cyclic boxcar Gabor bases optimize **window length on a different critical time-frequency grid**; the present design uses **all translations, exactly two frequency channels, and optimized positive channel powers**. Published two-/three-tap design studies vary different support models and objectives. These overlaps are specifically not counted as new observations.

## Limitations

The result is for a *half-cycle rectangular window*, a full cyclic translation bank, exactly two integer modulation channels, and a noiseless finite-dimensional frame operator. It does not characterize non-half-window lengths, nonuniform translations, more than two channels, or noninteger modulation frequencies. The best condition number grows quadratically, so the theorem is an optimal-design limitation rather than a uniformly stable reconstruction guarantee. Published literature may contain an older equivalent Fourier-pair optimization despite the inspected results not covering the full statement. No independent audit is asserted.

## References

1. O. Asipchuk, L. De Carli and L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139, initially public May 15, 2026, https://arxiv.org/abs/2605.16139 and https://arxiv.org/html/2605.16139v2.
2. M. Salanevich and D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, arXiv:2509.01325, https://arxiv.org/abs/2509.01325.
3. *Sharp conditioning of overlapping boxcar Gabor bases on odd cyclic fibers*, published November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-conditioning-of-overlapping-boxcar-gabor-bases-on-odd-cycl--55a7d3bf22b2.
4. *Balanced erasures uniquely optimize a two-modulation cyclic Gabor frame*, published November 2, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-balanced-erasures-uniquely-optimize-a-two-modulation-cyclic-gabo--87a89c0b24cf.
5. *Exact phase–frequency design and tightness transition for three-tap cyclic Gabor frames*, published November 2, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-phase-frequency-design-and-tightness-transition-for-three--9d47ac973e0f.
