# Five-to-one transition in the sharp Lipschitz spread of bridge-connected cliques

## Finding

Let \(B_{m,n}\), for integers \(m,n\ge2\), denote the unweighted *bridge barbell*: disjoint cliques of orders \(m\) and \(n\), joined by a single unit edge between distinguished vertices. All vertices have uniform mass. Write \(N=m+n\), \(L=\min(m,n)\), and \(H=\max(m,n)\). Then the sharp real Lipschitz variance is

\[
\operatorname{spr}(B_{m,n})=\max_{\lvert f(u)-f(v)\rvert\le1\ (uv\in E)}\frac1N\sum_{v}\bigl(f(v)-\overline f\bigr)^2
=\frac{9mn-4N+\left\lfloor (H-5L)_+^2/4\right\rfloor}{N^2},
\]

where \(x_+=\max(x,0)\). All extremizers have the following precise form up to adding a constant, multiplying by \(-1\), and permuting the nondistinguished clique vertices: orient the bridge from the smaller clique to the larger clique, give its endpoints values \(0,1\), give **all** other vertices of the smaller clique value \(-1\), and give \(d\) of the other vertices of the larger clique value \(1\) and its remaining \(H-1-d\) vertices value \(2\). Exactly the integer values

\[
d\in\operatorname*{argmax}_{e\in\mathbb Z_{\ge0}} e(H-5L-e)
=\begin{cases}
\{0\},&H\le5L,\\
\{\lfloor(H-5L)/2\rfloor,\lceil(H-5L)/2\rceil\},&H>5L
\end{cases}
\]

are allowed (duplicate entries in the set are interpreted once). These values are all at most \(H-1\). If \(m=n\), either clique may be designated first.

The first nontrivial tie with a partly occupied larger clique occurs precisely at \(H=5L+1\); the partially occupied construction gives a strictly greater variance than the fully separated construction for every \(H\ge5L+2\). The exact *numerator* gain relative to the fully separated configuration is \(\lfloor (H-5L)_+^2/4\rfloor\).

At fixed total order \(N\), the sharp spread increases strictly whenever the smaller clique is enlarged by one vertex and the larger reduced by one, as long as the smaller clique remains no larger than the other. In fact the exact numerator is

\[
N^2\operatorname{spr}(B_{L,N-L})=
\begin{cases}
\lfloor N^2/4\rfloor+6NL-4N,&N-L\ge5L,\\
9L(N-L)-4N,&N-L\le5L.
\end{cases}
\]

At the shared boundary both expressions agree.

## Assumptions and scope

The graph contains precisely two vertex-disjoint complete graphs, including their bridge endpoints, and exactly one bridge edge. Every edge has unit length, the distance is graph shortest-path distance, and the measure is uniform on *all* \(N\) vertices. The optimization concerns real functions with edge differences bounded by one. No restriction to integer-valued functions is imposed. The formula is valid for every pair of integers \(m,n\ge2\), including \(B_{2,2}=P_4\).

## Proof

**Step 1: extrema must saturate and have few values.** Normalize one bridge endpoint to value zero. The admissible functions form a compact convex polytope. The centered squared norm is strictly convex after this normalization: its quadratic part is positive definite on the anchored subspace. Consequently every maximizer is an extreme point. For fixed within-clique value differences, translate the whole second clique relative to the first. Feasibility permits the second bridge-endpoint value to range over \([-1,1]\), and the variance is a strictly convex quadratic in this displacement, with strictly positive quadratic coefficient \(mn/N^2\). Therefore the bridge must be saturated. By replacing \(f\) with \(-f\) if needed, the bridge endpoints are \(0,1\).

Now fix both bridge endpoints. If the tight-edge graph inside either clique were disconnected, one tight component could be shifted by a sufficiently small positive and negative amount, contradicting extreme-point status. The tight edges therefore connect every vertex to the distinguished root. Since tight edges carry differences \(\pm1\), all values in the first clique are integers; as all its pairwise distances are one and its root value is zero, they belong to \(\{-1,0\}\) or \(\{0,1\}\). Similarly the second clique uses \(\{0,1\}\) or \(\{1,2\}\). (The all-constant case is harmless for this necessary condition.)

**Step 2: strict reflection.** The variance has the pairwise form

\[
N^2\operatorname{Var}(f)=\sum_{\{u,v\}\subset V}\bigl(f(u)-f(v)\bigr)^2.
\]

If a first-clique vertex has value \(1\), reflect all values on that clique through zero. Intra-clique distances do not change, but for every cross-clique vertex of value \(y\ge0\), replacing \(1\) by \(-1\) increases its squared difference by \(4y\). The other bridge endpoint has \(y=1\), so the increase is strict. Hence every maximizing first-clique value is \(-1\) or \(0\). Next, if a second-clique vertex has value \(0\), reflect the entire second clique through the value \(1\). For each first-clique value \(x\le0\), replacing \(0\) by \(2\) increases the squared cross difference by \(4(1-x)>0\). Hence every maximizing second-clique value is \(1\) or \(2\).

