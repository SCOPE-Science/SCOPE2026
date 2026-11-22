# Exact entropic spectral gap for zero-temperature Ising friendship networks

## Finding
For every integer \(n\ge2\), the zero-field antiferromagnetic Ising model on the friendship graph consisting of \(n\) triangles sharing a single vertex has \(2\cdot3^n\) ground states. Restrict its continuous-time single-spin Metropolis dynamics to those ground states, proposing each individual spin flip at rate one and allowing precisely energy-neutral proposals. The chain is irreducible and reversible under the uniform measure.

Its spectral gap \(\lambda_n\) is the unique root in \((0,1)\) of
\[
1+2\sum_{k=0}^n\frac{\binom nk 2^{n-k}/3^n}{3k-\lambda_n}=0.
\]
In particular,
\[
0<\lambda_n<2(2/3)^n<1,\qquad
\lambda_n=2(2/3)^n\left(1-\frac2n+O(n^{-2})\right),
\]
and the longest relaxation time is
\[
\lambda_n^{-1}=\tfrac12(3/2)^n\left(1+\frac2n+O(n^{-2})\right).
\]
Thus the ground-state chain has an exponentially slow collective spin mode even though, with the central spin fixed, each peripheral-triangle mode has spectral gap at least one.

## Assumptions and scope
The graph \(F_n\) has vertex set \(\{o,a_1,b_1,\dots,a_n,b_n\}\), and edges \(\{oa_i,ob_i,a_ib_i:1\le i\le n\}\). Every spin is in \(\{-1,+1\}\). The Hamiltonian is \(\mathcal H(\sigma)=J\sum_{uv\in E(F_n)}\sigma_u\sigma_v\) with \(J>0\) and zero magnetic field. Its ground energy is \(-nJ\). Write \(\Omega_n\) for all ground configurations. The rate-one ground-state flip generator is
\[
(Lf)(\sigma)=\sum_{v:\sigma^v\in\Omega_n}[f(\sigma^v)-f(\sigma)],\qquad \sigma\in\Omega_n.
\]
Here \(\sigma^v\) changes precisely spin \(v\). This is the zero-temperature **Metropolis** ground-state restriction, not the conventional rate-one heat-bath chain, for which a neutral move has half this rate. All asymptotics hold as integer \(n\to\infty\).

## Proof
**Ground-state graph.** On each triangle exactly one of the three Ising bonds must have equal spins. Fixing the central spin \(s=\sigma_o\), the two outer spins can be \((-s,-s)\), \((s,-s)\), or \((-s,s)\), independently in each triangle. Call these configurations \(0,+,-\), respectively. Each peripheral spin flip connects \(0\) to one of \(+,-\), with rate one in either direction; no direct \(+\leftrightarrow-\) edge exists. Hence each central-spin sector is the product \(P_3^{\square n}\) of three-vertex paths with unit edge rates. A hub flip is legal exactly if every triangle is mixed, so the two sectors are joined by a perfect matching of \(2^n\) peripheral all-mixed configurations. These facts imply connectivity, uniform reversibility, and \(|\Omega_n|=2\cdot3^n\).

**Isolation of the slow symmetry sector.** On one sector, the Cartesian-product path Laplacian has spectrum formed from the one-factor eigenvalues \(0,1,3\). Its smallest positive eigenvalue is one. If a function on \(\Omega_n\) has conditional mean zero in each central-spin sector, its intra-sector Dirichlet energy is at least its squared \(L^2\)-norm; the inter-sector contribution is nonnegative. Let \(R\) flip all spins and let \(S_i\) swap \(a_i,b_i\). These commuting involutions preserve the chain. Every global-flip-even function orthogonal to constants has mean zero in each hub sector, as does every function odd under some \(S_i\). Therefore every such invariant subspace has spectral bottom at least one. The remaining sector is odd under \(R\) and even under all \(S_i\); its elements have the form \(f(\sigma)=\sigma_o g(q_1,\dots,q_n)\), with \(q_i=0\) for both outer spins opposite the hub, and \(q_i=1\) for either mixed state. The generator induced on \(g\) has independent bit flips \(0\to1\) at rate two and \(1\to0\) at rate one, plus killing rate two at \(B=(1,\dots,1)\) from the central flip. The associated nonnegative operator is \(H=H_0+2\mathbf1_B\), where \(H_0\) is the negative bit-flip generator.

