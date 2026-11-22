# A Poisson founding-quorum sex-allocation law with a monotone budget response

## Finding
Fix an integer \(r\ge1\) and a total expected number \(n>0\) of surviving founders. Assign independently Poisson-distributed male and female founding counts \(M\sim\operatorname{Pois}(u)\) and \(F\sim\operatorname{Pois}(n-u)\). A quorum means at least one male and at least \(r\) females are present. A single male can fertilize all females, but this criterion requires at least \(r\) available females. The success probability is
\[
P_{n,r}(u)=(1-e^{-u})\left(1-e^{-(n-u)}\sum_{j=0}^{r-1}\frac{(n-u)^j}{j!}\right),\qquad 0\le u\le n.
\]

**Theorem (complete optimum and comparative statics).** Define, for \(y>0\),
\[
B_r(y)=\frac{(r-1)!}{y^{r-1}}\left(e^y-\sum_{j=0}^{r-2}\frac{y^j}{j!}\right),
\qquad \phi_r(y)=\log B_r(y),
\]
where an empty sum is zero and both functions are extended continuously to \(y=0\) with \(B_r(0)=1\). For every \(n>0\) and every integer \(r\ge1\), the **unique global maximum** of \(P_{n,r}\) is attained at \(u_*=\phi_r(y_*)\), where \(y_*\) is the **unique positive solution** of
\[
y_*+\phi_r(y_*)=n.
\]
For \(r=1\), the optimal male share is exactly \(u_*/n=1/2\). For each fixed \(r\ge2\), the optimal male share is **strictly increasing** with total expected founder count \(n\), lies strictly between \(1/(r+1)\) and \(1/2\), and approaches these two bounds respectively as \(n\downarrow0\) and \(n\to\infty\). For fixed \(n>0\), the optimum male share strictly **decreases** as the required female quorum \(r\) increases.

For each fixed integer \(r\ge2\), the sharp small- and large-budget expansions are
\[
\frac{u_*}{n}=\frac1{r+1}+\frac{r(r-1)}{2(r+1)^4}\,n+O_r(n^2),\qquad n\downarrow0,
\]
\[
u_*=\frac n2-\frac{r-1}{2}\log(n/2)+\frac12\log((r-1)!)+o_r(1),\qquad n\to\infty.
\]
For every fixed \(r\ge1\), the optimized quorum failure probability satisfies
\[
1-P_{n,r}(u_*)\sim \frac{2e^{-n/2}(n/2)^{(r-1)/2}}{\sqrt{(r-1)!}},\qquad n\to\infty.
\]
The small-budget leading success probability, for every fixed \(r\ge1\), is
\[
P_{n,r}(u_*)\sim\frac{r^r}{r!(r+1)^{r+1}}n^{r+1},\qquad n\downarrow0.
\]
In particular the optimum is biased toward females for any finite budget as soon as at least two females are essential, but its optimal male share strictly grows toward parity as budget grows.

## Assumptions and scope
The expected total number of founding animals is \(n\), not an exact integer count. A controllable fraction \(u/n\in[0,1]\) of the independently surviving founder-arrival intensity is allocated to males and the remaining fraction to females; independent Poisson thinning then yields the stated counts. It is assumed that founders are exchangeable within sex, mixing is complete, no mate-search or male-capacity limits apply, and success means only that the stated initial quorum exists. This is neither an ecological persistence probability nor a prediction of the evolutionarily stable sex ratio. The female threshold \(r\) is a biologically specified integer, not a fitted continuous parameter. All endpoints, including \(u=0\) and \(u=n\), are included. Theorems are exact for arbitrary real \(n>0\) and integer \(r\ge1\), with asymptotics at fixed \(r\).

