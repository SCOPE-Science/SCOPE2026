# Independent mathematical audit

## correctness

PASS

The undirected modulo-three edge rule gives 24 distinct vertices and four neighbors per vertex. Nonempty, distinct closed-neighborhood intersections are exactly the domination and symmetric-difference hitting conditions; adding any sensor preserves them. An independent signature-based enumeration (not a run of the frozen verifiers) covered all 735471 eight-subsets and 1307504 nine-subsets, finding zero and 48 respectively. Monotonicity then rules out all smaller subsets; every returned nine-set is minimum. The 48 sets in the census agree with the actual frozen OPTIMA.txt. The mask 0x901669 decodes to the nine stated stage/address pairs and has stage profile (4,3,2). Translation preserves the flip indices, rotation sends the flip at stage i to that at i+k, and the reflection of the stage pair (i,i+1) has outgoing stage 2-i and flips bit 2-i. These maps form the group of eight translations extended by the six rotations/reflections of the stage triangle. The replay checked all 27648 ordered-pair/map tests and verified that the representative orbit is the census; its size is 48, so the action is free and transitive. Each stage profile permutation occurs eight times. No determination of the full graph automorphism group is needed. UTC replay on 2026-11-24: /workspace/branches/144062aa-650b-4b97-986d-bf5a4186d99e/audit_b3.py, audit_result.json, size8_complete.json and size9_complete.json.

## originality

PASS

The supported distinction is the exact first cyclic degree-four butterfly census, including one free orbit of all 48 labeled minima and its stage profiles. The definition, lower bound 8 and analogous code investigations on other graphs are prior work. The comparison is bounded, not a first-priority certification.

## value

PASS

Three is the smallest stage count in this degree-four cyclic family, where the known upper construction does not apply. The exact gap above the general lower bound is useful as a benchmark for identifying codes on the correct wrapped topology. The complete placement census and single free orbit are stronger than one optimum and answer whether genuinely different minimum sensor patterns occur. This is a natural finite boundary case, not an arbitrary parameter cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
