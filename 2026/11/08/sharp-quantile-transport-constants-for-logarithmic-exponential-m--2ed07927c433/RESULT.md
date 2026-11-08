# Sharp quantile-transport constants for logarithmic exponential maxima

## Finding
Let \(E_1,E_2,\ldots\) be independent rate-one exponential variables and set
\[
Y_n=\log\!\left(\max_{1\le j\le n}E_j\right),\qquad n\ge1.
\]
Write \(F_n\) for the distribution function of \(Y_n\), \(Q_n=F_n^{-1}\) for its continuous quantile, and \(T_{n,m}=Q_m\circ F_n\) for the increasing quantile transport. For every pair of integers \(1\le n<m\), the transport is continuously differentiable and has the **sharp global slope bounds**
\[
\boxed{\frac nm<T_{n,m}'(y)<1\quad\text{for every }y\in\mathbb R,}
\]
with \(T_{n,m}'(y)\to n/m\) as \(y\to-\infty\), and \(T_{n,m}'(y)\to1\) as \(y\to+\infty\). Neither constant can be improved.

Equivalently, for every \(0<u<v<1\),
\[
\boxed{\frac nm\bigl(Q_n(v)-Q_n(u)\bigr)
 <Q_m(v)-Q_m(u)<Q_n(v)-Q_n(u).}
\]
Consequently the entire family decreases *strictly in dispersive order*. Under common uniform-quantile coupling, distances between independent copies contract pathwise by these two factors. In particular, for independent copies \(Y_n'\) and \(Y_m'\) of their respective laws and every \(p>0\),
\[
\left(\frac nm\right)^p\mathbb E|Y_n-Y_n'|^p
<\mathbb E|Y_m-Y_m'|^p
<\mathbb E|Y_n-Y_n'|^p.
\]
For \(p=2\),
\[
\boxed{\left(\frac nm\right)^2\operatorname{Var}(Y_n)
<\operatorname{Var}(Y_m)<\operatorname{Var}(Y_n).}
\]
The centered variables also satisfy \(Y_m-\mathbb EY_m\le_{\mathrm{cx}}Y_n-\mathbb EY_n\) in convex order, with distinct distributions.

## Assumptions and scope
The samples comprise independent, identically distributed \(\operatorname{Exp}(1)\) variables. All \(n,m\) are finite positive integers, with \(n<m\). Quantile bounds are pointwise over the entire open unit interval, and all moments displayed are finite. An arbitrary common exponential rate \(\lambda>0\) simply shifts each \(Y_n\) by \(-\log\lambda\), leaving these conclusions unchanged.

## Proof
For \(y\in\mathbb R\), independence gives \(F_n(y)=(1-\exp(-\exp y))^n\), and hence
\[
Q_n(u)=\log\!\bigl[-\log(1-u^{1/n})\bigr],\qquad 0<u<1.
\]
Fix \(u\in(0,1)\), put \(s=-\log u>0\), and define
\[
h(x)=\frac{x\exp(-x)}{(1-\exp(-x))[-\log(1-\exp(-x))]},\qquad x>0.
\]
Direct differentiation yields
\[
Q_n'(u)=\frac{h(s/n)}{us}.
\]
We establish the two properties \(h'(x)>0\) and \((h(x)/x)'<0\) for all \(x>0\). Put \(t=\exp(-x)\in(0,1)\), \(a=-\log(1-t)>0\). Then
\[
(1-t)\frac{h'(x)}{h(x)}
=\frac{1-t}{x}-1+\frac{t}{a}.
\]
The strict elementary logarithmic inequality \(\log z<z-1\) for \(z\ne1\) gives
\[
x=-\log t<\frac{1-t}{t},\qquad
a=-\log(1-t)<\frac{t}{1-t}.
\]
Thus \((1-t)/x>t\) and \(t/a>1-t\); their sum exceeds one, so \(h'(x)>0\). Also
\[
\frac{d}{dx}\log\frac{h(x)}x
=\frac{t/a-1}{1-t}<0,
\]
because \(a=-\log(1-t)>t\), another strict elementary logarithmic inequality. Both monotonicity assertions follow without numerical assumptions.

Now \(s/m<s/n\). The strict increase of \(h\) and strict decrease of \(h(x)/x\) imply
\[
\frac nm<\frac{h(s/m)}{h(s/n)}
=\frac{Q_m'(u)}{Q_n'(u)}<1.
\]
Since \(F_n(Q_n(u))=u\), the chain rule gives
\[
T_{n,m}'(Q_n(u))=\frac{Q_m'(u)}{Q_n'(u)}.
\]
This proves the pointwise transport bounds. Integrating \(Q_m'\) and \(Q_n'\) between arbitrary \(u<v\) proves the strict two-sided interquantile inequality.

To establish sharpness, as \(x\to+\infty\), \(-\log(1-e^{-x})\sim e^{-x}\), so \(h(x)\sim x\). As \(x\downarrow0\), \(1-e^{-x}\sim x\) and \(-\log(1-e^{-x})\sim\log(1/x)\), so \(h(x)\sim1/\log(1/x)\). Therefore, as \(u\downarrow0\), the derivative ratio tends to \(n/m\), while as \(u\uparrow1\), it tends to one. The corresponding \(Q_n(u)\) runs from \(-\infty\) to \(+\infty\), establishing the asserted sharp transport slopes.

For the pairwise statements, take independent \(U,V\sim\operatorname{Unif}(0,1)\) and couple each law as \(Q_j(U),Q_j(V)\), for \(j=n,m\). Almost surely \(U\ne V\); the interquantile inequalities imply, pointwise,
\[
\frac nm|Q_n(U)-Q_n(V)|
<|Q_m(U)-Q_m(V)|
<|Q_n(U)-Q_n(V)|.
\]
All moments exist: the left tail of \(Y_j\) decays exponentially, and its right tail decays superexponentially. Taking positive powers and expectations gives the claimed strict moment inequalities. The identity \(\operatorname{Var}(Y_j)=\tfrac12\mathbb E(Y_j-Y_j')^2\) yields the variance bounds.

Finally \(D(u)=Q_n(u)-Q_m(u)\) is strictly increasing, since \(Q_n'(u)>Q_m'(u)\). Write \(\bar D=\int_0^1D(u)\,du\). Every proper initial interval has mean \(D\) strictly less than \(\bar D\), so \(\int_0^v(D(u)-\bar D)\,du<0\) for \(0<v<1\). The integrated-quantile criterion for equal-mean convex order now implies \(Y_m-\mathbb EY_m\le_{\mathrm{cx}}Y_n-\mathbb EY_n\); strict inequalities make the laws distinct.

## Verification
Run \`python3 CHECK.py\` in the directory containing this file. This standard-library checker re-evaluates CDF inversion, the quantile derivative, finite meshes of the two-sided slope and interquantile inequalities, the logarithmic inequalities used in the proof, endpoint approaches and independent numerical quadrature of variances. In the packaged run it passed **9,264 finite numerical diagnostics**. Approximate variances for \(n=1,2,3,4,10\) were respectively \(1.644526317,0.683914582,0.448440664,0.343987229,0.171416227\) using midpoint quadrature. The exact first variance is \(\pi^2/6\); quadrature errors are numerical and are not used in the proof.

## Relationship to prior work
Doumas (2026, arXiv:2603.11129, Section 2) identifies \(\operatorname{Var}(Y_n)\) with the alternating-binomial coefficient governing the fixed-player asymptotic variance of the fastest of independent coupon collectors, and asks whether that coefficient decreases with the number of players. **That scalar monotonicity was already proved by Kia Keng Giam (2026), and is not claimed here.** The statement here concerns every pair of quantiles, a sharp *two-sided* global derivative bound for the monotone transport, and resulting distributional/convex-order implications; scalar variance monotonicity does not imply these stronger statements. Standard dispersive-order definitions and implications are described by Jeon, Kochar and Park (2006) and Kochar (2012). Their general comparison principles do not, from the inspected material, state the particular sharp logarithmic-exponential quantile transport bounds.

Under the usual fixed-player coupon collector limit, \(-Y_n\) has the law of the minimum of \(n\) independent standard Gumbel variables. The theorem thus provides a sharp comparison of *all* limiting completion-time quantile widths as the number of independent collectors varies.

## Limitations
This is a statement about the limiting fixed-player distribution, not a uniform-in-player-count finite-coupon theorem. It does not assert that every finite-size coupon completion-time interquantile width decreases with player count. The prior paper of Giam establishing scalar variance monotonicity was located through its published abstract and bibliographic record, but its full text could not be accessed for a line-by-line comparison; a possible unrecognized equivalent dispersive statement in that article remains a priority risk. Likewise a general stochastic-order theorem could imply the sharp transport comparison under a different name. Independent validation and an exhaustive historical-priority audit have not been performed. No claim of a solution to the already-settled variance conjecture is made.

## References
1. A. V. Doumas, *An inequality involving alternating binomial sums*, arXiv:2603.11129v1 (first public posting 2026-03-11), https://arxiv.org/html/2603.11129v1 ; Statistics & Probability Letters **235** (2026), 110735, https://doi.org/10.1016/j.spl.2026.110735 .
2. K. K. Giam, *Decreasing nature of a sequence related to the Coupon Collector's problem*, Statistics & Probability Letters **236** (2026), 110790, https://doi.org/10.1016/j.spl.2026.110790 ; preprint record https://ssrn.com/abstract=6447308 .
3. J. Jeon, S. Kochar, and C. G. Park, *Dispersive ordering—Some applications and examples*, Statistical Papers **47** (2006), 227–247, https://doi.org/10.1007/s00362-005-0285-4 .
4. S. Kochar, *Stochastic Comparisons of Order Statistics and Spacings: A Review*, International Scholarly Research Notices (2012), article 839473, https://doi.org/10.5402/2012/839473 .
