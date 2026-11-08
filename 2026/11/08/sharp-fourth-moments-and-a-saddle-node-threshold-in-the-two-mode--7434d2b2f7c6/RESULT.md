# Sharp fourth moments and a saddle-node threshold in the two-mode Poisson–Charlier plane

## Finding
Let \(X\) have Poisson distribution with mean \(\lambda>0\). Write
\[
C_1(X)=X-\lambda,\qquad C_2(X)=X(X-1)-2\lambda X+\lambda^2.
\]
For every nonzero real \(f=aC_1+bC_2\), the normalized fourth moment \(\mathbb E f^4/(\mathbb E f^2)^2\) fills a sharp interval \([L_\lambda,U_\lambda]\), both endpoints uniquely attained up to nonzero real scaling. Set
\[
Q_\lambda(t)=(48\lambda^2+8\lambda)t^4-(48\lambda+4)t^3-(54\lambda+12)t^2-(12\lambda+11)t-3.
\]
For every \(\lambda>0\), this polynomial has exactly one positive root \(t_+(\lambda)\); its largest negative root \(t_-(\lambda)\) is simple. With \(K_\lambda(t)\) defined below,
\[
L_\lambda=K_\lambda(t_-(\lambda)),\qquad U_\lambda=K_\lambda(t_+(\lambda)).
\]
The only minimizing lines are \(\mathbb R(C_1+t_-C_2)\), and the only maximizing lines are \(\mathbb R(C_1+t_+C_2)\).

There is an additional exact *stationary-geometry transition*. Let \(\lambda_*\) be the unique positive root of
\[
\begin{aligned}
R(\lambda)={}&5038848\lambda^8-11967264\lambda^7+4047408\lambda^6+4710798\lambda^5\\
&+251748\lambda^4+10260\lambda^3+7587\lambda^2+180\lambda-1.
\end{aligned}
\]
Then \(1/250<\lambda_*<1/200\) and \(\lambda_*=0.0046412067125479685\ldots\). For \(0<\lambda<\lambda_*\), \(K_\lambda\) has four distinct real projective stationary directions: two local minima and two local maxima. At \(\lambda=\lambda_*\) one **nonglobal negative minimum** and an adjacent **negative local maximum** coalesce into a stationary inflection; for \(\lambda>\lambda_*\) precisely two real stationary directions remain, the unique global minimum and maximum. The extra local minimum never becomes globally optimal.

## Assumptions and scope
The distribution is on the nonnegative integers with probabilities \(e^{-\lambda}\lambda^k/k!\). The coefficient space is real and exactly \(\operatorname{span}\{C_1,C_2\}\). Normalization is by squared \(L^2\)-mass, with no additive constant mode. For \(a\ne0\), put \(t=b/a\); the projective point \(a=0\) means \(t=\infty\). The moment ratio is continuous on this real projective circle.

Poisson orthogonality gives \(\mathbb E C_1^2=\lambda\), \(\mathbb E C_2^2=2\lambda^2\), and \(\mathbb E C_1C_2=0\). Put
\[
\begin{aligned}
B_\lambda(t)={}&1+3\lambda+24\lambda t+(48\lambda+60\lambda^2)t^2\\
&+(32\lambda+192\lambda^2)t^3+(8\lambda+144\lambda^2+60\lambda^3)t^4,
\end{aligned}
\]
so the exact objective is
\[
K_\lambda(t)=\frac{B_\lambda(t)}{\lambda(1+2\lambda t^2)^2},\qquad
K_\lambda(\infty)=15+\frac{36}{\lambda}+\frac{2}{\lambda^2}.
\]

## Proof
**Exact moments.** The Touchard identity \(\mathbb E X^m=\sum_{j=0}^m \left\{\begin{smallmatrix}m\\j\end{smallmatrix}\right\}\lambda^j\), for \(0\le m\le8\), gives \(\mathbb E(C_1+tC_2)^4=\lambda B_\lambda(t)\), and the stated orthogonality gives \(\mathbb E(C_1+tC_2)^2=\lambda(1+2\lambda t^2)\). Direct differentiation yields
\[
\frac{dK_\lambda}{dt}=\frac{-8\lambda^3Q_\lambda(t)}{[\lambda(1+2\lambda t^2)]^3}.
\]

**Number of real stationary directions.** The coefficient signs of \(Q_\lambda(t)\) have exactly one change, so Descartes' rule gives exactly one positive real root, counted with multiplicity. Since \(Q_\lambda(-\infty)>0\) and \(Q_\lambda(0)=-3\), there is at least one negative root. Its quartic discriminant is exactly \(-256R(\lambda)\). The exact rational Sturm sequence of \(R\) has sign-variation counts \((3,3,2,2)\) at \((0,1/250,1/200,+\infty)\), respectively, and \(\gcd(R,R')=1\). Hence \(R\) has exactly one positive simple root in the stated rational interval; \(R<0\) below it and \(R>0\) above. A real quartic with at least two real roots and nonzero discriminant has four real simple roots when its discriminant is positive and precisely two when it is negative. At the transition the unique positive root stays simple; a pair of negative roots forms one double root. Continuity from \(Q_0(t)=-(t+1)(2t+1)(2t+3)\) shows the three negative roots below the threshold have two roots below \(-1\) and the largest in \((-1,-1/2)\): neither of the former can pass \(-1\), since \(Q_\lambda(-1)=2\lambda(24\lambda+7)>0\). The largest negative root persists uniquely for larger parameters, because \(Q_\lambda(-1)>0>Q_\lambda(0)\).

