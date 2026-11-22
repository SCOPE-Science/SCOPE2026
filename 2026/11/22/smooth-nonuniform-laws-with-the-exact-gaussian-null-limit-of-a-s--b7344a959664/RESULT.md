# Smooth nonuniform laws with the exact Gaussian null limit of a scalar uniformity test

## Finding

Consider the complete-data scalar uniformity test of Kattumannil and Sreedevi (2021), subsequently published by Sreedevi and Kattumannil (2023). Its symmetric pair kernel is
\[
k(x,y)=\max(x,y)-x-y+\tfrac12(x^2+y^2),\qquad 0\le x,y\le1,
\]
and its statistic on \(n\ge2\) independent observations is
\[
\widehat\Delta_n=\binom n2^{-1}\sum_{1\le i<j\le n}k(X_i,X_j).
\]
**Theorem.** There exists \(\epsilon>0\) and real-analytic functions \(a,b:(-\epsilon,\epsilon)\to\mathbb R\) with \(a(0)=b(0)=0\) such that, for every fixed \(0<|c|<\epsilon\), the polynomial
\[
F_c(x)=x+cH(x)+a(c)G_1(x)+b(c)G_3(x),\quad 0\le x\le1,
\]
with
\[
H(x)=x(1-x),\qquad G_1(x)=x(1-x)(1-2x),\qquad G_3(x)=x(1-x)(1-2x)^3,
\]
is a strictly increasing CDF with a strictly positive real-analytic density, is not uniform, and nevertheless obeys
\[
\mathbb E_{F_c}k(X_1,X_2)=0,\qquad
\sqrt n\,\widehat\Delta_n\ \xrightarrow{\mathcal D}\ N(0,1/45).
\]
The very same Gaussian limit holds under the uniform null. Therefore, at **every** fixed \(\alpha\in(0,1)\), the original two-sided test using the asymptotic normal cutoff \(z_{1-\alpha/2}/\sqrt{45n}\) has rejection probability tending to \(\alpha\) under each of these fixed nonuniform alternatives, not to one. Meanwhile,
\[
\sup_{0\le x\le1}|F_c(x)-x|\ge |c|/4>0,
\]
so a Kolmogorov–Smirnov test distinguishes each alternative consistently. The unique local analytic coefficients have expansions
\[
a(c)=\frac{29}{112}c^2+O(c^3),\qquad b(c)=\frac9{16}c^2+O(c^3).
\]
This result is an *existence theorem* for all sufficiently small fixed nonzero \(c\), not a claim of equality of finite-sample statistic distributions.

## Assumptions and scope

Samples are iid from the stated fixed law on \([0,1]\), have no censoring or estimated nuisance parameters, and \(n\to\infty\). The Gaussian asymptotic normality is for the **unstudentized** complete-data pair U-statistic with the fixed null normalization \(\sqrt{45n}\). The coefficient \(\epsilon\) is positive but not given a numerical optimal value. The functions \(a(c),b(c)\) are characterized locally by two explicit polynomial-integral equations and are not represented by decimal approximations.

## Proof

**1. Population contrast.** For a continuous CDF \(F\) on \([0,1]\) with endpoints \(0,1\), the standard tail-integral identities give
\[
\begin{split}
\Delta(F)&=\mathbb E\max(X_1,X_2)-2\mathbb EX+\mathbb EX^2\\
&=\int_0^1\left(2(1-x)F(x)-F(x)^2\right)\,dx.
\end{split}
\]
Put \(F_{a,b,c}(x)=x+aG_1(x)+bG_3(x)+cH(x)\). Then \(D(a,b,c)=\Delta(F_{a,b,c})\) is polynomial in the parameters, and direct integration yields
\[
D(0,0,0)=0,\quad (D_a,D_b,D_c)(0,0,0)=(1/15,1/35,0),\quad
D(0,0,c)=-c^2/30.
\]

**2. Exact projected variance.** Define
\[
v_F(x)=2xF(x)+2\int_x^1 t\,dF(t)-2x+x^2,
\qquad V(F)=\operatorname{Var}_{X\sim F}(v_F(X)).
\]
The bounded symmetric-kernel U-statistic central limit theorem gives asymptotic variance \(V(F)\), since \(v_F\) differs from twice the first Hoeffding projection by a constant. For the polynomial family, integration by parts yields the equivalent identity
\[
v_F(x)=1+2x^2-2x-2\int_x^1(F(t)-t)\,dt.
\]
Consequently \(V(a,b,c)=V(F_{a,b,c})\) is a polynomial in \((a,b,c)\). At the uniform law, \(v_0(x)=1+2x^2-2x\) and \(V(0,0,0)=1/45\).

