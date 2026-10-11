# Exact degree-two discretized Carathéodory–Fejér constant on every cyclic grid
## Finding
For every integer \(N\ge 5\), consider the sampled cosine polynomials
\[
T_{a,b}(r)=1+a\cos(2\pi r/N)+b\cos(4\pi r/N),\qquad r\in\mathbb Z_N,
\]
and define \(M_N^{(2)}\) as the supremum of \(a\) over all real \(b\) for which \(T_{a,b}(r)\ge0\) for every \(r\in\mathbb Z_N\). Put
\[
j=\lfloor 3N/8\rfloor,\qquad u=\cos(2\pi j/N),\qquad v=\cos(2\pi(j+1)/N).
\]
Then
\[
M_N^{(2)}=-\frac{2(u+v)}{1+2uv}.
\]
The value satisfies \(M_N^{(2)}\ge\sqrt2\), with equality exactly for \(8\mid N\), and \(M_N^{(2)}\to\sqrt2\) as \(N\to\infty\).

This is the degree-two case of the discretized Carathéodory–Fejér extremal problem: in the notation of Kolountzakis–Révész it is the fixed higher-frequency set \(H=\{2\}\).

## Assumptions and scope
The modulus is an arbitrary integer \(N\ge5\). The coefficients \(a,b\) are real, the constant term is normalized to one, and nonnegativity is required only on the \(N\)-point cyclic grid. The restriction \(N\ge5\) keeps the frequencies \(0,\pm1,\pm2\) distinct modulo \(N\).

The assertion is an exact infinite-family formula. No claim is made here for higher degrees or for arbitrary sparse frequency sets.

## Proof
Write
\[
x_r=\cos(2\pi r/N),\qquad d_r=\cos(4\pi r/N)=2x_r^2-1.
\]
For \(0\le r\le\lfloor N/2\rfloor\), the values \(x_r\) strictly decrease. The indices \(j=\lfloor3N/8\rfloor\) and \(j+1\) straddle the angle \(3\pi/4\). Thus, with \(u=x_j\), \(v=x_{j+1}\),
\[
d_u:=2u^2-1\le0,\qquad d_v:=2v^2-1>0,
\]
except that \(d_u=0\) exactly when \(8\mid N\). Also \(v<u\), \(u+v<0\), and \(1+2uv>0\). For \(N\ge6\), both \(u\) and \(v\) are nonpositive, so the last inequality is immediate; for \(N=5\), it is \(1+2uv=1/2\).

Suppose first that \(8\nmid N\). Any feasible pair \((a,b)\) satisfies
\[
1+au+bd_u\ge0,\qquad 1+av+bd_v\ge0.
\]
Multiply the first inequality by \(d_v\), the second by \(-d_u\), and add. The \(b\)-term cancels:
\[
d_v-d_u+a(d_vu-d_uv)\ge0.
\]
Using
\[
d_v-d_u=2(v-u)(u+v),\qquad d_vu-d_uv=(v-u)(1+2uv),
\]
and \((v-u)(1+2uv)<0\), we obtain
\[
a\le-\frac{2(u+v)}{1+2uv}.
\]
If \(8\mid N\), then \(u=-1/\sqrt2\) and the single constraint at \(r=j\) gives \(1+au\ge0\), hence \(a\le\sqrt2\); the displayed formula also reduces to \(\sqrt2\).

For sharpness, set
\[
a_*=-\frac{2(u+v)}{1+2uv},\qquad b_*=\frac1{1+2uv}.
\]
For a sampled value \(x=x_r\),
\[
1+a_*x+b_*(2x^2-1)=\frac{2(x-u)(x-v)}{1+2uv}.
\]
The numbers \(u=x_j\) and \(v=x_{j+1}\) are adjacent in the decreasing list of distinct cosine samples on \([0,\pi]\). Therefore no sampled \(x_r\) lies strictly between \(v\) and \(u\), so \((x_r-u)(x_r-v)\ge0\) for every \(r\). Hence \((a_*,b_*)\) is feasible and attains the upper bound.

