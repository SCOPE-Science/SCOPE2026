# Independent mathematical audit

## correctness

PASS

Fixing the first bit on a retained path determines the rest. Two binary preimages have alternating differences +1,-1, so both occur exactly for the all-one reading (empty for a singleton); this gives one doubleton and 2^v-2 singleton readings. Disjoint paths give independent Cartesian factors, proving the spectrum, maximal list, and image-size capacity. For a_v=2^v-1, a_(v+1)^2-a_v a_(v+2)=2^v>0. Strict ratio monotonicity proves that every unbalanced pair can be improved by balancing, and that moving one vertex from a smaller part at least two to a larger part strictly decreases capacity until at most one nonsingleton remains. All compositions are realizable. Marking one erased edge gives n anchored compositions per ordered type and e representations of each mask, yielding the stated generating function. A singleton fiber exists exactly when every gap is at least two. Marked positive gaps after subtracting one from each count these masks; for e=O(sqrt(n)) the log product is -e^2/n+O(e/n+e^3/n^2), while for sqrt(n)<<e<=n/2 the probability is at most 2 exp(-e^2/n), and it is zero beyond n/2. The all-erased mask has empty observation and one fiber of size 2^n. Independent replay: python3 -I -B /workspace/reproduce.py 4 checked 2032 masks and 1396040 source instances by packed observations, including both extremal equality tests and coefficient extraction; it also covered e=1 as a check, not as new scope. The uploaded script was inspected only. The n=100..6400 illustration in RESULT.md is not part of that uploaded script's output; the limit rests on the analytic proof.

## originality

PASS

The single-path ambiguity is known, and the exact one-erasure result covers that boundary. Multiplying the old local factors is straightforward once the surviving components are identified, and the random-mask exponent is a classical no-adjacency phenomenon once translated. The distinct claim is the combined exact arbitrary-mask classification with sharp placement conditions and aggregate list census for known cyclic pair-sum erasures. None of the inspected sources supplies that classification as stated or through a direct parameter substitution.

## value

PASS

Mask geometry, not merely the number of reads remaining, changes the entire list spectrum and the optimal zero-error image size. The strict placement classification gives a concrete design and worst-case guarantee, and the generating function quantifies ambiguity across all placements. The random result locates loss of the existence of any uniquely decoded output, not source-average decoding success. These are natural exact invariants of a simple erasure model; the value is in their combination and mask dependence, not in the already known path lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
