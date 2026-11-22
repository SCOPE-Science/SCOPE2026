# Three-term mean record law for a common-phase binomial carry process

## Finding

For each integer \(d\ge 2\), define the binary functions
\[
F_{d,j}(x)=\lfloor dx\rfloor-\lfloor jx\rfloor-\lfloor(d-j)x\rfloor,
\qquad 1\le j<d,\quad 0\le x<1.
\]
Let \(X\) be Lebesgue-uniform on \([0,1)\) and let \(I_d(X)\) indicate the event that **all** \(d-1\) functions \(F_{d,j}(X)\) vanish. Define the count \(R_N(X)=\sum_{d=2}^{N}I_d(X)\) for \(N\ge1\), with the empty sum zero. Put
\[
H_m=\sum_{j=1}^m\frac1j,\qquad
H_m^{(2)}=\sum_{j=1}^m\frac1{j^2},\qquad
H_0=H_0^{(2)}=0.
\]
Then, for **every** integer \(N\ge1\),
\[
\boxed{\mathbb E R_N=\frac12\sum_{k=1}^{N}\frac{\mu(k)}{k^2}
\left(H_{\lfloor N/k\rfloor}^2-H_{\lfloor N/k\rfloor}^{(2)}\right).}
\tag{1}
\]
Writing \(Z=\zeta(2)\), \(Z'=\zeta'(2)\), \(Z''=\zeta''(2)\), and letting \(\gamma\) be Euler's constant, this has the **three-term** expansion
\[
\boxed{\begin{aligned}
\mathbb E R_N={}&\frac{(\log N)^2}{2Z}
+\left(\frac{\gamma}{Z}-\frac{Z'}{Z^2}\right)\log N+C
+O\!\left(\frac{(\log N)^2}{N}\right),\\
C={}&\frac12\left(\frac{\gamma^2-Z}{Z}
-\frac{2\gamma Z'+Z''}{Z^2}+\frac{2(Z')^2}{Z^3}\right).
\end{aligned}}
\tag{2}
\]
Here \(\log\) is natural, the implied constant is absolute, and the asymptotic assertion concerns \(N\to\infty\). Numerically, the three coefficients of \((\log N)^2\), \(\log N\), and \(1\) are respectively
\(0.303963550927013\ldots\), \(0.697399781010136\ldots\), and \(-0.368829863948792\ldots\).

In particular, the mean number of new upper records in the fractional-part sequence \(\{X\},\{2X\},\ldots,\{NX\}\) is \((3/\pi^2)(\log N)^2+O(\log N)\). This concerns a **single common random phase** and does not assign independent randomness to the carry indicators.

## Assumptions and scope

The parameter \(X\) is uniform with respect to ordinary Lebesgue measure, and all carry variables use this same phase. Identities involving interval components are asserted away from the finite set of rationals whose denominator is at most \(d\); changing these exceptional values has no effect on the expectation. No assertion concerns valuations of randomly sampled integers or the almost-sure growth of \(R_N(X)\) for a fixed \(X\).

For \(d\ge2\), define \(E_d\) as the almost-everywhere event \(F_{d,j}(X)=0\) for all \(1\le j<d\). Its precise one-index probability is
\[
\mathbb P(E_d)=\frac1d\sum_{\substack{1\le b<d\\gcd(b,d)=1}}\frac1b.
\tag{3}
\]
This Farey-geometric ingredient is a consequence of the classical characterization of extreme points of Weyl sequences by adjoining Farey neighbors (Zhigljavsky--Aliev, 1999, Lemma 1); the claimed additional quantitative result is the **all-index finite expectation and three-term expansion** (1)--(2), not priority for the Farey characterization itself.

## Proof

**Step 1: Convert the full carry event into an upper-record event.** For irrational \(x\in(0,1)\), write \(u_j=\{jx\}\). Since
\[
F_{d,j}(x)=\lfloor u_j+u_{d-j}\rfloor,
\qquad\{dx\}=u_j+u_{d-j}-F_{d,j}(x),
\]
and \(0<u_j,u_{d-j}<1\), we have the *exact equivalence*
\[
F_{d,j}(x)=0\quad\Longleftrightarrow\quad\{dx\}>\{jx\}.
\]
Thus \(E_d\) means that the \(d\)-th fractional part is strictly greater than all its predecessors.

**Step 2: Identify the event using Farey neighbors.** Set \(r=\lceil dx\rceil\) and \(\varepsilon=r/d-x\), so \(1\le r\le d\) and \(0<\varepsilon<1/d\). If \(g=\gcd(r,d)>1\), use \(j=d/g\). Then \(jr/d\) is an integer, and
\[
\{jx\}=1-j\varepsilon>1-d\varepsilon=\{dx\},
\]
so \(E_d\) is impossible. If \(\gcd(r,d)=1\), then \(r<d\). Let \(b\in\{1,\ldots,d-1\}\) be the unique inverse \(rb\equiv1\pmod d\), and set \(a=(rb-1)/d\). The adjacent reduced Farey fractions \(a/b<r/d\) satisfy \(rb-ad=1\); no rational of denominator at most \(d\) lies strictly between them.

For \(x\) just left of \(r/d\), all \(\{jx\}\) with \(1\le j<d\) tend to fractional parts strictly below one, whereas \(\{dx\}\to1\). The ordering can change only at a rational of denominator at most \(d\). Hence the entire interval \((a/b,r/d)\) belongs to \(E_d\). Conversely, if \((r-1)/d<x<a/b\), then \(\varepsilon>1/(bd)\), while \(\varepsilon<1/d\), and
\[
\{bx\}=1+\frac1d-b\varepsilon
>1-d\varepsilon=\{dx\}.
\]
This rules out the rest of the \(r\)-th cell. Thus, up to rational boundary points,
\[
E_d=\bigsqcup_{\substack{1\le r<d\\\gcd(r,d)=1}}
\left(\frac{a_r}{b_r},\frac rd\right),
\quad rb_r-da_r=1,\quad 1\le b_r<d.
\tag{4}
\]
The lengths are exactly \(1/(db_r)\); inversion permutes the reduced residues, proving (3). The Farey geometry in (4) is classical and is not claimed as the original part.

**Step 3: Sum all record probabilities.** By linearity, (3) implies
\[
\mathbb E R_N
=\sum_{2\le d\le N}\ \sum_{\substack{1\le b<d\\\gcd(b,d)=1}}
\frac1{bd}.
\]
Insert the exact Möbius identity \(\mathbf 1_{(b,d)=1}=\sum_{k\mid(b,d)}\mu(k)\), write \(d=km\), \(b=kn\), and rearrange the finite sum. The inner triangular harmonic sum is
\[
\sum_{1\le n<m\le M}\frac1{mn}
=\frac12\big(H_M^2-H_M^{(2)}\big).
\]
Taking \(M=\lfloor N/k\rfloor\) proves (1), including \(N=1\).

**Step 4: Compute all three asymptotic coefficients with a uniform error.** Let \(L=\log N\), \(A(s)=1/\zeta(s)\). For \(1\le k\le N\), the uniform harmonic estimates
\[
H_{\lfloor N/k\rfloor}=\log(N/k)+\gamma+O(k/N),
\qquad
H_{\lfloor N/k\rfloor}^{(2)}=\zeta(2)+O(k/N)
\]
give, upon insertion in (1), an aggregate error
\[
O\left(\frac1N\sum_{k\le N}\frac{1+\log(N/k)}k\right)
=O\!\left(\frac{(\log N)^2}{N}\right).
\]
The extension of the main sum from \(k\le N\) to all \(k\ge1\) has error \(O(1/N)\), since \(\sum_{k>N}k^{-2}(1+\log(k/N)^2)=O(1/N)\). For every nonnegative integer \(j\le2\), absolute convergence justifies
\[
\sum_{k\ge1}\frac{\mu(k)(\log k)^j}{k^2}=(-1)^j A^{(j)}(2).
\]
Expanding \(\big(L-\log k+\gamma\big)^2-\zeta(2)\) yields
\[
\mathbb E R_N=\frac{A(2)}2L^2+
\big(\gamma A(2)+A'(2)\big)L
+\frac{(\gamma^2-\zeta(2))A(2)+2\gamma A'(2)+A''(2)}2
+O\!\left(\frac{L^2}{N}\right).
\]
Finally \(A'=-\zeta'/\zeta^2\) and \(A''=2(\zeta')^2/\zeta^3-\zeta''/\zeta^2\) give (2). The leading coefficient \(1/(2\zeta(2))=3/\pi^2\) follows from Euler's evaluation of \(\zeta(2)\).

## Verification

The standalone Python 3 program `verify.py` reconstructs the full carry vector at exact rational midpoints of every Farey cell, independently compares all surviving intervals with (4) for \(2\le d\le55\), and verifies that the direct sum of exact rational probabilities equals the Möbius--harmonic formula for each \(1\le N\le55\). It returned **54 interval classifications**, **939 surviving cells**, and **55 exact expectation comparisons**, all passing. The asymptotic coefficients and rate are proved analytically above; a finite test does not establish the infinite statement.

## Relationship to prior work

The geometric part uses the classical Farey--Weyl extremum principle, explicitly in Zhigljavsky and Aliev (1999, Lemma 1), which describes the largest and smallest points in a Weyl sequence via adjacent Farey fractions. No novelty is claimed for that lemma or the elementary interval lengths themselves. The 2026 binomial-gcd papers of Wu and of Guo--Qiu--Cao--Feng--Gao investigate Kummer/Lucas divisibility restrictions, not the expectation of common-phase all-index records. The specific exact Möbius--harmonic formula and its three-term, constant-precision mean asymptotic were not found in the inspected sources or searched research records. In contrast, determining all pairwise carry covariances does not determine this all-coordinate event or its mean across denominators.

## Limitations

The distribution of \(R_N\), its variance, and almost-sure growth are not determined here. An asymptotic mean is not a typical-phase law. An older or unindexed source might have derived the same expectation implicitly, especially through continued-fraction theory; the priority assessment is not an independent audit. The Farey interval description is established prior work, and only the finite-\(N\) mean identity and three-term expansion are considered as the additional finding. This result does not quantify primes or integer-sampled Kummer valuations.

## References

1. A. Zhigljavsky and I. Aliev, *Weyl sequences: Asymptotic distributions of the partition lengths*, Acta Arithmetica 88 (1999), 351--363, especially Lemma 1, Section 2.1. https://matwbn.icm.edu.pl/ksiazki/aa/aa88/aa8845.pdf
2. Chai Wah Wu, *Computing the Greatest Common Divisor of Binomial Coefficients* \(\binom{mn}{mk}\), arXiv:2606.20940v1, first public 2026-06-18. https://arxiv.org/abs/2606.20940
3. Dakai Guo, Ruichen Qiu, Yichuan Cao, Ruyong Feng and Xiao-Shan Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1, first public 2026-06-22. https://arxiv.org/abs/2606.22997
4. Classical Möbius inversion and Euler's evaluation \(\zeta(2)=\pi^2/6\), used in their standard forms.
