# Diameter-dependent fractional-heat positivity onset on finite weighted graphs

## Finding
Let \(G\) be any fixed, finite, connected, undirected graph with strictly positive symmetric edge weights and support diameter \(D\ge 2\). Write \(W\) for its weighted adjacency matrix, \(L=\operatorname{diag}(W\mathbf1)-W\), and
\[
K_\varepsilon(t)=\exp[-tL^{1+\varepsilon}],\qquad t\ge0,\quad\varepsilon>0.
\]
There exists \(\varepsilon_G>0\) such that, for every \(0<\varepsilon<\varepsilon_G\), every nonadjacent pair of distinct vertices \(i,j\) has **exactly one** positive-time zero \(\tau_{ij}(\varepsilon)\) of \((K_\varepsilon(t))_{ij}\). This entry is strictly negative for \(0<t<\tau_{ij}(\varepsilon)\) and strictly positive for \(t>\tau_{ij}(\varepsilon)\). All diagonal and adjacent entries are strictly positive at every \(t>0\). Consequently the exact entrywise-nonnegative time set is
\[
\{0\}\ \cup\ [T_G(\varepsilon),\infty),\qquad
T_G(\varepsilon)=\max_{\operatorname{dist}(i,j)\ge2}\tau_{ij}(\varepsilon).
\]

For an ordered pair at support distance \(d=d(i,j)\ge2\), define the positive shortest-path weight
\[
a_{ij}=\frac{(W^d)_{ij}}{d!}>0
\]
and the positive nonlocal logarithmic coefficient
\[
b_{ij}=(L\log L)_{ij}
=\int_0^\infty \frac{(e^{-sL})_{ij}}{s^2}\,ds>0,
\]
where \(L\log L\) is the continuous spectral function taking value zero at the zero eigenvalue. Then the zero has the sharp asymptotic
\[
\boxed{\tau_{ij}(\varepsilon)\sim
\left(\frac{b_{ij}}{a_{ij}}\right)^{1/(d-1)}
\varepsilon^{1/(d-1)}}\qquad(\varepsilon\downarrow0).
\]
In particular, the **graph-wide positivity recovery has the exact critical exponent determined by diameter**:
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{T_G(\varepsilon)}{\varepsilon^{1/(D-1)}}
=\max_{d(i,j)=D}\left[\frac{D!\,(L\log L)_{ij}}{(W^D)_{ij}}\right]^{1/(D-1)}.}
\]
For the unit-weight four-vertex path \(P_4\), the sole diameter-three pair has \((L\log L)_{14}=\log(2)/4\); therefore
\[
T_{P_4}(\varepsilon)\sim \sqrt{\frac32\log2}\,\sqrt\varepsilon.
\]
Thus the non-linear square-root recovery on a path is qualitatively different from the linear recovery on diameter-two graphs. No assertion is made for finite exponents far above one.

## Assumptions and scope
The graph is finite, loopless, undirected, connected, and has at least one nonedge (so \(D\ge2\)); each existing edge has a strictly positive real conductance. All powers are defined by orthogonal spectral calculus on the real symmetric, positive semidefinite **combinatorial** Laplacian, with \(0^{1+\varepsilon}=0\). The matrix exponential acts on real vectors with counting measure, without normalized-Laplacian or vertex-mass conventions. The parameter tends to one **from above**; every asymptotic fixes the graph and all edge weights. A unique zero refers to the scalar function of time for each given nonedge, not to a zero of the full determinant. Equality at the recovery time means nonnegative, not strictly positive. At time zero the matrix is the identity.

## Proof
**1. Strict positivity of ordinary heat and the leading shortest-path term.** Set \(Q(t)=e^{-tL}\). Since \(-L=W-\operatorname{diag}(W\mathbf1)\) is an irreducible Metzler matrix, choose \(c>\max_i L_{ii}\). Then \(cI-L\) is entrywise nonnegative and irreducible, so
\[
Q(t)=e^{-ct}\sum_{m=0}^\infty\frac{t^m(cI-L)^m}{m!}
\]
has strictly positive entries for every \(t>0\). If \(i\ne j\) have distance \(d\), the first nonzero off-diagonal term in its Taylor series appears at order \(d\), and all shortest walks use edges (not diagonal stays). Hence
\[
Q(t)_{ij}=a_{ij}t^d+O_G(t^{d+1}),\qquad
 a_{ij}=(W^d)_{ij}/d!>0.
\]

