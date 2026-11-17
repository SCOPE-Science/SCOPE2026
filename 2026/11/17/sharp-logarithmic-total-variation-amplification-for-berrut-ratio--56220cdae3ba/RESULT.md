# Sharp logarithmic total-variation amplification for Berrut rational interpolation

## Finding
For integer \(n\ge2\), set \(x_j=j\), \(0\le j\le n\), and let \(B_n\) be Berrut's alternating-weight rational interpolation operator. Its variation gain from discrete nodal total variation into continuous total variation satisfies
\[
C_n:=\sup_{V_d(y)>0}\frac{\operatorname{Var}_{[0,n]}(B_n y)}{V_d(y)}=\frac2\pi\log n+O(1),
\]
where the implied constant is **absolute and uniform in** \(n\). More precisely, with step data \(s^{(k)}_j=\mathbf1_{\{j\ge k\}}\),
\[
C_n=\max_{1\le k\le n}\operatorname{Var}_{[0,n]}(B_ns^{(k)}),\qquad
\operatorname{Var}_{[0,n]}(B_ns^{(1)})=\frac2\pi\log n+O(1).
\]
The first equality is exact for every finite \(n\); the second and third are sharp first-order asymptotics, not asserted exact finite formulas. This shows that bounded range overshoot of step data does not imply bounded *accumulated oscillation*.

## Assumptions and scope
For a real vector \(y=(y_0,\ldots,y_n)\), define \(V_d(y)=\sum_{j=0}^{n-1}|y_{j+1}-y_j|\). For noninteger \(x\in(0,n)\),
\[
(B_ny)(x)=\frac{\sum_{j=0}^n(-1)^j y_j/(x-j)}{\sum_{j=0}^n(-1)^j/(x-j)},
\]
continuously extended at each node by \((B_ny)(j)=y_j\). All real data are allowed. The denominator has no zero away from nodes: on every cell the positive alternating-tail decomposition in the proof gives its absolute value. Variation means the ordinary Jordan total variation over the full closed interval, including all cells, not just nodal oscillation. Constants implicit in \(O(1)\) are independent of the step position and the number of cells.

## Proof
**1. Reduction to the natural extremizers.** Constants are reproduced. Every data vector decomposes exactly as
\[
y=y_0\mathbf1+\sum_{k=1}^n(y_k-y_{k-1})s^{(k)}.
\]
Linearity, Jordan variation's triangle inequality and the interpolatory nature of \(B_n\) give the upper bound by the largest step variation. Taking the maximizing step proves the finite-dimensional identity for \(C_n\).