**Step 3: exact discrete quadratic.** Let \(k\) be the number of first-clique vertices at \(-1\) and \(\ell\) the number of second-clique vertices at \(2\), excluding bridge endpoints. Then \(0\le k\le m-1\), \(0\le\ell\le n-1\), and

\[
\sum_v f(v)=n-k+\ell,\qquad \sum_v f(v)^2=n+k+3\ell.
\]

Thus the unnormalized numerator is

\[
F(k,\ell)=N(n+k+3\ell)-(n-k+\ell)^2.
\]

Take the first clique to be the smaller one, \(m=L\le n=H\). The forward difference in \(k\) is \(F(k+1,\ell)-F(k,\ell)=N+2(H-k+\ell)-1>0\). Therefore every maximizer has \(k=L-1\). Write \(\ell=H-1-d\), where \(0\le d\le H-1\). Direct expansion gives

\[
F(L-1,H-1-d)=9LH-4N+d(H-5L-d).
\]

The concave integer quadratic is maximized by \(d=0\) when \(H\le5L\), and otherwise by the nearest integer(s) to \((H-5L)/2\); they are admissible because \(0\le(H-5L)/2<H-1\). The improvement equals \(\lfloor(H-5L)_+^2/4\rfloor\). This proves the formula and, because every preceding step was strict unless the stated structure held, the complete equality classification.

**Step 4: fixed-order balance and the threshold.** At fixed \(N=L+H\), if \(H\ge5L\), expanding the square in the floor gives \(N^2\operatorname{spr}=\lfloor N^2/4\rfloor+6NL-4N\), which increases by \(6N\) when \(L\) increases by one within that region. If \(H\le5L\), the numerator is \(9L(N-L)-4N\), whose forward increment is \(9(N-2L-1)>0\) while the smaller part can grow. The expressions meet at the boundary \(L=N/6\), so the discrete sequence is strictly increasing throughout. Finally the transition at \(H=5L+1\) has a tie between \(d=0,1\), while \(H\ge5L+2\) has positive gain.

## Verification

Run the standalone Python 3 script `verify_barbell_spread.py` with no third-party packages. The checker independently enumerates all anchored integral Lipschitz functions for small cliques, all labelled extreme-clique profiles for a larger range, reduced exact integer quadratic optima for 16,384 parameter pairs, exact transition ties over 46,501 cases, and fixed-order balancing over 296 total orders. It uses integer arithmetic; these finite tests corroborate but do not substitute for the all-parameter analytical proof.

A useful boundary check is \(B_{2,2}=P_4\), where the formula returns variance \(5/4\), attained by a length-three path height function. The diameter bound \(\operatorname{spr}(B_{m,n})\le9/4\) is respected, and for \(m=n\to\infty\) the formula approaches \(9/4\) from below.

## Relationship to prior work

Alon–Boppana–Spencer introduced the spread constant for finite metric spaces, showed the existence of integral maximizers, and used it in asymptotic product-space isoperimetry. Addario-Berry–Janson–McDiarmid examined spread for random graphs. Yancey studied general structural properties of variance-optimal functions and examples on trees and cycles. Those structural results are background and are not claimed anew. The present result is the specific sharp formula and complete equality classification for **two cliques joined by a bridge**, including the integer five-to-one transition. The same graph family has been studied for other invariants such as negative type, heat-flow Lipschitz norms, and zero forcing; those invariant calculations do not determine the sharp centered Lipschitz variance. Literature coverage cannot exclude all unindexed or independently named equivalent results.

## Limitations

The theorem assumes two cliques, a single unit bridge, uniform vertex mass, and real quadratic variance. It does not give the spread of heterogeneous block graphs with longer bridges, weighted edges, nonuniform masses, or higher centered moments. The equality classification is for all real-valued admissible functions; finite checking is used only as a consistency test. The originality conclusion is limited to the sources inspected and recorded in the accompanying review.

## References

1. N. Alon, R. Boppana, J. Spencer, *An Asymptotic Isoperimetric Inequality*, Geometric and Functional Analysis 8 (1998), 411–436. Author-hosted manuscript: https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf ; DOI:10.1007/s000390050062.
2. L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, first arXiv posting 2009-02-06, https://arxiv.org/abs/0902.1156.
3. M. P. Yancey, *Probabilistic and Geometrical Applications to Graph Theory*, first arXiv posting 2017-05-26, https://arxiv.org/abs/1705.09725.
4. S. Bobkov, C. Houdré, P. Tetali, *\(\lambda_\infty\), Vertex Isoperimetry and Concentration*, Combinatorica 20 (2000), 153–172, DOI:10.1007/s004930070018.
