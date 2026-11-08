# A unique exceptional disjointness offset for powers of twice the golden ratio

## Finding
Let \(\alpha=1+\sqrt5=2\varphi\), with \(\varphi=(1+\sqrt5)/2\), and define \(R_m=\{\lfloor k\alpha^m\rfloor:k\in\mathbb Z_{\ge1}\}\). For all \(1\le i<j\), write \(d=j-i\). Then
\[
R_i\cap R_j=\varnothing\quad\Longleftrightarrow\quad d\text{ is odd and }(d\mid i\ \text{or}\ d=3).
\]
The exceptional distance three holds for **every** starting index, unlike the ordinary odd-divisor pattern. Every even distance admits an intersection. Every odd distance \(d\ge5\) has an intersection unless \(d\mid i\).

## Assumptions and scope
All indices and Beatty multipliers are positive integers. The number \(\alpha\) is irrational and exceeds one, so the Skolem--Bang theorem applies to every pair of \(\alpha^i,\alpha^j\). Fibonacci numbers are normalized by \(F_0=0,F_1=1,F_{n+2}=F_{n+1}+F_n\). Empty intersection is a statement about infinite Beatty sets, not a bounded numerical sample.

## Proof
The classical Skolem--Bang criterion for irrational \(u,v>1\) states that \(B(u)\cap B(v)=\varnothing\) exactly when positive integers \(r,s\) exist with \(r/u+s/v=1\). Applying this to \(u=\alpha^i,v=\alpha^{i+d}\), the condition becomes
\[
\alpha^{i+d}=r\alpha^d+s,\qquad r,s\in\mathbb Z_{>0}.
\]
The quadratic equation \(\alpha^2=2\alpha+4\) and Fibonacci recurrence give, by induction,
\[
\alpha^n=2^{n-1}F_n\alpha+2^nF_{n-1}\quad(n\ge1).
\]
Comparison of coefficients in the independent rational basis \(1,\alpha\) forces
\[
r=\frac{2^iF_{i+d}}{F_d},\qquad
s=(-1)^{d-1}\frac{2^{i+d}F_i}{F_d}.
\]
The second identity follows from the Fibonacci determinant identity
\[
F_{i+d}F_{d-1}-F_{i+d-1}F_d=(-1)^dF_i.
\]
Since all Fibonacci numbers involved are positive, the sign of \(s\) first forces \(d\) odd. For odd \(d\), the Fibonacci residues modulo four have period six, with \(F_d\) odd if \(3\nmid d\) and \(F_d\equiv2\pmod4\) if \(3\mid d\). Therefore the two integer conditions for \(r,s\) reduce to \(H_d\mid F_i\), where \(H_d\) is the odd part of \(F_d\): the power of two in each numerator cancels any possible single factor two, and \(F_{i+d}=F_{d+1}F_i+F_dF_{i-1}\) shows that divisibility of \(F_i\) implies that of \(F_{i+d}\).

If \(d=1\) or \(d=3\), then \(H_d=1\), so every positive \(i\) qualifies. Suppose now that \(d\ge5\) is odd. If \(d\mid i\), then \(F_d\mid F_i\), so the condition holds. Conversely suppose \(H_d\mid F_i\). Strong divisibility gives \(\gcd(F_d,F_i)=F_g\), where \(g=\gcd(d,i)\). Hence \(H_d\mid F_g\) and \(F_g\mid F_d\). Because \(F_d/H_d\) is either one or two, it follows that \(F_d/F_g\le2\). If \(g<d\), however, oddness implies \(g\le d/3\), and Fibonacci monotonicity implies \(F_d>2F_g\) for all odd \(d\ge5\): when \(g=1\), \(F_d\ge F_5=5>2F_1\); when \(g\ge2\), \(d\ge3g\ge g+2\) and \(F_{g+2}>2F_g\). This contradiction forces \(g=d\), i.e. \(d\mid i\). This proves both directions and exhausts all indices.

## Verification
The standalone `verify.py` uses exact Fibonacci integers to compare the derived Skolem--Bang divisibility criterion with the claimed classification on all \(25600\) pairs \((i,d)\) with \(1\le i,d\le160\). It separately constructs exact Beatty terms using integer square roots and checks all predicted empty intersections for row pairs with indices at most seven in a finite window. The checked power identity also gives \(\alpha^4=3\alpha^3+8\), illustrating the universal exceptional distance. `python3 verify.py` prints `VERIFY_OK`. The infinite theorem rests on the proof above, not on finite experiments.

## Relationship to prior work
Ashburn (2026), Theorem 7, classifies disjoint rows for powers of the golden ratio and, in Theorem 9, for quadratic units satisfying \(x^2=cx+1\). Both give the odd-divisor criterion without an exceptional gap. The present base \(\alpha=2\varphi\) instead satisfies \(\alpha^2=2\alpha+4\), with norm \(-4\), and its exceptional distance three changes the complete classification. This uses the classical Skolem--Bang theorem as input and makes no claim to discover that theorem or Fibonacci strong divisibility. Pongsriiam's earlier study concerns the powers of \(\varphi\) themselves. The comparison concerns mathematical implications, not merely titles.

## Limitations
This is a classification for precisely the natural quadratic base \(\alpha=2\varphi\); it does not classify all nonunit quadratic bases or simultaneous intersections of three or more Beatty sequences. The result is unreviewed by an independent mathematical auditor. Historical priority is subject to potentially unindexed literature. The finite verification is supporting evidence rather than an independent infinite proof.

## References
1. A. Ashburn, *On three conjectures of Kimberling concerning the array* \(\lfloor k\varphi^n\rfloor\), arXiv:2610.05776v1 (first posted 2026-10-05), Theorems 6, 7 and 9, https://arxiv.org/abs/2610.05776.
2. P. Pongsriiam, *Combinatorial structure and sumsets associated with Beatty sequences generated by powers of the golden ratio*, Electronic Research Archive 30 (2022), 2385–2405, https://doi.org/10.3934/era.2022121.
3. T. Skolem, *On certain distributions of integers in pairs with given differences*, Math. Scand. 5 (1957), and T. Bang, *On the sequence* \(\lfloor n\alpha\rfloor\), Math. Scand. 5 (1957), as recorded in Ashburn's Theorem 6.
