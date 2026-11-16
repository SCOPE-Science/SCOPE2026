# Sharp hexaphase self-ambiguity support spectrum on the seven-cycle

## Finding
Let \(\zeta=e^{\pi i/3}\), and let \(f:\mathbb Z_7\to\mu_6\) be any full-support sixth-root phase word. Define the unnormalized cyclic self short-time Fourier transform
\[
A_f(x,k)=\sum_{t=0}^{6}f(t)\overline{f(t-x)}e^{-2\pi i kt/7},\qquad (x,k)\in\mathbb Z_7^2.
\]
Its possible support cardinalities are **exactly** \(7,39,41,43\). After the unique normalization \(f(0)=1\), the respective numbers of words are \(1,252,4536,41867\) (a total of \(46656=6^6\)). Every value is attained.

For every nonconstant word, the six points \((0,k)\) with \(k\ne0\) vanish, while **all** \(36\) points with \(xk\ne0\) are nonzero. Additional zeros occur only at \((x,0)\), in conjugate shift pairs \(\{x,-x\}\). The possible numbers of such extra zeros are \(0,2,4\), but not \(6\). Every two-pair exceptional word (support \(39\)) belongs to precisely one of four affine-index/conjugation orbits, of respective sizes \(84,42,84,42\).

More precisely, write \(f(t)=\zeta^{a_t}\) with \(a_0=0\), and set \(J(f)=\{x\in\{1,2,3\}:A_f(x,0)=0\}\). Its complete distribution is

| \(J(f)\) | Number of normalized words |
|---|---:|
| \(\varnothing\) | 41868 |
| \(\{1\},\{2\},\{3\}\) | 1512 each |
| \(\{1,2\},\{1,3\},\{2,3\}\) | 84 each |
| \(\{1,2,3\}\) | 0 |

The four exceptional orbit representatives, written as exponent vectors \((a_0,\ldots,a_6)\) modulo six, are
\[
(0,0,0,0,0,2,3),\ (0,0,0,0,2,5,2),\ (0,0,0,2,2,5,2),\ (0,0,2,4,1,4,2).
\]
The equivalence action is \(a_t\mapsto \epsilon a_{ut+v}-\epsilon a_v\pmod6\), where \(u\in\mathbb Z_7^\times\), \(v\in\mathbb Z_7\), and \(\epsilon\in\{1,-1\}\).

## Assumptions and scope
The cyclic indices and Fourier frequencies are modulo seven. All seven entries have modulus one and are sixth roots of unity. There are no zeros in the word itself, and there is no restriction to real or binary phases. Global multiplication by any sixth root leaves \(A_f\) unchanged; normalization \(f(0)=1\) removes exactly this sixfold redundancy. Support means the number of **nonzero complex coefficients**, independent of the positive scalar normalization of the STFT. All counts are for indexed normalized words, not equivalence classes except where orbit sizes are stated.

## Proof
**1. Off-axis rigidity.** Put \(h_x(t)=f(t)\overline{f(t-x)}\in\mathbb Q(\zeta_6)\). Since \(\gcd(6,7)=1\), the seventh cyclotomic polynomial \(1+X+\cdots+X^6\) is irreducible over \(\mathbb Q(\zeta_6)\) (the cyclotomic fields of coprime conductors have intersection \(\mathbb Q\)). If \(k\ne0\) and \(A_f(x,k)=0\), the polynomial \(\sum_{t=0}^6 h_x(t)X^t\), evaluated at a primitive seventh root, must be a scalar multiple of that cyclotomic polynomial. Hence \(h_x(t)=c\) for all \(t\). If also \(x\ne0\), the product over \(t\) gives \(c^7=1\), while \(c\in\mu_6\), so \(c=1\). Thus \(f(t)=f(t-x)\) for all \(t\), and the nonzero shift generates \(\mathbb Z_7\), forcing \(f\) constant. Consequently for nonconstant \(f\), \(A_f(x,k)\ne0\) whenever \(x\ne0\) and \(k\ne0\). Moreover \(A_f(0,k)=\sum_t e^{-2\pi ikt/7}\), which is \(7\) at zero and zero otherwise.

