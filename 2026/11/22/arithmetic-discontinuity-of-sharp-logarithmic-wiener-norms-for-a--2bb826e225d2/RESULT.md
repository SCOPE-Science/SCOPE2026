# Arithmetic discontinuity of sharp logarithmic Wiener norms for asymmetric tent phases

## Finding

For every real \(0<\alpha<1\), define the continuous \(2\pi\)-periodic tent phase on \([0,2\pi]\) by
\[
\varphi_\alpha(x)=\begin{cases}x,&0\le x\le2\pi\alpha,\\
\dfrac{\alpha(2\pi-x)}{1-\alpha},&2\pi\alpha\le x\le2\pi,\end{cases}
\qquad F_\alpha(x)=e^{i\varphi_\alpha(x)}.
\]
Write \(A(\mathbb T)\) for the Wiener algebra with \(\|f\|_A=\sum_{k\in\mathbb Z}|\widehat f(k)|\), where \(\widehat f(k)=(2\pi)^{-1}\int_0^{2\pi}f(x)e^{-ikx}\,dx\). Then \(F_\alpha\in A(\mathbb T)\) and, for positive integers \(n\to\infty\),
\[
\boxed{\displaystyle\lim_{n\to\infty}\frac{\|F_\alpha^n\|_A}{\log n}
=\begin{cases}
\dfrac4{\pi q}\cot\!\left(\dfrac\pi{2q}\right),&\alpha=p/q\text{ reduced},\ 1\le p<q,\\[5pt]
\dfrac8{\pi^2},&\alpha\notin\mathbb Q.
\end{cases}}
\]
For rational \(\alpha\), the remainder after subtracting the displayed coefficient times \(\log n\) is bounded by a constant depending on \(\alpha\). The rational coefficients depend only on the reduced denominator \(q\), increase strictly from \(2/\pi\) at \(q=2\), and approach \(8/\pi^2\) from below. Thus the logarithmic coefficient is discontinuous at every rational parameter and continuous at every irrational parameter.

## Assumptions and scope

The exponent \(n\) is a positive integer, the logarithm is natural, and \(\alpha\) is fixed independently of \(n\). All Fourier integrals use normalized Haar measure on the circle. The two linear slopes are \(1\) and \(-\alpha/(1-\alpha)\). The result is a limit for this specified one-parameter class, not a claim about arbitrary nonsmooth phases or arbitrary real exponents. The phase is continuous and Lipschitz, hence \(F_\alpha\) belongs to \(W^{1,2}(\mathbb T)\subset A(\mathbb T)\).

## Proof

**1. Exact coefficient formula.** Put \(L=n/(1-\alpha)\), \(\beta=\alpha/(1-\alpha)\), and \(t=n-k\), with \(k\in\mathbb Z\). Integration on the two affine pieces, using continuity at \(x=2\pi\alpha\), gives whenever both denominators are nonzero
\[
\widehat{F_\alpha^n}(k)
=\frac{e^{2\pi i\alpha(n-k)}-1}{2\pi i}
\left(\frac1{n-k}+\frac1{n\beta+k}\right).
\]
Consequently
\[
\big|\widehat{F_\alpha^n}(k)\big|
=\frac{L}{\pi}\frac{|\sin(\pi\alpha t)|}{|t|\,|L-t|}.
\tag{1}
\]
At \(t=0\) the continuous value is \(\alpha\); if \(L\in\mathbb Z\), then at \(t=L\) it is \(1-\alpha\). This convention also follows by direct integration and covers all denominator coincidences.

**2. A uniform harmonic-mean lemma.** Put \(h_\alpha(j)=|\sin(\pi\alpha j)|\) for integers \(j\). Let
\[
 s_\alpha=\begin{cases}
 q^{-1}\sum_{j=0}^{q-1}|\sin(\pi p j/q)|,&\alpha=p/q\text{ reduced},\\
 \int_0^1|\sin(\pi u)|\,du,&\alpha\notin\mathbb Q.
 \end{cases}
\]
For every \(M\to\infty\), the mean of \(h_\alpha\) over each block of \(M\) consecutive integer indices tends to \(s_\alpha\), **uniformly over the block's starting index**. For rational parameters this is immediate from periodicity, with uniformly bounded deviations of partial sums from \(M s_\alpha\). For irrational parameters approximate the continuous, period-one function \(u\mapsto|\sin(\pi u)|\) uniformly by a finite trigonometric polynomial and sum each nonconstant exponential over the irrational rotation; the normalized geometric sums tend to zero uniformly in starting phase. Abel summation therefore gives, uniformly in integer \(b\) and real \(0\le\delta\le1\),
\[
\sum_{j=1}^M\frac{h_\alpha(b+j)}{j+\delta}
=s_\alpha\log M+o_\alpha(\log M).
\tag{2}
\]
For rational \(\alpha\), the error in (2) is \(O_\alpha(1)\). The same applies to the reversed sequence \(h_\alpha(b-j)\) since it is another orbit of the rotation. This follows from summation by parts and boundedness of \(\sum_{j\ge1}j^{-2}\), which absorbs replacing \(j\) by \(j+\delta\).

**3. Four logarithmic shoulders.** From (1), the norm is \(\pi^{-1}\) times the sum over \(t\in\mathbb Z\) of \(Lh_\alpha(t)/(|t||L-t|)\), with the two continuous-value conventions. Work separately in the regions \(0<|t|\le L/4\) and \(0<|t-L|\le L/4\), and then on their complement.

