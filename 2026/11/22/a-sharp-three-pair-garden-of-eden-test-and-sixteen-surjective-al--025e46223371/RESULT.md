# A sharp three-pair Garden-of-Eden test and sixteen surjective alternating number-conserving automata

## Finding

Exactly 174 ordered rule pairs in the class below preserve the number of ones on every even periodic ring. Exactly 16 of the conserving pairs are surjective on the bilateral full shift. Eight are reversible and the other eight onto pairs are noninjective. Of the 158 nonsurjective pairs, the shortest missing even-aligned output word has length one, two or three two-cell symbols, for 4, 84 or 70 pairs respectively. The three-symbol cutoff is sharp.

## Assumptions and scope

For every binary bi-infinite configuration \(x\), let
\[
(Fx)_i=r_{i\bmod 2}(x_{i-1},x_i,x_{i+1},x_{i+2}),\qquad r_0=f,\quad r_1=g.
\]
The rule number encodes \(r(a,b,c,d)\) as bit \(8a+4b+2c+d\), with bit zero the least significant. Periodic rings have even length so the parity phases are consistent across the boundary. Global surjectivity and injectivity concern \(\{0,1\}^{\mathbb Z}\), not just periodic rings. A collision on an even ring gives a collision on the full shift by periodic repetition, but does not disprove global surjectivity.

## Proof

**Conservation census.** On an even ring of length at least eight, changing a single input bit from zero to one affects the four distinct output positions whose windows contain it, two using \(f\) and two using \(g\). Setting the resulting difference of the four contributions equal to one gives an affine equation in the 32 truth-table bits. Range over both site parities and the six other bits in the affected windows. All such contexts can occur already on the length-eight ring. For a Boolean rule pair conserving on the eight-ring, the constant inputs force each of \(f(0000),g(0000)\) to be zero and each of \(f(1111),g(1111)\) to be one. Conversely the local equations and these constant conditions suffice: starting from the all-zero word and turning on each input one in succession proves conservation on each even ring of length at least eight. For any shorter even ring, repeat its word to reach a multiple of that ring length at least eight. The repeated output is the repetition of the short-ring output, since the local windows and rule parity agree, so equality on the longer ring gives equality on the shorter one.

The rational system of the 256 length-eight ring equations has coefficient rank 17 with 15 free variables. The local-flip system with **four individual constant-bit constraints** has rank 19 with 13 free variables. On Boolean truth tables they are equivalent; equality of their rational ranks is not required. Row reduction followed by exhaustive assignment of the free bits in each system, retaining only solutions whose pivot bits are also Boolean, gives the same set of 174 rule pairs.

**Image automaton.** Group outputs \((2j,2j+1)\) as letters of \(\Sigma=\{00,01,10,11\}\). The graph has the eight input triples \(abc\) as states, with edges \(abc\to cde\) for \(d,e\in\{0,1\}\) labeled
\[
\bigl(f(a,b,c,d),g(b,c,d,e)\bigr).
\]
Each edge is a five-input fragment; consecutive edges overlap in precisely the common input triple. Thus a finite even-aligned output word is possible exactly when a path has those labels. Start with the subset of all eight states and update a subset by taking all successors along the desired label. The subset is empty exactly when the desired word is impossible. Breadth-first search from the full subset therefore finds a shortest missing word, or verifies that the empty subset is unreachable. If it is unreachable, preimage constraints for all finite even-aligned windows of an arbitrary bilateral output are jointly satisfiable: the sets of full input configurations meeting the constraints for a nested sequence of windows are nonempty compact sets with nonempty intersection. This proves surjectivity on the bilateral full shift.

Searching the reachable subsets (at most 256) for each conserving pair gives 16 with no missing word and 158 whose shortest missing words have depths 1, 2 and 3 in multiplicities 4, 84 and 70. The complete list of surjective pairs in the stated encoding is:

`(43690,43690)`, `(43690,61680)`, `(44204,61644)`, `(51914,52464)`, `(52428,52428)`, `(52428,65280)`, `(52464,51914)`, `(55512,64560)`, `(58596,62400)`, `(61644,44204)`, `(61680,43690)`, `(61680,61680)`, `(62400,58596)`, `(64560,55512)`, `(65280,52428)`, `(65280,65280)`.

**Reversibility.** The rules `0xAAAA`, `0xF0F0`, `0xCCCC` and `0xFF00` copy source offsets 2, 0, 1 and −1 respectively. The eight pairs made from two offsets of the same parity permute spatial coordinates bijectively and have local inverses, since the two parity classes map to distinct parity classes by translations. All eight pairs are in the list above. The `collision_witnesses.json` data give distinct periodic inputs of length 2, 4 or 6 with identical outputs for each of the other 166 conserving pairs; the witnesses are checked directly by evaluating the local rules. Thus exactly eight of the onto pairs are noninjective.

## Verification

With `verify.py`, `check_surj.py` and `collision_witnesses.json` in one directory, run `python3 verify.py` and then `python3 check_surj.py`. They require only the Python standard library. The first enumerates the eight-ring and local-flip Boolean solution sets using exact rational row reduction and checks all 166 periodic collision witnesses and all eight coordinate permutations. The second uses the adjacent verifier's eight-ring census and computes the complete finite subset reachability test, not a sample of short words.

## Relationship to prior work

Wolnik et al. (2025) give a graph framework for number conservation in the broader nonuniform radius-three-halves binary setting. That conservation graph plays a different role from the image automaton here. The reversible subset is not claimed as new in isolation; the AUTOMATA 2024 presentation reports preliminary exploration of this nonuniform class. The contribution here is the sharp full-shift image classification in the alternating conserving four-input subclass: which rules are onto, the onto but noninjective cases, and the distribution of shortest missing even-aligned output words. The related 2026 barriers-and-blocks article describes its results in the abstract as small-block dynamics for number conservation on finite grids. The full text was not available via the inspected open routes; possible overlap cannot be excluded.

## Limitations

The result is restricted to the binary alphabet, four consecutive inputs, exact spatial alternation, and conservation on even rings. It does not claim the cutoff for longer periods or different neighborhoods, or characterize full-shift surjectivity by finite-ring surjectivity. The bibliographic comparison is not an exhaustive priority assertion.

## References

- B. Wolnik et al., *A directed graph allowing for the exploration of the set of number-conserving non-uniform one-dimensional binary cellular automata with radius one and half*, 2025, https://doi.org/10.1007/s11047-025-10015-y.
- B. Makuracki et al., *Preliminary results of the exploration of the set of number-conserving non-uniform one-dimensional binary cellular automata with radius one and half*, AUTOMATA 2024 conference presentation, https://automata2024.webspace.durham.ac.uk/wp-content/uploads/sites/364/2024/07/5-Non-uniform-cellular-automata-with-radius-one-and-half.pdf.
- B. Makuracki et al., *Exploration of number-conserving non-uniform cellular automata with a neighborhood of size four: barriers and blocks*, 2026, https://doi.org/10.1007/s11047-025-10059-0 (abstract: https://biblio.ugent.be/publication/01KK1J5XM58N7QFXQJH0BB6C2B).
