# Independent mathematical audit

## correctness

PASS

For a nonempty set of open rungs, an intact exterior top (left) and bottom (right) segment is necessary. Successive open rungs have no working rung between them, so traversing each interior interval requires and suffices to have one intact rail there; all these tests use disjoint edges. The product is therefore p^L times the product of (2-p^d); with no open rungs the terminals are disconnected. Endpoint moves increase some positive-weight term (including the all-open term when q=1) and decrease none. With three rungs the entire position dependence is -q^2(1+q)(p^x+p^(L-x)), giving the center by strict convexity; one rung gives qp^L regardless of location. For four and q=1, strict concavity of log(2-p^d) gives exactly the integer-balanced triples. At fixed 0<q<1 the first-order gap weight is the probability of open rungs on both sides. Its middle-minus-outer difference is q^2(1-q)>0, so the unique first-order maximizer, hence the exact maximizer for p sufficiently near 1 at each fixed L,q, is (1,L-2,1). In the joint scaling, only same-gap two-rail failures and the appropriate adjacent rail failure paired with a failed endpoint rung contribute to order two. These give sum(d^2)+lambda(a+c); no single failure disconnects. Balancing a,c at each b and using the strictly increasing discrete forward differences of Phi proves the threshold 2L-8 and precisely the three stated ties there. This is a leading-order threshold, not a finite-epsilon tie-breaking claim. Read the nested verification/verify_ladder.py; independently ran `python3 /workspace/branches/ladder-review-reproduction.py`: 762 exact successes-by-rail-failure histograms (all placements for k=1..4, L=3..5, each vertical state) and 116 endpoint layouts at L=5..10 with zero, one and two failures agree. The finite test corroborates, not replaces, the proof. The phrase 'perfectly reliable rails' in the limitations should be read as reliable vertices on two rails: the rail bonds have p<1 throughout.

## originality

PASS

The exact reliability method and weighted ladder layout analogies are not new. The checked statements do not provide the discrete change of the optimal installed layout as the Bernoulli rung reliability changes, its minimum rung count, or the joint-scaling quadratic optimizer. The pass is limited to those distinctions and the examined evidence.

## value

PASS

Opposite-terminal reliability at fixed link count is a natural design objective distinct from weighted trees and effective resistance. The smallest number of rungs at which a strictly balanced-versus-clustered change can occur is a meaningful cutoff, and the joint failure calculation explains when the two design effects compete. This is not just another evaluation of a known ladder reliability polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
