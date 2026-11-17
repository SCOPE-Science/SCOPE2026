# Equilibrium rigidity and two efficiency regimes in one-vacancy biclique diversity games

## Finding

**Theorem.** Fix integers \(a,b\ge2\) and \(r,s\ge1\) with \(r+s=a+b-1\). Place \(r\) red and \(s\) blue agents on distinct vertices of the complete bipartite graph \(K_{a,b}\), leaving exactly one vertex vacant. All agents may jump to the vacancy and maximize the fraction of *occupied* neighbors having the opposite color. A configuration is a pure Nash equilibrium if and only if **the part opposite the vacancy is monochromatic**.

Write \(\binom nk=0\) whenever \(k\notin\{0,1,\ldots,n\}\). The exact number of equilibria when agents of the same color are indistinguishable is
\[
E_{a,b}(r)=a\left[\binom{a-1}{r-b}+\binom{a-1}{r}\right]
+b\left[\binom{b-1}{r-a}+\binom{b-1}{r}\right].
\]
For distinguishable agents the number is \(r!s!E_{a,b}(r)\), and \(E_{a,b}(r)>0\) for every permitted composition.

Two consequences show sharply different relationships between equilibrium and welfare.

**Balanced bicliques.** For \(K_{m,m}\), \(m\ge2\), with \(m\) red and \(m-1\) blue agents, there are exactly \(2m\) indistinguishable-color equilibrium configurations. All achieve the maximal social welfare \(2m-1\). A uniformly random assignment with those color counts (including a uniformly random vacant vertex) is an equilibrium with probability
\[
\frac{2}{\binom{2m}{m}}\sim 2\sqrt{\pi m}\,4^{-m}.
\]
Thus equilibrium is exponentially rare although every equilibrium is efficient.

**Unbalanced thin bicliques.** For \(K_{a,2}\), \(a\ge3\), with two red and \(a-1\) blue agents, the social optimum equals \(a+1\), but the least equilibrium welfare equals \(2+4/(a-1)\). Consequently the *exact* social price of anarchy is
\[
\operatorname{PoA}(K_{a,2})=\frac{a-1}{2}.
\]
There are \(a[1+\binom{a-1}{2}]\) equilibria, of which \(a\binom{a-1}{2}\) are in the low-welfare class (the distinction vanishes at \(a=3\)). For \(a\ge4\), the fraction of worst-welfare equilibria tends to one as \(a\to\infty\). This linear inefficiency occurs with both color populations of size at least two, on graphs of minimum degree two, diameter two and vertex connectivity two.

## Assumptions and scope

The graph is simple and complete bipartite, with labeled vertices in parts of sizes \(a,b\ge2\). There is exactly one empty vertex, no stubborn agents, and no restrictions on jumps beyond moving into that vacancy. An agent's utility is the count of occupied neighbors of the opposite color divided by its total count of occupied neighbors, with the usual zero convention when there are none. A deviation is profitable only when it *strictly* increases utility; ties do not disrupt equilibrium. The empty neighbor is excluded from the utility denominator. The formula counts colored placements, not distinguished-agent permutations, until the factorial multiplier is applied. Social welfare is the sum of these utilities; the price of anarchy divides maximum feasible welfare by minimum equilibrium welfare.

## Proof

**Step 1: One empty side forces the opposite occupied side to be monochromatic.** Suppose the vacancy lies in the part of size \(a\). Let \(x\) denote the number of red occupants there (among \(a-1\) occupants), and \(y\) the number of red occupants of the fully occupied part of size \(b\). An agent already in the first part is indifferent between its current vertex and the vacancy, because the occupied neighbors in the other part do not change. A red agent in the second part has present utility \(1-x/(a-1)\) and, after jumping, utility \(1-(y-1)/(b-1)\). If such a red agent exists, no improvement requires
\[
(b-1)x\le(a-1)(y-1).
\]
A blue agent in the second part has present utility \(x/(a-1)\) and, after jumping, utility \(y/(b-1)\). If such a blue agent exists, no improvement requires
\[
(a-1)y\le(b-1)x.
\]
If both colors occur in the second part, \(1\le y\le b-1\), and the two inequalities are contradictory:
\[
(a-1)y\le(b-1)x\le(a-1)(y-1).
\]
Hence that part is monochromatic. Conversely, if the fully occupied part is monochromatic, each of its agents obtains utility zero by moving to the vacant vertex, while an agent in the partly occupied part has no utility change upon moving within the same part. No profitable move exists. The same argument applies with the parts interchanged.

