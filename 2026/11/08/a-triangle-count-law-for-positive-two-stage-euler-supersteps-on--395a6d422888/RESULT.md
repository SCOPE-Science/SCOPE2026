# A triangle-count law for positive two-stage Euler supersteps on regular graphs

## Finding

Let \(G\) be a finite connected simple undirected \(d\)-regular graph, \(d\ge1\), with adjacency matrix \(A\), Laplacian \(L=dI-A\), and nonnegative Euler substeps \(h_1,h_2\). The endpoint map after two substeps is
\[
P(h_1,h_2)=(I-h_2L)(I-h_1L).
\]
It is *endpoint-positive* when it is entrywise nonnegative, equivalently when it maps every nonnegative initial state to a nonnegative final state. The intermediate Euler state is not required to be nonnegative.

For every edge \(ij\), let \(c_{ij}=|N(i)\cap N(j)|\), and put \(t=\min_{ij\in E(G)}c_{ij}\). Introduce the dimensionless substeps \(x=dh_1\), \(y=dh_2\), their sum \(s=x+y\), and product \(q=xy\). Then **the exact endpoint-positivity region** is
\[
1-s+\left(1+\frac1d\right)q\ge0,
\qquad
s\ge\left(2-\frac td\right)q,
\qquad x,y\ge0.
\]
Thus all constraints collapse to the vertex degree and the *minimum edge triangle count*.

If \(G\) is not complete, necessarily \(d\ge2\) and \(0\le t\le d-2\). The **exact maximal dimensionless total Euler time** is
\[
\boxed{s_*(G)=\frac{2d-t}{d-1-t}},
\qquad
\boxed{h_1+h_2\le \frac{2d-t}{d(d-1-t)}}.
\]
Every total \(0<s\le s_*\) is attained by strictly positive substeps with a nonnegative endpoint. At the maximum, the unordered normalized pair is unique:
\[
\boxed{\{x,y\}=
\left\{\frac{2d-t+\sqrt{t^2+4d}}{2(d-1-t)},
\frac{2d-t-\sqrt{t^2+4d}}{2(d-1-t)}\right\}}.
\]
The corresponding endpoint transition kernel has the exact graph-theoretic form
\[
\boxed{P_* = \frac{A^2-tA-dI}{d(d-1-t)}}.
\]
It is symmetric, entrywise nonnegative, and row- and column-stochastic. When \(t=0\), this is the familiar two-step nonbacktracking random-walk kernel on a regular graph. If \(G\) is complete, no finite upper bound on \(h_1+h_2\) exists: one Euler substep can project exactly onto constants and erase arbitrarily large excursions of the other substep.

As a structured example, for a complete balanced \(r\)-partite graph with \(r\ge2\) parts of size \(k\ge2\), one has \(d=(r-1)k\), \(t=(r-2)k\), and \(s_*=rk/(k-1)\). Its extremal endpoint map jumps uniformly to *another vertex of the same part* and nowhere else; when \(k=2\) this is a deterministic involution.

## Assumptions and scope

All graphs here are finite, connected, simple, undirected, and unweighted. The degree \(d\) is a fixed positive integer and \(h_1,h_2\) are real, nonnegative Euler durations. The endpoint is inspected only after both substeps, which commute because the generator \(L\) is time-independent. Repeating an endpoint-positive two-step block preserves nonnegative states and total mass at block boundaries. The maximal total time is an optimization over *all* positive pairs \(h_1,h_2\), not merely over equal-stage or conventional Chebyshev choices. No accuracy claim is made for large steps.

## Proof

