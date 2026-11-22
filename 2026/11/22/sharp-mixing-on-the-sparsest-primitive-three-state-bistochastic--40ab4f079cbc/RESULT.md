# Sharp mixing on the sparsest primitive three-state bistochastic supports

## Finding

**Theorem (minimal-support optimum and exceptional point).** Let \(\mathcal P_5\) be the set of primitive \(3\times3\) doubly stochastic transition matrices with exactly five strictly positive entries. Five is the smallest possible number of positive entries for any primitive three-state doubly stochastic matrix. Every matrix in \(\mathcal P_5\), up to a simultaneous relabeling of its states, has the form

\[
P(p)=\begin{pmatrix}0&0&1\\p&1-p&0\\1-p&p&0\end{pmatrix},\qquad 0<p<1.
\]

The uniform law \(\pi=(1/3,1/3,1/3)\) is stationary and the asymptotic mixing factor \(\eta(P)=\lim_{n\to\infty}\|P^n-\Pi\|^{1/n}\), where \(\Pi\) has every entry \(1/3\), is

\[
\eta(P(p))=\begin{cases}
\dfrac{p+\sqrt{p^2-8p+4}}2,&0<p\le 4-2\sqrt3,\\[5pt]
\sqrt{2p-1},&4-2\sqrt3\le p<1.
\end{cases}
\]

Consequently the **unique optimal weight**, up to state relabeling and the induced representation, and the **sharp optimal factor** are

\[
\boxed{p_*=4-2\sqrt3,\qquad \min_{P\in\mathcal P_5}\eta(P)=2-\sqrt3.}
\]

At this optimum the two nonstationary eigenvalues collide at \(\lambda_*=\sqrt3-2\), forming a defective Jordan block. Thus for every initial probability vector outside one proper affine line, the total-variation distance to stationarity obeys \(\|\mu P(p_*)^n-\pi\|_{\mathrm{TV}}=\Theta(n(2-\sqrt3)^n)\). The maximizing spectral gap on the minimal support class is \(\sqrt3-1\).

## Assumptions and scope

A real \(3\times3\) matrix is **doubly stochastic** if its entries are nonnegative and its row and column sums are one. It is **primitive** if some positive integer power has every entry strictly positive. A positive entry is a permitted directed transition, including a self-loop when on the diagonal. The **support budget** counts positive matrix entries, not undirected edges or the number of nontrivial parameters.

The norm in the definition of \(\eta\) may be any matrix norm; finite-dimensional spectral-radius theory makes the limit norm-independent. The entropy or one-step contraction coefficient is not being optimized. Simultaneous state relabeling acts by conjugation with permutation matrices. All interior parameters \(0<p<1\) are included, but the two endpoints are excluded because they cease to be primitive. Only time-homogeneous chains with uniform stationary probability are considered.

## Proof

**1. Minimal support and exhaustive structure.** By the Birkhoff--von Neumann theorem, any doubly stochastic \(3\times3\) matrix is a convex combination of permutation matrices. A permutation has three positive positions. Any two distinct permutations disagree on at least two rows, so their support union has at least five positions. Consequently a doubly stochastic matrix supported on at most four positions is itself a permutation matrix and is not primitive.

Suppose now the matrix has exactly five positive positions and is not a permutation. It must use at least two distinct permutation matrices in its Birkhoff decomposition. Their union already has at least five positions, so exactly two such permutations occur and they differ in exactly two rows. They agree in precisely one position, and the union consists of one common position and a four-edge alternating square. No third permutation has support inside that union. Thus every such matrix is a **unique strictly interior convex combination of two permutations sharing one position**. If the common position is diagonal, that common state is absorbing, so the matrix is reducible. If the common position is off-diagonal, simultaneous relabeling sends the two permutations to a three-cycle and a transposition and their mixture to the displayed \(P(p)\). Its directed graph contains a three-cycle and a self-loop connected to it; it is strongly connected and aperiodic for all \(0<p<1\). Hence it is primitive. This proves both the five-positive-entry minimum and the complete conjugacy classification.

**2. Exact nonstationary spectrum.** Direct determinant expansion gives

\[
\det(zI-P(p))=(z-1)(z^2+pz+2p-1).
\]

The stationary eigenvalue is one, and the remaining eigenvalues are

\[
\lambda_{\pm}(p)=\frac{-p\pm\sqrt{p^2-8p+4}}2.
\]

The discriminant \(p^2-8p+4\) has precisely one zero in \((0,1)\), at \(p_*=4-2\sqrt3>1/2\). For \(0<p<p_*\) the two nonstationary roots are real and their largest absolute value is \((p+\sqrt{p^2-8p+4})/2\). For \(p>p_*\), they form a conjugate pair and their common modulus is \(\sqrt{2p-1}\), because their product is \(2p-1>0\). Continuity covers the transition.

**3. Sharp optimization.** The derivative of the first branch is

\[
\eta'(p)=\frac12\left(1+\frac{p-4}{\sqrt{p^2-8p+4}}\right)<0
\]

