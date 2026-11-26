# Independent mathematical audit

## correctness

PASS

Independently exhausted all initial states at lengths 1–7 using disjoint excited and refractory bit planes, two rail shifts and a rung swap to compute the synchronous threshold-two update. The small maxima are 2,3,3,4,4,4,5. At time three there are no excitations on lengths ≤6, and on length 7 the only time-three sites are the two middle vertices (108 initial words in each case). Projecting the actual upper words onto single rungs gives exactly the seven frozen sets; the product of their cardinalities is the observed 108, establishing equality with the Cartesian product. Rail swap proves the lower identity, and the second rung has code 3 versus code 1, proving disjointness. A time-three site's radius-three ball either matches the middle or the corresponding end site of the seven-rung graph when n≥7: neighbors outside that ball cannot enter the three-step dependency cone. If an upper target had both rail neighbors excited at time three, the two upper triggers would give conflicting upper states at column j+2 (1 versus 0 or 2). A rail neighbor and the rung neighbor would give conflicting upper states at column j (0 or 2 versus 1). Reflect across the rails for lower targets. Thus E_4 is empty, E_3 survives as refractory at time four, and tau=5 iff a trigger exists; all-rest is absorbing. Any word in a central dependency window can be embedded for sharpness at every larger length. Prefix counts by depth 0–7 are 1,5,6,12,36,72,72,216, yielding the stated 204 proper-prefix states. Longest-prefix-suffix avoidance transitions count exactly the complement, and independent inclusion–exclusion over windows gives 216,3888,52488,629856 at lengths 7–10. A top word has window probability 108/9^7=4/3^11, proving the stated lower bound using independent disjoint windows. Replay: python3 /workspace/evidence/5_ladder.py (NumPy); output /workspace/evidence/5_ladder.txt. Inspected the frozen C++, Python and output; did not execute uploaded scripts. The finite replay certifies the local cone and small maxima, not an extrapolation from sampled large ladders.

## originality

PASS

The same graph at threshold one, a general threshold-two density bound, the separate threshold-two wheel and fan five-update results, and the exact three-row strip ceiling do not give the sharp open two-row clock and the complete seven-rung excitation law. No coverage of that result was found in the checked sources; absolute priority is not certified.

## value

PASS

Eventual extinction was previously accessible from sparsity, but it does not answer whether a longer strip can sustain a longer transient. The common smallest strip width with two-contact activation along both axes yields a sharp size-independent cutoff here. The full local classification, rather than only a late witness, decides which initial data attain the cutoff and gives an exact census and a probability law for labelled random states. Both the locality horizon and the count are useful to researchers comparing transient lifetimes across strip widths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
