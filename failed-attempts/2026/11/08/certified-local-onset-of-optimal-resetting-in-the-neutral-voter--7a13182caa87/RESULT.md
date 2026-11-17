# Certified local onset of optimal resetting in the neutral voter diffusion

## Finding

Consider the neutral complete-graph voter model in its diffusion scaling, with state \(X_t\in[0,1]\), infinitesimal generator
\[
\mathcal L f(x)=x(1-x)f''(x),
\]
and absorption at \(0\) or \(1\). Starting at \(x\in(0,1)\), independently reset the process to that same \(x\) at Poisson rate \(\lambda\ge 0\), stopping the process at first absorption. Write \(M_x(\lambda)\) for the mean absorption time with resetting.

**Theorem (a certified local onset and coefficient).** Define \(H(x)=-x\log x-(1-x)\log(1-x)\), \(V(x)=\mathbb E_x T^2\), \(W(x)=\mathbb E_x T^3\) for the absorption time \(T\) without resetting, and
\[
c_1(x)=H(x)^2-\tfrac12V(x),\qquad
c_2(x)=H(x)^3-H(x)V(x)+\tfrac16W(x).
\]
There is exactly one \(x_c\in(0.8152,0.8154)\) satisfying \(c_1(x_c)=0\). Its derivative satisfies \(c_1'(x_c)<0\) and \(c_2(x_c)>0\). Consequently, for every \(m>m_c:=2x_c-1\) sufficiently close to \(m_c\), \(M_{(1+m)/2}(\lambda)\) has a unique strict local minimum at a positive rate \(\lambda_{\mathrm{loc}}(m)\) in a fixed neighborhood of zero, and
\[
\lambda_{\mathrm{loc}}(m)
=K(m-m_c)+O((m-m_c)^2),\qquad
K=-\frac{c_1'(x_c)}{4c_2(x_c)}>0.
\]
The symmetric onset near \(m=-m_c\) follows by replacing \(x\) by \(1-x\). Numerical evaluation (not required for the proof) gives
\[
x_c=0.8152986253902179148\ldots,\quad
m_c=0.6305972507804358297\ldots,\quad
K=34.38629374451234\ldots.
\]
This is a **local** minimum/onset statement; it does not assert global optimality at arbitrary rates or uniqueness of every possible zero of \(c_1\) outside the certified interval.

More generally the entire reset-time mean has the exact special-function representation
\[
M_x(\lambda)=\frac{1-F(x,\lambda)}{\lambda F(x,\lambda)},\quad \lambda>0,
\]
where, writing \(a=(1+\sqrt{1-4\lambda})/2\) and \(b=(1-\sqrt{1-4\lambda})/2\),
\[
F(x,\lambda)=\Gamma(2-a)\Gamma(2-b)
\left[x\,{}_2F_1(a,b;2;x)+(1-x)\,{}_2F_1(a,b;2;1-x)\right].
\]
For \(\lambda>1/4\) use the conjugate pair \(a,b\); the expression remains real. The value at zero is the continuous limit \(M_x(0)=H(x)\).

## Assumptions and scope

The original finite process has \(N\ge2\) agents in a complete graph. One uniformly chosen agent copies one other uniformly chosen agent at each microscopic step. Writing \(x=j/N\) for the fraction holding a specified opinion, a one-step change is \(\pm1/N\) with probability \(j(N-j)/(N(N-1))\) each. The diffusion generator above is obtained when \(N\to\infty\) and time is measured in microscopic steps divided by \(N^2\). A Poisson reset rate \(\lambda\) on this diffusion scale corresponds formally to a per-step reset probability of order \(\lambda/N^2\). The theorem is proved for the diffusion process itself; it does **not** exchange the limits \(N\to\infty\) and optimization over finite-population reset probabilities.

The two endpoint states are absorbing for the first-passage calculation. Reset events have zero time overhead. Every reset returns to the *original* fraction \(x\), rather than a fresh independent fraction.

## Proof

**1. Exact no-reset transform.** For \(T=\inf\{t\ge0:X_t\in\{0,1\}\}\), \(F(x,\lambda)=\mathbb E_x e^{-\lambda T}\) is the unique bounded solution of
\[
x(1-x)F_{xx}=\lambda F,\qquad F(0,\lambda)=F(1,\lambda)=1.
\]
Substituting \(x\,{}_2F_1(a,b;2;x)\), where \(a+b=1\) and \(ab=\lambda\), into this equation gives one fundamental solution vanishing at zero. Reflection about \(1/2\) gives the complementary solution vanishing at one. Gauss's endpoint evaluation \({}_2F_1(a,b;2;1)=1/[\Gamma(2-a)\Gamma(2-b)]\) fixes the coefficients and yields the displayed formula. The boundary-value uniqueness follows from the maximum principle for \(\lambda>0\). In particular \(0<F(x,\lambda)<1\) for interior \(x\) and positive \(\lambda\).

**2. Restart identity.** A Poisson reset either interrupts an attempt before absorption or the attempt finishes first. The renewal equation gives the classical exact identity
\[
M_x(\lambda)=\frac{1-F(x,\lambda)}{\lambda F(x,\lambda)}.
\]
Because absorption in this bounded diffusion has exponentially decaying survival tails, its moments are finite and the identity has an analytic expansion near \(\lambda=0\). Expanding \(F=1-\lambda H+\lambda^2 V/2-\lambda^3 W/6+O(\lambda^4)\) yields
\[
M_x(\lambda)=H(x)+c_1(x)\lambda+c_2(x)\lambda^2+O(\lambda^3).
\]

**3. Exact moments.** Put \(U_k(x)=\mathbb E_x[T^k]\) with \(U_0=1\). The backward recursion and zero boundary conditions are
\[
U_k''(x)=-\frac{kU_{k-1}(x)}{x(1-x)},\qquad U_k(0)=U_k(1)=0.
\]
The first two solutions are \(U_1=H\) and
\[
V(x)=\frac{\pi^2}{3}-2\left[(1-x)\operatorname{Li}_2(1-x)+x\operatorname{Li}_2(x)+H(x)\right].
\]
The third has a positive Green representation
\[
W(x)=3\left[(1-x)\int_0^x\frac{V(y)}{1-y}\,dy+x\int_x^1\frac{V(y)}{y}\,dy\right].
\]
All three are symmetric about \(1/2\), strictly positive in the interior, and strictly concave there; thus they decrease on \((1/2,1)\). Direct differentiation gives
\[
c_1'(x)=2H(x)\log\frac{1-x}{x}+\operatorname{Li}_2(x)-\operatorname{Li}_2(1-x).
\]

**4. Rigorous transversality and curvature.** Let \(A=1019/1250=0.8152\) and \(B=4077/5000=0.8154\). The exact-rational interval checker `certificate.py` encloses logarithms by the positive/negative atanh series, the dilogarithm by its positive power series and Euler's reflection identity, and \(\pi\) by a bounded alternating Machin arctangent series. The resulting rational bounds establish
\[
c_1(A)>0,\qquad c_1(B)<0,\qquad
\sup_{x\in[A,B]}c_1'(x)<-0.5074.
\]
Therefore precisely one transverse root \(x_c\) lies in \((A,B)\). Concavity and symmetry of \(W\) imply \(W(x_c)\ge W(B)\). Concavity of \(V\) makes each endpoint minimum a lower bound across its grid cell; applying this on 128 equal subintervals to the positive Green integral (with a split at \(B\)) gives the certified rational inequalities
\[
W(B)>0.6640,\qquad 6H(A)^3<0.6578.
\]
At the root, \(V(x_c)=2H(x_c)^2\). Since \(H\) decreases beyond \(1/2\),
\[
6c_2(x_c)=W(x_c)-6H(x_c)^3
\ge W(B)-6H(A)^3>0.
\]
The checker prints the actual tighter rational bounds. Its sole arithmetic consists of exact fractions; the printed decimals merely display these enclosures.

**5. Local onset.** Define \(G(x,\lambda)=\partial_\lambda M_x(\lambda)\), analytically continued around \(\lambda=0\). The established inequalities give \(G(x_c,0)=0\), \(\partial_xG(x_c,0)=c_1'(x_c)<0\), and \(\partial_\lambda G(x_c,0)=2c_2(x_c)>0\). The analytic implicit-function theorem supplies a unique analytic zero \(\lambda_*(x)\) near \((x_c,0)\), with derivative \(-c_1'(x_c)/(2c_2(x_c))>0\). For \(x>x_c\) sufficiently close, this zero is positive and \(\partial_\lambda^2M_x(\lambda_*(x))>0\), proving the unique strict *local* minimum in that neighborhood. Replacing \(x=(1+m)/2\) yields the claimed coefficient \(K\).

## Verification

Run `python certificate.py` with Python 3's standard library. It tests the two signed moment boundaries, a uniform negative bound on the derivative throughout the bracket, and a strict positive lower bound for the second-order coefficient at the unique root. No floating-point quantity is used to establish the inequalities.

Optionally run `python numerical_check.py` with `mpmath` installed. It evaluates the root, the integral for the third moment, the asymptotic slope, and positive-rate local minima near the critical point, and checks the hypergeometric differential equation numerically. These computations illustrate, but do not replace, the rational sign certificate or analytic proof.

## Relationship to prior work

Argany Herrera, Alvarez-Zuzek and Artime (2026) formulated exogenous shocks in voter models and found a numerical critical magnetization around \(0.630\) with a near-linear onset of advantageous resetting; they explicitly left an analytical derivation of this scaling open. Their complete-graph first-passage process motivates the diffusion limit considered here. The general renewal formula and the universal *possibility* of linear vanishing for resetting optima were already developed by Ahmad, Nayak, Bansal, Nandi and Das (2019); neither the renewal identity nor universal exponent one is claimed as a new principle. Tran, Hofrichter and Jost (2012) treated the underlying neutral Wright–Fisher diffusion without resetting. The contribution assessed here is the special-function response and the certified, nondegenerate *model-specific* critical point and local coefficient for this voter first-passage problem.

## Limitations

The theorem concerns local optimality in the diffusion limit, not a global minimizer for every parameter, and it proves uniqueness of the onset root only within the stated rational interval. No claim is made about arbitrary networks, nonequilibrium stationary laws after consensus, nonzero reset overhead, directed or state-dependent resets, or finite-population corrections. The numerical values are approximations to rigorously specified constants. Independent validation has not been performed.

## References

- G. Argany Herrera, L. G. Alvarez-Zuzek and O. Artime, *Opinion dynamics under large-scale exogenous events* (2026), arXiv:2609.39858, first submitted 2026-09-30, https://arxiv.org/html/2609.39858 .
- S. Ahmad, I. Nayak, A. Bansal, A. Nandi and D. Das, *First passage of a particle in a potential under stochastic resetting: a vanishing transition of optimal resetting rate*, Physical Review E **99**, 022130 (2019), arXiv:1902.02955, https://arxiv.org/abs/1902.02955 .
- T. D. Tran, J. Hofrichter and J. Jost, *An introduction to the mathematical structure of the Wright–Fisher model of population genetics*, Theory in Biosciences **132**, 73–82 (2013), first published online 2012-12-14, https://doi.org/10.1007/s12064-012-0170-3 .
