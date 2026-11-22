# A sharp universal positivity gain for cubic Runge–Kutta on weighted bipartite networks

## Finding

Let \(G=(V,E)\) be any finite, connected, undirected bipartite graph with \(|V|\ge2\) and arbitrary strictly positive symmetric edge conductances \(w_{ij}=w_{ji}>0\). Set \(W=(w_{ij})\), with zero entries on nonedges and on the diagonal, \(d_i=\sum_jw_{ij}\), \(L=\operatorname{diag}(d_i)-W\), and \(\Delta=\max_i d_i>0\). The completed classical three-stage, third-order Runge–Kutta step for \(y'=-Ly\) is
\[
T_3(h)=I-hL+\frac{h^2}{2}L^2-\frac{h^3}{6}L^3,\qquad h\ge0.
\]
For each vertex define \(\sigma_i=\sum_jw_{ij}^2\), \(\tau_i=\sum_jd_jw_{ij}^2\), and
\[
q_i(h)=1-d_ih+\frac{d_i^2+\sigma_i}{2}h^2-\frac{d_i^3+2d_i\sigma_i+\tau_i}{6}h^3.
\]
The function \(q_i\) has exactly one positive zero \(\delta_i\). For each distinct pair \(i,j\) sharing at least one neighbor, put
\[
m_{ij}=\sum_kw_{ik}w_{kj}>0,\qquad
c_{ij}=(d_i+d_j)m_{ij}+\sum_kd_kw_{ik}w_{kj},\qquad
\theta_{ij}=\frac{3m_{ij}}{c_{ij}}.
\]
Then the **entire set of entrywise nonnegative timesteps** is the single closed interval
\[
\boxed{\{h\ge0:T_3(h)\ge0\text{ entrywise}\}=[0,h_*(G)],\quad
h_*(G)=\min\Big\{\min_{i\in V}\delta_i,\ \min_{i\ne j:m_{ij}>0}\theta_{ij}\Big\}.}
\]
An empty pairwise minimum is \(+\infty\). Every positive step beyond \(h_*\) has a negative diagonal or distance-two entry; **positivity never returns**. Edge entries and distance-three entries are strictly positive for all positive steps, while entries between vertices more than three edges apart vanish identically.

Moreover, let \(\alpha\) be the unique positive zero of \(1-z+z^2/2-z^3/6\), so \(\alpha=1.5960716379833217\ldots\). Then
\[
\boxed{\frac1\Delta\le h_*(G)<\frac{\alpha}{\Delta}.}
\]
Both constants are optimal over the class: the lower bound is attained on every unweighted four-cycle, while on the unweighted star with \(m\) leaves, \(m h_*(G)\to\alpha\) as \(m\to\infty\). The upper bound is never attained by a finite connected graph.

## Assumptions and scope

Weights may be any strictly positive real numbers and need not be integral or equal. Bipartiteness, symmetry, absence of self-loops, finiteness and connectedness are required. The result concerns the *completed* linear RK endpoint, not each internal stage, general nonlinear strong stability, or monotonicity in a nonstandard norm. The matrix \(T_3(h)\) always has row sums one, so entrywise nonnegativity is equivalent to the Markov stochasticity of the completed step. The statement concerns all real timesteps \(h\ge0\), including the endpoints, and both the local exact criterion and the universal comparison are part of the single result.

## Proof

**1. Local walk identities.** Because the graph is bipartite, every walk of even length remains in its starting class and every walk of odd length switches class. Expanding \(L=D-W\), with \(D=\operatorname{diag}(d_i)\), gives
\[
(L^2)_{ij}=(W^2)_{ij}-(d_i+d_j)w_{ij}\quad(i\ne j),
\]
\[
L^3=D^3-D^2W-DWD-WD^2+DW^2+WDW+W^2D-W^3.
\]
For distinct same-class vertices \(i,j\), we have \(w_{ij}=(W^3)_{ij}=0\). Therefore
\[
[T_3(h)]_{ij}=\frac{h^2m_{ij}}2-\frac{h^3c_{ij}}6
=\frac{h^2m_{ij}}2\left(1-\frac h{\theta_{ij}}\right).
\]
If \(m_{ij}=0\), the entry vanishes identically. If \(m_{ij}>0\), it is nonnegative precisely for \(0\le h\le\theta_{ij}\), and strictly negative at every larger \(h\).

For opposite-class distinct vertices with \(w_{ij}=0\), the same expansion gives \([T_3(h)]_{ij}=h^3(W^3)_{ij}/6\ge0\), strictly positive whenever the graph distance is three. For an edge \(ij\), it instead gives
\[
[T_3(h)]_{ij}=hw_{ij}\left[1-\frac{(d_i+d_j)h}{2}+
\frac{h^2}{6}\left(d_i^2+d_id_j+d_j^2+\frac{(W^3)_{ij}}{w_{ij}}\right)\right].
\]
The bracket is a quadratic with positive leading coefficient and discriminant at most
\[
\frac{(d_i+d_j)^2}{4}-\frac23(d_i^2+d_id_j+d_j^2)
=-\frac{5d_i^2+2d_id_j+5d_j^2}{12}<0.
\]
Thus every edge entry is strictly positive at every \(h>0\). Pairs of graph distance four or more have no contributing walks of length at most three, so their entries are zero. This exhausts all off-diagonal entries.

**2. Diagonal entries have one permanent sign crossing.** Bipartiteness gives \((W^3)_{ii}=0\). The diagonal terms of the above matrix powers yield \([T_3(h)]_{ii}=q_i(h)\). Since \(L\) is symmetric positive semidefinite, it has an orthonormal eigenbasis with eigenvalues \(\lambda_k\ge0\), and
\[
q_i(h)=\sum_k |\phi_k(i)|^2\left(1-h\lambda_k+\frac{h^2\lambda_k^2}{2}-\frac{h^3\lambda_k^3}{6}\right).
\]
The scalar derivative is \(-\lambda[1-h\lambda+(h\lambda)^2/2]\), strictly negative when \(\lambda>0\) because \(1-x+x^2/2=((x-1)^2+1)/2>0\). As \(d_i=L_{ii}>0\), vertex \(i\) has nonzero spectral weight on at least one positive eigenvalue. Therefore \(q_i'(h)<0\) for every \(h\ge0\). Also \(q_i(0)=1\), and the leading coefficient of \(q_i\) is strictly negative, so \(q_i(h)\to-\infty\). Hence \(q_i\) has exactly one positive simple root \(\delta_i\), becoming permanently negative thereafter.

**3. Exact criterion and no recovery.** The entry types in Steps 1 and 2 establish that the update is entrywise nonnegative precisely when all \(q_i(h)\ge0\) and all \(1-h/\theta_{ij}\ge0\). Their single-crossing properties give the stated exact minimum. Since at least one diagonal root exists, the minimum is finite. Beyond it, that same diagonal or distance-two entry remains negative, proving no reentry.

**4. Universal lower bound.** Put \(F(h)=I-hL\). At \(0\le h\le1/\Delta\), \(F(h)\) is nonnegative and row-stochastic. The exact third-degree identity
\[
T_3(h)=\frac13I+\frac12F(h)+\frac16F(h)^3
\]
proves \(T_3(h)\ge0\) throughout this interval. Thus \(h_*(G)\ge1/\Delta\). On the four-cycle with equal unit weights, every degree equals two and an opposite-vertex pair has \(\theta=3/(2+2+2)=1/2\), so equality is attained.

**5. Sharp universal upper bound.** Let \(i\) have \(d_i=\Delta\), and define \(u=\sigma_i/\Delta^2>0\), \(v=\tau_i/\Delta^3>0\). With \(z=h\Delta\),
\[
q_i(z/\Delta)=\left(1-z+\frac{z^2}{2}-\frac{z^3}{6}\right)
+\frac{u z^2}{6}(3-2z)-\frac{v z^3}{6}.
\]
The scalar cubic decreases strictly from 1 to negative infinity, and its unique positive root \(\alpha\) lies strictly between \(3/2\) and 2. At \(z=\alpha\), its first parenthesis vanishes, while \(3-2\alpha<0\) and \(u,v>0\); hence \(q_i(\alpha/\Delta)<0\). Therefore \(h_*(G)\le\delta_i<\alpha/\Delta\).

For the unit star with \(m\ge2\) leaves, \(\Delta=m\), the hub diagonal at \(h=z/m\) equals
\[
1-z+\frac{z^2}{2}-\frac{z^3}{6}+\frac{z^2(3-2z)}{6m}-\frac{z^3}{6m^2}.
\]
Every leaf diagonal tends to 1 for fixed \(z\) as \(m\to\infty\), and the distance-two thresholds are \(3/(m+2)\), so their normalized values tend to 3. The hub diagonal converges uniformly on compact \(z\)-intervals to the scalar cubic, whose unique root is \(\alpha<3\). The exact minimum therefore obeys \(m h_*(G)\to\alpha\). This proves asymptotic sharpness and completes the proof.

## Verification

Run `python3 verify.py` with Python 3 and only the standard library, from the directory containing the script. It constructs 486 weighted bipartite examples (including random positive rational edge weights, stars and cycles), directly computes \(L^2,L^3\) over exact rational arithmetic, and checks every claimed entry identity at five positive rational timesteps, together with row-stochasticity. It reports `VERIFY_OK weighted_bipartite_graphs= 486 exact_entry_checks= 178505 SSP_assertions= 20`. These finite computations corroborate but do not replace the analytic argument for arbitrary real weights and arbitrarily many vertices. For orientation, an unweighted three-vertex path is diagonal-limited at approximately \(h=0.7180571651\), below its distance-two threshold \(3/4\); an unweighted four-vertex path is distance-two-limited at exactly \(h=3/5\), below all its diagonal roots. The code checks identities and stochasticity, not historical novelty.

## Relationship to prior work

General strong-stability-preserving theory gives the sufficient forward-Euler range for SSPRK(3,3), and positivity-preserving adaptive and exponential methods for graph-Laplacian dynamics are developed by Nüßlein–Ranocha–Ketcheson and Blanes–Iserles–Macnamara. Those results do not establish the sharp graph-by-graph fixed-weight RK3 endpoint criterion or the extremal \(\alpha\)-factor across all weighted bipartite graphs. Horváth–Song–Terlaky show how to find an initial invariance-preserving timestep by testing polynomial roots on a polyhedron; that general procedure does not by itself identify the contributing graph distances, establish single-crossing of every potentially negative entry, or yield the sharp universal improvement factor.

Related published graph-specific Taylor results treat constant-rate regular bipartite graphs and complete multipartite graphs: some regular bipartite cases attain the lower bound \(1/\Delta\), and certain complete multipartite cubic cases reduce to diagonal or same-part transitions. The present claim does not reassert those special cases as new. Its scope is the **arbitrary positive weighted bipartite network** together with an exact local all-step classification and a sharp universal relative-to-Euler upper envelope. Stronger or equivalent results could exist in specialist literature under another formulation; the comparison is not an independent priority certification.

## Limitations

The graph must be undirected, weighted-symmetric and bipartite; nonbipartite triangles modify the cubic walk signs. Intermediate RK stages need not be positive beyond the forward-Euler limit. The sharp factor controls positivity of the completed transition matrix, not overall error, spectral stability, runtime, or an optimal choice among different integrators. The full text of the older specialist Horváth (2005) article was not obtained, so unindexed historical coverage remains a risk.

## References

1. S. Nüßlein, H. Ranocha and D. I. Ketcheson, *Positivity-Preserving Adaptive Runge–Kutta Methods*, arXiv:2005.06268v1, first public 2020-05-13, https://arxiv.org/abs/2005.06268.
2. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for population models* (later *Positivity-preserving methods for ordinary differential equations*), arXiv:2102.08242v1, first public 2021-02-16, https://arxiv.org/abs/2102.08242.
3. Z. Horváth, Y. Song and T. Terlaky, *Steplength Thresholds for Invariance Preserving of Discretization Methods of Dynamical Systems on a Polyhedron*, arXiv:1406.6755v1, first public 2014-06-26, https://arxiv.org/abs/1406.6755.
4. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89–112, https://doi.org/10.1137/S003614450036757X.
