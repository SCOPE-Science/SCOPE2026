# Five pollinators are sharp for survival-dependent quorum-service augmentation

## Finding

A three-plant interaction network in which *each* plant needs two different surviving pollinator species admits a single optimal link addition for every pollinator-survival probability whenever the number of pollinators is at most four. Five is sharp: exactly six labeled-plant neighborhood multisets, forming one class under plant relabeling, force the optimal addition to change at \(p=1/3\).

Specifically, with pollinator neighborhoods encoded by nonzero three-bit masks (A=1, B=2, C=4), consider
\[
(1,1,2,6,7).
\]
There are two competing actions. Action L adds plant A to the pollinator having neighborhood BC (mask 6); action H adds plant C to the pollinator having neighborhood B (mask 2). If \(R_L(p)\) and \(R_H(p)\) are the probabilities that all three plants each retain at least two pollinator partners, then
\[
R_L(p)-R_H(p)=p^2(1-p)(1-3p).
\]
Action L is uniquely optimal among link types for \(0<p<1/3\), the two tie at \(p=1/3\), and H is uniquely optimal for \(1/3<p<1\). All other missing links are strictly worse than H for every interior probability. The six exceptional labeled-plant neighborhood multisets are exactly the distinct relabelings of the displayed example.

## Assumptions and scope

Take precisely three permanent plants and \(m\) independently surviving pollinator species. Pollinator identities are irrelevant for the classification, but identical neighborhood types may occur for distinct pollinators. Each pollinator initially has a nonempty set of plant partners, and each plant has at least two distinct partners in the intact network. One previously absent plant–pollinator link is added before survival. A plant meets its service requirement if at least two distinct linked pollinators survive. One pollinator can support multiple plants; **no exclusive-capacity or matching constraint** is imposed. All three plants must meet this two-partner quorum simultaneously. Compare decisions for every \(p\in(0,1)\); endpoint ties are not treated as switching. No assumption of graph connectivity is needed. A network with no missing link has no allowable decision and is outside the optimization statement.

## Proof

**1. Complete incidence encoding.** A pollinator's nonempty plant-neighborhood is one of the masks \(1,\ldots,7\). Since permuting pollinators cannot change the success law or available action types, every admissible isomorphism class with labeled plants and \(m\) pollinators is represented exactly once by a nondecreasing \(m\)-tuple of these masks. Every tuple is tested for at least two partners at each plant. Adding an absent link means selecting a mask \(s\) present in the tuple and a zero bit \(2^v\), then replacing one copy of \(s\) by \(s+2^v\). The algorithm constructs all and only distinct action types, including when duplicate pollinator masks occur.

**2. Exact survival coefficients.** For a modified network \(G\), let \(q_k(G)\) count the \(k\)-element subsets of pollinators that give each plant at least two neighbors. By independence,
\[
R_G(p)=\sum_{k=0}^{m} q_k(G)p^k(1-p)^{m-k}.
\]
In an admissible starting network \(q_0=q_1=0\) and \(q_m=1\). A link addition preserves the latter properties. Since every Bernstein-basis factor is positive on \(0<p<1\), one action whose \(q_k\) are coordinatewise at least those of every other action is optimal for every survival probability.

**3. Exhaustive finite certificate.** The accompanying executable `verifier.py` uses `combinations_with_replacement(range(1,8),m)` for \(m=2,3,4,5\), the complete set of neighborhood multisets from Step 1. It enumerates all admissible missing links, computes every coefficient two independent ways—first by scanning live pollinator configurations and incrementing plant degrees, and second by intersecting live subsets with the three plant-specific neighbor bitsets—and asserts equality for every action. It verifies 1,284 such independent pairs of coefficient vectors. The numbers of admissible multisets with at least one missing interaction for \(m=2,3,4,5\) are, respectively, \(0,13,77,251\). For every one of the 13 and 77 admissible multisets with \(m=3,4\), a coefficientwise-dominating action exists. For \(m=2\), the two pollinators must both meet all three plants, leaving no missing interaction. This exhaustively establishes the lower bound.