**2. Autocorrelation reduction.** At zero frequency, \(A_f(x,0)=C_f(x)\) is the periodic autocorrelation. As \(C_f(-x)=\overline{C_f(x)}\), its off-origin zero set is the union of the three pairs \(\{\pm1\},\{\pm2\},\{\pm3\}\). If \(z=|J(f)|\), step 1 gives exactly \(43-2z\) nonzero coefficients for nonconstant \(f\). A constant word instead has only the seven coefficients \((x,0)\) nonzero.

**3. Exact finite classification.** Every normalized word is uniquely encoded by \((a_1,\ldots,a_6)\in\{0,\ldots,5\}^6\). Because \(\zeta^2=\zeta-1\), the six roots have integral-basis coordinate pairs
\[
(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1).
\]
For a fixed \(x\), the sum \(C_f(x)=\sum_t\zeta^{a_t-a_{t-x}}\) vanishes **if and only if** the two integer coordinate sums vanish. The complete bounded enumeration of all \(6^6\) exponent tuples is supplied in `verify_support.py`: it checks precisely the three positive shifts and derives the displayed seven nonempty-mask counts and empty three-pair case. The second, independent `verify_increments.py` enumerates all cyclic difference words satisfying \(\sum_t(a_t-a_{t-1})\equiv0\pmod6\), using real and imaginary integer coordinates rather than the first basis. This is a bijective enumeration and yields exactly the same mask and support counts. Neither program uses floating-point arithmetic or partial sampling.

**4. Orbits.** The affine relabelings \(t\mapsto ut+v\), complex conjugation, and global phase normalization preserve the self-ambiguity support. The explicit finite orbit computation in `verify_support.py` produces disjoint orbit sizes \(84,42,84,42\) from the four displayed representatives; its union equals exactly the \(252\)-word set with two zero pairs. Thus the orbit classification is exhaustive, not merely a list of examples.

## Verification
Run with a standard Python 3 interpreter from the directory containing the supplied files:

```bash
python3 verify_support.py
python3 verify_increments.py
```

The first prints `PASS` for the complete support census, seven autocorrelation masks and the four orbit sizes. The second independently prints `PASS` for the matching complete census. Each traverses exactly \(46656\) normalized words, performing integer operations only. The two checkers are included verbatim, with no external packages or network dependencies.

## Relationship to prior work
Nicola's 2022 finite-cyclic STFT uncertainty theorem classifies the unrestricted minimum-support equality case. It implies that the constant word gives support seven but does not imply the nonminimal restricted-alphabet support spectrum \(\{39,41,43\}\), its exact multiplicities, or the four exceptional orbits. Lam–Leung's theorem on vanishing sums of roots of unity explains why mixed sums of seven sixth roots can vanish: \(7=2+2+3\); it does not impose the simultaneous cyclic-shift constraints that yield the sharp two-pair maximum and the counts. Classical group-invariant Butson–Hadamard work addresses completely zero off-origin autocorrelation (perfect sequences), rather than the exhaustive spectrum of partial zero autocorrelations here. The nonexistence of a perfect seven-site sixth-phase sequence is **not** presented as an independent novelty claim.

## Limitations
This is a complete but finite exact classification for length seven and alphabet \(\mu_6\), not a claim for arbitrary lengths or alphabets. It concerns the locations of exact zero coefficients, not their nonzero magnitudes, minimum sidelobe *amplitudes*, noise stability or recovery stability. Exhaustive finite arithmetic proves the stated finite census but gives no infinite-parameter theorem. Historical specialist waveform classifications not available in complete form could contain these exact counts; any priority claim remains provisional pending broader independent checking.

## References
1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1, April 29, 2022. https://arxiv.org/abs/2204.14176
2. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209v1, November 13, 1995; *Journal of Algebra* 224 (2000), 91–109. https://arxiv.org/abs/math/9511209
3. B. Schmidt, D. Q. Wong and Q. Xiang, *Constructions of Butson Hadamard matrices invariant under Abelian p-groups*, *Journal of Combinatorial Theory, Series A* 181 (2021), article 105433. https://doi.org/10.1016/j.jcta.2021.105433
4. K. T. Arasu, W. de Launey and S. L. Ma, *On Circulant Complex Hadamard Matrices*, *Designs, Codes and Cryptography* 25 (2002), 123–142. https://doi.org/10.1023/A:1013817013980
