# Independent mathematical audit

## correctness

PASS

The universal two-step history count for n≥k≥1 is (n-k+1)(n+1). Each pair of disjoint original k-windows gives two distinct commuting histories with the same output; they are pairwise-disjoint history pairs and number binom(max(n-2k+2,0),2). Thus every source sphere has size at most the stated difference. A constant source a^n and its first inserted complement block b^k allow an exact count: second-window intersections of size t>=1 have distinct b-populations across t and distinguishable first b-run lengths across crossing types; t=0 outputs are two b^k runs separated by a-run with precisely the disjoint-history double representations. The proof covers k=1 and n<2k. Constant words attain the bound for every fixed-point-free complement alphabet; in fact construction works for all k though only odd k claimed. Independent brute checked 3286 binary-source cases across odd k and small n, with constant-source equality; it is not used as an all-n proof.

## originality

PASS

PASS, qualified. Zabokritskiy arXiv:2609.00779 proves the same numerical two-duplication bound for EVEN k using palindromic/reverse-complement conjugacy; the odd-k case cannot follow from that parity-restricted conjugacy. Prior length-two all-maximizer results and odd-k palindromic large-alphabet distinct-symbol constructions do not imply odd-k RC sharpness on fixed-point-free binary alphabet by constant words. Novelty specifically concerns the missing odd-k half of the natural fixed-length two-error sphere classification, not history-commutation upper bounds.

## value

PASS

PASS: The exact maximal error-ball volume under two sequential reverse-complement duplications at odd k is a natural coding-theoretic finite combinatorial invariant, resolves a parity gap left by earlier even-block results, and the constant-source equality proof shows collisions are exactly the unavoidable disjoint-window commutations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
