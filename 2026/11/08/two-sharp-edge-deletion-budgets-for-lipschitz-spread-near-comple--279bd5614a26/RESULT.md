# Two sharp edge-deletion budgets for Lipschitz spread near complete graphs

## Finding

Let \(n\ge4\), let \(B_n=\lfloor n^2/4\rfloor\), and consider all connected simple graphs \(G\) on \(n\) vertices, each endowed with unit-edge distance and uniform vertex probability. Write \(H=\overline G\) for its graph of missing edges, and define
\[
\operatorname{spr}(G)=\max_{|f(u)-f(v)|\le1\,\text{on every edge}}\left(\frac1n\sum_{v}f(v)^2-\left(\frac1n\sum_vf(v)\right)^2\right).
\]

Two **exact extremal budgets** hold:

1. For every integer \(0\le k\le\lfloor(n-2)/2\rfloor\), among graphs with at most \(k\) missing edges,
\[
\max_{|E(H)|\le k}\operatorname{spr}(G)=
\begin{cases}
 B_n/n^2,& k=0,\\
 n^{-2}\max\{B_n,\,n(k+1)-(k-1)^2\},&k\ge1.
\end{cases}
\]
The extremal value is attained by deleting the \(k\) edges of a star from the complete graph. Once \(n(k+1)-(k-1)^2>B_n\), this star-deletion graph is the **unique extremal graph up to isomorphism**; its maximizing functions (modulo constants and global sign) take values \(-1\) at the star center, \(+1\) at its \(k\) leaves, and \(0\) elsewhere. The first strict increase occurs with exactly
\[
 k_*(n)=1+\left\lfloor\frac{n+2-\sqrt{8n+(n\bmod 2)}}2\right\rfloor
\]
missing edges. Every deletion set of smaller size preserves the complete-graph spread, while a deleted \(k_*(n)\)-edge star increases it.

2. For every integer \(0\le r<n/2\), among graphs in which each vertex loses at most \(r\) of its original complete-graph neighbors,
\[
\max_{\Delta(H)\le r}\operatorname{spr}(G)=n^{-2}\max\{B_n,\,2nr\}.
\]
The value is attained by deleting all edges of a \(K_{r,r}\) on two disjoint vertex sets and leaving every other edge intact (when \(r=0\), this means no deletion). If \(2nr>B_n\), a graph attains the budget maximum **if and only if** its missing-edge graph has a \(K_{r,r}\) component; the other missing-edge components may be arbitrary subject to degree at most \(r\). Every maximizing function in this strict regime is, up to translation and sign, \(-1\) and \(+1\) on the two sides of such a component and zero off it. Hence the largest degree-deletion budget preserving spread for **every** graph is
\[
 r_*(n)=\left\lfloor\frac{B_n}{2n}\right\rfloor.
\]
At the next integer budget, a deleted complete biclique produces a strict increase.

These are sharp adversarial stability laws in two different norms of the deletion pattern, rather than estimates for a prescribed random edge-deletion model.

## Assumptions and scope

The graphs are finite, undirected, simple, unweighted, connected, and have \(n\ge4\) vertices. The missing-edge graph \(H\) is taken on exactly the same vertex set. The vertex measure is uniform, the function values are real, and spread is the squared operator norm of the canonical centered inclusion of graph Lipschitz functions (modulo constants) into \(L^2\). The edge-budget equality is claimed only for \(k\le\lfloor(n-2)/2\rfloor\); the degree-budget equality holds for every integer \(r<n/2\). No formula for larger deletion budgets is claimed.

## Proof

**Step 1 (diameter and integer extrema).** If \(\Delta(H)<n/2\), each nonedge \(uv\) of \(G\) has at least \(n-2\Delta(H)\ge1\) common neighbors in \(G\): among the other \(n-2\) vertices, at most \(2(\Delta(H)-1)\) fail to connect to \(u\) or \(v\). Hence \(G\) has diameter at most two. Both deletion-budget regimes in the theorem satisfy this bound: \(\Delta(H)\le|E(H)|\le k\le(n-2)/2\) in the first, and \(\Delta(H)\le r<n/2\) in the second.

Every maximizing Lipschitz function, after fixing one value to zero, has an integer value at every vertex. Indeed, take its tight-edge subgraph, retaining exactly edges with absolute value difference one. If this subgraph were disconnected, perturbing one proper component by a small positive or negative amount would remain feasible. The variance along this perturbation is a strictly convex quadratic, contradicting maximality. Therefore the tight-edge subgraph is connected, and all values differ by integers along its paths. After subtracting the minimum, a maximizer consequently takes only values \(0,1,2\). This reproduces the relevant extreme-potential principle of Alon, Boppana, and Spencer; integrality is not asserted as new.

