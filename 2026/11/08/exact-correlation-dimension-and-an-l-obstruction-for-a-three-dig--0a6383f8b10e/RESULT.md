# Exact correlation dimension and an \(L^2\) obstruction for a three-digit four-adic convolution

## Finding

Let \(D=\{0,1,3\}\), and let \(\mu\) be the distribution of \(\sum_{j\geq1}\xi_j4^{-j}\), where the digits \(\xi_j\) are independent and uniform on \(D\). Write \(\nu=\mu*\mu\). For
\[
A_n=\left\{\sum_{j=0}^{n-1}d_j4^j:d_j\in D\right\},\qquad
E_n=\#\{(a,b,c,d)\in A_n^4:a+b=c+d\},
\]
put \(\lambda_\pm=(25\pm\sqrt{265})/2\). The complete additive-energy sequence is
\[
E_0=1,\qquad E_1=15,\qquad E_{n+2}=25E_{n+1}-90E_n,
\]
and, for every integer \(n\geq0\),
\[
E_n=\frac{\sqrt{265}+5}{2\sqrt{265}}\lambda_+^n+
\frac{\sqrt{265}-5}{2\sqrt{265}}\lambda_-^n.
\]
The correlation dimension of the actual continuous convolution measure exists and is exactly
\[
D_2(\nu)=\frac{4\log3-\log\lambda_+}{\log4}
=0.986260078410508\ldots<1.
\]
Consequently, \(\nu\) has no density in \(L^2(\mathbb R)\), even though \(\mu\) has Hausdorff dimension \(\log3/\log4>1/2\). This does not assert that \(\nu\) is singular or lacks an \(L^p\) density for smaller \(p\).

## Assumptions and scope

All probabilities are exact, all digit choices independent, and convolution is on the real line. The dimension uses the grid-energy convention
\[
D_2(\nu)=\lim_{n\to\infty}
-\frac{\log\sum_{k\in\mathbb Z}\nu([k4^{-n},(k+1)4^{-n}))^2}{n\log4}.
\]
The limit exists by the proof. It coincides with the usual correlation or \(L^2\)-dimension: comparing arbitrary small lengths with adjacent fourth-power scales changes the relevant exponent by a vanishing relative amount. We make no pointwise-density or Fourier-decay claim.

## Proof

**Exact carry matrix.** Given four digits \(a,b,c,d\in D\), the one-digit signed difference \(\delta=a+b-c-d\) belongs to \([-6,6]\). In an equality of two sums, the incoming carry \(i\in\{-1,0,1\}\) can produce only an outgoing carry \(j\in\{-1,0,1\}\), with \(\delta+i=4j\). The exact digit-count matrix, in the order \((-1,0,1)\), is
\[
T_{i,j}=\#\{(a,b,c,d)\in D^4:a+b-c-d+i=4j\}
=\begin{pmatrix}8&10&2\\3&15&3\\2&10&8\end{pmatrix}.
\]
For any word of length \(n\), the initial and final carries are zero if and only if the two length-\(n\) digit sums agree. Therefore \(E_n=(T^n)_{0,0}\), where the subscript \(0\) denotes the middle row and column. Reflection of the carry states decomposes \(T\) into an odd eigenmode of eigenvalue \(6\) and a two-dimensional even sector. The latter has characteristic polynomial \(\lambda^2-25\lambda+90\); the central state lies in this sector. Hence \(E_{n+2}=25E_{n+1}-90E_n\). The directly counted \(E_0=1\), \(E_1=15\) yield the displayed closed form. Its leading coefficient is positive and \(\lambda_+>\lambda_->0\).