**Step 2: Exact enumeration and unconditional existence.** If the vacancy is in the \(a\)-part, there are \(a\) choices for it. If the entire \(b\)-part is red, the remaining \(r-b\) red agents choose vertices among \(a-1\) positions; if the entire \(b\)-part is blue, all \(r\) red agents choose those positions. This gives the first bracket of \(E_{a,b}(r)\). Exchanging parts gives the other bracket. These cases are pairwise disjoint, as both parts have size at least two, and every stable configuration is counted. Each colored configuration allows exactly \(r!s!\) assignments of distinguishable agents. For existence, assume without loss of generality \(a\le b\). Since \(r+s=a+b-1\ge2a-1\), at least one color class has size at least \(a\). Make the whole \(a\)-part that color and leave the vacancy in the \(b\)-part; the resulting configuration is stable.

**Step 3: Balanced rarity and perfect welfare.** For \(a=b=m\) and \(r=m\), the only nonzero binomial terms are the two terms fixing an entire part red, yielding \(E_{m,m}(m)=2m\). Every colored equilibrium places all red agents on one side and all blue agents on the occupied vertices of the other, so each of the \(2m-1\) agents obtains utility one. The complete space of colored placements has size \(2m\binom{2m-1}{m}\). Hence the equilibrium probability is \(1/\binom{2m-1}{m}=2/\binom{2m}{m}\). Stirling's formula gives the displayed asymptotic.

**Step 4: The sharp inefficiency family.** In \(K_{a,2}\) with \(a\ge3\), neither type has enough agents to fill the entire \(a\)-part, so equilibrium vacancy must lie in that part. If the two-vertex part is red, all \(a-1\) occupied vertices of the first part are blue, every agent gets utility one, and welfare is \(a+1\), the trivial universal upper bound. If the two-vertex part is blue, the first part contains two red and \(a-3\) blue agents. Its two red agents each have utility one, while its blue agents have utility zero; the two blue agents in the second part each have utility \(2/(a-1)\). Thus welfare is \(2+4/(a-1)\). Both equilibrium types exist. Their quotient is
\[
\frac{a+1}{2+4/(a-1)}=\frac{a-1}{2},
\]
and the placements of the low-welfare type are exactly \(a\binom{a-1}{2}\). For \(a\ge4\) this class is strictly less efficient and its share among equilibria approaches one. The claimed connectivity and minimum-degree properties follow directly from the structure of \(K_{a,2}\).

## Verification

Run the dependency-free Python 3 program `verify.py` from the directory containing this result. It constructs every two-color placement with one vacancy for all \(2\le a,b\le5\) and nonempty color counts, tests every allowed unilateral jump using exact rational payoffs, and compares the resulting equilibrium counts with the theorem. In total it checks \(15{,}136\) placements across \(80\) population cases. It separately checks the exact welfare/price-of-anarchy formula for \(3\le a\le6\) and the balanced cases \(2\le m\le5\). The explicit proof above, not the finite program, establishes the statements for all admissible integers.

## Relationship to prior work

Narayanan, Sabbagh and Voudouris introduce the fraction-of-unlike-neighbors diversity-seeking jump game and prove general welfare bounds (their Theorem 6.1) and a large-price-of-anarchy family on stars with a singleton minority type (their Theorem 6.3). The theorem here instead classifies *every* equilibrium in the complete-bipartite one-vacancy subclass, gives its exact census, and shows linearly increasing price of anarchy even on two-vertex-connected graphs with at least two agents per type. The general upper bound does not give this equality classification or family. Agarwal and coauthors study the opposite, similarity-seeking objective; that payoff criterion has different profitable deviations and does not directly characterize the present equilibria. Subsequent variety-seeking work uses a distinct utility (number of different types represented), not the fraction of opposite-color neighbors.

## Limitations

The classification needs exactly two colors, exactly one vacancy and the complete bipartite graph. It does not assert robustness to additional vacancies, stubborn agents, other topologies or other utility conventions. The exponential rarity statement is for uniformly distributed colored assignments of a *specified* population composition, and the sharp price of anarchy is for the specified thin-biclique family. The novelty comparison is based on inspected accessible sources and mathematical-record search; publication priority is not independently certified and unindexed equivalent results remain possible. Finite numerical verification is not an infinite proof.

## References

1. L. Narayanan, Y. Sabbagh and A. A. Voudouris, *Diversity-seeking Jump Games in Networks*, arXiv:2305.17757, first public version May 28, 2023; inspected HTML version 3 (March 14, 2024). https://arxiv.org/html/2305.17757v3
2. A. Agarwal, E. Elkind, J. Gan, A. Igarashi, W. Suksompong and A. A. Voudouris, *Schelling games on graphs*, Artificial Intelligence 301 (2021), 103576. https://doi.org/10.1016/j.artint.2021.103576
3. L. Narayanan, J. Opatrny, S. Tummala and A. A. Voudouris, *Variety-Seeking Jump Games on Graphs*, arXiv:2505.10005 (2025). https://arxiv.org/abs/2505.10005
