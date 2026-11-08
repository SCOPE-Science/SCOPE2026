# Parity obstruction and Hadamard finite termination for Rademacher zeroth-order descent

## Finding
For the standard symmetric two-point Rademacher gradient estimator on \(f(x)=\|x\|_2^2/2\) in dimension \(d\), choose the mean-square-optimal constant step \(\eta=1/d\). For every odd \(d\ge3\), from any coordinate vector the exact-arithmetic iterates never equal zero after any finite number of steps, for *every* sequence of signs. Nevertheless they converge to zero almost surely. Conversely, whenever a real Hadamard matrix of order \(d\) exists, the same independent-sign iteration reaches zero almost surely in finite time from *every* initial vector. Moreover, a sequence of exactly \(d\) updates annihilates every initial vector if and only if its sign directions are the rows of a Hadamard matrix (up to ordering); hence existence of a universal \(d\)-step annihilating word is equivalent to a real Hadamard matrix of order \(d\).

## Assumptions and scope
Let \(d\ge1\), \(x_0\in\mathbb R^d\), and let independent \(u_k\) be uniform on \(\{-1,1\}^d\). Define \(\widehat g(x;u)=[f(x+\mu u)-f(x-\mu u)]u/(2\mu)=(u^\top x)u\) for arbitrary \(\mu>0\); set \(x_{k+1}=x_k-\widehat g(x_k;u_k)/d=P_{u_k}x_k\), where \(P_u=I-uu^\top/d\) is the orthogonal projector onto \(u^\perp\). All finite-termination assertions use exact arithmetic. A Hadamard matrix is a \(d\times d\) matrix with entries \(\pm1\) and orthogonal rows.

## Proof
**One-step contraction and optimality.** Since \(\mathbb E uu^\top=I\), \(P_u^2=P_u\), and \(\|u\|^2=d\), we have \(\mathbb E\|P_ux\|^2=(1-1/d)\|x\|^2\). At a general step \(\eta\), the factor is \(1-2\eta+d\eta^2\), uniquely minimized at \(\eta=1/d\). Thus \(\mathbb E\|x_k\|^2=(1-1/d)^k\|x_0\|^2\) and Markov's inequality plus monotonicity (or Borel–Cantelli) yields almost-sure convergence for every \(d\ge2\).

**Odd-dimensional arithmetic obstruction.** For odd \(d\ge3\), let \(B_u=dI-uu^\top\), an integral matrix. Modulo 2 every sign vector equals the all-ones vector, and \(B_u\equiv Q:=I+J\pmod2\), where \(J\) is the all-ones matrix. Since \(d\) is odd, \(J^2=dJ\equiv J\), hence \(Q^2=I+J=Q\) over \(\mathbb F_2\). Therefore for any signs and \(k\ge1\), \(d^k x_k=B_{u_{k-1}}\cdots B_{u_0}e_i\equiv Qe_i\pmod2\), where \(Qe_i\) has one zero and \(d-1\) ones. It is nonzero, so the integer numerator \(d^kx_k\) cannot vanish, proving \(x_k\ne0\). For \(k=0\) the assertion is immediate. In fact the same holds for every integer starting vector whose residues modulo 2 are neither all zero nor all one: \(Qv=v+(\sum_i v_i)\mathbf1\) has kernel \(\operatorname{span}\{\mathbf1\}\) in odd dimension.

**Hadamard finite termination.** If \(u_1,\ldots,u_d\) are the mutually orthogonal rows of a Hadamard matrix, then their projectors commute and \(P_{u_d}\cdots P_{u_1}=I-\sum_{j=1}^d u_ju_j^\top/d=0\). Any consecutive block of \(d\) independent uniform sign draws equals this prescribed sequence with probability \(q=2^{-d^2}>0\). Disjoint blocks are independent, so for the stopping time \(T=\inf\{k:x_k=0\}\), \(\Pr(T>kd)\le(1-q)^k\). Thus \(T<\infty\) almost surely for every starting vector.

**Minimal universal word.** Each orthogonal projector has a one-dimensional kernel, so reducing rank from \(d\) to zero needs at least \(d\) updates. If exactly \(d\) projections have zero product, rank must drop by exactly one at each multiplication. Writing \(V_j=\operatorname{im}(P_{u_j}\cdots P_{u_1})\), rank drops at stage \(j\) exactly when \(u_j\in V_{j-1}\); then \(V_j=V_{j-1}\cap u_j^\perp\). Inductively the chosen \(u_j\) are pairwise perpendicular and form a Hadamard matrix. The converse was established above.

## Verification
The accompanying `verify.py` checks exact rational projector products for Hadamard orders \(2,4,8\), the modulo-2 obstruction on odd dimensions \(3,5,7\) across enumerated sign-word prefixes, and the exact contraction polynomial. These finite checks support, but do not replace, the arbitrary-dimensional proof above. Run `python verify.py` using Python 3's standard library.

## Relationship to prior work
Song et al., *Zeroth-Order Optimization at the Edge of Stability*, arXiv:2604.14669 (first public April 16, 2026), establish sharp mean-square spectral stability for Gaussian two-point ZO methods, and their Appendix B.2 explicitly defines the covariance operator for non-Gaussian directions. The result here instead isolates the exact-arithmetic stopping-time structure of discrete Rademacher probes. Classical randomized Kaczmarz theory supplies expected linear convergence for random projections, while classical Hadamard orthogonality underlies the annihilating word. Neither ingredient alone states the odd-dimensional modular obstruction together with the almost-sure finite-termination contrast in this particular algorithm.

## Limitations
The result is for the isotropic quadratic, exact two-point evaluations, independent uniformly random signs, the exactly tuned step \(1/d\), and exact arithmetic. It makes no assertion that all even dimensions admit finite termination or that finite termination survives roundoff. Hadamard availability is established for powers of two and many other orders, not all multiples of four. This theorem is not a characterization of all nonzero initial vectors with possible finite stopping in odd dimension.

## References
1. M. Song, L. Zhang, B. Li, N. He, M. Muehlebach, S. Oh. *Zeroth-Order Optimization at the Edge of Stability*. arXiv:2604.14669, initial posting 2026-04-16. https://arxiv.org/abs/2604.14669
2. T. Strohmer and R. Vershynin. *A randomized Kaczmarz algorithm with exponential convergence*. Journal of Fourier Analysis and Applications 15 (2009), 262–278.
3. Z.-Z. Bai and W.-T. Wu. *Randomized Kaczmarz iteration methods: Algorithmic extensions and convergence theory*. Japan Journal of Industrial and Applied Mathematics 40 (2023), 1421–1443. https://doi.org/10.1007/s13160-023-00586-7
