# Exact golden-ratio symbolic entropy and a uniform metric-entropy gap in an auxiliary Fibonacci-bimodal map

## Finding
For the countable-branch auxiliary map \(T_\lambda\) introduced by Ji and Ma [1], \(0<\lambda<1\), the Gurevich entropy of its natural one-sided countable Markov itinerary is exactly
\[
h_G=\log(2+\sqrt5),
\]
independent of \(\lambda\). For \(0<\lambda<1/2\), let \(\mu_\lambda\) be the absolutely continuous invariant probability measure constructed from the paper's stationary Markov weights. Its Kolmogorov--Sinai entropy is
\[
h_{\mu_\lambda}(T_\lambda)=-\log(1-\lambda)-\frac{\lambda}{1-\lambda}\log\lambda.
\]
The metric entropy increases strictly from \(0\) to \(\log4\) as \(\lambda\uparrow1/2\). Thus the exact uniform entropy deficit satisfies
\[
h_G-h_{\mu_\lambda}(T_\lambda)>\log\frac{2+\sqrt5}{4}>0,
\]
and its infimum over \(0<\lambda<1/2\) is the rightmost constant. In particular, these absolutely continuous invariant probabilities are not maximal-entropy measures for the Markov itinerary. The associated graph has a positive-recurrent maximal-entropy Markov measure.

## Assumptions and scope
Fix \(0<\lambda<1\) and the intervals \(V_j=(\lambda^j,\lambda^{j-1}]\) for integers \(j\ge1\). Consider exactly the auxiliary map on \((0,1]\) specified in [1, Section 5.1]:
\[
T_\lambda(x)=\begin{cases}
(x-\lambda)/(1-\lambda),&x\in V_1,\\
(x-\lambda^2)/(\lambda(1-\lambda)),&x\in V_2,\\
(x-\lambda^3)/(\lambda^2(1-\lambda)),&x\in V_3,\\
(x-\lambda^4)/(\lambda^2(1-\lambda)),&x\in V_4,\\
(x-\lambda^j)/(\lambda(1-\lambda)),&x\in V_j,\ j\ge5.
\end{cases}
\]
Use endpoint conventions modulo the countable itinerary-boundary set. This is the paper's separate auxiliary map \(T_\lambda\), **not** the original odd bimodal map \(f_\lambda\) or its distinct induced map \(F_\lambda\); [1] explicitly says the latter and \(T_\lambda\) are not semiconjugate. No entropy formula for \(f_\lambda\) or \(F_\lambda\) is asserted.

Set \(A_{ij}=1\) if \(T_\lambda(V_i)\) contains the interior of \(V_j\), otherwise \(A_{ij}=0\). Then, independently of \(\lambda\),
\[
A_{ij}=1\iff\begin{cases}
j\ge1,&1\le i\le3,\\
j\ge2,&i=4,\\
j\ge i-1,&i\ge5.
\end{cases}
\]
The countable Markov shift on this graph has Gurevich entropy \(h_G:=\lim_{n\to\infty}n^{-1}\log(A^n)_{11}\). These closed-walk counts are finite for each \(n\), although each row has infinitely many outgoing edges.

## Proof
**Symbolic entropy.** Define \(r=(3-\sqrt5)/2\), \(\beta=2+\sqrt5\), and the strictly positive sequence
\[
w_1=w_2=w_3=1,\qquad w_i=2r^{i-3}\quad(i\ge4).
\]
Direct algebra gives \(\beta r(1-r)=1\), \(\beta=3+2r/(1-r)\), and \(2\beta r=2+2r/(1-r)\). Summing the geometric tails verifies \(Aw=\beta w\) at states \(1,2,3\), at state \(4\), and at every state \(i\ge5\), respectively. In particular, since \(w_1=1\), \((A^n)_{11}\le\beta^n\) for all \(n\ge1\).

