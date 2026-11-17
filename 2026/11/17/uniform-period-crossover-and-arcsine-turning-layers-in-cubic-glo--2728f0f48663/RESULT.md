# Uniform period crossover and arcsine turning layers in cubic global centers

## Finding

**Theorem.** Fix \(h>0\). For every \(k\geq0\), the planar cubic system
\[
\dot x=y,\qquad \dot y=-x-kx^3-hxy^2
\tag{1}
\]
has a global center at the origin. Let \(A>0\) be the positive turning coordinate of the unique orbit through \((A,0)\), and \(T_{h,k}(A)\) its minimal period in the original physical time. The function \(A\mapsto T_{h,k}(A)\) is strictly decreasing from \(2\pi\) to zero. Moreover, **uniformly across the entire unbounded coefficient range** \(k\in[0,\infty)\),
\[
\boxed{\displaystyle
T_{h,k}(A)=\frac{2\pi}{\sqrt h\,A\sqrt{1+kA^2}}\bigl(1+O_h(A^{-2})\bigr)}
\qquad(A\to\infty).
\tag{2}
\]
Thus the period is of order \(A^{-1}\) when \(k=0\), of order \(A^{-2}\) when \(k>0\) is fixed, and, for every nonnegative coefficient sequence satisfying \(k_A A^2\to\rho<\infty\),
\[
A\,T_{h,k_A}(A)\longrightarrow\frac{2\pi}{\sqrt{h(1+\rho)}}.
\tag{3}
\]

Let \(U_A\) be uniformly distributed over one original-time period of the orbit and set
\[
R_A=A^2-x(U_A)^2,\qquad W_A=\exp(-hR_A/2),\qquad S_A=\operatorname{sgn}x(U_A).
\]
For every \(A>0\), \(S_A\) is a fair \(\{\pm1\}\)-valued sign and is independent of \(R_A\). As \(A\to\infty\), **uniformly for all \(k\ge0\)**, the law of \(R_A\) converges in total variation at rate \(O_h(A^{-2})\) to the probability density
\[
\boxed{\displaystyle p_h(r)=\frac{h}{\pi\sqrt{e^{hr}-1}}\,,\qquad r>0.}
\tag{4}
\]
Equivalently, the limiting squared-gap cumulative distribution is \(\Pr(R\le r)=2\pi^{-1}\arcsin\sqrt{1-e^{-hr}}\). Consequently, at the same total-variation rate \(W_A\) converges to the one-sided arcsine law
\[
\boxed{\displaystyle \Pr(W\in dw)=\frac{2\,dw}{\pi\sqrt{1-w^2}}\,,\qquad 0<w<1.}
\tag{5}
\]
In particular \(x(U_A)/A\) converges in distribution to a fair \(\pm1\) variable. The new assertions are the all-coefficient crossover (2)--(3) and the coefficient-uniform turning-layer law (4)--(5); the already published \(k=0\) leading period/square-wave limit is not claimed separately as new.

## Assumptions and scope

Both \(h>0\) and \(A>0\) are real; \(k\ge0\). In a fixed-parameter statement \(h,k\) are held fixed. The word *uniform* in (2), (4), and (5) means: for each fixed \(h>0\) there are \(A_0(h)>0\) and \(C(h)<\infty\), independent of the nonnegative number \(k\), giving the indicated error bounds for all \(A\ge A_0(h)\). The coefficient \(k\) may depend on \(A\) arbitrarily within this bound. Physical time is never reparametrized. Total variation is \(\sup_B|\Pr(R_A\in B)-\int_Bp_h(r)dr|\). Endpoints of each orbital traversal have zero time measure.

Define for \(s\ge0\)
\[
\Phi(s)=\int_0^s(1+ku)e^{hu}\,du,\quad
f_h(r)=\frac{e^{hr}-1}{h},\quad
g_h(r)=\frac{e^{hr}-1-hr}{h^2}.
\]
The exact first integral and positive squared orbital velocity are
\[
H(x,y)=e^{hx^2}y^2+\Phi(x^2),\qquad
v_A(x)=e^{-hx^2}\int_{x^2}^{A^2}(1+ks)e^{hs}\,ds\quad(|x|\le A).
\tag{6}
\]
Here \(v_A\) denotes \(y^2\) on the orbit, not a signed velocity.

## Proof

