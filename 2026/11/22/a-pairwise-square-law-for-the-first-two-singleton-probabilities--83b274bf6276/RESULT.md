# A pairwise-square law for the first two singleton probabilities at coupon completion

## Finding

Consider independent draws from a finite alphabet of \(N\ge2\) coupon types, with fixed strictly positive probabilities \(p_1,\ldots,p_N\) summing to one. Stop at the first draw by which all types have appeared. Let \(U\) count types that have appeared **exactly once** at that moment; equivalently, \(U\) is the number of missing coupon types in the first sibling's album when the main collector completes the collection. Put
\[
F_k(t)=1-(1+p_k t)e^{-p_k t},\qquad t\ge0.
\]
Then the following *exact* identity holds:
\[
\boxed{\Pr_p(U=1)-\Pr_p(U=2)=
\sum_{1\le i<j\le N}(p_i-p_j)^2
\int_0^\infty t e^{-(p_i+p_j)t}
\prod_{k\notin\{i,j\}}F_k(t)\,dt.}
\tag{1}
\]
In particular, for every finite \(N\ge2\),
\[
\boxed{\Pr_p(U=1)\ge\Pr_p(U=2),\quad
\Pr_p(U=1)=\Pr_p(U=2)\iff p_1=\cdots=p_N=1/N.}
\tag{2}
\]
For two types, (1) reduces to the elementary but sharp boundary \(\Pr(U=1)-\Pr(U=2)=(p_1-p_2)^2\). The new assertion is the universal all-\(N\) inequality and its strictly positive pairwise heterogeneity decomposition; the uniform-case singleton distribution was previously known.

## Assumptions and scope

The sampling probabilities are strictly positive, fixed across independent draws, and sum to one. The number of types is any integer \(N\ge2\). The stopping time is the **first** full coverage, not a fixed observation time nor the first time two copies of every type have been collected. Consequently \(U\in\{1,\ldots,N\}\) because the last new type occurs exactly once. The first sibling is album index two in the usual sibling collector convention. If a coupon has zero probability, full coverage does not occur; such probability vectors are outside the claim.

## Proof

**Step 1 (Poissonized completion).** Embed the categorical draws as marks of a rate-one Poisson process. The separate type-counting processes \(N_k(t)\) are independent, each with rate \(p_k\). The marks in the superposition are independent with the given type probabilities, so the vector of counts at the instant of the last *first* arrival has exactly the same law as the discrete stopped collector. Let \(T=\max_k\inf\{t:N_k(t)\ge1\}\). As positive-rate first arrivals are independent continuous random variables, precisely one type \(j\) achieves the maximum almost surely. The joint density that the last new type is \(j\), appearing at time \(t\), is \(p_j e^{-p_jt}\prod_{k\ne j}(1-e^{-p_kt})\).

**Step 2 (the two relevant probabilities).** For a nonfinal type \(k\), having at least two arrivals by time \(t\) has probability \(F_k(t)=1-(1+p_k t)e^{-p_k t}\), while having exactly one arrival has probability \(p_k t e^{-p_k t}\). Independence gives
\[
A_j:=\Pr(U=1,\text{last type}=j)
=\int_0^\infty p_j e^{-p_jt}\prod_{k\ne j}F_k(t)\,dt,
\]
and
\[
B_{ij}:=\Pr(U=2,\text{last type}=j,\text{other singleton}=i)
=\int_0^\infty p_i p_j t e^{-(p_i+p_j)t}
\prod_{k\notin\{i,j\}}F_k(t)\,dt
\quad(i\ne j).
\]
Thus \(\Pr(U=1)=\sum_j A_j\), \(\Pr(U=2)=\sum_j\sum_{i\ne j}B_{ij}\), and \(B_{ij}=B_{ji}\).

