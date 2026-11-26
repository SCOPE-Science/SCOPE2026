# Sharp \(3/5\) Zak-zero isolation threshold for the centered order-three B-spline

## Finding
For the centered cardinal B-spline \(B_3\) of order three (polynomial degree two), define the Zak transform
\[
Z_\lambda B_3(x,\nu)=\sqrt\lambda\sum_{k\in\mathbb Z}B_3(\lambda(x-k))e^{2\pi i k\nu},\qquad \lambda>0.
\]
**Theorem.** For every real \(3/5\le\lambda\le1\), the full zero set in the half-open fundamental square \([0,1)\times[0,1)\) is precisely
\[
\big\{(x,\nu):Z_\lambda B_3(x,\nu)=0\big\}=\{(1/2,1/2)\}.
\]
The lower endpoint is sharp for this connected interval: for every \(3/7<\lambda<3/5\), the frequency fiber \(\nu=1/2\) contains the nondegenerate zero segment
\[
\left[\frac32\left|2-\frac1\lambda\right|,\;1-\frac32\left|2-\frac1\lambda\right|\right]\times\{1/2\}.
\]
This does not assert a classification of zeros at all smaller positive scales. The zero-segment obstruction is known in related B-spline literature; the new statement is the exact zero exclusion for the entire interval \([3/5,1]\).

## Assumptions and scope
The spline is the compactly supported even function
\[
B_3(t)=\begin{cases}
3/4-t^2,&|t|\le1/2,\\
\tfrac12(3/2-|t|)^2,&1/2\le|t|\le3/2,\\
0,&|t|\ge3/2.
\end{cases}
\]
The overlapping formulas agree at their endpoints. Parameters, position and frequency are real. The Zak sum is finite at every point. No limiting hypothesis beyond \(3/5\le\lambda\le1\) is imposed. It is useful to put \(q=\lambda\) and \(S_q(x)=\sum_{k\in\mathbb Z}(-1)^k B_3(q(x-k))\), so \(Z_q B_3(x,1/2)=\sqrt q\,S_q(x)\).

