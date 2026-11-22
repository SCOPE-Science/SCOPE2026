# Exact bfloat16 cycle spectra under two arithmetic orders of a remainder-added linear map

## Finding

Consider the remainder-added linear map introduced by Moysis, Kafetzis, Baptista and Volos (2022, equation (23)), at the parameter values used in their Figure 5:
\[
 H(x)=\frac{x}{10}+\operatorname{rem}(100x,1),\qquad x\geq0,
\]
where \(\operatorname{rem}(y,1)=y-\lfloor y\rfloor\) for nonnegative \(y\). Let \(\mathcal S\) be all **16,385 distinct nonnegative bfloat16 values** in \([0,2]\), including subnormal numbers and positive zero, with negative zero omitted. Let \(R\) be bfloat16 round-to-nearest, ties-to-even. The two precise deterministic state maps are
\[
 \begin{aligned}
 A(x)&=R\!\left(\frac{x}{10}+\operatorname{rem}(100x,1)\right),\\
 B(x)&=R\!\left(R(x/10)+\operatorname{rem}(R(100x),1)\right).
 \end{aligned}
\]
In \(A\), the complete real-valued expression is evaluated exactly and rounded once. In \(B\), the product and division are rounded separately, the fractional part of the rounded product is exact, and the final sum is rounded. Both maps send \(\mathcal S\) into itself.

For every starting state in \(\mathcal S\), the eventual primitive cycle and number of transient steps are completely classified by the following tables. The basin count is **the number of representable starting encodings**, not Lebesgue measure. The representative is the minimum hexadecimal positive-code bit pattern belonging to the cycle.

| Once-rounded \(A\): representative | Primitive period | Complete basin size |
| --- | ---: | ---: |
| `0000` | 1 | 1 |
| `3d68` | 18 | 2,040 |
| `3de8` | 24 | 14,344 |

| Staged \(B\): representative | Primitive period | Complete basin size |
| --- | ---: | ---: |
| `0000` | 1 | 1 |
| `3f0e` | 1 | 1,326 |
| `3d72` | 3 | 11,103 |
| `3d6a` | 3 | 3,221 |
| `3c03` | 3 | 537 |
| `3c13` | 3 | 117 |
| `3b83` | 3 | 58 |
| `3ba4` | 3 | 8 |
| `3a83` | 3 | 7 |
| `3b03` | 3 | 7 |

Thus the once-rounded system has exactly three cycles, with maximum period \(24\), while the staged system has exactly ten cycles, with all primitive periods at most \(3\). Their maximal entry-to-cycle preperiods are respectively \(51\) and \(44\) steps. Their immediate successors differ on exactly \(3,545\) of the \(16,385\) starting encodings. In particular, inserting intermediate rounding changes the entire nonzero recurrent period spectrum from \(\{18,24\}\) to \(\{1,3\}\), with eight distinct primitive three-cycles.

## Assumptions and scope

A nonnegative bfloat16 code is the 16-bit integer \(j\in\{0,1,\ldots,\texttt{0x4000}\}\) interpreted as a positive IEEE-like bfloat16 floating-point value. Both signed zeros would denote the same real state; only positive zero is included. There are \(\texttt{0x4000}+1=16,385\) such codes, including all positive subnormal values. Rounding is exact real round-to-nearest with ties resolved to an even trailing significand bit, with no flush-to-zero, stochastic rounding, overflow, compiler re-association, or fused-operation assumptions.

All inputs and all outputs lie in \([0,2]\). Indeed \(0\le H(x)<1.2\) for \(0\le x\le2\). For \(B\), the separately rounded quotient \(R(x/10)\) is at most \(R(1/5)\), and the exact fractional part of a rounded product is less than one, so even final rounding remains below two. Every rounded product \(R(100x)\) is between zero and \(200\), hence finite and within the auxiliary bfloat16 table up to \(256\).

This is a complete finite-state theorem for these specified evaluation orders, not a theorem asserting that real-valued chaotic orbits become periodic or that a specific physical processor necessarily implements either order. The classification uses the parameter values \(k=10\), \(a=100\), \(N=1\) of the source's illustrated linear case; it does not select arbitrary parameters after seeing the outcomes.

## Proof

**1. Exact encoding.** Put \(Q=2^{133}\). Write \(j=128e+f\) with exponent field \(e\) and fraction field \(0\le f<128\). If \(e=0\), the exact bfloat16 value is \(x_j=f/Q\). For \(e>0\), it is
\[
 x_j=\frac{(128+f)2^{e-1}}{Q}.
\]
Thus \(v_j=Qx_j\) is an integer for every enumerated code, and the integers \(v_j\) are strictly increasing. This includes subnormals, exact normal-exponent boundaries and both endpoints.

