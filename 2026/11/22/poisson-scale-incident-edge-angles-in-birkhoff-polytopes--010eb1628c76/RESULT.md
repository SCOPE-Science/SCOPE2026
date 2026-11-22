# Poisson-scale incident-edge angles in Birkhoff polytopes

## Finding
For each integer \(n\ge3\), let \(\mathcal B_n\subset\mathbb R^{n\times n}\) be the Birkhoff polytope with the ambient Frobenius Euclidean metric. Fix any permutation-matrix vertex \(P\). Draw two incident edges independently and uniformly *with replacement*, and let \(\Theta_n\in[0,\pi]\) be their angle at \(P\), measured between the outward edge vectors.

Let \(S,T,M\) be three independent \(\operatorname{Poisson}(1)\) variables. Then
\[
\Theta_n\xrightarrow{\mathsf P}\frac\pi3,
\qquad
n\left(\Theta_n-\frac\pi3\right)
\xrightarrow{\mathsf d}\frac{S+T-2M}{2\sqrt3}.
\]
The limit is a non-Gaussian discrete law of mean zero and variance \(1/2\). Equivalently, with \(C_n=\cos\Theta_n\),
\[
 n\left(C_n-\frac12\right)
 \xrightarrow{\mathsf d}\frac{2M-S-T}{4},
\]
whose limit has variance \(3/8\).

There is also an exact finite-dimensional identity. By an orthogonal row-column relabeling take \(P=I\). Label incident edges by independent uniform permutations \(\sigma,\tau\) having exactly one nontrivial cycle (and any number of fixed points). With \(s=|\operatorname{Fix}(\sigma)|\), \(t=|\operatorname{Fix}(\tau)|\), and \(m=|\{i:\sigma(i)=\tau(i)\}|\),
\[
\boxed{\quad C_n=\frac{n-s-t+m}{2\sqrt{(n-s)(n-t)}}.\quad}
\]
In fact the triple \((s,t,m)\) converges jointly in law to \((S,T,M)\) with **independent** Poisson coordinates. Thus the limiting angle law does not arise from a Gaussian central-limit approximation, despite the ambient dimension \((n-1)^2\) growing quadratically.

## Assumptions and scope
All coordinates refer to the conventional embedding of doubly stochastic matrices in \(\mathbb R^{n\times n}\), with inner product \(\langle A,B\rangle=\operatorname{tr}(A^\mathsf TB)\). The vertex \(P\) can be chosen arbitrarily because row and column permutations act transitively by Euclidean isometries. An incident edge is an undirected one-dimensional face, oriented away from \(P\). Both edges are sampled uniformly from all incident edges; independent sampling allows them to coincide. The theorem is an \(n\to\infty\) limit along positive integers; it does **not** assert finite-dimensional independence or a total-variation error rate for the angle itself.

The adjacency characterization used below is the classical one: \(I\) is adjacent to \(P_\sigma\) if and only if \(\sigma\) is a single nontrivial cycle with arbitrary fixed points. Its original status is explicitly distinguished from the new metric limit.

## Proof
**Step 1 (uniform neighbor law).** The number of nontrivial cycles on exactly \(k\) moving indices is \(\binom nk(k-1)!\). Thus the vertex degree is
\[
 d_n=\sum_{k=2}^n\binom nk(k-1)!=n!\sum_{s=0}^{n-2}\frac1{s!(n-s)}.
\]
For a uniform neighbor, \(S_n\) counts fixed indices and has exact distribution
\[
 \Pr(S_n=s)=\frac{1/[s!(n-s)]}{\sum_{u=0}^{n-2}1/[u!(n-u)]},\qquad 0\le s\le n-2.
\]
Multiplying numerator and denominator by \(n\) proves \(S_n\Rightarrow\operatorname{Poisson}(1)\): for fixed \(s\), \(n/(n-s)\to1\), and the normalized sum tends to \(e\). To justify interchange, split at \(u\le n/2\), where \(n/(n-u)\le2\), and \(u>n/2\), whose factorial tail, multiplied by at most \(n\), vanishes. Independent neighbors yield independent \(S_n,T_n\), both converging to unit Poisson.

**Step 2 (conditional common-arrow factorial moments).** Conditional on their fixed sets \(A,B\) and on \(\sigma\), let \(U=[n]\setminus A\) and \(V=[n]\setminus B\). The restriction of \(\sigma\) to \(U\) is one directed cycle; independently, \(\tau|_V\) is a uniform directed cycle on \(V\). Define
\[
 q=\bigl|\{i\in U\cap V:\sigma(i)\in V\}\bigr|,
 \qquad H=\sum_{i\in U\cap V}\mathbf1\{\sigma(i)\in V,\ \tau(i)=\sigma(i)\}.
\]
One has \(n-|A|-2|B|\le q\le n\). For every fixed positive integer \(j\), provided \(j<|U|\) and \(j\le |V|-1\), any selection of \(j\) distinct eligible arrows of \(\sigma\) is a union of disjoint directed paths and cannot itself close a cycle. A uniform directed cycle on \(V\) contains these \(j\) prescribed arrows with probability
\[
 \frac{(|V|-j-1)!}{(|V|-1)!}=\frac1{(|V|-1)_{\underline j}},
\]
by contracting the paths. Consequently the **exact** conditional falling-factorial moment is
\[
 \mathbb E\big[(H)_{\underline j}\mid A,B,\sigma\big]
 =\frac{(q)_{\underline j}}{(n-|B|-1)_{\underline j}}.
\]
For bounded fixed-set sizes this tends uniformly to one, the \(j\)-th factorial moment of \(\operatorname{Poisson}(1)\). The method of factorial moments gives conditional Poisson convergence uniformly over \(A,B,\sigma\) with bounded fixed-set sizes. Since \(\Pr(|A|+|B|>K)\) can be made arbitrarily small with \(K\), it follows that \((S_n,T_n,H)\) converges jointly to three **independent** unit Poisson variables.

