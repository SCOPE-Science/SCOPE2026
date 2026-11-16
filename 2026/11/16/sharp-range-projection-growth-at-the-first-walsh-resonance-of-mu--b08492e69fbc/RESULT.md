# Sharp range-projection growth at the first Walsh resonance of multipartite independent sets

## Finding
For each integer \(m\ge1\), put \(q=2^m\) and \(r=q+1\). Let \(G_m\) be the complete \(r\)-partite simple graph with \(m\) vertices per part. Its independent-set incidence vectors form a subset \(A_m\subseteq\mathbb F_2^{mr}\). Write \(f_m=\mathbf1_{A_m}\) and let \(C_m h=f_m*h\) denote **unnormalized** convolution on \(\mathbb F_2^{mr}\). Let \(\Pi_m=C_mC_m^\dagger\) be the orthogonal projection onto its range, equivalently the Walsh multiplier equal to one where \(\widehat f_m\ne0\) and zero elsewhere.

Then the convolution rank and its smallest positive singular value are, exactly,
\[
\operatorname{rank}C_m=q^r-r(q-1)^{r-1},\qquad \sigma_{\min}^{+}(C_m)=q.
\]
The range projection has the **sharp endpoint operator norms**
\[
\boxed{\displaystyle
\|\Pi_m\|_{\ell^1\to\ell^1}=\|\Pi_m\|_{\ell^\infty\to\ell^\infty}
=1+\frac{r(q-1)^{r-1}}{q^r}\left((q-2)2^{r-1}+2\right).}
\]
As \(m\to\infty\), equivalently \(q\to\infty\) through powers of two, their common value satisfies
\[
\boxed{\|\Pi_m\|_{\ell^1\to\ell^1}\sim\frac qe\,2^q.}
\]
Thus the first singular member of this natural multipartite family has an exact exponentially large endpoint range-projection norm, although its positive singular values stay at least \(q\).

## Assumptions and scope
Each part is identified with \(H=\mathbb F_2^m\), so the vertex-incidence group is \(H^r\), with \(|H|=q\) and \(|H^r|=q^r\). The Walsh transform is unnormalized, \(\widehat g(\omega)=\sum_{x\in H^r}g(x)(-1)^{\langle\omega,x\rangle}\), and its inverse includes the factor \(q^{-r}\). Convolution is \((g*h)(x)=\sum_y g(y)h(x-y)\). The stated \(\ell^1\), \(\ell^2\), and \(\ell^\infty\) spaces use ordinary counting measure; constant renormalization of that measure leaves the operator norms unchanged. The Moore–Penrose inverse and the orthogonal range projection refer to the counting-measure Hilbert space. Exactly one part can contribute nonzero entries of an independent-set incidence vector.

