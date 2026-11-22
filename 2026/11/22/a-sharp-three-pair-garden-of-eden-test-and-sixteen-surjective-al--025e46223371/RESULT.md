# A sharp three-pair Garden-of-Eden test and sixteen surjective alternating number-conserving automata

## Finding

Among all binary one-dimensional cellular automata which apply a 16-bit rule \(f\) at even sites and a 16-bit rule \(g\) at odd sites, with four consecutive inputs per site, exactly 174 ordered rule pairs preserve the number of ones on every even periodic ring. Exactly 16 of these are globally surjective on \(\{0,1\}^{\mathbb Z}\). Exactly eight are reversible, while **the other eight are surjective but noninjective**. The remaining 158 maps have unattainable even-aligned output blocks of at most three consecutive two-cell symbols; the sharp shortest-obstruction distribution is 4 at length one, 84 at length two, and 70 at length three.

## Assumptions and scope

For every indexed bi-infinite binary configuration \(x\), put
\[
 (Fx)_i = r_{i\bmod 2}(x_{i-1},x_i,x_{i+1},x_{i+2}),\qquad r_0=f,\quad r_1=g.
\]
A rule number \(r\in\{0,\ldots,65535\}\) is encoded so that \(r(a,b,c,d)\) equals bit number \(8a+4b+2c+d\) of the binary expansion of \(r\), with bit zero the least significant bit. We require that on every even cyclic ring, the output contains exactly as many ones as the input. Global surjectivity and injectivity refer to the entire bilateral full shift, **not** to finite-ring maps; periodic collisions certify noninjectivity but do not disprove surjectivity.

## Proof

**Conservation census.** At any even length, the output-sum functional is the sum of local contributions. Changing one input bit changes exactly four output contributions: two governed by \(f\), two by \(g\). The condition that every one-bit change in a cyclic input changes the total output count by exactly one is therefore an explicit affine linear system in the 32 truth-table bits, obtained by ranging over both site parities and all six-bit neighboring contexts. Together with the constant-input conditions, it is sufficient for conservation on every even ring by sequentially flipping the ones of any input from the all-zero input. Conversely, conservation on every even ring implies all these equations. The standalone `verify.py` constructs this system independently of the direct 256 input equations for the eight-cell ring; both have exact rational rank 17 and yield exactly the same 174 Boolean solutions out of 15 affine free bits. Necessity of the six-bit equations already follows from the eight-cell ring: the affected four outputs are distinct, and all six context bits can be assigned arbitrarily.

**Image automaton.** Group consecutive output coordinates \((2j,2j+1)\) as letters of \(\Sigma=\{00,01,10,11\}\). Construct an eight-state labeled graph with states the binary input triples \(abc\), edges \(abc\to cde\) for every choice of \(d,e\in\{0,1\}\), and edge label
\[
 \bigl(f(a,b,c,d),\,g(b,c,d,e)\bigr).
\]
Any finite even-aligned output-pair word is realizable if and only if it labels a path in this graph. Starting from the subset of all eight states, for each letter advance the subset by the union of all matching labeled successors. The empty subset is reached exactly for an unattainable word. This is an exact finite-state equivalence for *all* lengths; if the empty subset is unreachable, every finite output word is attainable, and compactness of the full shift proves global surjectivity for arbitrary bilateral output configurations.

The accompanying `check_surj.py` builds these eight-state labeled graphs for all 174 conservation solutions and performs exhaustive breadth-first search of their reachable state subsets (there are at most 256). Exactly 16 never reach the empty subset; the 158 others first reach it at depths one, two, three in multiplicities 4, 84, 70. In particular the worst-case depth of three is attained. The exact 16 surjective ordered rule pairs, in the stated 16-bit encoding, are

`(43690,43690)`, `(43690,61680)`, `(44204,61644)`, `(51914,52464)`, `(52428,52428)`, `(52428,65280)`, `(52464,51914)`, `(55512,64560)`, `(58596,62400)`, `(61644,44204)`, `(61680,43690)`, `(61680,61680)`, `(62400,58596)`, `(64560,55512)`, `(65280,52428)`, `(65280,65280)`.

**Reversibility classification.** The eight ordered pairs with both local rules chosen from `0xAAAA`, `0xF0F0`, `0xCCCC`, `0xFF00` and matching parity of source offsets implement bijective spatial coordinate permutations (the source offset is respectively 2, 0, 1, -1). All eight appear in the surjective list. For every one of the remaining 166 conserving rules, `collision_witnesses.json` gives two different periodic inputs on some ring of length two, four, or six with equal outputs; `verify.py` checks every witness. In particular each of the other eight surjective pairs is noninjective. Therefore exactly eight of the 16 globally onto pairs are nonreversible.

## Verification

Run `python3 verify.py` followed by `python3 check_surj.py`, with `collision_witnesses.json` alongside both programs. Both use only the Python standard library. The first program independently solves the local flip equations and the eight-ring conservation equations in exact rational arithmetic, checks all 166 collision witnesses, and checks the eight coordinate permutations. The second enumerates the complete finite subset automaton for each of the 174 rules, not merely a bounded collection of output words, and reproduces every listed surjectivity count and the three-symbol sharp bound. All computations use exact integer masks and finite exhaustive state sets.

## Relationship to prior work

Wolnik and collaborators' 2025 number-conserving nonuniform automata study establishes the conservation-graph framework. A 2024 presentation by Makuracki and collaborators classifies reversible number-conserving nonuniform radius-one-and-a-half binary automata; the eight reversible alternating pairs are consistent with that stronger reversibility classification and are **not** claimed as new in isolation. The new classification concerns *global surjectivity*, which is logically weaker than reversibility, and discovers eight surjective nonreversible conserving maps plus an exact sharp Garden-of-Eden test for all nonsurjective alternating conserving pairs. Earlier general graph constructions do not automatically determine this image-language census. See originality-risk discussion in `REVIEW.md`.

## Limitations

This is restricted to binary alphabets, four consecutive input coordinates, and strict alternation of two local rules, with conservation on all even periodic rings. It makes no claim for other neighborhood sizes, longer spatial periods, or injectivity on finite rings as a characterization of global surjectivity. An accessible abstract of a 2026 related paper on barriers and blocks was inspected, but its full text was unavailable; undiscovered implicit prior surjectivity data remain a historical-priority risk. No independent mathematical audit has been performed.

## References

- B. Wolnik et al., *A directed graph allowing for the exploration of the set of number-conserving non-uniform one-dimensional binary cellular automata with radius one and half*, 2025, https://doi.org/10.1007/s11047-025-10015-y.
- Makuracki et al., *Preliminary results of the exploration of the set of number-conserving non-uniform one-dimensional binary cellular automata with radius one and half*, AUTOMATA 2024 conference presentation, https://automata2024.webspace.durham.ac.uk/wp-content/uploads/sites/364/2024/07/5-Non-uniform-cellular-automata-with-radius-one-and-half.pdf.
- B. Wolnik et al., *Exploration of the set of number-conserving non-uniform one-dimensional binary cellular automata with radius one and half: Barriers and blocks*, 2026, https://doi.org/10.1007/s11047-025-10059-0 (abstract only inspected).