**Global maximum.** For \(t>0\), \(B_\lambda(t)-B_\lambda(-t)=48\lambda t+(64\lambda+384\lambda^2)t^3>0\). Thus no negative finite coefficient ratio can maximize. The positive critical root is the unique maximum on \((0,+\infty)\). Neither \(t=0\) nor the projective point \(t=\infty\) is an extremum: the derivative at zero is positive, and the derivative is strictly negative for all sufficiently large positive and negative \(t\), so the two sides of infinity have opposite differences from its limiting value. Thus the positive critical root is the unique global maximizing line.

**Global minimum and exclusion of metastable minima.** The same signed comparison excludes all positive finite \(t\), leaving negative critical roots. Above the transition there is only one such root, which is the minimum. Below the transition there are exactly two negative local minima; only the left one, at \(t<-1\), needs exclusion. Set \(F=\lambda B_\lambda\), \(N=\lambda(1+2\lambda t^2)\). For \(t=-1-u\) with \(u\ge0\), the *exact* difference polynomial
\[
\frac{F(t)N(-1/2)^2-F(-1/2)N(t)^2}{\lambda^4}=c_0+c_1u+c_2u^2+c_3u^3+c_4u^4
\]
has coefficients
\[
\begin{aligned}
c_0&=(192\lambda^3+284\lambda^2+53\lambda+2)/4,\\
c_1&=2\lambda(120\lambda^2+185\lambda+58),\\
c_2&=2(216\lambda^3+360\lambda^2+163\lambda-2),\\
c_3&=8\lambda(42\lambda^2+79\lambda+46),\\
c_4&=4(24\lambda^3+52\lambda^2+37\lambda+2).
\end{aligned}
\]
All coefficients except possibly \(c_2\) are positive; moreover
\[
4c_0c_4-c_2^2=32\lambda(104-2812\lambda-12850\lambda^2-22109\lambda^3-17340\lambda^4-5256\lambda^5)>0
\]
for \(0<\lambda\le1/200\). Indeed the parenthetical polynomial is strictly decreasing there and remains positive at \(1/200\). The arithmetic–geometric mean inequality \(c_0+c_4u^4\ge2\sqrt{c_0c_4}u^2\) makes the whole difference strictly positive. Therefore \(K_\lambda(t)>K_\lambda(-1/2)\) for every \(t\le-1\), while the rightmost negative local minimum is smaller than \(K_\lambda(-1/2)\) because \(Q_\lambda(-1/2)=\lambda(3\lambda-1)<0\). The left minimum cannot be global. Continuity and the same comparison settle the critical parameter. This proves the unique sharp lower bound and all equality cases. Since the projective circle is connected, every intermediate ratio is attained.

## Verification
Run `python check_ch.py` with SymPy 1.14.0. The checker reconstructs degree-eight Poisson moments using exact Stirling numbers, verifies the derivative and discriminant identities symbolically, obtains the four exact Sturm variations and the coprimality certificate for \(R\), checks the difference-polynomial coefficients and its positive-discriminant bound, and checks representative rational-parameter root counts. No finite sampling is used to infer the global statements.

## Relationship to prior work
Zacharovas and Hwang (arXiv:0810.4756v1, October 27, 2008) prove Poisson–Charlier orthogonality and the Parseval identity and develop Poisson approximation bounds; their Section 2 provides the starting normalization but not sharp mixed fourth moments or this bifurcation. Last and Penrose (arXiv:0909.3205v1, September 17, 2009) prove Fock/Poisson-chaos isometries and variance inequalities; those results likewise do not determine this fourth-order real-projective optimization. General mixed-chaos bounds, if available, need not be sharp in this two-mode subspace. The exact stationary-phase threshold, all-parameter sharp endpoints, and metastability exclusion are not implications of the checked results.

## Limitations
This is a two-dimensional real polynomial subspace, not the full Poisson chaos or any multivariate Poisson space. The threshold concerns stationary directions of the normalized \(L^4\) quotient, not a distributional phase transition. The mathematics has undergone self-review; no independent audit or exhaustive literature priority certification has been performed. Equivalent unindexed literature remains possible.

## References
1. V. Zacharovas and H.-K. Hwang, *A Charlier-Parseval approach to Poisson approximation and its applications*, arXiv:0810.4756v1 (first publicly submitted October 27, 2008), especially Section 2.
2. G. Last and M. D. Penrose, *Poisson process Fock space representation, chaos expansion and covariance inequalities*, arXiv:0909.3205v1 (first publicly submitted September 17, 2009), Sections 1–4.
