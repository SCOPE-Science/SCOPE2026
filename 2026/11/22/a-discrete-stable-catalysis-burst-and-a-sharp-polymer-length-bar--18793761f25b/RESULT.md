# A discrete-stable catalysis burst and a sharp polymer-length barrier in Pareto autocatalysis

## Finding

In a heavy-tailed, forward-ligation random polymer reaction network, the first catalysis events confined to short polymers have an exact **discrete-stable critical law**. The critical length has a logarithmic correction, not merely a linear fraction of the ambient maximum length. Moreover, in a parameter regime where at least one reflexively autocatalytic and food-generated (RAF) set exists with probability tending to one, every RAF nevertheless requires a polymer longer than the subcritical length cutoff.

Write the alphabet size as \(\kappa\ge2\), the Pareto index as \(0<\alpha<1\), and the global catalytic intensity as \(\lambda_n=N_n^{-\beta}\), where \(0<\beta<(1-\alpha)/\alpha\). Define
\[
\theta=\frac{\alpha(1+\beta)}{1+\alpha},\qquad
b_n=\theta n-\frac{\alpha}{1+\alpha}\log_\kappa n,
\qquad
C_{\kappa,\alpha,\beta}
=\Gamma(1-\alpha)\theta^\alpha
(\kappa-1)^{\alpha\beta-1}\kappa^{1-\alpha\beta}.
\]
Then \(0<\theta<1\). For any sequence of integral cutoffs \(\ell_n\) with \(\ell_n-b_n\) bounded, the number of short-molecule-to-short-reaction catalytic incidences has probability-generating function
\[
\mathbb E[z^{E_{n,\ell_n}}]
=\exp\{-C_{\kappa,\alpha,\beta}
\kappa^{(1+\alpha)(\ell_n-b_n)}(1-z)^\alpha\}+o(1),\quad 0\le z\le1.
\]
The error is uniform for each fixed \(z\) and bounded cutoff offset. Because cutoffs are integers, the offset may oscillate; an unconditional fixed-law limit is **not** asserted. Along subsequences where the offset tends to \(c\), the limit is a compound Poisson variable with intensity \(C_{\kappa,\alpha,\beta}\kappa^{(1+\alpha)c}\) and Sibuya\((\alpha)\) positive integer marks. The number of active short catalysts converges to a Poisson variable with the same intensity. The mark distribution has probability-generating function \(1-(1-z)^\alpha\), hence finite-sample bursts can have infinite-mean *limiting* marks, despite all finite counts being bounded.

For any \(h_n\to\infty\) with \(h_n=o(n)\), let \(\ell_n^-=\lfloor b_n-h_n\rfloor\), \(\ell_n^+=\lfloor b_n+h_n\rfloor\). The probability of even one short catalytic incidence tends to zero at \(\ell_n^-\) and to one at \(\ell_n^+\). Consequently, with probability tending to one, at least one RAF exists but **every** RAF uses a molecule of length greater than \(\ell_n^-\). This is a necessary length lower bound, not a sufficient condition for an RAF at \(\ell_n^+\).

## Assumptions and scope

For each positive integer \(n\), let \(X_n\) consist of all nonempty words over an alphabet of size \(\kappa\), with word length at most \(n\). Its cardinality and the number of ordered forward ligation reactions are
\[
N_n=\sum_{j=1}^n\kappa^j,
\qquad
R_n=\sum_{j=2}^n(j-1)\kappa^j.
\]
A forward reaction concatenates nonempty words \(u,v\) into \(uv\) of length at most \(n\). Set a fixed food length \(t\ge1\), so food consists of words of length at most \(t\). For each \(x\in X_n\), independently sample \(W_x\) with \(\Pr(W_x>w)=w^{-\alpha}\) for \(w\ge1\). Conditional on the weights, molecule–reaction catalytic indicators are mutually independent and
\[
\Pr\{x\text{ catalyzes }r\mid W_x\}
=1-\exp(-\lambda_nW_x/N_n),
\qquad \lambda_n=N_n^{-\beta}.
\]
This is the diffuse reaction-independent kernel of Kim and Sönmez (2026), specialized to the forward-reaction system. No cleavage reactions, spatial restrictions, chemical kinetics, or correlation of weights between molecule types are included.

For an integer cutoff \(2\le\ell\le n\), let \(E_{n,\ell}\) count catalytic pairs \((x,r)\) with \(x\in X_\ell\) and \(r\) a forward ligation reaction of total product length at most \(\ell\). For each \(x\in X_\ell\), let \(J_x\) count its such reactions, and put \(K_{n,\ell}=\sum_{x\in X_\ell}\mathbf1_{\{J_x>0\}}\). This statistic counts *all potential* short reaction incidences, not only reactions belonging to an RAF.