**Step 1 (exact matrix entries).** For any graph with degree \(d_i\), the diagonal of \(L^2\) is \(d_i^2+d_i\), an edge \(ij\) has \((L^2)_{ij}=c_{ij}-d_i-d_j\), and a nonedge \(ij\) has \((L^2)_{ij}=c_{ij}\). This follows by multiplying \(L=D-A\), using \((A^2)_{ij}=|N(i)\cap N(j)|\). For a regular graph,
\[
P=I-\frac{s}{d}L+\frac{q}{d^2}L^2
 = (1-s+q)I+\frac{s-2q}{d}A+\frac{q}{d^2}A^2.
\]
Hence
\[
P_{ii}=1-s+\left(1+\frac1d\right)q,
\qquad
P_{ij}=\frac{ds-(2d-c_{ij})q}{d^2}\ (ij\in E),
\qquad
P_{ij}=\frac{q c_{ij}}{d^2}\ (ij\notin E,\ i\ne j).
\]
Since \(q\ge0\), every nonedge entry is nonnegative. The worst edge is an edge with \(c_{ij}=t\); thus the two displayed inequalities are jointly necessary and sufficient. Since \(L\mathbf1=0\), all rows and columns always sum to one.

**Step 2 (the complete-graph dichotomy).** Always \(t\le d-1\). If every edge has \(d-1\) common neighbors, every pair of neighbors of a vertex must be adjacent, so each closed neighborhood induces a \((d+1)\)-clique. Degree regularity and connectivity force \(G=K_{d+1}\). Conversely this clique has \(t=d-1\). On \(K_{d+1}\), since \(L=(d+1)I-J\), choose \(h_2=1/(d+1)\); then \(I-h_2L=J/(d+1)\), and \(P=J/(d+1)\) for any \(h_1>0\). Thus the possible total duration is unbounded. Every connected \(1\)-regular graph is this complete case \(K_2\).

**Step 3 (universal upper bound for a fixed noncomplete regular graph).** Let
\[
a=2-\frac td,\qquad c=1+\frac1d.
\]
Here \(a>c>1\). Endpoint positivity forces \(q\le s/a\) and \(cq\ge s-1\). When \(s>1\), it follows that \((s-1)/c\le s/a\), or \(s\le a/(a-c)=(2d-t)/(d-1-t)\). For \(s\le1\) the bound holds automatically because the right-hand side exceeds \(2\).

**Step 4 (sharpness, all intermediate totals, and uniqueness).** The elementary inequality
\[
1-s+\frac c4s^2>0 \quad \text{for every real }s
\]
follows from \(c>1\) (its minimum is \(1-1/c>0\)). For \(0<s\le4/a\), use equal strictly positive substeps \(x=y=s/2\), so \(q=s^2/4\le s/a\), and both positivity conditions hold. For \(4/a\le s\le s_*\), prescribe \(q=s/a\) and take \(x,y\) to be the two positive roots of \(z^2-sz+q=0\). These roots are real because \(s\ge4/a\); the diagonal condition is \(1-s(1-c/a)\ge0\), equivalent to \(s\le s_*\). The two intervals cover \((0,s_*]\), since \(s_*>4/a\): the inequality \(a^2>4(a-c)\) follows from \((a-2)^2+4(c-1)>0\).

At \(s=s_*\) both inequalities in Step 3 are equalities, forcing \(q=q_*=s_*/a=d/(d-1-t)\). The quadratic with prescribed sum and product determines the unordered pair uniquely. Its discriminant is
\[
s_*^2-4q_* = \frac{t^2+4d}{(d-1-t)^2}>0,
\]
which gives the two displayed distinct positive roots.

**Step 5 (the extremal Markov kernel).** Substitute \(s_*\) and \(q_*\) into the matrix polynomial in Step 1 to obtain
\[
P_*=\frac{A^2-tA-dI}{d(d-1-t)}.
\]
Its diagonal entries vanish because \((A^2)_{ii}=d\); an edge entry is \((c_{ij}-t)/(d(d-1-t))\ge0\); a nonedge entry is \((A^2)_{ij}/(d(d-1-t))\ge0\). Every row sums to \([d^2-td-d]/[d(d-1-t)]=1\), and symmetry gives column-stochasticity. For \(t=0\), \(A^2-dI\) counts two-edge walks with immediate backtracks deleted, yielding the standard nonbacktracking two-step kernel. On balanced multipartite graphs, adjacent vertices have exactly \(t=(r-2)k\) common neighbors, while two distinct vertices in the same part have \(d\) common neighbors; inserting these counts gives precisely the uniform within-part jump stated above. This completes the proof.

