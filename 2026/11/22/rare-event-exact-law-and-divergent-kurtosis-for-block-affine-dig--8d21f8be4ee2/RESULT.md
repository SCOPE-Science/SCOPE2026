# Rare-event exact law and divergent kurtosis for block-affine digital quadrature

## Finding

For every pair of integers \(e\ge2\), \(m\ge1\), put \(N=2^{em}\). Scramble the complete one-dimensional binary grid of \(N\) points using a single infinite block-affine randomization of width \(e\). For the smooth benchmark integrand \(f(x)=x\), the error \(E_N\) has exactly the rare-event Rademacher-series law

\[
E_N\overset{d}{=}\frac1{2N}\sum_{j=1}^{\infty}2^{-j}B_jR_j,
\qquad B_j\stackrel{\mathrm{iid}}{\sim}\mathrm{Bernoulli}(1/N),
\quad R_j\stackrel{\mathrm{iid}}{\sim}\{-1,+1\}.
\]

All displayed sign variables and activation variables are mutually independent. In particular,

\[
\mathbb E E_N=0,\qquad
\operatorname{Var}(E_N)=\frac1{12N^3},\qquad
\mathbb E E_N^4=\frac{N+2}{240N^6},\qquad
\frac{\mathbb E E_N^4}{(\mathbb E E_N^2)^2}=\frac{3(N+2)}5.
\]

At fixed block width as \(m\to\infty\), the probability-normalized and logarithmic errors satisfy

\[
\sqrt{12N^3}\,E_N\xrightarrow{\mathbb P}0,
\qquad
\frac{-\log_2(2N|E_N|)}{N}\ \Rightarrow\ \mathrm{Exp}(1).
\]

By contrast, fully nested *uniform* binary scrambling of the same grid produces independent uniform jitter inside each dyadic stratum. Its variance is also \(1/(12N^3)\), but its standardized kurtosis is \(3-6/(5N)\) and its standardized error has a Gaussian limit. Thus identical exact mean-square errors conceal sharply different replication-error distributions.

## Assumptions and scope

The unscrambled input is the set \(\{a/N:0\le a<N\}\) with binary expansions terminating after \(em\) digits. The block-affine scramble is exactly the random map of Suzuki [1, Definition 2.14], specialized to binary digits in one coordinate: an infinite block lower-triangular binary matrix with independent uniform elements of \(\mathrm{GL}(e,2)\) on diagonal blocks and independent uniformly distributed binary \(e\times e\) matrices below diagonal, plus independent fair binary digit shifts. One single sampled random map acts on all \(N\) grid points; rows and shifts beyond digit \(em\) remain random. The integrand is precisely \(f(x)=x\) on \([0,1)\), with exact integral \(1/2\). A finite-digit implementation obeys the analogous truncated formula, not the infinite-digit identities unless its remaining tail is randomized as specified.

## Proof

**Prefix balance.** The first \(em\) scrambled output digits are an invertible affine transform on the entire space \(\mathbb F_2^{em}\). Since all input vectors occur once, the output prefixes run over all \(2^{em}=N\) possibilities. Their contribution to the average is therefore \((N-1)/(2N)\), i.e. exactly \(1/2-1/(2N)\), regardless of the random prefix transformation.

**Post-prefix digit law.** For output digit position \(em+j\) with \(j\ge1\), the corresponding random matrix row restricted to the first \(em\) input digits is a uniform element of \(\mathbb F_2^{em}\). Uniformity and independence across different suffix digit positions follow because each earlier block is an independently sampled unrestricted matrix, whose rows are themselves independent; the random shift bits are also independent. A nonzero restricted row is a balanced linear functional on the complete input cube, giving average output bit exactly \(1/2\). A zero restricted row, of probability exactly \(1/N\), gives the constant output bit equal to the random shift, and thus average deviation \(R_j/2\), where \(R_j\) is a fair sign. The contribution of that bit to the integration error is \(2^{-(em+j)}R_j/2 = 2^{-j}R_j/(2N)\). Summing all absolutely convergent suffix contributions proves the exact law. The prefix's deficit of \(1/(2N)\) is precisely canceled by the mean \(1/(2N)\) of the unused binary tail, so the series is centered at the true integral.

**Second and fourth moments.** Put \(p=1/N\). The independent centered terms have second moments \(p4^{-j}\) and fourth moments \(p16^{-j}\). The identities \(\sum_{j\ge1}4^{-j}=1/3\) and \(\sum_{j\ge1}16^{-j}=1/15\) give

\[
\begin{aligned}
\mathbb E E_N^2&=\frac{p}{4N^2}\frac13,\\
\mathbb E E_N^4&=\frac{1}{16N^4}
\left[\frac p{15}+3p^2\left(\frac19-\frac1{15}\right)\right].
\end{aligned}
\]