For completeness, a nonempty forward-reaction subset is an RAF if each reaction is catalyzed by some molecule in its food closure and its reactants can be generated from the food using those reactions. All molecule lengths of an RAF mean the food closure of that reaction subset (equivalently, all reactants, products and food catalysts used in its RAF property); the lower bound addresses the maximum length among them.

## Proof

**1. A single-molecule rare-burst transform.** Let \(R=R_\ell\), \(N=N_n\), \(u=\lambda_nR/N\), and write \(h_{R,u}(z)=\mathbb E[z^{J_x}]\). Independence conditional on \(W_x\) yields
\[
J_x\mid W_x\sim\operatorname{Bin}\bigl(R,1-e^{-uW_x/R}\bigr),
\quad
h_{R,u}(z)=\mathbb E\bigl[z+(1-z)e^{-uW_x/R}\bigr]^R.
\]
Since the Pareto density is \(\alpha w^{-\alpha-1}\) on \([1,\infty)\), the exact substitution \(v=uw\) gives
\[
\frac{1-h_{R,u}(z)}{u^\alpha}
=\alpha\int_u^\infty
\bigl[1-(z+(1-z)e^{-v/R})^R\bigr]
\,v^{-\alpha-1}\,dv.
\]
For \(R\to\infty\), the bracket tends pointwise to \(1-e^{-(1-z)v}\); it lies between zero and \(\min\{1,(1-z)v\}\). Since \(0<\alpha<1\), this bound is integrable against \(v^{-\alpha-1}\,dv\). Dominated convergence and integration by parts therefore give, for every \(0\le z\le1\),
\[
1-h_{R,u}(z)
\sim \Gamma(1-\alpha)(1-z)^\alpha u^\alpha
\quad\text{as }R\to\infty,\ u\to0,
\]
with the convention that at \(z=1\) both sides vanish exactly. The relevant triangular array satisfies \(u\to0\) automatically, since \(R_\ell\le R_n=O(nN_n)\) and \(\lambda_n n\to0\).

**2. The marked compound Poisson limit.** Independence of the weights and conditional catalysis fields for different molecules gives \(E_{n,\ell}=\sum_{x\in X_\ell}J_x\), a sum of independent identically distributed nonnegative integers. If \(\ell\to\infty\) and \(a_n=N_\ell u^\alpha\to a\in[0,\infty)\), then
\[
\mathbb E[z^{E_{n,\ell}}]=h_{R,u}(z)^{N_\ell}
\longrightarrow \exp\{-a\Gamma(1-\alpha)(1-z)^\alpha\}.
\]
The number of nonzero terms is exactly binomial with success probability \(q_{R,u}=1-h_{R,u}(0)\sim\Gamma(1-\alpha)u^\alpha\), and hence tends to Poisson\((a\Gamma(1-\alpha))\). Moreover, conditionally on a nonzero term,
\[
\mathbb E[z^{J_x}\mid J_x>0]
=\frac{h_{R,u}(z)-h_{R,u}(0)}{1-h_{R,u}(0)}
\longrightarrow 1-(1-z)^\alpha.
\]
The last generating function is that of a proper Sibuya distribution, with coefficients
\[
\Pr(Z=j)=\frac{\alpha\Gamma(j-\alpha)}{\Gamma(1-\alpha)\Gamma(j+1)},
\qquad j=1,2,\ldots.
\]
A finite set of independently marked rare active molecules therefore converges to the stated compound Poisson law. Its mean is not claimed finite; the finite prelimit counts are each bounded by \(R\).

**3. Exact logarithmic cutoff.** As \(m\to\infty\), elementary summation gives
\[
N_m\sim\frac{\kappa^{m+1}}{\kappa-1},\qquad
R_m\sim mN_m.
\]
Thus for \(\ell\sim\theta n\),
\[
N_\ell(\lambda_nR_\ell/N_n)^\alpha
\sim \ell^\alpha\,(\kappa-1)^{\alpha\beta-1}
\kappa^{1-\alpha\beta}
\kappa^{(1+\alpha)\ell-\alpha(1+\beta)n}.
\]
Substitute \(\ell=b_n+c_n\) with bounded \(c_n\). The power of \(n\) cancels precisely because the correction is \(-\alpha\log_\kappa(n)/(1+\alpha)\). This yields
\[
N_\ell u^\alpha
=\theta^\alpha(\kappa-1)^{\alpha\beta-1}
\kappa^{1-\alpha\beta}\kappa^{(1+\alpha)c_n}(1+o(1)),
\]
proving the stated law, including its lattice dependence. If \(c_n\to-\infty\) or \(+\infty\) while \(c_n=o(n)\), the same calculation gives \(N_\ell u^\alpha\to0\) or \(\infty\). For the zero-event probability, the exact formula is \(\Pr(E_{n,\ell}=0)=(1-q_{R,u})^{N_\ell}\); using \(q_{R,u}\sim\Gamma(1-\alpha)u^\alpha\) proves the sharp zero-one transition.

