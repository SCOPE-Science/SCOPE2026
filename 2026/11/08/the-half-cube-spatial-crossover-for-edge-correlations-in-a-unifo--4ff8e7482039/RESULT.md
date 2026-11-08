# The half-cube spatial crossover for edge correlations in a uniform hypercube spanning tree

## Finding

Let \(d\ge2\), let \(Q_d\) be the graph on \(\{0,1\}^d\) joining vertices that differ in one coordinate, and let \(T_d\) be its uniform spanning tree. Write \(I_e=\mathbf1_{\{e\in T_d\}}\). All edges have the same inclusion probability
\[
p_d=\frac{2(2^d-1)}{d2^d}.
\]
Two distinct edges are *parallel* when they change the same coordinate, otherwise *perpendicular*. Their separation \(r\) is the minimum Hamming distance between their endpoints. Put
\[
A_d(r)=2^{1-d}\int_0^1(1-t)^r(1+t)^{d-1-r}\,dt,\quad 0\le r\le d-1,
\]
\[
B_d(r)=2^{1-d}\int_0^1t(1-t)^r(1+t)^{d-2-r}\,dt,\quad0\le r\le d-2.
\]
For distinct edges \(e,f\),
\[
\operatorname{Cov}(I_e,I_f)=
\begin{cases}
-A_d(r)^2,& e,f\text{ parallel},\quad1\le r\le d-1,\\
-B_d(r)^2,& e,f\text{ perpendicular},\quad0\le r\le d-2.
\end{cases}
\]
Both magnitudes strictly decrease with separation, and for \(1\le r\le d-2\), \(A_d(r)>B_d(r)>0\). Thus all distinct edge indicators have strictly negative covariance; parallel pairs are more negatively correlated than perpendicular pairs at the same separation.

There is a sharp *half-cube crossover* when separation is a positive fraction of dimension. Set \(\rho_d=r/d\), and \(h(u)=-u\log u-(1-u)\log(1-u)\). For \(\rho_d\to\rho\in(0,1/2)\),
\[
A_d(r)=2e^{-dh(\rho_d)}\sqrt{\frac{2\pi\rho_d}{d(1-\rho_d)}}(1+o(1)),\qquad
\frac{B_d(r)}{A_d(r)}\longrightarrow\frac{1-2\rho}{2(1-\rho)}.
\]
For \(\rho_d\to\rho\in(1/2,1)\),
\[
A_d(r)=\frac{2^{1-d}}{d(2\rho_d-1)}(1+o(1)),\qquad
B_d(r)=\frac{2^{1-d}}{d^2(2\rho_d-1)^2}(1+o(1)).
\]
Finally, if \((r-d/2)/\sqrt d\to s\in\mathbb R\), then
\[
A_d(r)=\frac{2^{1-d}}{\sqrt d}\bigl(J_0(s)+o(1)\bigr),\qquad
B_d(r)=\frac{2^{1-d}}{d}\bigl(J_1(s)+o(1)\bigr),
\]
where \(J_k(s)=\int_0^\infty u^k e^{-u^2/2-2su}\,du\) for \(k=0,1\). These asymptotics are for the transfer-current magnitudes; the covariance is their negative square. In particular the perpendicular-to-parallel correlation-magnitude ratio tends to a positive constant below half the dimension, but vanishes polynomially at and beyond half the dimension.

## Assumptions and scope

The graph is the finite, unweighted, simple hypercube with a uniformly chosen spanning tree. Edge indicators refer to undirected inclusion, without conditioning on any other edges. Separation is *endpoint-set* Hamming distance, not line-graph distance. For perpendicular edges, the two possible relative orientations have opposite signed currents but the same covariance. The formulas hold for all finite \(d\ge2\); asymptotic statements use integer \(r\) in the stated admissible ranges. No independence or approximate-independence assertion stronger than the displayed probabilities is made.

## Proof

**1. Transfer-current reduction.** Arbitrarily orient every edge; its incidence vector \(b_e\) has a \(+1\) at the tail and \(-1\) at the head. For the graph Laplacian \(L\) and its Moore–Penrose pseudoinverse \(L^+\), the transfer-current kernel is \(K(e,f)=b_e^{\mathsf T}L^+b_f\). The uniform spanning-tree transfer-current theorem [1] yields
\[
\Pr(e,f\in T_d)=K(e,e)K(f,f)-K(e,f)^2\quad(e\ne f),
\]
so \(\operatorname{Cov}(I_e,I_f)=-K(e,f)^2\). The characters \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\), \(S\subseteq[d]\), form an orthogonal eigenbasis with \(L\chi_S=2|S|\chi_S\). Therefore
\[
K(e,f)=2^{-d}\sum_{S\ne\varnothing}
\frac{(\chi_S(e^-)-\chi_S(e^+))(\chi_S(f^-)-\chi_S(f^+))}{2|S|}.
\]
Here \(e^-\), \(e^+\) are its oriented endpoints. Coordinate translations and permutations allow \(e=(0,\mathbf e_i)\), \(f=(v,v+\mathbf e_j)\), with \(v_j=0\). If \(i=j\), also \(v_i=0\), and \(|v|=r\). If \(i\ne j\), write \(r\) for the number of ones of \(v\) outside coordinates \(i,j\), which equals endpoint-set separation. Exactly the subsets containing the required coordinate(s) survive in the preceding sum:
\[
K(e,f)=2^{1-d}\sum_{S\supseteq\{i,j\}}\frac{(-1)^{\sum_{a\in S}v_a}}{|S|},
\]
where \(\{i,j\}\) is the singleton \(\{i\}\) for parallel edges. Inserting \(1/|S|=\int_0^1t^{|S|-1}\,dt\) and multiplying the independent coordinate factors gives \(K=A_d(r)\) for parallel edges and \(K=(-1)^{v_i}B_d(r)\) for perpendicular edges. For \(f=e\), \(A_d(0)=2(2^d-1)/(d2^d)\). This proves the finite-dimensional probability identities.

