# Two-scale correlation crossover between exploration and displacement in a hypercube walk

## Finding

In the non-lazy coordinate-flip walk on the binary hypercube, let \(D_{n,t}\) be the number of distinct coordinates flipped during the first \(t\) steps and let \(H_{n,t}\) be the Hamming distance from the starting vertex. For every integer \(n\ge3\) and \(t\ge2\),

\[
\operatorname{Cov}(D_{n,t},H_{n,t})
=\frac{n p}{2}\left(1+(n-1)b-na\right)>0,
\]
where \(p=(1-1/n)^t\), \(a=(1-2/n)^t\), and \(b=(1-2/(n-1))^t\). This exact finite-size identity is the starting point for the **two-scale normalized-correlation theorem below**; it is also obtainable by summing the known richness–fixed-frequency covariance identity over odd frequencies, and is not asserted as separately new.

When \(n\to\infty\) and \(t/n\to c\in(0,\infty)\), the exact correlation converges to

\[
\rho(c)=\frac{e^{-c}[1-(1+2c)e^{-2c}]}{
\sqrt{[e^{-c}-(1+c)e^{-2c}][1-(1+4c)e^{-4c}]}},
\]
with \(\rho(c)\to1\) as \(c\downarrow0\) and \(\rho(c)\sim e^{-c/2}\) as \(c\to\infty\). In the logarithmic regime \(t/(n\log n)\to\beta\in(0,\infty)\),

\[
\operatorname{Corr}(D_{n,t},H_{n,t})\sim(1-1/n)^{t/2},\qquad
\frac{\log\operatorname{Corr}(D_{n,t},H_{n,t})}{\log n}\longrightarrow-\beta/2.
\]
Thus exploration and displacement are positively associated at every finite time, but their linear correlation decays polynomially on the \(n\log n\) scale.

## Assumptions and scope

Fix integers \(n\ge3\) and \(t\ge2\). Start at the all-zero vertex of \(\{0,1\}^n\). At each step choose an index independently and uniformly from \(\{1,\dots,n\}\) and flip that index. Let \(N_i\) be the number of times index \(i\) is chosen. Then \(D_{n,t}=\sum_i\mathbf1_{\{N_i>0\}}\) and \(H_{n,t}=\sum_i\mathbf1_{\{N_i\text{ odd}\}}\). The walk does not have holding steps; neither statistic counts *distinct vertices visited*. Let \(d=(1-4/n)^t\), which is well-defined even if the base is negative (for \(n=3\)).

The exact marginal moments, needed to define the correlation, are

\[
\begin{aligned}
\mathbb E D_{n,t}&=n(1-p),&\mathbb E H_{n,t}&=\tfrac n2(1-a),\\
\operatorname{Var}(D_{n,t})&=n[p+(n-1)a-np^2],&
\operatorname{Var}(H_{n,t})&=\tfrac n4[1+(n-1)d-na^2].
\end{aligned}
\]
Both variances are strictly positive in the stated range. At \(t=2\), the correlation is exactly one; at \(t=1\), both statistics equal one deterministically and the correlation is undefined.

## Proof

For any fixed coordinate \(i\), the probability it is untouched is \(p\), whereas parity of its number of flips is odd with probability \((1-a)/2\); this follows from \(\mathbb E(-1)^{N_i}=a\). For distinct \(i,j\), conditioning on \(N_i=0\) leaves \(t\) independent draws uniformly distributed among the remaining \(n-1\) coordinates; hence

\[
\mathbb E[\mathbf1_{\{N_i=0\}}\mathbf1_{\{N_j\text{ odd}\}}]
=\tfrac p2(1-b).
\]
Consequently the same-coordinate covariance between \(\mathbf1_{\{N_i>0\}}\) and \(\mathbf1_{\{N_i\text{ odd}\}}\) is \(p(1-a)/2\); each different-coordinate covariance is \(p(b-a)/2\). Summing the \(n^2\) pairs proves the displayed covariance.

For the sign, observe
\[
1-\frac2n=\frac1n\cdot1+\frac{n-1}{n}\left(1-\frac2{n-1}\right).
\]
For \(n\ge3\), both numbers on the right lie in \([0,1]\), and they are distinct. Strict convexity of \(u\mapsto u^t\) for \(t\ge2\), by Jensen's inequality, implies \(na<1+(n-1)b\). This proves the strict sign claim without requiring a normal approximation.

To obtain the variances, the two-coordinate avoidance probability is \(\Pr(N_i=N_j=0)=a\). Therefore \(\operatorname{Cov}(\mathbf1_{\{N_i>0\}},\mathbf1_{\{N_j>0\}})=a-p^2\) for distinct coordinates. Moreover \(\mathbb E[(-1)^{N_i+N_j}]=d\), so the covariance of the two odd-parity indicators is \((d-a^2)/4\). Summing diagonal and off-diagonal terms gives the exact formulas above. Nondegeneracy follows by comparing a path with all flips at one coordinate and a path with two distinct flipped coordinates (for arbitrary \(t\ge2\), appropriate parity patterns exist, and \(D\) is nonconstant); equivalently, the enumerated indicator covariances yield positive variances. More explicitly, \(H\) assumes distinct values for every \(t\ge2\): for even \(t\), compare all flips on one coordinate (distance zero) to one flip on each of two coordinates followed by pairs; for odd \(t\ge3\), compare all flips on one coordinate (distance one) to a three-odd-coordinate path (distance three).

