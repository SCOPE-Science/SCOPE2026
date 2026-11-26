# Independent mathematical audit

## correctness

PASS

The cyclic homogeneous recurrence forces period three and even parity on each triplet. If 3 does not divide n, periodicity forces constancy and the only constant kernel word is zero. At n=1,2 the full repeated-neighbor XORs give the identity, as required. At n=3m the four-word kernel has three shifts, each supported on 2m sites. One shift preserves source weight iff its support carries m ones, giving the pair count with orientation divisor 2. Two distinct shifts impose two pairwise class sums equal to m, hence class counts (2m-w,w-m,w-m) in a suitable order; the three choices of shift pair cancel the three anchors per unordered triple. Three shifts preserve weight iff each class has m/2 ones, with four anchors and exactly the stated even-m central condition. All other unindexed outputs or empty intersections are excluded as in the definition. These are the binomial moments of the nonempty fiber-size counts, so inversion and alternating inclusion-exclusion give the complete histogram and one-representative-per-output capacity. The positive pair moment is exactly on [m,2m]; at the center the triple moment equals four times the fourth moment, whereas away from center a positive triple moment is a genuine size-three fiber. Independent tuple-based direct enumeration matched all 135 (n,w) slices for n=1..15, totaling 65534 binary inputs; replay python3 /workspace/independent_checks.py 3. The supplied CHECK.py was inspected, not executed; neither finite test is an all-length proof.

## originality

PASS

The reversible-length split, period-three kernel and abstract coset or binomial-moment framework are not new. The supported distinct contribution is the evaluated full indexed, fixed-source-weight census in the singular lengths, including its exact layer injectivity and three-versus-four ambiguity regimes. Compared sources do not give that census as a special case; this assessment is bounded, not a historical priority guarantee.

## value

PASS

A weight-known source layer is a natural decoding regime. The full histogram gives both operational codebook size and exactly how many indexed readouts have each ambiguity size, exposing a sharp weight-dependent transition not visible from an unrestricted rank or kernel bound. The uniform all-length formula addresses a precise reconstruction question rather than adding a few table entries or restating reversible CA theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
