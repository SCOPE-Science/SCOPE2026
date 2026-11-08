# Exact real-axis stability frontier of SSP-optimal third-order implicit Runge–Kutta methods

## Finding
For every integer \(s\ge 2\), take the uniquely SSP-optimal, order-three, \(s\)-stage implicit Runge–Kutta tableau from Weng, Yu, and Zhu, with diagonal stage coefficient
\[
\gamma_s=\frac12\left(1-\sqrt{\frac{s-1}{s+1}}\right),
\]
strictly lower stage coefficient \(\delta_s=1/\sqrt{s^2-1}\), and weights \(b_i=1/s\). Define
\[
c_s=\sqrt{1-s^{-2}},\quad
q_s=\sqrt{\frac{s+1}{s-1}},\quad
t_s(x)=\frac{1-(\delta_s-\gamma_s)x}{1+\gamma_s x}\quad(x\ge0).
\]
The scalar-decay stability function is **exactly**
\[
R_s(-x)=1-c_s+c_s t_s(x)^s.
\]
Its closed negative-real-axis absolute-stability interval is \([-X_s,0]\), with no further stable negative-real points, where
\[
X_s=\begin{cases}
2\sqrt{s^2-1}\bigl(s+\sqrt{s^2-1}\bigr),&s\text{ even},\\[3pt]
\displaystyle\frac{1+u_s}{\delta_s-\gamma_s(1+u_s)},&s\text{ odd},
\end{cases}
\qquad
u_s=\left(\frac{2}{c_s}-1\right)^{1/s}.
\]
Precisely, \(|R_s(-x)|\le1\) if and only if \(0\le x\le X_s\), with strict inequality for \(0<x<X_s\). At the threshold \(R_s(-X_s)=1\) for even \(s\), whereas \(R_s(-X_s)=-1\) for odd \(s\). Beyond it, even-stage methods amplify positive scalar modes and odd-stage methods amplify with reversed sign:
\[
R_s(-x)>1\ (s\text{ even}),\qquad R_s(-x)<-1\ (s\text{ odd}),\quad x>X_s.
\]
The thresholds satisfy \(X_s=4s^2+O(1)\). At fixed \(s\), the arbitrarily-stiff limit is
\[
L_s:=\lim_{x\to\infty}R_s(-x)=1-c_s+(-1)^s c_s q_s^s,
\]
which is always outside \([-1,1]\). Along increasing even and odd stage counts respectively, \(L_s\to e\) and \(L_s\to-e\). Thus growing the number of SSP-optimal implicit stages expands the stable negative-real interval quadratically but does **not** yield unconditionally stable stiff decay.

