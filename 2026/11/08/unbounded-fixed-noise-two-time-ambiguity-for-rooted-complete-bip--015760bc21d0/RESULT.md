# Unbounded fixed-noise two-time ambiguity for rooted complete bipartite noisy-voter models

## Finding

**Theorem (unbounded fibers at a single fixed noise level).** For every integer \(k\ge 2\), there are \(k\) pairwise nonisomorphic, nonstar, finite connected rooted complete bipartite graphs whose *stationary single-root observations* under the synchronous fair-noise voter model with refresh probability \(\varepsilon=1/2\) have **identical joint distributions at every pair of times**. This holds simultaneously for all nonnegative time lags, not merely for a prescribed finite selection of lags.

An explicit family is as follows. Let
\[
L_k=\operatorname{lcm}\{5j-4:1\le j\le k\},\qquad n=2L_k,
\]
and for \(1\le j\le k\), set
\[
a_j=1+j(n-1),\qquad b_j=\frac{jn}{5j-4}.
\]
Both are integers with \(a_j\ge n\) and \(2\le b_j\le n\). Root \(K_{a_j,b_j}\) at a vertex in its \(a_j\)-vertex part. All \(k\) stationary lag correlations of these roots obey
\[
R_0=1,\quad R_{2\ell+1}=0\quad(\ell\ge0),\quad
R_{2\ell}=\frac{4^{1-\ell}}{3n+1}\quad(\ell\ge1).
\]
Thus for every lag \(d\ge0\), the two-time joint distribution of the two unbiased binary root opinions is the same for all \(j\); the sizes of the larger bipartition classes \(a_j\) strictly increase, so the rooted and unrooted graphs are pairwise nonisomorphic.

For example, the three rooted graphs \(K_{33,33}\), \(K_{65,11}\), and \(K_{97,9}\), with each root in the first named part, have the same lag-two spin correlation \(1/100\) and the same entire sequence of two-time laws at refresh probability \(1/2\).

## Assumptions and scope

All graphs are finite, simple, connected and undirected. The notation \(K_{a,b}\) denotes the complete bipartite graph with nonempty parts of sizes \(a,b\). At every integer time, every vertex updates *simultaneously and independently*: with probability \(\varepsilon\), replace its opinion by an independent fair sign in \(\{-1,+1\}\); otherwise copy the previous-time opinion of an independently sampled uniform neighbor. The model is not the asynchronous one-vertex-at-a-time process.

