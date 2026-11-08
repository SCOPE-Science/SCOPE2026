# Reentrant cubic response of rank-one Perron–Wright component weights

## Finding

Let \(S\) be a nonempty finite type set, let \(\mu\) be a probability law giving strictly positive mass to every type, and let \(u:S\to(0,\infty)\) satisfy \(\mathbb E_\mu u=1\). Put
\[
\alpha=\mathbb E_\mu u^2,\quad
\beta=\mathbb E_\mu u^3,\quad
\gamma=\mathbb E_\mu u^4,\qquad
\kappa(x,y)=\frac{u(x)u(y)}{\alpha}.
\]
The symmetric rank-one kernel \(\kappa\) is strictly positive and critical: its associated operator \(Kf(x)=\int\kappa(x,y)f(y)\,\mu(dy)\) satisfies \(Ku=u\) and has spectral radius one.

Let \(\mathsf C_t(k,r)\) be the fixed-size, fixed-surplus connected-graph weight of Hu--Sun (2026, equations (3.9)--(3.10)), where \(k\) is the number of labelled vertices, \(r=e-k+1\ge0\) is the surplus, and \(t>0\) is the edge-intensity tilt. For all \(t\) sufficiently near one, its analytic rooted-tree critical radius \(\rho(t)\) satisfies
\[
\log\rho(1+\varepsilon)
=\frac{\alpha^2}{2\beta}\varepsilon^2
+\mathfrak c_3\varepsilon^3+O(\varepsilon^4),\qquad
\boxed{\mathfrak c_3=\frac{\alpha^2(3\alpha^2\beta+\alpha\gamma-6\beta^2)}{6\beta^3}}.
\]
Consequently, for every fixed surplus \(r\ge0\) and bounded real \(s\), uniformly for \(s\) in compact sets,
\[
\boxed{
\exp\!\left\{\frac{\alpha^2}{2\beta}s^2 k^{1/3}\right\}
\frac{\mathsf C_{1+s k^{-1/3}}(k,r)}{\mathsf C_1(k,r)}
\longrightarrow\exp(-\mathfrak c_3 s^3)
}\qquad(k\to\infty).
\]
This is a cubic, non-Gaussian correction at the moderate-tilt scale; it concerns the *connected-component enumerator* and is not asserted as a probability limit for the largest components of an ambient random graph.

The cubic correction has a **reentrant sign** already within strictly positive two-type kernels. For \(0<a<1\), take
\[
\mu_a(1-a)=\frac{20}{20+a},\qquad
\mu_a(21)=\frac{a}{20+a}.
\]
Then \(\mathbb E_{\mu_a}u=1\), and the sign of \(\mathfrak c_3\) is the opposite of that of
\[
Q(a)=13000a^4-325210a^3+509550a^2-2860a+1.
\]
The polynomial \(Q\) has exactly two roots \(0<a_-<a_+<1\), with
\[
0.00037<a_-<0.00038,\qquad 0.00525<a_+<0.00527.
\]
Thus \(\mathfrak c_3<0\) for \(0<a<a_-\) and \(a_+<a<1\), whereas \(\mathfrak c_3>0\) for \(a_-<a<a_+\), with zero at each boundary. For example, at \(a=1/200\),
\[
(\alpha,\beta,\gamma)=\left(\frac{11}{10},\frac{6599}{2000},\frac{19835201}{400000}\right),\qquad
\mathfrak c_3=\frac{5826325450}{862096019397}>0.
\]
In contrast, the homogeneous one-type model has \(\mathfrak c_3=-1/3\). The sign of the moderate-tilt skew correction is therefore not universal, even among positive rank-one critical kernels.

## Assumptions and scope

