# Complete full-support fibers for the three-tap cyclic Fourier window in odd half-length

## Finding

Let \(N=2m\) with \(m\ge3\) odd, and let \(\zeta=\exp(2\pi i/N)\). For a signal \(f=(f_t)_{t\in\mathbb Z_N}\) define the complete three-tap window intensities
\[
I_f(t,k)=\left|f_t+\zeta^k f_{t+1}+\zeta^{2k}f_{t+2}\right|^2,
\qquad t,k\in\mathbb Z_N.
\]
For every coordinatewise nonzero \(f\), the fiber of this measurement map modulo a common unimodular scalar has **at most two elements**. It has two elements if and only if there are \(A,B\in\mathbb C\setminus\{0\}\) and an \(m\)-th root of unity \(\rho\) such that
\[
f_{2j}=A\rho^j,\qquad f_{2j+1}=B\rho^j
\quad(0\le j<m),
\]
and the unimodular number
\[
\delta=\frac{B\overline A\,\overline\rho}{A\overline B}
\]
is not \(1\). In that case a representative of the unique other projective class is
\[
 h_{2j}=\delta f_{2j},\qquad h_{2j+1}=f_{2j+1}.
\]
If the displayed periodic form does not hold or \(\delta=1\), the fiber consists only of the global-phase class of \(f\). Thus the nonunique locus is a finite union of explicit four-real-dimensional families inside the full-support signal space, and the full-support measurements are generically injective.

For example, for every \(N=4q+2\ge6\), the vectors obtained by repeating \((2,3i)\) and \((-2,3i)\) have identical complete intensity measurements, although they are not global-phase equivalent.

## Assumptions and scope

All indices are cyclic modulo \(N\). The signal \(f\) must have every coordinate nonzero; the comparison signal is initially unrestricted. The three-tap window has exactly three consecutive equal, nonzero coefficients, with all \(N\) translations and all \(N\) modulation frequencies measured. This is the standard cyclic short-time Fourier transform (STFT) magnitude up to harmless translation-dependent modulation phases and a sign change in frequency. The assumption that \(m=N/2\) is odd is essential to the parity-cycle step in the proof; the result makes no assertion for dimensions divisible by four or for unequal tap weights.

## Proof

**Step 1: exact autocorrelation recovery.** For fixed \(t\), expand the squared modulus as a Fourier polynomial in \(\zeta^k\). Since \(N\ge6\), its frequencies \(0,\pm1,\pm2\) are distinct modulo \(N\). Orthogonality of the \(N\)-point discrete Fourier transform therefore recovers exactly
\[
 C_0(t)=|f_t|^2+|f_{t+1}|^2+|f_{t+2}|^2,
\]
\[
 C_1(t)=f_t\overline{f_{t+1}}+f_{t+1}\overline{f_{t+2}},\qquad
 C_2(t)=f_t\overline{f_{t+2}}.
\]
Thus \(I_g=I_f\) is equivalent to equality of the three displayed correlations at every \(t\). Since every \(C_2(t)\) for \(f\) is nonzero, every coordinate of \(g\) is nonzero too.

**Step 2: only parity phases are possible.** Put \(r_t=g_t/f_t\). Equality of \(C_2\) gives
\[
 r_t\overline{r_{t+2}}=1
\quad\text{for every }t.
\]
It follows that \(r_{t+4}=r_t\). On either parity class, adding two traverses a cycle of odd length \(m\). A sequence that simultaneously has period four and cyclic period \(2m\) is therefore constant on each parity class. The same equation then forces its constants to have modulus one. Hence for some \(\alpha,\beta\in\mathbb T\),
\[
 g_{2j}=\alpha f_{2j},\qquad g_{2j+1}=\beta f_{2j+1}.
\]
Set \(\delta=\alpha\overline\beta\). If \(\delta=1\) then \(g\) is a global-phase multiple of \(f\), as required.

