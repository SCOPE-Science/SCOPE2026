# A uniform Brownian distance-field limit for Bernoulli recursive trees

## Finding

**Theorem.** Fix \(p\in(0,1)\) and put \(q=1-p\). Start with the edge \(v_0v_1\). Independently for each \(k\ge2\), give \(v_k\) parent \(v_{k-1}\) with probability \(p\), or \(v_{k-2}\) with probability \(q\). Let \(T_n\) be the tree on \(v_0,\ldots,v_n\), and write \(d_n\) for its graph distance. Define
\[
\mu=\frac{1}{1+q},\qquad
\sigma^2=\frac{pq}{(1+q)^3}>0.
\]

For the grid \(s=i/n,t=j/n\), \(0\le i,j\le n\), set
\[
Z_n(i/n,j/n)=\frac{d_n(v_i,v_j)-\mu|i-j|}{\sqrt n},
\]
and extend \(Z_n\) bilinearly across each grid square. In \(C([0,1]^2)\) with the uniform topology,
\[
Z_n\ \Longrightarrow\ Z,\qquad
Z(s,t)=\sigma\bigl(B(\max\{s,t\})-B(\min\{s,t\})\bigr),
\]
where \(B\) is standard Brownian motion. Thus for two ordered intervals \(I=[a,b]\) and \(J=[c,d]\),
\[
\operatorname{Cov}(Z(a,b),Z(c,d))=\sigma^2|I\cap J|.
\]

Furthermore, almost surely,
\[
\max_{0\le i,j\le n}\left|d_n(v_i,v_j)-\mu|i-j|\right|=o(n),
\]
and the finite metric-measure spaces \((V(T_n),d_n/n,\operatorname{Unif}(V(T_n)))\) converge in the measured Gromov--Hausdorff--Prokhorov sense to \(([0,\mu],|\cdot|,\operatorname{Unif}[0,\mu])\).

Let \(\operatorname{Diam}_n\) be the diameter, and set
\[
\overline d_n=\frac{2}{n(n+1)}\sum_{0\le i<j\le n}d_n(v_i,v_j).
\]
Then the same distance-field theorem gives
\[
\frac{\operatorname{Diam}_n-\mu n}{\sqrt n}\Longrightarrow N(0,\sigma^2),
\qquad
\sqrt n\left(\frac{\overline d_n}{n}-\frac\mu3\right)
\Longrightarrow N\left(0,\frac{2\sigma^2}{15}\right).
\]
These two consequences are projections of the *same* field limit, rather than additional independent findings.

## Assumptions and scope

All attachment choices are independent Bernoulli variables with the same fixed parameter \(0<p<1\). The root is \(v_0\); graph edges have unit length. Limits are taken as \(n\to\infty\) through positive integers. The second-order field is indexed by *birth times*, not by two vertices sampled independently after the tree has grown. The finite metric spaces have the uniform probability measure on their \(n+1\) vertices. Measured Gromov--Hausdorff--Prokhorov convergence means that Hausdorff distance and Prokhorov distance both tend to zero under suitable common isometric embeddings. The degenerate boundary parameters \(p=0\) and \(p=1\) are not part of the theorem.

## Proof

