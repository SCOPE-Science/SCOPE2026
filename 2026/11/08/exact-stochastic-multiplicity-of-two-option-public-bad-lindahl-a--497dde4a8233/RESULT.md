# Exact stochastic multiplicity of two-option public-bad Lindahl allocations

## Finding

Consider two agents, two publicly selected harmful alternatives \(A,B\), and a lottery assigning probability \(t\in[0,1]\) to \(A\). Each of the four marginal harms is sampled independently from the same strictly positive, atomless probability distribution. Let \(N\) denote the number of distinct lottery allocations admitting zero-respecting Lindahl prices (equivalently, the number of proportionally fair lotteries, by Cookson–Ebadian–Peters–Shah, Theorem 4.9). Then \(N\in\{1,3\}\) almost surely. Write

\[
H(r)=\Pr\{X/Y\le r\mid X<Y\},\qquad 0\le r\le1,
\]

where \(X,Y\) are independent draws of the common strictly positive, atomless harm distribution. The exact probability of three allocations is

\[
\boxed{\Pr\{N=3\}=\frac12\int_0^1\bigg[H\bigg(\frac1{2-r}\bigg)-H\bigg(\max\{0,2-1/r\}\bigg)\bigg] \,dH(r).}
\]

The value at \(r=0\) in the integrand is assigned by continuity. In the two canonical models the answer is explicit:

\[
\begin{aligned}
\text{i.i.d. Uniform}(0,1):&&\Pr\{N=3\}&=\log2-\tfrac12,&&\mathbb E N=2\log2;\\
\text{i.i.d. Exponential}(1):&&\Pr\{N=3\}&=\tfrac14\log3,&&\mathbb E N=1+\tfrac12\log3.
\end{aligned}
\]

Numerically these probabilities are about \(0.193147\) and \(0.274653\), respectively. Despite identical distributions of the agents' ordinal preferences (each prefers either alternative with probability one half), the magnitudes of harms substantially change the chance of multiple fair lotteries.

## Assumptions and scope

There are exactly two agents indexed \(i=1,2\) and two public-bad alternatives \(A,B\). For each agent, \(a_i=c_i(A)>0\) and \(b_i=c_i(B)>0\) are finite. Under the random model, all four numbers are mutually independent and identically distributed from an atomless probability measure supported in \((0,\infty)\). A lottery \(t\) chooses \(A\) with probability \(t\) and \(B\) otherwise; its cost for agent \(i\) is \(u_i(t)=t a_i+(1-t)b_i\). We count distinct lotteries, not personalized price-vector representations. All logarithms are natural. Uniform and exponential calculations are invariant under common positive rescaling.

The proportional-fairness (PF) criterion from the motivating paper reads

\[
\sum_{i=1}^2\frac{c_i(Y)}{u_i(t)}\ge 2\quad\text{for both }Y\in\{A,B\}.
\]

Every cost is strictly positive, so PF allocations are precisely zero-respecting Lindahl allocations by that paper's Theorem 4.9. This equivalence and the general PF inequalities are pre-existing results, not new claims here. The novelty asserted here is the stochastic multiplicity law and its two distribution-specific closed forms.

## Proof

**1. Reduction to a concave log product.** Set

\[
F(t)=\sum_{i=1}^2\log\big(b_i+t(a_i-b_i)\big).
\]

Direct differentiation gives

\[
F'(t)=\sum_i\frac{a_i-b_i}{u_i(t)},\qquad
F''(t)=-\sum_i\frac{(a_i-b_i)^2}{u_i(t)^2}.
\]

Unless both agents are exactly indifferent, \(F''(t)<0\) throughout \([0,1]\). The two PF inequalities have left-hand sides \(2+(1-t)F'(t)\) for alternative \(A\) and \(2-tF'(t)\) for alternative \(B\). Therefore \(t=0\) is PF exactly when \(F'(0)\ge0\); \(t=1\) is PF exactly when \(F'(1)\le0\); and an interior \(t\) is PF precisely when \(F'(t)=0\). By strict decrease of \(F'\), at most one interior PF lottery exists, and it exists exactly if \(F'(0)>0>F'(1)\). In that event both endpoint lotteries also satisfy PF, so \(N=3\). Otherwise, off equality boundaries, exactly one endpoint satisfies PF. The zero-derivative boundaries or perfect indifference have probability zero under iid atomless draws, proving \(N\in\{1,3\}\) almost surely.