## Proof
**Step 1: Exact stationarity equation.** Put \(y=n-u\), \(Q_r(y)=\Pr\{\operatorname{Pois}(y)\ge r\}\). For \(y>0\), direct differentiation gives
\[
Q'_r(y)=e^{-y}\frac{y^{r-1}}{(r-1)!}>0,
\qquad \frac{Q_r(y)}{Q'_r(y)}=B_r(y)-1.
\]
For \(u,y>0\), the derivative of log success is
\[
\frac{d}{du}\log P_{n,r}(u)
=\frac{1}{e^u-1}-\frac{Q'_r(y)}{Q_r(y)}
=\frac1{e^u-1}-\frac1{B_r(y)-1}.
\]
Thus its sign equals the sign of \(\phi_r(n-u)-u\). In particular a stationary point satisfies \(u=\phi_r(y)\) and hence \(n=y+\phi_r(y)\).

**Step 2: A probability representation and global uniqueness.** The absolutely convergent series for the exponential gives
\[
B_r(y)=\sum_{k=0}^{\infty}\frac{(r-1)!}{(r-1+k)!}y^k.
\]
For \(r=1\), this equals \(e^y\). For \(r\ge2\), the beta-integral identity gives
\[
B_r(y)=(r-1)\int_0^1e^{yv}(1-v)^{r-2}\,dv
=\mathbb E e^{yV_r},\qquad V_r\sim\operatorname{Beta}(1,r-1).
\]
Consequently \(\phi'_r(y)=\mathbb E_y V_r>0\) and, for \(r\ge2\),
\[
\phi''_r(y)=\operatorname{Var}_y(V_r)>0,
\qquad 0<\phi'_r(y)<1.
\]
The subscript denotes the strictly positive exponential tilt. For \(r=1\), \(\phi_1(y)=y\). Therefore \(G_r(y)=y+\phi_r(y)\) is strictly increasing from zero to infinity. The equation \(G_r(y)=n\) has a unique solution \(y_*\in(0,n)\), and \(u_*=n-y_*=\phi_r(y_*)\in(0,n)\). As \(u\) increases, \(\phi_r(n-u)-u\) strictly decreases from a positive to a negative value, so \(P_{n,r}\) strictly increases then decreases. At either boundary it is zero; its unique stationary point is the unique global maximizer.

**Step 3: Budget monotonicity and sharp bounds.** At zero, \(\phi'_r(0)=\mathbb EV_r=1/r\), with \(\phi_1'(0)=1\). For \(r\ge2\), strict convexity and \(0<\phi'_r(y)<1\) imply
\[
\frac yr<\phi_r(y)<y\quad(y>0),\qquad
\frac{d}{dy}\frac{\phi_r(y)}y>0.
\]
Since \(n=G_r(y)\), increasing \(n\) strictly increases \(y\), and
\[
\frac{u_*}{n}=\frac{\phi_r(y)}{y+\phi_r(y)}
\]
is strictly increasing from \(1/(r+1)\) and remains less than \(1/2\). The upper limit follows by bounding \(\phi'_r(y)\) away from \(1\) on any subinterval \([v_0,1]\) of positive beta measure: exponential tilting concentrates \(V_r\) arbitrarily close to \(1\) as \(y\to\infty\), so \(\phi'_r(y)\to1\). Cesàro averaging then gives \(\phi_r(y)/y\to1\). For \(r=1\), \(\phi_1(y)=y\) and parity is exact.

**Step 4: Quorum monotonicity.** For \(r\ge2\), the beta variable \(V_r\) has tail \(\Pr(V_r>v)=(1-v)^{r-1}\), \(0<v<1\). Increasing \(r\) strictly decreases this tail. Hence for each \(y>0\), \(B_{r+1}(y)<B_r(y)\) and \(\phi_{r+1}(y)<\phi_r(y)\). Because the unique root solves \(y+\phi_r(y)=n\), the root \(y_*\) strictly increases with \(r\), and the optimal male mean \(u_*=n-y_*\) strictly decreases. The same comparison at \(r=1\) follows because \(B_1(y)=e^y>B_2(y)\).

**Step 5: Asymptotics.** For fixed \(r\ge2\), the log-MGF Taylor expansion at zero is
\[
\phi_r(y)=\frac yr+\frac{r-1}{2r^2(r+1)}y^2+O_r(y^3).
\]
Solving \(n=y+\phi_r(y)\) by substitution gives the displayed small-budget male-share expansion. The leading success expression uses \(1-e^{-u}\sim u\), \(Q_r(y)\sim y^r/r!\), \(u\sim n/(r+1)\), and \(y\sim rn/(r+1)\).

At large \(y\), the finite sum in the definition of \(B_r\) is negligible relative to \(e^y\), so
\[
\phi_r(y)=y-(r-1)\log y+\log((r-1)!)+o_r(1).
\]
The stationarity equation implies \(y=n/2+O_r(\log n)\) and then yields the displayed additive asymptotic for \(u\). Finally, from
\[
1-P_{n,r}(u)=e^{-u}+e^{-y}\sum_{j=0}^{r-1}\frac{y^j}{j!}
-e^{-u-y}\sum_{j=0}^{r-1}\frac{y^j}{j!},
\]
the two leading terms have the same asymptotic magnitude at the optimum, each equivalent to \(e^{-n/2}(n/2)^{(r-1)/2}/\sqrt{(r-1)!}\); the product correction is negligible. For \(r=1\), \(u_*=n/2\) and this expression follows exactly from \(P=(1-e^{-n/2})^2\). This completes the proof.

## Verification
The included standalone standard-library script `verify_founder_quorum.py` evaluates the positive-series beta MGF, solves the unique stationary equation numerically, checks direct Poisson-tail probabilities against a hundred-point grid, tests monotonicity in expected budget and female quorum, and compares both asymptotic laws. It passed **13,569 diagnostic assertions**. For \(n=4\) and \(r=2\), it obtains \(u_*=1.498850985544\), male share \(0.374712746386\), and quorum probability \(0.553677309441\), versus \(0.513605783720\) at a balanced sex ratio. The diagnostics are finite and do not prove the universal statements; Steps 1–5 are the proofs. Run: `python3 verify_founder_quorum.py` (no external packages).

## Relationship to prior work
Bessa-Gomes, Legendre and Clobert (2004) analyze the effect of mating system and stochastic fixed-size sex ratios on Allee effects and extinction risk. Their fixed-size binomial expectations and the minimum mating function are distinct from the Poisson founding-quorum event optimized here. Their 2010 follow-up examines alternative mating functions, including the minimum of female availability and male mating capacity, and how these choices affect extinction; it does not optimize the probability of attaining a prescribed female quorum under a fixed Poisson founder budget. Schneider and collaborators (2012) consider stochastic sex determination and small-population extinction, not the present intensity-allocation problem. Duncan and collaborators (2014) study founding population size and establishment under independent demographic and environmental effects; the quorum threshold and its sex-allocation law are additional assumptions here.

A related finite-founder theorem, *Finite polygynous founder groups: a sharp sex-allocation tradeoff and logarithmic male reserves*, optimizes expected numbers of reproductive females for fixed binomial group size and finite male service capacity, and separately optimizes the probability of any mating. Its objective, parameterization, and implications do not establish this Poisson threshold-quorum law or the monotone budget-dependent male fraction. Derman, Lieberman and Ross (1974) study allocation to reliability systems with homogeneous component success functions and \(k\)-out-of-\(n\) structure. This is a plausible broader reduction to consider, but their accessible abstract's shared component-response assumption differs from two components with respective Poisson threshold responses \(Q_1\) and \(Q_r\). The full article could not be read here, so an unrecognized general heterogeneous-components theorem remains a risk. The beta MGF representation is a technique for the precise new objective, not evidence that the underlying probability model or Poisson thinning is new. All claims of originality are limited to the specified complete optimization, comparative statics and asymptotics, subject to the residual literature risks recorded in the accompanying review.

## Limitations
This is an initial-feasibility, one-generation calculation with independent sex-specific Poisson counts, complete mixing and unlimited male mating capacity. No immigration dynamics, age structure, correlated survival, sex-specific cost, density feedback or differential offspring fertility is modeled. The threshold \(r\) must be motivated by the organism's founding social or breeding requirements; its numerical choice cannot be optimized by this theorem. Positive quorum probability is not long-term establishment probability, and maximizing it is not a prescription for conservation releases without biological calibration. Approximation errors in observed sex ratios or founder intensities are not bounded here. A plausible broader reliability-allocation theorem might contain an equivalent optimization as a special case; no claim of exhaustive historical priority is made.

## References
1. C. Bessa-Gomes, S. Legendre, and J. Clobert (2004), “Allee effects, mating systems and the extinction risk in populations with two sexes,” *Ecology Letters* 7, 802–812. DOI: 10.1111/j.1461-0248.2004.00632.x. First online 2004-07-28. Open PDF: https://www.bio.ens.psl.eu/~legendre/biblio/Bessa-GomesLegendreClobert_AlleeEffects%26ExtinctionRisk_EcologyLetters_2004.pdf.
2. C. Bessa-Gomes, S. Legendre, and J. Clobert (2010), “Discrete two-sex models of population dynamics: On modelling the mating function,” *Acta Oecologica* 36, 439–445. DOI: 10.1016/j.actao.2010.02.010. First online 2010-05-26. Open PDF: https://www.bio.ens.psl.eu/~legendre/biblio/Bessa-GomesLegendreClobert_DiscreteTwoSexModels_ActaOecologica_2010.pdf.
3. Schneider and collaborators (2012), “Robustness Against Extinction by Stochastic Sex Determination in Small Populations,” arXiv:1204.4920, first posted 2012-04-22. https://arxiv.org/abs/1204.4920.
4. Duncan and collaborators (2014), “Quantifying invasion risk: relationship between establishment probability and founding population size,” *Methods in Ecology and Evolution*. DOI: 10.1111/2041-210X.12288. First online 2014-10-23.
5. Shyu and Caswell (2016), “A demographic model for sex ratio evolution and the effects of sex-biased offspring costs,” *Ecology and Evolution*. DOI: 10.1002/ece3.1902. First online 2016-02-09.
6. C. Derman, G. J. Lieberman, and S. M. Ross (1974), “Optimal Allocations in the Construction of k-Out-of-n Reliability Systems,” *Management Science* 21, 241–250. DOI: 10.1287/mnsc.21.3.241. First available online record 1974-11-01; full paper was not accessible in the attempted routes.
