# Tight exterior-energy resonances and parity switching for two-frequency Fourier sums

## Finding

Let \(h>0\), \(I=[-1,1]\), and \(E_h=[-1-h,-1]\cup[1,1+h]\). For any two distinct real frequencies \(\lambda_1,\lambda_2\) with gap \(d=|\lambda_1-\lambda_2|>0\), let \(V_d\) be their two-dimensional complex exponential span. Define the optimal exterior-energy transfer factor
\[
\mathcal T_h(d)=\sup_{0\ne f\in V_d}\frac{\int_{E_h}|f(t)|^2\,dt}{\int_I|f(t)|^2\,dt}.
\]
Put
\[
s(d)=\frac{\sin d}{d},\qquad q_h(d)=\frac{\sin((1+h)d)-\sin d}{d}.
\]
The **entire generalized energy spectrum**, including its maximizers, is
\[
\boxed{\mathcal T_h(d)=\max\left\{\frac{h+q_h(d)}{1+s(d)},\ \frac{h-q_h(d)}{1-s(d)}\right\}.}
\]
The first branch is attained by a common-carrier multiple of \(\cos(dt/2)\); the second by a common-carrier multiple of \(\sin(dt/2)\). When the branches are unequal these are the only maximizing directions; at equality every nonzero function in \(V_d\) maximizes.

For **every** \(h>0\), the sharp frequency-gap design problem has the exact answer
\[
\boxed{\inf_{d>0}\mathcal T_h(d)=h.}
\]
The infimum is attained, at infinitely many positive gaps, **precisely** when
\[
\boxed{\sin((1+h)d)=(1+h)\sin d.}
\]
At such a gap the stronger identity
\[
\int_{E_h}|f(t)|^2\,dt=h\int_I|f(t)|^2\,dt
\]
holds for **every** \(f\in V_d\), not only an extremizer. There is at least one such gap in every interval
\[
\big((n+\tfrac12)\pi,(n+\tfrac32)\pi\big),\quad n=0,1,2,\ldots.
\]
The maximizing parity alternates between these intervals' endpoints and must switch an odd number of times (counting sign crossings) in each interval. At any nonresonant gap the sharp transfer strictly exceeds \(h\).

As a quantitative collision boundary, the odd branch dominates for all sufficiently small positive \(d\), and
\[
\mathcal T_h(d)=h(h^2+3h+3)-\frac{h(h+1)^3(h+2)}{20}d^2+O_h(d^4),\qquad d\downarrow0.
\]
The positive coefficient measures the initial loss from the confluent linear-polynomial extrapolation limit.

## Assumptions and scope

The frequencies are distinct, arbitrary real numbers; coefficients are arbitrary complex numbers, not both zero. The input and output are measured with **unnormalized** Lebesgue squared-energy integrals. Both exterior pieces are present and have equal length \(h>0\). The sharp gap infimum varies the separation \(d\) while holding \(h\) fixed; it is **not** the supremum over all gaps of the transfer factor. A common carrier frequency is immaterial because its exponential has unit modulus. All identities hold for every real \(h>0\), without frequency-separation assumptions.

## Proof

**1. Parity diagonalization and exact spectrum.** Put \(c=(\lambda_1+\lambda_2)/2\) and \(d=|\lambda_1-\lambda_2|>0\). Every element of \(V_d\) has a unique expression
\[
f(t)=e^{ict}\big(A\cos(dt/2)+B\sin(dt/2)\big),\qquad A,B\in\mathbb C.
\]
Both \(I\) and \(E_h\) are invariant under \(t\mapsto-t\). Thus the cross terms between the even cosine and odd sine vanish in both squared-energy integrals, even for arbitrary complex \(A,B\). Elementary integration using \(2\cos^2(dt/2)=1+\cos(dt)\) and \(2\sin^2(dt/2)=1-\cos(dt)\) yields
\[
\begin{aligned}
\int_I|f|^2&=(1+s(d))|A|^2+(1-s(d))|B|^2,\\
\int_{E_h}|f|^2&=(h+q_h(d))|A|^2+(h-q_h(d))|B|^2.
\end{aligned}
\]
For every \(d>0\), \(|\sin d|<d\), so \(1\pm s(d)>0\). The energy quotient is a weighted mean of the two displayed branch ratios, giving their maximum exactly, along with the complete equality cases.

**2. Sharp global minimum and all equality gaps.** Direct subtraction gives
\[
\frac{h+q_h}{1+s}-h=\frac{q_h-hs}{1+s},\qquad
\frac{h-q_h}{1-s}-h=-\frac{q_h-hs}{1-s}.
\]
Thus at least one branch is at least \(h\). Both equal \(h\) exactly if \(q_h=hs\), equivalent, after multiplying by \(d>0\), to
\[
F_h(d):=\sin((1+h)d)-(1+h)\sin d=0.
\]
If \(F_h(d)\ne0\), one branch is strictly above \(h\) and the other strictly below. At a zero both diagonal energy forms are proportional by \(h\), proving the asserted identity for every combination \(A,B\).

