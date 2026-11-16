# Sharp constrained fourth moment at the first collision of square frequencies

## Finding
Let \(F(\theta)=\sum_{k=1}^{7}a_k e^{ik^2\theta}\), \(\theta\in\mathbb T=\mathbb R/(2\pi\mathbb Z)\), and assume the seven complex coefficients satisfy \(|a_1|\ge|a_2|\ge\cdots\ge|a_7|\). Normalize circle Haar measure to total mass one. Let \(s\) be the unique real root in \((1,2)\) of
\[
2s^3+s^2-2s-2=0.
\]
Then the **exact sharp coefficient-restricted fourth-moment inequality** is
\[
\int_{\mathbb T}|F(\theta)|^4\,d\theta
\le K_7\left(\sum_{k=1}^7|a_k|^2\right)^2,
\qquad
K_7=2-\frac{s^4-4s+6}{(s^2+6)^2}
=1.941278426541294\ldots.
\]
For a nonzero coefficient vector equality holds **if and only if**
\[
|a_1|=s t,\qquad |a_2|=\cdots=|a_7|=t>0,
\qquad a_1a_7\overline{a_5}^{\,2}>0
\quad\text{is real}.
\]
The remaining coefficient phases are unrestricted. The value \(K_7\) is the sharp fourth power of the coefficient-\(\ell^2\)-to-\(L^4\) norm for the seven-term square spectrum **under the nonincreasing-modulus constraint**; it is not an unrestricted \(\Lambda(4)\) constant.

## Assumptions and scope
This is a finite seven-term theorem for arbitrary complex coefficients (including zero coefficients) ordered by decreasing modulus in the **index** \(k\). The result does not assert the same constant at length eight or for arbitrary rearrangements. Exponentials are at positive-square frequencies \(1,4,9,16,25,36,49\), with normalized period-
\(2\pi\) integration. Squared magnitudes are denoted \(x_k=|a_k|^2\), with \(x_1\ge\cdots\ge x_7\ge0\), and \(S=\sum_k x_k\).

The first six positive square frequencies form a two-sum Sidon set (no nontrivial unordered pair collisions), while adjoining the seventh produces the first collision \(1+49=25+25\). This is why the seventh length, rather than an arbitrary finite cutoff, is studied.

## Proof
**1. Exact Fourier reduction.** Parseval applied to \(F^2\) gives the ordinary no-collision term \(2S^2-\sum_kx_k^2\). Enumerating the 28 unordered pairs of indices from \({1,\ldots,7}\) shows that the only repeated sum of squares is \(50=1^2+7^2=5^2+5^2\). Consequently
\[
\|F\|_4^4=2S^2-\sum_{k=1}^{7}x_k^2
+4\operatorname{Re}(a_1a_7\overline{a_5}^{\,2})
\le 2S^2-\sum_kx_k^2+4x_5\sqrt{x_1x_7}.
\]
Equality in this first inequality holds when \(a_1a_7\overline{a_5}^{\,2}\) is nonnegative real, and, at the final nonzero extremizer, positive real.

**2. Reduction to a quadratic certificate.** The cubic \(2s^3+s^2-2s-2\) is strictly increasing on \([1,2]\), negative at one and positive at two. Define
\[
f=\frac{s^4-4s+6}{(s^2+6)^2}
=\frac{1-s/2}{s^2+6}>0.
\]
The equality of the two expressions follows by multiplying out the cubic. Its root also satisfies \(s^2-1/s=1-s/2\). Since
\[
2\sqrt{x_1x_7}\le x_1/s+s x_7,
\]
we obtain
\[
\sum_kx_k^2-4x_5\sqrt{x_1x_7}-fS^2
\ge \sum_kx_k^2-\frac2s x_1x_5-2s x_5x_7-fS^2.
\]
Introduce the ordered gaps \(d_i=x_i-x_{i+1}\) for \(1\le i<7\) and \(d_7=x_7\). All \(d_i\ge0\), and \(x_i=\sum_{j=i}^7d_j\), \(S=\sum_{i=1}^7i d_i\). The right side is \(d^TBd\), where indices now range from one to seven and
\[
B_{ij}=\min(i,j)-\frac{\mathbf1_{i\ge5}+\mathbf1_{j\ge5}}s
-s\bigl(\mathbf1_{i\ge5,j\ge7}+\mathbf1_{i\ge7,j\ge5}\bigr)-fij.
\]
Here \(\mathbf1\) denotes the indicated condition's truth value.

