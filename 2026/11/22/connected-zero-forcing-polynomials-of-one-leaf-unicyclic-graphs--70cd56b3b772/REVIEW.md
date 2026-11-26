# Independent mathematical audit

## correctness

PASS

Each off-cycle rooted tree contributes at least one leaf, and branching contributes more, proving the graph identification. Initial connectedness and two white directions require a cycle interval of size at least two and permit a nonempty tail prefix only when it includes the hub in its cycle interval. If the hub is omitted, force along both sides of the unseeded arc and color the hub last on the cycle; otherwise use a nonhub cycle boundary. Finish the tail. There are q of the c proper q-intervals containing the hub. The convolution-difference calculation gives a positive difference k-b_(k-t) through k=c-2, and nonpositive -b_(k-t) thereafter. The c=3,4 and t=1 positive cases check directly; the first internal determinant 4-c is negative in the complementary region. Independent replay: python3 /workspace/review_checks.py 5; 55 graphs of order <=13, 147417 nonempty masks per pass, via hitting every minimal fort and testing induced connectivity; arithmetic checks on 840 cases with 3<=c<=30, 1<=t<=30. Proof, not finite enumeration, supplies unrestricted shape.

## originality

PASS

For the repaired coefficient-shape claim only. Existing cycle constraints, the known minimum and the matching t=1 enumerator are explicitly credited. The inspected results do not give the uniform unimodality and precise log-concavity split for all pendant-path lengths in the one-path class. Priority is bounded by the inspected evidence.

## value

PASS

This is the complete one-leaf unicyclic stratum. It gives a family of positive unimodal but non-log-concave count sequences with the first failure caused by the second tail vertex precisely for cycles of length >=5, along with an exact small-cycle boundary. The numerical adjacent-coefficient behavior is useful separately from the previously known minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
