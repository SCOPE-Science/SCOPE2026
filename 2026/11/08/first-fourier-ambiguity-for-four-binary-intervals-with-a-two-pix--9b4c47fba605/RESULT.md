# First Fourier ambiguity for four binary intervals with a two-pixel feature floor

## Finding

A binary grid aperture is a finite union \(\Omega_w=\bigcup_{j:w_j=1}[j,j+1)\), where \(w=w_0\cdots w_{N-1}\) is a binary word whose first and last digits are \(1\). Assume that \(w\) has exactly four maximal runs of \(1\)'s, that all four run lengths are at least \(2\), and that all three separating zero-run lengths are at least \(2\). Thus the physical aperture has four separated intervals and every occupied and unoccupied interior feature spans at least two unit pixels.

**Theorem.** For every integer \(N\) with \(14\le N\le21\), two such length-\(N\) apertures with equal Fourier-transform magnitudes at every real frequency are related by reflection about the midpoint of their common span (or by translation before normalization). At \(N=22\), exactly one unordered pair of inequivalent reflection classes has equal magnitudes. Representatives are the following two length-22 words:

```
A = 1110011000111110000011
B = 1110000011111001100011
```

Their seven run/gap length tuples are, respectively, \((3,2,2,3,5,5,2)\) and \((3,5,5,2,2,3,2)\). Consequently \(22\) is the sharp first ambiguous span within this precisely defined two-pixel, four-interval class, and the ambiguous pair is unique up to translation, reflection and exchanging the two apertures. No claim is made about spans above \(22\), arbitrary real endpoints, fewer or more intervals, or smaller feature widths.

## Assumptions and scope

The Fourier transform convention is
\[
\widehat{\mathbf 1_{\Omega}}(\xi)=\int_{\mathbb R}\mathbf 1_\Omega(t)e^{-2\pi i\xi t}\,dt,\qquad \xi\in\mathbb R.
\]
The pixel size is normalized to \(1\). A configuration is represented by seven integers \((a,g_1,b,g_2,c,g_3,d)\), all at least \(2\), whose sum is \(N\); the four occupied intervals have widths \(a,b,c,d\) and the separating gaps have widths \(g_1,g_2,g_3\). The configurations are compared within this class, with reflections and translations counted as trivial symmetries. Since both endpoints are occupied, the normalized span equals the word length \(N\), and no admissible configuration exists for \(N<14\).

## Proof

**Step 1: Fourier data equal aperiodic correlations.** Let \(P_w(z)=\sum_{j=0}^{N-1}w_jz^j\) and \(K(\xi)=\int_0^1e^{-2\pi i\xi t}\,dt\). Then
\[
\widehat{\mathbf1_{\Omega_w}}(\xi)=K(\xi)P_w(e^{-2\pi i\xi}).
\]
The nonzero values of \(K\) are dense, so equality of the continuous magnitudes is equivalent, by continuity, to equality of \(|P_w(z)|^2\) on the unit circle. For the integer aperiodic correlations
\[
C_w(h)=\sum_{j=0}^{N-1-h}w_jw_{j+h}\quad (0\le h<N),
\]
we have the Laurent identity \(P_w(z)P_w(z^{-1})=C_w(0)+\sum_{h=1}^{N-1}C_w(h)(z^h+z^{-h})\). Thus equality of continuous Fourier magnitudes is **equivalent** to equality of all \(C_w(h)\). The endpoint condition gives \(C_w(N-1)=1\), identifying the span from the correlation support even if different normalized lengths were allowed.

**Step 2: Exact finite classification.** For each \(N=14,15,\ldots,22\), enumerate the seven-tuples \(t=(t_1,\ldots,t_7)\) of integers at least \(2\) with sum \(N\). Write \(r=N-14\). All such tuples occur exactly once by choosing six strictly increasing cut positions from \(1,\ldots,r+6\), taking successive segment lengths and adding one to each segment length. There are exactly \(\binom{r+6}{6}\) tuples. Reversing the word reverses the seven-tuple. Retaining precisely those tuples lexicographically not exceeding their reversal selects one representative of every reflection class. A tuple is fixed under reflection exactly when its first, second and third coordinates equal its seventh, sixth and fifth; hence the number of fixed tuples is \(\binom{\lfloor r/2\rfloor+3}{3}\). Burnside's formula therefore independently checks that the class count is
\[
\frac{1}{2}\left[\binom{r+6}{6}+\binom{\lfloor r/2\rfloor+3}{3}\right].
\]
For each selected word, compute its complete correlation tuple \((C_w(0),\ldots,C_w(N-1))\) using exact integer bit intersections. Group these tuples, and reject any assumption of uniqueness whenever distinct reflection classes share a correlation tuple. `CHECK.py` implements these operations without floating point and includes independent pair-counting checks of the two exceptional correlations. Its complete counts are:

| \(N\) | Ordered tuples | Reflection classes | Distinct correlation tuples | Nontrivial fibers |
| ---: | ---: | ---: | ---: | ---: |
| 14 | 1 | 1 | 1 | 0 |
| 15 | 7 | 4 | 4 | 0 |
| 16 | 28 | 16 | 16 | 0 |
| 17 | 84 | 44 | 44 | 0 |
| 18 | 210 | 110 | 110 | 0 |
| 19 | 462 | 236 | 236 | 0 |
| 20 | 924 | 472 | 472 | 0 |
| 21 | 1716 | 868 | 868 | 0 |
| 22 | 3003 | 1519 | 1518 | 1 |

At the final span, the unique nontrivial fiber has exactly two reflection classes; the checker independently asserts that their representatives are exactly the words \(A,B\) displayed in the theorem. This is an exhaustive **finite** verification, because the seven-tuple parametrization is a bijection onto the entire stipulated aperture class, all possible tuples for each permitted \(N\) are visited, and every comparison uses the complete exact correlation vector. It is not an extrapolation from sampled experiments.

**Step 3: Explicit algebraic ambiguity witness.** Define
\[
F(z)=1-z^3+z^5,\qquad
G(z)=\sum_{j=0}^{6}z^j+\sum_{j=12}^{16}z^j.
\]
Direct integer polynomial multiplication gives
\[
P_A(z)=F(z)G(z),\qquad
P_B(z)=F(z)z^{16}G(z^{-1}).
\]
On \(|z|=1\), the real coefficients of \(G\) imply \(|z^{16}G(z^{-1})|=|G(z)|\), so \(|P_A(z)|=|P_B(z)|\). The words' run vectors are not reversals of each other, so the two normalized apertures are not related by reflection or translation. Both have all seven features at least two pixels wide. Their common complete correlation vector is
\[
(12,8,4,3,4,4,4,4,5,5,5,4,3,2,2,2,1,0,1,2,2,1).
\]
The exact enumeration in Step 2 proves minimality and uniqueness in the stated class.

## Verification

Run `python3 CHECK.py` with Python 3.10 or later; no nonstandard packages are required. The checker visits all \(6{,}435\) ordered seven-tuples and all \(3{,}270\) reflection classes, asserts the independently derived class totals, compares all exact aperiodic correlations, and checks the stated exceptional words and polynomial identities. It prints `CHECK_OK raw_compositions=6435 reversal_classes=3270 first_span=22 exceptional_unordered_pairs=1` followed by all nine span-level counts. The code is a finite proof certificate for this finite classification, not a claim about all lengths or real-endpoint intervals.

## Relationship to prior work

Xia and Xu (2026, arXiv:2606.19855) analyze continuous Fourier phase retrieval of indicator functions of finite unions of intervals, prove uniqueness for at most two intervals, and construct ambiguities for each larger number of intervals. Their general factor-reversal viewpoint is consistent with the witness above. The specific smallest integer-grid span and exact first-fiber classification under a **simultaneous two-pixel minimum for all four occupied intervals and all three gaps** is not supplied by the inspected theorem and construction statements. Willms (2012, arXiv:1206.4572) gives run-structural relations for binary autocorrelations; these provide context for the run parameterization but no identified classification matching this constrained four-run question. Earlier finite three-run classification with different width constraints is not a classification of this four-run class.

## Limitations

This is an exact, discrete, finite classification for the stipulated two-pixel feature-floor model through the first ambiguity. It does not prove that every higher-span four-run word is ambiguous, handle smaller/unequal pixel resolutions, characterize robustness under noisy Fourier magnitude, or classify arbitrary real interval endpoints. The finite certificate is readable and reproducible, but its correctness still depends on inspecting the code and its combinatorial exhaustiveness argument. Absolute originality cannot be guaranteed against unindexed older homometric-sequence classifications; independent audit has not been performed.

## References

1. Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855, first publicly posted 2026-06-18, https://arxiv.org/abs/2606.19855 .
2. Jürgen Willms, *Autocorrelations of Binary Sequences and Run Structure*, arXiv:1206.4572, first publicly posted 2012-06-20, https://arxiv.org/abs/1206.4572 .
