# Scientific review: laminar-support distinctive representation

## Correctness — PASS

The result is one precise classification plus its counting and sampling consequences. DR uses the exact source definition: selected supporter-set sizes equal \(q=\lceil n/k\rceil\), and every sufficiently large cohesive group has at least one represented voter. The residual form of JR is an if-and-only-if statement. Pairwise laminar and equal-cardinality quota supports are either identical or disjoint. Omission of an entire quota class leaves its \(q\) voters unrepresented, so each class is mandatory. Conversely, all classes together have an invariant union \(U\), and the original JR constraints become \(|S_c\setminus U|<q\). The bounds \(r\le\lfloor n/q\rfloor\le k\), \(M\ge k\), and the nonempty-subset generating functions complete the sufficiency and count. The asymptotic uses \(\binom{2k}{k}\sim4^k/\sqrt{\pi k}\). A standalone exact checker passed 134,760 independent finite count comparisons. No finite test is used as proof of the infinite theorem.

## Originality — PASS, with priority risk

The fully inspected relevant portions of Chingoma et al. (arXiv:2609.29332v2, sections 2, 6–7, Appendices D–E) introduce general DR and hardness and define local DR, but do not classify laminar candidate support sets or their exact DR committee multiplicities. Elkind et al. (arXiv:2108.12949, sections 2–4) optimize unrestricted JR-justifying groups under a candidate-tree representation; that neither restricts eligible candidates to exactly the Hare quota nor counts DR committees. Earlier JR work establishes existence without this fine structure. Targeted current literature and research-record searches found no dominating or equivalent statement; record searches returned only substantively different voting-rule classification and counting results. The exact condition may admit an elementary independent rediscovery, and inaccessible or unindexed literature could alter priority.

## Value — PASS

This is a full, natural classification of a newly proposed exact-support diversity axiom on hierarchical electorates, not a selected numerical test. The important structural conclusion is that all feasible committees cover the same precise electorate; the polynomial-time feasibility/counting algorithm converts an NP-complete general decision setting into an exact tractable subclass; and the exponential-rarity family shows why unguided committee sampling can be poor despite easy existence. The nonlaminar example identifies a real boundary of the rigidity phenomenon. The result is relevant to hierarchical voter groups and to computing precise diversity-constrained committee lotteries. No downstream theorem or independent external validation is claimed.

## Closest literature and limitations

See RESULT.md References 1–3 and AUDIT.json for the search comparisons. The key differences are quota-exact DR versus unrestricted JR, laminar supporter sets versus the distinct laminar-proportionality axiom, and exact counting versus general optimization of a single JR group. The theorem does not extend to arbitrary voter-interval or general approval profiles. Publication priority remains qualified.

Self-review: passed. Independent audit: not yet performed.
