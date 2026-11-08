# Universal fastest mixing and pendant-edge rigidity on vertex- and edge-transitive leaf coronas

## Finding
Let \(H\) be any finite, connected, simple, vertex- and edge-transitive \(d\)-regular graph on \(n\ge3\) vertices, with \(d\ge2\). Let \(\ell=\lambda_2(L_H)>0\) be the algebraic connectivity of its *unit-weight* combinatorial Laplacian, and let \(r\ge1\) be an integer. Form the leaf corona \(G=H\circ\overline{K_r}\) by attaching \(r\) distinct private degree-one vertices to each core vertex. Put
\[
a=\ell/d,\qquad t=\sqrt a,\qquad D=1+r(1+t)^2,\qquad \alpha=a/D.
\]
Among **all** real symmetric, entrywise-nonnegative stochastic matrices \(P\) whose off-diagonal support is contained in the edges of \(G\), with diagonal holding allowed, the globally smallest second-largest eigenvalue modulus (SLEM) is
\[
\boxed{\min_P\max\{|\lambda_2(P)|,|\lambda_{n(r+1)}(P)|\}=1-\alpha.}
\]
Eigenvalues here are sorted nonincreasingly with \(\lambda_1(P)=1\). A globally optimal transition matrix uses the same probability
\[
p_*={1+r(1+t)\over dD}
\]
on every core edge and the same probability
\[
q_*={t(1+t)\over D}
\]
on every private core–leaf edge. Its core holding probability is zero, and each leaf holds with probability \(1-q_*\).

**Global rigidity:** Every globally optimal feasible \(P\), whether or not it respects any graph automorphism, has **all pendant-edge probabilities exactly \(q_*\)** and **zero holding probability at each core vertex**. The core-edge probabilities are additionally forced to be \(p_*\) if \(P\) is automorphism-invariant; uniqueness of arbitrary non-invariant core-edge weights is not asserted.

## Assumptions and scope
The base is both vertex-transitive and edge-transitive; these are separate hypotheses. All allowed edge probabilities may be chosen independently and may vanish, but no off-graph transition is permitted. The model uses a symmetric kernel, hence the uniform stationary distribution, and self-loops are allowed. The SLEM concerns discrete-time convergence in spectral norm; no assertion about non-reversible kernels, asymmetric stationary distributions, total-variation mixing times, or cost-weighted conductances is made.

