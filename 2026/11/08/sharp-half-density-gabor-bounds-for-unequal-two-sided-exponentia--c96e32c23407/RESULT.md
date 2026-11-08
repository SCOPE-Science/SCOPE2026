# Sharp half-density Gabor bounds for unequal two-sided exponential tails

## Finding

Let \(h,\lambda_-,\lambda_+>0\). For the normalized continuous asymmetric two-sided exponential
\[
g(t)=c\begin{cases}e^{\lambda_-t},&t<0,\\e^{-\lambda_+t},&t\ge0,\end{cases}\qquad
c^2=\frac{2\lambda_-\lambda_+}{\lambda_-+\lambda_+},
\]
consider the rectangular Gabor family
\[
\mathcal G=\{e^{\pi i mt/h}g(t-nh):m,n\in\mathbb Z\}.
\]
Its exact, optimal squared lower and upper frame bounds admit the following explicit formulas for **every pair of unequal tail rates** (and extend continuously to equal rates).

Put \(a=h\lambda_-\), \(b=h\lambda_+\), \(r=e^{-a}\), \(s=e^{-b}\), and
\[
U=\frac1{1+s^2},\qquad
V=\frac{r^2}{1+r^2},\qquad
W=\frac{r(r+s)}{(1+s^2)(1+r^2)}.
\]
The unique positive root
\[
q_* = \frac{W(a-b)+\sqrt{W^2(a-b)^2+4abUV}}{2aV}
\]
satisfies \(1<q_*<e^{a+b}\). Define \(x_*=(\log q_*)/(a+b)\in(0,1)\). Then
\[
\boxed{\displaystyle
A_{\mathcal G}=2hc^2\bigl(Ue^{-2bx_*}+Ve^{2ax_*}-2We^{(a-b)x_*}\bigr)>0,}
\]
and
\[
\boxed{\displaystyle
B_{\mathcal G}=2hc^2\left[\left(\frac1{1-s^2}+\frac{r^2}{1-r^2}\right)^2+
\left(\frac{s}{1-s^2}+\frac{r}{1-r^2}\right)^2\right].}
\]
The lower symbol extremum occurs at the unique interior time-fraction \(x_*\) and the half-turn Zak phase \(\theta=\pi/2\pmod\pi\). The upper symbol extremum occurs at the integer time-fraction \(x=0\pmod1\), \(\theta=0\pmod\pi\). This identifies the precise spatial location of the worst-conditioned fiber for all independent left and right decay rates.

## Assumptions and scope

All three parameters are strictly positive, and no relation between the decay rates is imposed. The Fourier convention is \(M_{\omega}f(t)=e^{2\pi i\omega t}f(t)\); thus the modulation step in the displayed family is \(1/(2h)\) and the lattice density is exactly two. By definition, the optimal squared frame bounds are the largest \(A\) and smallest \(B\) such that
\[
A\|f\|_2^2\le\sum_{n,m\in\mathbb Z}|\langle f,M_{m/(2h)}T_{nh}g\rangle|^2\le B\|f\|_2^2
\quad(f\in L^2(\mathbb R)).
\]
The normalization satisfies \(\|g\|_2=1\). No assertion is made for a different lattice density or for discontinuous one-sided limits of the decay parameters.

## Proof

**Dilation and Zak diagonalization.** Write \(G(x)=e^{ax}\) for \(x<0\) and \(G(x)=e^{-bx}\) for \(x\ge0\). Under the unitary dilation \(f(t)\mapsto\sqrt h\,f(ht)\), the given system has the frame bounds of the unit-spaced family with window \(\sqrt h\,cG\). Hence it suffices first to compute the bounds for the unnormalized \(G\), then multiply by \(hc^2\). The usual unitary Zak transform
\[
\mathcal Zf(x,\theta)=\sum_{n\in\mathbb Z}f(x-n)e^{in\theta},\qquad 0\le x<1,\quad0\le\theta<2\pi,
\]
identifies the half-density frame operator with scalar multiplication by
\[
F(x,\theta)=|\mathcal ZG(x,\theta)|^2+|\mathcal ZG(x,\theta+\pi)|^2.
\]
This identity follows by splitting the modulation frequencies into their two residue classes modulo the integer Zak modulation step, and using Parseval in each class. There is no additional factor of two in this Zak-symbol identity: for \(G=\mathbf1_{[0,1)}\), it yields the known tight bound \(F=2\), after including both residue classes. Frame bounds are the essential extrema of the continuous, periodic symbol.

