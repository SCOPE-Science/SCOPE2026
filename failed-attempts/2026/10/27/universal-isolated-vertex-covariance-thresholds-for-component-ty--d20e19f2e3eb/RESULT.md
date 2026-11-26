# Universal isolated-vertex covariance thresholds for component-type counts

## Finding
Fix \(n\ge3\), \(2\le k<n\), and \(0<p<1\). For an Erdős–Rényi graph \(G\sim G(n,p)\), write \(I\) for its isolated-vertex count. Define a component statistic
\[
T=\sum_{S\subseteq[n],\,|S|=k} w_S(G[S])\,\boldsymbol 1\{S\text{ is a connected component of }G\},
\]
where each \(w_S\) is a deterministic, nonnegative function of the induced graph on \(S\), and \(\mathbb ET>0\). Then
\[
\operatorname{Cov}(I,T)=\mathbb EI\,\mathbb ET\left(\frac{n-k}{n(1-p)^k}-1\right),\qquad \mathbb EI=n(1-p)^{n-1}.
\]
Thus the sign is strictly negative for \(p<p_{n,k}\), zero for \(p=p_{n,k}\), and strictly positive for \(p>p_{n,k}\), where
\[
p_{n,k}=1-\left(1-\frac{k}{n}\right)^{1/k}.
\]
The thresholds increase strictly with \(k\). The conclusion holds for **every** nonnegative internal component-type weight, including the indicators of individual connected motifs and of trees or unicyclic components.

The thresholds span distinct random-graph scales:
\[
\begin{aligned}
p_{n,k}&=\frac1n+\frac{k-1}{2n^2}+O_k(n^{-3})&&\text{when }k\text{ is fixed},\\
np_{n,k}&\longrightarrow\frac{-\log(1-\theta)}{\theta}&&\text{when }k/n\to\theta\in(0,1),\\
p_{n,n-1}&\sim\frac{\log n}{n}&&\text{as }n\to\infty.
\end{aligned}
\]
The sign thresholds concern covariances of possibly rare component counts; they are not thresholds for existence of those components.

## Assumptions and scope
Graphs are simple, undirected, labelled on \([n]\), with independent Bernoulli-\(p\) edges. A summand uses only the induced graph \(G[S]\) and the event that all \(k(n-k)\) cross-edges are absent; weights do not depend on outside edges. Nonnegativity and \(\mathbb ET>0\) ensure the covariance has the asserted sign. No large-\(n\) assumption is made for the exact identity. The cases \(k=1\) (self-covariance effects), \(k=n\) (no outside vertex), and edge probabilities at the endpoints are not covered.

## Proof
Put \(q=1-p\) and write \(T=\sum_S W_S\), with \(W_S=w_S(G[S])\boldsymbol1\{S\text{ forms a connected component}\}\). If \(v\in S\), the event \(W_S>0\) forces \(v\) to have positive degree, because \(k\ge2\); hence \(\mathbb E[\boldsymbol1\{v\text{ isolated}\}W_S]=0\).

If \(v\notin S\), the component event in \(W_S\) already forces all \(k\) edges from \(v\) to \(S\) absent. The remaining \(n-k-1\) edges from \(v\) to vertices outside \(S\) are independent of \(W_S\). Thus
\[
\mathbb E[\boldsymbol1\{v\text{ isolated}\}W_S]=q^{n-k-1}\mathbb EW_S.
\]
Summing first over \(v\) and then over \(S\) yields
\[
\mathbb E[IT]=(n-k)q^{n-k-1}\mathbb ET.
\]
Since \(\mathbb EI=nq^{n-1}\), subtraction and factorization give the stated covariance identity. For \(\mathbb ET>0\), its sign equals the sign of \((n-k)/n-q^k\). This quantity grows strictly with \(p\in(0,1)\), starts negative and ends positive, and vanishes uniquely when \(q^k=1-k/n\).

For strict ordering across component sizes, put \(t=k/n\) and \(f(t)=-\log(1-t)/t\). The threshold has the representation \(p_{n,k}=1-\exp(-f(t)/n)\). On \((0,1)\),
\[
f'(t)=\frac{t/(1-t)+\log(1-t)}{t^2}>0,
\]
because the numerator vanishes at zero and has derivative \(t/(1-t)^2>0\). Therefore \(p_{n,k}\) is strictly increasing in \(k\).

For fixed \(k\), expand \(k^{-1}\log(1-k/n)=-1/n-k/(2n^2)+O_k(n^{-3})\), then exponentiate. For \(k/n\to\theta\in(0,1)\), continuity of \(f\) and \(1-e^{-z/n}\sim z/n\) give the mesoscopic limit. Finally \(p_{n,n-1}=1-\exp(-\log n/(n-1))\sim (\log n)/n\).

## Verification
An independent graph-enumeration implementation in `verify.py` enumerates every labelled graph for \(n=3,4,5,6\) with exact rational Bernoulli weights at \(p=1/5,2/5,3/5\). It compares both the total size-\(k\) component count and tree-only size-\(k\) counts against the covariance identity: 60 exact equalities passed. Separate numerical monotonicity checks covered 123,753 adjacent threshold pairs for \(3\le n\le500\), with 24 fixed-\(k\) expansion checks. These finite tests are supplementary; the proof above supplies the universal conclusions. Run `python verify.py` using Python 3 standard library.

## Relationship to prior work
Bollobás, Janson and Riordan study the \(p\asymp1/n\) giant-component transition and fixed-size component frequencies, including Theorem 9.1, but not the present exact finite-size mixed-covariance threshold law. Ghosh, Goldstein and Raič establish concentration bounds for the number of isolated vertices, not covariance with counts of distinguished component types. Pittel's earlier tree-census work establishes a joint asymptotic Gaussian law for tree-component counts, with a model-dependent covariance function; it is a particularly important potential source of stronger implied fixed-size asymptotics. The present statement concerns finite \(n\), all \(k<n\), and arbitrary nonnegative internal component weights, with a universal monotone threshold. The available Pittel abstract was compared, but its full text was not accessible for a conclusive implication check. These distinctions do not establish historical uniqueness.

## Limitations
The result is specific to independent equal-probability edges. Signed or outside-dependent weights need not satisfy the sign conclusion. The covariance can be tiny when the counted component type is rare. The asymptotic locations do not describe variance, correlation, or distributional limits of these statistics. Historical priority is provisional, especially against the full tree-census covariance literature.

## References
- B. Bollobás, S. Janson, O. Riordan, *The phase transition in inhomogeneous random graphs*, arXiv:math/0504589 (first public preprint 2005-04-29), particularly Section 9 / Theorem 9.1.
- S. Ghosh, L. Goldstein, M. Raič, *Concentration of measure for the number of isolated vertices in the Erdős–Rényi random graph by size bias couplings*, arXiv:1106.0048 (first public preprint 2011-05-31), Sections 1–2.
- B. Pittel, *On tree census and the giant component in sparse random graphs*, Random Structures & Algorithms **1** (1990), 311–342, doi:10.1002/rsa.3240010306 (abstract accessible; full text not inspected).
