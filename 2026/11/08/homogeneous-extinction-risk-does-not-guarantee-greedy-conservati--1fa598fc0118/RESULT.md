# Homogeneous extinction risk does not guarantee greedy conservation priority: the sharp four-taxon boundary

## Finding

Consider the equal-cost selection of a fixed number of phylogenetic taxa for independent conservation interventions, with expected **rooted** phylogenetic diversity as the objective. Each intervention strictly increases its taxon's survival probability but need not make survival certain. At most three taxa, the sequential marginal-gain greedy rule is optimal for every set of baseline survival probabilities, every set of improved survival probabilities, and every positive set of branch lengths. This holds for every permitted budget.

Four taxa suffice for failure, **even when every unprotected taxon has identical survival probability** \(1/2\), and even when every intervention increases survival strictly and leaves strictly positive extinction risk. An explicit four-taxon rooted binary tree and two-taxon budget give a unique greedy choice \(\{b,c\}\) of expected phylogenetic-diversity gain \(129/25\), while the unique optimum \(\{b,d\}\) has gain \(269/50\). The exact gap is \(11/50\). Thus four taxa are the sharp minimum for failure under homogeneous unprotected survival probability in this model.

## Assumptions and scope

A finite rooted phylogenetic tree has positive edge lengths, at least two children at its root when at least two leaves are present, and no stem edge above the root. Degree-one interior vertices may be suppressed by combining incident lengths. Each edge \(e\) has length \(\ell_e>0\) and a nonempty descendant leaf set \(C_e\). With the root included, the phylogenetic diversity of surviving taxa \(U\) is \(\operatorname{PD}(U)=\sum_{e:C_e\cap U\ne\varnothing}\ell_e\).