**2. Exact successor identities.** Define \(\mathcal R_d(m)\) to be the index of the bfloat16 number closest to the exact rational \(m/(dQ)\), resolving an exact midpoint toward the even encoded significand. It is computed by binary search among the ordered exact integers \(v_j\), followed by integer comparison of both distances. Let \(\mathcal R_d^+(m)\) be the same rounding lookup allowing auxiliary codes through \(\texttt{0x4380}\), which represents \(256\). The exact successor codes satisfy
\[
 \begin{aligned}
 a_j&=\mathcal R_{10}\left(v_j+10(100v_j\bmod Q)\right),\\
 p_j&=\mathcal R_1^+(100v_j),\quad \ell_j=\mathcal R_{10}(v_j),\\
 b_j&=\mathcal R_1\left(v_{\ell_j}+(v_{p_j}\bmod Q)\right).
 \end{aligned}
\]
Here \(a_j\) and \(b_j\) are the output bit-pattern indices; the exact integer remainder is valid because all relevant values are nonnegative. The auxiliary index \(p_j\) uses the extended table. No binary floating-point arithmetic enters this computation.

**3. Exhaustive graph classification.** The file `check.py` constructs \((a_j)\) and \((b_j)\) for **all** \(j=0,\ldots,16,384\). It recomputes every edge with a separate `Fraction`-based implementation using a different rounding search and exact rational fractional parts. All \(32,770\) successor determinations agree. A path-tracing graph algorithm then decomposes each deterministic map into its simple directed cycles and disjoint basins; an independent in-degree-elimination algorithm recomputes the same cycle vertex sets and basin multisets. Both compute the maximum transient lengths by back propagation.

The exact decomposition produces the two displayed cycle-and-basin tables, with basin sums each equal to \(16,385\). The cycle lengths are primitive because the cyclic vertices are recorded between the first repeated vertex and its preceding occurrence, without duplicates. Every state is visited by both algorithms, so the tables are exhaustive, not estimates from sampled trajectories. Finally, the bit-by-bit successor comparison counts exactly \(3,545\) differences. These finite integer identities constitute a reproducible exhaustive proof of the stated finite-state theorem.

## Verification

Run `python3 check.py` in a standard Python 3 installation. It uses only the standard library, exact integer comparisons and `fractions.Fraction`; neither NumPy nor an implementation-specific bfloat16 runtime is required. The output lists every cycle's complete hexadecimal member set and basin count. The final line is `complete independent exact-rational edge and graph checks PASS`.

The two independent edge constructions agree for every state; the independent path-tracing and Kahn-elimination decompositions agree on cycle memberships, basin sizes and maximal transient lengths. The cycles and the exact successor tables are recomputed each run. The checker is part of this package and is the computational certificate, not merely a log of an earlier experiment.

## Relationship to prior work

Moysis, Kafetzis, Baptista and Volos (2022) introduced this very recurrence in their equation (23), with the present parameters displayed in Figure 5. Their analysis concerns real-valued phase plots, Lyapunov exponents, unstable periodic points and pseudo-random-bit generation; it does not give a complete bfloat16 successor graph or distinguish the two arithmetic orders above. Their discussion of numerical accuracy and digit mixing motivates testing the precise rounding stages.

Klöwer, Coveney, Paxton and Palmer (2023) showed that deterministic low-precision simulations can have short periodic orbits, and studied logistic and generalized Bernoulli systems, including bfloat16. That general mechanism is prior knowledge and is **not** the novelty claim here. Earlier exact studies of differently rounded binary16 Bernoulli and logistic maps likewise establish the general sensitivity to evaluation order, not the particular combined remainder-plus-contraction map, its complete cycle representatives, basin counts, or the strong period-three staged restriction proved here. A prior analysis of the same real remainder-added family classified its confinement boundary and transport at a different parameter and exact-real semantics; those results do not determine the present rounded graphs.

The contribution is this natural, full-precision-format, source-parameter finite census with two explicit arithmetic orders, revealing an exact change in the full recurrent structure of a published robust-chaos construction. No new general theorem about arbitrary low-precision systems is asserted.

## Limitations

The results are exact for **these** two bfloat16 evaluation semantics only. A different order of operations, rounding mode, precision, remainder convention on negative values, subnormal policy or state interval could give a different graph. These results do not establish security, randomness, physical device behavior or a Lebesgue-measure claim. The finite-state phenomenon should not be confused with a loss of expansion in the underlying exact-real map. Publication-priority conclusions are limited to the primary texts and published mathematical results inspected; unindexed equivalent computations may exist. No independent mathematical audit has been conducted.

## References

1. L. Moysis, I. Kafetzis, M. S. Baptista and C. Volos, *Chaotification of One-Dimensional Maps Based on Remainder Operator Addition*, Mathematics **10** (2022), 2801; published 2022-08-07. DOI: `10.3390/math10152801`. Full text: https://www.mdpi.com/2227-7390/10/15/2801.
2. M. Klöwer, P. V. Coveney, E. A. Paxton and T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, Scientific Reports **13** (2023), 11410; published 2023-07-14. DOI: `10.1038/s41598-023-37004-4`. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC10349059/.
3. *Two exact cycle spectra for differently rounded half-precision beta shifts*, published mathematical result, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-exact-cycle-spectra-for-differently-rounded-half-precision-b--384041ddfda5.
4. *A sharp confinement transition and exact golden-ratio transport statistics for a remainder-added linear map*, published mathematical result, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-sharp-confinement-transition-and-exact-golden-ratio-transport--2024fba9948d.
