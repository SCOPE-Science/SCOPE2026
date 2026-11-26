# Exact dynamical sectors and a frozen-density threshold in long-jump exclusion

## Finding

For a periodic exclusion process with jumps of a fixed length \(I\ge 2\) across entirely vacant intermediate sites, the Arrhenius-Gibbs stationary measure is generally not dynamically ergodic. This note classifies all irreducible sectors on the **cyclically marked-particle cover**, determines the exact current of each mobile sector, counts every frozen physical configuration, and derives a sharp freezing-entropy threshold.

Let \(L>I\ge2\), \(2\le N<L\), and \(V=L-N\). Write the \(N\) forward numbers of vacant sites between consecutively marked particles as \(h_i\ge0\) with \(\sum_i h_i=V\). Define
\[
h_i=a_i+I k_i,\quad 0\le a_i<I,\quad k_i\ge0,\quad K=\sum_{i=1}^N k_i=\frac{V-\sum_i a_i}{I},\quad d=\gcd(L,I).
\]
A right or left jump transfers one unit between neighboring \(k\)'s; all \(a_i\) remain fixed. Let \(x_1\in\mathbb Z/L\mathbb Z\) be the position of the first marked particle. For every admissible residue vector \(\mathbf a\) with \(K\ge1\), and every possible \(x_1\bmod d\), **there is exactly one irreducible class** containing all \(\binom{K+N-1}{N-1}\) compositions \(\mathbf k\) and all \(L/d\) permitted values of \(x_1\). For \(K=0\), each configuration is an absorbing singleton.

For any finite real headway potential \((J_g)_{g\ge1}\), set
\[
w_i(k)=\exp J_{1+a_i+Ik},\qquad Z_{\mathbf a}(K)=\sum_{\substack{k_i\ge0\\\sum_i k_i=K}}\prod_{i=1}^N w_i(k_i).
\]
The unique invariant law in a mobile class is proportional to \(\prod_i w_i(k_i)\), uniformly in the allowed marked-root positions. For positive right and left baseline rates \(r_\star,\ell_\star\), the **stationary signed current per physical bond** is
\[
\boxed{\mathcal J_{\mathbf a}=\frac{IN}{L}(r_\star-\ell_\star)\frac{Z_{\mathbf a}(K-1)}{Z_{\mathbf a}(K)}}\qquad(K\ge1),
\]
and zero for the frozen singleton classes. The zero-range product weights and unrestricted Gibbs invariance are prior work; the sector conditioning and complete classification here are the additional assertions.

