# Logarithmic scale mixing and Dirichlet–Gamma limits for a balanced bipartite arithmetic Ising gas

## Finding
Fix an integer \(k\geq1\) and constants \(\mu,J>0\). On the complete bipartite graph \(K_{k,k}\), assign a nonnegative integer occupation \(a_i\) to each vertex of the first part and \(b_j\) to each vertex of the second part. With \(M=\sum_{i=1}^k a_i\), \(N=\sum_{j=1}^k b_j\), and inverse temperature \(\beta>0\), use the Hamiltonian
\[
H=\mu(M+N)+JMN.
\]
Write \(Z_k(\beta)\) for its grand-canonical partition function. As \(\beta\downarrow0\),
\[
\lim_{\beta\downarrow0}\frac{(k-1)!(\beta J)^k Z_k(\beta)}{\log(1/(\beta\mu))}=1.\tag{1}
\]
For \(\beta\mu<1\), put \(L_\beta=\log(1/(\beta\mu))\) and define
\[
V_\beta=\frac{\log(1+M)}{L_\beta},\qquad Y_\beta=\beta JMN.
\]
Define \(A_\beta=(a_1/M,\ldots,a_k/M)\) for \(M>0\), and \(B_\beta=(b_1/N,\ldots,b_k/N)\) for \(N>0\); at zero totals choose any fixed vector in the probability simplex. Then the full joint weak limit is
\[
(V_\beta,Y_\beta,A_\beta,B_\beta)
\ \Longrightarrow\ (U,G,D_A,D_B),\tag{2}
\]
where \(U\) is uniform on \([0,1]\), \(G\) is gamma with shape \(k\) and unit scale, \(D_A,D_B\) are two Dirichlet\((1,\ldots,1)\) probability vectors (point masses at \((1)\) when \(k=1\)), and **all four objects on the right are independent**. Thus the two total occupations vary over complementary powers of inverse temperature rather than concentrate on a fixed power, even though their interaction energy has a fixed gamma law.

For the same Gibbs system, \(\beta H\) converges in distribution with all finite moments to \(G\). In particular,
\[
\lim_{\beta\downarrow0}\beta\,\mathbb E_\beta H=k,
\qquad\lim_{\beta\downarrow0}\beta^2\operatorname{Var}_\beta(H)=k.\tag{3}
\]
Equation (3) is a consequence of the full result; the energy equipartition exponent alone is not presented as original.

## Assumptions and scope
The graph is precisely \(K_{k,k}\) with one undirected edge between each pair of opposite-part vertices; \(J>0\) is the energy coefficient **per such edge**. The occupations are unrestricted nonnegative integers with counting-measure single-site weights. Both \(k\) and \(\mu,J\) are fixed while \(\beta\downarrow0\). There is no particle-number constraint, quantum hopping, or thermodynamic limit in graph size. The periodic \(2\times2\) model discussed by Dhochak–Kikuchi–Singh has the same two-group form with \(k=2\) and their displayed double-sum normalization \(J=2U\); a different bond-counting convention can be represented by a different \(J\), without changing the theorem.

## Proof
**Exact reduction.** The number of weak compositions of \(m\) into \(k\) occupations is \(c_k(m)=\binom{m+k-1}{k-1}\). Therefore, by summing the opposite sublattice's geometric generating function,
\[
Z_k(\beta)=\sum_{m,n\geq0}c_k(m)c_k(n)
 e^{-\beta[\mu(m+n)+Jmn]}
=\sum_{m\geq0}\frac{c_k(m)e^{-\beta\mu m}}
{[1-e^{-\beta(\mu+Jm)}]^k}.\tag{4}
\]
All sums converge absolutely because \(\mu>0\). The same identity with \(J\) replaced by \((1+t)J\) gives the exact numerator of the Laplace transform of \(Y_\beta\) for every \(t\geq0\).

**Sharp logarithmic constant.** Denote the summand in (4) by \(q_\beta(m)\). Fix a large integer \(R\) and a small \(\varepsilon>0\). Uniformly in \(R\leq m\leq\varepsilon/\beta\), the estimates
\[
c_k(m)=\frac{m^{k-1}}{(k-1)!}(1+O_k(m^{-1})),
\quad 1-e^{-\beta(\mu+Jm)}=\beta(\mu+Jm)(1+O_{J,\mu}(\varepsilon+\beta))
\]
imply
\[
q_\beta(m)=\frac{1+O_{k,\mu,J}(R^{-1}+\varepsilon+\beta)}{(k-1)!(\beta J)^k m}.
\]
For fixed \(R\), the contribution from \(m<R\) is \(O_R(\beta^{-k})\). For fixed \(\varepsilon>0\), the contribution from \(m>\varepsilon/\beta\) is \(O_\varepsilon(\beta^{-k})\): the denominator in (4) is bounded below by \([1-e^{-J\varepsilon}]^k\), while \(\sum_m c_k(m)e^{-\beta\mu m}=O(\beta^{-k})\). Hence the central harmonic sum equals \(\log(1/\beta)+O_{R,\varepsilon}(1)\); first letting \(\beta\downarrow0\), then \(R\uparrow\infty\) and \(\varepsilon\downarrow0\) proves (1). Replacement of \(\log(1/\beta)\) by \(L_\beta\) changes its value only by a bounded constant.

