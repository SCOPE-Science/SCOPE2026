# A sharp assortativity switch between epidemic burden and outbreak-seeding rankings

## Finding

Consider two age or demographic groups with competing susceptibility and infectivity advantages. In the balanced two-group susceptible–exposed–infectious–removed (SEIR) model specified below, increasing within-group assortativity causes **exactly one change** from disagreement to agreement between the rankings of (i) final attack fractions and (ii) single-seed major-outbreak probabilities in the early branching approximation, unless the susceptibility and infectivity advantages are equal, when disagreement persists throughout all nonsegregated contact configurations.

Define
\[
h=\frac{(U-1)(V+1)}{(U+1)(V-1)},\qquad \eta_*=\min\{h,h^{-1}\}.
\]
For \(U\ne V\), the sharp switch occurs at \(\eta_*\in(0,1)\), with contrary rankings below and concordant rankings above. At the switch exactly one measure ties. If \(U=V\), the two measures remain oppositely ranked for every \(\eta<1\). The threshold is independent of the common transmission scale, common recovery rate and incubation rates within the supercritical domain.

## Assumptions and scope

Let two groups have equal population sizes and unit per-capita contact rates. Their contact proportions are symmetric and balanced:
\[
P_\eta=\frac12\begin{pmatrix}1+\eta&1-\eta\\1-\eta&1+\eta\end{pmatrix},\quad 0\le\eta<1,
\qquad a=\frac{1+\eta}{2},\quad b=\frac{1-\eta}{2}.
\]
The transmission probability per contact from infectious group \(j\) to susceptible group \(i\) is \(q u_i v_j\), where \((u_1,u_2)=(U,1)\) and \((v_1,v_2)=(1,V)\), with \(U,V>1\) and \(0<q<1/(UV)\). Both groups have the same exponentially distributed infectious lifetime with rate \(\gamma>0\), while progression from the nonfatal exposed stage occurs at any rates \(\delta_1,\delta_2>0\). Set \(c=q/\gamma\ge1\). The finite-time epidemic starts from a vanishing but positive fraction of infectives in at least one group, and \(z_i\) denotes its macroscopic positive-outbreak final attack fraction as that seed tends to zero. The quantity \(t_i\) is the survival probability of the corresponding infinite-population multitype Markov branching approximation begun with one exposed or infectious group-\(i\) individual. Neither \(t_i\) nor the positive-outbreak branch is asserted to be the exact finite-population probability or final-size distribution.

The two positive matrices controlling the two outcomes are transposes:
\[
A=c\begin{pmatrix}Ua&UVb\\b&Va\end{pmatrix},\qquad
B=A^\mathsf T=c\begin{pmatrix}Ua&b\\UVb&Va\end{pmatrix}.
\]
Their spectral radii agree. Since each row sum of \(A\) exceeds one for \(c\ge1\), the Perron spectral radius exceeds one uniformly for \(0\le\eta<1\); hence both outcome vectors have a unique strictly positive solution. The individual incubation rates do not enter either fixed-point equation because exposed individuals have neither disease death nor competing removal.

## Proof

**1. Exact fixed-point equations.** Integrating the susceptible and recovered equations (equivalently the final-size relation) gives
\[
z=F(Az),\qquad F(x)=1-e^{-x},
\]
where \(F\) is applied componentwise. Conditioning a type-\(j\) infectious individual's exponentially distributed lifetime on its competing secondary-infection Poisson events gives
\[
t=G(Bt),\qquad G(x)=\frac{x}{1+x},
\]
componentwise. The latter is also obtained by subtracting each extinction probability from unity in the branching generating-function equations. The positive progression rates \(\delta_i\) cancel because every exposed individual eventually becomes infectious.

**2. A two-dimensional rank lemma.** Let \(M\) be an arbitrary strictly positive \(2\times2\) matrix, and \(f\) be either \(F\) or \(G\). Whenever \(\rho(M)>1\), the equation \(x=f(Mx)\) has exactly one strictly positive solution, and
\[
\operatorname{sgn}(x_1-x_2)=\operatorname{sgn}\big((M\mathbf1)_1-(M\mathbf1)_2\big).
\]
For existence, take the positive Perron eigenvector \(v\), choose \(\varepsilon>0\) small enough that \(f(M\varepsilon v)>\varepsilon v\), and iterate the monotone map below the supersolution \(\mathbf1\). For uniqueness, if two positive fixed points \(x,y\) exist, choose a maximal coordinate ratio \(r=\max_i x_i/y_i>1\); then \(x\le ry\) and strict subhomogeneity \(f(rs)<r f(s)\) for \(s>0\) contradicts equality in the maximal coordinate. Interchanging \(x,y\) rules out any distinct pair.