**2. Two independently distributed preference ratios.** Three distinct PF lotteries require that the agents strictly prefer opposite alternatives: if both differences \(a_i-b_i\) have the same sign, \(F'\) cannot cross zero. Each opposite-order orientation has probability \(1/4\). By relabeling agents and alternatives, take \(a_1<b_1\) and \(a_2>b_2\) and define

\[
r=\frac{a_1}{b_1}\in(0,1),\qquad s=\frac{b_2}{a_2}\in(0,1).
\]

These two ratios are independent, each with conditional CDF \(H\). The endpoint derivatives become

\[
F'(0)=\frac1s+r-2,\qquad F'(1)=2-s-\frac1r.
\]

Consequently \(N=3\) is equivalent to

\[
\max\{0,2-1/r\}<s<\frac1{2-r}.
\]

Integrate with respect to \(s\) conditionally on \(r\), then to \(r\), and multiply by the total probability \(1/2\) of opposite-order preferences. This yields the claimed Stieltjes integral. Its boundaries have probability zero because the ratios have no atoms; the formula covers arbitrary positive atomless iid laws without requiring densities.

**3. Uniform costs.** For independent \(X,Y\sim\mathrm{Uniform}(0,1)\) and \(0\le r\le1\),

\[
\Pr\{X/Y\le r\mid X<Y\}=\frac{\int_0^1 ry\,dy}{1/2}=r.
\]

Thus the conditional opposite-order area is

\[
\int_0^{1/2}\frac{dr}{2-r}+\int_{1/2}^1\bigg(\frac1{2-r}-2+\frac1r\bigg)dr=2\log2-1.
\]

Multiplying by \(1/2\) proves the uniform probability \(\log2-1/2\).

**4. Exponential costs.** For independent unit-exponential \(X,Y\),

\[
\Pr\{X/Y\le r\mid X<Y\}=\frac{\int_0^\infty e^{-y}(1-e^{-ry})\,dy}{1/2}=\frac{2r}{1+r}.
\]

The associated density is \(h(r)=2/(1+r)^2\). Writing \(U(r)=1/(2-r)\) and \(L(r)=2-1/r\), the conditional opposite-order integral is

\[
\int_0^{1/2} h(r)\frac{2U(r)}{1+U(r)}dr+\int_{1/2}^1 h(r)\left[\frac{2U(r)}{1+U(r)}-\frac{2L(r)}{1+L(r)}\right]dr.
\]

Exact integration gives the respective terms \(\frac13-\frac14\log5+\frac12\log3\) and \(-\frac13+\frac14\log5\); their sum is \(\frac12\log3\). Multiplying by \(1/2\) proves \(\Pr\{N=3\}=\frac14\log3\). In either distribution the expected count is \(3p+1(1-p)=1+2p\). This completes the proof.

## Verification

The separately implemented, self-contained verifier `verification/check.py` exhaustively checks all \(9^4=6561\) integer-cost arrays with entries in \(\{1,\ldots,9\}\), comparing the derivative classification to the original two PF inequalities at every candidate lottery, and checks additional rational interior points. It obtains 6480 nonconstant arrays and 81 completely indifferent arrays. SymPy symbolically evaluates both integrals and compares with the exact closed forms; fixed-seed simulations with 240,000 draws for each distribution supply only a sampling sanity check and do not replace the symbolic proof. Run `python verification/check.py` from the extracted package root with SymPy installed.

## Relationship to prior work

Cookson, Ebadian, Peters, and Shah (arXiv:2607.26053v1, July 28, 2026) introduce PF and zero-respecting Lindahl allocations for public bads. Their Theorem 4.9 gives the equivalence used here, and their Proposition 6.1 supplies the general PF characterization. The reduction of the deterministic two-option case to stationary points of a Nash product is a straightforward specialization of these established results and is not claimed as new. Their examined computation discussion counts candidate supports but does not provide a distributional probability of multiple equilibria.

Bogomolnaia, Moulin, Sandomirskiy, and Yanovskaia (2019, *Social Choice and Welfare*, doi:10.1007/s00355-018-1157-x), Section 5, exhibit three competitive allocations in a two-agent, two-chore private-bads market and explicitly raise the question of how likely multiplicity is under random disutilities. The current setting instead concerns lotteries over two *public* bads, a one-dimensional feasible segment, with counts of Lindahl allocations. This earlier structural work motivates stochastic multiplicity but does not imply the two exact public-bad probabilities without the ratio-domain calculation.

## Limitations

Only two agents and two alternatives are covered. The probability formulas assume four mutually independent draws from one strictly positive atomless law; dependence, discrete atoms, structural zeros, more agents, and additional alternatives may have different multiplicities. We count allocation lotteries, not possibly nonunique personalized price systems. The general Stieltjes formula does not claim to give elementary closed forms for all sampling distributions. The uniform and exponential constants are analytic consequences of the stated model, not empirical market estimates. Complete worldwide originality cannot be certified by finite searches; equivalent unindexed work remains a residual risk. No independent scientific audit has been performed.

## References

1. B. Cookson, S. Ebadian, D. Peters, N. Shah, *Proportional Fairness for Harmful Decisions*, arXiv:2607.26053v1, publicly posted July 28, 2026. https://arxiv.org/abs/2607.26053 ; Theorem 4.9 and Proposition 6.1.
2. A. Bogomolnaia, H. Moulin, F. Sandomirskiy, E. Yanovskaia, *Dividing bads under additive utilities*, *Social Choice and Welfare* **52** (2019), 395–417. https://doi.org/10.1007/s00355-018-1157-x ; Section 5.