## Verification

The standalone Python 3 script `verify.py` uses only the standard library and exact fractions. It enumerates connected labeled regular simple graphs on up to six vertices, supplements them with cycle, multipartite and complete-graph families, and checks the positivity inequalities against full exact matrix multiplication for a rational grid of two-step durations. It also tests the endpoint kernel identities, row sums, clique projection, the upper-bound obstruction, and feasible subcritical durations. Replay with `python3 verify.py`. The run recorded `VERIFICATION_OK: 173 labeled connected regular graphs, 8304 rational endpoint pairs; sharp boundary identities checked`. Finite checks support but do not replace the proof for arbitrary graph size.

## Relationship to prior work

Two-stage super-time-stepping using factored Euler updates and Chebyshev spectral stability is established in Alexiades, Amiez and Gremaud (1996), particularly their Section 2 and two-stage discussion. The result above does **not** claim to invent such compositions or their spectral-stability acceleration. It instead optimizes the stronger *entrywise nonnegative endpoint* property across every connected regular graph, giving a sharp graph-local triangle parameter and an explicit extremal Markov kernel. Gottlieb, Shu and Tadmor (2001) develop strong-stability-preserving arguments by stagewise convex Euler decomposition; an overlarge intermediate stage here falls outside those sufficient stagewise conditions. Cheng et al. (2015) study random-walk matrix polynomials with nonnegative combination coefficients, whereas the extremal kernel above involves a signed combination of \(I,A,A^2\). Meyer, Balsara and Aslam (2012) study a different Legendre-based multistage method; their abstract concerns positivity for linear diffusion, but their full text was not inspected here. No claim of definitive publication priority is made.

## Limitations

The theorem concerns endpoint positivity, not positivity of internal Euler stages, strict positivity, local truncation error, high-order consistency, physical fidelity at very large supersteps, robustness under a varying generator, or weighted/irregular/directed networks. The maximizing map may move mass over two edges without approximating physical diffusion accurately at that nominal time. The full text of one related Legendre super-time-stepping study could not be inspected, and unlocated graph-specific literature might contain an equivalent formula. Independent mathematical validation has not been performed.

## References

1. V. Alexiades, G. Amiez and P.-A. Gremaud, “Super-time-stepping acceleration of explicit schemes for parabolic problems,” *Communications in Numerical Methods in Engineering* **12** (1996), 31–42. https://doi.org/10.1002/(SICI)1099-0887(199601)12:1%3C31::AID-CNM950%3E3.0.CO;2-5 . Author-hosted full text: https://web.math.utk.edu/~vasili/va/descr/sts.CNME96.pdf .
2. S. Gottlieb, C.-W. Shu and E. Tadmor, “Strong Stability-Preserving High-Order Time Discretization Methods,” *SIAM Review* **43** (2001), 89–112. First published online 2001-02-02. https://doi.org/10.1137/S003614450036757X . Author-hosted text: https://drum.lib.umd.edu/bitstreams/faa96f40-0fbb-4af0-84a3-5e3b80c908df/download .
3. C. D. Meyer, D. S. Balsara and T. D. Aslam, “A second-order accurate Super TimeStepping formulation for anisotropic thermal conduction,” *MNRAS* **422** (2012), 2102–2115. https://doi.org/10.1111/j.1365-2966.2012.20744.x .
4. D. Cheng, Y. Cheng, Y. Liu, R. Peng and S.-H. Teng, “Spectral Sparsification of Random-Walk Matrix Polynomials,” arXiv:1502.03496 (2015-02-12). https://arxiv.org/abs/1502.03496 .