**1. First integral, center, and original-time period.** Differentiating (6) and using (1),
\[
\frac{dH}{dt}=2e^{hx^2}y\,[\dot y+hx y^2+x(1+kx^2)]=0.
\]
The even function \(\Phi(x^2)\) is strictly increasing in \(|x|\), starts at zero, and tends to infinity. For each \(A>0\), the level \(H=\Phi(A^2)\) consists of the two graphs \(y=\pm\sqrt{v_A(x)}\), \(-A\le x\le A\), with simple turning points and with no equilibria. Every such oval is one periodic trajectory, proving global centricity. Its minimal physical period is
\[
T_{h,k}(A)=4\int_0^A\frac{dx}{\sqrt{v_A(x)}}
=4\int_0^1\left[\int_{u^2}^1(1+kA^2 t)e^{hA^2(t-u^2)}dt\right]^{-1/2}du.
\tag{7}
\]
For each \(0\le u<1\), the integral in brackets increases strictly with \(A\), because \(h>0\) and \(t>u^2\) except on a null set. Hence the period decreases strictly. As \(A\downarrow0\), its integrand tends to \((1-u^2)^{-1/2}\) and is bounded above by that integrable function; therefore \(T\to2\pi\). Convergence to zero at infinity follows from (2).

**2. Exact squared-turning-gap equation.** Write \(r=A^2-x^2\) and \(C=1+kA^2\). Changing variables in (6) gives the *exact identity*
\[
v_A(\sqrt{A^2-r})=\int_0^r[1+k(A^2-r+s)]e^{hs}ds
=Cf_h(r)-kg_h(r).
\tag{8}
\]
Since \(0\le g_h(r)/f_h(r)\le1/h\) for all \(r\ge0\), and since \(\epsilon=k/C\le A^{-2}\), the normalized velocity \(v_A/C=f_h-\epsilon g_h\) satisfies
\[
\left(1-\frac1{hA^2}\right)f_h(r)
\le f_h(r)-\epsilon g_h(r)\le f_h(r).
\tag{9}
\]
For \(A^2\ge2/h\) both bounds are positive. Equation (7), with \(dx=-dr/[2\sqrt{A^2-r}]\), is equivalently
\[
\frac{A\sqrt C}{2}\,T_{h,k}(A)=J_{A,k},\quad
J_{A,k}=\int_0^{A^2}\frac{dr}{\sqrt{1-r/A^2}\sqrt{f_h(r)-\epsilon g_h(r)}}.
\tag{10}
\]

**3. The uniform error bound.** Let
\[
J_\infty=\int_0^\infty f_h(r)^{-1/2}\,dr.
\]
This is finite: the integrand is asymptotic to \(r^{-1/2}\) at zero and decays exponentially at infinity. Its first moment \(\int_0^\infty r f_h(r)^{-1/2}dr\) is finite as well. On \(0\le r\le A^2/2\), the elementary inequalities \((1-s)^{-1/2}-1\le2s\) for \(0\le s\le1/2\) and \((1-t)^{-1/2}-1\le2t\) for \(0\le t\le1/2\), together with (9), give the pointwise bound
\[
0\le\frac1{\sqrt{1-r/A^2}\sqrt{f_h-\epsilon g_h}}
-\frac1{\sqrt{f_h}}
\le \frac{C_h(1+r)}{A^2\sqrt{f_h(r)}}.
\tag{11}
\]
On \(A^2/2\le r<A^2\), use (9) and \(f_h(r)^{-1/2}\le C_h e^{-hr/2}\) to bound the integrated contribution by \(C_h A^2e^{-hA^2/4}\). The missing limit tail past \(A^2\) is at most \(C_h e^{-hA^2/2}\). Hence, uniformly for \(k\ge0\),
\[
|J_{A,k}-J_\infty|\le C_h A^{-2}.
\tag{12}
\]
Substitute \(w=e^{-hr/2}\) to evaluate
\[
J_\infty=\sqrt h\int_0^\infty\frac{dr}{\sqrt{e^{hr}-1}}
=\frac2{\sqrt h}\int_0^1\frac{dw}{\sqrt{1-w^2}}=\frac\pi{\sqrt h}.
\tag{13}
\]
Combining (10)--(13) proves (2). With \(k_A A^2\to\rho\), (3) follows by taking the limit in \(A\sqrt{1+k_A A^2}T\). Fixed positive \(k\) yields \(T\sim2\pi/(\sqrt{hk}\,A^2)\); \(k=0\) yields \(2\pi/(\sqrt h A)\).