For the linear regime, put \(c_n=t/n\to c>0\). Uniform first-order binomial expansions for bounded \(c_n\) give
\[
\begin{aligned}
p&=e^{-c_n}[1-c_n/(2n)+O(n^{-2})],\\
a&=e^{-2c_n}[1-2c_n/n+O(n^{-2})],\\
b&=e^{-2c_n}[1-4c_n/n+O(n^{-2})],\\
d&=e^{-4c_n}[1-8c_n/n+O(n^{-2})].
\end{aligned}
\]
Substitution yields the three normalized limits
\[
\begin{aligned}
\frac1n\operatorname{Cov}(D,H)&\longrightarrow\frac{e^{-c}}2[1-(1+2c)e^{-2c}],\\
\frac1n\operatorname{Var}(D)&\longrightarrow e^{-c}-(1+c)e^{-2c},\\
\frac1n\operatorname{Var}(H)&\longrightarrow\tfrac14[1-(1+4c)e^{-4c}].
\end{aligned}
\]
The variance limits are strictly positive since \(e^c>1+c\) and \(e^{4c}>1+4c\). Their ratio proves \(\rho(c)\). Taylor expansion at zero gives the three bracket factors \(2c^2\), \(c^2/2\), and \(8c^2\), respectively; at infinity they approach one, \(e^{-c}\), and one. This proves the limits of \(\rho\).

Finally, assume \(t/(n\log n)\to\beta>0\). Here \(p=n^{-\beta+o(1)}\) and \(t=O(n\log n)\). Taylor expansion of the logarithms shows \(a=p^2[1+O(t/n^2)]\) and \(b=a[1+O(t/n^2)]\). Thus
\[
(n-1)a-np^2=O(p^2[1+t/n])=o(p),\quad
1+(n-1)b-na=1+o(1),
\]
and \(1+(n-1)d-na^2=1+o(1)\). Therefore \(\operatorname{Var}(D)\sim np\), \(\operatorname{Var}(H)\sim n/4\), and \(\operatorname{Cov}(D,H)\sim np/2\). Dividing proves \(\operatorname{Corr}\sim\sqrt p\). Taking logarithms gives the exponent \(-\beta/2\). These deductions require neither independence of coordinate occupancies nor a mixing-time assertion.

## Verification

`verify.py` enumerates all \(n^t\) sequences for 28 explicitly bounded parameter pairs with \(3\le n\le7\), \(2\le t\le7\), and \(n^t\le120000\). It compares all five exact moment identities using rational arithmetic, also checking their positivity. It separately evaluates ten linear-scale comparisons and three logarithmic-scale comparisons numerically. The finite checks do not establish the infinite theorem; that follows from the analytic arguments above. Execute `python3 verify.py` with standard-library Python 3.

## Relationship to prior work

The exact *numerator* covariance is an algebraic corollary of the full fixed-frequency occupancy covariance formula recorded in the earlier published-finding corpus finding *A one-switch covariance law for occupancy richness and frequency counts*: sum that formula over odd frequencies. We therefore do **not** claim originality for the finite cross-covariance formula or its direct Jensen sign corollary in isolation. The contribution assessed here is the joint-normalization and explicit two-regime correlation crossover, including the nonconstant \(ho(c)\) and the \(n\log n\) polynomial decay. Those require a parity variance and triangular-array asymptotics not asserted by the older single-frequency covariance theorem.

The occupancy model and its variance are classical; Bogachev, Gnedin and Yakubovich (2006) analyze occupied-box variances in an infinite-urn setting. Durieu and Wang (2015) discuss *both* occupied- and odd-occupied-box processes and related bit-flip walks, chiefly under infinite-urn regular-variation conditions. Diaconis, Graham and Morrison (1990) investigate high-dimensional hypercube random-walk mixing, using a walk with holding steps. These results motivate the comparison but their inspected statements do not provide the explicit finite equal-probability *normalized* correlation and its two scaling regimes derived here. An earlier explicit crossover or a general theorem implying it could still exist; priority is not guaranteed.

## Limitations

The claim is limited to independent uniform coordinate choices and exactly one flip per step. It does not concern the number of distinct *vertices* visited, nonuniform coordinate probabilities, or a lazy hypercube walk. No assertion of a central limit theorem, strictly monotone correlation in time, independence, or a mixing-time cutoff is made. Historical publication priority remains uncertain, particularly because some older bit-flipping works were accessible only through abstracts.

## References

- L. V. Bogachev, A. V. Gnedin, and Yu. V. Yakubovich. *On the variance of the number of occupied boxes* (submitted 18 September 2006), arXiv:math/0609498, https://arxiv.org/abs/math/0609498.
- O. Durieu and Y. Wang. *From infinite urn schemes to decompositions of self-similar Gaussian processes* (submitted 6 August 2015), arXiv:1508.01506, https://arxiv.org/abs/1508.01506.
- P. Diaconis, R. L. Graham, and J. A. Morrison. *Asymptotic analysis of a random walk on a hypercube with many dimensions*, Random Structures & Algorithms 1 (1990), 51–72, https://doi.org/10.1002/rsa.3240010105.
- A. Muratov and S. Zuyev. *Bit flipping and time to recover*, Journal of Applied Probability 53 (2016), 650–666, https://doi.org/10.1017/jpr.2016.32.
