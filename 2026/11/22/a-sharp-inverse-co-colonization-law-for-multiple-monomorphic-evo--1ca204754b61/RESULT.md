# A sharp inverse-co-colonization law for multiple monomorphic evolutionary stable states

## Finding

In the structured Gaussian replicator ensemble of Nassor, Biermé, Herniou and Madec [1], the number of **monomorphic** evolutionary stable states admits an exact expectation at every interaction ratio, an exact binomial law at zero ratio, and a sharp large-ratio expansion for its entire zero/one/multiple trichotomy. In particular, for each fixed integer \(N\ge 2\), the probability of at least two monomorphic ESSs is
\[
\Pr\{S_{\mu}\ge2\}=\frac{\binom N2}{\sqrt 2\,\pi\,4^{N-2}}\frac1\mu+O_N(\mu^{-2}),\qquad\mu\to\infty.
\]
Thus the residual chance of two alternative one-strain endpoints decreases at a precise inverse-rate scale, even though the leading antisymmetric limit rules out such alternatives entirely.

## Assumptions and scope

Fix an integer \(N\ge2\) and a real parameter \(\mu\ge0\). Let \((\alpha_{ij})_{1\le i,j\le N}\) be independent standard Gaussian random variables. The payoff, with row \(i\) interpreted as mutant and column \(j\) as resident, is
\[
\Lambda_{ij}=(1+\mu)\alpha_{ji}-\mu\alpha_{ij}-\alpha_{jj},\quad i\ne j,\qquad\Lambda_{ii}=0.
\]
On the probability simplex, consider \(\dot z_i=z_i[(\Lambda z)_i-z^{\mathsf T}\Lambda z]\). A pure state \(e_j\) is a strict ESS exactly when \(\Lambda_{ij}<0\) for all \(i\ne j\), almost surely; the continuous law makes all equality cases null. Write \(S_{\mu}=\sum_{j=1}^N\mathbf 1_{\{e_j\text{ is an ESS}\}}\). The count excludes all mixed-support ESSs. All limits keep \(N\) fixed.

Set \(v_\mu=1+2\mu+2\mu^2\), let \(Z\sim\mathcal N(0,1)\), and let \(\Phi\) and \(\phi\) denote the standard Gaussian distribution and density. Then
\[
\mathbb E S_\mu=N\,\mathbb E\bigl[\Phi(Z/\sqrt{v_\mu})^{N-1}\bigr]. \tag{1}
\]
At \(\mu=0\), the **full** count law is \(S_0\sim\operatorname{Binomial}(N,1/N)\). For \(N\ge3\), expression (1) is strictly decreasing for \(\mu\ge0\) and tends to \(N2^{-(N-1)}\); for \(N=2\), its value is constantly one.

With
\[
C_N=\frac{\binom N2}{\sqrt2\,\pi\,4^{N-2}},\qquad q_N=\frac{N}{2^{N-1}},
\]
the sharp trichotomy is
\[
\begin{aligned}
\Pr(S_\mu\ge2)&=C_N\mu^{-1}+O_N(\mu^{-2}),\\
\Pr(S_\mu=0)&=1-q_N+C_N\mu^{-1}+O_N(\mu^{-2}),\\
\Pr(S_\mu=1)&=q_N-2C_N\mu^{-1}+O_N(\mu^{-2}),\\
\Pr(S_\mu\ge3)&=O_N(\mu^{-2}).
\end{aligned}\tag{2}
\]
Consequently \(S_\mu\) converges in law to a Bernoulli random variable with success probability \(q_N\), the probability that a random antisymmetric tournament has a unique vertex that defeats every other vertex. Formula (2) is not a statement about the total number of all-support ESSs.

## Proof

**Pure-state ESS test and one-point law.** For the pure resident \(e_j\), every possible invader's invasion fitness is \(\Lambda_{ij}\), and strict negativity for all invading types is equivalent to strict ESS at \(e_j\). Condition on \(D_j=\alpha_{jj}=d\). The \(N-1\) random variables \((1+\mu)\alpha_{ji}-\mu\alpha_{ij}-d\) are independent Gaussian variables of mean \(-d\) and variance \((1+\mu)^2+\mu^2=v_\mu\). Their simultaneous negativity has conditional probability \(\Phi(d/\sqrt{v_\mu})^{N-1}\), proving (1) by exchangeability.