**4. Complete first-switch classification.** At \(m=5\), all but six of the 251 admissible multisets have a coefficientwise-dominating action. The six exceptions are precisely the orbit of \((1,1,2,6,7)\) under the six permutations of A, B and C. All six have the same set of action coefficient vectors \((q_0,\ldots,q_5)\):
\[
\begin{gathered}
(0,0,0,2,3,1),\quad (0,0,0,3,3,1),\\
(0,0,0,3,5,1),\quad (0,0,0,4,5,1),\\
(0,0,1,3,3,1).
\end{gathered}
\]
The vector \((0,0,0,4,5,1)\) dominates the first three of the displayed vectors and corresponds to H; the remaining vector \((0,0,1,3,3,1)\) corresponds to L. Direct substitution into Step 2 gives
\[
\begin{aligned}
R_L(p)-R_H(p)&=p^2(1-p)^3-p^3(1-p)^2-2p^4(1-p)\\
&=p^2(1-p)(1-3p).
\end{aligned}
\]
This difference is positive below \(1/3\), zero at \(1/3\), and negative above. The coefficientwise dominance of H over every other action gives the full choice classification. No numerical sampling is needed for the proof, and the finite search covers every case admitted by the stated hypotheses.

## Verification

Run `python3 verifier.py` with the standard Python 3 library. It constructs all 341 admissible nontrivial profiles for \(m\le5\), compares independent coefficient computations across all 1,284 link actions, verifies the six-exception orbit and its exact action vectors, and checks the factored difference using exact rational arithmetic. The verifier is the explicit exhaustive finite certificate; the proof above establishes why its loops cover the entire domain. A separate manual live-subset count for the displayed five-pollinator witness agrees with the two action vectors. The verifier checks no claim for \(m>5\).

## Relationship to prior work

Plant–animal network nestedness and specialization were characterized by Bascompte et al. (2003), and Memmott et al. (2004) modeled pollinator-removal robustness. Devoto et al. (2012) compared restoration for functional complementarity versus redundancy, while Astegiano et al. (2015) explicitly emphasized sensitivity to partner loss and the uncertainty of functional redundancy. These motivate the choice of a two-partner service objective, but no inspected full text provides the exact first probability-dependent one-link optimization classification reported here.

A related finite-guild study of capacity-limited service asks for a *matching* of three plants to distinct surviving pollinators. It does not imply the present theorem: here a pollinator can serve all three plants, but each plant requires two different partners. Similarly, the one-surviving-partner extinction model and other shared-resource covariance results use different logical objectives. Work on Boolean threshold models of ecological restoration (Fatemi Nasrollahi, Campbell and Albert, 2023) addresses dynamical attractors and restoration strategies rather than the exact independent-survival link-addition polynomial. Abstract-access limitations for some restoration studies prevent a historical-priority guarantee.

## Limitations

This is an exact finite classification only through five pollinators, for three permanent plants, two distinct required partners per plant, homogeneous independent pollinator survivals and exactly one link addition. There is no claim that two pollinator species always suffice to assure reproduction in nature or that every interaction has equal strength. A nonzero interaction need not represent a feasible management intervention. No result for bigger guilds, unequal probabilities, temporal rewiring or environmental correlation follows. Priority beyond the inspected sources remains provisional; an independent audit has not been performed.

## References

- Bascompte, J., Jordano, P., Melián, C. J., and Olesen, J. M. (2003), *The nested assembly of plant–animal mutualistic networks*. PNAS 100, 9383–9387. https://doi.org/10.1073/pnas.1633576100. First public online July 24, 2003.
- Memmott, J., Waser, N. M., and Price, M. V. (2004), *Tolerance of pollination networks to species extinctions*. Proceedings of the Royal Society B 271, 2605–2611. https://doi.org/10.1098/rspb.2004.2909.
- Devoto, M., Bailey, S., Craze, P., and Memmott, J. (2012), *Understanding and planning ecological restoration of plant–pollinator networks*. Ecology Letters 15, 319–328. https://doi.org/10.1111/j.1461-0248.2012.01740.x.
- Astegiano, J. et al. (2015), *The robustness of plant-pollinator assemblages: linking plant interaction patterns and sensitivity to pollinator loss*. PLOS ONE 10, e0117243. https://doi.org/10.1371/journal.pone.0117243.
- Fatemi Nasrollahi, F. S., Campbell, C., and Albert, R. (2023), *Predicting cascading extinctions and efficient restoration strategies in plant–pollinator networks via generalized positive feedback loops*. Scientific Reports 13, 902. https://doi.org/10.1038/s41598-023-27525-3.
