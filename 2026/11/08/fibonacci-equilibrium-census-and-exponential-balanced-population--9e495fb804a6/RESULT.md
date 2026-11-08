# Fibonacci equilibrium census and exponential balanced-population rarity in diversity-seeking cycle games

## Finding

Consider a simple cycle \(C_N\) with \(N\ge4\), exactly one vacant vertex, and \(r\ge1\) distinct red and \(b\ge1\) distinct blue strategic agents, where \(r+b=N-1\). Every agent's utility is the fraction of her *occupied* neighbors with the opposite color; a move consists of jumping to the currently vacant vertex. An assignment is a pure Nash equilibrium if no single agent improves her utility by that move.

Let \(E_{r,b}\) count equilibrium red/blue words for a **fixed vacancy** with agents of the same color temporarily indistinguishable. Define \(\binom{p}{q}=0\) whenever \(p<0\) or \(q\notin\{0,\ldots,p\}\). Then the exact census is

\[
E_{r,b}=\binom{r-1}{b}+\binom{b-1}{r}
+2\sum_{h\ge0}\binom{h}{r-h-1}\binom{h}{b-h-1}.
\]

Only finitely many terms are nonzero. The total number of equilibria for distinct, labeled agents, with any vertex eligible to be vacant, is

\[
N\,r!\,b!\,E_{r,b}.
\]

There is at least one equilibrium for every positive composition \((r,b)\). For fixed \(N\), when summing type words over all \(2^{N-1}\) red/blue words (also allowing the two monochromatic words), the number of equilibrium words at any fixed vacancy is

\[
H_n=F_{n+2}+\epsilon_n,\quad n=N-1,\qquad
\epsilon_n=\begin{cases}-1,&n\equiv0\pmod3,\\0,&n\equiv1\pmod3,\\1,&n\equiv2\pmod3,\end{cases}
\]

where \(F_j\) is the Fibonacci sequence \(F_0=0,F_1=1\). The total restricted to profiles containing both colors is \(H_n-2\).

For balanced populations \(r=b=m\ge2\), both vacancy-neighbor colors must differ in every equilibrium, and

\[
E_{m,m}=2\sum_{h\ge0}\binom{h}{m-h-1}^{\!2}.
\]

Thus among uniformly chosen balanced red/blue type words, the equilibrium proportion has the **exact exponential rate**

\[
\lim_{m\to\infty}\left(\frac{E_{m,m}}{\binom{2m}{m}}\right)^{1/m}
=\frac{\varphi^2}{4}=\frac{3+\sqrt5}{8}<1,
\qquad \varphi=\frac{1+\sqrt5}{2}.
\]

For example, a nine-vertex cycle with four red agents, four blue agents and one vacancy has exactly \(10\) equilibrium type words for each fixed vacancy, versus \(\binom84=70\) possible type words.

## Assumptions and scope

All vertices and all agents are labeled. There is exactly one vacancy, no stubborn agents, and exactly two types with positive population sizes. The underlying graph is a simple cycle, not a path, and neighborhood fractions are computed after removing empty neighbors. Only *strictly* improving unilateral jumps are deviations; ties do not disqualify equilibria. This is the diversity-seeking **fraction** utility of Narayanan, Sabbagh and Voudouris [1], not the variety-count utility of [2] or similarity-seeking utility of [3].

Write the occupied cycle, beginning just clockwise of the fixed vacant vertex, as a binary word \(c_1\cdots c_n\) with \(n=N-1\ge3\). A run is a maximal consecutive constant-color subword. The fixed-vacancy census counts such words, not their cyclic rotations. Every one of the \(N\) possible vacancy positions has the same number of words. Independently permuting labels within each color gives the factor \(r!b!\).

## Proof

**1. Exact local Nash test.** Suppose the two occupied neighbors of the vacancy have colors \(c_1,c_n\). An interior agent \(c_i\), for \(2\le i\le n-1\), has two occupied neighbors. Moving that agent to the vacancy leaves both \(c_1\) and \(c_n\) occupied, hence the post-move utility is

