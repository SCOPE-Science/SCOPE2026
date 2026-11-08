# Sharp Poisson approximation for missing vertices of random complete-bipartite subtrees

## Finding

Let \(S\) be selected uniformly from all nonempty subtrees of \(K_{a,b}\), including singleton trees. Let \(N=a+b\), and \(Z=N-|V(S)|\). In particular, choosing a subtree uniformly does **not** mean choosing its vertex set uniformly. Set \(\tau=a^{b-1}b^{a-1}\), let \(s_{N-k}\) be the number of subtrees with \(N-k\) vertices, and write \(R_k=s_{N-k}/\tau\). Use the prelimit parameter

\[
\theta=R_1=\frac ab\left(1-\frac1a\right)^{b-1}+\frac ba\left(1-\frac1b\right)^{a-1}.
\]

**Theorem.** For the balanced sequence \(a=b=m\to\infty\),

\[
d_{\mathrm{TV}}\big(\mathcal L(Z_{m,m}),\operatorname{Pois}(\theta)\big)=\Theta(m^{-2}),\qquad
R_2-\frac{\theta^2}{2}=\frac{7}{2e^2m^2}+O(m^{-3}).
\]

For arbitrary proportional unbalanced sequences \(a+b=N\to\infty\), \(a/N\to\alpha\in(0,1)\setminus\{1/2\}\), \(b/N\to\beta=1-\alpha\),

\[
d_{\mathrm{TV}}\big(\mathcal L(Z_{a,b}),\operatorname{Pois}(\theta)\big)=\Theta(N^{-1}),
\]

\[
N\left(R_2-\frac{\theta^2}{2}\right)\longrightarrow
-\frac12\left(\frac{e^{-\beta/\alpha}}{\beta}-\frac{e^{-\alpha/\beta}}{\alpha}\right)^2<0.
\]

Thus equality of the bipartition sizes cancels the first-order Poisson error in total variation, and the sign of the second-coefficient residual reverses. These are asymptotics of the **prelimit-matched** Poisson parameter, not claims about exact equality of distributions.

## Assumptions and scope

Graphs are finite, unweighted and simple, \(a,b\ge2\), and a subtree means any connected acyclic subgraph with its chosen edges, not necessarily induced. Total variation is \(d_{\mathrm{TV}}(P,Q)=\frac12\sum_{k\ge0}|P(k)-Q(k)|\). Big-O constants for the proportional case may depend on a fixed compact subset of \((0,1)\) containing the limiting part ratio. Both stated lower bounds refer to sufficiently large parameter values.

## Proof

**1. Exact coefficients (known counting starting point).** For \(x,y\ge1\), the complete-bipartite tree count is \(\tau(x,y)=x^{y-1}y^{x-1}\). Also define \(\tau(1,0)=\tau(0,1)=1\), and give other disconnected one-part vertex sets tree count zero. Choosing the deleted vertices in each part gives

\[
s_{N-k}=\sum_{i=\max(0,k-b)}^{\min(a,k)}\binom ai\binom b{k-i}\,\tau(a-i,b-k+i).
\]

This coefficient enumeration is classical and is **not** claimed as new; see Chin, Gordon, MacPhee and Vincent (2018). Put \(A=(a/b)(1-1/a)^{b-1}\), \(B=(b/a)(1-1/b)^{a-1}\), so \(\theta=A+B\). The exact second ratio is

\[
R_2=\frac{a(a-1)}{2b^2}\left(1-\frac2a\right)^{b-1}
+\left(1-\frac1a\right)^{b-2}\left(1-\frac1b\right)^{a-2}
+\frac{b(b-1)}{2a^2}\left(1-\frac2b\right)^{a-1}.
\]

**2. Balanced expansion and cancellation.** For any fixed deleted counts \(i,j\ge0\) with \(k=i+j\), the summand of \(R_k\), when \(k\le m^{1/9}\), equals

\[
W_{i,j}=\frac{e^{-k}}{i!j!}\left(1+\frac{3k/2-(i-j)^2}{m}+O\left(\frac{(k+1)^4}{m^2}\right)\right),
\]

uniformly in \(i,j\). This follows by taking logarithms of the binomial factors and powers \((1-i/m)^{m-j-1}(1-j/m)^{m-i-1}\); the cubic and higher log terms are uniformly bounded by \(O((k+1)^4/m^2)\) in this range. Summing over \(i+j=k\) uses the binomial identity \(\sum_i\binom ki(2i-k)^2=2^k k\) and gives

\[
R_k=\frac{(2/e)^k}{k!}\left(1+\frac{k}{2m}+O\left(\frac{(k+1)^4}{m^2}\right)\right).
\]

Meanwhile, \(\theta=2(1-1/m)^{m-1}=(2/e)(1+1/(2m)+O(m^{-2}))\). Thus, for the same range,

\[
\left|R_k-\frac{\theta^k}{k!}\right|\le \frac{C^k(k+1)^4}{k!\,m^2}
\]

for an absolute constant \(C\). Direct expansion of the exact \(R_2\) identity, or one more order of this logarithmic expansion, gives \(R_2-\theta^2/2=7/(2e^2m^2)+O(m^{-3})\).

