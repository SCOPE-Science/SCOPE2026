# Independent mathematical audit

## correctness

PASS

An ordered table of six three-bit rows gives exactly 512² distinct automata per fixed endpoint pair. State relabeling preserves the three statistics and gives weights 3 for coincident endpoints and 6 for distinct ones. Subset closure starts at the initial singleton and retains the empty rejecting sink if reached. Refinement by acceptance and ordered successor classes exactly tests equality on words of increasing length, and at its fixed point gives the complete minimal DFA. The union of reached subsets and reverse closure from the final state are respectively accessibility and coaccessibility on original states. An independent complete run on the 524,288 representative cases reproduced all 62 nonzero CSV rows, with trim totals 190,080 and 209,664 and labeled totals 2,359,296 overall and 1,828,224 trim. The only trim cell attaining R−M=5 is (7,2), with 3×216+6×178=1,716 cases. Conditional on trim and R=8, the minimum M is 4, with 3×192+6×116=1,272 cases. The all-R=8, trim-R=8 and all-(8,8) counts were also confirmed (15,660, 15,036 and 8,244).

## originality

PASS

The distinct supported result is the labeled joint distribution of reachable subset count and minimal complete DFA size with the trim and endpoint refinements. The closest checked sources give a different-dimensional threshold enumeration, attainable sizes, complexity measures or empirical compression, not that joint distribution or the conditional trim extremal counts.

## value

PASS

The natural smallest nontrivial binary powerset model is a complete calibrated benchmark for intermediate state blow-up versus final compressed size. Counting those quantities jointly, rather than just attaining each individually, exposes a concrete tradeoff: in trim automata the maximal additive loss occurs before full powerset reachability, and at full reachability the quotient cannot have fewer than four states. The exact frequencies distinguish these structural and typical-case questions from existence bounds and are useful for calibrating determinization and reduction experiments. The result is narrowly finite, with no implied general performance theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