\[
\frac{\mathbf1\{c_i\ne c_1\}+\mathbf1\{c_i\ne c_n\}}2.
\]

A boundary agent \(c_1\) or \(c_n\), however, vacates a vertex adjacent to the destination. The new utility is consequently \(\mathbf1\{c_1\ne c_n\}\), not a two-neighbor average. Before moving, the boundary agent's utility is \(\mathbf1\{c_1\ne c_2\}\) or \(\mathbf1\{c_n\ne c_{n-1}\}\), respectively.

If \(c_1=c_n=a\), the boundary agents have zero destination utility, and any interior agent of color \(a\) also has zero destination utility. Every interior agent of the other color has destination utility one and therefore must already have two neighbors of color \(a\). Hence **the opposite-color agents are isolated** among the \(a\)-agents; this condition is both necessary and sufficient for Nash stability.

If \(c_1\ne c_n\), either boundary agent would get utility one after moving, so both must presently have utility one: \(c_1\ne c_2\) and \(c_n\ne c_{n-1}\). Every interior agent would get exactly one half by jumping, and must therefore have at least one unlike occupied neighbor. Hence the **first and last runs have length one, all other runs have length one or two, and the number of runs is even**. These conditions are again both necessary and sufficient. This establishes the complete structural characterization without relying on a convergence theorem.

**2. Exact composition census.** In the equal-end case with red endpoints, every blue agent must occupy a different gap between successive red agents, yielding \(\binom{r-1}{b}\) words. Blue endpoints similarly contribute \(\binom{b-1}{r}\).

In the unequal-end case, there are \(2h+2\) alternating runs for some integer \(h\ge0\). Both terminal runs have length one, and the remaining \(h\) red and \(h\) blue runs independently have lengths one or two. For a fixed starting color, the numbers of length-two internal runs are \(r-h-1\) and \(b-h-1\), giving \(\binom{h}{r-h-1}\binom{h}{b-h-1}\). There are two choices for the starting color. These cases are disjoint and exhaustive and give the displayed formula. If \(r>b\), the red-end term \(\binom{r-1}{b}\) is positive; if \(b>r\), the blue-end term is positive; if \(r=b=m\), the alternating word with singleton runs is valid. Thus every positive composition admits an equilibrium. The labeling factor follows by free permutation of distinct agents of each color.

**3. Fibonacci total.** Introduce ordinary formal variables \(x,y\) marking the red and blue counts. In the equal-end case, the generating function over both colors present is

\[
\frac{x}{1-x-xy}-\frac{x}{1-x}
+\frac{y}{1-y-xy}-\frac{y}{1-y}.
\]

The unequal-end contribution is \(2xy/[1-xy(1+x)(1+y)]\). Upon setting \(x=y=z\) and restoring the two monochromatic words at every positive length, the full generating function is

\[
\sum_{n\ge1}H_nz^n
=\frac{2z}{1-z-z^2}+\frac{2z^2}{1-z^2(1+z)^2}
=\frac{1+z}{1-z-z^2}-\frac{1+z}{1+z+z^2}.
\]

The first term on the right has coefficient \(F_{n+2}\); the second has period-three coefficients \((-1,0,1)\) for \(n\equiv(0,1,2)\pmod3\). This proves the total census. Formally the constant coefficient cancels, consistent with counting only positive lengths.

**4. Balanced-population exponential rate.** If \(r=b=m\), both equal-end binomial terms vanish because \(\binom{m-1}{m}=0\), giving the stated balanced formula. Let \(D_n\) count only unequal-end equilibrium binary words of length \(n\), without fixing the population sizes. Its ordinary generating function is

\[
D(z)=\frac{2z^2}{1-z^2(1+z)^2}
=\frac{2z^2}{(1-z-z^2)(1+z+z^2)}.
\]

The unique smallest-modulus pole lies at \(z=\varphi^{-1}\), is simple, and has a positive residue coefficient. Therefore \(D_{2m}=\Theta(\varphi^{2m})\). At a fixed even length \(2m\) and fixed internal-run number \(h\), the number of unequal-end words with \(r=1+h+i\) red agents is proportional to