Finally,
\[
M_N^{(2)}-\sqrt2
=-\frac{\sqrt2(1+\sqrt2u)(1+\sqrt2v)}{1+2uv}.
\]
Because \(u\ge-1/\sqrt2>v\), the right-hand side is nonnegative, and it vanishes exactly when \(u=-1/\sqrt2\), equivalently \(3N/8\in\mathbb Z\), equivalently \(8\mid N\). Since both adjacent samples tend to \(-1/\sqrt2\), the limit is \(\sqrt2\).

## Verification
The proof above is symbolic and covers every \(N\ge5\). The accompanying script `artifacts/verify.py` is corroborative: it checks the closed formula and sampled nonnegativity through \(N=1000\), independently solves the two-variable sampled linear program by enumerating active-constraint intersections for every \(5\le N\le90\), and checks the equality criterion \(M_N^{(2)}=\sqrt2\) against divisibility by eight. Its successful terminal line is `VERIFY_OK`.

The finite computation is not used as a proof of the infinite statement.

## Relationship to prior work
Kolountzakis and Révész formulate exactly the discretized Carathéodory–Fejér problem \(M_m(H)\): maximize the first cosine coefficient with constant term one and nonnegativity imposed only on the \(m\)-point grid. Thus the present quantity is \(M_N(\{2\})\). Their Section 7 evaluates several other support patterns, including the larger interval \(H=[2,m/2)\) for even \(m\), but that larger admissible frequency set does not determine the singleton \(H=\{2\}\).

Ivanov and Ivanov (2010) formulate the equivalent second discrete Fejér problem \(\lambda(
u,p,q)\). In their normalization, for \(N\ge6\) the present constant is \(M_N^{(2)}=2\lambda(1,3,N)\). They state that at that stage the second discrete problem had been solved only for the highest coefficient \(
u=p-1\); the case \((
u,p)=(1,3)\) is therefore outside that solved family.

Ivanov (2018) subsequently solves several additional parameter regimes. Those theorems include the isolated degree-two moduli \(N=6,7,9\): Theorem 4 covers \(\lambda(1,3,6)\), Theorem 5 covers \(\lambda(1,3,7)\), and Theorem 6 covers \(\lambda(1,3,9)\). These values agree with the formula above. The inspected paper does not state a formula for \(\lambda(1,3,N)\) for arbitrary \(N\); its stated results concern selected relations among \(p\) and \(q\). The theorem here supplies one closed form for every \(N\ge5\), while subsuming those three previously solved moduli.

Krenedits and Révész give a general locally compact Abelian framework and the cyclic positive-definite reformulation, but the inspected full text does not evaluate this fixed five-point support. The classical continuous degree-two value is \(\sqrt2\); the formula above identifies the exact finite-grid excess and shows that it vanishes exactly when the grid contains the critical angle \(3\pi/4\), namely when \(8\mid N\).

## Limitations
The originality search covered the directly relevant full-text sources from 2003, 2010, 2013, and 2018, targeted web searches for the fixed support and formula, and semantic database searches under the principal aliases. No exact prior statement of this formula was located. A residual risk remains that an older or poorly indexed table of discrete Carathéodory–Fejér constants contains an equivalent degree-two formula in different notation.

The result concerns real even trigonometric polynomials. It does not classify complex-valued positive-definite extremizers beyond the real problem stated above.

## References
1. M. N. Kolountzakis and S. Gy. Révész, “On pointwise estimates of positive definite functions with given support,” arXiv:math/0302193, first public version 2003-02-17; Canadian Journal of Mathematics 58 (2006), DOI:10.4153/CJM-2006-017-8.
2. S. Krenedits and S. Gy. Révész, “Carathéodory–Fejér type extremal problems on locally compact Abelian groups,” arXiv:1304.0071, first public version 2013-04-02; Journal of Approximation Theory 194 (2015), DOI:10.1016/j.jat.2015.02.001.