**Step 1: an exact two-state height recursion.** Write \(H_k=d_n(v_0,v_k)\), independent of the final \(n\ge k\), and let \(X_k=H_k-H_{k-1}\), with \(X_1=1\). For \(k\ge2\), let \(A_k\) indicate attachment to \(v_{k-1}\). Then
\[
X_k=\begin{cases}1,&A_k=1,\\1-X_{k-1},&A_k=0.\end{cases}
\]
In particular \(X_k\in\{0,1\}\), \(H_k\) is nondecreasing, and \(H_k=\sum_{j=1}^kX_j\). Given the past \(\mathcal F_{k-1}\),
\[
\mathbb E(X_k\mid\mathcal F_{k-1})=1-qX_{k-1}.
\]
Its stationary mean is \(\mu=1/(1+q)\). Set \(Y_k=X_k-\mu\) and \(\xi_k=Y_k+qY_{k-1}\) for \(k\ge2\). The \(\xi_k\) are bounded martingale differences, and telescoping yields the *exact identity*, for every \(m\ge1\),
\[
(1+q)(H_m-\mu m)=\sum_{k=2}^m\xi_k+Y_1+qY_m.
\tag{1}
\]
The remainder \(Y_1+qY_m\) is bounded uniformly in \(m\). The predictable quadratic variation of the martingale on the right is
\[
\sum_{k=2}^m\mathbb E(\xi_k^2\mid\mathcal F_{k-1})
=pq\sum_{k=2}^mX_{k-1}.
\tag{2}
\]
A martingale strong law (or the bounded-difference concentration inequality) applied to (1) shows \(H_m/m\to\mu\) almost surely. Therefore the right side of (2), divided by \(m\), tends to \(pq\mu\). Bounded jumps ensure the conditional Lindeberg condition. The martingale functional central limit theorem applied to (1) gives
\[
\left(\frac{H_{\lfloor nt\rfloor}-\mu\lfloor nt\rfloor}{\sqrt n}\right)_{0\le t\le1}
\Longrightarrow (\sigma B(t))_{0\le t\le1}.
\tag{3}
\]
Here convergence can equivalently be stated for the continuous piecewise-linear interpolation of the heights.

**Step 2: a simultaneous deterministic ancestor bound.** Call \(k=1\) a forced success, and for \(k\ge2\) call \(k\) a success if \(A_k=1\). Whenever \(k\) is a success, \(v_{k-1}\) is an ancestor of *every* vertex with index at least \(k\): both \(v_k\) and \(v_{k+1}\) descend from \(v_{k-1}\), so induction covers all later vertices. For \(1\le i<j\le n\), let \(k\le i\) be the last success. Their lowest common ancestor therefore lies at height at least \(H_{k-1}\). Since the height increments are zero or one,
\[
0\le d_n(v_i,v_j)-(H_j-H_i)
=2(H_i-H_{\operatorname{LCA}(i,j)})
\le2(i-k+1).
\tag{4}
\]
For \(i=0\), the difference is zero. If \(L_n\) is the longest consecutive string of failures among \(A_2,\ldots,A_n\), (4) yields the uniform deterministic comparison
\[
0\le d_n(v_i,v_j)-|H_j-H_i|\le2(L_n+1)
\quad (0\le i,j\le n).
\tag{5}
\]
A union bound gives \(\Pr(L_n\ge r)\le nq^r\). Choosing \(r=\lceil 3\log n/|\log q|\rceil\) and using Borel--Cantelli establishes \(L_n=O(\log n)\) almost surely.

**Step 3: uniform Gaussian field and metric limit.** Combine (3) and (5). On the grid, the supremum of the difference between \(Z_n(i/n,j/n)\) and the height-increment field
\[
\frac{(H_{\max\{i,j\}}-\mu\max\{i,j\})-(H_{\min\{i,j\}}-\mu\min\{i,j\})}{\sqrt n}
\]
is at most \(2(L_n+1)/\sqrt n\to0\) almost surely. Piecewise-linear interpolation of the heights is a continuous-map input, and bilinear interpolation of these grid fields changes their supremum norm by at most the modulus of continuity across mesh size \(1/n\). Because the limiting height process is continuous, (3) and the continuous mapping theorem prove the asserted uniform functional convergence in \(C([0,1]^2)\).

The strong law in Step 1 and (5) also show uniform \(d_n(v_i,v_j)/n-\mu|i-j|/n\to0\) almost surely. Identify vertex \(v_i\) with the point \(\mu i/n\) in \([0,\mu]\); the distortion of this correspondence tends to zero and the pushed-forward empirical measure converges to uniform Lebesgue measure. This proves the claimed measured metric-space limit.

