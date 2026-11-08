# Five taxa are sharp for re-entrant single-species conservation priority

## Finding

For a rooted full-binary phylogenetic tree with positive, not necessarily clock-like, edge lengths, let each of its \(n\) taxa independently survive with a common probability \(p\in(0,1)\). One conservation action makes exactly one chosen taxon survive with probability one, at an equal cost for all taxa. Rank actions by the resulting gain in expected rooted phylogenetic diversity (PD).

**Sharp minimum.** If \(n\le4\), the gains for any two taxa can exchange order at most once as \(p\) varies over \((0,1)\). In particular, no taxon can be strictly globally optimal, cease to be optimal, and become strictly globally optimal again. For \(n=5\), a strictly globally optimal choice can switch twice, returning to the original taxon. For \(n=5\), a pair can cross twice only if its least common ancestor separates a three-tip clade from a two-tip clade, with one focal tip in each. All pairwise changes on five-tip trees number at most two.

**Complete two-crossing criterion for five tips.** Let focal taxon \(u\) belong to the three-tip side and taxon \(v\) to the two-tip side of their least common ancestor. Denote the incoming lengths of those two sides by \(L_3>0\) and \(L_2>0\). Set \(I\) equal to the length of the edge leading to the cherry containing \(u\), if \(u\) is in a cherry on the three-tip side, and zero if it is that side's isolated child. Let \(T_u,T_v\) be their pendant-edge lengths. Define \(A=L_3\), \(B=L_2-I\), \(C=T_u-T_v\). The gain difference, with \(q=1-p\), is

\[
G_u(p)-G_v(p)=q\bigl(Aq^2-Bq+C\bigr).
\]

It changes sign exactly twice in \(0<p<1\) **if and only if**

\[
C>0,\quad 0<B<2A,\quad B^2>4AC,\quad A-B+C>0.
\]

**Exact five-taxon witness.** The root separates the clades \(\{a,b,c\}\) and \(\{d,e\}\), with length one on both root edges. The three-taxon clade separates \(a\) from the cherry \(\{b,c\}\), whose incoming edge has length one. Pendant lengths are \(29/25\) for \(a\), \(1\) for \(d\), and \(1/20\) for each of \(b,c,e\). Every edge has strictly positive length. The gains are

\[
\begin{aligned}
G_a(p)&=q\left(\frac{29}{25}+q^2\right),&
G_d(p)&=q(1+q),\\
G_b(p)=G_c(p)&=q\left(\frac1{20}+q+q^2\right),&
G_e(p)&=q\left(\frac1{20}+q\right).
\end{aligned}
\]

Thus

\[
G_a(p)-G_d(p)=q\left(q-\frac15\right)\left(q-\frac45\right).
\]

The unique best action is protection of \(a\) when \(0<p<1/5\) or \(4/5<p<1\); it is protection of \(d\) when \(1/5<p<4/5\). At \(p=1/5\) and \(p=4/5\), and only there, \(a\) and \(d\) tie for first. The remaining three taxa never maximize the gain.

## Assumptions and scope

The tree is finite, rooted and full binary; each internal vertex has exactly two children. Edge lengths are arbitrary strictly positive real numbers, and there is no molecular-clock or ultrametric assumption. Survival events for distinct taxa are independent Bernoulli events with a common initial probability \(p\). Rooted PD is the sum of lengths of edges ancestral to at least one surviving taxon; the empty set has PD zero. A conservation action changes the survival probability of one taxon from \(p\) to one, leaving all others unchanged. The comparison is for a single equal-cost action and all \(p\in(0,1)\). A *crossing* means a change of strict rank across an interior tie, not a tie persisting on an interval.

## Proof

For an edge \(e\), write \(C_e\) for its descendant taxa, \(m_e=|C_e|\), and \(\ell_e\) for its length. The edge contributes to rooted PD if at least one descendant survives. Hence

\[
\mathbb E[\operatorname{PD}]=\sum_e\ell_e(1-q^{m_e}).
\]

If taxon \(i\) is made certain to survive, only edges ancestral to \(i\) change their inclusion probability. Their original probability of disappearance is \(q^{m_e}\), so the expected-PD gain is exactly

\[
G_i(p)=\sum_{e:\,i\in C_e}\ell_e q^{m_e}
=q\sum_{e:\,i\in C_e}\ell_e q^{m_e-1}.
\tag{1}
\]

This identity holds at arbitrary finite tree size, without approximation. The usual complementarity expression in the cited literature is equivalent to (1).