At \(\mu=0\), the event that \(e_j\) is an ESS says that \(\alpha_{jj}\) strictly exceeds the other \(N-1\) entries of row \(j\). Each row has exactly one uniformly distributed maximum position, and distinct rows are independent. Therefore the ESS indicators are independent Bernoulli variables with probability \(1/N\), proving the binomial law.

To verify strict monotonicity, define \(m=N-1\) and \(F(t)=\mathbb E\Phi(tZ)^m\). Gaussian integration by parts gives, for \(t>0\),
\[
F'(t)=\frac{m(m-1)t}{1+t^2}\,\mathbb E\left[\phi(tZ)^2\Phi(tZ)^{m-2}\right].\tag{3}
\]
When \(m\ge2\), this is positive. Since \(t=v_\mu^{-1/2}\) decreases strictly for positive \(\mu\), the expectation decreases strictly. The case \(m=1\) follows from \(\Phi(tZ)+\Phi(-tZ)=1\). As \(t\to0\), \(F(t)\to2^{-m}\). Its first derivative vanishes at zero, and its second derivative is bounded near zero, yielding \(\Pr(e_j\text{ ESS})=2^{-(N-1)}+O_N(\mu^{-2})\).

**Exact two-resident overlap representation.** Fix distinct \(i,j\). Put \(U=(\alpha_{ij}+\alpha_{ji})/2\), \(V=(\alpha_{ij}-\alpha_{ji})/2\), \(L=1+2\mu\), and \(D_i=\alpha_{ii}\), \(D_j=\alpha_{jj}\). The four variables are independent except for the deterministic definitions, and \(V\sim\mathcal N(0,1/2)\). Simultaneously having \(e_i\) and \(e_j\) as ESSs imposes the interval
\[
\frac{U-D_j}{L}<V<\frac{D_i-U}{L}.
\]
This interval is nonempty precisely if \(W=D_i+D_j-2U>0\). Let \(m=N-2\). Conditional on the four variables, the invader inequalities for outsiders of \(i\) and \(j\) concern disjoint Gaussian entries, and their probability is
\(\Phi(D_i/\sqrt{v_\mu})^m\Phi(D_j/\sqrt{v_\mu})^m\). Hence the **exact** pair probability is
\[
\begin{split}
P_{ij}(\mu)=\mathbb E\Big[&\big\{\Phi(\sqrt2(D_i-U)/L)-\Phi(\sqrt2(U-D_j)/L)\big\}_{+}\\
&\quad\times\Phi(D_i/\sqrt{v_\mu})^{N-2}\Phi(D_j/\sqrt{v_\mu})^{N-2}\Big].
\end{split}\tag{4}
\]
Here \(\{a\}_{+}=\max(a,0)\). Because the density of \(V\) at zero is \(1/\sqrt\pi\), a Taylor expansion of the Gaussian CDF (with an integrable quadratic error) gives
\[
P_{ij}(\mu)=\frac{4^{-(N-2)}}{\sqrt\pi L}\,\mathbb E[W_+]+O_N(L^{-2}).
\]
Since \(D_i,D_j\sim\mathcal N(0,1)\), \(U\sim\mathcal N(0,1/2)\) independently, \(W\sim\mathcal N(0,4)\) and \(\mathbb E W_+=\sqrt{2/\pi}\). Thus
\[
P_{ij}(\mu)=\frac{\sqrt2}{\pi\,4^{N-2}(1+2\mu)}+O_N(\mu^{-2})=\frac{1}{\sqrt2\,\pi\,4^{N-2}\mu}+O_N(\mu^{-2}).\tag{5}
\]
All errors are for fixed \(N\): the Gaussian CDF has bounded first and second derivatives and the Gaussian factors in (4) have finite moments of every order.

