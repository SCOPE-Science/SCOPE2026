# Independent sharp positivity thresholds for fourth-order diffusion on block-homogeneous complete networks

## Finding

Let \(r\ge2\), \(n_1,\ldots,n_r\ge1\) be integers, \(N=\sum_i n_i\), and \(B_1,\ldots,B_r\) a partition of \(N\) vertices into blocks of these sizes. Fix \(b>0\) and \(a_i\ge0\). The undirected edge conductance is \(b\) between distinct blocks and \(a_i\) between different vertices in block \(B_i\). Write \(L\) for the ordinary weighted combinatorial Laplacian and
\[
F(z)=\frac{z^2-6z+12}{z^2+6z+12},\qquad T(h)=F(hL).
\]
The full exact characterization is
\[
\boxed{\quad T(h)\ge0\ \text{entrywise for all }h\ge0\quad\Longleftrightarrow\quad
0\le \frac{a_i}{b}\le2+\frac{n_i}{N-n_i}\quad\text{for every }i\text{ with }n_i\ge2.\quad}
\]
Singleton-block parameters have no effect. For permitted parameters every entry is strictly positive at all positive steps; all matrices are symmetric and row-stochastic. If any block violates its bound, its distinct-vertex transition entries change sign once and become negative at all sufficiently large steps. These changes are blockwise independent: altering the conductances inside the other blocks cannot change the within-block sign test. All transitions between distinct blocks are positive at every positive step, for all parameters.

## Assumptions and scope

All claims concern exact arithmetic and the **completed endpoint update** of the two-stage, order-four Gauss–Legendre Runge–Kutta method for the linear graph heat system \(\dot u=-Lu\). They do not assert nonnegative internal Runge–Kutta stages, positivity for arbitrary weighted graphs, or an approximation guarantee for an arbitrarily large timestep. Edge weights \(a_i\) may vanish; \(b\) must be positive and ensures connectivity. The theorem covers every real \(h\ge0\), every finite number of blocks, and every positive integer block-size profile.

## Proof

Set \(q_i=N-n_i\), \(\gamma=Nb\), \(\lambda_i=q_i b+n_i a_i>0\), and \(D(z)=z^2+6z+12\). For any block \(B_i\), let \(E_i\) be the projector onto the vectors supported there with coordinate sum zero:
\[
E_i=I_{B_i}-\frac1{n_i}J_{B_i}.
\]
These are orthogonal projectors, with \(E_i=0\) for singleton blocks. Let \(E_0=J_N/N\) and \(E_c=I-E_0-\sum_iE_i\). The subspace of block-constant vectors with global coordinate sum zero has projector \(E_c\). Directly applying the edge-Laplacian definition gives
\[
LE_i=\lambda_iE_i,\qquad LE_c=\gamma E_c,\qquad LE_0=0.
\]
Therefore
\[
T(h)=E_0+F(\gamma h)E_c+\sum_iF(\lambda_i h)E_i.
\]
This identity remains valid when some eigenvalues coincide. Every eigenvalue of \(T(h)\) is strictly positive: the numerator of \(F(z)\) is \((z-3)^2+3\) for \(z\ge0\), and its denominator is positive. Hence \(T(h)\) is positive definite and all diagonal entries are strictly positive. Also \(T(h)\mathbf1=\mathbf1\).

