# A sharp six-vertex onset and an infinite amplification family for nonmonotone neutral fixation on trees

## Finding

Consider a finite connected simple unweighted tree under independently mixed neutral birth–death (Bd) and death–Birth (dB) replacement, with probability \(\delta\in[0,1]\) of a dB update at each step. The fixation probability of a mutant seeded at any specified vertex is monotone or constant in \(\delta\) whenever the tree has at most five vertices. There is a six-vertex tree and seed for which that probability has a unique strict maximum in \((0,1)\); thus six is the sharp minimum order for failure of monotonicity on trees.

Specifically, let \(D_{1,3}\) have adjacent hubs, of degrees two and four, with one and three pendant leaves respectively. Start with the sole leaf adjacent to the degree-two hub mutant and every other vertex resident. Its fixation probability is
\[
P_3(\delta)=\frac{(2-\delta)^2(1+3\delta)}{19+35\delta-8\delta^2-6\delta^3}.
\]
It has exactly one strict interior maximum, at the unique root \(\delta_*=0.033681049923\ldots\) in \((0,1)\) of
\[
15\delta^3-21\delta^2-29\delta+1=0.
\]
In particular \(P_3(\delta_*)=0.211065107458\ldots\), exceeding \(P_3(0)=4/19\), whereas \(P_3(1)=1/10\).

Moreover this is not an isolated small-graph accident. On every double star \(D_{1,m}\), with one leaf beside its degree-two hub and \(m\ge3\) leaves beside its degree-\(m+1\) hub, the same starting leaf has positive derivative at \(\delta=0\) and negative derivative at \(\delta=1\). An interior optimum therefore exists for every \(m\ge3\). Its fixation probability \(P_m\) satisfies
\[
\lim_{m\to\infty}mP_m(0)=1,\qquad
\lim_{m\to\infty}mP_m(1)=\frac12,\qquad
\lim_{m\to\infty}mP_m(m^{-1/2})=2.
\]
Consequently an interior mixture can asymptotically double this site's fixation probability relative to the better pure update rule. This last statement is a lower bound on the achievable improvement, not an assertion that the global maximizing improvement is exactly two.

## Assumptions and scope

Fix a tree \(T=(V,E)\) on \(N\ge2\) vertices, with positive integer degrees \(d_v\). At each discrete step, with probability \(1-\delta\), choose a parent uniformly from \(V\), then replace a uniformly chosen neighbor (Bd); with probability \(\delta\), choose the vertex to die uniformly, then choose its replacing parent uniformly among neighbors (dB). All individual fitnesses are one, mutation after initialization is absent, and the initial state contains one mutant at a specified vertex. The absorbing states are all-mutant and all-resident. Fixation means eventual absorption in the all-mutant state. No self-loops or weights are assumed. For \(D_{a,b}\), the two adjacent hubs have respectively \(a\) and \(b\) pendant neighbors, where \(a,b\ge1\).

## Proof

**1. Reproductive weights on trees.** For adjacent parent \(u\) and replaced vertex \(v\), the exact ordered copying probability is
\[
q_{u\to v}(\delta)=\frac1N\left(\frac{1-\delta}{d_u}+\frac{\delta}{d_v}\right)>0.
\]
Choose positive vertex weights \(w_v\), uniquely up to common scale, by setting a root weight and propagating along each edge with
\[
w_vq_{u\to v}=w_uq_{v\to u}.
\]
Because \(T\) has no cycles, these edge equations are consistent; because every edge has positive transition probability, all weights are positive. For a mutant indicator configuration \(X=(X_v)\), the process \(M(X)=\sum_{v}w_vX_v\) has conditional drift
\[
\mathbb E[M(X_{t+1})-M(X_t)\mid X_t=X]
=\sum_{\{u,v\}\in E}(X_u-X_v)(w_vq_{u\to v}-w_uq_{v\to u})=0.
\]
The finite connected copying process reaches consensus almost surely: from every nonabsorbing state a finite, positive-probability sequence of copying events propagates either present type across the tree, and the finite-state Markov chain therefore has no other closed communicating class. Bounded-martingale optional stopping at consensus gives fixation from \(v\) equal to \(w_v/\sum_u w_u\), including both pure-rule endpoints.

**2. An explicit double-star formula.** Put \(p=a+1\), \(q=b+1\), and define
\[
r_k(\delta)=\frac{1-\delta+k\delta}{k(1-\delta)+\delta},\qquad
h_{p,q}(\delta)=\frac{p(1-\delta)+q\delta}{q(1-\delta)+p\delta}.
\]
Use weight 1 for each of the \(a\) left leaves; the adjacent degree-\(p\) hub gets weight \(r_p\); the degree-\(q\) hub gets weight \(r_ph_{p,q}\); and each of its \(b\) leaves gets weight \(r_ph_{p,q}/r_q\). These weights satisfy each edge balance equation above by direct substitution. Thus the fixation probability at a left leaf is exactly
\[
P_{a,b}(\delta)=\left(a+r_p+r_ph_{p,q}+b\,r_ph_{p,q}/r_q\right)^{-1}.
\]
Substitution \(a=1,b=3\) and simplification gives the displayed formula for \(P_3\). Its derivative is
\[
P_3'(\delta)=\frac{6(2-\delta)(15\delta^3-21\delta^2-29\delta+1)}{(19+35\delta-8\delta^2-6\delta^3)^2}.
\]
The cubic changes sign exactly once: its derivative \(45\delta^2-42\delta-29\) is negative on \([0,1]\), and its endpoint values are 1 and \(-34\). All other derivative factors are positive for \(0\le\delta\le1\). Hence the specified optimum is unique and strict.

