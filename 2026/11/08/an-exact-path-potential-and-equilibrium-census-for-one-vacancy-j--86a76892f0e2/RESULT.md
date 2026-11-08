# An exact path potential and equilibrium census for one-vacancy jump dynamics on bicliques

## Finding

Consider a complete bipartite graph \(K_{a,b}\) with \(a,b\ge1\) and \(a+b\ge3\). There are \(r\ge1\) red and \(s\ge1\) blue agents, with \(r+s=a+b-1\), and exactly one vacant vertex. Every agent may jump into the vacancy, strictly improving her utility. Agents of each type share an arbitrary real-valued payoff function \(u_R,u_B:[0,1]\to\mathbb R\) of their same-type fraction in their *occupied closed neighborhood*, counting themselves. No monotonicity, continuity, or single-peakedness is assumed.

**Theorem.** Every strictly improving jump sequence terminates. In fact, its length is at most
\[
H(a,b,r)=\min\{2r,2a-1\}-\max\{-1,2(r-b)\}\le 2\min\{a,b\}.
\]
An explicit path-shaped integer ordinal potential is given below. It characterizes every pure Nash equilibrium by local maxima and gives the number of equilibria for labeled agents and labeled vertices by an exact finite expression. In particular, the theorem applies to all single-peaked utilities in the initiating jump Schelling model.

## Assumptions and scope

Let \(A\) and \(B\) be the two vertex parts of cardinalities \(a\) and \(b\). For an occupied vertex \(v\) hosting agent \(i\) of color \(c\), let
\[
f_i=\frac{1+|\{w\in N(v):\text{an agent of color }c\text{ occupies }w\}|}{1+|\{w\in N(v):w\text{ is occupied}\}|},
\qquad U_i=u_c(f_i).
\]
Every move transfers one agent to the unique vacant vertex. Moves with equal old and new payoff are not improvements and are excluded. Both color populations are positive, agents and vertices are individually labeled when counting equilibria, and the payoff functions are identical within each color (but can differ across colors). The graph has no loops; the occupant's own color is counted as the extra \(1\) in the displayed fraction.

Define quotient states \(L_x\), with the vacancy in \(A\) and \(x\) red agents in occupied \(A\), and \(R_x\), with the vacancy in \(B\) and \(x\) red agents in fully occupied \(A\). Precisely,
\[
L_x\text{ feasible}\iff 0\le x\le a-1,\quad0\le r-x\le b,
\]
\[
R_x\text{ feasible}\iff 0\le x\le a,\quad0\le r-x\le b-1.
\]
Place \(L_x\) at integer coordinate \(t=2x\) and \(R_x\) at \(t=2x-1\). All feasible quotient coordinates form the consecutive integer interval
\[
I=\{t_{\min},t_{\min}+1,\ldots,t_{\max}\},\quad
 t_{\min}=\max\{-1,2(r-b)\},\quad
 t_{\max}=\min\{2r,2a-1\}.
\]

## Proof

**1. Every nontrivial jump moves one step on the quotient path.** A jump within the same graph part leaves the moving agent's occupied closed-neighborhood color fraction unchanged: the opposite part contains exactly the same agents and the new position contributes the same single self-member. Thus no within-part jump is strict. A cross-part jump from a state \(R_x\) can be made by a blue agent to \(L_x\) or a red agent to \(L_{x-1}\); from \(L_x\) a blue agent can jump to \(R_x\) or a red agent to \(R_{x+1}\). Each feasible adjacent transition is realizable by a moving agent of its stated color, because positive numbers of that color on the source side are precisely the feasibility conditions at the destination. Therefore the strict-improvement relation projects completely to consecutive edges of \(I\).

**2. An edge has a state-independent gain sign.** On the edge \(R_x\leftrightarrow L_x\), the agent moving to increasing \(t\) is blue; its forward gain is
\[
g_B(x)=u_B\!\left(\frac{a-x}{a}\right)-u_B\!\left(\frac{b-r+x}{b}\right).
\]
On the edge \(L_x\leftrightarrow R_{x+1}\), the agent moving to increasing \(t\) is red; its forward gain is
\[
g_R(x)=u_R\!\left(\frac{r-x}{b}\right)-u_R\!\left(\frac{x+1}{a}\right).
\]
The reverse gain on either edge is the negative of the displayed gain, regardless of individual identities, since its endpoints' fractions depend only on the color counts and vacancy part.

For each \(t<t_{\max}\), define \(\varepsilon_t=\operatorname{sgn}(g_B(x))\) when \(t=2x-1\), and \(\varepsilon_t=\operatorname{sgn}(g_R(x))\) when \(t=2x\), where \(\operatorname{sgn}(0)=0\). Define
\[
\Phi(t_{\min})=0,\qquad \Phi(t+1)=\Phi(t)+\varepsilon_t.
\]
Every improving jump \(t\to t+1\) occurs only when \(\varepsilon_t=1\), whereas every improving jump \(t+1\to t\) occurs only when \(\varepsilon_t=-1\). Thus **every strictly improving jump increases \(\Phi\) by exactly one**. The range of \(\Phi\) has width at most \(|I|-1=t_{\max}-t_{\min}\). Consequently no improvement sequence repeats a quotient state, and every such sequence has length at most \(H(a,b,r)=t_{\max}-t_{\min}\). The displayed formulas for the interval endpoints immediately imply \(H\le2a\). If \(r\ge b\), then \(H\le2r-2(r-b)=2b\); otherwise \(H\le2r+1\le2b-1\). This proves the claimed bound.

