# A skew-beta stationary law for two opposed zealots on complete bipartite voter networks

## Finding

On the complete bipartite graph \(K_{m,n}\), fix one \(+\) voter permanently in the part of size \(m\) and one \(-\) voter permanently in the part of size \(n\). Each other voter copies a uniformly chosen neighbor at rate one. Write \(P_{m,n}\) and \(Q_{m,n}\) for the fractions of \(+\) vertices in the respective parts, sampled from the unique stationary distribution. Suppose \(m,n\to\infty\) with \(n/(m+n)\to\theta\in(0,1)\). Then

\[
(P_{m,n},Q_{m,n})\ \xrightarrow{\mathrm d}\ (Z,Z),\qquad
Z\sim\operatorname{Beta}(2\theta,2(1-\theta)).
\]

The overall positive fraction \(M_{m,n}=(mP_{m,n}+nQ_{m,n})/(m+n)\) therefore converges to the same beta law. In particular, equal part sizes produce the uniform law on \([0,1]\); unequal part sizes create a skew distribution even though there is exactly one frozen voter of each sign. The limiting variance of the overall positive fraction is \(\theta(1-\theta)/3\), which is strictly positive. At every finite \(m,n\ge2\), the stationary means obey

\[
\mathbb E P_{m,n}=\frac{n}{m+n-1},\quad
\mathbb E Q_{m,n}=\frac{n-1}{m+n-1},\quad
\mathbb E M_{m,n}=\frac{n}{m+n}.
\]

## Assumptions and scope

For integers \(m,n\ge2\), the graph is the simple undirected \(K_{m,n}\). Frozen voters copy nobody and never change. Every *nonfrozen* vertex has an independent rate-one clock, and at each ring copies the present opinion of a uniformly selected opposite-part vertex. Sampling an agreeing neighbor causes no state change. The stationary law refers to this finite continuous-time chain, rather than a quasistationary law conditioned on nonconsensus. The one frozen \(+\) vertex is in the \(m\)-part and the one frozen \(-\) vertex is in the \(n\)-part. The ratio limit is interior; no claim is made for \(n/(m+n)\to0\) or \(1\).

Let \(i\) count positive *mutable* vertices in the \(m\)-part and \(j\) count positive mutable vertices in the \(n\)-part. Thus \(0\le i\le m-1\), \(0\le j\le n-1\), with \(p=(i+1)/m\), \(q=j/n\). The count process jumps by one coordinate with rates

\[
\begin{array}{ll}
(i,j)\to(i+1,j): &(m-1-i)j/n,\\
(i,j)\to(i-1,j): &i(n-j)/n,\\
(i,j)\to(i,j+1): &(n-1-j)(i+1)/m,\\
(i,j)\to(i,j-1): &j(m-1-i)/m.
\end{array}
\]

The corner \((m-1,0)\) has no incoming transitions and is transient. All remaining count states form a communicating class: any state can reach \((0,0)\) by copying the frozen negative vertex into mutable first-part sites and then copying negative first-part sites into mutable second-part sites; conversely, from \((0,0)\) the frozen positive vertex creates second-part positives, which can create first-part positives, after which positive second-part sites can be removed whenever at least one mutable first-part negative remains. The exceptional corner can enter this closed class, but no transition returns to it. Therefore the count chain has a unique stationary law; this suffices for all observables considered here.

## Proof

**1. Exact stationary means.** Let \(L\) be the count-chain generator. Directly from the four rates,

\[
Lp=q-p+\frac{1-q}{m},\qquad Lq=p-q-\frac p n.
\]

Taking stationary expectations and solving the two linear equations gives

\[
\mathbb E p=\frac{n}{m+n-1},\quad
\mathbb E q=\frac{n-1}{m+n-1},\quad
\mathbb E(p-q)=\frac{1}{m+n-1}.
\]

The formula for \(\mathbb E M_{m,n}\) follows by degree-weighting these means. No mean-field approximation is used here.

**2. Synchronization between parts.** Put \(D=p-q\), \(h=1/m+1/n\), and \(c=(1-q)/m+p/n\). The generator satisfies \(LD=-2D+c\) with \(0\le c\le h\). The predictable quadratic-variation rate of \(D\), denoted \(a_D\), satisfies

\[
0\le a_D\le\frac{m-1}{m^2}+\frac{n-1}{n^2}\le h.
\]

Stationarity applied to \(D^2\) yields \(0=\mathbb E[-4D^2+2Dc+a_D]\). Since \(2Dc\le D^2+h^2\),

\[
\mathbb E D^2\le\frac{h+h^2}{3}\longrightarrow0.
\]

Hence both parts have the same macroscopic random positive fraction, although they need not have the same finite-size mean.

**3. Limiting one-dimensional generator.** Define \(X=(p+q)/2\), \(T=2mn/(m+n)\), \(\theta_{m,n}=n/(m+n)\). The exact scaled drift and quadratic-variation rate of \(X\) are

\[
T LX=\theta_{m,n}-X+(\theta_{m,n}-\tfrac12)D,
\]

\[
T a_X=X(1-X)+\frac{D^2}{4}
-\frac{n(1-q)}{2m(m+n)}
-\frac{mp}{2n(m+n)}.
\]

