# Log-uniform occupation and gamma energy in the four-site arithmetic Ising model

## Finding

For four nonnegative-integer occupations on the cycle graph \(C_4\), with a positive chemical-potential penalty \(\mu>0\) and repulsive edge coupling \(\kappa>0\), the high-temperature Gibbs state has a joint distributional limit that is not concentrated at a single occupation scale. Let \(A=n_1+n_3\), \(B=n_2+n_4\), \(H=\kappa AB+\mu(A+B)\), and \(L_\beta=\log[1/(\beta\kappa)]\). As \(\beta\downarrow0\),

\[
\left(\frac{\log(1+A)}{L_\beta},\frac{\log(1+B)}{L_\beta},\beta H\right)\ \Longrightarrow\ (1-T,T,G),
\]

where \(T\) is uniform on \([0,1]\), \(G\) has the gamma distribution with shape \(2\) and rate \(1\), and \(T\) and \(G\) are independent. The analogous limit holds with \(\beta\kappa AB\) replacing \(\beta H\). Moreover,

\[
Z_\beta=\frac{L_\beta+O(1)}{(\beta\kappa)^2},\qquad
S_\beta=2L_\beta+\log L_\beta+2+o(1),
\]

where \(S_\beta=\log Z_\beta+\beta\mathbb E_\beta H\) is Gibbs entropy in units of Boltzmann's constant. All limits hold for every fixed pair \(\kappa,\mu>0\). In particular, the leading partition-function coefficient and the finite entropy constant are independent of \(\mu\). The logarithmic occupation law is a finite-cluster description of the marginal, one-dimensional fractional-independent-set manifold, not an infinite-volume phase-transition claim.

## Assumptions and scope

There are exactly four labelled vertices with edges \(\{1,2\},\{2,3\},\{3,4\},\{4,1\}\), each counted once. Every \(n_i\) ranges independently over \(\mathbb N_0\). The canonical probability of a configuration is \(Z_\beta^{-1}e^{-\beta H}\), with \(\beta>0\). Finite \(\mu>0\) ensures normalization. Equivalently, the directed-neighbour convention on the \(2\times2\) periodic square torus doubles each of these four physical edge weights and corresponds to \(\kappa=2U\), with \(U>0\); the simple four-cycle convention corresponds to \(\kappa=U\). The theorem is uniform in the choice of either convention after fixing \(\kappa\). The limit \(\beta\downarrow0\) is taken with \(\kappa,\mu\) held fixed, and \(L_\beta>0\) once \(\beta\kappa<1\).

The gamma law is defined by the density \(y e^{-y}\,\mathbf1_{y>0}\), and \(\Longrightarrow\) means weak convergence on \(\mathbb R^3\). The \(O(1)\) constant may depend on \(\mu/\kappa\); it is bounded as \(\beta\) tends to zero. No claim is made about allowing \(\mu/\kappa\) to vary with temperature.

## Proof

**Exact sublattice reduction.** The four edges join the two opposite-vertex pairs completely, so their interaction sum is \(AB\). There are exactly \(a+1\) choices for a nonnegative ordered pair with sum \(a\). Therefore, for every \(\beta>0\), absolute convergence and the geometric generating function give

\[
Z_\beta=\sum_{a,b\ge0}(a+1)(b+1)e^{-\beta[\kappa ab+\mu(a+b)]}
=\sum_{b\ge0}\frac{(b+1)e^{-\beta\mu b}}{(1-e^{-\lambda_b})^2},
\qquad \lambda_b=\beta(\mu+\kappa b).
\tag{1}
\]

Call the summand \(w_\beta(b)\). Conditional on \(B=b\), \(A\) has the negative-binomial law

\[
\mathbb P_\beta(A=a\mid B=b)
=(a+1)(1-e^{-\lambda_b})^2e^{-\lambda_b a},\qquad a\in\mathbb N_0.
\tag{2}
\]