**Rank-one spectral equation.** The reversible product-bit measure has \(\Pr(q_i=1)=2/3\); the probability of \(B\) is \(p_n=(2/3)^n\). Each one-bit operator has eigenvalues \(0,3\). The rank-one projector \(\mathbf1_B\), understood as multiplication by the indicator and the corresponding rank-one operator in this \(L^2\)-space, has spectral weight
\[
w_k=\binom nk(2/3)^{n-k}(1/3)^k\quad\text{at the eigenvalue }3k.
\]
The matrix-determinant lemma, or the rank-one resolvent equation, gives \(1+2\sum_{k=0}^n w_k/(3k-\lambda)=0\) for the unique new eigenvalue below three. Its left-hand side is strictly increasing on \((0,3)\), tends to negative infinity as \(\lambda\downarrow0\), and to positive infinity as \(\lambda\uparrow3\); the root is therefore unique. The Rayleigh quotient of the constant bit function is \(2p_n\); it is not an eigenfunction, hence \(0<\lambda_n<2p_n\le8/9<1\) for \(n\ge2\). Since all other symmetry sectors have spectrum at least one, this root is the spectral gap of the complete ground-state chain.

**Sharp asymptotic.** Separating the zero-frequency term in the secular equation gives
\[
\lambda_n=\frac{2p_n}{1+2\sum_{k=1}^n w_k/(3k-\lambda_n)}.
\]
For \(K_n\sim\operatorname{Binomial}(n,1/3)\), concentration around \(n/3\) and a Taylor expansion of \(1/(3K_n)\) away from the exponentially unlikely lower tail show \(\mathbb E[\mathbf1_{\{K_n>0\}}/(3K_n)]=n^{-1}+O(n^{-2})\). Because \(\lambda_n=O((2/3)^n)\), replacing \(3k\) by \(3k-\lambda_n\) changes the sum by an exponentially small amount. Inversion gives the stated expansion. Reciprocation gives the relaxation-time expansion.

## Verification
The included `verify.py` independently enumerates every ground configuration for \(n=2,3,4,5,6\), checks the exact legal-flip generator against the reduced two-state tensor representation for every reduced basis vector, and verifies eight exact-rational resolvent identities. It reports `FRIENDSHIP_EXACT_CHECKS_PASSED ground_states= 2178 resolvent_cases= 8`. The included `numerical_check.py`, requiring NumPy and SciPy, separately constructs full symmetric generator matrices and compares their smallest positive eigenvalues with roots of the stated secular equation for \(n=2,3,4,5\); each difference is below \(9\cdot10^{-15}\). Neither finite test substitutes for the all-\(n\) proof above.

## Relationship to prior work
Kim, Kim and Lee (2003) investigate spin-flip nonequilibrium relaxation on the infinite triangular Ising antiferromagnet and identify the role of ground-state free spins. Ismail and Salem (2003) study small frustrated triangular spin clusters. Neither studied the friendship graph with arbitrarily many triangles sharing one hub as the exact ground-state Metropolis chain. Berger, Kenyon, Mossel and Peres (arXiv 2003) analyze Glauber spectral gaps and polynomial relaxation on bounded-degree trees and hyperbolic graphs; the current graphs have cycles and unbounded central degree. Chen, Feng, Yin and Zhang (2024) establish rapid mixing within a strict uniqueness regime, not the maximally frustrated zero-temperature manifold treated here. An earlier related result on \(K_{n,n,n}\) concerns a different graph and different ground-state geometry, with no implication for these exact spectral roots.

## Limitations
The theorem is only for the ground-state-restricted Metropolis chain with rate-one neutral flips, not the full positive-temperature chain, not heat-bath-normalized time, and not dynamics beginning in an excited configuration. The fixed hub has degree \(2n\); the construction is not bounded-degree. The finite numerical checks do not establish the asymptotics independently of the mathematical proof. Literature priority cannot be exhaustively certified. Full text of Kim et al. was not accessible through the inspected public routes , although its published abstract specifies the distinct two-dimensional triangular-lattice model.

## References
- G. Ismail and A. Salem, *Dynamics of Ising spins with antiferromagnetic bonds on a triangular lattice*, phys. stat. sol. (b) 237 (2003), 530–539. First public date verified 2003-04-16. DOI: https://doi.org/10.1002/pssb.200301657.
- N. Berger, C. Kenyon, E. Mossel and Y. Peres, *Glauber Dynamics on Trees and Hyperbolic Graphs*, arXiv:math/0308284, first posted 2003-08-28. https://arxiv.org/abs/math/0308284.
- E. Kim, B. Kim and S. J. Lee, *Nonequilibrium critical dynamics of the triangular antiferromagnetic Ising model*, Physical Review E 68 (2003), 066127; publicly issued 2003-12-31. https://doi.org/10.1103/PhysRevE.68.066127.
- X. Chen, W. Feng, Y. Yin and X. Zhang, *Rapid Mixing of Glauber Dynamics via Spectral Independence for All Degrees*, SIAM Journal on Computing (2024). https://doi.org/10.1137/22M1474734.
