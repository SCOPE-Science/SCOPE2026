# A sharp endpoint-activation threshold for one noisy integrated-Wiener sensor

## Finding
Let \(W\) be standard Brownian motion on \([0,1]\), and let \(X(s)=\int_0^s W(u)\,du\). For any fixed measurement-noise variance \(\eta>0\), choose one observation time \(t\in[0,1]\), observe \(Y_t=X(t)+\varepsilon\), where \(\varepsilon\sim N(0,\eta)\) is independent of \(W\), and minimize the integrated posterior path uncertainty
\[
R_\eta(t)=\int_0^1\operatorname{Var}(X(s)\mid Y_t)\,ds.
\]
There is a **unique global minimizer** \(t_\eta\). Its support undergoes an exact endpoint transition at
\[
\boxed{\eta_c=\frac8{273}}.
\]
For \(0<\eta<\eta_c\), the minimizer lies strictly inside the interval, is strictly increasing in \(\eta\), and is the unique \(t\in(t_0,1)\) satisfying
\[
\eta=-\frac{t^3(8t^3-105t^2+210t-105)}{21(2t^3-30t^2+75t-60)},
\]
where \(t_0\) is the unique root of \(8t^3-105t^2+210t-105=0\) in \((2/3,1)\), numerically \(t_0=0.80181805349\ldots\). For **every** \(\eta\ge8/273\), the unique minimizer is exactly \(t_\eta=1\). Approaching the boundary from below,
\[
1-t_\eta=\frac{1183}{264}(\eta_c-\eta)+O((\eta_c-\eta)^2).
\]

## Assumptions and scope
The horizon is the fixed interval \([0,1]\), with process covariance normalized by \(\operatorname{Var}(W(1))=1\). The latent path is continuously observed *only in the loss*, not in the data: precisely one scalar observation is allowed, at a deterministic freely chosen time. Noise is independent centered Gaussian with known strictly positive variance \(\eta\). The risk is integrated conditional variance, equivalently mean integrated squared error of the Gaussian posterior mean; it is *not* endpoint-only prediction error, a path-integral estimation loss, or an adaptive design. All assertions above hold for every real \(\eta>0\).

## Proof
**1. Covariance and risk reduction.** Using \(X(t)=\int_0^t(t-u)\,dW(u)\), for \(0\le s\le t\le1\),
\[
K(s,t)=\operatorname{Cov}(X(s),X(t))
=\int_0^s(s-u)(t-u)\,du=\frac{s^2(3t-s)}6.
\]
By symmetry, when \(s\ge t\), \(K(s,t)=t^2(3s-t)/6\). In particular \(K(t,t)=t^3/3\) and \(\int_0^1K(s,s)\,ds=1/12\). Gaussian conditioning on the one observation yields
\[
R_\eta(t)=\frac1{12}-\frac{C(t)}{\eta+t^3/3},\qquad
C(t)=\int_0^1K(s,t)^2\,ds
=\frac{t^4(105-105t+35t^2-2t^3)}{1260}.
\]
Thus minimizing risk is precisely maximizing \(F_\eta(t)=C(t)/(\eta+t^3/3)\), a continuous nonnegative function on \([0,1]\), strictly positive for every \(t>0\); hence \(t=0\) is never optimal.

