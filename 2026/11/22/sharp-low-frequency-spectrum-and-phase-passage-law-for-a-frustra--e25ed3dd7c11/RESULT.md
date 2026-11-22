# Sharp low-frequency spectrum and phase-passage law for a frustrated Ising tripartite network

## Finding

For every integer \(n\ge1\), consider the zero-field antiferromagnetic Ising model on the labeled complete tripartite graph \(K_{n,n,n}\), with coupling \(J>0\). Restrict continuous-time zero-temperature single-site Glauber heat-bath dynamics to the ground-state configurations: each vertex receives an independent rate-one update, and a flip with zero energy change is accepted with probability \(1/2\). Define \(L_n\) as the negative of its generator and list its eigenvalues in nondecreasing order with multiplicity, starting at \(\lambda_{0,n}=0\).

The **five nonzero low-frequency eigenvalues** have the exact asymptotic limits
\[
\lim_{n\to\infty}\frac{2^n}{n}(\lambda_{1,n},\ldots,\lambda_{5,n})=(1/4,1/4,3/4,3/4,1).
\]
In particular, the spectral gap satisfies \(\lambda_{1,n}\sim n/(4\cdot2^n)\). All other eigenvalues are bounded away from zero uniformly in sufficiently large \(n\). These eigenvalues are the nontrivial modes of an emergent six-cycle with effective edge conductance \(n/4\) and mass \(2^n\) at each vertex.

There are precisely six fully monochromatic, nonconstant part-spin configurations, ordered around that six-cycle. If two are at cycle distance \(d\in\{1,2,3\}\), the exact mean first-passage time from one to the other is
\[
\mathbb E_x\tau_y=\frac{(2^n-1)d(6-d)}{n}\sum_{k=0}^{n-1}\binom{n-1}{k}^{-1}.
\]
Thus the three distance classes have mean passage ratios \(5:8:9\), and for fixed \(d\), \(\mathbb E_x\tau_y\sim 2d(6-d)2^n/n\). The spectral and passage formulas refer to the same physical continuous-time clock and ground-state Markov chain.

## Assumptions and scope

The three parts \(A,B,C\) each have \(n\) labeled spins in \(\{-1,+1\}\); edges join precisely vertices in distinct parts. The Hamiltonian is \(H=J(M_AM_B+M_AM_C+M_BM_C)\), where \(M_i\) is the sum of spins in part \(i\), and the magnetic field is zero. Updates that increase energy are rejected, those decreasing energy accepted, and energy-neutral updates accepted with probability \(1/2\). The chain is initialized at a ground state, so only energy-neutral moves ever occur. A mean first-passage time begins at the source state and ends at the first hit of the specified target state. Spectral eigenvalues refer to the unique continuous-time chain on the ground-state class, not the full transient-state dynamics. The convention gives every permitted undirected spin-flip edge rate \(1/2\), not rate one.

## Proof

**Ground-state network.** Let \(a_i\in\{0,\ldots,n\}\) be the number of positive spins in part \(i\). Direct expansion gives the exact nonnegative identity
\[
H+Jn^2=\frac{4J}{n}\left[a_Aa_Ba_C+(n-a_A)(n-a_B)(n-a_C)\right].
\]
Both terms vanish exactly when one part is all positive and a different part is all negative; the third part is arbitrary. These configurations form six labeled \(n\)-dimensional Boolean cubes, each with two monochromatic endpoints, glued cyclically at the six nonconstant monochromatic configurations. There are \(N_n=6(2^n-1)\) distinct states. A ground-state flip necessarily has zero energy change, so its symmetric rate is \(1/2\). The chain is irreducible, and its stationary law is uniform. This ground-state graph description was previously established for a closely related discrete-time minority rule; it is used here as a starting fact, not claimed as a new discovery.