**2. Strict signs and geometry.** The two integrands are positive on \((0,1)\). Increasing \(r\) by one multiplies either by \((1-t)/(1+t)\), strictly between zero and one. Moreover, for the same \(r\le d-2\),
\[
A_d(r)-B_d(r)=2^{1-d}\int_0^1(1-t)^r(1+t)^{d-2-r}\,dt>0.
\]
Therefore the inequalities and the strict negative edge correlations hold for every permitted integer dimension and separation. Strictness is not deduced merely from general negative association: it follows from the positive integrals.

**3. Interior saddle regime.** Let \(f_\rho(t)=\rho\log(1-t)+(1-\rho)\log(1+t)\). For \(\rho<1/2\), this is strictly concave on \((0,1)\), with unique maximizer \(t_*=1-2\rho\),
\[
f_\rho(t_*)=\log2-h(\rho),\qquad f_\rho''(t_*)=-\frac1{4\rho(1-\rho)}.
\]
Express the integral defining \(A_d\) as \(2^{1-d}\int_0^1e^{df_{\rho_d}(t)}(1+t)^{-1}dt\) and the one defining \(B_d\) as \(2^{1-d}\int_0^1e^{df_{\rho_d}(t)}t(1+t)^{-2}dt\). Standard one-dimensional Laplace expansion at the nondegenerate interior maximizer gives the displayed asymptotic constant and their ratio, uniformly for \(\rho_d\) in any compact subinterval of \((0,1/2)\).

**4. Boundary saddle and central crossover.** If \(\rho_d\to\rho>1/2\), the maximizer moves to the endpoint \(t=0\), where \(f_\rho'(0)=1-2\rho<0\). Substituting \(t=u/d\), the normalized integrands converge to \(e^{-(2\rho-1)u}\) and \(u e^{-(2\rho-1)u}\). Their integrals are \(1/(2\rho-1)\) and \(1/(2\rho-1)^2\), respectively. Strict concavity controls the discarded tail and yields the supercritical formulas.

In the central window, substitute \(t=u/\sqrt d\). If \((r-d/2)/\sqrt d\to s\), the exponent obeys \(df_{r/d}(u/\sqrt d)\to-u^2/2-2su\). Concavity bounds the integrands on the scale \(u\), and mass outside that scale is negligible. Dominated convergence gives the functions \(J_0\) and \(J_1\), with the respective \(d^{-1/2}\) and \(d^{-1}\) factors. This proves all asymptotic regimes and their matching transition.

## Verification

The included independent executable `verify_hypercube_edges.py` uses exact arithmetic. In dimensions \(2,3,4,5\) it constructs the actual hypercube Laplacian, grounds one vertex, solves the electrical network independently of the Walsh formula, and checks the resulting currents against the proposed finite polynomial-integral sums for every edge. In dimensions \(2,3,4\), selected joint-inclusion probabilities are independently reconstructed as mixed finite differences of weighted Kirchhoff determinants, verifying the determinant covariance identity. Further exact integral comparisons check strict directional ordering in dimensions \(3\) through \(14\). The checker reports `VERIFY_OK 239 exact comparisons`. Numerical high-precision quadrature was separately used to stress-test the asymptotic constants at dimensions around \(200\). Finite checks test the algebra and boundary cases; the preceding Fourier/Laplace argument, not extrapolation from these tests, proves the all-dimensional claim.

Run from the file's directory with `python verify_hypercube_edges.py`, using Python 3.10+ and SymPy. This is a standalone computation, not a claim of independent mathematical certification.

## Relationship to prior work

The transfer-current determinant and its two-edge negative association are established general results [1]. The Walsh spectrum of the cube is elementary, and Bernardi [2] establishes a strong weighted *orientation/spin* independence and forest-enumerator factorization on hypercubes. These do not state spatially resolved inclusion covariances at fixed endpoint separation. Nachmias and Peres [3] derive local high-degree UST limits, and Archer, Nachmias and Shalev [4] derive high-dimensional GHP scaling, including the hypercube; their limit theorems do not compute the finite-distance integral or the half-dimensional separation crossover. The contribution claimed here is specifically the exact two-edge spatial classification and its three-regime asymptotic, including the Gaussian-width window; not the underlying determinantal theory, cube eigenvalues, or general negative association. Searches did not establish exhaustive historical priority.

## Limitations

The result concerns only the unweighted Boolean hypercube and pairwise edge inclusion, not higher-order correlations, random edge conductances, all Cartesian products, or continuum-tree geometry. In the limit statements, both dimension and separation vary as specified; no uniform expansion is asserted all the way down to bounded \(r\) or the extreme antipodal boundary. The crossover concerns magnitudes (or squared covariance magnitudes), not a sign change. Independent review and historical-priority certification remain outstanding.

## References

[1] R. Burton and R. Pemantle, *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances*, Annals of Probability 21 (1993), 1329–1371. https://arxiv.org/abs/math/0404048 .

[2] O. Bernardi, *On the Spanning Trees of the Hypercube and other Products of Graphs*, Electronic Journal of Combinatorics 19(4) (2012), #P51. https://doi.org/10.37236/2510 .

[3] A. Nachmias and Y. Peres, *The local limit of uniform spanning trees*, arXiv:2011.08833v1 (2020-11-17). https://arxiv.org/abs/2011.08833 .

[4] E. Archer, A. Nachmias and M. Shalev, *The GHP scaling limit of uniform spanning trees in high dimensions*, arXiv:2112.01203v1 (2021-12-02). https://arxiv.org/abs/2112.01203 .
