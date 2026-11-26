# Independent mathematical audit

## correctness

PASS

With x₀=0 the edge XOR word determines x uniquely; even parity is necessary and sufficient for closing the ring. A site flips iff both incident edges are 1 and the site is not pinned. XOR of the two endpoint flips with an edge bit shows that a zero never turns on, and that an edge currently 1 turns off exactly when it has just one neighboring 1 in the linear word (virtual zeros at the two ends). Thus both edges of any run of length ≥2 are removed at once, and singleton runs are fixed. This proves that the first fixed time is the largest floor(run length/2), and proves absence of cycles, with the empty-run maximum interpreted as zero. The parity-projected series follows by splitting at zero walls: one capped initial run, then any number of zero-plus-capped-run blocks. The coefficients at n<3 describe formal words; no physical boundary convention there is required. At time floor(n/2) the extremizers are exactly the even all-one word, or the two end-positioned length-(n−1) runs at odd n. The all-zero attractor requires every run length even; these words tile uniquely by 0 and 11, so the Fibonacci recurrence and its initial values follow directly. Division by the 2^(n−1) indexed starts and Binet's identity give the claimed asymptotic. Independent replay /tmp/opencode/frozen_majority_replay.py exhausts lengths 3–16 using bitwise open-string majority, checks each start's time and basin membership, and compares all cumulative counts to a parity/terminal-run-state automaton. At n=8 it gives [27,77,20,3,1] and basin 34; at n=16 [1292,18532,9900,2404,512,104,20,3,1] and basin 1597. The uploaded source and output were inspected without executing them. The unbounded conclusions use run erosion and exact formal-language counting, not the replay.

## originality

PASS

Qualified for the pinned all-time and consensus-basin counts, not the known same-model absence of nontrivial cycles, fixed-point enumeration or worst transient time. The model is exactly the open dynamic string with two fixed zero boundary values, not just analogous to it. Access limits for the 2000 full text are recorded below.

## value

PASS

Worst-case time and fixed-state totals do not answer how often a single immutable opinion wins or how quickly typical starting states freeze. These two natural exact invariants are given uniformly over sizes and times; in particular, certain fixation coexists with exponentially vanishing consensus probability. The value is the two exact pinned invariants, not a new local rule or arbitrary extracted slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
