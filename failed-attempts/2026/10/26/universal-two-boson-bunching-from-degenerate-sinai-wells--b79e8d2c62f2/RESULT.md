# Universal two-boson bunching from degenerate Sinai wells

## Finding

A completely dissipative bosonic lattice with symmetric binary hopping disorder has a sharp, disorder-independent high-loading bunching law. In the sequential limit where the number of particles tends to infinity on each fixed finite chain and the chain length then tends to infinity, the annealed probability that two distinct particles occupy the same site tends to

\[
\boxed{4\log 2-2=0.772588722239\ldots.}
\]

The limiting particle fractions across the degenerate deepest disorder wells form a finite-dimensional Dirichlet distribution; the number of such wells tends to a geometric random variable. For every strictly positive binary-disorder magnitude the limit above holds, whereas it equals zero when the disorder magnitude vanishes exactly. A finite-length generating function determines the full high-loading sequence, not just its limit.

## Assumptions and scope

Fix an integer \(L\ge2\), an integer total boson number \(N\ge2\), and a scale \(Q>0\). Consider the open chain with bosonic annihilation operators \(a_i\). There is no coherent Hamiltonian hopping. The only Lindblad operators, for bonds \(i=1,\ldots,L-1\), are

\[
L_i^R=\sqrt{Qe^{-h_i}}\,a_{i+1}^{\dagger}a_i,\qquad
L_i^L=\sqrt{Qe^{h_i}}\,a_i^{\dagger}a_{i+1}.
\]

Here \(h_i=h\varepsilon_i\), with \(h>0\) fixed and \(\varepsilon_i\) independent symmetric signs. Write \(S_1=0\), \(S_i=\sum_{j<i}\varepsilon_j\) and \(w_i=\exp(-2hS_i)\). Let \(\eta=(\eta_1,\ldots,\eta_L)\) be the integer occupations, with \(\sum_i\eta_i=N\). The population Markov chain has hopping rates

\[
Qe^{-h_i}\eta_i(\eta_{i+1}+1),\quad
Qe^{h_i}\eta_{i+1}(\eta_i+1).
\]

The diagonal density matrix constructed from the stationary occupation law is a stationary quantum state in this fixed-number sector. No statement about off-diagonal stationary states or a nonzero coherent Hamiltonian is needed.

Let \(T_L=\{i:S_i=\min_jS_j\}\), \(K_L=|T_L|\), and for fixed disorder define the conditional stationary pair co-location probability

\[
b_{L,N}=\mathbf E_{\pi_{L,N}}\left[\sum_{i=1}^L\frac{\eta_i(\eta_i-1)}{N(N-1)}\right].
\]

Let \(B_{L,N}=\mathbf E_{\varepsilon}b_{L,N}\). We study the limits IN THIS ORDER: first \(N\to\infty\) for each fixed \(L\), then \(L\to\infty\), for any fixed \(h>0\). This is a high-loading/long-chain sequential limit, **not** a fixed-density thermodynamic limit.

For the generating-function convention below, set \(B_1=1\) on the trivial one-site chain. The full conclusions are:

1. Conditional on each realization, the normalized occupations at \(T_L\) converge jointly to \(\operatorname{Dirichlet}(1,\ldots,1)\) of dimension \(K_L\), with all other normalized occupations tending to zero. Thus \(\lim_{N\to\infty} b_{L,N}=2/(K_L+1)\).
2. \(\lim_{L\to\infty}\mathbf P(K_L=k)=2^{-k}\) for each fixed integer \(k\ge1\).
3. Let \(B_L=\lim_{N\to\infty}B_{L,N}\), and define \(E(t)=(1-\sqrt{1-4t^2})/2\). The complete sequence has the formal power-series identity

\[
\sum_{L\ge1}2^{L-1}B_Lt^{L-1}
=\frac{2(1-E(t))\big[-\log(1-E(t))-E(t)\big]}{E(t)^2(1-2t)},
\]

where the removable singularity at \(E=0\) is interpreted by its power series. Consequently

\[
\lim_{L\to\infty}B_L=4\log2-2.
\]

At \(h=0\), the exact high-loading value is \(B_L=2/(L+1)\); its long-chain limit is zero.

## Proof