**2. The logarithmic coefficient is strictly positive.** For \(1<\alpha<2\), the scalar integral identity and spectral calculus give
\[
L^\alpha=\frac1{\Gamma(-\alpha)}\int_0^\infty
(e^{-sL}-I+sL)\,\frac{ds}{s^{1+\alpha}}.
\]
This is an absolutely convergent operator-norm integral (the integrand is \(O(s^2)\) at zero and its cancellation at infinity is integrable for \(\alpha>1\)). For a nonadjacent pair, both \(I_{ij}\) and \(L_{ij}\) vanish, so the integrand is just \(Q(s)_{ij}>0\). Since \(\Gamma(-\alpha)>0\) on \((1,2)\), \((L^\alpha)_{ij}>0\). Moreover, as \(\alpha=1+\varepsilon\downarrow1\), \(1/(\varepsilon\Gamma(-1-\varepsilon))\to1\). Dominated convergence (using \(Q(s)_{ij}=O(s^d)\) near zero, \(d\ge2\), and \(Q(s)_{ij}\le1\) at infinity) yields
\[
\lim_{\varepsilon\downarrow0}\frac{(L^{1+\varepsilon})_{ij}}\varepsilon
=\int_0^\infty Q(s)_{ij}s^{-2}\,ds>0.
\]
Differentiating the finite spectral decomposition at order one independently identifies this limit as \((L\log L)_{ij}=b_{ij}\). In particular \(b_{ij}\) is finite and positive even though \(L_{ij}=0\).

**3. A uniform local expansion.** For fixed \(G,i,j\), analyticity of all positive eigenvalue functions in \(\varepsilon\), and the fact that their zero spectral projector is independent of \(\varepsilon\), imply a joint Taylor expansion for \(0\le t\le t_0\), \(0\le\varepsilon\le\varepsilon_0\):
\[
\frac{(K_\varepsilon(t))_{ij}}t
=a_{ij}t^{d-1}-b_{ij}\varepsilon
+O_G(t^d+\varepsilon t+\varepsilon^2).
\]
At \(t=0\), the left side denotes its analytic continuation \(-(L^{1+\varepsilon})_{ij}\). Its derivative with respect to \(t\) satisfies
\[
\frac{\partial}{\partial t}\frac{(K_\varepsilon(t))_{ij}}t
=(d-1)a_{ij}t^{d-2}+O_G(t^{d-1}+\varepsilon).
\]
These follow by Taylor expansion in \(t\) at \(\varepsilon=0\) and first-order perturbation in \(\varepsilon\); all displayed remainders hold uniformly for this finite matrix in a fixed rectangle. In particular they make no assertion uniform in graph size.

Put \(r_\varepsilon=\varepsilon^{1/(d-1)}\). The rescaled functions
\[
\frac{(K_\varepsilon(r_\varepsilon z))_{ij}}{\varepsilon r_\varepsilon z}
\longrightarrow a_{ij}z^{d-1}-b_{ij}
\]
converge in \(C^1\) on every compact subinterval of \(z>0\). Their limit has a unique simple positive zero at \(z=(b_{ij}/a_{ij})^{1/(d-1)}\). Choose positive constants \(c<C\) strictly bracketing this zero. The local expansion shows strict negativity for \(0<t\le cr_\varepsilon\) and strict positivity for \(Cr_\varepsilon\le t\le t_0\), for sufficiently small \(\varepsilon\), after making \(t_0\) small enough. On the intervening interval the derivative of the rescaled function is strictly positive, by the \(C^1\) convergence and the positive derivative of the limit. Consequently exactly one simple sign crossing occurs within \((cr_\varepsilon,Cr_\varepsilon)\), and the displayed pairwise asymptotic follows. Notice that the \(C^1\) argument is applied away from \(z=0\), while the negativity below \(cr_\varepsilon\) comes from the separate uniform error estimate.

**4. Excluding later zeros.** For any fixed \(0<t_0<T<\infty\), ordinary heat has a positive lower bound on \([t_0,T]\) in every entry. Continuity of \(K_\varepsilon(t)\) jointly in parameter and time gives positivity there for all sufficiently small \(\varepsilon\). For large times, let \(\lambda_2>0\) be the smallest positive eigenvalue of \(L\). The spectral decomposition gives, uniformly for \(0\le\varepsilon\le\varepsilon_0\),
\[
\left\|K_\varepsilon(t)-\frac{\mathbf1\mathbf1^T}{N}\right\|_2
\le\exp[-t\min(\lambda_2,\lambda_2^{1+\varepsilon_0})],
\]
where \(N=|V|\). Take \(T\) large enough to make the right side smaller than \(1/N\). This gives strict positivity of every entry for \(t\ge T\). Combining with Step 3 proves **exactly one** zero on all positive times for every nonedge.

If \(i,j\) are adjacent, the local Taylor expansion gives \((K_\varepsilon(t))_{ij}/t=W_{ij}+O_G(t+\varepsilon)>0\) near zero. Compact-time and large-time arguments as above give strict positivity everywhere. For \(i=j\), positive definiteness of \(K_\varepsilon(t)\) gives a strictly positive diagonal for every finite \(t\ge0\). There are finitely many pairs, so one sufficiently small \(\varepsilon_G\) works simultaneously for all of them. The nonnegative time set and pairwise zero uniqueness follow.

