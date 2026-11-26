# Independent mathematical audit

## correctness

PASS

The degree of a vertex in part i is N-a_i. A singleton gives strong domination number 1; a unique nonsingleton minimum forces and suffices with its entire part; tied nonsingleton minima give number 2 by selecting from two minimum parts. These rules give exactly the stated minimum deletion sets. In particular at repeated minimum 3, one deletion preserves 2, and two deletions preserve 2 unless they create a singleton by occurring in the same size-three part; a newly created unique minimum of size two still has number 2. If singleton parts exist, every one must be deleted and doing so suffices, including the complete graph under the empty-graph convention. The witness counts follow by counting the classified vertices or pairs. Independently built adjacency masks, obtained degrees from those masks, evaluated the domination predicate by subset enumeration, and checked every individual deletion through the claimed minimum on all 183 multipartite profiles through order 11 (36,315 deletion sets), plus (4,4,4). All matched, including 9 optimum pairs in (3,3,3) and 12 optimum singletons in (4,4,4). Replay: node /workspace/branches/independent-checks.js (record 5 block). The frozen verifier and archived log were inspected, not executed; finite checks supplement the proof.

## originality

FAIL

The scalar theorem is already stated for the noncomplete domain in a distinct earlier-dated catalog entry, and the full minimum-set classification on that domain is also explicitly covered in a distinct later-dated indexed entry. This is statement coverage, not a claim that the later-dated entry had priority. The count W is a direct count from that classification, and the only extra case is the complete graph, where under the stipulated convention the whole vertex set is the only deletion that changes the number. There is no substantive distinct remainder to retain.

## value

PASS

The complete classification of optimum vertex-deletion witnesses is structurally useful in its own right, especially the change from singleton witnesses to same-part pairs at repeated minimum three. It also gives small explicit corrections to published balanced-case values. This scientific utility does not cure the originality failure; the uncovered complete-graph endpoint on its own would not justify a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