**Joint logarithmic coordinate and interaction law.** For any fixed \(0<a<b<1\), uniformly for \(m\) with \(\beta^{-a}\leq1+m\leq\beta^{-b}\), the previous estimate improves to \(q_\beta(m)=(1+o(1))/[(k-1)!(\beta J)^k m]\). Consequently
\[
\lim_{\beta\downarrow0}\mathbb E_\beta
\left[\mathbf1_{\{a\leq V_\beta\leq b\}}e^{-tY_\beta}\right]
=\frac{b-a}{(1+t)^k},\qquad t\geq0.\tag{5}
\]
Here the lower and upper cutoffs for \(V_\beta\) may equivalently use powers of \(\beta\mu\), since fixed \(\mu\) only shifts logarithms by \(O(1)\). In the numerator, multiplication by \(e^{-t\beta Jmn}\) replaces \(J\) with \((1+t)J\); applying the uniform summand estimate and (1) gives (5). At \(t=0\), (5) also proves \(V_\beta\Rightarrow\mathrm{Unif}(0,1)\): the distribution has mass \(b-a\) on every interior interval, with no residual mass outside \([0,1]\), since \(V_\beta\geq0\) and the intervals exhaust unit mass. Joint Laplace-transform uniqueness then identifies independent \(U\) and \(G\), because \((1+t)^{-k}\) is the Laplace transform of \(\mathrm{Gamma}(k,1)\).

**Microscopic shares.** Conditional on \(M=m,N=n\), every weak composition within each part is equally likely, and the two choices are independent. The uniform weak-composition vector divided by its total converges, as the total tends to infinity, to normalized Lebesgue measure on the \((k-1)\)-simplex, namely \(\mathrm{Dirichlet}(1,\ldots,1)\). The proof of (1), together with (4), yields \(\Pr_\beta(M\leq R)=O_R(1/L_\beta)\); symmetry gives the same bound for \(N\). Thus both totals tend to infinity in probability. Uniform Riemann-sum approximation for bounded continuous simplex tests, conditionally on totals, proves that the two Dirichlet vectors converge jointly and independently of each other and \((U,G)\). This proves (2).

**Total energy.** For \(-1<s<1\) (only \(s<1\) is needed), the moment-generating function of \(\beta H\) is exactly
\[
\mathbb E_\beta e^{s\beta H}
=\frac{Z_k((1-s)\beta)}{Z_k(\beta)}
\longrightarrow(1-s)^{-k}.
\]
The ratio follows from (1). For some fixed \(s\in(0,1)\), these moment-generating functions are uniformly bounded, ensuring uniform integrability of every polynomial moment. This proves (3) and the asserted total-energy limit. With Boltzmann's constant one, the specific heat \(\beta^2\operatorname{Var}_\beta H\) consequently tends to \(k\).

## Verification
The self-contained `check.py` uses finite composition counts, an independent truncated double sum, exact resummation of one part, the zero-interaction benchmark, and high-temperature one-decade increments. It passed 100 deterministic checks. For \(\mu=1,J=2\) the final measured normalized increments \((k-1)!J^k[\beta^k Z_k(\beta)]\) from \(\beta=10^{-4}\) to \(10^{-5}\) were \(2.302063\), \(2.301273\), and \(2.294666\) for \(k=1,2,3\), approaching \(\log10=2.302585\). This convergence is deliberately slow because of the logarithmic correction; finite checks are not proofs of (1)–(3). The analytic arguments above establish all infinite limits.

## Relationship to prior work
Dhochak, Kikuchi, and Singh (2026), arXiv:2608.19605v1, derive the exact \(k=2\) double sum (their Eq. (9)) and present numerical free-energy and entropy curves. That source is credited for the finite-volume exact partition representation. Andriolo, Nguyen, Richards, and Sulejmanpasic (2026), arXiv:2604.09768v2, prove the general high-temperature exponent and the existence of a logarithmic factor associated with the fractional-independent-set moduli space; consequently **the power \(\beta^{-k}\), the presence of \(\log(1/\beta)\), and equipartition by themselves are prior-covered and not claimed as new**. The distinction here is the exact leading coefficient in (1), the full independent log-uniform/Gamma/Dirichlet weak limit (2), and their explicit characterization on the natural balanced complete-bipartite family. Huang et al. (2025), arXiv:2512.07980, motivate the arithmetic Ising Hamiltonian and entropic ordering. Mehta and related work on high-temperature checkerboard order concern infinite-lattice phase stability, not the specified finite-graph joint distribution.

## Limitations
All limits take temperature to infinity at **fixed graph size**; neither spontaneous symmetry breaking nor an infinite-lattice order parameter is proved. For finite \(\beta\), the four limiting variables are not exactly independent. The first-order coefficient in (1) does not give the finite-temperature error constant; numerical convergence can be slow. Interactions involving unequal bipartite sizes, noncomplete graphs, onsite repulsion or quantum hopping are outside scope. Prior general finite-graph asymptotic theory already predicts the power-and-log orders, and an unindexed refinement of its flat-direction analysis could conceivably cover part of the present distributional result.

## References
1. A. Dhochak, K. Kikuchi, S. Singh, *Exact partition function of arithmetic Ising model*, arXiv:2608.19605v1, first public 2026-08-20. https://arxiv.org/html/2608.19605
2. E. Andriolo, M. Nguyen, E. Richards, T. Sulejmanpasic, *Proof of entropic order in Generalized Ising Models*, arXiv:2604.09768v2, first public 2026-04-10. https://arxiv.org/html/2604.09768v2
3. X. Huang, Z. Komargodski, A. Lucas, F. K. Popov, T. Sulejmanpasic, *Minimal Models of Entropic Order*, arXiv:2512.07980, first public 2025-12-08. https://arxiv.org/html/2512.07980
4. R. Mehta, *Order by disorder up to arbitrarily high temperature*, arXiv:2604.28026, first public 2026-04-30. https://arxiv.org/abs/2604.28026
