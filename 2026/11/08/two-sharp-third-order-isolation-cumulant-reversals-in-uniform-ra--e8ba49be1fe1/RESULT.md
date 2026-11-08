# Two sharp third-order isolation-cumulant reversals in uniform random key graphs

## Finding
Fix an integer \(K\ge1\). Construct the *uniform random key graph* on \(n\ge3\) labelled vertices by giving each vertex an independent uniform \(K\)-element subset of a pool of \(P\ge4K\) keys, and joining two vertices precisely when their sets intersect. Let \(X_i\) indicate that vertex \(i\) is isolated. Write
\[
q=\frac{\binom{P-K}{K}}{\binom PK},\qquad
r=\frac{\binom{P-2K}{K}}{\binom PK},\qquad
u=\frac{\binom{P-3K}{K}}{\binom PK}.
\]
For three distinct marked vertices the exact joint third cumulant is
\[
\kappa_3(n;P,K)=\mathbb E[(X_1-\mathbb EX_1)(X_2-\mathbb EX_2)(X_3-\mathbb EX_3)]
=qr\nu^{n-3}-3q^{n}r^{n-2}+2q^{3n-3}.
\]
For every \(P\ge4K\) its sign, as a function of integer \(n\ge3\), can change at most twice. For each fixed \(K\ge1\), as \(P\to\infty\) with \(n/P\to c>0\),
\[
\boxed{P^2\kappa_3(n;P,K)\longrightarrow e^{-3cK^2}K^3(cK-1)(3cK^2-3K-2).}
\]
Consequently, for all sufficiently large \(P\), the sign sequence in increasing \(n\) has *exactly two* transitions (allowing an isolated zero at a transition): positive, negative, positive. Its real-parameter crossing locations \(n_-(P,K)\) and \(n_+(P,K)\), obtained by extending the exponential expression to real \(n\), obey
\[
\frac{n_-(P,K)}{P}\to\frac1K,
\qquad\frac{n_+(P,K)}P\to\frac1K+\frac{2}{3K^2}.
\]
These are statements about third *joint* cumulants of three **distinct** vertex indicators, not the third central moment of the total isolated-vertex count.

## Assumptions and scope
All random key rings are mutually independent and uniformly sampled *without replacement within each ring*; there are no independent communication-channel failures. The finite identity and at-most-two-transition statement hold for all integers \(n\ge3,\ K\ge1,\ P\ge4K\). The asymptotics fix \(K\) and let the key pool and vertex count jointly diverge, with \(n/P\) convergent to a positive finite constant. At integer crossings the exact cumulant can be zero; the sign-sequence statement concerns its strict-sign regions on either side. The real crossings are used only for locating the transitions, not for asserting that fractional vertex counts are graphs.

## Proof
**Three marked isolation probabilities.** Let \(p_j\) denote the probability that \(j\) specified distinct vertices are all isolated, for \(j=1,2,3\). Their key rings must be mutually disjoint. After a first ring is selected, each successive marked ring avoids its predecessors with probability given by the corresponding binomial ratio. Every remaining ring must avoid the union of \(jK\) marked keys. Hence
\[
p_1=q^{n-1},\qquad p_2=qr^{n-2},\qquad p_3=qr\nu^{n-3}.
\]
Expansion of the centered product gives \(\kappa_3=p_3-3p_1p_2+2p_1^3\), proving the exact formula.

**At most two transitions.** For \(0\le z\le3\) define \(h(z)=\prod_{i=0}^{K-1}(P-zK-i)/(P-i)\), which is positive under \(P\ge4K\). The second derivative of \(\log h(z)\) is strictly negative. Therefore \(r<q^2\) and \(\nu<r^2/q<qr\). Set \(t=n-3\) and divide the exact cumulant by the positive factor \((qr)^t\). The sign equals that of
\[
G(t)=qr\left(\frac{\nu}{qr}\right)^t-3q^3r+2q^6\left(\frac{q^2}{r}\right)^t.
\]
The two exponential bases are respectively strictly below and strictly above one. Thus \(G''(t)>0\) for every real \(t\) and \(G(t)\to+\infty\) at both ends of the real line. Its negative set is empty or one interval, so the sign on integer \(t\ge0\) changes at most twice.