**One-cube capacity lemma.** On a single \(n\)-cube put conductance \(1/2\) on each edge. Let \(\mathcal E_Q(f)=\frac12\sum_{uv\in E(Q)}(f(u)-f(v))^2\), let \(m=2^{-n}\sum_{v\in Q}f(v)\), and let \(u,v\) be its two opposite corners. The mean-zero Green matrix for endpoint evaluation is
\[
G_n=\begin{pmatrix}\gamma_n&\delta_n\\\delta_n&\gamma_n\end{pmatrix},\quad
\gamma_n=2^{-n}\sum_{k=1}^n\frac{\binom nk}{k}=\frac2n(1+O(n^{-1})),\quad
\delta_n=2^{-n}\sum_{k=1}^n\frac{(-1)^k\binom nk}{k}=-2^{-n}H_n.
\]
For \(n\ge2\) this matrix is positive definite. The spectral decomposition of the cube generator, whose eigenvalues are \(0,1,\ldots,n\) with multiplicities \(\binom nk\), proves these formulas; the alternating binomial identity follows by integrating \([1-(1-t)^n]/t\) on \([0,1]\). By the Dirichlet principle in the mean-zero subspace, the minimum energy among functions with mean \(m\) and endpoint values \(x,y\) is exactly
\[
\begin{pmatrix}x-m&y-m\end{pmatrix}G_n^{-1}
\begin{pmatrix}x-m\\y-m\end{pmatrix}.
\]
In particular it equals \((n/2)(1+o(1))[(x-m)^2+(y-m)^2]\) uniformly over endpoint values. The minimizing extension is the linear combination of the two mean-zero Green representers; by the cube Poincaré inequality, its squared mean-zero \(\ell^2\) norm is at most its energy. These facts also prove the sharp matching upper construction below.

**Low-spectrum reduction.** Number the cubes cyclically by \(j\in\mathbb Z/6\mathbb Z\), with the \(j\)-th cube joining junctions \(x_j,x_{j+1}\); let \(m_j\) be the ordinary arithmetic mean of a test function over this entire cube, including its two endpoints. Sum the capacity bounds. As \(n\to\infty\), uniformly for all test functions,
\[
\mathcal E(f)\ge\frac n2(1-o(1))\sum_j\left[(x_j-m_j)^2+(x_{j+1}-m_j)^2\right]
\ge\frac n4(1-o(1))\sum_j(m_j-m_{j-1})^2.
\]
The second inequality minimizes separately over each junction value. Conversely choose \(x_j=(m_{j-1}+m_j)/2\) and use the exact capacity-minimizing extension in each cube. Its energy is \((n/4)(1+o(1))\sum_j(m_j-m_{j-1})^2\), with squared norm \(2^n\sum_jm_j^2+O(n\sum_jm_j^2)\). The cube Poincaré inequality (gap one) yields, for arbitrary test functions, \(\sum_j\sum_{v\in Q_j}(f(v)-m_j)^2\le\mathcal E(f)\). The graph norm counts each junction once rather than twice; its difference from the sum of cube norms is only the six junction squares. Each junction deviation from the neighboring cube mean is bounded by \(\gamma_n\mathcal E(f)\), so that difference is negligible for a bounded family of test functions with Rayleigh quotients of order \(n2^{-n}\). Therefore the map from such low-energy functions to their six cube means is asymptotically norm-preserving after rescaling by \(2^{-n/2}\), and its energy has the matching lower and upper six-dimensional forms just established. The min–max principle (with the mean-zero cube Poincaré bound excluding further vanishing eigenvalues) gives convergence of the first six eigenvalues, after multiplication by \(2^n/n\), to the spectrum of \(\tfrac14\) times the ordinary six-cycle Laplacian: \(0,1/4,1/4,3/4,3/4,1\). The seventh eigenvalue stays bounded away from zero: any dimension-seven trial subspace contains a nonzero vector whose six cube means vanish, on which cube Poincaré and double-counting at only six junctions yield a uniform positive Rayleigh lower bound.

