# Endpoint rigidity of the Stein size factor for a dense two-row hyper-negative-binomial law

## Finding
Let \(w\in[9/10,1)\) and let \(X\) have probabilities
\[
p_n=\frac{(1-w)^3}{1+w}(n+1)^2w^n,\quad n=0,1,\ldots.
\]
This is the equal-row, two-column hyper-negative-binomial law: it is the law of a common row total conditioned on equality of two independent \(\operatorname{NB}(2,q_i)\) totals, with \(w=q_1q_2\). For the Stein equation
\[
w(n+2)^2g_A(n+1)-n^2g_A(n)={\bf1}_A(n)-\Pr(X\in A),\quad g_A(0)=0,
\]
the sharp indicator sup-norm factor is exactly
\[
\boxed{\Gamma(w):=\sup_{A\subseteq\mathbb N_0}\sup_{j\ge1}|g_A(j)|
=\frac{1-(1-w)^3/(1+w)}{4w}.}
\]
The supremum occurs at the first positive argument \(j=1\). Quantitatively, every later argument \(j\ge2\) has sharp-in-\(A\) value at most \(1/5\), while the first has value at least \(1/4\). Consequently \(\lim_{w\uparrow1}\Gamma(w)=1/4\). The explicit interval is a guaranteed dense-parameter range, not an asserted optimal boundary.

## Assumptions and scope
All indices are nonnegative integers and \(w\) is real in the indicated interval. The law is normalized because \(\sum_{n\ge0}(n+1)^2w^n=(1+w)/(1-w)^3\). Only this equal-offset \(r=2,c=2\) hyper-negative-binomial family and its *size* Stein factor are addressed. No first-difference factor or general-row result is asserted.

## Proof
Write \(F_m=\sum_{j\le m}p_j\), \(G_{m+1}=\sum_{j>m}p_j\), and \(d(j)=j^2\). Detailed balance gives \(w(n+2)^2p_n=(n+1)^2p_{n+1}\). Multiply the Stein equation by \(p_n\), sum over \(0\le n\le m\), and telescope:
\[
(m+1)^2p_{m+1}g_A(m+1)=\sum_{n=0}^m p_n({\bf1}_A(n)-\Pr(X\in A)).
\]
The right-hand absolute value is maximized over all events \(A\) by the initial segment or its complement, and its maximum is \(F_mG_{m+1}\). Therefore
\[
\Gamma=\sup_{m\ge0}\Gamma_m,\qquad
\Gamma_m=\frac{F_mG_{m+1}}{(m+1)^2p_{m+1}}.
\]
At \(m=0\), \(p_1=4wp_0\), hence \(\Gamma_0=(1-p_0)/(4w)\). Since \((1-w)^2\le1+w\), \(p_0\le1-w\) and \(\Gamma_0\ge1/4\).

We bound all \(m\ge1\) uniformly. Put \(n=m+1\ge2\) and \(\varepsilon=1-w\). Exact summation gives
\[
F_m=\frac{\varepsilon^3}{1+w}\sum_{j=1}^{n}j^2w^{j-1},\qquad
\frac{G_{m+1}}{p_{m+1}}=\frac1\varepsilon+
\frac{2w}{(n+1)\varepsilon^2}+
\frac{w(1+w)}{(n+1)^2\varepsilon^3}.
\]
Using \(\sum_{j=1}^{n}j^2\le n^3\), \(w\le1\), and \(w(1+w)\le2\), these identities yield \(\Gamma_m\le5/n\). Indeed, if \(\varepsilon n\le1\), then
\[
\Gamma_m\le \varepsilon^2n+\frac{2\varepsilon n}{n+1}+\frac{2n}{(n+1)^2}\le\frac5n;
\]
if \(\varepsilon n\ge1\), then \(F_m\le1\), the tail ratio is at most \(5/\varepsilon\), and \(\Gamma_m\le5/(\varepsilon n^2)\le5/n\). In particular, \(\Gamma_m\le1/5\) for \(n\ge25\).

For the remaining finite range \(2\le n\le24\), use \(\varepsilon\le1/10\) and \(1+w\ge19/10\) in the same exact formulas:
\[
\Gamma_m\le B_n:=\frac{(2n+1)(n^2+22n+221)}{1140n(n+1)}.
\]
A rational rearrangement gives
\[
\frac15-B_n=\frac{-2n^3+183n^2-236n-221}{1140n(n+1)}.
\]
At \(n=2\), the numerator is \(23\). At each integer \(3\le n\le24\), it is at least \(135n^2-236n-221>0\), because \(2n\le48\). Therefore \(\Gamma_m<1/5\) throughout this finite range. Combining both ranges, every \(m\ge1\) satisfies \(\Gamma_m\le1/5<1/4\le\Gamma_0\), so the global supremum is uniquely realized at \(m=0\). Its explicit formula proves the result. \(\square\)

## Verification
The standalone standard-library script `check_factor.py` checks the rational inequality for every integer \(2\le n\le24\) and verifies the exact finite-index factor identities for four rational parameter values. It completed 842 exact-rational assertions. The infinite tail and the global supremum follow from the analytical two-regime bound, not the script.

## Relationship to prior work
DeSalvo (arXiv:2611.00275v1), Proposition 3.17, gives a general tail-supremum expression for the size factor and explicitly asks in Open Problem 7 for dense-parameter behavior of hyper-negative-binomial factors. Here that supremum is resolved in closed form for the first genuinely nonlinear two-row, two-column case on a certified near-one interval. General negative-binomial convolution ordering as in Zhang (2018) does not evaluate the indicator Stein size factor. Published first-lattice results for constant-birth Stein *increment* factors concern a different operator and factor and do not entail this supremum evaluation.

## Limitations
The interval \([9/10,1)\) is sufficient but not shown maximal. The case \(w<9/10\), unequal offsets, different shapes, additional rows and the Stein *increment* factor are outside the proof. Priority is assessed against the inspected literature, not certified independently. A numerical finite-index scan is not an infinite-index proof; the rigorous tail estimate supplies that step.

## References
1. Stephen DeSalvo, *Stein's method for negative binomial and hyper-negative-binomial laws, with applications*, arXiv:2611.00275v1 (first posted 2026-10-30), https://arxiv.org/html/2611.00275v1.
2. Ying Zhang, *Stochastic orders for convolution of heterogeneous gamma and negative binomial random variables*, arXiv:1811.11360v1 (2018), https://arxiv.org/pdf/1811.11360.
3. *The first-lattice-site law for Stein increments of log-concave birth-death targets*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-first-lattice-site-law-for-stein-increments-of-log-concave-b--c61fadb74d75 (distinct constant-birth increment result).