As \(m,n\to\infty\) at an interior fixed proportion, the error in the drift vanishes in stationary \(L^1\) by Step 2; the quadratic-variation error vanishes likewise. The jump sizes of \(X\) are \(1/(2m)\) or \(1/(2n)\). Since the total rate is at most \(m+n\), after multiplication by \(T\) the Taylor remainder in \(T Lf(X)\) is bounded by a constant depending on \(f\) times \((m+n)T\max(m^{-3},n^{-3})=O(1/\min(m,n))\) for every \(f\in C^3([0,1])\). Thus, under stationarity,

\[
0=\lim\mathbb E[T Lf(X)]
=\lim\mathbb E\left[(\theta-X)f'(X)+\tfrac12X(1-X)f''(X)\right]
\]

along any convergent subsequence of stationary laws. Compactness of \([0,1]\) ensures subsequential weak limits exist; the displayed equation is valid for each such limit.

**4. Unique identification.** Let \(\mu_k\) be the \(k\)-th moment of any weak subsequential limit, with \(\mu_0=1\). In the preceding identity choose \(f(x)=x^k\), for every integer \(k\ge1\). Division by \(k\) gives

\[
0=\left(\theta+\frac{k-1}{2}\right)\mu_{k-1}
-\frac{k+1}{2}\mu_k,
\qquad
\mu_k=\frac{2\theta+k-1}{k+1}\mu_{k-1}.
\]

Here \((a)_k=a(a+1)\cdots(a+k-1)\) is the rising factorial. These are precisely the moments \(\mu_k=(2\theta)_k/(2)_k\) of \(\operatorname{Beta}(2\theta,2(1-\theta))\), whose density is \[\frac{x^{2\theta-1}(1-x)^{1-2\theta}}{B(2\theta,2-2\theta)}\,\quad0<x<1,\] with \(B\) the beta integral normalizer. A probability law on the compact interval \([0,1]\) is uniquely determined by its polynomial moments, proving convergence of \(X\) without a boundary-condition assumption. Step 2 and the continuous mapping theorem imply \((p,q)\Rightarrow(Z,Z)\); the same holds for \(M\), a convex combination of \(p,q\). The beta variance is \(2\theta\cdot2(1-\theta)/(2^2\cdot3)=\theta(1-\theta)/3\). This proves the finding.

## Verification

The accompanying standalone `verify.py` enumerates every allowable labeled neighbor-copy update on small graphs and checks its aggregation against the exact four transition rates. It then checks the drift, quadratic variation and associated identities using exact rational arithmetic at every count state for six graph sizes. Exact rational stationary distributions on five small graphs confirm the finite-size means and the zero stationary mass of the transient corner. Additional sparse numerical solves compare the first four moments for three larger bipartite graphs to the predicted beta moments. Run with `python verify.py` using Python, NumPy, SciPy and SymPy. These are finite diagnostics; the convergence proof is Steps 2–4 above.

## Relationship to prior work

Mobilia, Petersen and Redner (2007) study competing zealots in a fully connected voter population and on spatial lattices; their complete-graph law does not specify the degree-heterogeneous bipartite topology or the skew-beta shape coefficients. Pickering and Lim (2014) study the ordinary voter model on the complete bipartite graph *without fixed opposing voters*: their spectral consensus analysis has absorbing configurations and is not a statement about the positive-recurrent stationary chain here. Mobilia (2015) treats the nonlinear \(q\)-voter model on a well-mixed population. Mori, Hisakado and Nakayama (2018) obtain beta-type densities for a different, many-voters-per-node model with intrinsic preference noise and a network diffusion limit. Abstract-level comparison to Yildiz and collaborators (2013) establishes that they derive moments for binary opinions with stubborn agents on arbitrary graphs, but their full text could not be accessed; possible implications of that framework are a priority risk. The claim is the exact finite-size first moments together with the interior-ratio joint stationary skew-beta limit, not generic beta limits or voter-model duality alone.

## Limitations

This is a stationary weak limit for \(m,n\to\infty\) with both parts occupying positive proportions. It does not give convergence rates, equilibration times, microscopic correlations, or a formula for the complete finite stationary joint distribution. The corner \((m-1,0)\) is transient, so no strict positivity claim applies to all count states. Source comparisons support novelty only on examined material; inaccessible or unindexed work may contain a stronger equivalent theorem.

## References

- M. Mobilia, A. Petersen, S. Redner, “On the Role of Zealotry in the Voter Model,” arXiv:0706.2892, first submitted 20 June 2007. https://arxiv.org/abs/0706.2892 (full text: https://arxiv.org/html/0706.2892v2).
- W. Pickering, C. Lim, “Solution of the Voter Model by Spectral Analysis,” arXiv:1408.2130, first submitted 9 August 2014. https://arxiv.org/abs/1408.2130.
- M. Mobilia, “Nonlinear \(q\)-voter model with inflexible zealots,” arXiv:1506.04911, first submitted 16 June 2015. https://arxiv.org/abs/1506.04911.
- Shintaro Mori, Masato Hisakado, Kazuaki Nakayama, “A voter model on networks and multivariate beta distribution,” arXiv:1810.05643, 2018. https://arxiv.org/abs/1810.05643.
- M. E. Yildiz, A. Ozdaglar, D. Acemoglu, A. Saberi, A. Scaglione, “Binary Opinion Dynamics with Stubborn Agents,” ACM Trans. Economics and Computation (2013), DOI:10.1145/2538508. Full text not accessed.
