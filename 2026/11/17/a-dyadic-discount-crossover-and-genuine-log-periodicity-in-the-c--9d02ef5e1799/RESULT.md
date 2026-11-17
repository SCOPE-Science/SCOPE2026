# A dyadic discount crossover and genuine log-periodicity in the cat-map resolvent trace

## Finding
Let \(A=\begin{pmatrix}1&1\\1&2\end{pmatrix}\) act on \(X_a=(\mathbb Z/2^a\mathbb Z)^2\) with \(a\geq2\). Let \(P_a\) be the associated permutation operator on functions on \(X_a\), and put
\[
R_a(\alpha)=4^{-a}\operatorname{tr}(I-\alpha P_a)^{-1},\qquad M_a=3\cdot2^{a-2}.
\]
For every real \(t>0\), choose the discount \(\alpha_a(t)=e^{-t/M_a}\). Then
\[
\boxed{\lim_{a\to\infty}R_a(\alpha_a(t))=L(t)=\frac34\sum_{j=0}^\infty\frac{4^{-j}}{1-e^{-t/2^j}}.}
\]
The convergence is locally uniform for \(0<t<\infty\), with \(O(2^{-a})\) error on every compact subinterval.

This crossover has two distinct asymptotic regimes:
\[
L(t)=\frac{3}{2t}+\frac12+\frac{t}{14}+O(t^3)\quad(t\downarrow0),
\]
\[
\boxed{L(t)=1+\frac{H(t)}{t^2}+O(e^{-2t})\quad(t\to\infty),}
\]
where
\[
H(t)=\frac34\sum_{k\in\mathbb Z}\frac{(t2^{-k})^2}{e^{t2^{-k}}-1},\qquad H(2t)=H(t).
\]
The function \(H\) is smooth, positive, and *nonconstant*. In the logarithmic coordinate \(s=\log_2t\), its Fourier coefficients are, with \(\omega_n=2\pi n/\log2\),
\[
\boxed{\widehat H(n)=\frac{3}{4\log2}\,\Gamma(2-i\omega_n)\zeta(2-i\omega_n)\neq0\quad(n\in\mathbb Z).}
\]
In particular the large-discount-scale correction \(t^2(L(t)-1)\) does **not** converge to a constant: it has a nontrivial multiplicatively dyadic phase.

## Assumptions and scope
The map is the deterministic integral Arnold cat map reduced modulo \(2^a\); \(a\) is an integer at least \(2\), and \(P_a\) is the permutation matrix induced by the map on functions (either pushforward or pullback gives the same trace). All formulas concern finite-dimensional resolvents at \(0<\alpha<1\) and the particular simultaneous limit \(a\to\infty\), \(\alpha=e^{-t/M_a}\), \(0<t<\infty\). The \(O\)-bounds are uniform only for \(t\) in specified compact intervals or in the stated single-variable limits; no joint uniformity as \(t\downarrow0\) with \(a\to\infty\) is asserted.

## Proof
**Step 1: a valuation lemma.** Direct multiplication gives
\[
A^3=\begin{pmatrix}5&8\\8&13\end{pmatrix}=I+4C,\qquad C=\begin{pmatrix}1&2\\2&3\end{pmatrix},\qquad\det C=-1.
\]
Modulo \(2\), the matrix \(A\) has order \(3\); for \(3\nmid m\), \(A^m-I\) is invertible modulo \(2\). For all positive integers \(q\), writing \(q=2^s u\) with \(u\) odd, repeated squaring from \(I+4C\) shows
\[
A^{3q}-I=2^{s+2}U_q,\qquad U_q\pmod 2\text{ invertible}.
\]
Indeed, \((I+2^kU)^2=I+2^{k+1}(U+2^{k-1}U^2)\), and for \(k\ge2\) the bracket remains congruent to \(U\) modulo \(2\). The remaining odd power \(u\) preserves its invertibility. Hence the displayed exact divisibility holds entrywise, not just as an upper bound on the matrix order.

**Step 2: all period classes.** For a nonzero residue vector \(x\), write \(x=2^{a-b}y\), where at least one coordinate of \(y\) is odd and \(1\le b\le a\). Then \(A^m x=x\pmod{2^a}\) precisely if \(A^m y=y\pmod{2^b}\). If \(3\nmid m\), this is impossible for primitive \(y\); otherwise Step 1 shows it is equivalent to \(2+\nu_2(m/3)\ge b\). Thus
\[
k(x)=3\,2^{\max(0,b-2)}.
\]
There are exactly \(4^b-4^{b-1}=3\cdot4^{b-1}\) vectors of depth \(b\). For \(a\ge2\), the exact numbers \(E_a(\ell)\) of points of each least period are therefore
\[
E_a(1)=1,\qquad E_a(3)=15,\qquad
E_a(3\cdot2^s)=3\cdot4^{s+1}\quad(1\le s\le a-2).
\]
The origin accounts for the single fixed point. The counts sum to \(4^a\). These elementary arithmetic counts are used as input to the new double-scaling statement and are **not** claimed as historically unknown period data.