All type probabilities are strictly positive, all type weights \(u(x)\) are strictly positive, and \(S\) is fixed and finite as \(k\to\infty\). The normalizations \(\mathbb E u=1\), \(\kappa=u\otimes u/\alpha\), and \(r=e-k+1\) are essential. The enumerator is explicitly
\[
\mathsf C_t(k,r)=\sum_{\substack{H\ \mathrm{connected\ simple}\ 
\mathrm{on}\ [k],\ |E(H)|=k+r-1}}
\mathbb E\!\left[
 t^{|E(H)|}\exp\!\left(-t\sum_{v=1}^k\frac{u(X_v)}\alpha\right)
 \prod_{\{i,j\}\in E(H)}\frac{u(X_i)u(X_j)}\alpha
\right],
\]
where \(X_1,\ldots,X_k\) are independent of law \(\mu\). This matches the source's weight convention by its gauge identity (4.42). For each fixed \(r\), the index \(k\) is sufficiently large that connected simple graphs with surplus \(r\) exist. The parameter \(t=1+s k^{-1/3}\) is positive for all sufficiently large \(k\) when \(s\) stays bounded.

## Proof

**1. Scalar critical-pair reduction.** Set \(F_j(z)=\mathbb E_\mu[u^j e^{zu}]\) for \(j\ge1\). The source's rooted-tree equation, with its field \(g_t(x)=\log t-(t-1)u(x)/\alpha\), is
\[
\tau(x)=\rho t\exp\!\left(-\frac{t}{\alpha}u(x)+(K\tau)(x)\right).
\]
Because \(K\tau(x)=u(x)m\) where \(m=\alpha^{-1}\mathbb E[u\tau]\), put \(z=m-t/\alpha\). Then
\[
\tau(x)=\rho t e^{zu(x)},\quad
m=\frac{\rho t}{\alpha}F_1(z).
\]
At the critical pair, the Perron eigenvalue of the positive rank-one derivative operator \(M_\tau K\) is one, equivalently \(\rho t F_2(z)/\alpha=1\). Eliminating \(m\) and \(\rho\) gives the **exact analytic parameterization**
\[
\boxed{t=\alpha\left(\frac{F_1(z)}{F_2(z)}-z\right),\qquad
\rho(t)=\frac{\alpha}{tF_2(z)}.}
\]
At \(z=0\), \(t=\rho=1\), and direct differentiation gives \(dt/dz=-\beta/\alpha\ne0\). Therefore the analytic inverse \(z=z(t)\) exists near one. This pair is the source's locally unique positive critical pair.

**2. Third-order coefficient.** Write \(\delta=\mathbb E u^5\). Expand
\[
F_1(z)=1+\alpha z+\frac\beta2z^2+\frac\gamma6z^3+O(z^4),\quad
F_2(z)=\alpha+\beta z+\frac\gamma2z^2+\frac\delta6z^3+O(z^4).
\]
Series inversion yields, for \(\varepsilon=t-1\),
\[
z=-\frac\alpha\beta\varepsilon
-\frac{\alpha(\alpha^2\beta+\alpha\gamma-2\beta^2)}{2\beta^3}\varepsilon^2+O(\varepsilon^3).
\]
Substitute the analytic inverse, through its third coefficient, into \(\log\rho=\log\alpha-\log t-\log F_2(z)\). The fifth-moment terms cancel, giving exactly
\[
\log\rho(1+\varepsilon)
=\frac{\alpha^2}{2\beta}\varepsilon^2
+\frac{\alpha^2(3\alpha^2\beta+\alpha\gamma-6\beta^2)}{6\beta^3}\varepsilon^3+O(\varepsilon^4).
\]
The cancellation and symbolic series reversion are checked independently by the accompanying \(\texttt{verify.py}\). This is an identity of analytic functions near \(t=1\), not a numerical extrapolation.

**3. Connected-weight moderate-tilt law.** The full shrinking-neighborhood estimate in Hu--Sun Theorem 3.6, equation (3.13), gives, for every fixed surplus \(r\),
\[
\frac{\mathsf C_t(k,r)}{\mathsf C_1(k,r)}=\rho(t)^{-k}\bigl(1+O_r(\eta_k+k^{-1/2})\bigr)
\]
uniformly for \(|t-1|\le\eta_k\), for any \(\eta_k\downarrow0\). Put \(t=1+s k^{-1/3}\) and \(\eta_k=(1+\sup|s|)k^{-1/3}\). Then
\[
k\log\rho(t)=\frac{\alpha^2}{2\beta}s^2 k^{1/3}+\mathfrak c_3s^3+O(k^{-1/3}),
\]
with uniform remainder on each compact \(s\)-range. Exponentiation proves the displayed limit. The sharp enumeration theorem is cited as an input; it is not reproved here.

