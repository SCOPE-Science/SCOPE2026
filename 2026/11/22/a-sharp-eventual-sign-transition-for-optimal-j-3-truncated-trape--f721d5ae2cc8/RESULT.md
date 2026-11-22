# A sharp eventual-sign transition for optimal \(J=3\) truncated-trapezoidal convolution weights

## Finding
For the optimized third-member truncated trapezoidal rule, let
\[
\delta_3(\zeta)=(1-\zeta)+\frac{(1-\zeta)^2}{2}+(\sqrt2-1)(1-\zeta)^3+\frac{2-\sqrt2}{4}(1-\zeta)^4.
\]
Fix a timestep \(h>0\) and an exponential relaxation rate \(\lambda>0\), with dimensionless product \(q=h\lambda\). Define its exponential-kernel convolution weights by
\[
\frac{h}{\delta_3(\zeta)+q}=\sum_{n\ge0}\omega_n(q)\zeta^n.
\]
Put
\[
\begin{split}
G(R)={}&R^5-(1+3\sqrt2)R^4+9(1+\sqrt2)R^3\\
&-\left(37+\frac{51\sqrt2}{2}\right)R^2+(72+46\sqrt2)R-(52+34\sqrt2).
\end{split}
\]
The polynomial \(G\) has exactly one real root \(R_*\) in \([1,3]\), and this root belongs to \((1769/1000,177/100)\). Define \(q_*=-\delta_3(R_*)\), approximately \(0.6108597918577606\). Then:

1. For every \(0<q\le q_*\), there is an integer \(N(q)\) such that \(\omega_n(q)>0\) for every \(n\ge N(q)\).
2. For every \(q>q_*\), infinitely many \(\omega_n(q)\) are strictly positive and infinitely many are strictly negative.

Thus \(q_*\) is the exact transition between **eventual positivity** and **infinitely recurring sign loss**. This is not a claim of positivity at *every* lag below the threshold. At the concrete choice \(q=1\), the fourth-lag coefficient is already negative:
\[
\frac{\omega_4(1)}h=\frac{109218772-77331942\sqrt2}{6436343}<0.
\]

## Assumptions and scope
The underlying convolution kernel is \(k(t)=e^{-\lambda t}\) for \(t\ge0\), with Laplace transform \(K(s)=1/(s+\lambda)\). The optimized \(J=3\) truncated-trapezoidal coefficients are \(c_2=2\sqrt2-2\) and \(c_3=2-\sqrt2\), exactly as in the published rule. The claims concern the unmodified, constant-step convolution weights over all nonnegative integer lags; \(h\) merely scales them by a positive factor. They do not assert an analogous classification for other \(J\), mixed kernels, variable steps, or fully coupled discretizations.

## Proof
Write \(d(z)=\delta_3(z)\), \(P_q(z)=d(z)+q\), and \(v=(2-\sqrt2)/4>0\). Expanding gives
\[
P_q(z)=v z^4-z^3+\left(\frac12+\frac{3\sqrt2}{2}\right)z^2-(1+2\sqrt2)z+1+\frac{3\sqrt2}{4}+q.
\]
Its derivative factors as
\[
d'(z)=(2-\sqrt2)\left(z-2-\frac{\sqrt2}{2}\right)\left(z^2-(1+\sqrt2)z+1+\sqrt2\right).
\]
The quadratic factor has negative discriminant and is everywhere positive. Hence \(d\) decreases up to its unique real minimum at \(R_c=2+\sqrt2/2\) and increases thereafter. Also \(d(z)>0\) for all \(z<1\), using its expression in positive powers of \(1-z\). The minimum value is \(-q_c\), where \(q_c=5/8+5\sqrt2/16\). Therefore \(0<q<q_c\) gives exactly two real roots \(1<R<R_c<T\), together with a nonreal conjugate pair \(z_\pm\). For \(q>q_c\), there are no real roots; at \(q=q_c\), the two real roots coalesce.

For the two-real-root regime, set \(Q(x)=P_q(Rx)/(1-x)=c_0+c_1x+c_2x^2+c_3x^3\). Its other roots are \(T/R\) and \(z_\pm/R\). Consequently it factors, for real \(t>0\), \(u\), and \(\nu>0\), as
\[
Q(x)=c_0(1-tx)(1-2ux+\nu x^2),\qquad t=R/T,\quad\nu=R^2/|z_+|^2,\quad u^2<\nu.
\]
A direct coefficient calculation gives
\[
\begin{split}
F&=c_1c_3-c_3^2+c_0^2-c_0c_2\\
&=c_0^2(1-\nu)(t^2\nu-2tu+1)\\
&=-vR^2G(R).
\end{split}
\]
The middle factor \(t^2\nu-2tu+1\) is strictly positive because \(u^2<\nu\). Thus \(\operatorname{sgn}(|z_+|-R)=-\operatorname{sgn}G(R)\).