For two taxa \(u,v\), all ancestral edges above their least common ancestor contribute identically to the two gains and cancel. Only the two child subtrees at this ancestor matter. If those subtrees have sizes \((1,k)\), the singleton side contributes only a pendant term proportional to \(q\); on the other side all nonpendant terms have strictly positive coefficients of higher powers of \(q\). After division by \(q>0\), their difference is therefore constant or strictly monotone and has at most one zero. If both children have size two, both focal paths contain only their own pendant edge and one edge of descendant size two, so the gain difference divided by \(q\) is affine and again has at most one zero. For at most four taxa, these cases exhaust all possible least-common-ancestor splits. This proves the four-tip impossibility, including trees with fewer than four tips.

With five taxa, the only remaining least-common-ancestor split that can support two crossings is \((2,3)\); a \((1,4)\) split remains monotone, and smaller descendant sets reduce to the preceding cases. For focal taxon \(u\) in the three-tip side and \(v\) in the two-tip side, their noncommon ancestral edges have descendant counts three and two, optionally two on the \(u\) side, and one at each pendant edge. Applying (1) yields \(q(Aq^2-Bq+C)\), with the definitions in the finding. Because \(A>0\), its quadratic factor has two distinct roots in \((0,1)\) precisely when its vertex lies in \((0,1)\), the discriminant is positive, and both endpoint values are strictly positive. These conditions simplify to the five displayed strict inequalities: positivity of \(C\), positivity and upper bound \(0<B<2A\), \(B^2>4AC\), and positivity of \(A-B+C\). This proves the necessary and sufficient classification and the bound of two crossings for five taxa.

In the specified witness, formula (1) gives all five gains displayed above. The factorization establishes the two ties and signs. For every \(q\in(0,1)\),

\[
G_a-G_b=G_a-G_c=q\left(\frac{111}{100}-q\right)>0,
\qquad G_d-G_e=\frac{19}{20}q>0.
\]

Consequently the global best is always one of \(a,d\), and their factorized difference proves the stated three phases. This also proves that five taxa suffice and therefore establishes sharpness.

## Verification

The standalone script `verify.py` uses only Python's standard library and exact rational arithmetic. Run `python verify.py` from the extracted package. It independently computes expected PD by enumerating all \(2^5=32\) possible survivor sets and compares the resulting protection gains against (1) at nine rational parameter values. It checks the two exact crossover points and optimality inequalities, constructs all rooted labeled binary shapes with up to five leaves (counts \(1,1,3,15,105\)), and verifies the topological exclusions for all 100 unordered tip comparisons in shapes with at most four leaves. The continuous-parameter and sharp-minimum claims are proved algebraically above; sampled checks and enumeration do not substitute for those arguments.

## Relationship to prior work

The rooted expected-PD formula and single-species complementarity score are established in the Noah's Ark and HED/HEDGE literature, especially Hartmann and Steel (2006), Steel, Mimoto and Mooers (2007, Theorems 3.1 and 4.1), and Faith (2008, Section 'Extinction Probabilities and Expected PD'). This result does **not** claim that formula, the independent-extinction model, or the optimal single-action principle as new. It resolves a distinct parameter-dependent structural question: the minimum number of taxa permitting a best protection choice to disappear and return as the *common* background survival probability varies, and the complete two-crossing conditions at that minimum. The checked works give gain/optimization expressions and examples of priority changes, not the sharp five-tip double-switch classification. An earlier exact result for equal unit edge lengths guarantees a common maximizer through seven taxa; it does not imply the present variable-length theorem, and the five-tip witness does not satisfy equal edge lengths.

## Limitations

Positive unequal edge lengths are essential to the exhibited example; no ultrametric or all-equal-length claim is made. Independent identical survival risks and equal-cost full protection are stylized. The theorem compares a single action, not optimal multi-taxon investment portfolios or correlated extinction outcomes. It does not estimate real extinction probabilities or imply any actual species should receive conservation resources. Historical priority is assessed only against the accessible sources and searches, not certified exhaustively.

## References

1. Hartmann, K. and Steel, M. (2006). 'Maximizing Phylogenetic Diversity in Biodiversity Conservation: Greedy Solutions to the Noah's Ark Problem.' *Systematic Biology* 55(4), 644–651. https://doi.org/10.1080/10635150600873876 (author-hosted full text: https://www.math.canterbury.ac.nz/~m.steel/Non_UC/files/research/noah.pdf).
2. Steel, M., Mimoto, A. and Mooers, A. Ø. (2007). 'Hedging Our Bets: The Expected Contribution of Species to Future Phylogenetic Diversity.' *Evolutionary Bioinformatics* 3, 237–244. https://doi.org/10.1177/117693430700300024 ; arXiv:0704.2649 (first posted 2007-04-20).
3. Faith, D. P. (2008). 'Threatened Species and the Potential Loss of Phylogenetic Diversity: Conservation Scenarios Based on Estimated Extinction Probabilities and Phylogenetic Risk Analysis.' *Conservation Biology* 22(6), 1461–1470. https://doi.org/10.1111/j.1523-1739.2008.01068.x.