**4. Reentrant sign.** For the two-point family, its two masses sum to one and its mean equals one by direct calculation. Exact rational expansion gives
\[
3\alpha^2\beta+\alpha\gamma-6\beta^2=-2Q(a).
\]
Since \(\alpha,\beta>0\), the cubic sign is \(-\mathrm{sgn}(Q(a))\). Further,
\[
Q''(a)=156000a^2-1951260a+1019100>0\quad(0\le a\le1/2),
\]
where the left side is decreasing on that interval and has value \(82470\) at \(a=1/2\). For \(1/2\le a\le1\),
\[
Q'(a)=a(52000a^2-975630a+1019100)-2860>0,
\]
since the parenthesis decreases on that interval and is at least \(95470\). Hence \(Q\) first decreases and then increases on \((0,1)\). Finally \(Q(0)=1\), \(Q(1/1000)<0\), and \(Q(1/100)>0\). There are exactly two simple roots in \((0,1)\), with the announced sign pattern and rational root brackets. At \(a=1/200\), substitution gives the stated positive rational \(\mathfrak c_3\). The one-type computation uses \(\rho(t)=e^{t-1}/t\), and gives \(-1/3\).

## Verification

Run \(\texttt{python verify.py}\) after installing the single optional symbolic dependency listed in \(\texttt{requirements.txt}\). The verifier checks formal rational-function series reversion, the exact fourth-moment coefficient, the two-type quartic identity, rational sign barriers, root isolation and derivative bounds, exact example fractions, and a weighted Cayley tree identity by exhaustive labelled trees at small sizes. It also checks the homogeneous critical-radius formula. It does **not** independently prove the source's uniform Perron--Wright asymptotic or establish novelty; those require the analytic source and literature comparison.

## Relationship to prior work

Hu and Sun (2026), Theorem 3.6, establish the analytic radius, the quadratic coefficient \(\alpha^2/(2\beta)\), and a uniform full-radius enumerator estimate for shrinking tilts. Their proof supplies the critical-pair equation and the gauge \(g_t\). These results imply that some cubic coefficient exists and make the moderate-tilt transfer possible, but the examined theorem and proof leave that coefficient inside an \(O(|t-1|^3)\) remainder. The new part here is the **explicit rank-one cubic formula and its rigorously classified reentrant sign**, together with the resulting explicit skew factor in the \(k^{-1/3}\) enumerator regime. The rank-one critical-graph scaling limits of Bhamidi, Sen and Wang (2014) and the general phase-transition framework of Bollobás, Janson and Riordan (2007) do not directly specify this finite-component enumerator coefficient. No claim is made that the general Perron--Wright theorem or its uniform estimate is newly proved here.

## Limitations

The analytic statement is confined to fixed finite strictly positive rank-one kernels, fixed surplus, and local tilts. It is not a theorem for arbitrary finite-rank or countably supported kernels; it does not provide an independent remainder estimate for random-graph component counts after finite-population corrections. The fourth-moment term is part of a coefficient, not a full distributional skewness theorem. Prior-art searches cannot exclude an equivalent formula in a different saddlepoint or weighted-tree notation. Independent mathematical audit has not been performed.

## References

1. W. Hu and W. Sun, *Perron--Wright asymptotics and critical component processes for regular inhomogeneous random graphs*, arXiv:2610.23003v1 (first public version October 16, 2026), particularly Theorem 3.6, equations (3.12)--(3.13), and Sections 4.1 and 4.4. https://arxiv.org/abs/2610.23003
2. S. Bhamidi, S. Sen and X. Wang, *Continuum limit of critical inhomogeneous random graphs*, arXiv:1404.4118 (2014). https://arxiv.org/abs/1404.4118
3. B. Bollobás, S. Janson and O. Riordan, *The phase transition in inhomogeneous random graphs*, Random Structures & Algorithms 31 (2007), 3--122. https://doi.org/10.1002/rsa.20168