## Proof
**1. A universal spectral upper bound on the gap.** Write \(L_H=dI-A_H\) and let \(E=\ker(L_H-\ell I)\), of dimension \(k\ge1\), with orthonormal basis \(u_1,\ldots,u_k\). The orthogonal projector onto \(E\) has constant diagonal \(k/n\) by vertex transitivity. For each core edge \(ij\), edge transitivity implies that the squared displacement \(\sum_{j'=1}^k(u_{j'}(i)-u_{j'}(j))^2\) is constant, so summing the Fiedler energies yields the exact value \(2k\ell/(nd)=2ka/n\).

For each \(u_{j'}\) define \(v_{j'}\in\mathbb R^{n(r+1)}\) by assigning \(u_{j'}(i)\) to each core vertex \(i\), and \((1+t)u_{j'}(i)\) to **each** of its \(r\) leaves. These mutually orthogonal vectors have squared norm \(D\), and each is orthogonal to the constant vector. An arbitrary admissible symmetric kernel is \(P=I-L\), where \(L\) is the weighted edge Laplacian. Write \(w_e\ge0\) for base-edge probabilities and \(q_{is}\ge0\) for pendant-edge probabilities. Averaging the Rayleigh quotients of the \(v_{j'}\) gives the exact identity
\[
\frac1k\sum_{j'=1}^k\frac{v_{j'}^\top Lv_{j'}}{D}
=\frac{a}{nD}\left(2\sum_{e\in E(H)}w_e+\sum_{i,s}q_{is}\right).
\]
At every core vertex \(i\), stochasticity requires \(\sum_{e\ni i}w_e+\sum_s q_{is}\le1\). Adding these \(n\) inequalities shows \(2\sum_e w_e+\sum_{i,s}q_{is}\le n\). Because the vectors are orthogonal to constants, the min–max principle now yields \(\lambda_2(L)\le\alpha\), hence \(\operatorname{SLEM}(P)\ge1-\alpha\). The last implication uses \(\lambda_2(P)=1-\lambda_2(L)\) and \(0<\alpha<1\).

**2. Attainment and the remaining spectrum.** The proposed weights obey \(dp_*+rq_*=1\) and \(0<q_*<1\). The Laplacian separates into leaf-difference eigenvectors with eigenvalue \(q_*\) (multiplicity \(n(r-1)\)), plus, for each base-Laplacian eigenvalue \(\rho\), the symmetric \(2\times2\) block
\[
M_\rho=\begin{pmatrix}p_*\rho+rq_*&-\sqrt r\,q_*\\-\sqrt r\,q_*&q_*\end{pmatrix}.
\]
The smaller eigenvalue of this block is increasing in \(\rho\). At \(\rho=\ell\), the vector whose core coordinate is \(1\) and whose common leaf coordinate is \(1+t\) is an eigenvector of the corresponding (unscaled-leaf) block with eigenvalue \(\alpha\). Both coordinates are positive, so this is the smaller eigenvalue. At \(\rho=0\) the smaller eigenvalue is zero, while \(q_*>\alpha\). Therefore the smallest positive eigenvalue of \(L\) is exactly \(\alpha\).

Let \(\rho_{\max}\le2d\) be the largest base-Laplacian eigenvalue. The largest corona-Laplacian eigenvalue is the larger root of \(M_{\rho_{\max}}\), since this root is increasing in \(\rho\) and at least \(q_*\). By monotonicity of the smaller root,
\[
\lambda_{\max}(L)+\alpha
\le\operatorname{tr}(M_{\rho_{\max}})
=p_*\rho_{\max}+(r+1)q_*
\le 2dp_*+(r+1)q_*
\le 2(dp_*+rq_*)=2.
\]
Consequently \(\lambda_{\max}(L)\le2-\alpha\), so negative eigenvalues of \(P=I-L\) have absolute value at most \(1-\alpha\). Thus the lower bound is attained globally.

**3. Global pendant-edge rigidity.** Suppose an arbitrary feasible \(P\) attains SLEM \(1-\alpha\). Then \(\lambda_2(I-P)=\alpha\). The average Rayleigh quotient in Step 1 must equal \(\alpha\), forcing every core-row budget inequality to be an equality: all core holding probabilities vanish. Moreover, since every \(v_{j'}\) lies in the orthogonal complement of constants and has quotient at least \(\lambda_2(L)=\alpha\), equality of their average forces every \(v_{j'}\) to be an actual \(\alpha\)-eigenvector of \(L\). Its leaf coordinate at a private leaf \((i,s)\) gives
\[
q_{is}t\,u_{j'}(i)=\alpha(1+t)u_{j'}(i).
\]
Because the projector diagonal is \(\sum_{j'}u_{j'}(i)^2=k/n>0\), at least one such coordinate is nonzero for each \(i\), and hence
\[
q_{is}=\frac{\alpha(1+t)}t=\frac{t(1+t)}D=q_*
\]
for **every** private leaf. This proves the asserted rigidity without imposing automorphism invariance on \(P\). If \(P\) is automorphism-invariant, edge transitivity forces its remaining core-edge probabilities to be equal, and the saturated core-row budget then uniquely gives \(p_*\).

## Verification
The accompanying \(\texttt{verify.py}\) uses exact symbolic identities, exact rational spectra for the four-cycle with four private-leaf multiplicities, and a seeded finite comparison against both non-invariant and orbit-invariant stochastic competitors. The successful replay reports: 27 distinct exact spectral eigenvalues across four exact instances; 80 evaluated graph/multiplicity instances; 960 randomly generated non-invariant feasible competitors; and 1680 feasible invariant competitors. Sampled bases include cycles, complete graphs, hypercubes, and the Petersen graph. Execute \(\texttt{python verify.py}\) with the packages in \(\texttt{requirements.txt}\). These finite computations are diagnostic; the infinite-family statement is proved by the preceding analytic argument.

## Relationship to prior work
Boyd, Diaconis and Xiao (2004) formulated fastest symmetric stochastic mixing as a semidefinite optimization problem. Boyd, Diaconis, Parrilo and Xiao (2007) exploited graph automorphisms and gave specific cycle, path, wheel and related examples; the general optimization and the use of symmetries are not claimed new here. Barik, Pati and Sarma (2007) analyzed the Laplacian spectrum of graph coronas, an important precursor to the block spectral decomposition used above. Jafarizadeh (2010) treated symmetric multipartite Markov networks with a distinct edge incidence pattern. The specific universal closed-form optimum for leaf coronas of *arbitrary vertex- and edge-transitive cores*, together with rigidity of every pendant transition in *all* (including asymmetric-by-automorphism) global optima, is the contribution asserted here. Literature equivalence and priority remain subject to independent checking.

## Limitations
The conclusion does not determine whether every admissible core-edge probability is uniquely prescribed without an invariance hypothesis. A general irregular or merely vertex-transitive core need not satisfy the uniform edge-displacement condition used in Step 1. No guarantee applies to biased, nonsymmetric or nonreversible Markov chains. The spectral optimization is a discrete-time SLEM problem, not a bound on every finite-time total-variation performance metric. Earlier unindexed or inaccessible equivalent work may exist. Independent mathematical audit has not been performed.

## References
- S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, doi:10.1137/S0036144503423264; https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
- S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries* (2007 preprint), arXiv:0709.0955; https://arxiv.org/abs/0709.0955.
- S. Barik, S. Pati, B. K. Sarma, *The Spectrum of the Corona of Two Graphs*, SIAM Journal on Discrete Mathematics 21 (2007), 47–56, doi:10.1137/050624029.
- M. A. Jafarizadeh, *Fastest Mixing Markov Chain on Symmetric K-Partite Network* (2010 preprint), arXiv:1008.2588; https://arxiv.org/abs/1008.2588.
