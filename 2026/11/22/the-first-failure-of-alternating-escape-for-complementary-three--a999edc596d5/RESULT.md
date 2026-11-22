# The first failure of alternating escape for complementary three-bit moving holes

## Finding

Consider the doubling transformation \(T(x)=2x\bmod 1\) of \([0,1)\). At each nonnegative integer time \(i\), a predetermined binary symbol \(s_i\) opens the half-open hole \(H_0=[0,1/8)\) when \(s_i=0\), or \(H_1=[7/8,1)\) when \(s_i=1\). Let \(C_n(s)\) be the number of length-\(n+2\) binary words whose three-bit block at position \(i\) is not \(s_i s_i s_i\), for every \(0\le i<n\). The probability of surviving all \(n\) observations is \(P_n(s)=C_n(s)/2^{n+2}\).

**Sharp first reversal.** For every horizon \(1\le n\le4\), an alternating schedule \(0101\cdots\) minimizes \(C_n\) among all \(2^n\) schedules. At horizon \(n=5\), the strict improvement occurs for the first time: the minimum is \(64\), attained by exactly the four schedules `01001`, `01101`, `10010`, `10110`, whereas either alternating schedule has count \(65\). In particular the period-three schedule \(010010\cdots\) has \(P_5=1/2\) while alternation has \(P_5=65/128\).

**Infinite-horizon reversal.** Let \(a=(01)^\infty\) and \(b=(010)^\infty\). Their exponential survivor-word growth rates exist and satisfy
\[
 \lim_{n\to\infty} C_n(a)^{1/n}=\lambda_2^{1/2},\qquad
 \lim_{n\to\infty} C_n(b)^{1/n}=\lambda_3^{1/3},
\]
where \(\lambda_2\) and \(\lambda_3\) are respectively the unique real roots of
\[
 p_2(t)=t^3-2t^2-3t-1,\qquad
 p_3(t)=t^3-6t^2+4t-1.
\]
They obey the *strict reverse ordering*
\[
 \lambda_3^{1/3}<\lambda_2^{1/2},
\]
so the three-phase schedule has strictly faster asymptotic Lebesgue escape than strict alternation. Numerically, the survivor growth rates are approximately \(1.74110200\) and \(1.75487767\), respectively; the corresponding escape rates are \(\gamma(b)=\log2-\frac13\log\lambda_3\) and \(\gamma(a)=\log2-\frac12\log\lambda_2\). These are comparisons between two specified schedules, **not** an assertion that the three-phase schedule is globally optimal at every horizon or among all infinite schedules.

## Assumptions and scope

Binary codings are taken outside the countable set of dyadic endpoints, which does not affect Lebesgue probabilities. The schedule is exogenous and chosen before the starting point is known. The count \(C_n\) concerns \(n\) hole tests on \(n+2\) consecutive digits (not \(n\) digits); it includes precisely those words that pass every test. Every such finite word extends to an infinite surviving word, because a choice of next digit can always avoid the single prohibited three-block. The exponential comparisons concern the stated periodic schedules and the growth of their allowed finite prefixes; no time-one-invariant autonomous survivor shift is postulated.

The problem belongs primarily to symbolic dynamics, MSC2020 37B10. The exact first-horizon boundary and comparison of escape rates concern binary moving cylinders of depth three; no analogous conclusion for every depth or all hole locations is asserted.

## Proof

**1. Exact transfer matrices.** Index the four length-two suffix states in the order \(00,01,10,11\), and let \(v=(v_{00},v_{01},v_{10},v_{11})^{\mathsf T}\) count admissible prefixes in each state. Initialize \(v_0=(1,1,1,1)^{\mathsf T}\). Appending a digit while excluding `000` or `111` at the new check gives respectively
\[
 M_0=\begin{pmatrix}
 0&0&1&0\\1&0&1&0\\0&1&0&1\\0&1&0&1
 \end{pmatrix},\qquad
 M_1=\begin{pmatrix}
 1&0&1&0\\1&0&1&0\\0&1&0&1\\0&1&0&0
 \end{pmatrix}.
\]
Consequently for every finite binary schedule \(s=s_0\cdots s_{n-1}\),
\[
 C_n(s)=\boldsymbol1^{\mathsf T}M_{s_{n-1}}\cdots M_{s_0}\boldsymbol1.
\]
This identity follows by induction on \(n\) from the possible suffix transitions, independently of any limiting argument.

**2. Finite-horizon optimum.** The displayed integer matrices reduce the exhaustive small-horizon search to simple exact finite arithmetic. The complete minimum counts for \(n=1,2,3,4,5\) are respectively \(7,12,21,37,64\); the two alternating schedules attain these first four minima. At \(n=5\), exactly `01001`, `01101`, `10010`, `10110` attain \(64\), and both alternating schedules have count \(65\). This finite exhaustive assertion is independently proved by iterating the transfer rule for all \(2+4+8+16+32=62\) schedules, and the standalone program separately enumerates all \(2^{n+2}\) binary source words for each schedule and confirms every count. Since the state space and ranges are explicitly exhausted, this is an exhaustive finite proof, not a sample or extrapolation. This also proves the sharpness of the first reversal.

**3. Exact period matrices.** Grouping restrictions by periods gives
\[
 P_2=M_1M_0=\begin{pmatrix}
 0&1&1&1\\0&1&1&1\\1&1&1&1\\1&0&1&0
 \end{pmatrix},\quad
 P_3=M_0M_1M_0=\begin{pmatrix}
 1&1&1&1\\1&2&2&2\\1&1&2&1\\1&1&2&1
 \end{pmatrix}.
\]
Direct determinant expansion yields
\[
 \det(tI-P_2)=t\,p_2(t),\qquad
 \det(tI-P_3)=t\,p_3(t).
\]
The product \(P_2^2\) has all entries strictly positive; \(P_3\) already has all entries strictly positive. Hence they are primitive and Perron–Frobenius theory gives the asserted limits, not merely subsequence estimates.