**2. The stationary-noise function.** Put
\[
H(t)=2t^3-30t^2+75t-60,\quad
U(t)=8t^3-105t^2+210t-105,
\]
\[
J(t)=2t^3-35t^2+105t-105,\quad
G(t)=4t^3-45t^2+75t-30.
\]
Direct differentiation gives \(C'(t)=-t^3H(t)/180\). On \([0,1]\), \(H'(t)=6t^2-60t+75\ge21>0\) and \(H(1)=-13\), so \(H<0\) and \(C'(t)>0\) for \(t>0\). Define
\[
E(t)=\frac{C(t)(t^2)}{C'(t)}-\frac{t^3}{3}
=-\frac{t^3U(t)}{21H(t)}\qquad (0<t\le1).
\]
Then
\[
F_\eta'(t)=\frac{C'(t)(\eta-E(t))}{(\eta+t^3/3)^2}.
\]
The cubic \(U\) is strictly increasing on \([0,1]\), because \(U'(t)=24t^2-210t+210\ge24>0\). Also \(U(2/3)<0\) and \(U(1)=8>0\). Hence it has exactly one zero \(t_0\in(2/3,1)\), with \(E(t)\le0\) for \(0<t\le t_0\) and \(E(t)>0\) for \(t>t_0\).

**3. Strict increase of \(E\) and the global classification.** Another exact differentiation yields
\[
E'(t)=-\frac{2t^2J(t)G(t)}{7H(t)^2}.
\]
The polynomial \(J\) is strictly increasing on \([0,1]\) since \(J'(t)=6t^2-70t+105\ge41>0\), and \(J(1)=-33\); consequently \(J<0\). For \(t\in[t_0,1]\subset(2/3,1]\),
\[
G(t)=4t^3+15(1-t)(3t-2)>0.
\]
Therefore \(E'(t)>0\) throughout \([t_0,1]\). At the right endpoint,
\[
E(1)=\frac8{273},\qquad E'(1)=\frac{264}{1183}>0.
\]
If \(0<\eta<E(1)\), the equation \(E(t)=\eta\) has exactly one solution \(t_\eta\in(t_0,1)\). The derivative \(F_\eta'\) is strictly positive before that solution and strictly negative afterward, making it the unique global maximizer. If \(\eta\ge E(1)\), then \(F_\eta'(t)>0\) for every \(0<t<1\), so \(t=1\) is uniquely optimal. Strict monotonicity of \(E\) also proves strict monotonicity of \(t_\eta\) below the threshold. Finally, the inverse-function theorem at \(E(1)=\eta_c\) gives \(1-t_\eta=(\eta_c-\eta)/E'(1)+O((\eta_c-\eta)^2)\), exactly the stated boundary law.

## Verification
The companion `check.py` independently reconstructs the covariance-square integral, derivative factorization, stationary-noise equation, strict-positivity identity, endpoint threshold, and boundary slope using exact symbolic rational arithmetic with SymPy. It also gives illustrative approximate stationary points for \(\eta=1/1000\) and \(\eta=1/100\). The global quantifiers follow from the sign proof above, not from sampling or numerical root finding. Reproduce with `python check.py` in an environment with SymPy installed.

## Relationship to prior work
Ji and Müller (first public preprint 18 April 2016) formulate integrated posterior-variance trajectory-recovery design for noisy observations of general processes. Their displayed general criterion requires solving a model-specific global optimization and does not furnish the above integrated-Wiener critical variance, root classification or boundary slope. Abundo (23 July 2013) studies integrated Gauss–Markov processes and records the variance \(t^3/3\) for integrated Brownian motion; the paper addresses representation and first-passage questions, not the single-sensor global placement optimization here. Earlier path-estimation work by Mukherjee studies exact designs for product-form covariances, especially ordinary Brownian motion, Brownian bridges and Ornstein–Uhlenbeck processes. An integrated-Wiener covariance is not of product form in ordered arguments; the dissertation full text was not accessible for a decisive all-appendix novelty comparison. These broad sources establish the framework but are not asserted to prove the phase law.

## Limitations
This is an exact benchmark for one point measurement with fixed known covariance and homoscedastic additive noise; it does not cover multiple sensors, sequential adaptive sampling, different path losses, unknown parameters, or higher-order integrated-Wiener processes. The result is analytically self-contained but has not undergone independent mathematical review. Publication priority is not established exhaustively: an inaccessible dissertation and unindexed specialized design literature may contain equivalent statements. In particular, absence of a search result is not a proof of originality.

## References
1. H. Ji and H.-G. Müller, *Optimal Designs for Longitudinal and Functional Data*, arXiv:1604.05375, first posted 2016-04-18, https://arxiv.org/abs/1604.05375; available author manuscript https://anson.ucdavis.edu/~mueller/f-optdes23.pdf.
2. M. Abundo, *On the representation of an integrated Gauss–Markov process*, arXiv:1307.5970, first posted 2013-07-23, https://arxiv.org/abs/1307.5970.
3. B. Mukherjee, *Optimal designs for estimating the path of a stochastic process*, Purdue University dissertation, catalog https://docs.lib.purdue.edu/dissertations/AAI3043760/; full text not inspected.