**From finite sums to the continuous measure.** Write \(X=\sum_{j\geq1}\xi_j4^{-j}\) and use an independent copy \(Y\). The first \(n\) digits give an integer prefix \(U_n\) with law uniform on \(A_n\), scaled by \(4^{-n}\), and \(4^n(X+Y)=U_n+V_n+X'+Y'\), where \(X',Y'\) are independent copies of \(X\), independent of the prefixes. Define
\[
w_{n,k}=3^{-2n}\#\{(a,b)\in A_n^2:a+b=k\}.
\]
Then \(\sum_kw_{n,k}^2=E_n/81^n\). Since \(0\leq X'+Y'\leq2\), and the endpoints have no mass, with \(q_0=\mathbb P(X'+Y'<1)\) and \(q_1=1-q_0\) the mass of the \(k\)-th fourth-power grid cell is
\[
v_{n,k}=q_0w_{n,k}+q_1w_{n,k-1}.
\]
Nonnegativity and Young's convolution inequality for \(\ell^2(\mathbb Z)\), with \(q_0+q_1=1\), give
\[
(q_0^2+q_1^2)\sum_kw_{n,k}^2
\leq\sum_kv_{n,k}^2
\leq\sum_kw_{n,k}^2.
\]
Because \(q_0^2+q_1^2\geq1/2\), the key uniform comparison is
\[
\frac{E_n}{2\cdot81^n}
\leq\sum_k\nu([k4^{-n},(k+1)4^{-n}))^2
\leq\frac{E_n}{81^n}.
\]
The leading root of the recurrence now proves the claimed \(D_2\) limit. The usual spatial-diameter correlation dimension follows from fixed-neighbor grid comparisons and monotonicity between successive \(4\)-adic scales.

**Failure of an \(L^2\) density.** If \(\nu=h(x)\,dx\) with \(h\in L^2(\mathbb R)\), Cauchy--Schwarz on each grid interval would give
\[
4^n\sum_kv_{n,k}^2\leq\|h\|_2^2
\quad(n\geq0).
\]
However, the derived lower bound grows as a positive multiple of \((4\lambda_+/81)^n\). Here \(4\lambda_+/81>1\) because \(\sqrt{265}>31/2\). This contradiction excludes \(L^2\) density. Finally, the three digit cylinder intervals of \(\mu\) have disjoint interiors and uniform masses \(3^{-n}\), so its Hausdorff (and correlation) dimension equals \(\log3/\log4\).

## Verification

The standalone `CHECK.py` enumerates all \(3^4\) one-digit signed configurations, constructs the carry matrix from its definition, checks the exact recurrence and spectral polynomial, and separately counts finite additive quadruples through depth four. The inequalities for continuous grid masses and the no-\(L^2\) conclusion are proved analytically above, not inferred from finite computation. Run with `python3 CHECK.py`; it uses only the Python standard library.

## Relationship to prior work

Carnovale, Fraser, and de Orellana (2026), arXiv:2606.07143, show why \(L^q\)-dimensions and convolution norms matter for Fourier restriction estimates; their results concern general restriction criteria, not the precise integer-digit convolution here. Oliveira and de Orellana (2026), arXiv:2602.08568, study convolution regularity in multilinear fractal Fourier extension, including an example involving three base-four digits paired with two base-three digits; their setting and conclusions differ. Wu (2022), arXiv:2201.01909, develops general finite-type matrix representations and regularity of \(L^q\)-spectra, but does not state the explicit three-state carry matrix, closed eigenvalue, or the concrete \(L^2\)-failure result for this digit set. The transfer-matrix method itself is not claimed as new.

The specific contribution is the exact natural arithmetic invariant and the near-one-dimensional but non-\(L^2\) convolution consequence. Equivalent computations in specialized overlap-IFS or digit-convolution literature are a remaining priority risk.

## Limitations

No general classification of digit sets or sharp \(L^p\)-density threshold is proved. The result is for a single unweighted, same-scale self-convolution. Dimension \(D_2(\nu)<1\) proves non-\(L^2\), but does not establish singularity, nonexistence of all densities, or failure of other Fourier restriction inequalities. Previously known finite-type algorithms could provide an alternative route to the exact number.

## References

1. M. Carnovale, J. M. Fraser, A. E. de Orellana, *Fourier restriction estimates based on \(L^q\)-dimensions: beyond Stein--Tomas*, arXiv:2606.07143, first submitted 2026-06-05.
2. I. Oliveira, A. E. de Orellana, *Knapp-type obstructions in multilinear fractal Fourier extension*, arXiv:2602.08568, first submitted 2026-02-09.
3. Y.-F. Wu, *Matrix representations for some self-similar measures on \(\mathbb R^d\)*, arXiv:2201.01909, first submitted 2022-01-06.