**4. Exact sampled-time law and total-variation rate.** Each interior position \(x\in(-A,A)\) is traversed exactly twice per period. Dividing the resulting time density \(2/(T\sqrt{v_A(x)})\) between the two symmetric signs shows that \(S_A\) is fair and independent of \(x^2\), hence of \(R_A\). On \(0<r<A^2\), change variables \(x=\sqrt{A^2-r}\), using two symmetric values of \(x\), to obtain
\[
\Pr(R_A\in dr)=\frac{D_{A,k}(r)}{J_{A,k}}dr,
\qquad D_{A,k}(r)=\frac{\mathbf1_{(0,A^2)}(r)}{\sqrt{1-r/A^2}\sqrt{f_h(r)-\epsilon g_h(r)}}.
\tag{14}
\]
The cancellation of \(A\sqrt C\) follows from (10); the normalization \(\int D_{A,k}=J_{A,k}\) is exact. The estimates in Step 3 also give the stronger \(L^1\) convergence
\[
\int_0^\infty|D_{A,k}(r)-f_h(r)^{-1/2}|dr\le C_h A^{-2}.
\tag{15}
\]
Since \(J_{A,k}\to J_\infty>0\), normalization preserves the \(O_h(A^{-2})\) bound. By (13) the limiting density is \(f_h^{-1/2}/J_\infty=h/[\pi\sqrt{e^{hr}-1}]\), proving (4). The strictly monotone transformation \(w=e^{-hr/2}\) sends (4) to the density \(2/[\pi\sqrt{1-w^2}]\), and measurable pushforward cannot increase total variation, proving (5). Finally \(R_A=O_{\Pr}(1)\) uniformly in \(k\) while \(x(U_A)^2=A^2-R_A\), so \(|x(U_A)|/A\to1\) in probability. Combined with the independent fair sign, this proves the final occupation statement.

## Verification

The standalone `CHECK.py` differentiates the first integral symbolically and verifies the exact gap identity by a second independent differentiation. It independently integrates the physical-time quadrature for several values of \(h\), \(k\), and \(A\), including a very large stiffness coefficient, and compares finite-period ratios and turning-gap cumulative probabilities to the theorem's constants. Running `python CHECK.py` in an environment with SciPy and SymPy must print `CUBIC_CENTER_UNIFORM_ENDPOINT_LAYER_CHECK_OK`. These finite tests are corroboration; the uniform bounds for all amplitudes and parameters follow analytically from (8)--(15).

## Relationship to prior work

Appis and Llibre (2024), Theorem 4, classify the present cubic system as a global center. In their notation \(a_4=-k\), \(a_6=-h\), with all other coefficients zero. Their full accessible paper proves qualitative classification, not a uniform nonlinear-period crossover or a turning-layer occupation theorem. Chanda, Ghose-Choudhury and Guha (2018) develop the general Jacobi-multiplier method for Liénard-type equations with squared-velocity terms; the existence of a first integral by this method is established background.

A published cubic-center result entitled *Universal logarithmic frequency and square-wave limit at a cubic global center* covers the \(k=0\) axis, including its leading period and coarse square-wave occupation, after identifying the parameter \(\kappa=h\). It does not imply the uniform \(k\ge0\) period law, the \(kA^2\) transition, or the total-variation turning-gap density. Another published result entitled *Strict period decrease and sharp large-amplitude laws for quintic global centers* treats \(\dot y=-x-\alpha x^3y^2-\beta x^5\), of different polynomial degree, and does not cover (1) as a case or by its stated hypotheses. A separate cubic-center Cauchy occupation theorem treats a linearly conjugate \(k=0\) field in another observable; its Cauchy and moment statements do not imply (4) for arbitrary \(k\).

## Limitations

The parameter \(h>0\) is fixed; the constants are not uniform as \(h\downarrow0\). The theorem does not treat negative cubic stiffness \(k\), external forcing, perturbations away from the integrable family, or the joint distribution of velocity and turning-gap statistics. The \(k=0\) leading period limit and coarse square-wave limit have prior coverage; new information lies in the exact all-\(k\) crossover and strong microscopic occupation law. Like any literature comparison, the searches do not prove universal publication priority against unindexed equivalent results. Independently checked mathematics beyond the stated self-review is not asserted.

## References

1. R. F. Appis and J. Llibre, *Global centers of a family of cubic systems*, *Aequationes Mathematicae* 98 (2024), 1373–1389. DOI: `10.1007/s00010-024-01051-7`; published online 2024-04-05; https://link.springer.com/article/10.1007/s00010-024-01051-7.
2. S. Chanda, A. Ghose-Choudhury and P. Guha, *Jacobi-Maupertuis metric of Liénard type equations and Jacobi last multiplier*, *Electronic Journal of Differential Equations* 2018 (120), 1–9. arXiv:`1706.02219`, https://ejde.math.txstate.edu/Volumes/2018/120/chanda.pdf.
3. *Universal logarithmic frequency and square-wave limit at a cubic global center*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-logarithmic-frequency-and-square-wave-limit-at-a-cubic--5ef7d7af5678.
4. *Strict period decrease and sharp large-amplitude laws for quintic global centers*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-strict-period-decrease-and-sharp-large-amplitude-laws-for-quinti--ffe383da977f.
5. *Cauchy time concentration and the order-one moment threshold in a cubic global center*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cauchy-time-concentration-and-the-order-one-moment-threshold-in--0ac06783efe2.