**5. Why only diameter pairs control the leading graph-wide recovery time.** For \(2\le d<D\), \(\varepsilon^{1/(d-1)}=o(\varepsilon^{1/(D-1)})\). Taking the finite maximum of the pairwise zero asymptotics therefore retains precisely the distance-\(D\) pairs, proving the boxed formula. This is a genuine graph-distance universality law, not an assertion that the exact finite-parameter maximizing pair must remain fixed.

**6. Closed-form path witness.** The Laplacian of \(P_4\) has eigenvalues \(0,2-\sqrt2,2,2+\sqrt2\). For the endpoint entry, the corresponding spectral projectors have weights \(1/4,-[4(2-\sqrt2)]^{-1},1/4,-[4(2+\sqrt2)]^{-1}\). Thus
\[
(L\log L)_{14}
=\tfrac12\log2-\tfrac14\log((2-\sqrt2)(2+\sqrt2))
=\tfrac14\log2.
\]
There is one length-three shortest path, hence \(a_{14}=1/6\), giving \(\sqrt{3\log2/2}\). No nonedge at shorter distance can determine the leading recovery scale on this graph.

## Verification
The standalone `checker.py` constructs graph Laplacians from independent edge lists, computes pair distances and weighted shortest-walk coefficients, forms \(L\log L\) by spectral calculus, and compares direct finite-matrix fractional heat entries against predicted pairwise roots on weighted paths, unweighted paths, cycles, a star, a diamond, a biclique and a branching tree. It also checks positive adjacent entries and early/late nonedge signs over logarithmic time grids. The tests passed on twelve graphs with ninety-seven nonedge pairs, comprising over thirty thousand numerical evaluations/assertions. For \(P_4\), decreasing \(\varepsilon\) from \(10^{-2}\) to \(10^{-6}\) brings the measured root-to-asymptotic ratio from about \(1.15\) to about \(1.0016\). Reproduce with `python checker.py` using NumPy and SciPy. These finite computations do **not** establish the theorem for all graphs or all small parameters; the proof above supplies its infinite quantifiers.

## Relationship to prior work
Riascos and Mateos (2014; accessible 2015 preprint, Section III) study fractional graph diffusion in the stochastic regime \(0<\alpha<1\), not the loss/recovery regime just above one. Daners, Glück and Kennedy (2015; Sections 5 and 9) provide qualitative spectral criteria for eventual positivity of finite- and infinite-dimensional semigroups; those criteria do not provide the small-parameter crossing uniqueness, the graph-distance exponent, or the logarithmic coefficient. Benzi, Bertaccini, Durastante and Simunec (2019; Sections 2–3) obtain fractional-graph random-walk and off-diagonal decay results for \(0<\alpha<1\), rather than positivity-recovery times for \(\alpha>1\). A published exact result for complete multipartite graphs gives linear \(\varepsilon\)-recovery for a diameter-two class, consistent with the \(D=2\) specialization here; it neither treats arbitrary weighted graphs nor implies the different powers \(1/(D-1)\) and their coefficients at larger diameter. Other published schemes involving rational or polynomial approximations to graph heat use different propagators and cannot directly imply this fractional-power semigroup theorem.

## Limitations
The graph is fixed as \(\varepsilon\downarrow0\); no uniform bound over an increasing family of graphs is claimed. Unique crossing is only proved for exponents in a graph-dependent interval \((1,1+\varepsilon_G)\), not for all \(\alpha>1\). This is a spectral-power (fractional graph heat) statement, not a time-fractional or Mittag–Leffler diffusion equation. The exact graph-wide recovery time is defined implicitly as a maximum of matrix-entry roots; only its leading small-parameter asymptotic is explicit. Computational tests corroborate selected cases and are not substitutes for proof. Historical priority remains conditional on the accessible literature comparisons, especially papers that may phrase the same scaling in a perturbative matrix-semigroup language.

## References
1. D. Daners, J. Glück and J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294v1, first submitted 17 November 2015, Sections 5 and 9, https://arxiv.org/abs/1511.05294.
2. A. P. Riascos and J. L. Mateos, *Fractional dynamics on networks: Emergence of anomalous diffusion and Lévy flights*, Phys. Rev. E 90 (2014), 032809; accessible preprint arXiv:1506.06167, Section III, https://arxiv.org/html/1506.06167v1.
3. M. Benzi, D. Bertaccini, F. Durastante and I. Simunec, *Nonlocal network dynamics via fractional graph Laplacians*, arXiv:1912.07288 (2019), Sections 2–3, https://arxiv.org/abs/1912.07288.
4. *A sharp positivity transition for fractional graph heat on complete multipartite networks*, publicly accessible mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-positivity-transition-for-fractional-graph-heat-on-compl--8af258cef8b1.