because \((4-p)^2-(p^2-8p+4)=12>0\) and \(4-p>0\). On the second branch \(\eta'(p)=1/\sqrt{2p-1}>0\). Therefore there is a unique global minimum at the discriminant zero, where \(\eta(p_*)=p_*/2=2-\sqrt3\). The endpoint limits of \(\eta\) equal one and cannot improve the optimum.

**4. Exceptional-point transient.** Let \(\Pi=\tfrac13\boldsymbol1\boldsymbol1^{\mathsf T}\), \(Q=P(p_*)\), and \(N=Q-\Pi-\lambda_*(I-\Pi)\). Since the two nonstationary eigenvalues coincide, Cayley--Hamilton on the sum-zero plane gives \(N^2=0\). Moreover \(N\ne0\): if \(N=0\), then \(Q=\Pi+\lambda_*(I-\Pi)\), a matrix with all off-diagonal entries \((1-\lambda_*)/3>0\), contradicting the displayed zero entries. Since \(\Pi N=N\Pi=0\), for every integer \(n\ge1\),

\[
Q^n-\Pi=\lambda_*^n(I-\Pi)+n\lambda_*^{n-1}N.
\]

For a row probability vector \(\mu\), the coefficient of the enhanced term vanishes precisely when \((\mu-\pi)N=0\). Since \(N\ne0\) is rank one on the two-dimensional sum-zero plane, that exceptional set is a proper affine line. For all other initial vectors, its nonzero coefficient dominates the first term as \(n\to\infty\), giving the displayed \(\Theta\) law in total variation. It also follows that diagonalizability does not characterize the spectral-rate optimum.

## Verification

Run `python3 verify.py` using Python 3 and SymPy. It symbolically checks the characteristic polynomial and seven exact Jordan-power identities at the radical parameter, enumerates all nine possible five-position supports of doubly stochastic three-state matrices and their six primitive support conjugates, and compares the exact spectral factors against numerical eigenvalue moduli for 25 rational parameters. Expected output:

`VERIFY_OK support_graphs=9 primitive_conjugates=6 exact_jordan_powers=7 spectral_test_parameters=25`

The finite tests check formulas and the exhaustive *finite* support classification; the proof above establishes the global variational claim over the continuum of real transition probabilities.

## Relationship to prior work

Coles and Pavlov, *Spectral gaps and mixing rates of primitive matrices* (arXiv:2611.10951, first public November 7, 2026), give general rate bounds using irreducibility distance and chainable index; their theorem does not optimize over minimal-support three-state bistochastic chains. The classical Birkhoff decomposition supplies the key combinatorial reduction but not the subsequent sharp spectral optimization. Boyd, Diaconis, and Xiao's fastest-mixing formulation concerns symmetric walks on undirected graphs, whereas the present minimal primitive supports are directed and nonreversible.

Among compared publicly accessible exact results, *An exceptional-point optimum for cyclic three-edge heat sweeps* obtains a different, fully positive three-state return kernel formed from three reversible heat updates; its optimum is \((2-\sqrt3)^3\) per three-edge sweep, whereas this result concerns a **single five-positive-entry** Markov transition with optimum \(2-\sqrt3\) per step. Likewise, *Complete three-transposition resonance in a quadratic population flow* gives a strictly positive three-factor return kernel that is, in fact, **isospectral to \(P(p)^3\)** on the nonstationary plane at the same parameter: its trace and determinant are precisely the third-power symmetric functions of the two eigenvalues displayed here. Thus the spectral collision and its radical are already substantially covered, not independently novel. The present contribution is the additional classification of **all minimally supported primitive bistochastic chains** and its distinct sharp one-step mixing-rate design statement; the earlier nonlinear-flow paper does not state that constrained minimum. A complete dimension-three Birkhoff coefficient law describes decomposition cardinality, not mixing-rate optimization. The known directed-triangle stay-or-advance model has six rather than five positive transitions and a different fastest-rate parameter. These comparisons distinguish statements and hypotheses, not merely titles or numerical coincidences.

## Limitations

The result is an **asymptotic spectral-radius** optimum within the entire sparsest primitive **uniform-stationary three-state** class. It does not optimize finite-time total variation, mixing time at a fixed tolerance, the fastest reversible three-state chain, or chains with more than five positive entries. Other support sizes can mix faster. The optimum is nonnormal and has a polynomial prefactor in generic finite-time convergence. Historical priority relative to unindexed older three-state Markov computations remains a risk; the inspected primary and related published results do not establish a direct equivalent.

## References

1. S. Coles and R. Pavlov, *Spectral gaps and mixing rates of primitive matrices*, arXiv:2611.10951v1 (first public 2026-11-07), https://arxiv.org/html/2611.10951v1 .
2. S. Boyd, P. Diaconis, and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, https://web.stanford.edu/~boyd/papers/fmmc.html .
3. G. Birkhoff, *Three observations on linear algebra*, Univ. Nac. Tucumán Rev. Ser. A 5 (1946), 147–151 (Birkhoff--von Neumann decomposition).
4. *An exceptional-point optimum for cyclic three-edge heat sweeps*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-exceptional-point-optimum-for-cyclic-three-edge-heat-sweeps--e5717c1e661f .
5. *Complete three-transposition resonance in a quadratic population flow*, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-complete-three-transposition-resonance-in-a-quadratic-population--88595ecbbef3 .
6. *A complete two-endpoint minimum Birkhoff decomposition law in dimension three*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-complete-two-endpoint-minimum-birkhoff-decomposition-law-in-di--21b7692ab8b7 .
7. *Exact finite-horizon total-variation optimizers for a lazy directed triangle*, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-finite-horizon-total-variation-optimizers-for-a-lazy-direc--5e5efd39850a .