**Stationary canonical law.** For a transition moving one boson from site \(i\) to site \(i+1\), the occupation factors in the reverse transition cancel exactly with those in the forward transition. Their rate ratio is \(e^{-2h_i}=w_{i+1}/w_i\). Hence detailed balance holds for

\[
\pi_{L,N}(\eta)=\frac{1}{Z_{L,N}}
\mathbf1_{\{\sum_i\eta_i=N\}}\prod_{i=1}^Lw_i^{\eta_i}.
\]

The finite occupation chain is irreducible, so this law is the unique stationary population law. This stationary-measure principle is a known special case of the reversible inclusion-process construction of Grosskinsky–Redig–Vafayi (2011), with inclusion parameter \(m=2\); it is not asserted as a novel theorem.

**Macroscopic occupation of repeated wells.** Normalize the weights by their maximum. On \(T_L\) the new weights equal one, and on its complement they are strictly below one. If \(M\) particles occupy the nonminimal sites, then the number of compatible ground-well allocations is \(\binom{N-M+K_L-1}{K_L-1}\), independently of the split among the ground wells. For any fixed nonminimal configuration the ratio of this count to \(\binom{N+K_L-1}{K_L-1}\) tends to one and is bounded by one. Summing the corresponding geometric tails over the finitely many nonminimal sites and using dominated convergence shows that \(M\) is tight as \(N\to\infty\), while conditional on \(M\) all weak compositions among the \(K_L\) ground sites have equal weight. Their uniform grid distribution on the simplex converges to the uniform Dirichlet law. Since \(\mathbf E\sum_{i=1}^k P_i^2=2/(k+1)\) for \((P_1,\ldots,P_k)\sim\operatorname{Dirichlet}(1,\ldots,1)\), bounded convergence proves \(b_{L,N}\to2/(K_L+1)\), including \(K_L=1\).

**Global-minimum multiplicities.** Put \(n=L-1\). Consider every length-\(n\) walk with signs \(\pm1\), and mark its number \(K\) of visits (including endpoints) to its global minimum. A path factors uniquely into a strictly positive meander before the first minimum (read backward), a sequence of strictly positive excursions from one minimum visit to the next, and a strictly positive meander after the last minimum. Let \(A(t)\) be the generating series of strictly positive meanders (including the empty path) and \(E(t)\) the generating series of strictly positive return excursions. By the Catalan decomposition,

\[
E(t)=\sum_{m\ge1}C_{m-1}t^{2m}
=\frac{1-\sqrt{1-4t^2}}2.
\]

Counting all paths after forgetting the minimum-visit mark gives \(A(t)^2/(1-E(t))=1/(1-2t)\). Thus the **exact bivariate counting generating function** is

\[
F(t,z)=\sum_{n\ge0}\sum_{\varepsilon\in\{\pm1\}^n}
 t^nz^{K(\varepsilon)}
=\frac{z(1-E(t))}{(1-zE(t))(1-2t)}.
\]

For each fixed integer \(k\ge1\), its coefficient of \(z^k\) is \((1-E(t))E(t)^{k-1}/(1-2t)\). The power-series coefficients of \((1-E)E^{k-1}\) are absolutely summable after weighting by \(2^{-n}\): both \(E^{k-1}\) and \(E^k\) have nonnegative coefficients and finite sums at \(t=1/2\). Therefore the coefficient-convolution identity

\[
2^{-n}[t^n]\frac{g(t)}{1-2t}
=\sum_{j=0}^n2^{-j}[t^j]g(t)
\longrightarrow g(1/2)
\]

applies with \(g=(1-E)E^{k-1}\). Since \(E(1/2)=1/2\), the limiting probability is \((1/2)^k\). These limits sum to one, proving convergence in distribution to the geometric law on positive integers.

**Exact annealed sequence and limit.** The high-loading pair probability for a configuration of length \(n\) is \(2/(K+1)=2\int_0^1z^K\,dz\). Hence its unnormalized length generating function is \(2\int_0^1F(t,z)\,dz\), and elementary integration yields

\[
2\int_0^1F(t,z)\,dz
=\frac{2(1-E(t))[-\log(1-E(t))-E(t)]}{E(t)^2(1-2t)}.
\]

