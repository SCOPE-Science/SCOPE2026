# Independent mathematical audit

## correctness

PASS

Greedy embedding of a symbol uses first position 1+((r-p) mod q), followed by independent positive jumps 1..q. The simultaneous first-symbol threshold multiset is {h+1..q} disjoint-multiset-union {q-h+1..q}; initial symbol plus jumps uniquely encodes the distinct received word. Summing coefficient partial sums gives the formula. Cumulative threshold dominance gives phase order; minimal threshold d+1 and unique all-one jump sequence gives LCS length max(0,n-d) and multiplicity including q=2h. Boundary ell=0 explicitly one. Independently tested 660 (q,n,h,ell) cases by literal distinct-subsequence sets, not a proof of all parameters.

## originality

PASS

The exact all-radius individual-pair spectrum and coefficientwise phase order do not follow from the inspected general deletion-ball upper bounds, extremal restricted-pair envelopes, LCS-only algorithms or same-period single-word embedding multiplicities. Originality is best-of-knowledge; Wang–Li–Fu and Sun–Ge full text not available in this run.

## value

PASS

Exact distinct-received-word ambiguity is a natural invariant of deletion channels; truncations of repeated permutations form a canonical structured family. The uniform exact spectrum, rather than mask-counts or only LCS, supplies meaningful quantified pair ambiguity and phase hierarchy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