Normalize edges using the Doob transform \(Q_{ij}=A_{ij}w_j/(\beta w_i)\). The eigenvector equation makes \(Q\) stochastic. For each \(i\ge5\), its destination is \(i-1+G\), where \(\Pr(G=k)=(1-r)r^k\) for \(k\ge0\). Hence its conditional drift in the state index is \(-1+r/(1-r)<0\), as \(r<1/2\). At the four remaining states the conditional next-state mean is finite, since outgoing weights decay geometrically. The irreducible, aperiodic chain \(Q\) therefore satisfies the Foster negative-drift condition outside a finite set and is positive recurrent. Thus \(Q^n_{11}\to\pi_1>0\) for its stationary law. The identity \((A^n)_{11}=\beta^nQ^n_{11}\) now supplies the reverse entropy inequality, proving \(h_G=\log\beta\). The positive-recurrent Doob chain also defines a Markov measure of maximal symbolic entropy (equivalently by countable-state Markov variational theory [2]).

**Metric entropy.** For any state \(i\), conditional normalized Lebesgue measure on \(V_i\) is carried by its affine branch to normalized Lebesgue measure on the full interval \(T_\lambda(V_i)\). Hence the successor cell index has the distribution \(j=b_i+G\), with \(\Pr(G=k)=(1-\lambda)\lambda^k\) for \(k\ge0\), where \(b_i=1\) for \(i\le3\), \(b_4=2\), and \(b_i=i-1\) for \(i\ge5\). In the range \(0<\lambda<1/2\), [1, Lemma 5.2] provides summable stationary weights \(p_i\). The density \(p_i/|V_i|\) on \(V_i\) is therefore an invariant probability density. Because each branch has derivative of absolute value at least \((1-\lambda)^{-1}>1\), the countable cell partition is generating, and its stationary entropy rate equals the Kolmogorov--Sinai entropy. Every transition row has the same geometric Shannon entropy, giving
\[
h_{\mu_\lambda}(T_\lambda)=-\sum_{k\ge0}(1-\lambda)\lambda^k\log((1-\lambda)\lambda^k)
=-\log(1-\lambda)-\frac{\lambda}{1-\lambda}\log\lambda.
\]
Differentiate: \(h'_{\mu_\lambda}=-\log\lambda/(1-\lambda)^2>0\). The limits are \(0\) as \(\lambda\downarrow0\) and \(\log4\) as \(\lambda\uparrow1/2\). Since \(2+\sqrt5>4\), the asserted strict gap and its infimum follow.

## Verification
The accompanying `verify_entropy.py` performs exact SymPy simplifications of all three eigenvector equations, the negative-drift inequality, the entropy formula, its derivative and its limiting values. It independently checks the stationary cell-weight reduction displayed in [1, Section 5.1]. Numerical Perron-root computations on four finite truncations \(N=10,20,40,80\) agree with \(2+\sqrt5\). These finite truncations are diagnostics only; the infinite-state entropy is proved by the positive-recurrent Doob chain, not by extrapolation.

## Relationship to prior work
Ji and Ma [1] define this auxiliary map, supply its countable transition matrix, and establish the stationary weights and conservative/dissipative regimes. Their treatment does not evaluate the Gurevich entropy, the exact Kolmogorov--Sinai entropy curve, or the resulting uniform entropy gap. General countable Markov thermodynamics [2] supplies conceptual machinery but not the graph-specific algebraic Perron root or the parameter-dependent quantitative comparison. The contribution is these **joint exact invariants for the specific natural graph and its invariant probability**, not a new general Gurevich-entropy theorem, nor the existence of the underlying Markov partition.

## Limitations
This theorem is only about \(T_\lambda\) and its countable Markov coding. In particular it does not transfer by conjugacy to \(f_\lambda\) or \(F_\lambda\), whose relationships [1] explicitly distinguish. The metric-entropy formula concerns the specific absolutely continuous invariant probability available for \(0<\lambda<1/2\); it is not asserted at or beyond the null-recurrent threshold. The countable shift's Gurevich entropy is not automatically the topological entropy of every conceivable noncompact interval-map extension. Independent priority review has not been performed.

## References
[1] H. Ji and W. Ma, *Phase transition for piecewise linear fibonacci bimodal map*, AIMS Mathematics 8(4) (2023), 8403--8430; publicly posted 2023-02-03; doi:10.3934/math.2023424. Open primary PDF: https://www.aimspress.com/aimspress-data/math/2023/4/PDF/math-08-04-424.pdf.

[2] O. M. Sarig, *Thermodynamic formalism for countable Markov shifts*, Ergodic Theory and Dynamical Systems 19(6) (1999), 1565--1593, doi:10.1017/S0143385799146820.