## Proof
**1. Signed independence polynomial and singular threshold.** Let \(H_i\) denote the coordinate subgroup supported on part \(i\). Since their pairwise intersections equal \(\{0\}\), the indicator of their union obeys
\[
f_m=\sum_{i=1}^r\mathbf1_{H_i}-(r-1)\delta_0.
\]
Let \(t(\omega)=\#\{i:\omega_i=0\in H\}\). Orthogonality of binary characters on \(H\) yields
\[
\widehat f_m(\omega)=q\,t(\omega)-(r-1)=q(t(\omega)-1),
\]
because \(r=q+1\). Thus exactly the characters with one zero block are missing from the Fourier support. Their number is \(Z=r(q-1)^{r-1}\). The remaining nonzero multiplier values have least absolute value \(q\), attained by \(t=0\) and \(t=2\) (both occur). Walsh diagonalization gives the rank and the positive spectral minimum. For context, for arbitrary part count \(s\ge2\) the same argument gives \(\widehat f=q t-(s-1)\), which can vanish if and only if \(s\equiv1\pmod q\); hence \(r=q+1\) is the first singular part count with \(s\ge2\).

**2. The omitted-shell kernel.** Put \(Z_m=\{\omega:t(\omega)=1\}\). For any \(x\in H^r\), let \(k(x)=\#\{i:x_i\ne0\}\). The character sum over nonzero frequency blocks in one coordinate is \(q-1\) if \(x_i=0\) and \(-1\) otherwise. Summing over the choice of the unique zero-frequency coordinate gives
\[
T(x):=\sum_{\omega\in Z_m}(-1)^{\langle\omega,x\rangle}
=(-1)^{k(x)}(q-1)^{r-k(x)-1}(r-qk(x)).
\]
This formula also holds at \(k(x)=r\), where the exponent is \(-1\): the other factor \(r-qr=r(1-q)\) makes the displayed expression an integer, as required by the character sum.

The convolution kernel of \(\Pi_m\) is exactly \(K(x)=\delta_0(x)-q^{-r}T(x)\). At \(x=0\) it equals \(1-Z/q^r>0\). At every \(x\ne0\), it equals \(-q^{-r}T(x)\). The endpoint norms of convolution by \(K\) both equal \(\sum_x|K(x)|\), since all matrix rows and columns are translates and the appropriate sign function realizes the maximal absolute sum.

**3. Evaluation of the absolute sum.** There are exactly \(\binom rk(q-1)^k\) group elements with \(k(x)=k\). Therefore
\[
\|\Pi_m\|=1-\frac Z{q^r}
+\frac{(q-1)^{r-1}}{q^r}\sum_{k=1}^r\binom rk|r-qk|.
\]
With \(r=q+1\), the term \(r-qk\) is positive only at \(k=1\), where it equals \(1\), and is negative for \(k\ge2\). By \(\sum_{k\ge1}\binom rk=2^r-1\) and \(\sum_{k\ge1}k\binom rk=r2^{r-1}\),
\[
\sum_{k=1}^r\binom rk|r-qk|
=r((q-2)2^{r-1}+3).
\]
Substitution of \(Z=r(q-1)^{r-1}\) yields precisely the stated endpoint norm. The formula is sharp because the absolute kernel sum is itself an attained convolution norm, not merely an upper bound.

**4. Asymptotics.** With \(r=q+1\), the norm minus one is
\[
\left(1+q^{-1}\right)(1-q^{-1})^q\bigl((q-2)2^q+2\bigr).
\]
The first two factors tend to \(e^{-1}\), and the final factor is asymptotic to \(q2^q\). This proves the claimed limit.

## Verification
The self-contained `artifacts/check.py` uses an independent exhaustive integer Walsh–Hadamard transform of the complete independent-set indicator for \(m=1\) and \(m=2\), enumerating \(8\) and \(1024\) group elements respectively. It compares every Fourier multiplier against the subgroup formula, constructs the range-projection Fourier multiplier, transforms it back and sums absolute kernel values exactly as fractions. The results are, respectively, rank \(5\), norm \(7/4\), and rank \(619\), norm \(7397/512\). It additionally evaluates the closed formula at \(m=3\), producing \(39965296585/67108864\), without claiming to exhaustively inspect the \(134217728\)-element group. Run `python artifacts/check.py` using Python 3 standard library. These finite checks corroborate but do not prove the quantified theorem.

## Relationship to prior work
Scott and Sokal [1] set out the multivariate independent-set polynomial and explicitly evaluate complete-bipartite examples. Zhu and Lu [2] give the complete-multipartite **univariate** independence-polynomial decomposition. Consequently the signed-independence multiplier identity in Step 1 is a specialization of established graph-enumeration mathematics and is **not** claimed as new. The main contribution here is the exact **range projection** onto *nonzero Fourier multipliers* at the first singular part count, its sharp endpoint norm, and exponential asymptotic law. This is distinct from spectral restriction of low-degree characters onto a Hamming shell (see [4], [5]), and from general bounds for norms of integer-valued Fourier idempotents [3]. The dual viewpoint is that the omitted frequencies form a \(q\)-ary Hamming shell of weight \(r-1\); the Fourier kernel has a first-degree Krawtchouk-type factor. An equivalent classical Hamming-scheme norm calculation is a residual priority risk.

## Limitations
The graph family requires binary blocks of equal positive size and exactly \(2^m+1\) parts. The result concerns the range projection, not sharp endpoint norms of the Moore–Penrose pseudoinverse. Its rank and multiplier formulas use known independent-set enumeration; their appearance is explanatory rather than a novelty assertion. An exhaustive literature-priority guarantee is not claimed. The checker is finite verification rather than an independent mathematical audit.

## References
1. A. D. Scott and A. D. Sokal, *The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma*, first publicly posted 2003-09-15, arXiv:cond-mat/0309352, https://arxiv.org/abs/cond-mat/0309352.
2. B.-X. Zhu and Q. Lu, *Unimodality of the independence polynomials of some composite graphs*, first publicly posted 2015-07-21, arXiv:1507.05754, https://arxiv.org/abs/1507.05754.
3. B. Green and T. Sanders, *A quantitative version of the idempotent theorem in harmonic analysis*, arXiv:math/0611286, https://arxiv.org/abs/math/0611286.
4. *An all-degree spectral law for Fourier sampling on q-ary Hamming spheres*, publicly available scientific report, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-all-degree-spectral-law-for-fourier-sampling-on-q-ary-hamming--f3d01cadaa90.
5. *Exact q-ary Hamming-shell Fourier concentration and the arithmetic tightness criterion*, publicly available scientific report, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-q-ary-hamming-shell-fourier-concentration-and-the-arithmet--89a15e26e594.