The bounded function \(k\mapsto 2/(k+1)\) and the geometric convergence then imply

\[
\lim_{L\to\infty}B_L
=\sum_{k\ge1}\frac{2^{1-k}}{k+1}
=4\log2-2.
\]

The result is independent of \(h>0\) because a fixed nonzero disorder amplitude changes weight gaps but not which potential heights coincide. When \(h=0\), every site is a ground site, so the normalized occupation vector tends to \(\operatorname{Dirichlet}(1,\ldots,1)\) on all \(L\) sites and \(B_L=2/(L+1)\). The two sequential limits therefore do not commute with setting the disorder amplitude to zero.

## Verification

Run `python3 verify_condensate.py` in any Python 3.11+ installation. It uses only the standard library. Its deterministic checks enumerate symmetric walks of 0 through 12 steps and compare their exact global-minimum multiplicity polynomials with the Catalan generating function; verify finite-particle detailed-balance ratios and exact canonical pair expectations using rational weights; test the clean finite-chain value \(2/(L+1)\); and independently check truncated geometric sums and high-loading convergence. The script reports 142018 passing exact/deterministic assertions. The infinite limits are proved above, not inferred from these finite tests.

## Relationship to prior work

Longhi (2026, arXiv:2602.14698) introduced the globally reciprocal *in distribution* incoherent-hop Liouvillian with symmetric binary asymmetries, analyzed its single-particle random-potential localization and Sinai transport, and discussed the many-boson regime via mean field. The present theorem concerns a different, exact high-loading multi-boson stationary observable for its strictly incoherent specialization.

Grosskinsky, Redig and Vafayi (2011, arXiv:1009.2799, Theorem 2.1 and Section 2.2) already proved general reversible product and canonical measures for inclusion processes. Those results **subsume the stationary canonical formula**, and their unique-largest-weight condensation theorem handles related nondegenerate settings. The conditional Dirichlet splitting is a standard combinatorial limit once the known canonical distribution is given. The model-specific claim assessed here is the random degeneracy profile of the deepest binary potential wells, its exact finite-length generating function, and the consequent universal two-boson bunching constant and zero-disorder discontinuity, not a rediscovery of canonical stationarity.

Garbe et al. (2023/2024, arXiv:2301.11339) study bosonic asymmetric transport with reservoirs and boundary condensation under uniform hopping bias. Jatuviriyapornchai, Chleboun and Grosskinsky (2019, arXiv:1907.12166) analyze homogeneous inclusion-process condensation, including Poisson–Dirichlet laws with vanishing diffusion parameter. Neither directly states the finite-sample symmetric binary-disorder minimum-multiplicity generating function and its pair co-location limit for the above sector.

## Limitations

The result applies to the diagonal stationary sector with zero coherent hopping, a fixed finite open chain prior to increasing particle number, equal-probability binary bond disorder, and fixed strictly positive disorder strength. It is **not** a fixed-density joint limit, not an unconditional result for nonzero Hamiltonian hopping, and not a proof of an experimentally realized dynamical condensation transition. Ground-well Dirichlet splitting and the random-walk geometric law have classical probabilistic antecedents; a broader theorem might implicitly imply parts of this special construction. Independent literature and mathematical verification remain appropriate.

## References

1. Stefano Longhi, *Erratic Liouvillian Skin Localization and Subdiffusive Transport*, arXiv:2602.14698v1 (first public posting 2026-02-16); revised arXiv HTML inspected at https://arxiv.org/html/2602.14698, especially Eqs. (6)–(7) and Appendix C.
2. Stefan Grosskinsky, Frank Redig and Kiamars Vafayi, *Condensation in the Inclusion Process and Related Models*, *Journal of Statistical Physics* 142 (2011), 952–974; arXiv:1009.2799; https://doi.org/10.1007/s10955-011-0151-9.
3. Louis Garbe, Yuri Minoguchi, Julian Huber and Peter Rabl, *The bosonic skin effect: boundary condensation in asymmetric transport*, arXiv:2301.11339; *SciPost Physics* 16 (2024), 029.
4. Watthanan Jatuviriyapornchai, Paul Chleboun and Stefan Grosskinsky, *Structure of the condensed phase in the inclusion process*, arXiv:1907.12166.
