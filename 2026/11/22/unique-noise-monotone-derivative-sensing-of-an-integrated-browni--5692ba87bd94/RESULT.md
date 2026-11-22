# Unique noise-monotone derivative sensing of an integrated Brownian bridge and its endpoint-design conflict

## Finding

Let \(B\) be a standard Brownian bridge on \([0,1]\), and let its integral be \(X(s)=\int_0^s B(u)\,du\). A single noisy derivative sensor can observe \(Y_t=X'(t)+\varepsilon=B(t)+\varepsilon\), where \(\varepsilon\) is independent centered Gaussian noise with variance \(\eta>0\) and \(t\in[0,1]\) is freely chosen. We distinguish integrated posterior **trajectory** risk
\[
R_\eta(t)=\int_0^1\operatorname{Var}(X(s)\mid Y_t)\,ds
\]
from the posterior **terminal-area** risk \(Q_\eta(t)=\operatorname{Var}(X(1)\mid Y_t)\).

Define \(\beta\) as the unique root in \((2/5,5/12)\) of
\[
f(t)=4t^3+9t^2-24t+8=0,
\]
and \(\alpha=\sqrt6-2\). Thus \(\beta\approx0.406490758540456\) and \(\alpha\approx0.449489742783178\). For **every** finite \(\eta>0\), the trajectory-risk minimizer is a **unique** time \(t_\eta\) satisfying
\[
\beta<t_\eta<\alpha<\tfrac12.
\]
It is the unique root in \((\beta,\alpha)\) of
\[
\eta\,A(t)+B_*(t)=0,\qquad
A(t)=2(4-3t)(t^2+4t-2),\quad
B_*(t)=t(t-1)(4t^3+9t^2-24t+8).
\]
The map \(\eta\mapsto t_\eta\) is strictly increasing, with sharp endpoint asymptotics
\[
 t_\eta=\beta-\frac{A(\beta)}{B_*'(\beta)}\eta+O(\eta^2)\quad(\eta\downarrow0),
\]
\[
 t_\eta=\alpha-\frac{B_*(\alpha)}{A'(\alpha)}\eta^{-1}+O(\eta^{-2})\quad(\eta\to\infty).
\]
Both displayed positive coefficients are well defined. In contrast, the *same* derivative sensor, with the *same* noise, uniquely minimizes terminal-area risk at \(t=1/2\) for every \(\eta>0\). In the high-noise limit, the ratio of trajectory variance reductions between the optimal path sensor and the midpoint sensor tends to
\[
\frac{112896-46080\sqrt6}{23}\approx1.022289241354488.
\]
This ratio concerns the variance reduction, not the ratio of total posterior risks.

## Assumptions and scope

The bridge is centered Gaussian with covariance \(k(u,v)=\min(u,v)-uv\), normalized to the unit interval, and is integrated once without additional drift or trend. The sensor measures its derivative \(X'(t)=B(t)\), **not** the integrated state \(X(t)\). The Gaussian noise variance \(\eta\) is constant across locations and strictly positive. The posterior risks are Bayes risks under the stated fully known Gaussian prior and observation model, not worst-case deterministic recovery errors. No assertion is made about multiple sensors, colored noise, other priors or arbitrary observation weights.

## Proof

**1. Exact covariance and objective.** For \(0\le s,t\le1\), integrate \(k(u,t)\) in \(u\) to obtain
\[
C(s,t)=\operatorname{Cov}(X(s),B(t))=
\begin{cases}
(1-t)s^2/2,&0\le s\le t,\\
t(s-s^2/2)-t^2/2,&t\le s\le1.
\end{cases}
\]
In particular, \(\operatorname{Var}(B(t))=t(1-t)\) and \(C(1,t)=t(1-t)/2\). Direct double integration gives \(\operatorname{Var}(X(s))=s^3/3-s^4/4\), hence the prior integrated risk is \(1/30\). Conditional Gaussian variance yields
\[
R_\eta(t)=\frac1{30}-\frac{F(t)}{\eta+t(1-t)},\qquad
F(t)=\int_0^1 C(s,t)^2\,ds
=\frac{t^2(1-t)^2(8-4t-t^2)}{60}.
\]
All denominators are strictly positive for \(\eta>0\). At either observation endpoint the derivative sensor returns no information, whereas interior observation has strictly positive gain.

**2. Global uniqueness.** Let \(G_\eta(t)=F(t)/(\eta+t(1-t))\); minimizing risk means maximizing \(G_\eta\). Exact differentiation gives
\[
G_\eta'(t)=\frac{t(t-1)[\eta A(t)+B_*(t)]}{60[\eta+t(1-t)]^2}.
\]
On \([0,1]\), the polynomial \(f(t)=4t^3+9t^2-24t+8\) has exactly one root \(\beta\): its derivative \(12t^2+18t-24\) changes from negative to positive at \((\sqrt{41}-3)/4\), while \(f(0)=8\), \(f(1)=-3\); the exact brackets \(f(2/5)=12/125>0\) and \(f(5/12)=-4/27<0\) isolate it. The function \(A(t)\) is strictly negative for \(t<\alpha\) and strictly positive for \(t>\alpha\). As \(t(t-1)<0\), \(B_*(t)<0\) on \((0,\beta)\) and \(B_*(t)>0\) on \((\beta,1)\). Thus \(G_\eta'>0\) to the left of \(\beta\) and \(G_\eta'<0\) to the right of \(\alpha\). In the intervening interval \((\beta,\alpha)\), both \(A'(t)>0\) (indeed \(A'(t)=44-32t-18t^2\)) and
\[
B_*'(t)=(2t-1)f(t)+t(t-1)f'(t)>0
\]
because \(2t-1<0\), \(f(t)<0\), \(t(t-1)<0\), and \(f'(t)<0\) there. Thus \(\eta A+B_*\) is strictly increasing on \((\beta,\alpha)\), is negative at \(\beta\), and is positive at \(\alpha\). It therefore has precisely one zero, where \(G_\eta'\) switches from positive to negative. This establishes a unique global minimizer of \(R_\eta\), for every \(\eta>0\).

**3. Monotonicity and limits.** At its root, implicit differentiation gives
\[
\frac{dt_\eta}{d\eta}=-\frac{A(t_\eta)}{\eta A'(t_\eta)+B_*'(t_\eta)}>0.
\]
The unique root tends to \(\beta\) as \(\eta\downarrow0\), and tends to the unique zero \(\alpha\) of \(A\) as \(\eta\to\infty\). Both roots are simple with \(B_*'(\beta)>0\) and \(A'(\alpha)>0\), so Taylor expansion of the scalar root equation gives the claimed first-order terms with the stated remainders.

**4. Endpoint design and strict conflict.** As \(C(1,t)=t(1-t)/2\), Gaussian conditioning gives
\[
Q_\eta(t)=\frac1{12}-\frac{[t(1-t)]^2}{4[\eta+t(1-t)]}.
\]
Writing \(u=t(1-t)\), the gain \(u^2/[4(\eta+u)]\) is strictly increasing in \(u>0\) because its derivative is \(u(2\eta+u)/[4(\eta+u)^2]\). The unique maximizer of \(u\) is \(t=1/2\), which lies strictly to the right of the path-optimal \(t_\eta\). Finally, taking \(\eta\to\infty\) in the path-gain formula yields \(F(\alpha)/F(1/2)=(112896-46080\sqrt6)/23\), strictly greater than one.

## Verification

Run the standalone `verify.py` with Python 3.10+ and SymPy 1.11+; no data files or external services are needed. The script recomputes the covariance integrals, derivative factorization, exact polynomial brackets, endpoint risk, asymptotic coefficient identities, and high-noise variance-reduction ratio. As a separate check, Simpson quadrature of the piecewise covariance at ten sampling locations independently reproduces the integrated covariance gain. A bisection-based scan over eight noise values confirms the predicted root interval and locally tests risk inequalities. The supplied script reports 87 successful checks in the reference environment. Global uniqueness and the all-noise claims follow from the analytic sign proof above; finite checks alone do not establish them.

## Relationship to prior work

Lachal (2011, arXiv:1108.2132v1) develops the covariance and prediction theory for Brownian iterated-integral bridges, including an integrated process pinned through terminal derivative data; the inspected paper does not optimize an interior noisy derivative-observation time. Šimák (2002) develops the integrated prediction-error update for derivative observations, mainly with stationary differentiable covariance kernels, and explicitly distinguishes comparison of derivative information from solved designs. Schober, Duvenaud and Hennig (2014, arXiv:1406.2582v1) use integrated Wiener priors and derivative evaluations in numerical ODE algorithms; they do not derive this bridge-specific noise-monotone path-versus-endpoint design separation. Ji and Müller (2016, arXiv:1604.05375v1) give a general integrated prediction error for noisy observations of the *same* process; the present sensor observes a derivative of the process being recovered. These frameworks justify the criterion but do not algebraically imply the stated unique optimizer or its location interval without new covariance analysis. A closely related historical path-design dissertation by Mukherjee has a catalog-accessible abstract but the full text was not inspected; publication priority remains subject to that and other unindexed literature.

## Limitations

No independent mathematical audit has been performed. Publication priority is provisional because some historically plausible full texts are inaccessible and indexed searches cannot prove a result absent. The model has a single sensor with known homogeneous noise and normalized Gaussian covariance. The path-design gain over the midpoint is strictly positive but quantitatively modest: approximately 2.23% at high noise in relative variance reduction, not 2.23% in posterior risk. The numerical checks are supplementary, not substitutes for the global proof.

## References

1. A. Lachal, *A class of bridges of iterated integrals of Brownian motion related to various boundary value problems involving the one-dimensional polyharmonic operator*, arXiv:1108.2132v1, first publicly submitted 10 August 2011, https://arxiv.org/abs/1108.2132.
2. J. Šimák, *On Experimental Designs for Derivative Random Fields*, TU Bergakademie Freiberg dissertation (2002), https://webdoc.sub.gwdg.de/ebook/diss/2003/tu-freiberg/archiv/html/MathematikSimakJaroslav459358.pdf.
3. M. Schober, D. Duvenaud and P. Hennig, *Probabilistic ODE Solvers with Runge-Kutta Means*, arXiv:1406.2582v1, first publicly submitted 10 June 2014, https://arxiv.org/abs/1406.2582.
4. H. Ji and H.-G. Müller, *Optimal Designs for Longitudinal and Functional Data*, arXiv:1604.05375v1, publicly submitted 18 April 2016, https://arxiv.org/abs/1604.05375.
5. B. Mukherjee, *Optimal designs for estimating the path of a stochastic process*, Purdue dissertation catalog, https://docs.lib.purdue.edu/dissertations/AAI3043760/ (abstract available; full text uninspected).