Simplifying proves the three stated moment identities and the linearly diverging standardized kurtosis.

**The logarithmic limiting law.** Let \(J_N=\min\{j\ge1:B_j=1\}\). Since \(J_N\) is geometric with success probability \(1/N\), \(J_N/N\Rightarrow\mathrm{Exp}(1)\). Conditional on \(J_N\), the probability that the following two activations vanish is \((1-1/N)^2\to1\). On that event the first active term dominates the entire remaining dyadic tail:

\[
\frac34 2^{-J_N}\le
\left|\sum_{j\ge1}2^{-j}B_jR_j\right|
\le\frac54 2^{-J_N}.
\]

Consequently, \(-\log_2(2N|E_N|)=J_N+O(1)\) with probability tending to one, yielding the claimed exponential limit. For fixed \(N\), cancellation to precisely zero has probability zero: the first nonzero dyadic term could be exactly canceled only if every subsequent index were activated with the opposite sign, an event of probability zero. The exponential log law also implies \(\sqrt{12N^3}E_N\to0\) in probability, since \(J_N\) grows faster than \(\log_2N\) with probability tending to one.

**Fully nested comparator.** Each dyadic interval contains exactly one sampled point under fully nested *uniform* binary scrambling, and the binary digits after its distinguishing \(em\)-bit prefix are independent fair bits across distinct intervals. Thus these positions are independent uniforms \(U_a\) within their respective strata, with \(E_N^{\mathrm{nested}}=N^{-2}\sum_{a=0}^{N-1}(U_a-1/2)\). As \(\operatorname{Var}(U_a)=1/12\), \(\mathbb E(U_a-1/2)^4=1/80\) and fourth cumulant \(-1/120\), the formula for nested kurtosis follows, and the ordinary i.i.d. central limit theorem proves its Gaussian limit. This comparator does not assert that all block-wise fully nested scrambles have identical properties.

## Verification

The standalone Python program `verify.py` performs independent exact-rational checks of finite-suffix distributions and moments for \(N\in\{4,16,64\}\), directly enumerates uniformly sampled off-diagonal binary masks and shifts for a small complete input cube, and verifies the infinite-series moment formulas for six grid sizes. Run from a directory containing the file with `python verify.py`; the reviewed execution returned `VERIFY_OK 96`. Finite computations corroborate, but cannot replace, the analytic proof for arbitrary \(e,m\) and infinitely many digits.

## Relationship to prior work

Suzuki [1] introduces block-affine scrambling, its mixed-base equidistribution properties, gain-coefficient formulas, and variance bounds, and explicitly compares ordinary and coarse scrambling on one-coordinate projections. That established machinery is used as the definition, not claimed as new. Liu [2] studies median estimators and reports empirically increasingly heavy-tailed affine-scramble errors; its discussion identifies formal tail analysis as unresolved, but a later scholarly priority check may find other exact special cases. Yue and Hickernell [3] establish earlier gain-coefficient and discrepancy formulas, which concern second-order precision rather than the exact higher-order and logarithmic laws here. The new contribution claimed is restricted to the *joint* explicit series distribution, exact kurtosis, logarithmic exponential scale, and variance-matched fully nested comparison for the specified linear benchmark. No priority claim is made for the general observation that affine-scrambled integration errors can show rare outliers.

## Limitations

The theorem concerns a single smooth one-dimensional integrand and a complete dyadic grid under infinite random-digit block-affine scrambling. It gives no general bound on higher-dimensional integrands, actual error estimation from a finite number of independent scrambles, or the runtime merits of an implementation. The law is bounded for each \(N\), so divergent *standardized kurtosis* should not be interpreted as a Pareto tail at any fixed \(N\). Publicly accessible literature comparisons do not certify exhaustive historical priority. No independent validation has been performed.

## References

[1] Kosuke Suzuki, *Coarse scrambling for Sobol' and Niederreiter sequences*, arXiv:2510.02111v1, posted 2025-10-02, especially Definition 2.14 and Sections 3–5. https://arxiv.org/abs/2510.02111

[2] Yang Liu, *Affine matrix scrambling achieves smoothness-dependent convergence rates*, arXiv:2505.00411v1, posted 2025-05-01; a later version was withdrawn. Especially Section 5.2 and Discussion. https://arxiv.org/abs/2505.00411

[3] Rong-Xian Yue and Fred J. Hickernell, *The Discrepancy and Gain Coefficients of Scrambled Digital Nets*, Journal of Complexity 18 (2002), 135–151, https://doi.org/10.1006/jcom.2001.0630