## Assumptions and scope
This is the exact-arithmetic scalar linear test equation \(y'=-\lambda y\), with \(\lambda\ge0\), step \(h\ge0\), and \(x=h\lambda\). The tableau is precisely the one given by Theorem 5.2, equations (5.5)–(5.6), of the 2026 source. The claim quantifies over every integer \(s\ge2\) and every real \(x\ge0\). It classifies the intersection of absolute stability with the negative real axis; it makes no claim about the complete complex stability region.

## Proof
**1. Exact stage transfer.** For \(y'=zy\) with unit starting value, let \(v=(I-zA)^{-1}{\bf1}\), and \(S_i=\sum_{j=1}^{i}v_j\) with \(S_0=0\). The lower-triangular tableau gives
\[
(1-\gamma_s z)v_i=1+\delta_s z S_{i-1},\qquad
S_i=\frac{1+(\delta_s-\gamma_s)z}{1-\gamma_s z}S_{i-1}+\frac1{1-\gamma_s z}.
\]
Writing \(t(z)=(1+(\delta_s-\gamma_s)z)/(1-\gamma_s z)\), the finite geometric sum gives, for nonzero \(z\) away from the stage pole,
\[
S_s=\frac{t(z)^s-1}{\delta_s z}.
\]
Therefore \(R_s(z)=1+zb^{\mathsf T}(I-zA)^{-1}{\bf1}=1+(t(z)^s-1)/(s\delta_s)\). Since \(1/(s\delta_s)=c_s\), substitution \(z=-x\) proves the closed form; continuity covers \(x=0\).

**2. Monotone parameter geometry.** A direct differentiation gives
\[
t_s'(x)=-\frac{\delta_s}{(1+\gamma_s x)^2}<0,
\qquad t_s(0)=1,
\qquad \lim_{x\to\infty}t_s(x)=-q_s,
\]
where \(\delta_s/\gamma_s=1+q_s\). Thus \(t_s\) runs strictly through \((-q_s,1]\). Both \(c_s\in(0,1)\) and \(q_s>1\).

**3. Even-stage stability.** When \(s\) is even, \(R_s(-x)=1-c_s+c_s t_s(x)^s\ge1-c_s>0\). Hence \(|R_s(-x)|\le1\) is equivalent to \(|t_s(x)|\le1\). The strictly decreasing \(t_s\) first reaches \(-1\) when
\[
X_s=\frac2{\delta_s-2\gamma_s}.
\]
Here \(\delta_s-2\gamma_s=s/\sqrt{s^2-1}-1>0\), and rationalization gives the displayed exact even-stage threshold. For larger \(x\), \(t_s(x)<-1\), giving \(R_s(-x)>1\).

**4. Odd-stage stability.** When \(s\ge3\) is odd, \(t_s(x)^s\) and therefore \(R_s(-x)\) decrease strictly with \(x\), starting at \(1\). Its endpoint is \(L_s=1-c_s(1+q_s^s)\). Because
\[
q_s^s=\exp\bigl(s\operatorname{artanh}(1/s)\bigr)>e>2,
\qquad c_s\ge\sqrt{8/9}>2/3,
\]
one has \(L_s<-1\). Thus there is exactly one crossing of \(-1\), and it is the complete absolute-stability boundary. Solving \(1-c_s+c_s t_s(x)^s=-1\) yields \(t_s(x)=-u_s\) with \(1<u_s<q_s\), and solving this rational equation yields the displayed \(X_s\). The inequality \(u_s<q_s\) also ensures the denominator is strictly positive. For larger \(x\), \(R_s(-x)<-1\).

**5. Large-stage and stiff limits.** Since \(q_s^s=\exp(s\operatorname{artanh}(1/s))\to e\) and \(c_s\to1\), the stiff amplification tends to \(e\) along even \(s\) and \(-e\) along odd \(s\). Even-stage threshold rationalization gives \(X_s=4s^2-3+O(s^{-2})\). For odd \(s\), set \(w=1/s\). Expanding the explicitly defined parameters gives \(\gamma_s=w/2-w^2/4+w^3/4-3w^4/16+O(w^5)\), \(\delta_s=w+w^3/2+O(w^5)\), and \(u_s=1+w^3+O(w^5)\). Hence \(\delta_s-\gamma_s(1+u_s)=w^2/2-w^4/8+O(w^5)\), so \(X_s=4s^2+1+O(s^{-1})\), in particular \(X_s=4s^2+O(1)\). These prove the claimed common quadratic leading term. All endpoint inequalities are exact for each finite \(s\), not inferred from these expansions.

## Verification
The standalone `verify.py` independently computes the stability function by forward substitution in the \(s\)-stage triangular system, compares it with the closed form, checks both side limits of each proposed threshold, and tests the parity and large-stage expansions. Run `python verify.py`; on the prepared package it returned `VERIFY_OK 864`. These are finite high-precision numerical checks; the proof above covers all stages and all real nonnegative \(x\).

## Relationship to prior work
Weng, Yu, and Zhu (arXiv:2610.37425v1, Theorem 5.2) establish that this tableau is uniquely SSP-optimal among general implicit Runge–Kutta tableaux of third order and fixed stage count, but do not state its scalar-decay real-axis stability interval or alternating large-stage stiff limit. Ferracina and Spijker (2007, §3.3) give the same coefficient family as an optimization candidate. Ketcheson, Macdonald, and Gottlieb (2008 postprint / 2009 article, §2.2 and §3) explain the linear stability function and optimal SSP constructions, not this analytic all-stage threshold. Fekete and Horváth (2019, §2.2 and Fig. 2) plot the absolute-stability region for the four-stage member; their plotted left intercept is compatible with, but does not imply, the closed form for all stages and its parity-dependent stiff limit. Radius of absolute monotonicity is a different stability criterion from \(|R_s(-x)|\le1\).

## Limitations
The result covers exact scalar decay and, by spectral calculus, normal operators with nonpositive real spectrum; it does not prove nonlinear positivity, TVD, full complex A-stability regions, order-uniform stiff accuracy, or stable error propagation for nonnormal semidiscretizations. In particular the stable scalar-decay threshold should not be mistaken for the SSP radius. Literature priority remains subject to independent checking of other classical rational-stability analyses.

## References
1. Z. Weng, H. Yu, and Q. Zhu, *Phase-type representations for Strong Stability Preserving Runge–Kutta methods*, arXiv:2610.37425v1, first posted 2026-10-27. https://arxiv.org/abs/2610.37425
2. L. Ferracina and M. N. Spijker, *Strong Stability of Singly-Diagonally-Implicit Runge-Kutta Methods*, Leiden report 2007-11, 2007, §3.3. https://math.leidenuniv.nl/reports/files/2007-11.pdf
3. D. I. Ketcheson, C. B. Macdonald, and S. Gottlieb, *Optimal Implicit Strong Stability Preserving Runge–Kutta Methods*, *Applied Numerical Mathematics* **59** (2009), 373–392. https://www.davidketcheson.info/assets/papers/implicit_ssp_postprint.pdf
4. I. Fekete and Á. Horváth, *Some Embedded Pairs for Optimal Implicit Strong Stability Preserving Runge–Kutta Methods*, 2019, §2.2 and Fig. 2. https://imrefekete.web.elte.hu/files/2019_FH_ECMI.pdf