For \(0\le x\le1\), let \(P=e^{-bx}\), \(Q=e^{ax}\), \(z=e^{i\theta}\), \(y=z^2\), \(r=e^{-a}\), and \(s=e^{-b}\). Summing the two geometric tails directly gives
\[
\mathcal ZG(x,\theta)=\frac{P}{1-sz^{-1}}+\frac{Qr z}{1-rz}.
\]
Separating the even and odd powers in \(z\), write \(\mathcal ZG=E+zO\), where
\[
E=\frac{P}{1-s^2y^{-1}}+\frac{Qr^2y}{1-r^2y},\qquad
O=\frac{Ps y^{-1}}{1-s^2y^{-1}}+\frac{Qr}{1-r^2y}.
\]
Since \(\theta\mapsto\theta+\pi\) fixes \(E,O\) and reverses the sign of \(z\),
\(F=2(|E|^2+|O|^2)\).

**Angular rigidity.** With common denominator \(D=(1-s^2y^{-1})(1-r^2y)\), the two numerators are \(u+vy\) and \(w+zy^{-1}\), respectively, where
\[
\begin{aligned}
u&=P-Qr^2s^2,&v&=r^2(Q-P),\\
w&=r(Q-Psr),&z&=s(P-Qrs).
\end{aligned}
\]
The ratio \(P/Q=e^{-(a+b)x}\) lies in \([rs,1]\). Thus \(u,v,w,z\ge0\), and \(uv+wz>0\) throughout the closed interval (at the two endpoints, at least one product remains positive). Writing \(t=\cos(2\theta)\), we obtain
\[
F(x,\theta)=2\,
\frac{u^2+v^2+w^2+z^2+2(uv+wz)t}
{(1+s^4-2s^2t)(1+r^4-2r^2t)}.
\]
Every denominator factor is strictly positive and strictly decreasing in \(t\in[-1,1]\), whereas the positive numerator is strictly increasing. Therefore, at every \(x\), the unique angular minimum occurs at \(t=-1\) and the unique angular maximum at \(t=1\). Equivalently the minimum occurs at \(\theta=\pi/2\pmod\pi\) and the maximum at \(\theta=0\pmod\pi\).

**Upper extremum.** At \(t=1\), the expression reduces to
\[
F_+(x)=2\left[\left(\frac{P}{1-s^2}+\frac{Qr^2}{1-r^2}\right)^2+
\left(\frac{Ps}{1-s^2}+\frac{Qr}{1-r^2}\right)^2\right].
\]
This is a strictly convex function of \(x\): each square is a positive linear combination of \(e^{-2bx}\), \(e^{2ax}\), and \(e^{(a-b)x}\), and the first two terms alone have strictly positive second derivative. Quasiperiodicity \(\mathcal ZG(x+1,\theta)=e^{i\theta}\mathcal ZG(x,\theta)\) gives \(F_+(1)=F_+(0)\). Strict convexity therefore forces the maximum at the two identified equivalent endpoints, and substitution at \(x=0\) yields the stated formula for \(B_{\mathcal G}\).