**Step 3: finite trace and crossover.** On a cycle of length \(\ell\), the diagonal of the resolvent equals \((1-\alpha^\ell)^{-1}\). Consequently, for \(a\ge3\),
\[
R_a(e^{-t/M_a})=
\frac{4^{-a}}{1-e^{-t/M_a}}
+\frac{15\cdot4^{-a}}{1-e^{-3t/M_a}}
+\frac34\sum_{j=0}^{a-3}\frac{4^{-j}}{1-e^{-t/2^j}}.
\]
The case \(a=2\) is obtained directly from the first two terms, with the empty sum. For \(u>0\), \(0<(1-e^{-u})^{-1}\le1+u^{-1}\). Thus on a fixed compact \(t\)-interval bounded away from zero the first two terms and the omitted tail of the infinite sum are both \(O(2^{-a})\). This proves locally uniform convergence to \(L\).

**Step 4: the small-scale expansion.** The expansion \((1-e^{-u})^{-1}=u^{-1}+1/2+u/12+O(u^3)\) is uniform over \(0<u\le t\) for small \(t\). Summing each coefficient against \((3/4)4^{-j}\) gives, respectively, \(3/(2t)\), \(1/2\), and \(t/14\); the remainder is \(O(t^3)\).

**Step 5: the large-scale dyadic phase.** Since \((1-e^{-u})^{-1}=1+(e^u-1)^{-1}\),
\[
t^2(L(t)-1)=\frac34\sum_{j\ge0}f(t2^{-j}),\qquad f(u)=\frac{u^2}{e^u-1}.
\]
The two-sided periodization \(H(t)=(3/4)\sum_{j\in\mathbb Z}f(t2^{-j})\) is absolutely and locally uniformly convergent together with all derivatives in \(\log t\): as \(u\downarrow0\), \(f(u)=O(u)\), and as \(u\to\infty\), \(f(u)=O(u^2e^{-u})\). Shifting the summation index proves \(H(2t)=H(t)\). The missing negative indices contribute \(O(t^2e^{-2t})\) to \(H(t)\) for \(t\ge1\), proving the asserted large-\(t\) error.

For the Fourier coefficient at integer frequency \(n\), absolute convergence justifies unfolding the periodized sum:
\[
\widehat H(n)=\frac{3}{4\log2}\int_0^\infty\frac{u^{1-i\omega_n}}{e^u-1}\,du
=\frac{3}{4\log2}\Gamma(2-i\omega_n)\zeta(2-i\omega_n).
\]
The Mellin integral identity is valid because the real part of its exponent parameter is \(2>1\). The gamma function has no zeroes; the zeta function has none for \(\Re s>1\) by its absolutely convergent Euler product. Therefore every Fourier coefficient is nonzero, including the nonconstant modes. The mean coefficient is \(\pi^2/(8\log2)\), and the nontrivial log-periodicity is exact. \(\square\)

## Verification
Run `python verify.py` with Python 3. The standalone script checks \(A^3=I+4C\) and \(\det C=-1\) exactly, exhaustively enumerates period classes for moduli \(2^a\) with \(1\le a\le6\), checks the rational finite trace identities at \(\alpha=1/2\), and compares finite-size traces with the limit profile at three positive values of \(t\). If `mpmath` is installed, additional high-precision tests confirm periodization, the nonzero first Fourier mode, and a numerical phase difference. These finite checks test calculations but **do not prove** the infinite limiting theorem; the five proof steps above do.

## Relationship to prior work
Chandra [1] defined discounted return landscapes and the finite-permutation resolvent trace, proved landscape/period identities, and explicitly identified dyadic moduli as a further question. Those definitions and identities are prior results. Chen, Wong, Liao, and Xiang [2,3] studied exact distributions of cat-map periods, including prime-power settings. Neither raw dyadic orbit counts nor the trace reduction is asserted to be new here. The contribution isolated here is the explicit **simultaneous resolution/discount crossover**, its quantitative convergence, and its asymptotic **nonconstant dyadic phase with an exact, nonvanishing Mellin–zeta Fourier spectrum**. Statements and implications have been compared with accessible relevant literature; a 2012 prime-power source was not fully accessible, so final priority assessment remains open.

## Limitations
The theorem concerns one specific cat matrix and its powers-of-two reductions. It does not cover general prime powers, other hyperbolic matrices, arbitrary discount sequences, or a uniform two-parameter limit down to \(t=0\). The exponentially small first harmonic makes numerical detection of the log-periodicity delicate, although analytic nonvanishing is proved. The older prime-power literature was not all available in complete text, and independent review has not been performed.

## References
[1] Aryaman Chandra, *Arithmetic Landscape Functions for the Discrete Cat Map*, arXiv:2607.24857 (first public version July 26, 2026; updated October 29, 2026), https://arxiv.org/abs/2607.24857 .

[2] Fei Chen, Kwok-wo Wong, Xiaofeng Liao, Tao Xiang, *Period distribution of generalized discrete Arnold cat map for \(N=p^e\)*, IEEE Transactions on Information Theory 58 (2012), 445–452, https://doi.org/10.1109/TIT.2011.2171534 .

[3] Fei Chen, Kwok-wo Wong, Xiaofeng Liao, Tao Xiang, *Period distribution of generalized discrete Arnold cat map*, Theoretical Computer Science 552 (2014), 13–25, https://doi.org/10.1016/j.tcs.2014.08.002 .