For distinct vertices \(u\in B_i\) and \(v\in B_j\) with \(i\ne j\), the projector entries yield
\[
T(h)_{uv}=\frac{1-F(\gamma h)}N=\frac{12bh}{D(\gamma h)}>0\quad(h>0).
\]
For distinct \(u,v\in B_i\), \(n_i\ge2\), the exact formula is
\[
T(h)_{uv}=\frac{12h}{n_i}\left[\frac{\lambda_i}{D(\lambda_i h)}-\frac{q_i b}{D(\gamma h)}\right].
\]
As the denominators are positive, for \(h>0\) its sign equals that of the quadratic
\[
P_i(h)=12n_i a_i+6n_i b\lambda_i h+\lambda_i(\gamma^2-q_i b\lambda_i)h^2.
\]
The constant coefficient is nonnegative and the linear coefficient is strictly positive. Consequently, \(P_i(h)>0\) for every \(h>0\) if and only if its leading coefficient is nonnegative. Substitution yields
\[
\gamma^2\ge q_i b\lambda_i
\iff N^2b^2\ge (N-n_i)b[(N-n_i)b+n_i a_i]
\iff \frac{a_i}{b}\le\frac{2N-n_i}{N-n_i}=2+\frac{n_i}{N-n_i}.
\]
At equality the quadratic term vanishes but the strictly positive linear term remains. If the bound fails, write \(A_i=\lambda_i(q_i b\lambda_i-\gamma^2)>0\), \(B_i=6n_i b\lambda_i>0\), \(C_i=12n_i a_i>0\). Then \(P_i(h)=-A_ih^2+B_ih+C_i\) has exactly one positive root,
\[
h_i^*=\frac{B_i+\sqrt{B_i^2+4A_iC_i}}{2A_i},
\]
and the entry is positive on \((0,h_i^*)\), zero at \(h_i^*\), and negative for \(h>h_i^*\). No \(a_j\) with \(j\ne i\) appears anywhere in this formula. At \(h=0\), \(T(0)=I\), completing every boundary case and both implications.

## Verification

A standalone Python 3 standard-library exact-rational program, `verify.py`, constructs the actual weighted Laplacian for eleven diverse block-size profiles and three cross conductances. It evaluates all parameter combinations selected from zero, the sharp boundary, and a violating value; it checks four rational timesteps per choice. In **3,636 exact full-matrix cases**, it independently computes the matrix rational function by rational Gauss–Jordan elimination and compares every off-diagonal entry to the derived closed formula, verifies row sums and diagonals, and checks the predicted sign test. It prints `VERIFY_OK` on success. This is regression evidence; the spectral projector proof above establishes the all-dimension, all-real-timestep result.

## Relationship to prior work

Lóczi and Ketcheson's 2013 preprint studies rational absolute monotonicity and proves that the fourth-order \([2/2]\) Padé stability function has zero general absolute-monotonicity radius; this universal obstruction does not exclude all-step positivity for a structured Laplacian family. Zappavigna, Colaneri, Kirkland and Shorten (public repository copy deposited 2012) prove general Padé positivity obstructions and finite-step sufficient conditions, but their inspected theorems do not classify the present block-homogeneous networks for all steps.

Known specializations include a single internally weighted clique joined to an independent set, disjoint modified matching edges, and the unweighted complete multipartite family. The new scope is the simultaneous, arbitrary number of nontrivial blocks of arbitrary sizes, each independently weighted, with a complete necessary-and-sufficient positivity region in all those parameters. Those previously covered specializations are not asserted to be new.

## Limitations

The condition applies only when **all inter-block edge conductances are identical**, with each block internally homogeneous. Arbitrary edgewise perturbations and heterogeneously weighted inter-block pairs are outside the theorem. The completed positive matrix need not retain accurate physical heat dynamics when the timestep is large: this diagonal Padé filter approaches the identity on positive eigenmodes at large arguments. Numerical replay is finite and not a substitute for the projector proof. Relevant specialist publications not captured by the checked searches could affect publication priority; no independent mathematical audit is claimed.

## References

1. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1 (first posted 2013-03-26), especially Sections 1 and 2.2.1. https://arxiv.org/html/1303.6651v1
2. A. Zappavigna, P. Colaneri, S. Kirkland, and R. N. Shorten, *Essentially Negative News About Positive Systems*, repository full text deposited 2012-06-19, especially Section 4, Theorem 3. https://mural.maynoothuniversity.ie/id/eprint/3761/