For an infinitesimal CDF perturbation \(F(x)=x+\eta g(x)\), with \(g(0)=g(1)=0\), differentiation of the exact variance at \(\eta=0\) gives
\[
\left.\frac{d}{d\eta}V(x+\eta g)\right|_{\eta=0}
=\int_0^1w(x)g(x)\,dx,
\quad w(x)=-\frac43(2x-1)(7x^2-7x+1).
\]
This follows by writing \(q(x)=v_0(x)-\mathbb E_{U}v_0(U)=2x^2-2x+1/3\), differentiating \(\operatorname{Var}_{F}(v_F(X))\) in its density and projection terms, then using
\[
w(x)=-\frac{d}{dx}q(x)^2-4\int_0^x q(t)\,dt.
\]
Integrating against the three displayed polynomial directions gives
\[
(V_a,V_b,V_c)(0,0,0)=(0,4/945,0),\quad
V(0,0,c)=\frac1{45}-\frac{c^2}{420}-\frac{c^4}{225}.
\]

**3. Two simultaneous exact cancellations.** Consider the analytic map
\[
\mathcal G(a,b,c)=\big(D(a,b,c),\ V(a,b,c)-1/45\big).
\]
The Jacobian in \((a,b)\) at the origin is
\[
\begin{pmatrix}1/15&1/35\\0&4/945\end{pmatrix},
\qquad\det=4/14175>0.
\]
The real-analytic implicit-function theorem supplies \(\epsilon>0\) and unique analytic solutions \(a(c),b(c)\) near \(0\) for which \(D=0\) and \(V=1/45\). First differentiation gives \(a'(0)=b'(0)=0\). Substitution into the two equations at order \(c^2\) gives
\[
\frac{a_2}{15}+\frac{b_2}{35}=\frac1{30},
\qquad \frac4{945}b_2=\frac1{420},
\]
so \(a_2=29/112\) and \(b_2=9/16\), as claimed.

**4. Genuine, smooth alternatives and test power.** Each polynomial has the correct endpoint values. Since its derivative converges uniformly to one as \(c\to0\), it is a strictly increasing CDF with positive polynomial density for sufficiently small \(|c|\). The identities \(G_1(1/2)=G_3(1/2)=0\) and \(H(1/2)=1/4\) show \(F_c(1/2)=1/2+c/4\), proving strict nonuniformity and the Kolmogorov-distance lower bound. Boundedness of the pair kernel and \(V(F_c)=1/45>0\) permit the ordinary nondegenerate U-statistic CLT:
\[
\sqrt n\big(\widehat\Delta_n-\Delta(F_c)\big)
\xrightarrow{\mathcal D}N(0,V(F_c)).
\]
With \(\Delta(F_c)=0\), continuity of the Gaussian distribution gives asymptotic rejection probability \(\alpha\) for the stated fixed null cutoff. For the uniform law the same calculation applies. The Kolmogorov distance bound and uniform convergence of the empirical CDF imply consistency of a KS test against each fixed \(F_c\).

## Verification

Run `python verify.py` in the same directory, after installing SymPy from `requirements.txt`. The script verifies using exact polynomial arithmetic: both endpoint conditions; midpoint nonuniformity; all partial derivatives of \(D\); exact \(D(0,0,c)\); the projected variance and its three derivatives (by an independent direct differentiation and the displayed weight calculation); exact \(V(0,0,c)\); the positive Jacobian; both quadratic coefficient equations; and the population-contrast integral identity. It performs no infinite-sample simulations and is not a substitute for the implicit-function theorem or U-statistic CLT invoked in the proof.

## Relationship to prior work

Kattumannil and Sreedevi (2021), revised as Sreedevi and Kattumannil (2023), provide the kernel, variance formula and null cutoff. Their scalar contrast results do not supply a nonuniform family matching **both** the departure mean and the first-order null variance; their numerical power study only examines several named alternatives. Ebner, Liebenberg and Visagie (2021) instead square and integrate the entire parameter-indexed characterization over \(t\), and prove omnibus consistency for that different statistic. The present obstruction applies only to the scalar, signed integration used in the first paper and does not contradict the integrated-square result. Classical Hoeffding theory and the analytic implicit-function theorem are used as standard tools, not presented as novel general methods.

## Limitations

The local analytic family is established without a sharp global allowable \(c\)-range. The asymptotic equality does not imply equality at finite sample sizes, failure of every test against these alternatives, or a statement about the censoring-adjusted procedure. The result does not establish a minimax lower bound. Source comparison cannot conclusively establish global historical priority; a similar construction could exist in unindexed literature.

## References

1. S. K. Kattumannil and E. P. Sreedevi, *A new goodness of fit test for uniform distribution with censored observations*, first posted 11 June 2021, arXiv:2106.06368. https://arxiv.org/abs/2106.06368
2. E. P. Sreedevi and S. K. Kattumannil, *Goodness of fit test for uniform distribution with censored observation*, Journal of the Korean Statistical Society 52 (2023), 382–394, published online 23 January 2023. https://doi.org/10.1007/s42952-023-00205-8 ; open full text https://pmc.ncbi.nlm.nih.gov/articles/PMC9869324/
3. B. Ebner, S. C. Liebenberg, and I. J. H. Visagie, *A new omnibus test of fit based on a characterisation of the uniform distribution*, arXiv:2108.06391 (first posted 13 August 2021). https://arxiv.org/abs/2108.06391
4. W. Hoeffding, *A class of statistics with asymptotically normal distribution*, Ann. Math. Statist. 19 (1948), 293–325. Classical U-statistic central limit theorem.
