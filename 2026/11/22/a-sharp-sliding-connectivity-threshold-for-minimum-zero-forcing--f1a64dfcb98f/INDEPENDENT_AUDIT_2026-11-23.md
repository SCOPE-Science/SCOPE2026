# Independent mathematical audit

## correctness

PASS

Four or more whites preclude any first force since a blue vertex misses at most two whites in the path complement. For exactly three whites, a first force exists precisely when they include a pair a,a+2 about a blue center. After it, one of a−1,a+3 exists and can force one of the last two whites, and the complement has positive minimum degree for the final force. Counting witnesses and subtracting the n−4 double-witness triples gives (n−3)²+1. Every transition has a unique common white pair, so the completion-set binomial counts are disjoint. To replay the grouped counts for separation d≥3, write k=n−d: the two inward labels are always present and coincide only for d=4; each outward label occurs in max(0,k−2) completions sets indexed by the shared pair, and both occur jointly in max(0,k−4). Thus the unrestricted group count is k+4max(0,k−2)+max(0,k−4) for d=3 or d≥5 and 2max(0,k−2)+max(0,k−4) for d=4. Together with d=1 and 2 in the completion table this reproduces the unrestricted cubic. Consecutive completions at d=2 survive in the two intervals outside the three omitted labels; d=3 and 5 each give one consecutive pair per shared pair, with no other losses, yielding n²−5n+4 prohibited moves. For n≥7, connected fibres follow because a disconnected complement of an induced linear forest with at least four vertices would give a star with three leaves or a K₂,₂ cut. Overlap links each parity; 023↔035 joins them. At n=6 the isolated positions of the two endpoint fibres are absorbed by the overlapping connected fibres. At n=5 the unrestricted cycle is 013–023–024–124–134–013 and only 134↔013 is a slide. A separate finite enumeration using single forces and all state pairs for n=5 through 14 agreed in counts and slide component sizes, including (21 exchanges, 11 slides) at n=6. The all-order replay is RESULT.md Lemmas 1–3; the supplied scripts were inspected but not executed, and finite enumeration alone is not the proof.

## originality

PASS

Best-of-knowledge pass limited to relocation connectivity, the slide-only n=5 exception, and exact edge counts. Prior work supplies both the scalar minimum and the full minimum-state criterion, not just the number of states. The supplied criterion plus the move rule determines the graphs, but the checked earlier results do not mechanically give their connectedness or the all-order closed forms. A distinct same-day result concerns cycle complements and has a different exceptional regime; no priority inference is made from its date.

## value

PASS

Minimum-state reachability by graph-local moves is a natural question in zero-forcing reconfiguration. Three isolated optimum states at n=5 become part of a single connected space from n=6 onward even though the unrestricted graph is already connected at n=5. The fibre proof gives usable reachability structure. The exact edge formulas independently quantify the loss from restricting moves: quadratic lost edges out of cubic exchange edges, rather than just an unquantified connectivity comparison. These results go beyond reproducing a known minimum-set count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
