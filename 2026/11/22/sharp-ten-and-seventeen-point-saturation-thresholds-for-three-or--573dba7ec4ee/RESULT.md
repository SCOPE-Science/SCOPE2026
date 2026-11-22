# Sharp ten- and seventeen-point saturation thresholds for three ordered successor paths

## Finding
Let \(V\) be a finite nonempty set equipped with three independently chosen strict linear orders \(\prec_1,\prec_2,\prec_3\). Write \(S_i(x,y)\) when \(y\) immediately follows \(x\) in \(\prec_i\). A *reference edge* is an ordered pair \((x,y)\) satisfying \(S_1(x,y)\). We study the existence of one finite model realizing **every** possible two-coordinate atomic profile on its reference edges.

In the *successor-only language*, for a reference edge define its profile \((c_2,c_3)\in\{+, -,0\}^2\), where \(c_j=+\) means \(S_j(x,y)\), \(c_j=-\) means \(S_j(y,x)\), and \(c_j=0\) means neither. In the *order-visible language*, refine each zero into \(G_+\) if \(x\prec_j y\) and \(G_-\) if \(y\prec_j x\), while writing \(A_+,A_-\) for the two immediate-successor possibilities. Its profiles lie in \(\{A_+,A_-,G_+,G_-\}^2\).

**Theorem (two sharp finite spectra).** For every positive integer \(n\), a model on exactly \(n\) vertices realizing all nine successor-only profiles on reference edges exists **if and only if** \(n\ge10\). A model on exactly \(n\) vertices realizing all sixteen order-visible profiles exists **if and only if** \(n\ge17\). Both universal-profile properties are definable by a single first-order sentence of quantifier rank two over the respective signatures. At either minimum size, every profile occurs exactly once on the reference path; in particular, both minima are forced uniform, not merely attainable.

The refinement from the successor-only to the order-visible language thus changes the sharp simultaneous-realization budget from ten to seventeen elements. The theorem concerns three spanning directed paths induced by linear orders, not three arbitrary directed graphs.

## Assumptions and scope
All orders are strict, total, and on the same nonempty finite carrier; no two designated orders are required to differ. Each \(S_i\) is exactly the immediate-successor relation of \(\prec_i\), not just any path relation or a transitive closure. There are no colors, constants, extra binary symbols or quotient identifications. The successor-only language has \(S_1,S_2,S_3,=\), whereas the refined language has these symbols and \(\prec_1,\prec_2,\prec_3\). The orientation in each profile is relative to the *ordered* reference edge \((x,y)\). In the refined language, the four cases are exclusive and exhaustive for distinct \(x,y\). A gap is a nonconsecutive ordered pair, regardless of the number of intervening elements.

For completeness, let \(\theta_{+}^{j}(x,y)=S_j(x,y)\), \(\theta_-^{j}(x,y)=S_j(y,x)\), and \(\theta_0^{j}(x,y)=\neg S_j(x,y)\wedge\neg S_j(y,x)\). The successor-only saturation sentence is
\[
\Phi_3=\bigwedge_{(a,b)\in\{+,-,0\}^2}\exists x\exists y\bigl(S_1(x,y)\wedge\theta_a^2(x,y)\wedge\theta_b^3(x,y)\bigr).
\]
The refined sentence \(\Phi_4\) is defined by replacing the three possible \(\theta\)-statuses by the four predicates \(S_j(x,y)\), \(S_j(y,x)\), \((x\prec_j y)\wedge\neg S_j(x,y)\), and \((y\prec_j x)\wedge\neg S_j(y,x)\). Each conjunct has exactly two nested existential quantifiers, so both sentences have quantifier rank two.

## Proof
**1. The sharp lower bounds.** Any \(n\)-vertex strict linear order has precisely \(n-1\) directed immediate-successor edges. Since a reference edge has exactly one profile, realizing every member of a family of \(m\) distinct profiles requires \(n-1\ge m\). For the successor-only family \(m=3^2=9\), yielding \(n\ge10\); for the refined family \(m=4^2=16\), yielding \(n\ge17\). If equality holds, all reference edges have pairwise distinct profiles. Hence every profile must occur exactly once and the marginal frequencies of the statuses in each supplementary order are equal: three of each of \(+, -,0\) in the ten-vertex case, and four of each of \(A_+,A_-,G_+,G_-\) in the seventeen-vertex case. These give necessary structural equalities for every size-minimizing model.

**2. A ten-point construction.** On \(V=\{1,\ldots,10\}\), let the first order be \(1,2,\ldots,10\) and take the following lists as the successive elements of the second and third orders:

- \(\prec_2\): `7,10,9,8,3,4,5,6,2,1`
- \(\prec_3\): `5,6,7,4,3,2,1,10,8,9`

For each reference edge \((i,i+1)\), the pair of statuses in orders two and three is exactly:

| \(i\) | \(c_2\) | \(c_3\) |
|---:|:---:|:---:|
| 1 | \(-\) | \(-\) |
| 2 | \(0\) | \(-\) |
| 3 | \(+\) | \(-\) |
| 4 | \(+\) | \(0\) |
| 5 | \(+\) | \(+\) |
| 6 | \(0\) | \(+\) |
| 7 | \(0\) | \(0\) |
| 8 | \(-\) | \(+\) |
| 9 | \(-\) | \(0\) |

The table has one occurrence of each of the nine ordered pairs from \(\{+,-,0\}^2\). Thus \(\Phi_3\) has a ten-element model.

**3. A seventeen-point construction.** On \(V=\{1,\ldots,17\}\), again take the first order to be increasing and use:

- \(\prec_2\): `8,9,1,7,6,14,15,17,16,13,12,2,3,10,11,5,4`
- \(\prec_3\): `3,4,7,8,12,13,17,16,2,1,6,5,9,15,14,10,11`

The sixteen reference-edge profiles are:

| \(i\) | \(c_2\) | \(c_3\) |
|---:|:---:|:---:|
| 1 | \(G_+\) | \(A_-\) |
| 2 | \(A_+\) | \(G_-\) |
| 3 | \(G_+\) | \(A_+\) |
| 4 | \(A_-\) | \(G_+\) |
| 5 | \(G_-\) | \(A_-\) |
| 6 | \(A_-\) | \(G_-\) |
| 7 | \(G_-\) | \(A_+\) |
| 8 | \(A_+\) | \(G_+\) |
| 9 | \(G_+\) | \(G_+\) |
| 10 | \(A_+\) | \(A_+\) |
| 11 | \(G_-\) | \(G_-\) |
| 12 | \(A_-\) | \(A_+\) |
| 13 | \(G_-\) | \(G_+\) |
| 14 | \(A_+\) | \(A_-\) |
| 15 | \(G_+\) | \(G_-\) |
| 16 | \(A_-\) | \(A_-\) |

Every element of \(\{A_+,A_-,G_+,G_-\}^2\) occurs exactly once. This proves the sharp seventeen-element upper bound for \(\Phi_4\).

**4. All greater finite cardinalities.** Given either construction on \(m\) vertices, add \(n-m\) fresh vertices at the *end of each of the three orders*, in the same arbitrary order, for any \(n\ge m\). The restrictions of all three total orders to the old vertices are unchanged; crucially, no fresh vertex is inserted between two old consecutive vertices. Each existing reference edge remains a reference edge, and each supplementary adjacency and gap orientation on such a pair is unchanged. Therefore all previously realized profiles persist. This establishes sufficiency for every size above the corresponding minimum and completes the proof of both exact spectra.

## Verification
The standard-library program `checker.py` contains the two complete witnesses as immutable tuples. It independently materializes the strict-order and directed-successor relations, then checks all reference-edge profiles against the atomic definitions, confirms that the two sets of profiles are exactly the respective Cartesian squares, and checks each marginal frequency and all directed-path edge counts. It also explicitly constructs and tests every extended model at sizes ten through one hundred and seventeen through one hundred, respectively; the extension step for all sizes has already been proved in Part 4. Finite test loops do not establish mathematical impossibility at sizes below the minimum; the lower bounds follow from the analytic pigeonhole argument in Part 1. Reproduce with `python3 checker.py`; the expected output begins `VERIFY_OK thresholds=10,17`.

## Relationship to prior work
Jeż, Michaliszyn and Witkowski [1] prove decidability and a general finite-model upper bound for two-variable logic with arbitrarily many independently interpreted successor relations, using local pair masks and path constraints. Michaliszyn and Witkowski [2] give related satisfiability certificates and explicitly analyze the difference between accessible orders and successors. These works motivate the present exact local-profile test but do not assert a ten- or seventeen-vertex minimal simultaneous realization threshold for the two concrete sentences above. The refined language here **does include** the underlying order relations, unlike the signatures in [1] and [2]; no consequence for the general undecidable multiorder satisfiability problem is claimed. Figueira [3] studies the two-successor problem, using local permutation-neighborhood types; it neither supplies these three-path extremizers nor their exact size spectra.

Published work [4] on random independent successor orders classifies asymptotic rank-two limit theories through overlap-presence bits, and [5] enumerates their possible limiting probabilities. Neither a fixed-order sharp finite-spectrum statement nor an order-visible gap-orientation saturation threshold follows by merely matching the random asymptotics. The complete local-signature theorem for independently oriented tournaments [6] has different underlying relations: arbitrary tournaments rather than three constrained spanning directed paths. The bound, witnesses, and extension argument here give exact finite statements that require no asymptotic assumptions.

## Limitations
The theorem is a precise pair of **fixed, quantifier-rank-two finite-spectrum problems** in signatures with three orders; it does not improve general two-variable finite-model bounds, classify all rank-two sentences, address more than three paths, or determine all nonisomorphic optimizers. The seventeen-point case explicitly exposes distant-pair order comparisons, which are absent from pure successor logic; conflating the two signatures would invalidate the statement. The two tiny complete witness tables provide finite certificates, not an independent proof of historical novelty. An equivalent threshold under a different terminology for simultaneous Hamiltonian-path patterns could exist in earlier unindexed combinatorics or model-theory literature. No independent audit or priority certification has been performed.

## References
[1] A. Jeż, J. Michaliszyn and P. Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943v1, first public 2026-10-14, https://arxiv.org/html/2610.19943v1.

[2] J. Michaliszyn and P. Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758v1, first public 2026-10-07, https://arxiv.org/html/2610.09758v1.

[3] D. Figueira, *Satisfiability for two-variable logic with two successor relations on finite linear orders*, arXiv:1204.2495v3, originally 2012, https://arxiv.org/html/1204.2495v3.

[4] *Exact rank-two logical limit types for independent random successor orders*, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-rank-two-logical-limit-types-for-independent-random-succes--a1d5fcd736fe.

[5] *Exact rank-two probability spectra for independent random successor orders*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-rank-two-probability-spectra-for-independent-random-succes--ef51f4ed5442.

[6] *Sharp rank-two logical saturation for independently oriented multitournaments*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-rank-two-logical-saturation-for-independently-oriented-mul--df13150ad5d9.