In the physical (unmarked) \(N\)-particle ring the number of **frozen configurations** is exactly
\[
\boxed{F_{L,N,I}=\frac{L}{N}[z^{L-N}](1+z+\cdots+z^{I-1})^N.}
\]
Frozen configurations exist exactly when \(N\ge\lceil L/I\rceil\). At \(L=IN\) there are exactly \(I\) such configurations. For sequences with \(N/L\to\rho\in(1/I,1)\),
\[
\lim_{L\to\infty}\frac1L\log F_{L,N,I}=s_I(\rho)
=\rho\log f_I(z_\rho)-(1-\rho)\log z_\rho>0,
\]
where \(f_I(z)=\sum_{j=0}^{I-1}z^j\) and the unique \(z_\rho>0\) solves \(z_\rho f_I'(z_\rho)/f_I(z_\rho)=(1-\rho)/\rho\). This entropy is strictly below the binary configuration entropy \(H(\rho)=-\rho\log\rho-(1-\rho)\log(1-\rho)\). Hence a uniformly chosen canonical physical configuration is frozen with probability \(\exp\{-L[H(\rho)-s_I(\rho)]+o(L)\}\), even though frozen states are exponentially numerous.

For example, at \((L,N,I)=(12,8,2)\) there are exactly \(105\) frozen states among \(495\) physical configurations; simultaneously an active sector with all \(a_i=0\), \(K=2\), trivial potential, and \(r_\star-\ell_\star=1\) has current \(8/27\). The same particle density therefore supports both identically zero and strictly positive stationary transport, selected by initial preparation.

## Assumptions and scope

A finite periodic lattice has \(L\) distinct numbered sites, \(N\) exclusion particles, and a fixed hop length \(2\le I<L\). Every intermediate and destination site of a permitted hop is empty. The cyclic order of particles cannot change. The marked-particle cover tracks one physically distinguished particle \(x_1\); the remaining indices follow clockwise. Physical occupancy configurations arise after forgetting this mark. The distinction matters in class counting, but not in the frozen physical count.

The forward *vacancy* headway \(h_i\) is the number of empty sites before the next particle, so its physical separation is \(g_i=h_i+1\). A right hop by particle \(i\) is possible exactly for \(h_i\ge I\), and has rate \(r_\star\exp(J_{g_i-I}-J_{g_i})\); a left hop by particle \(i\) is possible for \(h_{i-1}\ge I\), at rate \(\ell_\star\exp(J_{g_{i-1}-I}-J_{g_{i-1}})\). Both baseline rates are strictly positive and all relevant potential values finite. The current counts net particle crossings of physical lattice bonds per unit time, including all \(I\) bonds traversed by each hop.

The thermodynamic frozen entropy is for a fixed integer \(I\), density strictly between \(1/I\) and \(1\), and a sequence of integer \((L,N)\) with \(N/L\to\rho\). The paper's Gibbs invariant law, general stationarity mechanism and thermodynamic ensemble current are prior results, not new claims.

## Proof

**1. Residues and exhaustive classes.** A right hop by particle \(i\) subtracts \(I\) from \(h_i\) and adds \(I\) to \(h_{i-1}\); a left hop reverses this. Thus every vacancy residue \(a_i=h_i\bmod I\) is constant. Fixing these residues fixes \(K\). For \(K\ge1\), the dynamics of \(\mathbf k\) is a nearest-neighbor zero-range movement of \(K\) indistinguishable tokens on a connected \(N\)-cycle with every nonempty donor active; hence all its compositions communicate. Tracking particle \(1\) shows each hop alters \(x_1\) either by \(0\) or by \(\pm I\), so \(x_1\bmod d\) is invariant. Move one available token successively once around the cycle in the same orientation. The token returns to its original site and every \(k_i\) is restored, while particle \(1\) has jumped once, translating \(x_1\) by \(I\). The subgroup generated by \(I\) in \(\mathbb Z/L\mathbb Z\) has exactly \(L/d\) elements. Combining such cycles with arbitrary token transfers proves both reachability and irreducibility within each specified residue/root class. If \(K=0\), no donor has \(k_i\ge1\), so every rate vanishes. This proves the classification and class sizes.

**2. Conditional stationarity.** Denote \(u_i(k)=w_i(k-1)/w_i(k)\) for \(k\ge1\), and \(u_i(0)=0\). For either orientation, an outgoing token transfer from donor \(i\) has rate equal to the corresponding baseline rate times \(u_i(k_i)\). Multiplying the state weight by that rate replaces \(w_i(k_i)\) with \(w_i(k_i-1)\). Its incoming counterpart from the adjacent donor, after reversing the predecessor move, produces the same weight with the same orientation rate. Summing around the cycle gives global balance separately for right and left transfers. This is the canonical zero-range balance mechanism; the allowed root phases all carry identical weight. Since the mobile class is finite and irreducible, its conditional product distribution is uniquely stationary.

**3. Finite-sector current.** For every index \(i\),
\[
\frac1{Z_{\mathbf a}(K)}\sum_{\sum k_j=K}\left(\prod_j w_j(k_j)\right)u_i(k_i)
=\frac{Z_{\mathbf a}(K-1)}{Z_{\mathbf a}(K)}.
\]
Indeed, after multiplying by \(u_i\), translate \(k_i\) downward by one; the resulting sum runs over all compositions of \(K-1\). Every jump traverses \(I\) bonds, so the spatial mean of signed bond current is \(I/L\) times the difference of total right and left jump rates. Stationary particle conservation implies that mean signed current across each individual physical bond is the same, even if a marked class is invariant only under translations by \(d\). Summing the identical donor averages gives the displayed \(IN/L\) formula.

**4. Frozen census and threshold.** A physical configuration is frozen if and only if every vacancy gap obeys \(0\le h_i\le I-1\): if one gap has \(h_i\ge I\), the particle immediately before it has a legal positive-rate right hop. Count marked configurations by a root site and a bounded composition: \(L[z^{L-N}]f_I(z)^N\). Every unmarked physical configuration has exactly \(N\) choices of the distinguished particle, giving the factor \(L/N\). A bounded composition exists iff \(0\le L-N\le N(I-1)\), equivalent to \(N\ge\lceil L/I\rceil\). Equality \(L=IN\) forces every \(h_i=I-1\), giving exactly \(I\) physical translations.

**5. Frozen entropy.** Put \(m_L=(L-N)/N\), which is eventually in \((0,I-1)\). Choose \(z_L>0\) so that \(p_{Lj}=z_L^j/f_I(z_L)\) has mean \(m_L\). The mean of this tilted law increases strictly from \(0\) to \(I-1\): its derivative with respect to \(\log z_L\) is the positive variance. Thus \(z_L\to z_\rho\), and all \(p_{Lj}\) stay bounded away from zero. For independent samples \(X_i\) from this law, the coefficient is
\[
[z^{L-N}] f_I(z)^N=f_I(z_L)^N z_L^{-(L-N)}\Pr\bigl(\textstyle\sum_i X_i=L-N\bigr).
\]
The logarithm of the last probability is \(O(\log N)\): it is at most zero, and one admissible multinomial type provides a lower bound. Round \(Np_{Lj}\) to integers \(n_j\) for \(j\ge2\), set \(n_1=L-N-\sum_{j\ge2}j n_j\), and set \(n_0=N-\sum_{j\ge1}n_j\). Then all \(n_j=Np_{Lj}+O(1)\) and are nonnegative for large \(N\). Stirling's formula gives \(\log((N!/\prod_j n_j!)\prod_j p_{Lj}^{n_j})=-O(\log N)\), since the empirical proportions differ from \(p_{Lj}\) by \(O(1/N)\) and the latter are bounded away from zero. This argument uses the tilt at the actual density, not a local estimate at the limiting mean with an uncontrolled deviation.

Taking logarithms and limits, including the subexponential factor \(L/N\), gives \(s_I(\rho)=\rho\,\mathrm{Ent}(p_\rho)>0\), where \(p_{\rho j}=z_\rho^j/f_I(z_\rho)\) and \(\mathrm{Ent}\) denotes Shannon entropy. The geometric law \(q_j=\rho(1-\rho)^j\) on \(j\ge0\) has the same mean. Because \(\log q_j\) is affine in \(j\), \(\mathrm{Ent}(q)-\mathrm{Ent}(p_\rho)=D(p_\rho\|q)>0\), with strictness since \(q\) has unbounded support. Hence \(s_I(\rho)<\rho\,\mathrm{Ent}(q)=H(\rho)\); dividing the frozen count by \(\binom LN\) gives the claimed exponential rate. At exact critical density (\(L=IN\)), the count is \(I\), so the entropy there is zero.

**6. Exact example.** For \((L,N,I)=(12,8,2)\), \(f_I(z)=1+z\), so \(F=(12/8)\binom84=105\). With all residues zero, \(K=2\), \(Z(2)=\binom97=36\), \(Z(1)=\binom87=8\), and current \((16/12)(8/36)=8/27\). Every absorbing state has zero current.

## Verification

A standalone, Python-standard-library checker `verify.py` exhaustively builds the directed communicating classes for small finite rings (\(4\le L\le11\), \(2\le N\le4\), \(N<L\), \(2\le I\le4\) with \(I<L\)). It compares their exact keys with the residue and root-phase classification and counts all frozen binary configurations against the exact coefficient formula. For classes of size at most 120, it checks exact-rational stationarity and sector current for a nonconstant weight \(w(g)=2\) when \(g=3\) and \(w(g)=1\) otherwise, with right and left prefactors \(2,1\). It also outputs exact larger-ring example counts. Run with `python3 verify.py`; no third-party package is needed. Finite checks illustrate, but do not replace, the arguments above for arbitrary ring size.

## Relationship to prior work

Nhung, Ngoc, and Thi (2026), *Invariant measures of exclusion processes with a look-ahead rule*, use the same fixed-length vacancy-clearance rule and Arrhenius rates, under restrictions on the potential. Their Theorem II.1 gives Gibbs stationarity through pairwise balance. Equation (10) gives the exact finite-ring current as a full canonical Gibbs expectation; Eq. (13) gives the thermodynamic current, and §III.4 of version 2 discusses exact finite-ring computation by convolution. These ensemble results do not distinguish the residue/root classes. The additional statements here are the exhaustive marked classification, the current conditioned on a single mobile class, and the frozen census and entropy. The zero-range canonical representation itself is prior. Belitsky, Ngoc and Schütz (2024/2025) analyze **single-site** jumps with long-range interactions, which lack the fixed-hop vacancy-residue obstruction. The one-way clearance model of Sun and Tan (2020), §2.2, has the same static criterion for an occupancy configuration to have no legal jumps, though its rates and dynamics differ. The novelty of the frozen result is not the clearance criterion itself. No assertion of global priority over unindexed earlier literature is made.

## Limitations

The communicating-class decomposition is stated on the marked-particle cover; unmarked classes may identify cyclically related marked sectors. The formula counts unmarked frozen states exactly but does not enumerate all unmarked mobile classes. The stated setting assumes strictly positive baselines in both directions. The signed current vanishes at equal baseline rates even inside an active class. The entropy is for fixed hop length and interior densities; the critical and empty/full boundary cases are separate. The analysis does not prove hydrodynamic limits or transient mixing times, and it does not claim a distinct Gibbs formula from the original paper.

## References

1. L. T. Nhung, N. P. N. Ngoc and H. A. Thi, *Invariant measures of exclusion processes with a look-ahead rule*, arXiv:2604.01796v2 (first submitted April 2, 2026). https://arxiv.org/html/2604.01796v2
2. V. Belitsky, N. P. N. Ngoc and G. M. Schütz, *Asymmetric exclusion process with long-range interactions*, arXiv:2409.05017v2. https://arxiv.org/html/2409.05017v2
3. Y. Sun and C. Tan, *On a class of new nonlocal traffic flow models with look-ahead rules*, Physica D 413 (2020), 132663. https://arxiv.org/abs/2001.10017
4. A. Sopasakis and M. A. Katsoulakis, *Stochastic modeling and simulation of traffic flow: Asymmetric single exclusion process with Arrhenius look-ahead dynamics*, SIAM J. Appl. Math. 66 (2006), 921–944. https://doi.org/10.1137/040617790
