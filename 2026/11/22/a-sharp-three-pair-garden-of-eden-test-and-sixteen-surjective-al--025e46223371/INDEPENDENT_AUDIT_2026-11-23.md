# Independent mathematical audit

## correctness

PASS

The corrected finding retains the exact 174/16/8 counts and sharp 4/84/70 shortest-obstruction distribution. For even rings of length at least eight, a bit flip affects four distinct outputs and any six-bit context is available on the eight-ring. These flip equations and the constant-input conditions are necessary there and sufficient on every sufficiently long even ring by starting from zero and inserting the ones one at a time. Repeating any shorter even-ring input to a longer multiple preserves both parity and the local windows, establishing the remaining lengths. Importantly, the frozen line 17's assertion that both rational ranks are 17 is false: the eight-ring system has rank 17/free dimension 15, while the system of flip equations with the four individual constant-bit constraints has rank 19/free dimension 13. An independent exact row reduction gives both ranks and equality of the two Boolean solution sets, with 174 pairs. Path labels in the eight-state graph are precisely finite output pair-words, since the five-symbol input fragments overlap in three symbols. The subset automaton reaches the empty set exactly on an unattainable word; full finite reachability and compactness of nested bilateral preimage constraints prove the surjectivity test at all lengths. Independent exact enumeration confirmed the 16 onto rules and 4/84/70 minimum depths. Mapping coordinates by the eight matching-parity pairs gives local inverse permutations. All other 166 pairs were independently checked against the supplied periodic collision data (80/76/10 witnesses of lengths 2/4/6); periodic repetition makes them full-shift collisions, not obstructions to onto-ness. The repaired RESULT.md corrects the rank assertion and short-ring proof; the repaired check_surj.py removes the unrelated absolute module search path. Replay with those two replacements in a copy of the source directory, keeping the original verify.py and collision_witnesses.json alongside them. Independent replay did not execute the uploaded code. This PASS is for the corrected files, not the frozen rank assertion.

## originality

PASS

Credit is limited to the exact bilateral image classification for the number-conserving alternating four-input subclass: the sixteen onto pairs, the noninjective onto cases, and the sharp three-pair test and histogram. The conservation graph, the general image-language method and the reversible subset are not separately claimed as original. The strongest inspected indexed matches solve different rule classes; the available primary material gives conservation or short finite-block dynamics rather than the exact full-shift census. Repairing the ranks and proof exposition does not create or enlarge the originality claim.

## value

PASS

The short neighborhood and smallest nontrivial spatial period give a natural conserving subclass in which infinite-system onto-ness can be compared directly with reversibility. The exact classification demonstrates that half of the onto rules have collisions, and a witness of at most three even-aligned pairs diagnoses every failure of onto-ness, with three necessary for 70 cases. This sharp finite criterion and structural distinction have independent use beyond a count of conserving assignments. The repair preserves those conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
