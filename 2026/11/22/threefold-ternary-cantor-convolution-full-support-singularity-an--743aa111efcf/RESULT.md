# Exact typical digit frequencies of a threefold 3-adic Cantor sum

## Finding

Let \(X_i=\sum_{j\ge0}\epsilon_{i,j}3^j\), for \(i=1,2,3\), where the \(\epsilon_{i,j}\) are mutually independent with probability \(1/2\) for each of \(0,1\). In \(\mathbb Z_3\) let \(\mu\) be the law of \(X_1+X_2+X_3\). Write the ternary digits of the sum in order from least to most significant. Then for \(\mu\)-almost every sum their empirical frequencies converge to
\[
(f_0,f_1,f_2)=\left(\frac{11}{40},\frac{14}{40},\frac{15}{40}\right).
\]
Thus the set of sums with this frequency vector is a Borel set of full \(\mu\)-measure and zero normalized Haar measure. The law \(\mu\) is nonatomic and its topological support is all of \(\mathbb Z_3\).

## Motivation and scope

Two summands of this kind never produce a carry. Three summands are the first case in which a carry changes the typical digit distribution. A frequency vector gives an explicit digit statistic that distinguishes typical sums from Haar-typical expansions even though every finite digit word is possible. The result is for exactly three fair digit streams added in \(\mathbb Z_3\); it does not assert independence of the output digits or a dimension formula.

## Proof

Let \(S_j=\epsilon_{1,j}+\epsilon_{2,j}+\epsilon_{3,j}\). The raw sums \(0,1,2,3\) have probabilities \(1/8,3/8,3/8,1/8\). The initial carry is \(C_0=0\); the output digit is \(D_j=(S_j+C_j)\bmod 3\) and the new carry is \(C_{j+1}=\lfloor(S_j+C_j)/3\rfloor\). These equations compute the sum modulo \(3^k\) using the first \(k\) digits and therefore compute the digits of the \(3\)-adic sum. Since \(S_j+C_j\le4\), the only carry states are \(0,1\). The independent raw sums give the carry transition matrix and the conditional digit table
\[
Q=\frac18\begin{pmatrix}7&1\\4&4\end{pmatrix},\qquad
\bigl(\mathbb P(D_j=d\mid C_j=c)\bigr)_{c=0,1;\,d=0,1,2}
=\frac18\begin{pmatrix}2&3&3\\3&2&3\end{pmatrix}.
\]
The first matrix is irreducible, with stationary row vector \(\pi=(4/5,1/5)\). The time averages of the carry-state indicators converge almost surely to the corresponding entries of \(\pi\), also when starting at zero. For each \(d\), the deviations of \(\mathbf 1_{\{D_j=d\}}\) from its conditional mean given the raw sums up through position \(j-1\) are bounded martingale differences. Their empirical average tends to zero almost surely, by the exponential martingale deviation bound and Borel–Cantelli. Thus the empirical digit frequencies are the \(\pi\)-weighted averages in the conditional digit table, yielding the three displayed fractions.

For Haar measure the digit indicators come from independent uniform ternary digits (the cylinder masses at depth \(k\) are all \(3^{-k}\)). Their limiting frequencies are \((1/3,1/3,1/3)\) almost surely. Since the two vectors differ, the sets of expansions realizing them are disjoint. Each of these sets is Borel because it is defined by limits of measurable empirical averages.

Each individual input is nonatomic: for a given value its first \(k\) digits have probability at most \(2^{-k}\). Conditioning on \(X_2+X_3\) then proves that the sum has no atoms. Finally, every output digit can be made from three binary digits with carry zero and no new carry, using \(000\), \(100\), or \(110\). Choosing these triples for any desired prefix gives that cylinder positive probability. This proves full topological support.

## Verification

Run `python3 check.py` to check the carry and digit tables, stationary frequencies, and digit marginals through eight positions using rational arithmetic and integer prefix counts. The almost-sure assertion is a consequence of the proof, not the finite marginal checks.

## Relationship to related results

- W. Abram and J. C. Lagarias, [*p-adic path set fractals and arithmetic*](https://arxiv.org/abs/1210.2478), Theorem 1.3 and §4.2, construct support automata for Minkowski sums. In contrast, the frequency computation uses the probabilities of different inputs reaching a given carry and producing each digit; these are not given by the support language.
- V. P.-W. Fong, K. E. Hare and D. L. Johnstone, *Multifractal Analysis for Convolutions of Overlapping Cantor Measures*, Asian J. Math. **15** (2011), 53–70, §4, study local dimensions of the real triple Cantor convolution projected to the circle. The folded finite prefix counts considered there are closely related to finite residue counts here by digit reversal and multiplication by the ternary unit two. Local dimensions are a different statistic from typical digit frequencies in the stated \(3\)-adic law.
- [*Exact sixth Fourier moments of finite middle-thirds Cantor spectra*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-sixth-fourier-moments-of-finite-middle-thirds-cantor-spect--a30ba852d85c) gives the finite **integer** collision transfer for the same three input streams. Its carry matrix also computes the **modular** collision count by allowing every terminal carry rather than requiring carry zero. This collision calculation and its dimension exponent are not part of the finding here. The difference-carry matrix for two independent sums does not track the frequencies of the output digits of a single sum.