**4. A nonvacuous RAF length obstruction.** At the lower cutoff, with high probability there is no catalysis incidence between any molecule and forward reaction within \(X_{\ell_n^-}\). If an RAF had every molecule in its food closure of length at most \(\ell_n^-\), every reaction would be short and its required catalyst would also be short, a contradiction. Kim and Sönmez's Theorem 8, applied to this diffuse kernel, independently gives the existence of an RAF with probability approaching one because
\[
\lambda_n^\alpha N_n^{1-\alpha}
=N_n^{1-\alpha-\alpha\beta}\longrightarrow\infty.
\]
The union bound between these two probability-one events proves that RAFs exist but every RAF contains at least one molecule longer than the lower cutoff, with probability tending to one. The argument does not assert an RAF built solely from molecules shorter than the upper cutoff.

## Verification

An independent standalone standard-library script, `check.py`, reproduces the exact counts, evaluates the finite-network no-edge probabilities at the Pareto half-index by a separate one-dimensional integral, checks the logarithmic cutoff constants, and tests the Sibuya generating-function coefficients. These are **sanity checks**, not substitutes for the dominated-convergence and finite-RAF arguments above.

For example, at \(\kappa=2\), \(\alpha=\beta=1/2\), the critical fraction is \(\theta=1/2\) and the Poisson intensity prefactor is \(C=2.1078147305108117\ldots\). For \(n=60\) and \(\ell=28\), direct evaluation of the finite formula gives \(\Pr(E_{60,28}>0)\approx0.8504251761\). At the same offset formula the limiting expression is an approximation, not an exact finite probability.

## Relationship to prior work

Kim and Sönmez (2026), Theorem 8 and Section 3.3.4, establish the full-network heavy-tail RAF formation transition; their Theorem 5 studies heavy-tailed reaction degrees at a different catalysis normalization and fixed intensity; their Proposition 10 permits a single molecule to catalyze a whole RAF. Those results are retained as prior work. They do not state the short-polymer catalytic incidence distribution, its logarithmically centered threshold, or the resulting universal lower bound on the longest molecule in every RAF.

Hordijk and Steel (2016) examine variable and power-law *numbers* of reactions assigned to catalysts, with different, typically bidirectional reaction conventions; their existence and RAF-size results do not imply the present length-specific Pareto-weighted compound Poisson limit. Steel, Hordijk and Smith (2012) establish minimum RAF reaction-count lower bounds in another catalysis regime, not a sharp molecular-length cutoff for a vanishing-intensity diffuse Pareto kernel. Hordijk and Steel (2019) compare minimum ambient maximum polymer lengths needed for RAF formation in a constant-catalysis regime, a different question from fixed ambient length with power-law weighted catalyst activity.

The compound Poisson and Sibuya probability-generating-function constructions are classical. The proposed contribution is their *specific joint occurrence* in the heavy-tailed polymer catalysis model, the sharp logarithmic length window and the RAF length obstruction, not a new general limit theorem for rare random sums.

## Limitations

The incidence event is a necessary condition for a short-molecule RAF, not sufficient; upper critical-incidence onset does not establish a short RAF. The theorem does not find the actual minimum possible RAF length. It treats only independent Pareto molecular weights, reaction-independent diffuse compatibility, fixed food length and forward ligations. The law is asymptotic as maximal polymer length tends to infinity, and a single fixed lattice-shifted limit may not exist. An equivalent formulation may appear in classical random-polymer or regularly varying cluster literature not covered by the inspected sources. No laboratory origin-of-life claim or chemical-kinetics inference follows.

## References

1. J. Kim and E. Sönmez, *Can a self-sustaining chemical network emerge due to just a few catalysts?*, arXiv:2611.06033v1 (first public 2026-11-04), https://arxiv.org/abs/2611.06033 .
2. W. Hordijk and M. Steel, *Autocatalytic sets in polymer networks with variable catalysis distributions*, arXiv:1605.03919 (2016), https://arxiv.org/abs/1605.03919 .
3. M. Steel, W. Hordijk and J. Smith, *Minimal autocatalytic networks*, arXiv:1212.4450 (2012), https://arxiv.org/abs/1212.4450 .
4. W. Hordijk and M. Steel, *Molecular Diversity Required for the Formation of Autocatalytic Sets*, Life 9(1), 23 (2019), https://www.mdpi.com/2075-1729/9/1/23 .
