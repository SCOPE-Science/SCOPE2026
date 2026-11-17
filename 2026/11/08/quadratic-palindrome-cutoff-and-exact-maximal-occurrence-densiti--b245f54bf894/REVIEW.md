# Independent mathematical audit

## correctness

PASS

For b>=3 the fixed point w of 0->0^(b-1)1, 1->1^(b-1)0 has the XOR transition sequence d with mandatory 1 at residue b-2, optional 1 at b-1 and zeros elsewhere. No b consecutive zeros nor three consecutive ones occur. Reflection of mandatory transition ones in a transition palindrome restricts its center to two residues; lengths b^2 and b^2-1 would force b forbidden consecutive parent symbols. For maximal w-palindrome length b^2-1 the residue count and parity exclude all start residues except 0; an exact run of b parent letters yields only the two stated complementary words. Every b-run starts at parent block end, giving occurrence positions b^2*t+b(b-1) with w(t)=1-a,w(t+1)=a. The primitive induced transition substitution has 1-density 2/(b+1), yielding 01 and 10 densities 1/(b+1) and each maximal-palindrome start density 1/[b^2(b+1)]. The b=2 case is explicitly excluded. Independent literal prefix enumeration for bases 3,4,5,6,7 at 25,000 letters each matched all predicted maximal starts and found no length b^2 palindromes.

## originality

PASS

The Mephisto substitution and the general finite-palindrome/automatic-prefix-length theory are prior art. The infinite-base sharp cutoff, exact two maximizing words, and complete occurrence-density law survive comparison to the identified primary literature and unrelated published morphic-word classifications.

## value

PASS

A natural automatic-word family has a sharp quadratic palindromic cutoff, precisely two extremal factors and exact occurrence densities, all over an infinite base parameter. These are structural combinatorics-on-words facts, not arbitrary finite-window counts or a mere reindexing of prefix palindromic length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
