# Uniform logarithmic correction for greedy matching with partially forbidden pairs

## Finding

For integers \(n\ge2\) and \(0\le r\le n\), let \(G_{n,r}\) be obtained from \(K_{n,n}\) by deleting \(r\) mutually vertex-disjoint edges. Choose an available edge uniformly, match its endpoints, and repeat on the unmatched vertices. Let \(p_{n,r}\) be the probability that the final matching is not perfect. Define
\[
v_{n,r}=\frac{r(r-1)}{n(n-1)(n+1)(n+2)},\qquad H_n=\sum_{j=1}^n\frac1j.
\]
Every output has cardinality \(n\) or \(n-1\), and
\[
\boxed{\left|p_{n,r}-\left(\frac{2r}{n(n+1)}-4v_{n,r}(H_n-1)\right)\right|\le36v_{n,r}.}
\]
Consequently, uniformly over all integer choices \(2\le r\le n\),
\[
\boxed{\frac{\frac{2r}{n(n+1)}-p_{n,r}}{4v_{n,r}\log n}\longrightarrow1.}
\]
For \(r=0\) and \(r=1\), the leading expression is **exact**: \(p_{n,0}=0\) and \(p_{n,1}=2/[n(n+1)]\). The finite law is computable by the exact two-parameter recurrence in the proof.

## Assumptions and scope

The graph is simple, bipartite, and balanced, with \(n\) vertices in each class; the \(r\) deleted edges share no endpoints. The algorithm makes independent uniform choices among presently feasible edges (equivalently, it accepts matching edges in a uniformly random permutation of the original graph edges). No random-graph averaging or vertex-priority selection is involved. The asymptotic statement is for \(n\to\infty\), uniformly over \(2\le r=r(n)\le n\). A probability of failure means one unmatched vertex in each class, not the absence of a perfect matching in the underlying graph.

## Proof

**State reduction.** At a stage with \(k\) unmatched vertices on each side, let \(T_k=t\) count deleted original pairs with both endpoints still unmatched. There are exactly \(k^2-t\) available edges. An accepted edge joining endpoints from two different intact forbidden pairs destroys two intact pairs, and there are \(t(t-1)\) such edges. An edge between an intact-pair endpoint and an unmatched vertex outside all intact pairs destroys one intact pair, and there are \(2t(k-t)\) such edges. The remaining \((k-t)^2\) edges destroy no intact pair. Thus for \(k\ge2\),
\[
\begin{split}
\Pr(T_{k-1}=t-2\mid T_k=t)&=\frac{t(t-1)}{k^2-t},\\
\Pr(T_{k-1}=t-1\mid T_k=t)&=\frac{2t(k-t)}{k^2-t},\\
\Pr(T_{k-1}=t\mid T_k=t)&=\frac{(k-t)^2}{k^2-t}.
\end{split}
\]
Terms of zero numerator are omitted. For \(k\ge2\), \(k^2-t\ge k(k-1)>0\), so the algorithm necessarily reaches \(k=1\). At that stage it fails exactly when \(T_1=1\). Consequently \(p_{n,r}=\mathbb E[T_1]\) for the chain started at \(T_n=r\). If \(F(1,0)=0\), \(F(1,1)=1\), then for \(k\ge2\) and \(0\le t\le k\),
\[
F(k,t)=\frac{t(t-1)F(k-1,t-2)+2t(k-t)F(k-1,t-1)+(k-t)^2F(k-1,t)}{k^2-t},
\]
where zero-weight invalid terms are omitted, and \(p_{n,r}=F(n,r)\). This is a terminating rational recurrence, not an approximation.

**First factorial-moment potential.** Set \(U_k=T_k/[k(k+1)]\). Direct substitution in the transition probabilities, for each \(k\ge2\), gives
\[
\mathbb E[U_{k-1}\mid T_k=t]-\frac{t}{k(k+1)}
=-\frac{2t(t-1)}{k(k-1)(k+1)(k^2-t)}.
\]
Telescoping expectations from \(n\) to \(1\), using \(2\mathbb E U_1=p_{n,r}\), yields the exact identity
\[
d_{n,r}:=\frac{2r}{n(n+1)}-p_{n,r}
=4\sum_{k=2}^{n}\mathbb E\!\left[\frac{T_k(T_k-1)}{k(k-1)(k+1)(k^2-T_k)}\right].
\tag{1}
\]
In particular \(d_{n,r}\ge0\), and for \(r\le1\) it vanishes identically.