To establish that there is exactly one crossing, substitute \(R=1+2x\), \(0\le x\le1\), into \(G'(R)\). Its degree-four Bernstein coefficients, in increasing order, are
\[
26+10\sqrt2,\quad20-\frac{13\sqrt2}{2},\quad44-29\sqrt2,\quad130-\frac{163\sqrt2}{2},\quad390-188\sqrt2.
\]
All five are strictly positive, proving \(G'>0\) on \([1,3]\). Exact substitution gives \(G(1769/1000)<0<G(177/100)\); hence the unique \(R_*\) lies in that interval, below \(R_c\). Because \(R(q)\) increases strictly with \(q\), we have \(|z_+|>R\) for \(q<q_*\), and \(|z_+|<R\) for \(q_*<q<q_c\). The latter inequality persists at \(q=q_c\) by continuity.

For \(q<q_*\), \(1/P_q\) has exactly one pole of least modulus: the simple positive pole \(R\). Its coefficient expansion therefore satisfies
\[
\frac{\omega_n(q)}h\sim A R^{-n},\qquad A=-\frac1{R P_q'(R)}>0,
\]
which proves eventual strict positivity.

For \(q>q_*\), no pole of least modulus lies on the positive real axis. If the real coefficients of \(1/P_q\) were eventually nonnegative, subtracting their finite initial polynomial would yield a nonnegative-coefficient power series whose radius-of-convergence point on the positive real axis must be singular (Pringsheim's theorem). This contradicts the exact pole locations. The same argument for the negated tail excludes eventual nonpositivity. Therefore both positive and negative coefficients occur infinitely often.

It remains to include \(q=q_*\). At the crossing, write \(z_+=u+iV\), with \(V>0\), \(R=|z_+|\), and let \(T>R\) be the second real root. Partial fractions give
\[
\frac{\omega_n(q_*)}h=A R^{-n}+2\operatorname{Re}(B z_+^{-n})+O(T^{-n}),
\quad A=-\frac1{R P_{q_*}'(R)}>0,\quad B=-\frac1{z_+P_{q_*}'(z_+)}.
\]
The inequality \(A>2|B|\) is equivalent, after cancellation of positive factors and using \(V^2=R^2-u^2\), to
\[
(R+u)((T-u)^2+V^2)>2R(T-R)^2.
\]
The exact rational-radical certificate in `check_ttr3.py` shows
\[
1.769<R<1.77,\quad3.2<T<3.4,\quad0.7<u<1.1.
\]
These bounds make the left-hand side greater than \(15\) and the right-hand side less than \(10\), so the inequality holds strictly. The contribution from \(T\) decays more rapidly than \(R^{-n}\), proving eventual strict positivity at equality as well.

## Verification
Run `python check_ttr3.py` with SymPy installed. This verifies the defining coefficients, derivative factorization, uniqueness through positive Bernstein coefficients, root and parameter brackets, exact modulus-crossing resultant, strict endpoint residue-domination inequalities, and the exact negative fourth-lag coefficient at \(q=1\). The universal coefficient-sign conclusions follow from the proof; finite lag calculations and approximations to \(q_*\) alone would not prove them.

## Relationship to prior work
Ferrari derived the optimized \(J\)-indexed truncated-trapezoidal coefficients and proved their A-stability and second-order accuracy; the present finding uses exactly the published \(J=3\) coefficients. It does not rederive those optimization results. Earlier convolution-quadrature analysis by Lubich and Banjai provides the numerical framework. Banjai's positivity statement is an operator-coercivity inequality, not positivity of each exponential-kernel quadrature weight. A distinct prior analysis of the optimized \(J=2\) method obtained an all-lag exponential-kernel positivity threshold; neither its different polynomial nor its all-lag statement implies the \(J=3\) eventual-sign threshold here. Sign behavior is independent of A-stability: even an A-stable generating function can have signed convolution weights.

## Limitations
The result concerns eventual, not all-lag, positivity. Neither negativity of a particular convolution coefficient nor a sign-oscillation theorem is by itself a theorem about the stability or accuracy of a full convolution-equation solver. At the crossing, the eventual positivity proof gives no claimed uniform cutoff in the parameter \(q\). Historical priority beyond the inspected sources remains open to independent review.

## References
- Matteo Ferrari, *Convolution quadrature based on a truncated trapezoidal rule*, arXiv:2607.11422v1, first submitted 2026-07-13, especially Section 3, Theorem 3.1 and Table 2. https://arxiv.org/abs/2607.11422
- L. Banjai, *Implicit/explicit, BEM/FEM coupled scheme for acoustic waves with the wave equation in the second order formulation*, Comput. Methods Appl. Math. 22 (2022), 757–773. https://doi.org/10.1515/cmam-2021-0186
- C. Lubich, *Convolution quadrature and discretized operational calculus I–II*, Numer. Math. 52 (1988), 129–145 and 413–425.
- Ph. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009; singularity analysis and Pringsheim's theorem.