**3. Positive-semidefinite-plus-nonnegative decomposition.** Form the symmetric matrix \(P\) from \(B\) by replacing \(B_{1i},B_{i1},B_{7i},B_{i7}\) by zero for \(i=2,3,4\), and replacing \(B_{67},B_{76}\) by \(B_{67}-s/2\). Every removed coefficient is strictly positive: explicitly \(B_{1i}=1-if>0\) and \(B_{7i}=i-1/s-7if>0\) for \(i=2,3,4\), and \(s/2>0\). Hence \(B-P\) is entrywise nonnegative and has zero diagonal, implying \(d^T(B-P)d\ge0\) for all \(d\ge0\).

The exact cubic identities imply
\[
Bv=(0,s/2,s,3s/2,0,s/2,0)^T,
\qquad v=(s^2-1,0,0,0,0,0,1)^T,
\qquad Pv=0.
\]
The upper-left \(6\times6\) principal block of \(P\) is positive definite: exact directed rational interval Gaussian elimination at \(1142138768653/10^{12}<s<1142138768654/10^{12}\) produces the six lower bounds \(0.94,1.76,0.93,0.92,0.31,0.84\) for its successive positive \(LDL^T\) pivots. The appended standalone integer-interval checker establishes these inequalities without numerical rounding assumptions. Thus \(P\) has a six-dimensional positive definite restriction, an exact nonzero null vector \(v\), and is positive semidefinite with \(\ker P=\mathbb Rv\). Therefore \(d^TBd\ge0\) for all ordered coefficient magnitudes.

**4. Sharpness and equality.** From the preceding estimates, \(\|F\|_4^4\le(2-f)S^2\). If equality holds with \(S>0\), then \(d^TPd=0\), so \(d=cv\) for some \(c>0\). It follows that \(x_1=s^2c\) and \(x_2=\cdots=x_7=c\). This profile also realizes equality in the elementary square-root inequality. Conversely these magnitudes with \(a_1a_7\overline{a_5}^{\,2}>0\) real give \(\|F\|_4^4=(2-f)S^2\). This proves the optimal constant and all equality cases.

## Verification
Run `python3 CHECK.py` using the Python standard library. It (i) isolates the cubic root using exact rational signs; (ii) exhaustively enumerates all 28 unordered pairs and their sole collision; (iii) checks positivity of the coefficients removed in \(B-P\); and (iv) verifies all six positive \(LDL^T\) pivots with outward-directed integer intervals at a fixed scale \(10^{15}\). The exact null identity is proved algebraically in Step 3; the checker also encloses each of its components about zero. The program's finite calculations certify the explicitly displayed finite matrix, rather than purporting to prove an infinite theorem by sampling.

## Relationship to prior work
Vasilyev (2026) studies Fourier norm bounds for polynomial phases with coefficient restrictions and discusses the classical Córdoba square-frequency problem. Its theorems supply qualitative or asymptotic bounds rather than the sharp length-seven monotone-modulus constant or its extremizers. A published sharp \(\Lambda(4)\) theorem for one pair-product collision determines the **unrestricted** constant \(15/7\) in the diagonal/off-diagonal case and realizes its extremizers only on the three colliding characters; the present decreasing-modulus hypothesis prohibits that sparse support, so the unrestricted result does not imply the sharp constrained constant \(K_7<2\). The finite collision identity itself and Parseval are standard prior tools; only the constrained optimum and equality classification are advanced here.

## Limitations
The theorem addresses only the first seven positive square frequencies and the nonincreasing modulus order. It does not imply a uniform \(L^4\) bound for all quadratic spectra or settle the large-length square-frequency question. The external-literature search may miss older equivalent extremal calculations under Sidon-set or additive-energy terminology; historical priority remains provisional. Independent review has not been performed.

## References
1. I. Vasilyev, "Norm bounds on Fourier series with polynomial spectra and constrained coefficients," arXiv:2608.19132 (first public 2026-08-19); https://arxiv.org/abs/2608.19132.
2. "Sharp \(\Lambda(4)\) constants for a single pair-product collision," public research record (2026-10-11); https://github.com/published-finding corpus/2026 (public RESULT.md blob SHA 434cefb224141a094f03de4af694e713f39e7b64).
3. A. Córdoba, *Suprematism in Harmonic Analysis*, Birkhäuser (2024), DOI 10.1007/978-3-031-73737-4; cited for the square-spectrum coefficient-restriction setting.