**Step 3 (integration by parts and pairing).** The derivative is
\[
F_i'(t)=p_i^2 t e^{-p_i t}.
\]
For every \(j\), the function \(\prod_{k\ne j}F_k(t)\) vanishes at zero (since \(N\ge2\)) and is bounded by one at infinity. Integrate \(A_j\) by parts using \(p_j e^{-p_jt}\,dt=d(-e^{-p_jt})\), with zero boundary terms:
\[
A_j=\sum_{i\ne j}\int_0^\infty e^{-p_jt}F_i'(t)
\prod_{k\notin\{i,j\}}F_k(t)\,dt
=\sum_{i\ne j}\frac{p_i}{p_j}B_{ij}.
\]
Subtracting the two probabilities and pairing the ordered terms \((i,j)\) and \((j,i)\) yields
\[
\begin{aligned}
\Pr(U=1)-\Pr(U=2)
&=\sum_{i<j}\left(\frac{p_i}{p_j}+\frac{p_j}{p_i}-2\right)B_{ij}\\
&=\sum_{i<j}(p_i-p_j)^2
\int_0^\infty t e^{-(p_i+p_j)t}
\prod_{k\notin\{i,j\}}F_k(t)\,dt.
\end{aligned}
\]
This proves (1). Every integral on the right is finite and **strictly positive**: the exponential term ensures integrability, and \(F_k(t)>0\) for all \(t>0\) and all positive \(p_k\). For \(N=2\), the empty product equals one. Therefore (1) vanishes if and only if all pairs of probabilities are equal, proving (2). These steps establish the claim for arbitrary finite \(N\) and arbitrary strictly positive probabilities; no limiting or numerical approximation is involved.

## Verification

The standalone `verify.py` uses only the Python standard library. It independently obtains the stopped singleton distribution by exact-rational recursion over finite occupancy states \(\{0,1,\ge2\}^{N}\), **without using** the integral identity. Separately, it expands the right-hand side of (1) as a finite signed sum of exact gamma integrals, evaluating each term by \(\int_0^\infty t^m e^{-\lambda t}\,dt=m!/\lambda^{m+1}\). The checker passes 522 exact-rational assertions across nonuniform, uniform and unequal configurations of \(2\le N\le6\), comparing the two independently computed expressions and checking equality cases. Run `python3 verify.py` alongside this file. The finite tests check implementation consistency; the proof above establishes all-size and continuum validity.

## Relationship to prior work

Myers and Wilf (2003, Section 4) derived the complete singleton-count distribution under **uniform** coupon sampling. Adler, Oren and Ross (2003, Section 3) addressed nonuniform sibling counts mainly through their expectations and bounds. Doumas and Papanicolaou (2014/2018) developed expectation asymptotics; Doumas and Spektor (arXiv:2606.21591, first public June 19, 2026) established that uniform probabilities maximize expected sibling deficits. Long (arXiv:2606.31391, Proposition 2.1) supplied an exact nonuniform probability-generating-function representation and radial transform/binomial-moment comparisons, but explicitly distinguished these from coefficientwise stochastic-order statements. Formula (1) follows from the Poissonized joint law by a separate integration-by-parts pairing; the published transform orders, by themselves, do not establish this **within-distribution** comparison of the first two atoms.

Closest further comparisons include previously published finite-type stochastic-order results (for three and four coupon types) and a conditional likelihood-ratio theorem for singleton counts given continuous completion time. Those have different conclusions: they compare sampling laws against uniform or condition on completion time, not the all-type unconditional mass difference in (1). The result does **not** claim a general stochastic-order comparison or a new formula for the full distribution.

## Limitations

The inequality concerns only the two atoms \(U=1\) and \(U=2\), not the mode or monotonicity of the entire distribution and not a comparison of two distinct nonuniform probability vectors. The identity is special to the first sibling; for example, with two equiprobable types the number missing in the **second sibling** (album index three) has probabilities \(\Pr(U_3=1)=1/4\) and \(\Pr(U_3=2)=3/4\), reversing (2). Although the proof and finite diagnostics are self-contained, independent mathematical validation and a comprehensive historical-priority audit have not been performed. General occupancy identities in older literature may yield an equivalent inequality under different notation.

## References

1. A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229 (first public April 16, 2003), especially Section 4. https://arxiv.org/abs/math/0304229
2. I. Adler, S. Oren and S. M. Ross, *The Coupon-Collector's Problem Revisited*, Journal of Applied Probability **40** (2003), 513–518, especially Section 3. https://oren.ieor.berkeley.edu/pubs/coupon.pdf
3. A. V. Doumas and V. G. Papanicolaou, *The Siblings of the Coupon Collector*, arXiv:1412.4346 (2014 preprint; published 2018). https://arxiv.org/abs/1412.4346
4. A. V. Doumas and S. Spektor, *Equal probabilities maximize the expected deficit in the siblings of the coupon collector*, arXiv:2606.21591, first public June 19, 2026. https://arxiv.org/abs/2606.21591
5. C. D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, arXiv:2606.29635, first public June 28, 2026. https://arxiv.org/abs/2606.29635
6. C. D. Long, *Radial Transform Extremality for the Siblings of the Coupon Collector*, arXiv:2606.31391, first public June 30, 2026; especially Proposition 2.1 and Remark 1.2. https://arxiv.org/abs/2606.31391
