# Sharp finite-size onset of stationary bimodality in a triadic SIS chain with spontaneous infection

## Finding

For each integer \(N\ge3\), recovery rate \(\mu>0\), spontaneous infection rate \(0<\varepsilon<\mu/N\), and triadic intensity \(\gamma\ge0\), let the infected count be the continuous-time birth–death chain on \(\{0,\ldots,N\}\) with birth rate \(b_i=(N-i)(\varepsilon+\gamma i(i-1)/[(N-1)(N-2)])\) and death rate \(d_i=\mu i\). Put \(m=\lfloor N/2\rfloor\) and \(\Gamma_N=(N-1)(N-2)[\mu(m+2)/(N-m-1)-\varepsilon]/[m(m+1)]\). Its unique stationary law is strictly decreasing for \(\gamma<\Gamma_N\), nonincreasing with exactly one nontrivial adjacent equality \(\pi_{m+1}=\pi_{m+2}\) at \(\gamma=\Gamma_N\), and has precisely two separated local modal plateaus for \(\gamma>\Gamma_N\): the singleton at zero and one upper mode or two-point upper plateau. The upper plateau begins at an infected count at least three. In the vanishing-importation limit, for every \(m\ge2\), \(\Gamma_{2m}(\mu,0^+)=\Gamma_{2m+1}(\mu,0^+)=2\mu(2m-1)(m+2)/[m(m+1)]\). This parity-paired threshold attains its global maximum \(21\mu/5\) at \(m=4,5\) (population sizes 8,9,10,11) and tends to \(4\mu\) from above. Here a local modal plateau means a maximal consecutive block of equal stationary probabilities strictly higher than any immediate outside neighbor.

The cutoff is exact for each finite population, including the equality case and upper-mode ties. An interesting finite-size effect is the parity-paired, nonmonotone threshold in the rare-importation limit: its maximum occurs at intermediate sizes rather than in the infinite-population limit.

## Assumptions and scope

Fix \(N\in\mathbb Z\) with \(N\ge3\). The population forms a complete 2-dimensional simplicial complex: every triple is an interaction group. Each susceptible individual is spontaneously infected at rate \(\varepsilon>0\) and receives an additional rate \(\gamma/\binom{N-1}{2}\) for each pair of infected other individuals. Every infected individual recovers independently at rate \(\mu\). There is no pairwise contact-infection term. Throughout the finite-threshold claim, assume \(\mu>0\), \(0<\varepsilon<\mu/N\), and \(\gamma\ge0\). A population configuration with \(i\) infected individuals induces the infected-count birth–death chain on \(\{0,1,\dots,N\}\), with
\[
 b_i=(N-i)\left(\varepsilon+\gamma\frac{i(i-1)}{(N-1)(N-2)}\right),\qquad d_i=\mu i.
\]
Write \(\pi_i\) for the stationary probability of count \(i\). A *local modal plateau* is a maximal nonempty interval of consecutive indices on which \(\pi_i\) is constant and whose immediate exterior neighbors, if any, have strictly smaller probability; endpoints of \(\{0,\dots,N\}\) count as having no exterior neighbor. A singleton interval is permitted. Consequently a flat shoulder during overall descent is *not* a local modal plateau. We distinguish the stationary distribution (which always exists for positive importation) from the absorbing, unseeded process at \(\varepsilon=0\).

## Proof

**Exact law and edge tests.** Positive spontaneous importation and positive recovery make the finite birth–death chain irreducible. By detailed balance,
\[
 \pi_i=\frac{w_i}{\sum_{j=0}^Nw_j},\quad w_0=1,\quad w_i=\prod_{h=0}^{i-1}\frac{b_h}{\mu(h+1)}\quad(1\le i\le N).
\]
Thus \(r_i:=\pi_{i+1}/\pi_i=b_i/[\mu(i+1)]\). The importation hypothesis yields \(r_0=N\varepsilon/\mu<1\) and \(r_1=(N-1)\varepsilon/(2\mu)<1\). For each \(2\le i\le N-1\), define
\[
 G_i=\frac{(N-1)(N-2)}{i(i-1)}\left(\frac{\mu(i+1)}{N-i}-\varepsilon\right).
\]
These are positive and \(r_i\gtreqless1\) exactly when \(\gamma\gtreqless G_i\). In particular, every possible increasing edge in the stationary probability sequence must begin at count at least two.

**A single sharp valley in the edge thresholds.** Put \(a=N\varepsilon/\mu\in(0,1)\). Dividing \(G_i\) by the common positive factor \(\mu(N-1)(N-2)\), set
\[
 g_i(a)=\frac{(i+1)/(N-i)-a/N}{i(i-1)}.
\]
For \(2\le i\le N-2\), the denominator of \(g_{i+1}-g_i\) is positive. Its numerator is affine in \(a\). At \(a=0\) the numerator, after removal of positive factors, has sign
\[
 P_0=2i^2+5i+1-N(i+3),
\]
and at \(a=1\) its sign is that of
\[
 P_1=(2i-N)(N+1)(i+1).
\]
For \(i\le\lfloor N/2\rfloor\), we have \(N\ge2i\), so \(P_0\le1-i<0\) and \(P_1\le0\). For \(i\ge\lfloor N/2\rfloor+1\), we have \(N\le2i-1\), so \(P_0\ge4>0\) and \(P_1>0\). Since the numerator depends affinely on \(a\) and \(0<a<1\), it follows that \(G_i\) strictly decreases up to index \(m+1\) and strictly increases thereafter, with unique minimum \(G_{m+1}\). Substitution gives
\[
 \Gamma_N=G_{m+1}=\frac{(N-1)(N-2)}{m(m+1)}\left(\frac{\mu(m+2)}{N-m-1}-\varepsilon\right).
\]
For \(N=3\), there is just one threshold \(G_2\), so the same conclusion holds without differences.

