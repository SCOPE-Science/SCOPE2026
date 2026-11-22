# Review: six projective line-intersection profiles of maximum legal coverings

## Correctness
PASS. The point–line model uses the explicitly presented field \(\mathbb F_4\). Both independent implementations check 21 normalized points, 21 lines, degree five, and unique intersections between every two lines, then exhaust every one of the \(2^{21}\) candidate point subsets. The reverse deletion recurrence and forward addition recurrence count legal orders, excluding eleven-vertex supports and agreeing on exactly 140,448 ten-point supports, 36,288,000,000 orders and all six signature populations. A ten-step coordinate witness independently checks the attained bound; shore independence and binomial shuffles establish the graph-level figures. No larger-order generalization is inferred from finite checking.

## Originality
PASS, subject to residual priority uncertainty. Brešar et al. (2014) introduced legal covering sequences. Brešar–Henning–Rall (2016, arXiv:1601.07525), Theorem 8.4, establish the incidence-graph conversion, not the exact quaternary-plane covering number or counts. Gologranc–Jakovac–Kos–Marc (2019, arXiv:1906.12235) treat a different graph constructed using projective-plane incidence complements. The closest indexed Grundy-total-domination findings concern book graphs and rook graphs, whereas an indexed quaternary-plane cap-complex finding addresses a different invariant. Source statements and implications, not title coincidence, were compared. The searchable literature and accessible prior claims showed no subsuming exact enumeration, but unindexed prior computations cannot be ruled out.

## Value
PASS. The quaternary projective plane is the first Desarguesian projective plane over a proper extension of the prime field. Its 21-point/21-line configuration is a natural design benchmark for greedy-versus-minimum covering length; the length-ten maximum contrasts with the minimum five-point cover. The six exact intersection types and separation into 56,448 whole-line versus 84,000 proper blocking configurations expose geometric structure rather than an arbitrarily chosen parameter value. The product/shuffle identities give a complete 42-vertex graph-level extremal census.

## Scientific limits
This work does not classify automorphism orbits or quantify other projective-plane orders; no full exhaustive historical publication guarantee is possible. The 2016 and 2014 foundations are credited explicitly. Verification is reproducible with standard Python 3 and C++17, and no independent scholarly audit has been performed.

Self-review: passed. Independent audit: not yet performed.