**Step 4: diameter and mean pair distance.** Since heights are nondecreasing and \(d_n(v_0,v_n)=H_n\), (5) gives
\[
H_n\le\operatorname{Diam}_n\le H_n+2(L_n+1).
\]
Thus (3) at \(t=1\) proves the diameter CLT. For the all-pairs mean, the deterministic baseline is exactly
\[
\frac{2\mu}{n(n+1)}\sum_{0\le i<j\le n}(j-i)=\frac{\mu(n+2)}3.
\]
The uniform field limit and Riemann sums on \(\{(s,t):0\le s<t\le1\}\) show that the centered, rescaled pairwise mean converges to
\[
2\sigma\int_0^1\!\int_s^1 (B(t)-B(s))\,dt\,ds
=2\sigma\int_0^1 t(1-t)\,dB(t).
\]
The Itô isometry gives variance \(4\sigma^2\int_0^1t^2(1-t)^2dt=2\sigma^2/15\). This proves all assertions.

## Verification

The supplied standalone `check.py` enumerates every attachment sequence through vertex index 13 (12 independent attachment decisions) and checks the two-state recursion, the uniform pairwise-distance inequality, the edge-cut identity for total pairwise distance, and the diameter bound. It also compares exact rational height first and second moments against closed recurrences for five rational reinforcement probabilities and checks the martingale identity pathwise. Separately, deterministic-seed simulations assess variance-scale sanity in the height and pairwise mean, without treating finite Monte Carlo as an asymptotic proof.

Execute in a standard Python 3 environment using `python3 check.py`. The checker contains no nonstandard dependencies. It reports 708,747 assertions passed: 708,743 finite identity/exact arithmetic checks and four simulation-tolerance checks. The mathematical proof above, not these finite tests, establishes the infinite-limit statements.

## Relationship to prior work

Tang, Wang and Wu (2026, arXiv:2607.02916) introduce exactly the preceding-two-vertex attachment rule and prove one-endedness and infinite collisions. Their Section 3 also characterizes trunk steps and branch lengths and cites bounds for the longest failure run. These ingredients are close background; the present claim does **not** assert originality for those branch or run facts. Their stated theorems and sections do not contain the full birth-time-indexed Brownian *pairwise-distance field*, its interval-overlap covariance, the measured linear interval limit, or the joint-derived diameter and pair-mean fluctuation constants.

Iksanov and Kabluchko (2018, arXiv:1801.04606) establish a functional theorem for the number of vertices at fixed low levels in *uniform recursive trees*, whose parent choices range over all earlier vertices. Berzunza Ojeda and Janson (2020, arXiv:2009.00572) study distance profiles of *conditioned Galton--Watson/simply generated trees* at square-root distance scale with the Brownian continuum random tree as limit. These are mathematically related but have different tree laws, normalization, and observables. The present result concerns a linear-distance, nearly path-like model with second-order Gaussian fluctuations for every pair of birth times. No priority claim about general abstract martingale or metric transfer principles is made.

## Limitations

The parameter \(p\) is fixed strictly between zero and one. No uniformity in a sequence of changing probabilities \(p=p_n\), rates of weak convergence, exact finite-sample law, or independent verification is asserted. The Gaussian field is an *annealed* distributional limit with respect to tree randomness, not a quenched limit for additional walk trajectories on a fixed tree. The novelty comparison is based on identified literature and accessible scientific records; it cannot rule out an unlocated broader theorem whose hypotheses imply this particular model.

## References

1. J.-s. Tang, F. Wang and X.-Y. Wu, *Infinite collisions of simple random walks on random recursive trees generated by Bernoulli sequences*, arXiv:2607.02916, first submitted 3 July 2026. https://arxiv.org/abs/2607.02916
2. A. Iksanov and Z. Kabluchko, *A functional limit theorem for the profile of random recursive trees*, arXiv:1801.04606 (2018). https://arxiv.org/abs/1801.04606
3. G. Berzunza Ojeda and S. Janson, *The distance profile of rooted and unrooted simply generated trees*, arXiv:2009.00572 (2020). https://arxiv.org/abs/2009.00572
4. C. Mailler and G. Uribe Bravo, *Random walks with preferential relocations and fading memory: a study through random recursive trees*, arXiv:1810.02735 (2018). https://arxiv.org/abs/1810.02735