**Lower extremum.** At \(t=-1\), a direct expansion gives
\[
F_-(x)=2\left(Ue^{-2bx}+Ve^{2ax}-2We^{(a-b)x}\right).
\]
Its derivative has the sign of
\[
p(q)=aVq^2-W(a-b)q-bU,\qquad q=e^{(a+b)x}>0.
\]
The leading coefficient is strictly positive and the constant term strictly negative. Therefore the quadratic has exactly one positive root \(q_*\), with \(p(q)<0\) below that root and \(p(q)>0\) above it. As above, \(F_-(1)=F_-(0)\) by Zak quasiperiodicity. The function \(F_-\) is not constant because its three exponential exponents \(-2b\), \(a-b\), and \(2a\) are distinct and both \(U,V\) are positive. Consequently its unique turning point must lie in \((0,1)\), and is the strict global minimum. This establishes the expression for \(x_*\) and the sharp lower bound.

**Strict positivity.** The lower symbol is a sum of two squared moduli \(F_-(x)=2(|E(x,-1)|^2+|O(x,-1)|^2)\). Simultaneous vanishing would require both
\[
\frac QP=\frac{1+r^2}{r^2(1+s^2)}
\quad\text{and}\quad
\frac QP=\frac{s(1+r^2)}{r(1+s^2)},
\]
which implies \(rs=1\), contrary to \(0<r,s<1\). Hence \(F_-(x_*)>0\), so the family is a frame. The strict extrema on the compact Zak torus are essential extrema because the symbol is continuous. They are the actual optimal constants, not merely estimates.

## Verification

The standalone file `check_asym_gabor.py` is executable with Python 3 standard-library modules only. It compares the closed-form Zak symbol against independent truncated two-sided Fourier sums; checks the proposed extremal fibers and their strict positivity on deterministic parameter sets; and tests 6,160 interior Zak evaluations (12,320 lower/upper comparisons) for inclusion between the proposed extrema. Invoke `python3 check_asym_gabor.py`. The expected output is `ASYMMETRIC_EXPONENTIAL_GABOR_CHECKS_PASS 12431`.

The checker is a finite consistency test, not a substitute for the identities, monotonicity proof, or all-parameter argument above. The lower/upper bound normalization is also checked on the unit indicator window: at redundancy two, the Zak symbol is identically two.

## Relationship to prior work

Faulhuber and Shafkulovska (first arXiv version April 6, 2022, arXiv:2204.02917) study sharp Gabor frame bounds and optimal lattice shapes for several windows, including **the even two-sided exponential** \(e^{-\lambda|t|}\). They do not establish the unequal-left/right-rate formulas or the asymmetric bottleneck location above. The equal-rate specialization is not presented as new. Kloos and Stöckler (arXiv:1311.7359) prove general frame-set results for totally positive generators and treat quantitative lower bounds for the **even** two-sided exponential; this implies frame existence but not the present exact unequal-rate spectral constants. Gröchenig (arXiv:2301.00857) treats full rectangular frame sets of totally positive functions, a qualitative coverage rather than an exact frame-bound classification. Janssen's 1996 frame-bound calculations are an important possible source of earlier quantitative special cases; its plausible full text could not be accessed during this comparison, so priority cannot be certified against that source.

## Limitations

The result is restricted to rectangular lattices with product \(h\cdot(1/(2h))=1/2\), windows continuous at the origin with positive unequal exponential tail rates, and the optimal **squared** frame constants. It makes no claim about other redundancies, nonrectangular lattices, or optimal choice of \(h\). Historical novelty is provisional pending independent literature review (notably inaccessible early frame-bound calculations), and the symbolic/numerical checker does not constitute independent proof certification.

## References

1. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917 (first public version 2022-04-06), especially Sections 2.4 and 8, https://arxiv.org/html/2204.02917v2 .
2. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), especially Sections 4–5, https://arxiv.org/abs/1311.7359 .
3. K. Gröchenig, *Totally Positive Functions and Gabor Frames over Rational Lattices*, arXiv:2301.00857 (2023), https://arxiv.org/abs/2301.00857 .
4. A. J. E. M. Janssen, *Some Weyl–Heisenberg frame bound calculations*, Indagationes Mathematicae 7 (1996), 165–183, DOI 10.1016/0019-3577(96)85088-9 (full text not accessed).