**4. Certified strict inequality.** The cubic discriminants are \(-23\) for \(p_2\) and \(-139\) for \(p_3\), so each has a unique real root. Exact rational sign evaluation isolates these roots in
\[
 \frac{3079595}{10^6}<\lambda_2<\frac{3079596}{10^6},\qquad
 \frac{5278039}{10^6}<\lambda_3<\frac{5278040}{10^6}.
\]
The integer inequality
\[
 \left(\frac{5278040}{10^6}\right)^2 <
 \left(\frac{3079595}{10^6}\right)^3
\]
is exact (multiply by \(10^{18}\) to check). It follows that \(\lambda_3^2<\lambda_2^3\), equivalently \(\lambda_3^{1/3}<\lambda_2^{1/2}\). Finally, for a periodic schedule of period \(p\), its survival probability is \(C_n/2^{n+2}\); dividing logarithms by \(n\) gives escape rate \(\log2-(1/p)\log\rho(P_p)\). Thus the spectral inequality is a strict asymptotic escape-rate advantage, completing the proof.

## Verification

Run `python verify.py` with standard Python 3. The program constructs the two transition matrices explicitly, computes the characteristic polynomials through exact determinant interpolation, checks rational root brackets, confirms the integer inequality, and independently enumerates every source word for each of the \(510\) schedules of lengths one through eight. It confirms all transfer counts and the sharp horizon-five minimizers. All assertions passed. This independently corroborates the finite calculation and spectral coefficients; the infinite growth-rate step follows from the explicitly established primitive matrix products and Perron–Frobenius theory.

## Relationship to prior work

Kong, Sun and Wang, *Open dynamical systems with a moving hole* (first public 2025-05-05), develop dimension and transfer-matrix theorems for moving cylinder holes over alphabets of size at least three. Their final remarks explicitly exclude the binary base from their proofs; the inspected theorem statements and proofs do not determine the sharp binary two-hole scheduling reversal or the two exact period polynomials here. Their matrix approach is a precursor, not a claim of independent invention of transfer-matrix methods.

Two publicly available exact switching results concern the **length-two** endpoint cylinders `00` and `11`: *Sharp moving-hole escape envelopes and a zero-entropy alternating phase for the doubling map* and *Optimal alternating Markov-hole escape in integer expanding maps*. Both establish strict alternation's all-horizon optimality in that smaller-hole-depth setting. The present theorem exhibits precisely where that natural extrapolation fails: **depth three, first at five observations**, and with a genuine spectral inversion that survives asymptotically. The nearby published bigram overlap-code theorem applies only to length-two forbidden blocks over alphabets of size at least three. A different analysis of periodically breathing *nested* zero-holes concerns time-varying widths, not switches between equal-width opposite cylinders.

Kong, Li, Ma and Simon (2026-10-22) extend moving-hole dimension theory to inhomogeneous systems with at least three symbols; the inspected abstract does not evaluate these binary switching schedules, but its full text was not accessible in this inspection. Classical transfer-matrix enumeration, finite-type constrained-code presentations, and Perron spectral growth are not claimed as new. The novelty claim is the *evaluated sharp first failure and two-period asymptotic reversal*; historical priority is not proven by database search alone.

## Limitations

Only binary base, equal length-three complementary endpoint cylinders, Lebesgue initial law, and predetermined schedules are studied. The four minimizers are classified only at the specified first failure horizon, and no optimality among all long-period or aperiodic schedules is asserted. Generic constrained-coding and moving-hole matrix formulas can compute related cases; a complete historical priority check of every coding-theory capacity table has not been performed. The recent inhomogeneous moving-hole paper was inspected at abstract level only; this is a residual historical-coverage risk. No independent mathematical audit has been performed.

## References

1. D. Kong, B. Sun, Z. Wang, *Open dynamical systems with a moving hole*, arXiv:2505.02336v1, first public 2025-05-05. https://arxiv.org/abs/2505.02336 . Sections 1.1, 2–3, 6.
2. D. Kong, K. Li, C.-Y. Ma, K. Simon, *Open dynamics with a moving hole: inhomogeneous IFS and exponential separation condition*, arXiv:2610.31128v1, first public 2026-10-22. https://arxiv.org/abs/2610.31128 . Abstract inspected.
3. *Sharp moving-hole escape envelopes and a zero-entropy alternating phase for the doubling map*, publicly available result at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-moving-hole-escape-envelopes-and-a-zero-entropy-alternatin--91c8d26540fd . Full RESULT.md inspected.
4. *Optimal alternating Markov-hole escape in integer expanding maps*, publicly available result at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-optimal-alternating-markov-hole-escape-in-integer-expanding-maps--962cd78c291c . Full RESULT.md inspected.
5. *Complete overlap-code classification of moving two-digit holes*, publicly available result at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-overlap-code-classification-of-moving-two-digit-holes--f19d7b26fc6b . Full RESULT.md inspected.
6. *Sharp phase-ordering coefficients for periodically breathing dyadic holes*, publicly available result at https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-phase-ordering-coefficients-for-periodically-breathing-dya--6dadc656cf56 . Full RESULT.md inspected.
7. T.-L. Poo and B. H. Marcus, *Time-Varying Maximum Transition Run Constraints*, IEEE Transactions on Information Theory **52** (2006), 4464–4480. DOI 10.1109/TIT.2006.881706. Abstract and indexed technical excerpts inspected, full text not independently analyzed.