**Triple intersections, counting, and the limit.** Suppose three distinct vertices \(i,j,k\) are pure ESSs. Apply the preceding mutual-invasion interval constraint to the two pairs \((i,j)\) and \((i,k)\). Conditional on diagonals and symmetric pair entries, their antisymmetric contrasts are independent Gaussians. The probability of each interval is at most \(W_+/(\sqrt\pi L)\); expectations of products are finite by Gaussian moments. Hence the probability of this triple event is \(O_N(L^{-2})\), uniformly over the finitely many triples. The same bound controls any intersection of at least three pure-ESS events.

Inclusion-exclusion, (5), and \(\Pr(e_i\text{ ESS})=2^{-(N-1)}+O_N(\mu^{-2})\) yield all four formulas (2). In the antisymmetric limit, each unordered pair selects a random winner independently; at most one vertex can defeat all others, and its probability is \(N2^{-(N-1)}\), confirming the Bernoulli limit. This finishes the proof.

## Verification

A standalone script `check_pure_ess.py` reconstructs the signs directly from independent Gaussian interaction matrices, compares numerical Gaussian quadrature with (1), checks the exact two-strain bivariate normal orthant formula, and compares finite-ratio multiplicities with (2). It uses a deterministic random seed and prints its diagnostics. Those finite trials check implementation only; the theorem, including every fixed-\(N\) asymptotic, is established by the analytic steps above.

## Relationship to prior work

Nassor et al. [1, §§4.2–4.3, Eq. (22), Figs. 15–16] specify exactly this structured Gaussian replicator and numerically report that larger co-colonization ratio \(\mu\) strongly reduces ESS multiplicity; their results concern ESSs on all supports and do not state a monomorphic closed-form law or a sharp inverse-ratio constant. Madec and Gjini [2] develop the co-colonization invasion structure and its antisymmetric limit, without the fixed-\(N\) Gaussian pure-ESS distribution. Hart, Rinott and Weiss [3] study ESSs in a different random-game ensemble with independently distributed game payoffs, not this Gaussian co-colonization matrix. Chawanya and Tokita [4] concern high-dimensional antisymmetric replicator systems; the accessible abstract does not supply the finite-ratio rare-pair constant in (2). The formula for a random tournament's unique universal winner is classical and is not claimed as new. The contribution is the **joint** exact finite-ratio expectation and sharp nonzero inverse-ratio rare-multiplicity correction for this specific correlated ensemble.

## Limitations

The analysis is annealed over independent Gaussian interactions, keeps \(N\) fixed as \(\mu\to\infty\), and treats only monomorphic strict ESS states. In particular, \(\Pr(S_\mu=0)\) does **not** mean that no mixed ESS or dynamically stable state exists. It does not characterize the full all-support ESS count, population-size-uniform remainders, non-Gaussian interactions, empirical estimation uncertainty, or real biological infection outcomes. An equivalent specialized result in literature not recovered by the inspected sources remains a historical-priority risk. No independent mathematical audit is claimed.

## References

1. H. Nassor, H. Biermé, E. Herniou, and S. Madec, *A system-centered probabilistic formalism linking multiple equilibria and biodiversity in ecological and evolutionary models*, arXiv:2609.17232v1 (first public posting 2026-09-15), https://arxiv.org/abs/2609.17232.
2. S. Madec and E. Gjini, *The ratio of single to co-colonization is key to complexity in interacting systems with multiple strains*, Ecology and Evolution 11 (2021), doi:10.1002/ece3.7259, https://pmc.ncbi.nlm.nih.gov/articles/PMC8258234/.
3. S. Hart, Y. Rinott, and B. Weiss, *Evolutionarily Stable Strategies of Random Games*, 2008, arXiv:0801.3353, https://arxiv.org/abs/0801.3353.
4. T. Chawanya and K. Tokita, *Large-dimensional replicator equations with antisymmetric random interactions*, Journal of the Physical Society of Japan 71 (2002), doi:10.1143/JPSJ.71.429, https://doi.org/10.1143/JPSJ.71.429 (abstract consulted).
