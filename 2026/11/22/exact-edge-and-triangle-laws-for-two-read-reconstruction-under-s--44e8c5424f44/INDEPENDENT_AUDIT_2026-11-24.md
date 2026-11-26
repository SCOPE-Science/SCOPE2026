# Independent mathematical audit

## correctness

PASS

Cai et al.'s Type-A characterization applies to sets of distinct one-deletion outputs. It can also be reconstructed directly: if the first and last mismatches are p and q, any common deletion with the first deletion index earlier than the second yields the same descendant as deleting p from the first word and q from the second (shift alignment on [p,q] and a constant run up to p). The reverse order yields the other candidate. Two distinct outputs require p<q and both shift alignments, forcing opposite alternating phases between p and q. In a triangle the difference sets are intervals and one is the symmetric difference of the other two. Two intervals with nonempty interval symmetric difference must be adjacent and disjoint, or nested with one shared end. Thus there is one long edge split into two adjacent shorter edge intervals of lengths at least two. In the 001-avoiding graph the cut producing 00 is immediately followed by 1; the cut producing 11 preserves admissibility, including the phase-dependent external boundaries. The prefix must be empty or legal ending in 1, the suffix must be legal and not start in 01; this gives the stated Fibonacci factors. The unique interval and cut validate both counts, including the empty small-length sums. The dominant double pole is at phi^(-1), where z^2/(1-z)=1 and the edge leading constant is phi^3/5; hence the triangle-to-edge ratio tends to 1. Complement and reversal give the other individual forbidden factors. An independent inverted deletion-index census (python3 /workspace/branches/audit_exact_124.py 2) matched every coefficient through length 12, including the empty word, for all four motifs. This is corroboration, not the all-length proof.

## originality

PASS

The edge normal form and unrestricted splice geometry/counts are prior. The distinct supported claim is the exact induced edge and triangle census for one fixed motif in the reversal/complement orbit of 001, including the one-splice coefficient law. Neither unrestricted count can give this restriction by specialization of alphabet size, and the closest restricted censuses examined use other languages.

## value

PASS

This gives a benchmark for ambiguity on a natural memory-constrained binary source. Triangles detect three pairwise ambiguities that edge totals alone do not capture, and the forbidden-splice mechanism gives a sharp identity and limiting edge multiplicity, not just a small table. It does not solve the independence-number or optimal reconstruction-code problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