The positive refresh probability makes the finite configuration Markov chain strictly positive after one update, hence it has a unique stationary distribution. Let \(\sigma_t(v)\) be the stationary sign at vertex \(v\). Global sign symmetry gives \(\mathbb E\sigma_t(v)=0\). For a distinguished root \(u\), let
\[
R_d=\mathbb E[\sigma_t(u)\sigma_{t+d}(u)]\qquad(d\in\mathbb Z_{\ge0}).
\]
For unbiased signs, the complete two-time law is determined by \(R_d\): for \(s,s'\in\{-1,+1\}\),
\[
\Pr(\sigma_t(u)=s,\sigma_{t+d}(u)=s')=\frac{1+ss'R_d}{4}.
\]
The theorem concerns stationary two-time laws, not higher-order joint laws, distinguishability from the full observation stream, or finite-sample inference.

## Proof

**1. Symmetry-reduced equal-time correlations.** Write \(c=1-\varepsilon\), \(q=c^2\). Root \(K_{a,b}\) at a vertex of its \(a\)-vertex part \(A\), and call the other part \(B\). By automorphism invariance, equal-time spin correlations between distinct vertices are constants \(x\) within \(A\), \(y\) within \(B\), and \(z\) across the parts. Conditional independence of the updates at distinct vertices implies that the correlation after one update is \(q\) times the mean correlation of the two independently chosen parents.

For a cross-part pair, the two parents again lie in opposite parts. Hence \(z=qz\), so \(z=0\) for \(0<q<1\). For two different vertices in \(A\) (respectively in \(B\)), their parents coincide with probability \(1/b\) (respectively \(1/a\)). Consequently
\[
x=\frac{q}{b}\bigl(1+(b-1)y\bigr),\qquad
y=\frac{q}{a}\bigl(1+(a-1)x\bigr).
\]
Solving this pair of equations gives
\[
y=\frac{qb+q^2(a-1)}{ab-q^2(a-1)(b-1)}.
\]
The denominator is strictly positive because \(ab>q^2(a-1)(b-1)\) for positive integers \(a,b\) and \(0<q<1\).

**2. All stationary temporal correlations.** Let \(P\) be the uniform-neighbor transition matrix. Conditional expectation iterated over future updates gives
\[
\mathbb E[\sigma_{t+d}(u)\mid\sigma_t]
=c^d\sum_v(P^d)_{uv}\sigma_t(v).
\]
For every \(\ell\ge1\), \(P^{2\ell}(u,\cdot)\) is uniform on \(A\), whereas \(P^{2\ell+1}(u,\cdot)\) is uniform on \(B\) for all \(\ell\ge0\). Because \(z=0\), the odd correlations vanish. The second equal-time equation yields
\[
R_{2\ell}=c^{2\ell}\frac{1+(a-1)x}{a}
=c^{2\ell-2}y\quad(\ell\ge1).
\]
This is an exact identity for all lags, not a finite-horizon approximation.

**3. Fixed-noise coincidence identity.** At the fixed refresh probability \(\varepsilon=1/2\), \(c=1/2\) and \(q=1/4\), hence
\[
y(a,b)=\frac{a+4b-1}{15ab+a+b-1}.
\]
In particular \(y(n,n)=1/(3n+1)\). For arbitrary positive integers \(a,b,n\), the equality \(y(a,b)=1/(3n+1)\) is equivalent, after cross multiplication, to
\[
(5a-4n-1)b=n(a-1).
\]
Now substitute \(a=a_j=1+j(n-1)\) and \(b=b_j=jn/(5j-4)\). Both sides become \(jn(n-1)\), because
\[
5a_j-4n-1=(5j-4)(n-1).
\]
Thus \(y(a_j,b_j)=1/(3n+1)\) for all \(1\le j\le k\). Step 2 supplies their identical correlation sequence and Step 2 together with sign symmetry supplies their identical two-time joint laws.

**4. Arbitrarily many nonisomorphic graphs.** The integer \(n=2L_k\) is divisible by every \(5j-4\), so each \(b_j\) is integral. For \(k\ge2\), \(L_k\ge6\), hence \(n\ge12\); moreover \(b_j\ge n/5>2\) and \(a_j\ge n\). For \(j=1\), \((a_1,b_1)=(n,n)\); for \(j>1\), \(a_j>n\) and \(b_j<n\). The sequence \(a_1<a_2<\cdots<a_k\) is strictly increasing, and \(a_j\) is the larger side of each bipartition, so no two of the resulting graphs are isomorphic. They are connected and are not stars because both parts have at least two vertices. Since \(k\) was arbitrary, the fiber cardinalities are unbounded. \(\square\)

## Verification

The standalone Python file `verify.py` runs with the standard library only (`python3 verify.py`). It constructs a full unordered-vertex-pair stationary covariance linear system directly from the transition rule and solves it using exact rational Gaussian elimination. It independently checks all stationary lag correlations through lag 12 for the two separate collisions \((a,b)=(4,4),(5,2)\) and \((6,6),(11,2)\). It also performs exact arithmetic checks for simultaneous collisions across fourteen parameter choices \(2\le k\le15\), and additional divisibility examples. An extracted execution of the bundled checker returned `VERIFY_OK 560 exact-rational assertions`.

The infinite theorem is proved by the identities above. The finite tests are consistency checks only; they do not certify all integers or substitute for the symbolic proof.

## Relationship to prior work

Benjamini, Helman Tov and Zhukovskii (first public preprint 2022-07-04), Section 6, already derive complete-bipartite noisy-voter repetition behavior and prove the existence of *pairs* of nonisomorphic rooted complete bipartite graphs for arbitrarily large size thresholds and suitably selected noise parameters whose repetition probabilities agree at every lag. That existing pairwise nonidentifiability statement is **not** claimed as new here. Their Theorem 6.1(4) allows the noise to vary and does not assert that at one **fixed** refresh probability, arbitrarily many different graphs share one common complete two-time observation law. The new statement supplies this simultaneous unbounded-fiber quantifier and a constructive common value at \(\varepsilon=1/2\), rather than merely exhibiting another pair. Section 6 further distinguishes some exceptional pairs by four-time statistics, which is consistent with this theorem's explicitly second-order scope.

Pymar and Rivera (first public preprint 2021-12-02) study a different noisy-voter update convention (one vertex updated per step) and density-process fluctuations, not simultaneous fixed-noise families of indistinguishable two-time *single-root* distributions. Carro, Toral and San Miguel (published 2016-04-20) study macroscopic noisy-voter correlations on complex networks, likewise not this exact synchronous rooted fiber problem.

## Limitations

No assertion is made that any graphs in the constructed family have the same **three- or four-time** joint distributions, or that they are indistinguishable from the full stationary observation sequence. The refresh probability is fixed at \(1/2\); the claim does not extend to all noise levels. Root placement in the specified part matters. These counterfamilies establish no statistical minimax rate or finite-sample bound. Prior-work searches and source inspection provide best-knowledge support for the simultaneous fixed-noise unbounded-fiber distinction, not an independent priority determination.

## References

1. I. Benjamini, H. Helman Tov, M. Zhukovskii, *Global information from local observations of the noisy voter model on a graph*, first public arXiv version 2022-07-04, especially Theorem 6.1 and Section 6, https://arxiv.org/abs/2207.01224.
2. R. Pymar, N. Rivera, *On the stationary distribution of the noisy voter model* (also listed as *Asymptotic behaviour of the noisy voter model density process*), first public arXiv version 2021-12-02, https://arxiv.org/abs/2112.01478.
3. A. Carro, R. Toral, M. San Miguel, *The noisy voter model on complex networks*, Scientific Reports 6, 24775 (2016), published 2016-04-20, https://doi.org/10.1038/srep24775.