## Proof
**1. Symmetries and interior-frequency exclusion.** Quasiperiodicity and evenness reduce the search to \(0\le x\le1/2\), \(0\le\nu\le1/2\). Specifically, \(Z_qB_3(1-x,\nu)=e^{2\pi i\nu}\overline{Z_qB_3(x,\nu)}\), and \(Z_qB_3(x,1-\nu)=\overline{Z_qB_3(x,\nu)}\). Fix \(3/5\le q\le1\). On \(0\le x\le1/2\), only indices \(-2,-1,0,1,2\) can contribute. With \(\theta=2\pi\nu\) and
\[
A_j(x)=B_3(q(j-x))-B_3(q(j+x))\quad(j=1,2),
\]
we have
\[
\operatorname{Im}\Big(\frac{Z_qB_3(x,\nu)}{\sqrt q}\Big)
=\sin\theta\,[A_1(x)+2A_2(x)\cos\theta].
\]
Put \(h(t)=-B'_3(t)\) for \(t\ge0\). Explicitly \(h(t)=2t\) for \(0\le t\le1/2\), \(h(t)=3/2-t\) for \(1/2\le t\le3/2\), and zero thereafter. Differentiating the differences and integrating from zero gives
\[
A_1(x)-2A_2(x)=q\int_0^x H_q(t)\,dt,
\]
\[
H_q(t)=h(q(1-t))+h(q(1+t))-2h(q(2-t))-2h(q(2+t)).
\]
On \(0\le t\le1/2\), the first pair of \(h\)-terms is nonincreasing in \(t\): it is constant while both arguments lie in the decreasing branch of \(h\), and subsequently decreases with slope \(-3q\). The second pair is
\[
(3/2-2q+qt)_++(3/2-2q-qt)_+,
\]
which is nondecreasing in \(t\). Here \(y_+=\max(y,0)\). Thus \(H_q\) is nonincreasing, and direct endpoint evaluation gives
\[
H_q(t)\ge H_q(1/2)=(5q-3)/2\ge0.
\]
At \(q=3/5\) the inequality is strict on \(0\le t<1/2\), as follows from the preceding piecewise linear formulas. Hence \(A_1(x)>2A_2(x)\) whenever \(x>0\). Since \(A_2(x)\ge0\), for every \(x>0\) and \(0<\nu<1/2\), the displayed imaginary part is strictly positive. No zero lies in that rectangle.

**2. The position boundary.** At \(x=0\), the Zak sum is real. Write \(c=\cos\theta\), \(b_1=B_3(q)=(3/2-q)^2/2\) and \(b_2=B_3(2q)=(3/2-2q)_+^2/2\). Then
\[
\frac{Z_qB_3(0,\nu)}{\sqrt q}=3/4+2b_1c+2b_2(2c^2-1).
\]
For \(3/5\le q\le1\), one has \(b_1\ge4b_2\), so this quadratic is nondecreasing for \(-1\le c\le1\). At \(c=-1\) its value is \(3(q-1/2)^2>0\) when \(q\le3/4\), and \(3/4-(3/2-q)^2>0\) when \(q\ge3/4\). Therefore no zero occurs at \(x=0\); positivity of the Zak sum at \(\nu=0\) follows from the nonnegative spline and its strictly positive central tap.

**3. The half-frequency boundary.** The cardinal spline has Fourier transform \(\widehat{B_3}(\xi)=[\sin(\pi\xi)/(\pi\xi)]^3\) under the \(2\pi\)-Fourier convention. Poisson summation (or direct Fourier coefficient comparison of anti-periodic functions) gives
\[
S_q(x)=\frac1q\sum_{n\in\mathbb Z}\left[\frac{\sin(\pi(n+1/2)/q)}{\pi(n+1/2)/q}\right]^3e^{2\pi i(n+1/2)x}.
\]
The series converges absolutely and uniformly. For \(3/5\le q\le1\), put \(d=2-1/q\in[1/3,1]\) and \(\mu=1/d=q/(2q-1)\in[1,3]\). At every half-integer \(r=n+1/2\), the identity \(\sin(\pi(2-d)r)=\sin(\pi dr)\) implies, by Fourier coefficient comparison,
\[
\boxed{S_q(x)=(2q-1)^2 S_\mu(x)}.\tag{1}
\]
We prove \(S_\mu(x)>0\) for \(0\le x<1/2\), every \(1\le\mu\le3\). When \(3/2\le\mu\le3\), only taps \(k=0,1\) contribute for these \(x\); therefore \(S_\mu(x)=B_3(\mu x)-B_3(\mu(1-x))>0\), by strict decay of the spline on \([0,3/2]\). When \(1\le\mu\le3/2\), only taps \(-1,0,1\) contribute. Define
\[
t_0=3/(2\mu)-1,\qquad t_1=1/(2\mu),\qquad 0\le t_0\le t_1\le1/2.
\]
Direct substitution into the spline formula yields
\[
S_\mu(x)=\begin{cases}
3/4-(3/2-\mu)^2-2\mu^2x^2,&0\le x\le t_0,\\
3/4-\mu^2x^2-\tfrac12(3/2-\mu+\mu x)^2,&t_0\le x\le t_1,\\
\mu(3-\mu)(1/2-x),&t_1\le x\le1/2.
\end{cases}
\]
Each branch is nonincreasing. The first branch has value \(3/4-3(3/2-\mu)^2\ge0\) at \(t_0\), with equality only at \(\mu=1\), \(t_0=1/2\). The second has value \([1-(2-\mu)^2]/2\ge0\) at \(t_1\), with equality only at \(\mu=1\), \(t_1=1/2\). The last is strictly positive whenever \(x<1/2\). Also \(S_\mu(1/2)=0\) by pairing \(k\) and \(1-k\). Thus \(S_q(x)>0\) for \(0\le x<1/2\), while \(S_q(1/2)=0\). Together with the previous steps and the stated symmetries, this proves the complete one-zero classification.

**4. Sharpness just below \(3/5\).** Let \(3/7<q<3/5\) and \(b=1/q\in(5/3,7/3)\). Set \(d=|2-b|<1/3\). If \(d=0\), all half-integer Fourier coefficients of \(S_q\) vanish, hence \(S_q\equiv0\). Otherwise, with \(\mu=1/d>3\), the same Fourier comparison gives \(S_q(x)=\pm(d/b)^2S_\mu(x)\), where the sign is negative if \(b>2\). For \(3d/2\le x\le1-3d/2\), each term in \(S_\mu(x)\) is zero because \(\mu x\ge3/2\) and \(\mu(1-x)\ge3/2\). This interval has positive length as \(d<1/3\). It is therefore a full zero segment at frequency \(1/2\), proving the threshold cannot be lowered to a larger connected interval ending at \(1\).

## Verification
The accompanying standalone `verify.py` uses exact rational arithmetic to check the spline identities, half-frequency alias identity (1), all relevant branch inequalities and the zero segments on a finite rational grid. It separately checks the sign of the imaginary Zak sum numerically at interior sample points. Run `python3 verify.py` with Python's standard library. The finite sample is corroboration only; the inequalities, Fourier series comparison and finite-branch argument above prove the theorem for all real parameters in the stated interval.

## Relationship to prior work
Hasannasab--Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames* (2026), classify higher-order B-spline Zak zeros on the larger-scale side \(\lambda>1\), while the present theorem fills a continuous order-three window on the other side of the critical scale. Lemvig--Nielsen (2015) and Lemvig (2026) give Gabor-frame obstructions associated with horizontal Zak-zero segments; that mechanism supports the sharpness comparison but does not yield uniqueness of the half-frequency zero inside \([3/5,1]\). Kloos--Stöckler (2013) consider the separate variation-diminishing class of totally positive and exponential B-splines; the present scaled cardinal spline's knot pattern does not follow from a unit-scale unique-zero statement. These differences concern theorem hypotheses and conclusions, not merely titles.

## Limitations
This paper does not classify the full Zak-zero set for all \(0<\lambda<3/5\), address B-spline orders greater than three in this parameter interval, or establish general Gabor frame regions beyond the stated Zak-zero statement. The sharpness segment is not claimed as novel independently of the earlier B-spline obstruction theory. The literature comparison is bounded and may miss a hidden equivalent of the uniqueness result; no independent validation is claimed.

## References
1. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116 (first public 2026-09-11), https://arxiv.org/abs/2609.13116.
2. J. Lemvig and K. H. Nielsen, *Counterexamples to the B-spline conjecture for Gabor frames*, arXiv:1507.03982 (2015), https://arxiv.org/abs/1507.03982.
3. J. Lemvig, *A new family of hyperbolic slits in the Gabor frame set of B-spline generators*, arXiv:2601.07642 (2026), https://arxiv.org/abs/2601.07642.
4. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), https://arxiv.org/abs/1311.7359.
