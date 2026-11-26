# Independent mathematical audit

## correctness

PASS

Fix the exact length difference two, ordinary reversal, and count words, not embeddings. If a receiver is xxᴿ with |x|=m−1, any embedding uses its last first-half letter by parent index m+1. Either x already fits in the parent first half, or the other half must use the whole final m−1 suffix, again forcing x to fit in the parent first half. Reflection gives the converse. For a fixed inserted symbol only consecutive insertion sites separated entirely by that symbol give identical words, hence summing duplicate histories over all symbols removes exactly m−1 from qm. For a nonpalindromic receiver with equal outer letters c, a parent with a different outer letter would have to spend both deletions on its ends, leaving a palindrome. Thus all parents have outer letter c, and an embedding can use both ends without changing its internal matches, yielding the shell-stripping bijection. With unequal core ends a and b, a candidate parent must use one of those letters as its outer pair and delete its opposite endpoint; it cannot delete both endpoints. This reduces each of two branches to an even-palindrome parent from a single insertion into an odd word. Parity forces the inserted symbol, if possible. Two different placements of that symbol would have opposite discrepancies at the first and last differing positions, whereas the disagreement positions of two palindromes are symmetric and their letters on those positions are equal within each palindrome. Thus each branch has at most one word, and insertion and verification reconstruct all of them. The two exhibited distinct halfwords really contain a^(2m−3)b after two deletions for every m≥2, while the palindromic count is then at least three. This proves exactly q^(m−1) maximizers; m=1 gives the empty receiver and q parents directly.

## originality

PASS

One-deletion rigidity and the single-insertion sphere count are antecedents. The distinct result combines them with a two-omission symmetric embedding and a two-branch reduction, obtaining sharp fixed-receiver list sizes for all lengths and alphabets. The matching index entry for the frozen theorem itself is the object under review, not another source of priority.

## value

PASS

The receiver-conditioned ambiguity is a natural decoder quantity. A palindromic output admits a list growing linearly with semilength and alphabet size, while any nonpalindromic output admits at most two independently of either, with a sharp witness and full branch reconstruction. This distinction and the exact set of worst receivers are usable without solving the unrelated code-size problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