**Sharp partition function.** Fix \(\kappa,\mu>0\) and let \(N=\lfloor\beta^{-1}\rfloor\). Taylor expansion uniformly over \(0\le b\le N\), using boundedness of \(\lambda_b\), yields

\[
\beta^2w_\beta(b)=\frac{b+1}{(\mu+\kappa b)^2}\left[1+O\bigl(\beta(b+1)\bigr)\right].
\tag{3}
\]

The summed error in (3) is \(O(1)\), since \((b+1)^2/(\mu+\kappa b)^2\) is bounded. Further,

\[
\sum_{b=0}^N\frac{b+1}{(\mu+\kappa b)^2}
=\kappa^{-2}\log N+O(1).
\tag{4}
\]

For \(b>N\), \(1-e^{-\lambda_b}\ge1-e^{-\kappa}\) for small \(\beta\), and hence \(\beta^2\sum_{b>N}w_\beta(b)=O(1)\) by the exponential factor \(e^{-\beta\mu b}\). Combining (3)-(4) proves

\[
\beta^2\kappa^2Z_\beta=L_\beta+O(1).
\tag{5}
\]

**Uniform logarithmic occupation.** Fix \(0<u<v<1\). For integer \(b\) between \((\beta\kappa)^{-u}\) and \((\beta\kappa)^{-v}\), both \(b\to\infty\) and \(\beta b\to0\) uniformly. Equation (3), now with relative error \(o(1)\), implies

\[
\sum_{(\beta\kappa)^{-u}\le b\le(\beta\kappa)^{-v}}w_\beta(b)
=\frac{(v-u)L_\beta+o(L_\beta)}{(\beta\kappa)^2}.
\tag{6}
\]

With (5) this shows \(\log(1+B)/L_\beta\Longrightarrow T\), uniform on \([0,1]\); the endpoint tails follow from (3)-(5), first restricting to \([\delta,1-\delta]\), then sending \(\delta\downarrow0\). For a conditioning value with \(\delta\le\log(1+b)/L_\beta\le1-\delta\), \(\lambda_b\to0\), \(\kappa b/(\mu+\kappa b)\to1\), and

\[
\mathbb E_\beta[e^{-s\lambda_b A}\mid B=b]
=\left(\frac{1-e^{-\lambda_b}}{1-e^{-(1+s)\lambda_b}}\right)^2
\longrightarrow(1+s)^{-2},\qquad s\ge0,
\tag{7}
\]

uniformly in this conditioning range. Thus \(\lambda_b A\) converges conditionally, uniformly away from the logarithmic endpoints, to \(G\sim\Gamma(2,1)\), independently of the limiting \(T\). Since \(\lambda_b/(\beta\kappa b)\to1\), the same holds for \(\beta\kappa AB\). The gamma limit is positive and finite almost surely, and \(-\log\lambda_b/L_\beta=1-\log(1+b)/L_\beta+o(1)\) uniformly on compact logarithmic intervals. Applying these facts to \(\log(1+A)\) and then discarding the negligible endpoint tails establishes

\[
\left(\log(1+A)/L_\beta,\log(1+B)/L_\beta,\beta\kappa AB\right)
\Longrightarrow(1-T,T,G),\qquad T\perp G.
\tag{8}
\]

In these same compact logarithmic intervals, \(\beta\mu B\to0\) and \(\beta\mu A=\mu\lambda_b A/(\mu+\kappa b)\to0\) in probability, uniformly using (7). Endpoint negligibility implies \(\beta\mu(A+B)\to0\) in probability. Slutsky's theorem gives the asserted full-energy limit.

**Entropy.** Under (2), \(\mathbb E[A\mid B=b]=2/(e^{\lambda_b}-1)\). Therefore

\[
0\le\mathbb E_\beta[\beta\kappa AB\mid B=b]
=\frac{2\beta\kappa b}{e^{\lambda_b}-1}\le2.
\tag{9}
\]