The total number of matching arrows \(M_n=|\{i:\sigma(i)=\tau(i)\}|\) equals \(H+|A\cap B|\). Given fixed-set cardinalities \(s,t\), the sets are independent uniform subsets, so \(\mathbb E|A\cap B|=st/n\). Tightness of \(s,t\) implies \(|A\cap B|\to0\) in probability. Therefore
\[
 (S_n,T_n,M_n)\xrightarrow{\mathsf d}(S,T,M)
\]
with independent unit Poisson limits.

**Step 3 (exact Euclidean angle and scaled limit).** The edge vectors from \(I\) are \(P_\sigma-I\) and \(P_\tau-I\). Their squared norms are \(2(n-s)\) and \(2(n-t)\), and their inner product is
\[
\operatorname{tr}[(P_\sigma-I)^\mathsf T(P_\tau-I)]=n-s-t+m.
\]
This proves the exact cosine identity. The three counts are tight, so Taylor expansion of the denominator on each bounded-count event gives
\[
 n\left(C_n-\frac12\right)=\frac{2M_n-S_n-T_n}{4}+o_{\mathsf P}(1).
\]
The continuous mapping theorem yields the cosine law, and the derivative of \(\arccos\) at \(1/2\) is \(-2/\sqrt3\); hence
\[
 n\left(\Theta_n-\frac\pi3\right)
 =\frac{S_n+T_n-2M_n}{2\sqrt3}+o_{\mathsf P}(1).
\]
Three independent Poisson variables of unit variance make the limiting angle variance \((1+1+4)/12=1/2\), and the cosine-limit variance \((4+1+1)/16=3/8\). This completes the proof.

## Verification
The accompanying standalone script `check_birkhoff_angles.py` constructs every incident permutation at \(I\) for \(n=3,4,5,6\), counting respectively \(5,20,84,409\) neighbors and \(25,400,7056,167281\) ordered neighbor pairs. It checks the full Frobenius matrix inner product against the exact trace identity, the Cauchy--Schwarz bound, and the conditional falling-factorial formula for every permissible fixed set and test order up to three. It also samples 35,000 independent pairs at \(n=100\) with a fixed random seed, checking that the three empirical means are near one and the off-diagonal covariances are small. The run ended with `BIRKHOFF_LOCAL_ANGLE_EXACT_PASS`.

These finite tests and Monte Carlo checks are not a proof of asymptotic convergence. The all-dimensional statement is established by the conditional factorial-moment argument in the Proof section.

## Relationship to prior work
Kane, Lovett and Rao [1] identify the Birkhoff polytope's graph with the Cayley graph generated by single nontrivial cycles; this is the essential established adjacency input, not a new combinatorial characterization. Bengtsson et al. [2] analyze Frobenius distances and edges for \(n=3,4\), including angles subtended at the **polytope center**. Those center-angles differ from the present **angles between two incident edge rays at a vertex**, and [2] does not give the all-dimensional local Poisson limit. Mui [3] analyzes coalescence probabilities for products of two full cycles and earlier cycle-product enumeration. The present result concerns joint counts of fixed points of two independent random *single-nontrivial-cycle neighbors* and their matching arrows, and evaluates the resulting Euclidean angle fluctuations; [3] does not directly supply this joint law. The conditional prescribed-arrow calculation above establishes the needed independence rather than assuming it.

## Limitations
This is an asymptotic law under the *uniform incident-edge* sampling measure; it need not describe angles under length-biased or normal-cone sampling. The limiting law is discrete and non-Gaussian; convergence in distribution alone does not assert uniform integrability of arbitrary powers. Historical priority is provisional pending specialist comparison with possibly unindexed permutation-cycle overlap results, particularly those formulated without polyhedral terminology. No independent mathematical audit is claimed.

## References
[1] D. Kane, S. Lovett, S. Rao, *The independence number of the Birkhoff polytope graph, and applications to maximally recoverable codes*, arXiv:1702.05773, first submitted 2017-02-19. https://arxiv.org/abs/1702.05773

[2] I. Bengtsson, Å. Ericsson, M. Kuś, W. Tadej, K. Życzkowski, *Birkhoff's polytope and unistochastic matrices, N=3 and N=4*, arXiv:math/0402325, 2004; *Communications in Mathematical Physics* **259** (2005), 307–324. https://arxiv.org/abs/math/0402325

[3] H. Mui, *Coalescence Probabilities of Cycle Products*, arXiv:2409.01415, first submitted 2024-09-02. https://arxiv.org/abs/2409.01415