\[
\binom{h}{i}\binom{h}{2m-2-2h-i}.
\]

As a function of \(i\), this product is symmetric and unimodal around \(i=m-h-1\), corresponding exactly to \(r=b=m\). Thus in each internal-run class the balanced color count is maximal. There are at most \(2m+1\) possible red counts. Summing the inequalities over \(h\) gives

\[
\frac{D_{2m}}{2m+1}\le E_{m,m}\le D_{2m}.
\]

Consequently \(E_{m,m}=\varphi^{2m+o(m)}\). Stirling's formula gives \(\binom{2m}{m}=4^{m+o(m)}\), and taking \(m\)-th roots yields \(\varphi^2/4=(3+\sqrt5)/8\). This is an exact exponential rate, **not** a claim of an unproved asymptotic prefactor.

## Verification

Run `python3 verify.py` in the directory containing this document and the standalone verifier. The standalone program computes each agent's original utility and post-jump utility from the actual cycle graph, without invoking the run characterization. It checked \(131{,}064\) binary colorings for all occupied lengths from \(3\) through \(16\), compared every result to the local criterion, checked the exact fixed-composition census over \(3{,}159\) parameter pairs through length \(80\), checked balanced identities through \(m=80\), and replayed a full labeled four-vertex instance. All checks passed. The infinite generating-function identities and asymptotic limit are established by the proof above, not by finite computations.

## Relationship to prior work

Narayanan, Sabbagh and Voudouris [1] define exactly the fraction-valued diversity-seeking jump model and prove, in particular, convergence/potentiality for regular graphs with one vacancy and for maximum-degree-two graphs. Those general results guarantee the existence of an equilibrium but do not enumerate equilibria by population composition or give a Fibonacci census or exponential balanced-population rate. The calculation here conditions on the vacancy, explicitly handles departure-adjacency changes, and fully classifies all pure equilibria on cycles. This is a more specific mathematical question, not an implication of potentiality alone.

Narayanan, Opatrny, Tummala and Voudouris [2] instead use the **number of distinct alternative types** among neighbors, not the fraction of opposite-color neighbors; the objectives differ even for two types. For example the word \(AABBA\) around a vacancy is stable for the variety-count objective but is unstable for the fraction objective, because a blue agent with one red and one blue neighbor improves from \(1/2\) to \(1\) after moving to the vacancy. Kreisel, Boehmer, Froese and Niedermeier [3] analyze similarity-seeking payoffs and equilibrium robustness, not these diversity-seeking counts. Related similarity-seeking ring results likewise cannot be transferred merely by replacing a word or parameter because strategic moves relocate agents.

## Limitations

This result applies only to two types, a simple cycle, one vacant vertex, all agents strategic, and the exact fraction-valued utility. It neither determines the distribution of absorbing equilibria under a particular stochastic best-response rule nor applies to multiple vacancies, more types, or other network topologies. Novelty is based on comparison with accessible mathematical records and inspected primary literature; it is not a formal proof of worldwide publication priority.

## References

[1] L. Narayanan, Y. Sabbagh and A. A. Voudouris, *Diversity-Seeking Jump Games in Networks*, arXiv:2305.17757, first public version May 28, 2023. https://arxiv.org/abs/2305.17757 . Especially the model, Sections 5 and 6, and open problems.

[2] L. Narayanan, J. Opatrny, S. Tummala and A. A. Voudouris, *Variety-Seeking Jump Games on Graphs*, arXiv:2505.10005, 2025. https://arxiv.org/abs/2505.10005 . Distinct variety-count utility and potentiality results.

[3] L. Kreisel, N. Boehmer, V. Froese and R. Niedermeier, *Equilibria in Schelling Games: Computational Hardness and Robustness*, Autonomous Agents and Multi-Agent Systems 38 (2024), article 9. https://doi.org/10.1007/s10458-023-09632-7 . Similarity-seeking jump game and robustness results.