**Step 2 (missing biclique).** If the potential takes only \(0\) and \(1\), its variance is at most \(B_n/n^2\), with equality for every balanced binary partition, always Lipschitz on every graph. Otherwise let \(A\) and \(B\) be its nonempty \(0\)- and \(2\)-level sets, of sizes \(a,b\ge1\); all remaining vertices have value one. Every \(A\)-to-\(B\) pair must be a missing edge of \(G\), so \(H\) contains a complete crossing bipartite graph between \(A\) and \(B\). With \(p=ab\) and \(t=a+b\), a direct variance calculation yields
\[
 n^2\operatorname{Var}(f)=n(a+b)-(a-b)^2=t(n-t)+4p.
\]
Conversely any disjoint nonempty sets \(A,B\) whose complete crossing edges are missing determine such a feasible three-level function, regardless of other edges of \(G\). This is an exact reduction, not a relaxation.

**Step 3 (total missing-edge budget).** Suppose \(1\le k\le\lfloor(n-2)/2\rfloor\) and \(|E(H)|\le k\). Then \(p=ab\le k\), and
\[
 t=a+b\le ab+1=p+1\le k+1\le n/2,
\]
since \(p+1-t=(a-1)(b-1)\ge0\). The function \(q(s)=s(n-s)\) increases strictly on this range, hence
\[
 n^2\operatorname{Var}(f)=q(t)+4p\le q(p+1)+4p
 =n(p+1)-(p-1)^2\le n(k+1)-(k-1)^2.
\]
The last inequality is strict when \(p<k\), because the right-hand polynomial increases over \(1\le p\le k\); its successive increment at \(p\) is \(n-2p+1>0\). Equality in this upper bound requires \(p=k\) and \(a+b=p+1\), equivalently \(\min(a,b)=1\). Since the \(k\) crossing edges are already all missing edges, \(H\) must itself be the \(k\)-edge star. Conversely that star gives a feasible \(-1,0,+1\) potential with the displayed variance. Combining with the binary value proves the first formula, uniqueness in the strictly super-binary regime, and the complete optimizer description there.

The quadratic difference \(n(k+1)-(k-1)^2-B_n\) has smaller real root
\[
 \rho_n=\frac{n+2-\sqrt{8n+(n\bmod2)}}2.
\]
Its larger root exceeds the permitted range. At \(k=\lfloor(n-2)/2\rfloor\), this difference is positive for every \(n\ge4\), so the smallest increasing integer is exactly \(k_*(n)=\lfloor\rho_n\rfloor+1\), including cases where \(\rho_n\) is an integer.

**Step 4 (maximum lost degree).** If \(\Delta(H)\le r<n/2\), any nonempty opposite level sets satisfy \(a,b\le r\) because each vertex in either set has all vertices of the other set as missing-edge neighbors. Therefore
\[
 n^2\operatorname{Var}(f)=n(a+b)-(a-b)^2\le 2nr.
\]
A missing \(K_{r,r}\) gives equality, with \(-1,+1\) on its respective parts and zero elsewhere. If \(2nr>B_n\) then equality in the spread bound forces \(a=b=r\). All \(2r\) vertices have already used their entire allowed missing-degree on the crossing biclique, so it is a connected component of \(H\). Conversely any such component yields the displayed extremizing potential, and the variance bound excludes all other shapes. The integer transition at \(r_*(n)=\lfloor B_n/(2n)\rfloor\) is immediate.

## Verification

The standalone standard-library checker `verify_dense.py` evaluates all admissible missing-edge graphs on \(3\) through \(6\) vertices by direct enumeration of all three-level potentials; it also tests independent random graphs through \(10\) vertices, exact missing-biclique constructions, all edge-budget envelopes for sizes up to \(100\), and the closed-form threshold inequalities up to \(9999\). All arithmetic is integral. Run `python verify_dense.py` from the extracted package directory. The infinite statements are proved above; finite tests are supplementary.

## Relationship to prior work

Alon, Boppana, and Spencer introduced graph spread and established the integral extremizer principle used in Step 1. Addario-Berry, Janson, and McDiarmid surveyed graph-spread basics and proved bounds for sparse random graphs, including convergence toward complete-graph spread in a high-degree random regime. Yancey studied equality functions and graph isoperimetry in other families. The present result instead solves two deterministic extremal **adversarial deletion budgets** exactly, identifies the sharp nonincrease thresholds, and proves rigidity of the strict-budget extremizers. It does not claim the integer-extremizer principle or complete-graph baseline as new.

## Limitations

The result assumes unit graph distances and uniform masses, and does not cover general edge weights, nonuniform probabilities, or supercritical edge budgets larger than \(\lfloor(n-2)/2\rfloor\). General degree budgets \(r\ge n/2\) can produce disconnected graphs and are excluded. No claim of independent validation or exhaustive literature coverage is made; an equivalent unindexed formulation remains possible.

## References

1. N. Alon, R. Boppana, J. Spencer, *An asymptotic isoperimetric inequality*, Geometric and Functional Analysis 8 (1998), 411–436, Theorem 2.1. Author-hosted full text: https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf .
2. L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, first arXiv version 2009-02-06, arXiv:0902.1156, especially Sections 1.1 and 5; https://arxiv.org/abs/0902.1156 .
3. M. P. Yancey, *Probabilistic and Geometrical Applications to Graph Theory*, arXiv:1705.09725 (2017), Section 1 and variance-optimal function discussions; https://arxiv.org/abs/1705.09725 .