The conditional expression tends to \(2\) uniformly on every interior logarithmic range, so dominated convergence with (6) proves \(\mathbb E_\beta[\beta\kappa AB]\to2\). Also, (3) and the tail bound give \(\sum_{b\ge0}b\,w_\beta(b)=O(\beta^{-3})\); hence (5) implies \(\beta\mu\mathbb E_\beta B=O(L_\beta^{-1})\). Symmetry gives the same for \(A\), so \(\beta\mathbb E_\beta H\to2\). Taking logarithms in (5), \(\log Z_\beta=2L_\beta+\log L_\beta+o(1)\), and the Gibbs entropy formula gives the stated expansion. \(\square\)

## Verification

The accompanying standalone `verify.py` checks the edge-counting reduction against direct four-spin enumeration with finite caps, uses the conditional negative-binomial and energy identities to compute partition and occupation diagnostics directly from the one-dimensional positive series (1) at successive inverse temperatures. This is a finite computational cross-check, **not** a proof of the weak limits. The proof above supplies the all-parameter asymptotics and boundary control.

To reproduce: use Python 3 with NumPy and run `python verify.py` from the directory containing this file. The code evaluates a finite positive sum with exponentially controlled tail; it does not simulate a Monte Carlo process.

## Relationship to prior work

Dhochak, Kikuchi and Singh (arXiv:2608.19605v1, first public 2026-08-20) obtain an exact \(2\times2\) arithmetic-Ising partition series in their directed-bond convention, equivalent to (1) with \(\kappa=2U\). The exact series and the model are theirs; the distributional logarithmic occupation/independent gamma-energy limit, exact leading coefficient and entropy constant are the statements established here, rather than a new finite-temperature partition representation. Their paper describes high-temperature entropy qualitatively from plots, not these weak limits.

Andriolo, Nguyen, Richards and Sulejmanpasic (arXiv:2604.09768v2, first public 2026-04-10) prove the general high-temperature power and logarithmic **orders** of occupied-subgraph weights using fractional-independent-set moduli, and obtain the leading equipartition coefficient; for a fully occupied even cycle at the marginal exponent, their theory already predicts the \(\beta^{-2}\log(1/\beta)\) order. It neither supplies the amplitude \(\kappa^{-2}\) nor a joint Gibbs law on the logarithmic scales and the interaction energy for this four-site object. The general fractional-independent-set framework strongly motivates the present finer limit and should not be mistaken for unrelated work. Huang and collaborators (arXiv:2512.07980v2, first public 2025-12-08) introduce and study the arithmetic Ising model and its entropic-order mechanism using mean-field and numerical methods.

## Limitations

This is a statement for exactly four sites and fixed positive couplings, not a thermodynamic-limit result. It does not claim the existence of spontaneous symmetry breaking on an infinite lattice. The source's full partition-series identity trivially determines finite-temperature probabilities; deriving the singular joint limit still requires the analysis given here. The logarithmic factor and equipartition exponent are prior results, not new claims. A more general theorem giving an explicit joint limit on marginal fractional-independent-set manifolds, if it exists outside the literature inspected, could cover this statement; publication priority remains subject to such a comparison and independent review. No assertion is made at \(\mu=0\), \(\kappa=0\), or with parameters varying with \(\beta\).

## References

1. A. Dhochak, K. Kikuchi, S. Singh, *Exact partition function of arithmetic Ising model*, arXiv:2608.19605v1 (submitted 2026-08-20), https://arxiv.org/abs/2608.19605.
2. E. Andriolo, M. Nguyen, E. Richards, T. Sulejmanpasic, *Proof of entropic order in Generalized Ising Models*, arXiv:2604.09768v2 (first submitted 2026-04-10), https://arxiv.org/abs/2604.09768.
3. X. Huang, Z. Komargodski, A. Lucas, F. K. Popov, T. Sulejmanpasic, *Minimal Models of Entropic Order*, arXiv:2512.07980v2 (first submitted 2025-12-08), https://arxiv.org/abs/2512.07980.
