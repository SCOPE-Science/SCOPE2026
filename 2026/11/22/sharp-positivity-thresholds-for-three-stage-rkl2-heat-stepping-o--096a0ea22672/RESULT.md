# Sharp positivity thresholds for three-stage RKL2 heat stepping on complete bipartite graphs

## Finding

**Theorem (complete bipartite endpoint-positivity classification).** Let \(1\le p\le q\) be integers and \(L\) the ordinary combinatorial Laplacian of the unweighted complete bipartite graph \(K_{p,q}\), with every edge having conductance one. Apply the three-stage, second-order Runge–Kutta–Legendre (RKL2) stability polynomial to the graph heat equation \(u'(t)=-Lu(t)\). Its completed step is
\[
M(h)=I-hL+\frac{h^2}{2}L^2-\frac{h^3}{15}L^3,\qquad h\ge0.
\]
Define \(r(t)=1-t+t^2/2-t^3/15\), and let \(\alpha\in(5,6)\) be the unique solution of \(r(\alpha)=-1\). For every \(q\ge2\), let \(\tau_q\in(5,45/8)\) be the unique solution of \(r(\tau_q)=-1/q\). Then \(M(h)\) is entrywise nonnegative if and only if \(0\le h\le H_{p,q}\), where
\[
\boxed{
H_{p,q}=\begin{cases}
\alpha/2,&p=q=1,\\
\tau_q/(q+1),&p=1<q,\\
15/[2(p+2q)],&2\le p\le q.
\end{cases}}
\]
In every case, the same matrix is a Euclidean contraction if and only if \(0\le h\le\alpha/(p+q)\). Except for the two-vertex graph, positive timesteps can therefore be Euclidean-stable but fail to map all nonnegative states to nonnegative states. The first failing entry is a hub diagonal for stars and a transition between distinct vertices of the smaller bipartite class for \(p\ge2\).

For \(p=q\ge2\), the ratio of the positivity horizon to the Euclidean-stability horizon equals \(5/\alpha\approx0.861106\). For fixed \(p\ge2\) and \(q\to\infty\), it approaches \(15/(4\alpha)\approx0.645829\). The star thresholds instead satisfy \((q+1)H_{1,q}=\tau_q\to\tau_\infty\), where \(r(\tau_\infty)=0\) and \(\tau_\infty\approx5.154488\).

## Assumptions and scope

Graphs are finite, simple, connected, undirected complete bipartite graphs with positive integers \(p\le q\) and unit edge weights. The matrix is **endpoint-positive** when all its entries are nonnegative; because \(M(h)\mathbf1=\mathbf1\), endpoint positivity is equivalent to preservation of every nonnegative state together with unit row sums. This is distinct from stage-by-stage positivity and nonlinear strong stability preservation. Euclidean contraction means \(\|M(h)\|_2\le1\), in the usual unweighted vector norm, for the symmetric graph Laplacian. A uniform edge conductance \(c>0\) rescales all thresholds by \(1/c\). No statement is made for arbitrary weighted or incomplete bipartite graphs.

## Proof

**1. The scalar polynomial and its two regions.** In the usual three-stage RKL2 normalization, with \(P_3(x)=(5x^3-3x)/2\),
\[
R_3(z)=\frac7{12}+\frac5{12}P_3(1+2z/5)
=1+z+z^2/2+z^3/15.
\]
Consequently \(r(t)=R_3(-t)\). For \(0\le t\le5\), the argument of \(P_3\) lies in \([-1,1]\), and \(|P_3(x)|\le1\) there (by its endpoint and critical values). Thus
\[
\frac16\le r(t)\le1\qquad(0\le t\le5).
\]
For \(t\ge5\), \(r'(t)=-1+t-t^2/5<0\), and \(r(5)=1/6\), \(r(6)=-7/5\). Therefore \(r\) crosses \(-1\) at exactly one \(\alpha\in(5,6)\), and for \(t\ge0\), \(|r(t)|\le1\) precisely when \(t\le\alpha\). Also
\[
1-r(t)=t\left(1-\frac t2+\frac{t^2}{15}\right)>0\quad(t>0),
\]
since the quadratic has negative discriminant and positive leading coefficient.

**2. Four entry types.** Put \(N=p+q\). The Laplacian has eigenvalues \(0\) (the constants), \(N\) (the contrast between classes), \(q\) (zero-sum vectors on the \(p\)-vertex class), and \(p\) (zero-sum vectors on the \(q\)-vertex class), omitting the last two eigenspaces when their multiplicities vanish. Equivalently, its spectral projectors give the following completed-step entries. For vertices in *opposite* classes,
\[
C(h)=\frac{1-r(Nh)}N>0\qquad(h>0).
\]
For distinct vertices in the \(p\)-vertex class (when \(p\ge2\)), the entry is
\[
A(h)=qh^2\left(\frac12-\frac{(N+q)h}{15}\right),
\]
and for distinct vertices in the \(q\)-vertex class (when \(q\ge2\)), the entry is
\[
B(h)=ph^2\left(\frac12-\frac{(N+p)h}{15}\right).
\]
The respective diagonal entries are \(A(h)+r(qh)\) and \(B(h)+r(ph)\). In the singleton-class case \(p=1\), the unique hub diagonal also equals
\[
D_{\mathrm{hub}}(h)=\frac{1+q\,r(Nh)}N.
\]
These identities follow by substituting \(r\) into the three eigenprojectors: for a part of size \(a\) with complementary size \(b=N-a\), the within-part off-diagonal projector entry is \([a+b r(Nh)-N r(bh)]/(Na)\), and the diagonal additionally contains \(r(bh)\). Expansion gives the displayed factorizations. Since \(L\mathbf1=0\) and \(r(0)=1\), every row sum of \(M(h)\) is one.

**3. Both classes nonsingleton.** Suppose \(2\le p\le q\). The first possible zero of \(A(h)\) after zero is
\[
h_*=\frac{15}{2(N+q)}=\frac{15}{2(p+2q)}.
\]
The first possible zero of \(B(h)\) is \(15/[2(N+p)]\ge h_*\). As \(Nh_*\le5\) (equivalent to \(p\le q\)), both \(ph\) and \(qh\) lie in \([0,5]\) for all \(0\le h\le h_*\). Step 1 therefore makes every diagonal nonnegative, while the factorizations make every off-diagonal nonnegative. For every \(h>h_*\), the existing within-\(p\)-class off-diagonal \(A(h)<0\), excluding all later steps. This establishes the third case, including its endpoint.

**4. Stars with at least two leaves.** Suppose \(p=1\) and \(q\ge2\). The hub diagonal vanishes exactly when \(Nh=\tau_q\), where \(r(\tau_q)=-1/q\). It is positive before that point and negative afterward, because \(r\) is positive on \([0,5]\) and strictly decreasing beyond 5. Moreover
\[
r(45/8)=-343/512<-1/2\le-1/q,
\]
so \(5<\tau_q<45/8\). The leaf-to-leaf entry \(B(h)\) first becomes negative at the normalized step \(Nh=15N/[2(N+1)]\), which is at least \(45/8\) for \(N=q+1\ge3\). Thus no leaf-to-leaf transition fails before the hub. All leaf diagonals are positive up to the hub threshold because \(h\le(45/8)/3=15/8<5\), whence \(r(h)\ge1/6\), and \(B(h)\ge0\). All cross-class entries are strictly positive for positive steps by Step 2. Hence the hub criterion is necessary and sufficient globally, proving the second case.

**5. The two-vertex exception and stability.** For \(K_{1,1}\), the completed matrix has diagonal \([1+r(2h)]/2\) and off-diagonal \([1-r(2h)]/2\). Step 1 shows that both are nonnegative precisely for \(2h\le\alpha\). In all cases, the eigenvalue \(N\) exists and is the largest positive Laplacian eigenvalue. Since the scalar interval \(|r(t)|\le1\) is exactly \([0,\alpha]\), and every Laplacian eigenvalue lies in \([0,N]\), the symmetric matrix \(M(h)\) is a Euclidean contraction exactly for \(hN\le\alpha\).

**6. Asymptotic comparisons.** For \(p=q\), \(Nh_*=5\), so \(H_{p,p}/(\alpha/N)=5/\alpha\). For fixed \(p\ge2\) with \(q\to\infty\), \(NH_{p,q}\to15/4\), yielding \(15/(4\alpha)\). Finally \(\tau_q\) decreases to the unique root \(\tau_\infty>5\) of \(r(\tau_\infty)=0\), by strict monotonicity and continuity of \(r\). All claims follow.

## Verification

The accompanying standard-library-only Python program `verify.py` constructs exact rational graph Laplacians, independently forms the matrix polynomial by matrix multiplication, and compares it entry by entry to the derived formulas over many small complete bipartite graphs and rational step sizes. It also checks exact cutoff signs for all class sizes in a finite range and uses rigorous rational bisection brackets for star and two-state thresholds. On replay it printed `VERIFY_OK 52755`. This finite test does **not** establish the all-size theorem: the proof rests on the explicit spectral projectors, sign factorizations and monotonicity inequalities above.

## Relationship to prior work

Tan, Aslam and Bertozzi (arXiv:2611.16238v1, posted 2026-11-12) give the RKL/RKG stabilized time-stepping setup and prove a one-dimensional maximum principle in a Strang-split Allen–Cahn setting; Section 4, Remark 4.3 explicitly notes that higher-dimensional RKL2 monotonicity is not automatic. Their earlier work (arXiv:2507.17062) establishes monotone stability in specified grid settings. Neither result gives an all-partition endpoint classification for unweighted complete bipartite graph heat equations.

Earlier RKL2 research and an exact three-state *directed pure-birth* counterexample establish that some three-stage RKL2 Markov updates have disconnected positivity sets; that does not yield thresholds for the present symmetric, reversible complete bipartite graphs. An exact classification for degree-two, degree-three and degree-four *Taylor Runge–Kutta* polynomials on complete multipartite graphs uses a different third-degree coefficient, \(1/6\) rather than the present RKL2 coefficient \(1/15\), so its numerical bounds do not imply this theorem. The contribution here is the complete analytic split between stars and nonsingleton bicliques, the exact all-size cutoff formulas, and their comparison with the scalar stability range.

## Limitations

The graph family is complete bipartite with uniform positive conductance; neither arbitrary graph topology nor nonuniform weights nor other stage counts are covered. Only the completed endpoint matrix is classified; internal stage positivity and nonlinear maximum principles are not implied. Nonnegative endpoint matrices can still have large local truncation errors at the permitted largest steps. Historical priority is qualified because differently worded analyses of graph-specific RKL methods outside the inspected literature may exist. Independent mathematical audit has not been performed.

## References

1. Z. Tan, T. D. Aslam and A. L. Bertozzi, *Fully Explicit Stabilized Runge–Kutta Methods for Allen–Cahn and Cahn–Hilliard Dynamics*, arXiv:2611.16238v1, first posted 2026-11-12, https://arxiv.org/html/2611.16238v1.
2. Z. Tan, T. D. Aslam and A. L. Bertozzi, *Explicit Monotone Stable Super-Time-Stepping Methods for Finite Time Singularities*, arXiv:2507.17062, https://arxiv.org/abs/2507.17062.
3. C. D. Meyer, D. S. Balsara and T. D. Aslam, *A stabilized Runge–Kutta–Legendre method for explicit super-time-stepping of parabolic and mixed equations*, Journal of Computational Physics 257 (2014), 594–626, https://doi.org/10.1016/j.jcp.2013.08.021.
4. *Reentrant endpoint positivity of three-stage RKL2 on a minimal Markov chain*, published mathematical record 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-reentrant-endpoint-positivity-of-three-stage-rkl2-on-a-minimal-m--3730497a7f20.
5. *Exact positivity radii and an order-three reversal for Taylor Runge–Kutta diffusion on complete multipartite graphs*, published mathematical record 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-positivity-radii-and-an-order-three-reversal-for-taylor-ru--0aa3ec090e79.