**2. Alternating tails and reciprocal denominator.** Define for integers \(q\ge1\) and real \(z>0\)
\[
A_q(z)=\sum_{r=0}^{q-1}\frac{(-1)^r}{z+r},\qquad A_0(z)=0,\qquad
A_\infty(z)=\int_0^1\frac{u^{z-1}}{1+u}\,du.
\]
Alternating-series bounds yield \(A_q(z)>0\), \(A_q(z)\le z^{-1}\), \(|A'_q(z)|\le z^{-2}\), and \(A_q(z)\ge[z(z+1)]^{-1}\). The exact remainder formula is
\[
A_q(z)=A_\infty(z)-(-1)^qA_\infty(z+q).
\]
Since \(A_\infty(z)=1/(2z)+O(z^{-2})\) for \(z\ge1\), uniformly for all positive integers \(q\),
\[
A_q(z)=\frac1{2z}-\frac{(-1)^q}{2(z+q)}+O(z^{-2}),\qquad z\ge1.
\]
For a cell \(x=m+t\), \(0\le m\le n-1\), \(0<t<1\), the absolute denominator is
\[
S_m(t)=A_{m+1}(t)+A_{n-m}(1-t)>0.
\]
The infinite-tail reflection identity is
\[
A_\infty(t)+A_\infty(1-t)=\frac\pi{\sin\pi t}.
\]
Write \(\delta_m=(m+1)^{-1}+(n-m)^{-1}\). The tail remainder and its first derivative are bounded by an absolute multiple of \(\delta_m\) on the closed cell. Furthermore \(S_m\ge[2t(1-t)]^{-1}\), and its derivative has absolute value at most \(t^{-2}+(1-t)^{-2}\). Taking reciprocals, then differentiating the reciprocal identity, proves the uniform *endpoint-inclusive* estimate
\[
\left\|\frac1{S_m(t)}-\frac{\sin\pi t}{\pi}\right\|_{C^1[0,1]}\le C\delta_m.
\]
The displayed reciprocal expressions extend smoothly to endpoints; this is an estimate on those extensions, not on singular denominators.

**3. Variation of a single jump.** Fix \(1\le k\le n\). To the left of its jump cell, \(m\le k-2\), its rational interpolant is, up to a sign, \(A_{n-k+1}(k-m-t)/S_m(t)\). To the right, \(m\ge k\), it equals one minus, up to a sign, \(A_k(m+t-k+1)/S_m(t)\). The exceptional cell \(m=k-1\) has absolute variation bounded by a universal constant: separate the single poles at \(t=0\) and \(t=1\), multiply numerator and denominator by \(t(1-t)\), and use the alternating-tail bounds and the positive lower bound \(t(1-t)S_m(t)\ge1/2\). The resulting numerator and denominator and their first derivatives are uniformly bounded.

On an ordinary cell, let \(d=k-m\ge2\) on the left or \(d=m-k+1\ge1\) on the right, with corresponding finite-tail length \(q=n-k+1\) or \(q=k\). Since \(|A'_q(z)|\le z^{-2}\), its numerator differs in \(C^1\) from the constant \(A_q(d)\) by \(O(d^{-2})\). Combining this with the reciprocal-denominator estimate gives
\[
\left|\operatorname{Var}_{[m,m+1]}B_ns^{(k)}-\frac2\pi A_q(d)\right|
\le C\left(\frac1{d^2}+\frac{\delta_m}{d}\right).
\]
Here the main comparison wave is \(A_q(d)\sin(\pi t)/\pi\), whose variation is exactly \(2A_q(d)/\pi\). Both error sums are uniformly bounded: \(\sum d^{-2}\le\pi^2/6\); the remaining sums reduce either to a \(d^{-2}\) sum or to \(\sum_{d=1}^{h}1/[d(h-d+1)]=2H_h/(h+1)\le2\), where \(H_h=\sum_{r=1}^h1/r\). Consequently, with empty sums interpreted as zero,
\[
\operatorname{Var}_{[0,n]}B_ns^{(k)}
=\frac2\pi\left(\sum_{d=2}^k A_{n-k+1}(d)+\sum_{d=1}^{n-k}A_k(d)\right)+O(1),
\]
with **uniform remainder** for all \(k,n\).

**4. Sharp coefficient.** Substitute the alternating-tail asymptotic and sum the harmonic terms. Put \(\alpha=(-1)^{k+1}\) and \(\beta=(-1)^{n-k}\). Replacing boundedly different endpoint harmonic indices gives
\[
\sum_{d=2}^k A_{n-k+1}(d)+\sum_{d=1}^{n-k}A_k(d)
=\frac12\big[(1-\alpha)H_k+(1-\beta)H_{n-k}+(\alpha+\beta)H_n\big]+O(1).
\]
There are only four sign pairs. For \((\alpha,\beta)=(+1,+1)\), the bracket is \(2H_n\); for \((+1,-1)\), it is \(2H_{n-k}\); for \((-1,+1)\), it is \(2H_k\); and for \((-1,-1)\), it is \(2(H_k+H_{n-k}-H_n)\). Each is at most \(2H_n\). Thus every step has variation at most \((2/\pi)H_n+O(1)\), uniformly. For the endpoint-adjacent step \(k=1\), the only nonempty main sum is \(\sum_{d=1}^{n-1}A_1(d)=H_{n-1}\), hence its variation is \((2/\pi)H_{n-1}+O(1)\). The step norm identity from part 1 and \(H_n=\log n+O(1)\) prove both assertions.

## Verification
The accompanying standalone `CHECKER.py` verifies exact alternating barycentric step identities with rational arithmetic over 2,469 configurations; it separately tests jump decomposition and numerical variation at grid sizes up to 128. The reported variation values show the leading logarithmic law but are **not** used as a proof of the unbounded-dimensional result. The proof above is analytical and gives a uniform absolute remainder.

## Relationship to prior work
Bos, De Marchi and Hormann investigate logarithmic growth of the **Lebesgue** (bounded-data-to-maximum-norm) constant of the equispaced Berrut interpolant. Their openly available dated manuscript contains no total-variation norm theorem. Bos, De Marchi, Hormann and Klein likewise study Lebesgue functions of barycentric rational interpolation; Bos, De Marchi, Hormann and Sidon extend maximum-norm results to other node classes. Nochetto and Salgado construct a different interpolation operator that is explicitly variation diminishing. Published results on bounded monotone range for Berrut data do not imply bounded accumulated total variation: the variation is a sum of many oscillations, not a one-point range extremum. The sharp \(2/\pi\) coefficient here concerns the variation of a single step's rational interpolant and the induced discrete-BV operator norm; it is not a restatement of a Lebesgue norm.

## Limitations
Only unweighted consecutive equidistant nodes, the original alternating-weight Berrut formula, real data and full-interval Jordan variation are treated. No exact closed form for the finite-\(n\) maximum or uniqueness of the maximizing step is claimed. The statement does not cover irregular nodes, weighted variation, different barycentric schemes or continuous variation of data between sample locations. The earliest-source date is the date on the openly hosted 2010 manuscript; the date that its file first became accessible online could not be independently established. Absence of an indexed covering result does not establish historical priority; an unindexed equivalent remains possible. Independent mathematical validation has not been performed.

## References
1. L. Bos, S. De Marchi and K. Hormann, *On the Lebesgue constant of Berrut's rational interpolant at equidistant nodes*, openly hosted manuscript dated October 25, 2010, https://www.math.unipd.it/~demarchi/papers/lebesgue2.pdf; subsequent J. Comput. Appl. Math. 236 (2011), 504–510, https://doi.org/10.1016/j.cam.2011.04.004.
2. L. Bos, S. De Marchi, K. Hormann and G. Klein, *On the Lebesgue constant of barycentric rational interpolation at equidistant nodes*, https://www.math.unipd.it/~demarchi/papers/lebesgue.pdf.
3. L. Bos, S. De Marchi, K. Hormann and J. Sidon, *Bounding the Lebesgue constant for Berrut's rational interpolant at general nodes*, manuscript May 10, 2012, https://www.math.unipd.it/~demarchi/papers/Lebesgue-Berrut-General.pdf.
4. R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, https://arxiv.org/abs/1211.1069 (2012).
