# Metastable geometric fixation and an exponential hierarchy at zero reinforcement

## Finding

For each integer \(n\ge2\), consider \(n\) candidates and \(n\) independent ballots per round. Begin with one vote for every candidate. At later rounds each ballot chooses uniformly among candidates receiving at least one vote in the preceding round; candidates that receive no votes never return. Write \(K_t\) for the number of supported candidates after round \(t\), with \(K_0=n\), and \(T_n=\inf\{t\ge0:K_t=1\}\).

Let \(G_n\) have the geometric law on positive integers with parameter \(q_n=2^{1-n}\). Then

\[
d_{\mathrm{TV}}(\mathcal L(T_n),\mathcal L(G_n))\le
\frac1{2^n-1}+2^{1-n}\sum_{k=3}^{n}\left(\frac{k}{k-1}\right)^n
=O((3/4)^n).
\]

Consequently \(T_n/2^{n-1}\) converges in law to a mean-one exponential random variable. Moreover, for every fixed integer \(r\ge2\),

\[
\mathbb E T_n=\sum_{k=2}^{r}\frac1k\left(\frac{k}{k-1}\right)^n
+O_r\left(\left(\frac{r+1}{r}\right)^n\right)
\qquad (n\to\infty).
\]

In particular,

\[
\mathbb E T_n=2^{n-1}+\frac13\left(\frac32\right)^n
+O\left(\left(\frac43\right)^n\right).
\]

There is also a complete exact finite-\(n\) probability-generating-function recursion given below. The geometric bound holds for any initial state with at least two active candidates, not only the all-singleton state. The asymptotic expectation expansion concerns the all-singleton initial state.

## Assumptions and scope

The update is synchronous: all \(n\) ballots are conditionally independent and each is uniform on the currently active candidate set. The state \(K_t\) is a number in \(\{1,\ldots,n\}\), is nonincreasing, and absorbs at \(1\). This is the *zero-reinforcement survivor-only endpoint*, defined directly by the positive-support weight \(\mu(x)=\mathbf1_{\{x>0\}}\); it is not the positive-exponent process with \(\mu(x)=x^\alpha\) for fixed \(\alpha>0\). In particular no assertion about fixed strictly positive exponents is made.

Let \({n\brace j}\) denote a Stirling number of the second kind, and \((k)_j=k(k-1)\cdots(k-j+1)\). For \(1\le j\le k\le n\), the support chain has exact kernel

\[
P_n(k,j)=\frac{(k)_j\,{n\brace j}}{k^n}.
\]

If \(F_{n,k}(z)=\mathbb E[z^{T_n}\mid K_0=k]\), then \(F_{n,1}(z)=1\) and, for \(2\le k\le n\),

\[
F_{n,k}(z)=\frac{z\sum_{j=1}^{k-1}P_n(k,j)F_{n,j}(z)}{1-zP_n(k,k)}
\qquad(0\le z\le1).
\]

This is an exact constructive description of every finite absorption-time law.

## Proof

**1. Exact support kernel.** For \(K_t=k\), the \(n\) ballots are independent uniform choices from \(k\) labels. The number of functions with image size \(j\) is \(\binom{k}{j}j!{n\brace j}=(k)_j{n\brace j}\), giving the kernel. At each \(k\ge2\), at least one candidate can disappear with positive probability, so eventual fixation has probability one. First-step conditioning yields the generating-function recursion.

**2. Time before two survivors.** Put \(\tau=\inf\{t:K_t\le2\}\). While \(K_t=k\ge3\), a particular candidate gets no next-round ballots with probability \((1-1/k)^n\). Thus the conditional exit probability from support level \(k\) is at least \((1-1/k)^n\); the process never revisits any support level after leaving it. Therefore

\[
\mathbb E\tau\le\sum_{k=3}^{n}\left(\frac{k}{k-1}\right)^n.
\]

At a level \(k\ge3\), the probabilities of jumping directly to support sizes \(1\) and \(2\) are respectively

\[
P_n(k,1)=\frac{k}{k^n},\qquad
P_n(k,2)=\frac{\binom{k}{2}(2^n-2)}{k^n}.
\]

Hence, conditional on a jump to \(\{1,2\}\), the chance of jumping to \(1\) is at most \(1/(2^n-1)\). Considering the first jump into \(\{1,2\}\) yields \(\Pr(K_\tau=1)\le1/(2^n-1)\).

**3. Geometric comparison.** With two candidates active, the next round fixes the process with probability \(q_n=2(1/2)^n\), independent of their current positive vote counts. By the strong Markov property, conditional on \(K_\tau=2\), the remaining duration is an independent \(G_n\). Couple an independent copy of \(G_n\) to every trajectory, including trajectories that jump directly to one survivor. On the latter event, the coupling can fail; elsewhere \(T_n=\tau+G_n\). For any nonnegative integer \(u\),