**3. Unbalanced expansion.** Set \(\alpha_N=a/N\), \(\beta_N=b/N\), with both bounded below by a positive constant. With \(A_0=(a/b)e^{-b/a}\) and \(B_0=(b/a)e^{-a/b}\), uniformly for \(k\le N^{1/9}\) and deleted counts \(i+j=k\), the exact-count summand obeys

\[
W_{i,j}=\frac{A_0^i B_0^j}{i!j!}\left(1+O\left(\frac{(k+1)^2}{N}\right)\right).
\]

Consequently \(\sum_{k\le N^{1/9}}|R_k-\theta^k/k!|=O(N^{-1})\). Expanding just the exact two-deletion formula and subtracting \(\theta^2/2\) yields

\[
N\left(R_2-\frac{\theta^2}{2}\right)
=-\frac12\left(\frac{e^{-\beta_N/\alpha_N}}{\beta_N}-\frac{e^{-\alpha_N/\beta_N}}{\alpha_N}\right)^2+O(N^{-1}).
\]

Its limit is nonzero when \(\alpha\ne\beta\): writing \(x=\alpha/\beta\), equality would require \(\log x+x-1/x=0\), and this strictly increasing function has its only positive root at \(x=1\).

**4. Uniform coefficient tails.** Let \(\delta=\min(a,b)\ge cN\) for some fixed \(c>0\). Every subtree omitting \(k\) vertices has at least \(k(\delta-k+1)\) edges by which one deleted vertex can be attached. Conversely, each larger tree has at most \(N-k+1\) possible one-leaf deletions. Double counting yields

\[
\frac{s_{N-k}}{s_{N-k+1}}\le\frac{N-k+1}{k(\delta-k+1)},\quad
R_k\le\frac{N^k}{k!(\delta-k+1)^k}\le\frac{(2/c)^k}{k!}
\quad(1\le k\le\delta/2).
\]

For \(L=\lfloor\delta/2\rfloor\), every smaller subtree extends to a subtree with exactly \(N-L\) vertices, and an \((N-L)\)-vertex tree contains at most \(2^{N-L}\) subtrees. Therefore

\[
\sum_{k\ge L}R_k\le 2^N R_L=o(N^{-M})\qquad\text{for every fixed }M>0.
\]

The same factorial-tail estimate handles the Poisson comparison. Summing the coefficient expansions proves \(\sum_kR_k=e^\theta+O(m^{-2})\) in the balanced case, respectively \(e^\theta+O(N^{-1})\) in the unbalanced case. Because \(\Pr(Z=k)=R_k/\sum_jR_j\), this proves the two total-variation **upper** bounds.

**5. Sharp lower bounds.** For any distribution with \(p_0>0\), define \(\Phi(p)=p_2/p_0-\tfrac12(p_1/p_0)^2\). It vanishes for every Poisson law. Since both distributions under consideration have \(p_0\) bounded away from zero and their first three masses bounded, \(\Phi\) is uniformly Lipschitz near the two laws. Here \(\Phi(\mathcal L(Z))=R_2-\theta^2/2\); the nonzero asymptotic expressions from steps 2–3 force total-variation lower bounds of orders \(m^{-2}\) and \(N^{-1}\), completing the proof.

## Verification

The standalone standard-library checker `verify.py` reconstructs the bipartite subtree coefficients independently by enumerating connected acyclic edge sets on small graphs; it also checks the exact \(R_1,R_2\) algebra using rational arithmetic for many parameters and numerically tests the two leading asymptotic residual constants. Running `python verify.py` gives `VERIFY_OK 310 finite and asymptotic checks`. Finite checks corroborate, but do not establish, the uniform asymptotic bounds proved above.

## Relationship to prior work

Chin, Gordon, MacPhee and Vincent (2018), Proposition 3.1, explicitly enumerate subtrees of complete bipartite graphs, and their results already include the balanced spanning-subtree limit. Wagner (2019) develops general subtree-count bounds for dense graphs. Wagner and Wang (2026), Theorem 2, give a general dense-graph Poisson approximation with a coarse error term, but not this sharp \(m^{-2}\) versus \(N^{-1}\) rate distinction, its second-coefficient signs, or the cancellation analysis. The claim is an asymptotic refinement of known exact enumerations, **not a new subtree-count formula or the first Poisson limit**.

## Limitations

Only proportional part sizes are analyzed; extreme imbalance and uniform estimates across the balanced/unbalanced transition are not claimed. The optimal comparison uses the varying prelimit parameter \(\theta=R_1\), rather than a fixed limiting parameter. Earlier unpublished or differently indexed treatments may contain equivalent expansions; priority is not independently certified. Computational checks cover finite examples only. There has been no independent mathematical audit.

## References

- Chin, Gordon, MacPhee and Vincent, *Subtrees of graphs* (2018), Proposition 3.1, https://doi.org/10.1002/jgt.22359 ; accessible full text https://www.researchgate.net/publication/324905745_Subtrees_of_graphs .
- Wagner, *On the number of subtrees in graphs with large minimum degree* (2019), https://arxiv.org/abs/1910.07349 .
- Wagner and Wang, *Subtrees in dense graphs* (2026), Theorem 2, https://arxiv.org/html/2605.03583v1 .