**3. Exact characterization and labeled equilibrium count.** A configuration is a pure Nash equilibrium precisely when its quotient coordinate \(t\) is a weak local maximum of \(\Phi\) on \(I\):
\[
t\in\mathcal M\iff \Phi(t)\ge\Phi(t-1)\text{ whenever }t-1\in I,
\quad \Phi(t)\ge\Phi(t+1)\text{ whenever }t+1\in I.
\]
(The weak inequalities accommodate tied edges, which are not strict improvements.) Every nonempty finite directed path has a sink, so such equilibria always exist. For any feasible \(L_x\), choosing the vacant vertex and red occupied positions gives \(a\binom{a-1}{x}\binom{b}{r-x}\) red/blue colorings. For any feasible \(R_x\), the corresponding number is \(b\binom{a}{x}\binom{b-1}{r-x}\). Each coloring admits exactly \(r!s!\) assignments of the distinct agents to the red and blue vertices. Thus the exact number of *labeled pure Nash equilibria* is
\[
\boxed{E=r!s!\left(
\sum_{\substack{x:\,L_x\text{ feasible}\\2x\in\mathcal M}}
 a\binom{a-1}{x}\binom{b}{r-x}
+\sum_{\substack{x:\,R_x\text{ feasible}\\2x-1\in\mathcal M}}
 b\binom{a}{x}\binom{b-1}{r-x}
\right).}
\]
Only \(H+1\le2\min\{a,b\}+1\) quotient states and their adjacent gain comparisons are required; binomial and factorial arithmetic then gives the exact count. This completes the proof.

## Verification

The accompanying standalone script `verify.py` directly enumerates all colorings and possible single-agent jumps for \(1\le a,b\le5\), \(a+b\ge3\), all nonempty red and blue populations, and six pairs of rational peaks for continuous triangular single-peaked utilities. It independently recomputes occupied closed-neighborhood payoffs and compares every move with the predicted directed quotient edge and integer potential; it also compares the enumeration of equilibria against the displayed count after removing the agent-label factorial. The exact-rational run passed 600 instances, 3,000 projected-state visits, 2,400 projected edges, 719,520 individual jump checks, and 35,980 equilibrium colorings. Run using `python verify.py` in the directory containing the two files. These finite checks are corroborative; the preceding arguments prove the theorem for arbitrary sizes and arbitrary type-homogeneous payoff functions.

## Relationship to prior work

Friedrich, Lenzner, Molitor, and Seifert (2023) introduce single-peaked jump Schelling games, prove existence of equilibria under a sufficiently large independent set (Theorem 3.2), identify a special cycle potential (Theorem 2.4), and exhibit nonconvergent improvement cycles on other graphs. Their existence theorem can apply to bicliques, so equilibrium **existence itself** is not asserted as a new consequence here. The new claim concerns a universal path potential, bounded convergence time, and the complete equilibrium census on an explicitly delimited family, none of which follows merely from existence. Narayanan, Sabbagh, and Voudouris (2023) obtain a potential for a different linear diversity-seeking objective on regular and spider graphs with one empty node; balanced bicliques overlap their regular-graph domain, but their result neither covers general utilities on all bicliques nor gives this census. Kanellopoulos, Kyropoulou, and Voudouris (2020) study the self-counting monotone Schelling model, and Agarwal et al. (2019) the earlier graph-based model, without the all-utility biclique path result identified here.

## Limitations

The result assumes exactly one vacancy, two colors, and common payoffs within each color; it does not establish convergence for two vacancies, more colors, asymmetric preferences within one color, or arbitrary graphs. With more vacancies, quotient transitions need not form a path. No random-move mixing-time bound is asserted: the bound counts strictly improving moves, not idle decisions or stochastic scheduling delays. The preceding literature comparison is based on inspected accessible primary articles and search results, not an exhaustive priority certificate. Independent external verification has not been performed.

## References

1. T. Friedrich, P. Lenzner, L. Molitor, and L. Seifert, *Single-Peaked Jump Schelling Games*, original public preprint 2023-02-23, https://arxiv.org/abs/2302.12107 (especially Sections 2--3 and Theorems 2.4, 3.2).
2. P. Kanellopoulos, M. Kyropoulou, and A. A. Voudouris, *Modified Schelling Games*, 2020 preprint, https://arxiv.org/abs/2005.12149 (closed-neighborhood utility and Appendix A).
3. L. Narayanan, Y. Sabbagh, and A. A. Voudouris, *Diversity-seeking Jump Games in Networks*, 2023 preprint, https://arxiv.org/abs/2305.17757 (potential on regular and spider graphs).
4. A. Agarwal, E. Elkind, J. Gan, A. Igarashi, W. Suksompong, and A. A. Voudouris, *Schelling Games on Graphs*, 2019 preprint, https://arxiv.org/abs/1902.07937.
