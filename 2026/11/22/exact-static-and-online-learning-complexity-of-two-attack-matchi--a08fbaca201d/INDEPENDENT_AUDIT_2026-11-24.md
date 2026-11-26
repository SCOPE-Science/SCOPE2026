# Independent mathematical audit

## correctness

PASS

The original n=4 proof incorrectly says no matching gives exactly two positives on the path ab,bc,cd: matching ad,bc gives 101. The complete replacement proves the right obstruction: the first and last omissions ab and cd are complementary, so their labels always agree on four vertices, and 110 is impossible. It also clarifies that the four positive omissions are a cycle with the matching edges as diagonals, and that three cycle edges identify those diagonals via the path's bipartition. Every unmatched vertex must be included and exactly one endpoint of each matched edge must be omitted, so an all-positive support has a common omission size. This gives the singleton and pair counts (on four vertices only three complementary two-omission pairs fail; for n>=5 a spare vertex allows either individual positive label). Only two-edge hypotheses have three or more positives and three of their four transversal pairs form a P4. All eight trace witnesses with a fifth vertex check directly; any three positives from a full cycle force the fourth. For the online upper bound, a second distinct two-omission query sharing one vertex with the first leaves, in the joint-positive fiber, a fixed edge and a second edge with a single varying endpoint; any further query is constant or true for at most one endpoint. A disjoint second two-omission query leaves at most two hypotheses. Thus no root-positive class can support depth three; zero- and one-omission cases are smaller, and >2 omissions have no positives. For n<=4 no root-positive class can support depth two; the stated small static lower bounds then suffice. Independent bounded check `python3 /tmp/opencode/argument-review.py` used all 2^n queries, endpoint-first matching enumeration and each framework's conflict-free attack-union test, then direct restriction traces and exact bounded splitting for n=1..5. It reproduced the profiles and depths, including exactly 000,010,101,111 for the n=4 path and (1,16,55,60) with depth 3 at n=5. Frozen verify.py was inspected, not executed. The all-order result rests on the repaired argument, not finite tests.

## originality

PASS

The distinct contribution is the exact labeled support enumeration and adaptive dimension for the varying symmetric at-most-two-edge framework class. The same-day functional-attack record counts extension multiplicities, not restriction traces as the framework varies. The closest learning paper is credited and remains a specific access risk; the evidence supports a best-of-current-knowledge verdict for the exact claim rather than a blanket statement about stable-semantics learnability. The repair changes only the validity of the n=4 argument and explanation, not the priority comparison.

## value

PASS

Two disjoint symmetric attacks give the first matching class with interacting omitted-pair queries and static triples. The exact P4 characterization and the four-versus-five-vertex threshold reveal why the size-three traces appear; the positive-fiber obstruction also bounds a genuinely adaptive learner, which static enumeration alone cannot do. This is a useful sharp structural baseline for synthesis or learning with sparse symmetric attacks, not a restatement of the stable-extension definition or a one-instance count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