\[
d_{\mathrm{TV}}(\mathcal L(G_n+u),\mathcal L(G_n))
=1-(1-q_n)^u\le q_nu.
\]

Mixing over \(\tau\) and adding the shortcut event gives the displayed total-variation inequality. The sum of exit-time bounds is at most \((3/2)^n+n(4/3)^n=O((3/2)^n)\), so the error is \(O((3/4)^n)\). The exponential limit follows from \(q_nG_n\Rightarrow\operatorname{Exp}(1)\).

**4. Exact exponential hierarchy for the mean.** Let \(h_{n,k}=\Pr_n(\text{ever visit support level }k)\), and \(a_{n,k}=1-P_n(k,k)\) for \(2\le k\le n\). Each visited level has a geometric holding time of mean \(1/a_{n,k}\), so

\[
\mathbb E_nT_n=\sum_{k=2}^n\frac{h_{n,k}}{a_{n,k}}.
\]

Fix \(k\ge2\). For any \(\ell>k\), when next support is at most \(k\), the conditional probability that it is below \(k\) is bounded by

\[
\frac{\sum_{j=1}^{k-1}P_n(\ell,j)}{P_n(\ell,k)}
\le C_k\left(\frac{k-1}{k}\right)^n
\]

for sufficiently large \(n\). Indeed, \((\ell)_j/(\ell)_k\le1\) and the classical surjection bounds
\({n\brace j}\le j^n/j!\) and
\({n\brace k}\ge k^n(1-k((k-1)/k)^n)/k!\) give this uniformly over \(\ell>k\). Apply the estimate at the first entry into \(\{1,\ldots,k\}\) to get

\[
1-h_{n,k}=O_k\left(\left(\frac{k-1}{k}\right)^n\right).
\]

Inclusion-exclusion on empty cells gives, for each fixed \(k\),

\[
a_{n,k}=k\left(\frac{k-1}{k}\right)^n
\left[1+O_k\left(\left(\frac{k-2}{k-1}\right)^n\right)\right],
\]

where the bracket is exactly one at \(k=2\). Consequently

\[
\frac{h_{n,k}}{a_{n,k}}=\frac1k\left(\frac{k}{k-1}\right)^n+O_k(1).
\]

For the remaining levels \(k\ge r+1\), the exit-probability bound in Step 2 yields

\[
\sum_{k=r+1}^{n}\frac{h_{n,k}}{a_{n,k}}
\le\left(\frac{r+1}{r}\right)^n
+n\left(\frac{r+2}{r+1}\right)^n
=O_r\left(\left(\frac{r+1}{r}\right)^n\right).
\]

Combining the finite initial terms and tail proves the hierarchy. All bounds are uniform in the initial support level for Step 3; only the level-hitting estimate in Step 4 uses the all-\(n\)-active initialization.

## Verification

The supplied standard-library checker `check.py` computes Stirling-based transition probabilities as exact fractions, independently enumerates small complete ballot allocations, checks hitting and occupation recursions, checks shortcut and pre-bottleneck bounds, and compares a separate finite-horizon tail recursion with the explicit two-state geometric tail. It passed 2,501 assertions. Numerical instances of the expectation expansion are diagnostics, not the argument for its infinite asymptotic claim. Run `python3 check.py` from the package directory.

## Relationship to prior work

Benjamini, Cai, Chen, Gong and Li (2026) introduced the reinforced conclave process with strictly increasing weights and studied fixed \(\alpha>0\). Their results include exponentially long survival when \(0<\alpha<1\), and a linear-time regime at \(\alpha=1\). The present survivor-only \(\alpha=0\) rule is explicitly defined separately; no fixed-positive-\(\alpha\) conclusion is deduced from their theorem. Classical one-round occupancy theory supplies the Stirling-number transition kernel; iterating it with permanently inactive candidates is the additional stochastic operation. The claims here concern the multi-round absorption law and its complete exponential mean-time hierarchy rather than a one-round occupancy count.

## Limitations

This proves results only for the particular zero-reinforcement survivor-only process. Nothing is asserted for a fixed positive reinforcement exponent, for weights that allow a zero-count candidate to revive, or for nonuniform candidate selection. The classical occupancy kernel is not new. Historical uniqueness is conditional on accessible literature; a broader exact iterative-occupancy theorem not found in the searches might subsume the result. No independent mathematical audit has been performed.

## References

1. I. Benjamini, Z. Cai, G. Chen, S. Gong, Z. Li, *The Conclave Process*, arXiv:2607.22324 (first public version July 24, 2026), https://arxiv.org/abs/2607.22324 .
2. E. W. Weisstein, *Classical Occupancy Problem*, MathWorld, https://mathworld.wolfram.com/ClassicalOccupancyProblem.html .
3. N. Cancrini and G. Posta, *Mixing time for the Repeated Balls into Bins dynamics*, arXiv:2001.11246, https://arxiv.org/abs/2001.11246 . Its dynamics differ because allocation is to the fixed bin set.