**Two sharp limiting crossings.** Let \(x=P^{-1}\) and \(L_j=\log\bigl(\binom{P-jK}{K}/\binom PK\bigr)\). For fixed \(K\), Taylor expansion of each logarithmic factor gives, uniformly through cubic order,
\[
L_j=-\sum_{\ell=1}^3\frac{x^\ell}{\ell}\sum_{i=0}^{K-1}[(jK+i)^\ell-i^\ell]+O_K(x^4),\qquad j=1,2,3.
\]
Put \(c_P=n/P\) and \(t=n-3\). Dividing \(\kappa_3\) by \(qr\nu^t\) yields \(1-3e^A+2e^B\), where
\[
A=2L_1+t(L_1+L_2-L_3),\qquad B=5L_1-L_2+t(3L_1-L_3).
\]
For bounded \(c_P\) bounded away from zero, substitution of \(t=c_P/x-3\) gives
\[
\begin{aligned}
A&=2K^2(c_PK-1)x+K^2(8K^2c_P-2Kc_P-8K+1)x^2+O(x^3),\\
B&=3K^2(c_PK-1)x+\frac{K^2}{2}(22K^2c_P-6Kc_P-22K+3)x^2+O(x^3).
\end{aligned}
\]
The constant and linear coefficients in \(1-3e^A+2e^B\) cancel. The quadratic coefficient factors exactly as
\[
K^3(c_PK-1)(3c_PK^2-3K-2).
\]
Also \(qr\nu^t\to e^{-3cK^2}\), yielding the stated limit. The expansion is uniform over compact subintervals of \(c>0\). The limiting polynomial has exactly two distinct positive simple roots, at \(1/K\) and \(1/K+2/(3K^2)\), with respective positive/negative/positive strict signs on the three regions. For any sufficiently large \(P\), integer choices \(n\) with \(n/P\) in fixed compact subintervals of those three regions have exactly these signs. Strict convexity already excludes more than two sign reversals. Moreover the real crossing locations must converge to the two roots: otherwise continuity, uniform compact convergence, and the at-most-two-crossing property would contradict those strict-sign test points. This proves the full classification.

## Verification
The standalone `verify.py` uses only Python's standard library. It independently enumerates key-ring assignments in seven small parameter instances, evaluates each of the three marked isolation probabilities by literal incidence tests, checks exact rational identities, tests strict ratio inequalities over 160 additional pool sizes, and compares high-precision finite-pool values with the derived asymptotic. The executed script printed `VERIFICATION_OK exact_assertions=403`. These finite calculations validate examples and algebraic checkpoints, not the infinite limiting assertion, whose proof is the expansion above.

At the nontrivial finite example \((P,K)=(8,2)\), the exact cumulant is positive for \(n=4\), negative for \(n=5\), and positive for \(n=6\). This exhibits both reversals without taking a limit.

## Relationship to prior work
Yağan and Makowski's 2008 random-key-graph analysis derives the one-vertex isolation probability and the two-vertex joint probability, and treats absence-of-isolation thresholds and Poisson approximation. Their later full-text connectivity paper develops related zero-one laws. Those results supply the model and pair-level comparison, but the examined sections do not state the three-distinct-vertex connected cumulant, its two sharp sign changes, or the fixed-\(K\), \(n/P\to c\) quadratic profile. The elementary marked-ring enumeration is an extension of known moment methods, not itself a new general enumerative principle. Searches of relevant mathematical records found no equivalent evaluated asymptotic or sign-phase theorem; priority cannot be proven by negative searches.

## Limitations
The theorem assumes fixed ring size \(K\), independent uniform key assignments, and a full-visibility intersection graph. It makes no assertion about \(K\) growing with \(P\), partial visibility, monotonicity of the full isolated-count skewness, or connectivity thresholds. The finite sign sequence may have zero or one sign transition for small pools; uniqueness of each crossing is guaranteed only when there are both negative and positive regions, in particular for sufficiently large pools at fixed \(K\). Possible implicit coverage in broader random-intersection-graph higher-factorial-moment formulas is a residual historical-priority risk. Independent validation has not been performed.

## References
1. O. Yağan and A. M. Makowski, *On the random graph induced by a random key predistribution scheme under full visibility (extended version)*, ISIT 2008, https://users.ece.cmu.edu/~oyagan/Conferences/ISIT2008-extended.pdf.
2. O. Yağan and A. M. Makowski, *Zero-one laws for connectivity in random key graphs*, arXiv:0908.3644, first submitted 2009-08-25, https://arxiv.org/abs/0908.3644.