Taxa survive independently. Before intervention, taxon \(i\) has extinction probability \(q_i\in(0,1)\). An equal-cost intervention on taxon \(i\) replaces this with \(q_i'\in(0,q_i)\), independently of interventions on other taxa. Exactly \(k\) different taxa are selected, with \(0\le k\le n\). The greedy rule starts at the empty set and repeatedly selects an unselected taxon giving the largest increase in expected phylogenetic diversity. Ties can be resolved arbitrarily. The theorem concerns full interventions on selected taxa, not continuous fractional spending, varying costs, correlated extinctions, or unrooted diversity.

Write \(F(S)=\mathbb E[\operatorname{PD}(U_S)]-\mathbb E[\operatorname{PD}(U_\varnothing)]\), where \(U_S\) is the random survivor set when exactly taxa \(S\) are treated. Independence gives the exact identity

\[
F(S)=\sum_e\ell_e\left[\prod_{i\in C_e}q_i-\prod_{i\in C_e}\big(q_i'\mathbf 1_{\{i\in S\}}+q_i\mathbf 1_{\{i\notin S\}}\big)\right].
\]

## Proof

**The lower bound.** For one or two leaves all root-to-leaf branches are disjoint, and \(F\) is additive. Greedy is optimal. At three leaves, a reduced rooted tree either has a three-leaf root star or has one two-leaf clade, say \(\{b,c\}\), with the other leaf \(a\) attached directly to the root. No edge can have all three taxa below it, because there is no root stem. Hence every leaf-set interaction is confined to the pair \(b,c\). In the star case the objective is additive. In the cherry case, put \(A=F(\{a\})\), \(B=F(\{b\})\), \(C=F(\{c\})\). For every set \(S\),

\[
F(S)=A\mathbf 1_{\{a\in S\}}+B\mathbf 1_{\{b\in S\}}+C\mathbf 1_{\{c\in S\}}-T\mathbf 1_{\{b,c\subseteq S\}},
\]

where \(T\ge0\) is the sum over edges with clade \(\{b,c\}\) of \(\ell_e(q_b-q_b')(q_c-q_c')\). In particular the three pair gains are \(A+B\), \(A+C\), and \(B+C-T\).

Only the two-taxon budget is nontrivial. If greedy first chooses \(a\), then \(A\ge\max(B,C)\), and the better of the pairs containing \(a\) is at least \(B+C\ge B+C-T\). If it first chooses \(b\), then \(B\ge\max(A,C)\). If it next chooses \(a\), the greedy comparison gives \(A\ge C-T\), so \(A+B\ge B+C-T\), and \(B\ge C\) gives \(A+B\ge A+C\). If it next chooses \(c\), the greedy comparison gives \(C-T\ge A\), so \(B+C-T\ge A+B\), while \(B\ge C\ge A+T\) gives \(B+C-T\ge A+C\). The case where it first chooses \(c\) is symmetric. Every greedy pair is therefore optimal, including under ties. Budgets zero, one and three are trivial.

**The strict four-taxon witness.** Use the rooted binary tree \((a,(b,(c,d)))\). The six edge lengths, specified by descendant clade, are

| Descendant clade | \(\{a\}\) | \(\{b\}\) | \(\{c\}\) | \(\{d\}\) | \(\{c,d\}\) | \(\{b,c,d\}\) |
|---|---:|---:|---:|---:|---:|---:|
| Length | 3 | 5 | 2 | 9 | 7 | 8 |

Each baseline extinction probability is \(1/2\). After intervention the extinction probabilities for \((a,b,c,d)\) respectively are \((1/5,1/10,1/10,3/10)\). All are strictly between zero and the common baseline. Substitution into the exact edge formula yields:

| Protected set | Exact gain |
|---|---:|
| \(\{a\}\) | \(9/10\) |
| \(\{b\}\) | \(14/5\) |
| \(\{c\}\) | \(3\) |
| \(\{d\}\) | \(29/10\) |
| \(\{a,b\}\) | \(37/10\) |
| \(\{a,c\}\) | \(39/10\) |
| \(\{a,d\}\) | \(19/5\) |
| \(\{b,c\}\) | \(129/25\) |
| \(\{b,d\}\) | \(269/50\) |
| \(\{c,d\}\) | \(251/50\) |

The unique highest singleton is \(c\), and conditional on that choice the unique best second selection is \(b\). The globally best pair is uniquely \(\{b,d\}\). The greedy shortfall equals \(269/50-129/25=11/50>0\). Combining this witness with the universal three-taxon proof gives the sharp cutoff.

## Verification

Run `python3 check.py` with Python 3 and no third-party dependencies. The script uses exact rational arithmetic to calculate all singleton and pair gains both from the edge-survival product identity and from independent enumeration of the 16 possible survivor sets, checking agreement for all 16 intervention subsets. It then checks uniqueness of the greedy selection and of the optimal two-taxon set, and confirms the exact gap. The universal small-tree argument is mathematical, not inferred from finite enumeration.

## Relationship to prior work

Hartmann and Steel (2006) already prove exact greedy optimality for the Noah's Ark problem when all selected taxa receive the same multiplicative reduction in extinction probability (their Theorem 1), and already exhibit a **four-taxon** non-greedy example with **nonidentical** initial survival probabilities (their Figure 2). Neither generic greedy failure nor their theorem is new here. The restriction established by the present witness is that all **unprotected** taxa can instead have exactly the same initial risk, with heterogeneous efficacy alone causing the failure; the accompanying lower bound rules out smaller trees for all efficacy parameters. The previously published example does not logically establish this homogeneous-baseline restriction.

Steel, Mimoto and Mooers (2007) derive the rooted expected-marginal phylogenetic-diversity formula, which is used here. The later analysis by Billionnet (2018; preprint 2022) explicitly assumes **certain survival** following protection, so it does not cover the imperfect-intervention witness. This result does not claim an algorithmic complexity breakthrough, nor does it replace the broader conservation framework of Hartmann and Steel.

## Limitations

This result isolates a theoretical mechanism. It does not predict ecological survival rates or intervention success in any real reserve. Its four-leaf instance has unequal branch lengths and unequal conditional intervention success, and it does not identify the smallest failure under additional ultrametric or equal-edge-length restrictions. It does not assert that the homogeneous-baseline counterexample is absent from all historical publications; the inspected literature establishes closely related general failures, and historical-priority uncertainty remains. A full-text comparison with Moulton, Semple and Steel (2007) was unavailable, although the directly relevant Hartmann and Steel (2006) primary full text was inspected.

## References

1. Hartmann, K. and Steel, M. (2006), *Maximizing phylogenetic diversity in biodiversity conservation: Greedy solutions to the Noah's Ark problem*. Systematic Biology 55(4), 644–651. https://doi.org/10.1080/10635150600873876 . Lawful author manuscript: https://www.math.canterbury.ac.nz/~m.steel/Non_UC/files/research/noah.pdf . First published 1 August 2006.
2. Steel, M., Mimoto, A. and Mooers, A. Ø. (2007), *Hedging our bets: the expected contribution of species to future phylogenetic diversity*. arXiv:0704.2649, first public 20 April 2007. https://arxiv.org/html/0704.2649v1 .
3. Moulton, V., Semple, C. and Steel, M. (2007), *Optimizing phylogenetic diversity under constraints*. J. Theor. Biol. 246, 186–194. https://doi.org/10.1016/j.jtbi.2006.12.021 .
4. Billionnet, A. (2018), *Quantifying extinction probabilities of endangered species for phylogenetic conservation prioritization may not be as sensitive as might be feared*. Biodiversity and Conservation 27, 829–844. Later open version: https://arxiv.org/pdf/2203.12278 .
5. Bennett, J. R. et al. (2014), *Balancing phylogenetic diversity and species numbers in conservation prioritization*. Biological Conservation 174, 47–54. https://doi.org/10.1016/j.biocon.2014.03.013 .
