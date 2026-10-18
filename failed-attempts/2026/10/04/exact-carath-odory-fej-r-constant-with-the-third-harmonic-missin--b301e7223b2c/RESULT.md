# Exact Carathéodory–Fejér constant with the third harmonic missing
## Finding
Consider real trigonometric polynomials
\[
T(t)=1+\lambda\cos(2\pi t)+b\cos(4\pi t)+c\cos(8\pi t),\qquad t\in\mathbb T,
\]
with \(T(t)\ge0\) for every \(t\). Then
\[
\sup \lambda=\frac32.
\]
Moreover the polynomial attaining \(\lambda=3/2\) is unique. Its remaining coefficients are
\[
b=\frac7{12},\qquad c=-\frac1{12},
\]
and, after putting \(x=\cos(2\pi t)\), it factors as
\[
T_*(t)=\frac{(2-x)(x+1)(2x+1)^2}{6}.
\]

Equivalently, if \(\psi:\mathbb Z\to\mathbb R\) is positive definite, \(\psi(0)=1\), and
\[
\operatorname{supp}\psi\subset\{0,\pm1,\pm2,\pm4\},
\]
then
\[
\psi(1)\le\frac34.
\]
Equality is attained by exactly one such real sequence, namely
\[
\psi(\pm1)=\frac34,\qquad
\psi(\pm2)=\frac7{24},\qquad
\psi(\pm4)=-\frac1{24},
\]
with all other values equal to zero.

## Assumptions and scope
The coefficient class is real and even: the allowed cosine frequencies are \(1\), \(2\), and \(4\), while the third harmonic is forbidden. The constant term is normalized to one and nonnegativity is required on the whole circle, not merely on a finite sampling grid.

In the notation introduced by Kolountzakis and Révész for the Carathéodory–Fejér-type problem, this is the exact value \(M(\{2,4\})\). The positive-definite formulation is the real finitely supported formulation supplied by Herglotz' theorem.

## Proof
Let \(x=\cos(2\pi t)\). Two evaluations already force the sharp upper bound. At \(t=1/2\),
\[
T(1/2)=1-\lambda+b+c\ge0.
\]
At \(t=1/3\), all three allowed nonconstant cosines equal \(-1/2\), so
\[
T(1/3)=1-\frac{\lambda}{2}-\frac{b+c}{2}\ge0.
\]
Therefore
\[
T(1/2)+2T(1/3)=3-2\lambda\ge0,
\]
which gives \(\lambda\le3/2\).

For sharpness, take
\[
\lambda_* =\frac32,\qquad b_* =\frac7{12},\qquad c_*=-\frac1{12}.
\]
Using \(\cos(4\pi t)=2x^2-1\) and \(\cos(8\pi t)=8x^4-8x^2+1\), direct expansion gives
\[
1+\frac32x+\frac7{12}(2x^2-1)-\frac1{12}(8x^4-8x^2+1)
=\frac{(2-x)(x+1)(2x+1)^2}{6}.
\]
For \(-1\le x\le1\), every factor on the right is nonnegative except that \((2x+1)^2\) is a square, so the product is nonnegative. Hence \(\lambda=3/2\) is attainable.

It remains to prove uniqueness at the optimum. Equality in the upper-bound identity implies
\[
T(1/2)=T(1/3)=0,
\]
because both terms are individually nonnegative. The first equality gives
\[
b+c=\frac12.
\]
The point corresponding to \(t=1/3\) has \(x=-1/2\), which is an interior zero of the nonnegative polynomial in \(x\). Its derivative must therefore vanish. Differentiating
\[
Q(x)=1+\lambda x+b(2x^2-1)+c(8x^4-8x^2+1)
\]
and inserting \(x=-1/2\) and \(\lambda=3/2\) yields
\[
\frac32-2b+4c=0.
\]
Together with \(b+c=1/2\), this uniquely gives \(b=7/12\) and \(c=-1/12\).

Finally, for a real finitely supported sequence with the stated support, positivity definiteness is equivalent to nonnegativity of
\[
\sum_{k\in\mathbb Z}\psi(k)e^{2\pi i k t}
=1+2\psi(1)\cos(2\pi t)+2\psi(2)\cos(4\pi t)+2\psi(4)\cos(8\pi t).
\]
Thus \(\lambda=2\psi(1)\), and the trigonometric statement is exactly the positive-definite statement.

## Verification
The proof is exact and does not depend on finite computation. The accompanying script `artifacts/verify.py` checks the rational coefficient identities, the two-point upper certificate, the uniqueness equations, and the factorization using exact arithmetic. It also performs a dense floating-point circle scan only as a corroborative sign check. The finite scan is not used to infer the theorem.

## Relationship to prior work
Kolountzakis and Révész define, for an arbitrary allowed higher-frequency set \(H\), the extremal quantity \(M(H)\) obtained by maximizing the first cosine coefficient of a normalized nonnegative trigonometric polynomial. Their full text lists exact values for several structured sets, including singleton sets, complements of singletons, tails, and the even or odd frequencies, and records the general duality
\[
M(H)M(\mathbb N_{\ge2}\setminus H)=2.
\]
The inspected list does not contain \(H=\{2,4\}\); the duality alone also does not evaluate this set because it merely exchanges it with its two-hole complement.

Révész's earlier duality theorem supplies a general minimax framework for trigonometric extremal problems, but it does not itself state the numerical value for this support. Krenedits and Révész later place the same problem in a general locally compact Abelian-group framework and restate the positive-definite-sequence equivalence; that broader framework likewise does not provide the value for this particular support in the inspected material.

The result also sits naturally between two classical full-support constants. Allowing only the second harmonic gives the continuous degree-two value \(\sqrt2\); allowing every harmonic through degree four gives \(\sqrt3\). Allowing the second and fourth harmonics but forbidding the third gives the exact intermediate value \(3/2\).

## Limitations
The theorem concerns the specific first missing-harmonic support \(\{1,2,4\}\) in the real even problem. It does not classify arbitrary sparse frequency sets, nor does it assert the corresponding optimum for complex coefficient sequences without the reality restriction.

The literature comparison included the directly relevant full texts and targeted searches under the Carathéodory–Fejér, positive-definite-sequence, sparse-support, and missing-harmonic formulations. No prior statement of this exact support value was located. A residual risk remains that the same elementary special case appears in older or poorly indexed extremal-polynomial literature under different notation.

## References
1. M. N. Kolountzakis and S. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, arXiv:math/0302193, first public arXiv version 2003-02-17; Canadian Journal of Mathematics 58 (2006), 401–418, DOI 10.4153/CJM-2006-017-8.
2. Sz. Gy. Révész, *Some trigonometric extremal problems and duality*, Journal of the Australian Mathematical Society 50 (1991), 384–390, DOI 10.1017/S1446788700032985.
3. S. Krenedits and S. Gy. Révész, *Carathéodory–Fejér type extremal problems on locally compact Abelian groups*, arXiv:1304.0071, first public arXiv version 2013-03-30; Journal of Approximation Theory 194 (2015), 108–131.