**Second factorial-moment potential.** Set
\[
V_k=\frac{T_k(T_k-1)}{k(k-1)(k+1)(k+2)},\qquad k\ge2.
\]
For \(k\ge3\) and \(t\ge2\), another exact substitution gives
\[
\mathbb E[V_{k-1}\mid T_k=t]
=V_k\left(1-\eta_{k,t}\right),\qquad
\eta_{k,t}=\frac{2(k+2t-6)}{(k-2)(k^2-t)}.
\]
For \(t=0,1\) both sides are zero. Since \(2\le t\le k\),
\[
0\le\eta_{k,t}\le\frac6{k(k-1)}.
\]
Thus \(\mathbb E V_k\) is nonincreasing when moving toward smaller \(k\), and \(\mathbb E V_k\le V_n=v_{n,r}\). Moreover, telescoping the conditional loss and bounding each earlier expectation by \(v_{n,r}\), for every \(2\le k\le n\),
\[
0\le v_{n,r}-\mathbb E V_k
\le6v_{n,r}\sum_{j=k+1}^{n}\frac1{j(j-1)}
\le\frac{6v_{n,r}}k.
\tag{2}
\]
Let \(W_k=(k+2)/(k^2-T_k)\). For \(2\le T_k\le k\) and also for \(T_k=0,1\),
\[
0\le W_k-\frac1k
=\frac{2k+T_k}{k(k^2-T_k)}
\le\frac3{k(k-1)}.
\tag{3}
\]
Equation (1) is exactly \(d_{n,r}=4\sum_{k=2}^{n}\mathbb E[V_kW_k]\). By (2) and (3),
\[
\begin{split}
\left|d_{n,r}-4v_{n,r}\sum_{k=2}^n\frac1k\right|
&\le4\sum_{k=2}^n\frac{v_{n,r}-\mathbb E V_k}{k}
 +4\sum_{k=2}^n\mathbb E[V_k(W_k-1/k)]\\
&\le4v_{n,r}\left(6\sum_{k=2}^{\infty}\frac1{k^2}
 +3\sum_{k=2}^{\infty}\frac1{k(k-1)}\right)\\
&\le36v_{n,r},
\end{split}
\]
using \(\sum_{k=2}^{\infty}k^{-2}\le1\) and \(\sum_{k=2}^{\infty}[k(k-1)]^{-1}=1\). This proves the finite inequality. Because \(H_n-1=\log n+O(1)\), division by \(4v_{n,r}\log n\) gives the displayed limit, with an \(O(1/\log n)\) relative error that is uniform for all \(2\le r\le n\).

## Verification

The companion `verify.py` independently evaluates exact full unmatched-vertex subset recurrences for all \(2\le n\le6\), \(0\le r\le n\), and compares them to the reduced recurrence. It also verifies the conditional first- and second-moment identities for every integer \(2\le k\le40\), \(0\le t\le k\), and tests the claimed explicit uniform inequality with rational arithmetic for every \(2\le n\le30\), \(0\le r\le n\). Run `python verify.py` using Python 3's standard library; the expected terminal line is `VERIFY_OK 4937 exact assertions`. The infinite uniform limit is established by the analytical bounds above, not by these finite tests.

## Relationship to prior work

Arnosti (2021) defines the same random-edge selection algorithm and compares its average performance on random bipartite edge sets, rather than evaluating deterministic matching-deleted bicliques. Johnston, Kayll and Palmer (2022) investigate the exact enumeration of perfect matchings avoiding forbidden partners; counting such perfect matchings under a uniform perfect-matching measure is different from running the random-edge greedy process. Dyer and Frieze (1991), and Miller and Pritikin (1997), study general randomized greedy matching and performance bounds; no exact partial-forbidden-pair logarithmic correction was identified in accessible statements. Existing analyses of the full crown graph yield a first-order failure law \(p_{n,n}=2/n+O(\log n/n^2)\); the quantified universal second-order coefficient for every deletion size \(r\) is the additional result claimed here. The partial deletion family interpolates the exact single-forbidden-edge law with the dense full-crown regime. No claim is made that the general random-edge algorithm or the finite state recursion itself is new.

## Limitations

The finding concerns the uniform-random-edge algorithm, not random-vertex or ranking variants, and only deleted edge sets that are matchings. The error bound is uniform but its constant is not asserted optimal; it describes a second-order asymptotic, not an exact closed form for every probability. The exact recurrence provides finite values. Historical priority is subject to inaccessible full text of older general greedy-matching papers; the available comparisons do not constitute an independent originality certification.

## References

- N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, *Stochastic Systems* (published online November 2, 2021), DOI: https://doi.org/10.1287/stsy.2021.0082 ; author manuscript: https://nickarnosti.com/ResearchPapers/Arnosti_GreedyMatching.pdf.
- D. Johnston, P. M. Kayll, C. Palmer, *Deranged matchings: proofs and conjectures*, first arXiv version September 22, 2022, https://arxiv.org/abs/2209.11319.
- M. Dyer, A. Frieze, *Randomized greedy matching*, *Random Structures & Algorithms* 2 (1991), 29–45, https://doi.org/10.1002/rsa.3240020104.
- Z. Miller, D. Pritikin, *On randomized greedy matchings*, *Random Structures & Algorithms* 10 (1997), 353–383, https://doi.org/10.1002/(SICI)1098-2418(199705)10:3%3C353::AID-RSA5%3E3.0.CO;2-V.
