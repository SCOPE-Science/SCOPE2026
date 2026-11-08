# Joint law and independence threshold for two tandem-duplication descendant counts

## Finding

Fix integers \(q\geq2\), \(1\leq k<\ell\), and \(n\geq\ell\). Choose \(X\) uniformly from \(\Sigma^n\), where \(|\Sigma|=q\). Let \(D_h(X)\) be the number of **distinct** length-\(n+h\) words obtainable by duplicating exactly one contiguous block of length \(h\) next to itself, for \(h\in\{k,\ell\}\). Put
\[
Y_h=n-h+1-D_h(X),\quad g=\gcd(k,\ell),\quad a=k/g,\quad b=\ell/g,\quad L=k+\ell.
\]
Then \(Y_h\) has the binomial distribution \(\operatorname{Bin}(n-h,1/q)\), and the pair \((D_k,D_\ell)\), equivalently \((Y_k,Y_\ell)\), is independent **if and only if**
\[
n\leq k+\ell-g.
\]
In particular, for every \(n\geq\ell\), the two descendant counts are uncorrelated, although they are dependent once \(n\geq L-g+1\).

The joint law is explicitly evaluable in the entire range \(\ell\leq n\leq L\). Define \(c=\max\{0,n-L+g\}\). Its joint binomial generating polynomial is
\[
\begin{aligned}
F_{n;k,\ell}(u,v)&=\mathbb{E}[(1+u)^{Y_k}(1+v)^{Y_\ell}]\\
&=(1+u/q)^{n-k-cb}(1+v/q)^{n-\ell-ca}\\
&\quad\times\left[(1+u/q)^b(1+v/q)^a+\frac{q-1}{q^{a+b}}u^bv^a\right]^c.
\end{aligned}
\]
All exponents here are nonnegative integers. Thus the ordinary joint probability generating polynomial of \((Y_k,Y_\ell)\) is \(F_{n;k,\ell}(s-1,t-1)\).

In the same range, the first mixed factorial-moment discrepancy is exactly
\[
\mathbb{E}\left[\binom{Y_k}{b}\binom{Y_\ell}{a}\right]
-\mathbb{E}\binom{Y_k}{b}\;\mathbb{E}\binom{Y_\ell}{a}
=\frac{c(q-1)}{q^{a+b}}.
\]
For \(n>L\) the displayed joint polynomial is not asserted, but the sharp independence criterion remains valid.

## Assumptions and scope

The alphabet symbols are independently sampled uniformly, with no biological or Markov dependence. The duplicated block is inserted immediately after its original; both copies are identical. Positions are distinct operations but identical resulting words are counted only once. The two lengths \(k\) and \(\ell\) are different; the case \(n=\ell\), in which the longer duplication has a single possible position, is included. The pair of descendant counts refers to two separate one-error experiments on the **same** random source word, not a sequence of two duplications.

## Proof

**1. Collapse of duplication positions.** Use zero-based indices. If \(0\leq i\leq n-h\), duplication at position \(i\) produces
\[
T_{i,h}(x)=x[0:i+h]\;x[i:i+h]\;x[i+h:n],
\]
where the brackets denote half-open substrings and juxtaposition means concatenation. For \(i<j\), deleting the common prefix \(x[0:i+h]\) and common suffix \(x[j+h:n]\) shows that \(T_{i,h}(x)=T_{j,h}(x)\) is equivalent to
\[
x[i:j+h]=x[i+h:j+h]\;x[j:j+h].
\]
Comparing the first \(j-i\) symbols, and observing that the remaining \(h\) symbols are automatically equal, shows this happens precisely when \(x_t=x_{t+h}\) for every \(i\leq t<j\). Consequently the equal-output positions form contiguous classes, separated by the indices where \(x_t\ne x_{t+h}\). Hence
\[
D_h(x)=1+\sum_{i=0}^{n-h-1}\mathbf 1\{x_i\ne x_{i+h}\},\qquad
Y_h=\sum_{i=0}^{n-h-1}\mathbf 1\{x_i=x_{i+h}\}.
\]

**2. Equality-constraint graph.** Construct the undirected graph \(G_{n;k,\ell}\) on vertices \(0,\ldots,n-1\), with a \(k\)-colored edge \(\{i,i+k\}\) for \(0\leq i<n-k\), and an \(\ell\)-colored edge \(\{i,i+\ell\}\) for \(0\leq i<n-\ell\). Because \(k\ne\ell\), all edges are distinct. For any selected edge set \(S\), the probability that all endpoint equalities on \(S\) hold is
\[
q^{-|V(S)|+\kappa(S)}=q^{-|S|+\beta(S)},
\]
where \(\kappa(S)\) is the number of components of its incident-vertex graph and \(\beta(S)=|S|-|V(S)|+\kappa(S)\) is its cycle rank. In particular, on a forest, all the edge-equality indicators are mutually independent Bernoulli variables of parameter \(1/q\). The edges of any single color separately form a forest (a union of arithmetic-progression paths), proving the binomial marginals. Two **different** edges are a forest even if incident, proving pairwise independence of all distinct equality indicators and thus \(\operatorname{Cov}(D_k,D_\ell)=0\).

