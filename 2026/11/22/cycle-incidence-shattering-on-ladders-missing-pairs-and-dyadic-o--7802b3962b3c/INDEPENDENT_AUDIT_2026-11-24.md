# Independent mathematical audit

## correctness

PASS

The frozen proof asserted that the top and bottom portions of a cycle each form a single path; its appeal to revisiting a row does not justify this central step. The complete corrected /workspace/repairs/3/RESULT.md proves the unchanged theorem: take the extreme columns of a simple cycle; every intermediate two-rail cut must be crossed by connectedness and crossed evenly by the cycle degree sum. Both rails therefore occur across every intermediate gap. Degree two excludes interior rungs and forces the two extreme ones. From this representation, any two distinct rung queries admit all traces for n>=4. For tracks in different gaps, two columns in one of the three complementary blocks realize the zero trace (by pigeonhole), and the single-gap and full rectangles realize the other traces. A mixed pair admits both singletons exactly when the selected rung's side of the gap has a second column; removing that rung's column leaves two columns on some side for the zero trace. This excludes the same-gap twins and the four extreme mixed pairs and gives the stated coefficient. With three rungs the all-positive trace fails; two rungs force one rectangle, one rung makes two distinct rail answers nested or exclusive conditional on that rung, and three distinct rail gaps cannot give a 101 trace. The cases n=2 and 3 follow from cycle count and singleton variation. Distinct concepts per adaptive leaf give the information bound; two independent threshold searches on disjoint blocks of m=floor(n/2) endpoints prove the lower bound, which equals the upper bound at dyadic n. The checked depth-three tree at n=5 embeds at all larger n. Reviewer-authored `python3 /workspace/independent_reproduction.py ladder` enumerated graph cycles for n=2..9, checked 6,910 supports through triples, reproduced all ranks through n=12 by finite adaptive recursion, and checked the actual certificate's eight leaves. This corroborates, not replaces, the all-order proof in the repaired file.

## originality

PASS

For the unchanged repaired statement, checked earlier wheel and complete-bipartite results establish analogous edge-cycle rank phenomena, and finite-interval methods already explain the rail-only online lower bounds. The full physical-edge ladder support classification, including endpoints and duplicate gap predicates, was not found as a covered result. The online conclusions are credited as applications of classical threshold and counting arguments; the combined ladder classification is the distinct claim.

## value

PASS

The corrected proof establishes a complete shattering census on distinct physical edges of a standard connected subcubic planar graph, and gives exact infinite dyadic adaptive ranks as well as the first strict-gap boundary. The count detects duplicate and extreme coordinate effects hidden by VC dimension alone. The bounded-degree planar example complements, rather than restates, wheel-based separations and is not a claim about all non-dyadic ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