**Modal classification.** If \(\gamma<\Gamma_N\), all edge ratios are strictly below one. If \(\gamma=\Gamma_N\), the only ratio equal to one is \(r_{m+1}\); every other ratio is strictly below one. Thus the law is nonincreasing with exactly the adjacent equality stated, which is a descending shoulder, not a second local modal plateau. If \(\gamma>\Gamma_N\), then \(\{i\ge2:r_i>1}\) is a nonempty consecutive interval because the sequence \(G_i\) decreases and then increases. The \(r_0,r_1\) inequalities force a first local mode at index zero; the consecutive block of increasing edges produces exactly one further local modal plateau after a valley, at an index at least three. If \(\gamma=G_i\) at its right boundary, that upper mode is a two-point plateau; otherwise it is a singleton. Since the \(G_i\) are strictly increasing to the right of their unique minimum, no upper plateau can contain three points. Possible equality at the left boundary of the increasing block is merely a flat valley. No third mode is possible.

**Exact parity pairing and finite-size maximum.** Take \(\varepsilon\downarrow0\) in the *threshold formula*, not in the stationary law. Writing \(N=2m\) or \(N=2m+1\) gives, for every \(m\ge2\),
\[
 \Gamma_{2m}(\mu,0^+)=\Gamma_{2m+1}(\mu,0^+)=\mu F(m),\quad
 F(m)=\frac{2(2m-1)(m+2)}{m(m+1)}.
\]
A direct subtraction yields
\[
 F(m+1)-F(m)=\frac{2(4-m)}{m(m+1)(m+2)}.
\]
Consequently \(F\) increases through \(m=4\), ties between \(m=4\) and \(m=5\), and then decreases. The tied maximum is \(F(4)=F(5)=21/5\). Rewriting \(F(m)=4+2(m-2)/[m(m+1)]\) proves convergence to \(4\) from above. The separate case \(N=3\) gives the limit \(3\mu\), below that maximum. This completes the proof.

## Verification

The accompanying standalone `verify.py` works entirely with rational arithmetic and the actual birth and death rates above. It compares the analytic transition threshold with every finite edge threshold, checks detailed balance and each stationary master equation independently, classifies maximal constant local-modal plateaus (including exact threshold ties), and verifies the rare-importation parity identity and the intermediate-size maximum. Run `python verify.py` with standard Python 3; no external dependencies or stochastic approximations are needed. Exact finite tests are corroboration of the preceding proof, not a substitute for universal quantifiers.

## Relationship to prior work

Kiss, Iacopini, Simon and Georgiou (2023), especially their Eqs. (II.3)–(II.7), establish the complete-simplicial complex triadic infection mechanism and the unseeded finite-state master equation. Their bifurcation analysis addresses deterministic higher-order contagion and does not state this positive-importation finite-stationary mode threshold. Vezzani, Muñoz and Burioni (2022), Eqs. (2)–(3) and Sections III–IV, give the general birth–death stationary product and a different \(q\)-SIS choice in which both creation and annihilation require \(q\) infected agents; their exact product formula is credited as the standard starting point, not a new contribution. Their scaling and quasi-stationary results do not provide the discrete minimizer, parity-paired finite threshold, or nonmonotonic-size maximum here. Kiss, Bick and Simon (2024) analyze deterministic higher-order equilibrium bifurcations, including coupled populations, not finite seeded stationary modes. Claims are restricted to the stated scalar count chain and do not cover graph heterogeneity, quenched geometry or multiple simultaneous infections.

## Limitations

For \(\varepsilon=0\), state zero is absorbing and the unique finite stationary distribution is concentrated at zero; the displayed limits concern only the boundary of the *positive-importation modal threshold*. We require \(0<\varepsilon<\mu/N\) to ensure a strict zero-count modal peak. The theorem describes local modes, not the relative heights or weights of the two modes, metastable transition times, or a thermodynamic phase transition. A high-mode plateau may have two adjacent equal entries at isolated parameter values, so universal *strict* bimodality would be inaccurate. More general birth–death rates admit standard stationary product formulae, and independently published equivalent finite-mode classifications cannot be categorically excluded by targeted searching.

## References

1. I. Z. Kiss, I. Iacopini, P. L. Simon, N. Georgiou, *Insights from exact social contagion dynamics on networks with higher-order structures*, arXiv:2309.12752v1 (public 2023-09-22), https://arxiv.org/abs/2309.12752.
2. A. Vezzani, M. A. Muñoz, R. Burioni, *Anomalous finite-size scaling in higher-order processes with absorbing states*, arXiv:2210.03504v1 (public 2022-10-07), https://arxiv.org/abs/2210.03504.
3. I. Z. Kiss, C. Bick, P. L. Simon, *Decoding how higher-order network interactions shape complex contagion dynamics*, arXiv:2410.15330v1 (public 2024-10-20), https://arxiv.org/abs/2410.15330.