**3. Exact small-length cycle decomposition.** For \(n\leq L=k+\ell\), view the edge graph as an induced subgraph of the graph on residues \(0,\ldots,L-1\) with edges joining residues differing by \(\pm k\pmod L\). Indeed, among residues in this interval, such edges have ordinary positive length exactly \(k\) or \(\ell=L-k\). This larger graph has exactly \(g=\gcd(k,L)\) disjoint simple cycles, one for each residue class modulo \(g\), each with \(a+b=L/g\) vertices. Every such cycle has exactly \(b=\ell/g\) edges of length \(k\) and \(a=k/g\) of length \(\ell\). The orbit indexed by residue \(r\in\{0,\ldots,g-1\}\) has maximum vertex \(L-g+r\). Thus its whole cycle survives the induced restriction to \(0,\ldots,n-1\) exactly when \(r\leq n-L+g-1\). There are precisely \(c=\max\{0,n-L+g\}\) complete cycles; all other components are paths or isolated vertices.

**4. Joint polynomial.** For a path or forest component, the equality-edge indicators are independent, producing a factor \(1+u/q\) for each \(k\)-edge and \(1+v/q\) for each \(\ell\)-edge in \(\mathbb E\prod_e(1+t_e\mathbf1\{X_{e^-}=X_{e^+}\})\). On one complete cycle of \(r=a+b\) edges, every proper subset is a forest and has equality probability \(q^{-|S|}\); the full set has probability \(q^{1-r}\), rather than \(q^{-r}\). The only correction to the independent-edge product is therefore \((q-1)u^bv^a/q^r\). Distinct components depend on disjoint independent letters, so their generating factors multiply. There are \(n-k-cb\) remaining \(k\)-edges and \(n-\ell-ca\) remaining \(\ell\)-edges, giving the formula. Extracting the coefficient of \(u^bv^a\) and subtracting the independent-marginal coefficient yields the stated exact discrepancy.

**5. Sharp independence threshold at all lengths.** If \(n\leq L-g\), the above decomposition is a forest, hence \(Y_k,Y_\ell\) are independent. For any \(n\geq L-g+1\), the vertex interval contains the complete residue-zero cycle on \(0,g,2g,\ldots,L-g\). Consider the mixed factorial moment with \(b\) selected \(k\)-edges and \(a\) selected \(\ell\)-edges. Expanding it as a sum over distinct edge selections, each selection contributes \(q^{-r+\beta(S)}\geq q^{-r}\). The independent-binomial product would give exactly \(q^{-r}\) per selection. At least the complete cycle contributes strictly more, because \(\beta(S)=1\) and \(q\geq2\). Therefore the factorial moment cannot factor, proving dependence. This argument applies without an upper restriction on \(n\).

## Verification

Run `python verify_joint.py` to independently enumerate alphabet words and compare every rational coefficient of the joint factorial polynomial against the closed form over 28 nontrivial parameter cases, including both coprime and noncoprime lengths and both independent and dependent regimes. Run `python check_graph.py` to check graph-component cycle ranks for 90 parameter triples, all pairwise duplication-position collisions over 19,329 short words, and strict mixed-factorial dependence beyond the threshold. Both programs use only the Python standard library. Verification is finite corroboration; the proof above covers all stated integers.

At \(q=2\), \(k=2\), \(\ell=3\), \(n=5\), the first dependence occurs at five letters. Here \(F_{5;2,3}(u,v)=(1+u/2)^3(1+v/2)^2+u^3v^2/32\): despite zero covariance, the joint law differs from independent binomial marginals in an exactly identified fifth-degree term.

## Relationship to prior work

The fixed-length tandem-duplication channel and its derivative/zero-block-insertion representation are established in Jain, Farnoud, Schwartz, and Bruck (2016), and further analyzed for fixed-length error correction by Kovačević and Tan (2018). Jain, Farnoud, and Bruck (2015) investigate duplication-system capacity and expressiveness, whereas Penso-Dolfin and Greenman (2014) investigate different duplication-evolution word counts. Those results motivate the model but do not furnish this **two-length same-source joint distribution**, the gcd-dependent independence threshold, or the evaluated small-length bivariate law. The forest-equality and cycle-rank identities used here are elementary standard graph-probability facts; they are not claimed as new. General graph probability identities alone do not supply the explicit residue-cycle count for this pair of lengths. Historical priority of the specialized combination has not been independently adjudicated.

## Limitations

The complete joint polynomial is asserted only when \(n\leq k+\ell\); beyond that range, only the exact independence threshold and zero covariance are proved, not the whole joint distribution. Uniform independent letters are essential to the independent-edge argument, and no conclusions are made for biased or dependent sources, noisy duplications, two successive errors, or biological mutation rates. The result is a mathematical distributional property, not a new code construction or capacity bound.

## References

- L. Penso-Dolfin and C. D. Greenman, *The Combinatorics of Tandem Duplication*, arXiv:1402.0104, first public version 2014-02-01. https://arxiv.org/html/1402.0104v1
- S. Jain, F. Farnoud, and J. Bruck, *Capacity and Expressiveness of Genomic Tandem Duplication*, arXiv:1509.06029, first public version 2015-09-20. https://arxiv.org/abs/1509.06029
- S. Jain, F. Farnoud, M. Schwartz, and J. Bruck, *Duplication-Correcting Codes for Data Storage in the DNA of Living Organisms*, arXiv:1606.00397, first public version 2016-06-01. https://arxiv.org/abs/1606.00397
- M. Kovačević and V. Y. F. Tan, *Asymptotically Optimal Codes Correcting Fixed-Length Duplication Errors in DNA Storage Systems*, arXiv:1808.10328, first public version 2018-08-30. https://arxiv.org/abs/1808.10328