**Step 3: the exceptional form is necessary.** Suppose \(\delta\ne1\). Write
\[
 a_t=f_t\overline{f_{t+1}},\qquad b_t=f_{t+1}\overline{f_{t+2}}=a_{t+1}.
\]
Equality of \(C_1\), separately for even and odd \(t\), yields
\[
 \frac{b_t}{a_t}=
 \begin{cases}\delta,&t\text{ even},\\
 \delta^{-1},&t\text{ odd}.
 \end{cases}
\]
Both ratios have modulus one, so \(|f_{t+2}|=|f_t|\). Multiplication of two successive ratios gives \(a_{t+2}/a_t=1\). Define the unimodular ratio \(\rho_t=f_{t+2}/f_t\). Then
\[
 1=\frac{a_{t+2}}{a_t}=\rho_t\overline{\rho_{t+1}},
\]
so \(\rho_{t+1}=\rho_t\) at every site. Thus \(\rho_t\) is a constant \(\rho\in\mathbb T\), and cyclicity implies \(\rho^m=1\). Taking \(A=f_0\), \(B=f_1\) gives exactly the claimed form. Evaluating the even-indexed ratio yields
\[
 \delta=\frac{b_0}{a_0}=
 \frac{B\overline A\,\overline\rho}{A\overline B}.
\]
There is therefore at most one nontrivial relative parity phase and at most two projective classes.

**Step 4: the exceptional form is sufficient.** Conversely suppose \(f_{2j}=A\rho^j\) and \(f_{2j+1}=B\rho^j\) with \(\rho^m=1\), and define \(h\) using the stated \(\delta\). Its coordinate magnitudes agree with those of \(f\), so their \(C_0\) agree. Each \(C_2\) agrees because both coordinates have the same parity. The even and odd ratios \(b_t/a_t\) are respectively \(\delta\) and \(\delta^{-1}\), so substitution shows the \(C_1\) agree as well. By Step 1, all intensities agree. If \(\delta\ne1\), the even and odd multipliers differ, hence \(h\) is not globally phase equivalent to \(f\). This proves necessity, sufficiency, and the exact fiber cardinalities.

The exceptional set is parameterized by the finite choice \(\rho^m=1\) and two independent nonzero complex numbers \(A,B\). For distinct \(\rho\) the families are disjoint since \(\rho=f_2/f_0\), and the nontriviality condition \(\delta\ne1\) removes a lower-dimensional subset. This proves the dimension and generic-injectivity assertions.

## Verification

The complete exact comparison for the period-two examples uses integer complex arithmetic on all cyclic autocorrelation rows; direct Fourier intensities were also checked for lengths \(6,10,14,18\). Additional root-of-unity examples test all intensity samples for nontrivial \(\rho\) and the same four lengths. Generic controls and direct discrete-Fourier recovery of \(C_0,C_1,C_2\) were tested independently. Reproduce with `python3 checks.py`; successful output begins `THREE_TAP_FIBER_PASS`. These checks are supplementary: Steps 1–4 are proofs for every allowed length and every full-support complex input.

## Relationship to prior work

Generic recovery from periodic phaseless STFT data, including known-window results, is treated by Bendory, Cheng and Edidin (earliest arXiv posting 2021-12-06). Generic recovery does not classify every fiber of one fixed equal three-tap window. Jaganathan, Eldar and Hassibi prove almost-everywhere nonvanishing STFT phase retrieval under short-window hypotheses; an almost-everywhere result permits the explicit exceptional families proved here. Bartusel studies injectivity for short windows, including support-separated signals. The theorem for separated signals in that paper excludes the everywhere-nonzero class considered here. The present result adds a precise fixed-window full-support fiber classification, including the exact exceptional locus and universal maximum fiber cardinality.

## Limitations

No classification is asserted for lengths divisible by four, for signals with zeros, for incomplete sampling, or for unequal window taps. The exceptional dimension is a relative, full-support statement and not a stability estimate. The novelty comparison is based on identified published results and searchable literature; an unindexed earlier equivalent specialized calculation cannot be ruled out. Independent validation has not been performed.

## References

1. T. Bendory, C.-y. Cheng and D. Edidin, *Near-optimal bounds for signal recovery from blind phaseless periodic short-time Fourier transform*, arXiv:2112.02836, first posted 2021-12-06; https://arxiv.org/abs/2112.02836.
2. K. Jaganathan, Y. C. Eldar and B. Hassibi, *STFT Phase Retrieval: Uniqueness Guarantees and Recovery Algorithms*, arXiv:1508.02820, first posted 2015-08-12; https://arxiv.org/abs/1508.02820.
3. D. Bartusel, *Injectivity conditions for STFT phase retrieval on Z, Z_d and R^d*, arXiv:2206.06729, first posted 2022-06-14, Journal of Fourier Analysis and Applications **29**, article 53 (2023); https://arxiv.org/abs/2206.06729.
4. R. Alaifari and M. Wellershoff, *Stability Estimates for Phase Retrieval from Discrete Gabor Measurements*, Journal of Fourier Analysis and Applications **27**, article 6 (2021); https://doi.org/10.1007/s00041-020-09802-1.
