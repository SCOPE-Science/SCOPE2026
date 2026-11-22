# Independent mathematical audit

## correctness

PASS

An 11-bit time column u_i encodes the full exact time-return condition of synchronous cyclic Rule 30; the spatial recurrence T(a,b)=(rotate_11(a) XOR(a OR b),a) is reversible as a closed-walk-to-configuration bijection, not a sampled-ring heuristic. A fresh C++17 indegree-peeling implementation on the COMPLETE 2^22=4,194,304 pair-state graph independently found 4,193,883 peeled, 421 recurrent states, precisely one directed cycle each of lengths 1,2,143,275; count checked against supplied traversal. Independent direct Rule30 updates of the two actual bitstrings confirm primitive temporal eleven and primitive spatial lengths 143,275, with Hamming weights 73,137. Prime 11 reduces least-period choices to 1/11, the 1- and 2-length transfer cycles give all fixed states, and division by 11 yields exactly 13 and 25 indexed temporal orbits whenever those spatial periods divide n. This finite exhaustive transfer graph, plus the bijection, legitimately proves every n≥3.

## originality

PASS

PASS best knowledge with explicit historical risk. Wolfram's original 2002 page 268 gives a 275-cell time-11 repeating example and states that 275 cells are required; the actual 143-site word provides a verified smaller fixed-ring exact recurrence, and the all-width closed-walk census is stronger than a single example. A JS-heavy historical Faase catalogue could not be fully inspected; no claim of proof of exclusive historical novelty for the 143 word alone. Published Rule30 one-step preimage and period-twelve results do not imply period-eleven finite cycle counts.

## value

PASS

PASS: the sharp minimum ring circumference for a classic nonlinear cellular automaton's first 11-period recurrence is a motivated exact finite-state classification, not an unmotivated short brute-force table. The 143-site witness corrects a specific prominent 275-cell bound under exact temporal return; the full all-circumference formula and 4,194,304-state certificate make this precise, reproducible and independently useful. It does not purport to classify other temporal periods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
