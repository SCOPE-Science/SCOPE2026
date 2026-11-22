# Sharp square-root normal-cone collision amplification for single-split hypersimplices

## Finding

Let \(P_{n,h,k,r}\) be the canonical Euclidean base polytope obtained by imposing one cardinality split on a hypersimplex:
\[
P_{n,h,k,r}=\operatorname{conv}\left\{\mathbf{1}_B:B\subseteq[n],\ |B|=k,\ |B\cap[h]|\le r\right\}\subset\mathbb R^n.
\]
For an isotropic Gaussian linear objective, write \(V\) for its almost surely unique maximizing vertex. Put
\[
M=\binom nk,\quad N_t=\binom ht\binom{n-h}{k-t},\quad
F=\sum_{t\le r}N_t,\quad p=\frac1M\sum_{t\ge r}N_t,
\]
where binomial coefficients with inadmissible lower indices are zero. **Every vertex has one of exactly two possible normal-cone probabilities**:
\[
\Pr(V=\mathbf{1}_B)=
\begin{cases}
M^{-1},&|B\cap[h]|<r,\\
p/N_r,&|B\cap[h]|=r.
\end{cases}
\]
In particular, for two independent Gaussian objectives with maximizing vertices \(V,V'\), the exact angular collision probability is
\[
C_{n,h,k,r}:=\Pr(V=V')=\frac{F-N_r}{M^2}+\frac{p^2}{N_r}.
\]

There is a sharp critical-window amplification. Suppose \(n\to\infty\), \(h/n\to\rho\in(0,1)\), \(k/n\to\kappa\in(0,1)\), and, for fixed \(a\in\mathbb R\),
\[
\mu_n=\frac{hk}{n},\quad
\sigma_n^2=\frac{k(n-k)h(n-h)}{n^2(n-1)},\quad
r=\lfloor\mu_n+a\sigma_n\rfloor.
\]
Writing \(\Phi\) and \(\phi\) for the standard normal distribution function and density, respectively, one has
\[
\boxed{\lim_{n\to\infty}\frac{M C_{n,h,k,r}}{\sigma_n}=
\frac{(1-\Phi(a))^2}{\phi(a)}.}
\]
Moreover,
\[
\Pr(|B\cap[h]|=r\mid V=V')\longrightarrow1,
\]
where \(B\) is the support of the common vertex; and
\[
\frac{\Pr(V=V')}{1/F}\sim
\sigma_n\,\frac{\Phi(a)(1-\Phi(a))^2}{\phi(a)}.
\]
Thus Gaussian normal-cone sampling has a collision probability larger by a sharp factor of order \(\sqrt n\) than uniformly sampling vertices of the *same* polytope, although the collision event concentrates on its single split-facet vertex orbit. In contrast, the uniformly sampled vertex lies in that orbit with probability tending to zero.

## Assumptions and scope

For the finite formula, take integers \(n\ge4\), \(1\le h<n\), \(1\le k<n\), and \(r\) satisfying \(L<r<U\), where \(L=\max(0,k-(n-h))\) and \(U=\min(k,h)\). These hypotheses guarantee a proper nontrivial split and \(N_r>0\). All objectives are independent standard Gaussian vectors in \(\mathbb R^n\), equivalently uniform random directions in the intrinsic affine span because the all-ones component contributes the same constant to every vertex. Distinct objective-coordinate values occur almost surely, so no tie-breaking convention is necessary. Every admitted \(0/1\) vector is an actual vertex.

The critical-window statement uses arbitrary integer sequences \(h,k\) with the displayed proportions, and the stated rounding convention for \(r\); its finite hypotheses hold eventually. The symbol \(\Pr(|B\cap[h]|=r\mid V=V')\) refers to the common support of the equal vertices, not to an independently sampled basis.

## Proof

**Step 1: feasible maximizers.** For any strict objective order, let \(A\) be its unrestricted top-\(k\) coordinate set and \(T=|A\cap[h]|\). If \(T\le r\), then \(A\) remains the unique optimizer. If \(T>r\), the unique optimizer is the set consisting of the top \(r\) objective coordinates in \([h]\) together with the top \(k-r\) in its complement. To justify the second assertion, for each possible first-block count \(t\), the greatest objective sum is the sum of the top \(t\) first-block weights and top \(k-t\) second-block weights. Its successive differences decrease with \(t\), and its unrestricted maximum occurs at \(t=T\); hence its maximum over \(t\le r<T\) occurs at \(t=r\). This directly checks the constrained optimization rather than assuming that a downloaded or sampled order certifies it.

**Step 2: the complete spherical normal-cone law.** The top-\(k\) set \(A\) is uniformly distributed over the \(M\) possible \(k\)-subsets, so \(T\) is hypergeometric with \(\Pr(T=t)=N_t/M\). If a fixed feasible \(B\) has \(|B\cap[h]|<r\), it can be selected only when \(A=B\); a binding solution would have exactly \(r\) first-block coordinates. Thus its probability is \(1/M\). The subgroup of coordinate permutations \(S_h\times S_{n-h}\) acts transitively on the \(N_r\) feasible boundary vertices and preserves the objective distribution. Their aggregate selection probability is \(\Pr(T\ge r)=p\), so each has mass \(p/N_r\). These probabilities add to \(1\), because \((F-N_r)/M+p=1\).

**Step 3: collision identity.** For two independent objectives, sum the squares of all vertex probabilities. There are \(F-N_r\) interior-count vertices and \(N_r\) boundary-count vertices, yielding exactly \((F-N_r)/M^2+p^2/N_r\). The collision joint law is similarly the normalized squared vertex-mass distribution. This proves the exact results for every allowed finite quadruple.

**Step 4: critical local limit.** For the stated proportional sequences, the classical hypergeometric central and local central limit theorems at a bounded standardized displacement give
\[
\frac{F}{M}\to\Phi(a),\quad p\to1-\Phi(a),\quad
\sigma_n\frac{N_r}{M}\to\phi(a),\quad \sigma_n\sim\sqrt{\rho(1-\rho)\kappa(1-\kappa)n}.
\]
The lattice rounding error is \(O(\sigma_n^{-1})\) in standardized coordinates and does not change any limit. Multiply the exact collision identity by \(M/\sigma_n\): the first term is at most \(1/\sigma_n\) and vanishes, while the boundary term tends to \((1-\Phi(a))^2/\phi(a)\). The same comparison gives the conditional boundary-collision limit of \(1\). A uniform feasible vertex has boundary probability \(N_r/F\sim\phi(a)/(\sigma_n\Phi(a))\to0\), and its collision probability is exactly \(1/F\). Multiplication of the preceding limits proves the sharp collision amplification.

The standard hypergeometric local limit used here can also be reconstructed directly from Stirling's formula applied to \(N_r/M\) with \(r-\mu_n=O(\sqrt n)\); the distribution-function limit follows, for example, by summing the local approximation over a growing fixed standardized interval and applying hypergeometric tail concentration outside it. No finite enumeration is used in place of this infinite argument.

## Verification

The standalone file `verify_split_angles.py` exhaustively enumerates all \(n!\) strict objective-coordinate orders for every nontrivial split with \(4\le n\le8\) (70 parameter configurations). It checks each individual vertex probability and the exact collision rationally; for \(n\le6\), its independently exhaustive objective maximization additionally checks the greedy optimizer. The replay produced `SPLIT_ANGLE_EXACT_PASS 70`.

The optional `asymptotic_check.py` numerically evaluates hypergeometric probabilities, not simulated objectives, for \(n=200,800,3200,12800\) and \(a\in\{-1,0,1\}\), confirming convergence trends and conditional boundary collision mass; its output ended `CRITICAL_SCALING_NUMERIC_PASS`. It requires Python 3 and SciPy. These calculations are finite diagnostics; the proof of the asymptotic statement is Step 4.

## Relationship to prior work

Fan and Li (arXiv:2110.11549, first public version 2021-10-22) study lattice-point and Ehrhart enumeration of Schubert matroid base polytopes. Ferroni and Schröter's treatment of Schubert elementary split matroids (DOI:10.1112/jlms.12984, Sections 2.2 and 3.5) identifies the class and its bases. Their subsequent face-enumeration paper (DOI:10.1017/S0963548325000021, Section 2.2) explicitly identifies the one-inequality hypersimplex model \(P_{n,h,k,r}\), up to conventional parameter relabeling, and computes face-number information. The exact random-normal exposure mass, two-objective coincidence probability, and critical square-root amplification are distinct metric-probabilistic quantities not determined by those face counts or Ehrhart coefficients.

A related indexed result on rank-two matroid angular spectra concerns fixed-rank parallel-class structures. Its rank-two conclusions do not imply this proportional-rank \(k/n\to\kappa\in(0,1)\) critical-window theorem. General matroid greedy optimization explains the algorithm in Step 1, but by itself does not evaluate this angular collision distribution or its sharp asymptotic constant. Searches for synonyms such as clipped hypersimplex, Schubert split matroid, random greedy base, Gaussian normal cone, and hypergeometric collision did not identify an equivalent evaluated statement.

## Limitations

This theorem is for the canonical coordinate metric and isotropic Gaussian objectives; arbitrary anisotropic objectives need not produce the same two-angle law. It treats a single cardinality split, not arbitrary intersections of splits or arbitrary Schubert matroids. Its critical limit requires fixed positive limiting proportions; it does not cover fixed-rank or vanishing-block regimes. The claim is an explicit special-family normal-cone and asymptotic theorem, not a general normal-cone classification for matroids. Unindexed or inaccessible formulations of random greedy optimization may create historical priority risk. Independent external mathematical review has not been performed.

## References

1. N. J. Y. Fan and Y. Li, *On the Ehrhart Polynomial of Schubert Matroids*, arXiv:2110.11549 (first public 2021-10-22), https://arxiv.org/abs/2110.11549.
2. K. Bérczi, T. Király, T. Schwarcz, Y. Yamaguchi and Y. Yokoi, *Hypergraph characterization of split matroids*, arXiv:2202.04371 (first public 2022-02-09), https://arxiv.org/abs/2202.04371.
3. L. Ferroni and B. Schröter, *Valuative invariants for large classes of matroids*, DOI:10.1112/jlms.12984, https://doi.org/10.1112/jlms.12984.
4. L. Ferroni and B. Schröter, *Face enumeration for split matroid polytopes*, DOI:10.1017/S0963548325000021, https://doi.org/10.1017/S0963548325000021.