**Exact phase-passage times.** By coordinate permutation symmetry, all vertices at the same Hamming level between opposite corners of one cube have equal electrical potential. The effective opposite-corner resistance of one cube is therefore
\[
R_n=\sum_{k=0}^{n-1}\frac{2}{(n-k)\binom nk}=\frac2n\sum_{k=0}^{n-1}\binom{n-1}k^{-1}.
\]
The six cubes are connected only through their two endpoints, so their effective resistances form an ordinary six-cycle. Between junctions at distance \(d\), the total resistance is \(R_n d(6-d)/6\). For a continuous-time symmetric finite chain with edge rates equal to conductances, the commute-time identity is \(\mathbb E_x\tau_y+\mathbb E_y\tau_x=N_n R_{xy}\). A reflection interchanges these two junctions while preserving all rates, so each directional expectation is half the commute time. Substitution proves the displayed exact formula. Finally, the reciprocal-binomial sum is \(2+O(n^{-1})\), by splitting off the two endpoints and bounding the middle terms, giving the passage asymptotics.

## Verification

The self-contained `verify.py` uses the standard library and independently enumerates the ground-state configurations, constructs the physical continuous-time generator, solves exact rational linear systems for the three junction-distance classes, and checks the stated passage formula for \(n=1,2,3\). Its expected report is `EXACT_GROUND_WALK_CHECKS_PASSED 9`. An independent optional `spectrum_check.py` constructs the weighted radial quotient of the full graph and computes its six smallest positive generalized eigenvalues for sizes up to \(n=28\) using NumPy and SciPy (requirements listed in `requirements.txt`). The observed values converge to \(1/4,1/4,3/4,3/4,1\) after the stipulated scaling. These finite evaluations check the formulas but are not infinite-size proofs; the capacity lemma and min–max argument establish the theorem for arbitrary size.

## Relationship to prior work

*Stochastic Minority on Graphs* by Rouquier, Regnault and Thierry establishes the background stochastic-minority convention and supplies general Markov-chain tools. A subsequent public result, *One communicating ground-state class and an exponential bottleneck for stochastic minority on balanced tripartite graphs* (2026), already proves exactly the six-cube ground-state communication graph, its state count and an exponential **lower bound** on discrete-time mixing. The present work does **not** claim those results as new. The distinctive statements here are the precise low-frequency eigenvalue constants for the physical continuous-time Glauber clock, the limiting full six-mode spectral multiplicity, and the exact three-class passage-time law. The prior mixing lower bound and graph identity do not state these constants or the full asymptotic spectral classification. Another public study, *Field-resonant weak minima and parity-alternating complexity on complete tripartite Ising networks* (2026), classifies the static configurations, not their slow eigenvalues or passage expectations. Standard electrical-network commute identities are used transparently as antecedents, not presented as discoveries. Spirin, Krapivsky and Redner study ferromagnetic lattice Glauber freezing on a different geometry.

## Limitations

The model is exactly zero-temperature, zero-field, balanced complete tripartite, uniformly coupled, and restricted to the connected ground-state sector. It does not establish equilibration from arbitrary excited initial conditions, metastable switching at positive temperature, or all eigenvalues at finite \(n\). The exact passage law follows in part from previously published ground-state geometry together with classical electrical-network methods, and is not asserted to be independently novel apart from its use in the unified kinetic description. The sharp low-frequency spectral limit is a separate substantive asymptotic result; no claim of exhaustive worldwide historical priority or external independent verification is made. Finite checks do not prove the asymptotic theorem.

## References

1. J.-B. Rouquier, D. Regnault and É. Thierry, *Stochastic Minority on Graphs*, arXiv:1011.5119 (first public 2010-11-23), https://arxiv.org/html/1011.5119v1 .
2. *One communicating ground-state class and an exponential bottleneck for stochastic minority on balanced tripartite graphs* (public 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-one-communicating-ground-state-class-and-an-exponential-bottlene--4639e5e1dc43 .
3. *Field-resonant weak minima and parity-alternating complexity on complete tripartite Ising networks* (public 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-field-resonant-weak-minima-and-parity-alternating-complexity-on--b9b1601dcfa6 .
4. V. Spirin, P. L. Krapivsky and S. Redner, *Freezing in Ising Ferromagnets*, arXiv:cond-mat/0105037 (first public 2001-05-02), https://arxiv.org/html/cond-mat/0105037v1 .
5. S.-K. Baek, T. Ha and H. Jeong, *Absorbing states of zero-temperature Glauber dynamics in random networks*, arXiv:1112.5927 (first public 2011-12-27), https://arxiv.org/abs/1112.5927 .