For the rank assertion, replace \(M\) by \(sM\) and vary \(s>1/\rho(M)\). The unique positive fixed point depends continuously on \(s\): its Jacobian \(\operatorname{diag}(f'(sMx))sM\) has spectral radius strictly below one because \(f'(y)y<f(y)\) at every \(y>0\), so the implicit-function theorem applies. As \(s\downarrow1/\rho(M)\), the positive fixed point tends to zero (there is no positive critical fixed point); after normalization its direction tends to the strictly positive Perron right eigenvector. In dimension two, the sign of the difference between the entries of that Perron vector equals the sign of the difference between the row sums of \(M\): writing the ratio of its entries in the positive-root quadratic and evaluating at ratio one gives this equivalence. Finally the sign cannot change at any \(s\) unless the positive fixed point has equal coordinates, which on substitution forces the two row sums of \(M\) to be equal. If the row sums are equal, the unique positive fixed point is symmetric. This proves the rank lemma in all cases.

**3. Two competing row-sum contrasts.** By direct algebra,
\[
(A\mathbf1)_1-(A\mathbf1)_2
=\frac{c}{2}\left[(U-1)(V+1)-\eta(U+1)(V-1)\right],
\]
whereas
\[
(B\mathbf1)_1-(B\mathbf1)_2
=\frac{c}{2}\left[-(U+1)(V-1)+\eta(U-1)(V+1)\right].
\]
The first contrast vanishes at \(\eta=h\); the second at \(\eta=1/h\). The two thresholds are reciprocal. If \(U<V\), then \(0<h<1\), so only the burden contrast changes sign for \(\eta\in[0,1)\); the seeding contrast remains strictly negative. If \(U>V\), then \(h>1\), so only the seeding contrast changes sign, while the burden contrast remains strictly positive. When \(U=V\), both equalities would require the excluded full-segregation point \(\eta=1\), and the contrasts have opposite signs throughout the permitted interval. The rank lemma gives every stated strict inequality and tie.

**4. Exact instance.** With \(U=2\), \(V=3\), \(q=1/100\), and \(\gamma=1/100\), the threshold is exactly \(\eta_*=2/3\); any positive \(\delta_1,\delta_2\) are permitted. At \(\eta=1/2\), the class with greater susceptibility has both the higher final attack fraction and the **lower** probability of initiating a large outbreak. At \(\eta=3/4\), group two has the larger quantity in both comparisons. At \(\eta=2/3\) the two final attack fractions coincide while the two seeding probabilities differ strictly. The contact transmission probabilities are all below one (indeed at most \(6/100\)).

## Verification

The embedded standalone script `verify.py` performs exact symbolic checks of both row-sum contrasts, reciprocal threshold algebra, balanced contact normalization, and the rational example. It independently solves the two nonlinear fixed-point systems for samples of parameters and checks the classifications. This finite numerical checking is supplementary: the infinite-parameter assertion follows from the rank lemma and exact algebra above. Execute `python verify.py` in a Python environment with SymPy and NumPy.

## Relationship to prior work

Zhang, Wu, Yang, Xiao and Bai (2026) derive the age-structured final-size and branching-extinction systems, then compare group risk rankings across empirical contact networks. Their calculations exhibit disagreement between high-burden and high-outbreak-trigger groups, and discuss varying mixing patterns as a way of investigating its mechanism. The present result gives a **complete exact two-group balanced-contact classification**, with a unique reciprocal assortativity boundary, within a natural susceptibility–infectivity opposition. It does not assert novelty of the underlying fixed-point systems or the classical multitype epidemic theorem.

Magal, Seydi and Webb (2016) study final sizes in a general two-group SIR system, without providing a joint branching-survival and final-burden assortativity crossover in the inspected material. El Khalifi (2026) studies dependence of aggregate outcomes on the joint trait law under homogeneous well-mixed contacts; this does not vary a within-group contact assortativity parameter. Ball and Critcher (2026) analyze multitype household epidemics with proportionate global mixing and other local contacts; their framework is structurally different from the symmetric two-group balanced contact system studied here. More general fixed-point theory underlies the proof; no broad claim of absolute historical priority is made.

## Limitations

The theorem requires two equally sized groups, equal contact rates, common infectious recovery, and the specific symmetric assortative mixing family. It is not a theorem about larger numbers of groups, unequal demographic sizes, frequency-dependent removal, or empirically observed data. The positive-outbreak deterministic branch and early-branching survival probabilities describe different limiting objects, and no finite-population equality is asserted. Near-critical and full-segregation boundaries are not covered by the interior strict-ranking conclusions. The result contains no causal intervention analysis or data-fitting claim. Absolute historical priority has not been independently established.

## References

1. S. Zhang, M. Wu, J. Yang, J. Xiao, and F. Bai, *Indication of demographic and epidemiological data on early-stage risks and long-term epidemic burden*, arXiv:2611.19854v1 (2026), https://arxiv.org/abs/2611.19854v1 .
2. P. Magal, O. Seydi, and G. F. Webb, *Final Size of an Epidemic for a Two-Group SIR Model*, SIAM Journal on Applied Mathematics 76 (2016), 2042–2059, https://doi.org/10.1137/16M1065392 .
3. M. El Khalifi, *Dependence Structure and Epidemic Outcomes in Heterogeneous SIR Models*, arXiv:2601.01549v1 (2026), https://arxiv.org/abs/2601.01549 .
4. F. Ball and L. Critcher, *Multitype SIR epidemics among a population partitioned into households with proportionate global mixing*, Journal of Mathematical Biology 92, 77 (2026), https://doi.org/10.1007/s00285-026-02359-5 .
