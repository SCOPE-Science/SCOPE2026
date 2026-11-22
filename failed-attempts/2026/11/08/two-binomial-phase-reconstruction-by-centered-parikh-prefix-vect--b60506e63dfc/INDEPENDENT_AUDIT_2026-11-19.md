# Independent mathematical audit

## correctness

PASS

The assigned source proves an exact cyclic one-letter move formula for all distinct letter pairs: C_xy(F_(i+1)^m)-C_xy(F_i^m)=m(A_x [u_i=y]-A_y [u_i=x]); summing yields m(A_x v_y-A_y v_x). Repeated-letter pairs depend only on the fixed full-period letter counts. Because each occurring letter has A_x>0, all mixed differences vanish exactly when v_x/A_x is constant, equivalently H_i=H_j for H_i(x)=p P_i(x)-i A_x. The p=1 and one-letter cases are vacuous but consistent. For m>=1 the factor m never changes equality. Bezout on reduced composition A/g implies collision distance is a multiple of p/g. For q>=3 distinct single-letter runs, any proper segment meeting all q labels contains an entire interior run, contradicting required strict proportionality; the one-binomial deck stays constant. The O(pq) expected integer-arithmetic grouping bound follows by forming p prefix vectors of dimension q, with hashing; bit complexity is not claimed. Recomputed the original seven-entry Git tree from actual source blob SHAs, obtaining 72caaec1601d35d1f8637145119b45cb6bc74740. Independently enumerated full scattered-pair decks for 2,970 words with alphabets of 1..4 letters, 111,585 phase pairs across m=1..3, 498,552 exact pair-count difference scaling checks and 1,344 grouped-run vectors for q=3..5; all agree with the theorem. These finite checks supplement rather than prove the universal equations.

## originality

FAIL

A previously published fixed-content theorem for k>=3 states exactly the same H_i centered-prefix collision criterion, gcd restriction and injectivity of grouped distinct-letter runs, and proves a strictly stronger complete attainable-spectrum result. The new all-powers m quantifier is an elementary immediate corollary of B_xy(w^m)=m B_xy(w)+binom(m,2)|w|_x|w|_y, since all rotations have identical letter counts. The k=2 case follows the same cross-product identity and known binary rotation-count theory; k=1 is trivial. The original proof does not contain a separate unanticipated classification beyond prior theorems and standard concatenation. Exact first-public priority of all mirrored records is not fully established, but complete mathematical coverage is verified by reading the earlier-dated primary RESULT. This is a mathematical implication decision, not an inference from unsuccessful searches.

## value

FAIL

The complete 2-binomial cyclic-phase partition is a natural reconstruction problem, and its computational form can be pedagogically useful. However, the same exact prefix-signature classification, gcd collision obstruction and three-or-more grouped-run injectivity appear explicitly in the earlier fixed-content spectrum theorem. Replacing one-period rotations by m repeated periods adds only a degree-two concatenation identity; the algorithm hashes the already published H_i signatures. The extension to trivial one-letter or elementary binary cases is not a separate motivated unknown invariant. There is thus no new mathematical classification, boundary, or exact fact of distinct value after removing covered assertions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