**3. Existence of infinitely many tight gaps and switches.** For \(d_n=(n+\tfrac12)\pi\),
\[
F_h(d_n)=\sin((1+h)d_n)-(1+h)(-1)^n.
\]
Since \(1+h>1\) and every sine lies between \(-1\) and \(1\), this is strictly negative for even \(n\), strictly positive for odd \(n\). Consequently each open interval \((d_n,d_{n+1})\) contains a zero by continuity, furnishing infinitely many sharp global minimizers. The branch difference is
\[
\frac{h+q_h}{1+s}-\frac{h-q_h}{1-s}
=\frac{2F_h(d)}{d(1-s(d)^2)}.
\]
The denominator is positive. Thus the winning cosine/sine branch changes between consecutive points \(d_n\), yielding an unavoidable parity switch in each indicated interval. No uniqueness of roots within an interval is claimed.

**4. Small-gap law.** Taylor expansion at \(d=0\) yields
\[
\begin{aligned}
s(d)&=1-\frac{d^2}{6}+\frac{d^4}{120}+O(d^6),\\
q_h(d)&=h-\frac{(1+h)^3-1}{6}d^2+\frac{(1+h)^5-1}{120}d^4+O_h(d^6).
\end{aligned}
\]
The cosine branch tends to \(h\), while the sine branch tends to \((1+h)^3-1=h(h^2+3h+3)>h\), so the sine branch is strictly optimal for small positive gaps. Dividing its two analytic even-power series gives
\[
\frac{h-q_h(d)}{1-s(d)}=h(h^2+3h+3)-\frac{(1+h)^5-(1+h)^3}{20}d^2+O_h(d^4).
\]
The numerator of the quadratic coefficient is \(h(h+1)^3(h+2)>0\). This establishes the expansion and completes the proof.

## Verification

Run `python3 CHECK.py` using only Python's standard library. The script compares the analytic even/odd transfer factors with independent Simpson quadrature for multiple window lengths and frequency gaps, verifies arbitrary complex-coefficient quotients remain between the predicted eigenvalues, bisects roots in prescribed half-integer-\(\pi\) brackets, and tests the small-gap asymptotic. These are reproducible finite numerical tests; the proof above establishes the universal claims without reliance on the script.

## Relationship to prior work

Zhang (2026) introduces the same symmetric adjacent exterior region and studies its worst-case integrated \(L^2\) transfer over the unrestricted class of \(k\)-term Fourier sums (Theorem 1.4 and Proposition 5.6, Section 5.3). The paper gives general asymptotic upper/lower estimates and does not resolve the **fixed two-frequency-gap** generalized spectrum, its exact minimum over the gap, or the infinite set of tight-transfer resonances. The global supremum over frequencies in Zhang's notation is a different optimization direction from the present **infimum of fixed-gap worst-case transfer**.

Two previously available exact two-frequency results determine **single exterior-point** evaluation norms and their collision defect. Integrating their pointwise sharp bounds cannot automatically give a sharp integrated transfer bound, because the maximizing coefficient vector varies with the observation point. The present result instead diagonalizes the entire integral operator on the two-sided exterior set and identifies all gaps at which its generalized eigenvalues coincide. Published results on bandlimited concentration over separated windows concern a different, infinite-dimensional frequency model and do not imply this two-dimensional gap-design statement.

## Limitations

The theorem covers only two frequencies and **symmetric, equal-length exterior observation intervals**. It does not determine the worst transfer over all possible frequency gaps, the one-sided interval transfer optimum, the corresponding problem with unequal exterior intervals, or stability under noisy frequency estimation. The root equation exactly characterizes optimal gaps but does not give a simple explicit ordered list or assert one root per bracket. A specialized historical result using different language (e.g. two-atom windowed frame design) could still give equivalent coverage; independent external validation is not claimed.

## References

1. Ruizhe Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, arXiv:2607.10501, first public 2026-07-11, Theorem 1.4, Section 5.3, Proposition 5.6. https://arxiv.org/html/2607.10501v2
2. *Sharp two-frequency exterior Fourier leverage and the quadratic collision defect*, publicly available research result (2026). https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-sharp-two-frequency-exterior-fourier-leverage-and-the-quadratic--517d41b07a68/RESULT.md
3. *Sharp exterior leverage for two arbitrary Fourier frequencies*, publicly available research result (2026). https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-exterior-leverage-for-two-arbitrary-fourier-frequencies--a88bbfc8602c/RESULT.md