**3. Minimality.** Every tree with at most five vertices is either bidegreed (at most two distinct vertex degrees), or is the unique five-vertex fork \(D_{1,2}\) with degree values 1, 2, 3. In the bidegreed cases, the neutral single-site fixation probabilities are constant or monotone for every mixture by the established bidegreed theorem of Brewster, Huang, Mitzenmacher and Nowak [1, Thm. 3.4]. For the fork, substituting \(a=1,b=2\) in the preceding exact expression gives all four distinct vertex-orbit probabilities. Their derivatives, in order left leaf, left hub, right hub, right leaf, have a common positive squared denominator \((2\delta^3+5\delta^2-32\delta-23)^2\), with numerators
\[
\begin{aligned}
N_1&=-28\delta^4+156\delta^3-79\delta^2-354\delta-31,\\
N_2&=16\delta^4-96\delta^3+16\delta^2+168\delta+88,\\
N_3&=4\delta^4+156\delta^3+409\delta^2+342\delta+97,\\
N_4&=4\delta^4-108\delta^3-173\delta^2-78\delta-77.
\end{aligned}
\]
Their signs on \([0,1]\) can be certified without graph enumeration: set \(t=\delta/(1-\delta)\), for \(0\le\delta<1\). The coefficients from highest to lowest power of the polynomial \((1+t)^4N_i(t/(1+t))\) are respectively
\[
\begin{aligned}
&(-336,-1188,-1327,-478,-31),\\
&(192,792,1048,520,88),\\
&(1008,2388,2017,730,97),\\
&(-432,-996,-869,-386,-77).
\end{aligned}
\]
Each has a fixed strict sign for all \(t\ge0\); the signs persist at \(\delta=1\) by continuity. Therefore none of the five-or-fewer-vertex trees has a nonmonotone single-site fixation probability. Combining this with \(D_{1,3}\) establishes sharpness.

**4. Infinite family and scale.** The general formula in step 2 at \(a=1,b=m\) has exact boundary values and derivatives
\[
\begin{aligned}
P_m(0)&=\frac{2(m+1)}{2m^2+5m+5}, &
P_m(1)&=\frac1{2(m+2)},\\
P_m'(0)&=\frac{2m^4-7m^2-16m-3}{(2m^2+5m+5)^2},&
P_m'(1)&=-\frac{7m^2+11m+6}{8(m+1)(m+2)^2}.
\end{aligned}
\]
The numerator in \(P_m'(0)\) is 48 at \(m=3\) and strictly increases thereafter (its derivative in real \(m\) is \(8m^3-14m-16>0\) for \(m\ge3\)). Thus each \(m\ge3\) has an interior improvement over both endpoints. Finally substitute \(\delta=m^{-1/2}\) into the same rational expression and divide numerator and denominator by their leading powers of \(m\); this gives \(mP_m(m^{-1/2})\to2\). The two pure-rule limits follow directly from the displayed boundary formulas. Since \(P_m(0)>P_m(1)\) for every \(m\ge1\), the better pure rule is always Bd for this seed, and the attained improvement approaches a factor of two.

## Verification

The standalone Python 3 / SymPy script `verify.py` checks every nonabsorbing mutant set's exact martingale drift and all dual vertex-balance identities at four mixtures for each of four double stars, including the five-vertex fork and six-vertex witness. It also checks the complete fork derivative-sign coefficient certificates, the six-vertex rational formula and derivative, all family endpoint identities, and the three asserted asymptotic limits. Run `python verify.py` with SymPy installed. The script reports `PASS 1514 exact one-step identities and symbolic checks` on successful completion. The infinite cardinality statements are established by the analytic arguments above, not by those finite checks.

## Relationship to prior work

Brewster, Huang, Mitzenmacher and Nowak [1] introduce and systematically study mixed updating on arbitrary graphs, prove bidegreed monotonicity (their Theorem 3.4), and show that nonmonotonic fixation behavior can occur. Their discussion explicitly poses classification of graphs with monotone fixation responses; the particular tree-size threshold, the four-orbit five-vertex certificate, and the \(D_{1,m}\) family amplification statement above are not among the results inspected in their main neutral-evolution section or appendix on bidegreed graphs. Their separate earlier conference preprint [2] is credited for the model and prior results. Zukewich and collaborators [3] previously formulated the Bd/dB mixture in evolutionary games on regular populations; it is not a classification of neutral location-specific probabilities on finite irregular trees. An existing general exact tree-weight formula or unindexed derived classification might imply portions of this claim; absence from the sources inspected is not proof of global priority.

## Limitations

Only neutral fitness, discrete-time update mixing, loopless unweighted trees, and single-site initial mutants are covered. The sharp claim concerns the smallest *tree* order, not the smallest graph order, and neither uniqueness among all six-vertex trees nor global uniqueness of optima for every \(D_{1,m}\) is claimed. The limit two is an achievable asymptotic improvement, not a proved global optimum across mixtures or graphs. Historical-priority assessment is limited to the examined sources and database searches. An independent mathematical audit remains outstanding.

## References

[1] D. A. Brewster, Y. Huang, M. Mitzenmacher, M. A. Nowak, *Mixed updating in structured populations*, arXiv:2512.11164, first publicly submitted December 11, 2025, https://arxiv.org/abs/2512.11164 ; relevant main section 3.1, Theorems 3.4–3.5, Appendix E.1.

[2] Same authors, *The Mixed Birth-death/death-Birth Moran Process*, arXiv:2511.18252, first publicly submitted November 23, 2025, https://arxiv.org/abs/2511.18252 . Earlier conference version, not to be conflated with revisions of [1].

[3] J. Zukewich, V. Kurella, M. Doebeli, C. Hauert, *Consolidating Birth-Death and Death-Birth Processes in Structured Populations*, PLOS ONE 8(1):e54639 (2013), https://doi.org/10.1371/journal.pone.0054639 .
