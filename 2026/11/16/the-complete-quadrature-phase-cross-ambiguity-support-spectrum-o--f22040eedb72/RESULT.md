# The complete quadrature-phase cross-ambiguity support spectrum on the four-cycle

## Finding
Let \(\mu_4=\{1,i,-1,-i\}\). For every ordered pair \(f,g:\mathbb Z_4\to\mu_4\), define the full cyclic cross short-time Fourier transform
\[
V_gf(x,k)=\sum_{t=0}^{3}f(t)\overline{g(t-x)}i^{-kt},\qquad (x,k)\in\mathbb Z_4^2.
\]
Its support cardinality is **exactly one of** \(4,6,8,11,12,16\), and every listed cardinality occurs. Quotienting by independent global fourth-root multiplications of \(f\) and \(g\), there are exactly \(4^6=4096\) normalized ordered pairs, with the following complete census.

| Support cardinality | Normalized QPSK pairs | Normalized binary-phase pairs |
|---|---:|---:|
| 4 | 32 | 8 |
| 6 | 64 | 16 |
| 8 | 32 | 8 |
| 11 | 768 | 0 |
| 12 | 1024 | 0 |
| 16 | 2176 | 32 |

For each shift \(x\), let \(r_x\) be the number of nonzero frequency bins \(k\). The **complete sorted shift-row profile classification** for quadrature-phase pairs is

| Sorted \((r_0,r_1,r_2,r_3)\) | Number of normalized pairs |
|---|---:|
| (1,1,1,1) | 32 |
| (1,1,2,2) | 64 |
| (2,2,2,2) | 32 |
| (1,2,4,4) | 256 |
| (1,3,3,4) | 512 |
| (2,3,3,4) | 512 |
| (3,3,3,3) | 512 |
| (4,4,4,4) | 2176 |

In particular, the first support beyond the uncertainty minimum is \(6\); no pair has \(5,7,9,10,13,14,15\) nonzero bins. The exceptional odd support \(11\) has precisely two shift-profile types, neither possible for binary-phase pairs.

## Assumptions and scope
All 8 coefficients are individually of modulus one and belong to exactly the alphabet \(\mu_4\) (or \(\mu_2=\{1,-1\}\) for the comparison). Both sequences have four nonzero samples. The transform is the full \(4\times4\) periodic cross transform, without window truncation. Fourier normalization by a nonzero scalar does not affect support. Counts are for ordered pairs modulo independent global phase scalings only; time-frequency shifts and conjugations are **not** quotiented out. Thus raw QPSK counts are sixteen times the normalized counts and raw binary counts four times the normalized counts.

## Proof
1. Multiplying either input by a scalar from its phase alphabet multiplies the entire transform by a nonzero scalar; thus every orbit under independent input global phases has a unique representative with \(f(0)=g(0)=1\). For the QPSK alphabet this gives exactly \(4^3\) choices for each normalized sequence; for the binary alphabet, \(2^3\) each.
2. For each shift, put \(h_t=f(t)\overline{g(t-x)}\). All these numbers are Gaussian integer units. The four Fourier coefficients of that row are exactly
\[
\begin{aligned}
H_0&=(h_0+h_2)+(h_1+h_3),\\
H_2&=(h_0+h_2)-(h_1+h_3),\\
H_1&=(h_0-h_2)+i(h_3-h_1),\\
H_3&=(h_0-h_2)-i(h_3-h_1).
\end{aligned}
\]
These identities are just the exact \(4\)-point Fourier transform. Therefore zero/nonzero is decided by equality of pairs of integers, with no rounding or tolerance.
3. The embedded standalone `checker.py` iterates **every** normalized exponent vector \((a_1,a_2,a_3,b_1,b_2,b_3)\) in \(\{0,1,2,3\}^6\), calculates all sixteen entries by Gaussian-integer multiplication, and independently recomputes row supports by the displayed factorization. It asserts agreement for every input, records all sorted row profiles, and verifies the exact expected counts and exhaustive domain size. It repeats this proof on the restricted exponent alphabet \(\{0,2\}^6\). As every counted candidate is explicitly realized and every possible normalized candidate is enumerated, this finite computation establishes both exhaustive exclusion and attainability.

## Verification
Run `python3 checker.py` from the directory containing this document. The executable uses only the Python standard library and exact integer pairs for Gaussian integers. It asserts the eight-profile census, six support values, binary comparison, agreement of two independently implemented transform formulas, and totals \(4096\) and \(64\). All assertions passed during preparation of this result. Example phase-exponent witnesses are printed for each attained support count. No sampling, numerical approximation, random input, or timeout is used for the finite proof.

## Relationship to prior work
Nicola's 2022 public preprint (Theorems 1.1 and 1.2) gives the sharp general lower bound and classifies the **minimum-support** case for arbitrary complex sequences on cyclic groups. It does not give this complete QPSK support distribution or the shift-profile multiplicities. Krahmer–Pfander–Rashkov studied broad support-size constraints for finite Gabor transforms, not the claimed quaternary length-four census. Levanon–Freedman studied the ambiguity of specific quadriphase radar pulse codes, a related but different phase-coded question. A separate published result about quantized-phase Gabor **basis/frame** conditions does not imply the support distribution for every ordered cross pair. The complete finite census complements, but neither strengthens nor contradicts, those general results.

## Limitations
Only the four-point cyclic group and the two named finite phase alphabets are classified. Nothing is asserted about arbitrary complex phases, larger cyclic groups, complete magnitude distributions, or noise stability. Some historical specialist waveform tables may contain related small code statistics; systematic historical priority requires external review. Independent mathematical auditing has not been performed.

## References
1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, first public arXiv version 29 April 2022, arXiv:2204.14176v1, https://arxiv.org/abs/2204.14176.
2. F. Krahmer, G. E. Pfander, P. Rashkov, *Support size conditions for time-frequency representations on finite Abelian groups*, technical report (2007), https://sopus.constructor.university/frontdoor/index/index/docId/673.
3. N. Levanon, A. Freedman, *Ambiguity Function of Quadriphase Coded Radar Pulse*, IEEE Transactions on Aerospace and Electronic Systems 25 (1989), 848–853, https://doi.org/10.1109/7.40724.