On either side of \(t=0\), the factor \(L/(|t||L-t|)\) differs from \(1/|t|\) by \(O(L^{-1})\); hence the two contributions total \(2s_\alpha\log L+o_\alpha(\log L)\), by (2). On either side of the moving pole \(t=L\), the factor differs from \(1/|t-L|\) by \(O(L^{-1})\), and (2) again gives \(2s_\alpha\log L+o_\alpha(\log L)\). To handle any integer \(t\) exceptionally close to \(L\), observe that
\[
\alpha t=t-n-(1-\alpha)(t-L),\quad
|\sin(\pi\alpha t)|=|\sin(\pi(1-\alpha)(t-L))|
\le\pi(1-\alpha)|t-L|.
\]
Thus the nearest-integer term contributes \(O_\alpha(1)\) even if \(L\) approaches an integer superpolynomially closely; an actual coincident pole contributes exactly \(1-\alpha\). Away from both neighborhoods and for \(-L\le t\le2L\), each summand is \(O(L^{-1})\), so their sum is \(O(1)\). For \(|t|>2L\), the summand is \(O(L/t^2)\) and the tails also sum to \(O(1)\). The \(t=0\) term is \(\alpha\). Consequently,
\[
\|F_\alpha^n\|_A=\frac{4s_\alpha}{\pi}\log L
+\begin{cases}O_\alpha(1),&\alpha\in\mathbb Q,\\o_\alpha(\log L),&\alpha\notin\mathbb Q.\end{cases}
\tag{3}
\]
For rational \(\alpha=p/q\), the moving-pole fractional offsets range over a finite set, so the bounded-error assertion in (2) and the nearest-integer estimate yield the stronger \(O_\alpha(1)\) remainder. Since \(\log L=\log n-\log(1-\alpha)\), the same leading coefficient governs \(\log n\).

**4. Evaluation and arithmetic ordering.** If \(\alpha=p/q\) is reduced, multiplication by \(p\) permutes the residues modulo \(q\), so
\[
 s_\alpha=\frac1q\sum_{j=1}^{q-1}\sin(\pi j/q)
=\frac1q\cot\!\left(\frac\pi{2q}\right).
\]
For irrational \(\alpha\), \(s_\alpha=2/\pi\). The function \(x\mapsto x\cot x\) is strictly decreasing for \(0<x<\pi/2\), since \(\sin x\cos x<x\), and tends to \(1\) as \(x\downarrow0\). Setting \(x=\pi/(2q)\) proves strict growth of rational coefficients to \(8/\pi^2\). Irrationals and rationals of arbitrarily large denominator approach any fixed parameter, whereas any fixed rational has strictly smaller coefficient; this proves the asserted continuity and discontinuity pattern.

## Verification

The coefficient identity was checked against independently evaluated piecewise Fourier integrals for rational and irrational parameters and for both resonant and nonresonant Fourier indices. The accompanying standard-library script repeats these finite checks and the exact symmetric-case benchmark
\[
\|F_{1/2}^n\|_A=1+\frac4\pi\sum_{j=1}^{n}\frac1{2j-1},\qquad n\ge1,
\]
which follows by splitting the integer frequency sum in (1) at the two poles. These computations only corroborate finite identities; the infinite limiting assertion follows from the uniform harmonic-mean proof above, not from finite testing. Run the packaged script with `python3 checks/verify_tent_phase.py`.

## Relationship to prior work

Ohrysko's October 2026 proof of Kahane's conjecture establishes logarithmic averaged growth under general nonconstant phases and reproduces the symmetric tent example, with an order-of-growth estimate and its Fourier coefficient formula [1, Section 8.1]. Lebedev [2, pp. 1–2] and [3, introduction] cite the classical fact that nonaffine piecewise-linear phases have Wiener norms of order \(\log n\), without the two-kink sharp coefficient or its arithmetic discontinuity. The present claim gives a leading constant for an asymmetric one-parameter phase family, including an exact rational-denominator law and an irrational limit, neither implied by the two-sided order estimates. It does not strengthen Kahane's general rigidity theorem.

## Limitations

The error estimate for irrational parameters is \(o_\alpha(\log n)\), not a uniform bound in \(\alpha\) and not generally a bounded remainder. The two-kink phase has a specifically normalized first slope. The result gives no classification for three or more breakpoints. Kahane's 1970 monograph is cited through later primary texts, but the original chapter has not been fully inspected; an older equivalent calculation remains a bibliographic risk. No independent verification is claimed.

## References

1. P. Ohrysko, *A proof of Kahane's conjecture in the Wiener algebra*, arXiv:2610.14981, first posted 2026-10-10, especially Sections 1 and 8.1. https://arxiv.org/abs/2610.14981
2. V. Lebedev, *Absolutely convergent Fourier series. An improvement of the Beurling–Helson theorem*, arXiv:1112.4892, first posted 2011-12-21. https://arxiv.org/abs/1112.4892
3. V. Lebedev, *On uniform convergence of Fourier series*, arXiv:1203.6703, first posted 2012-03-30. https://arxiv.org/abs/1203.6703
4. J.-P. Kahane, *Séries de Fourier absolument convergentes*, Springer, 1970, Ch. VI, Section 2 (not fully inspected; cited in [1–3]).
