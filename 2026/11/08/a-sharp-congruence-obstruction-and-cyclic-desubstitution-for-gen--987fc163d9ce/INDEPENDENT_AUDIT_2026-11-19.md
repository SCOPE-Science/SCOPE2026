# Independent mathematical audit

## correctness

PASS

Reconstructed the transition identity d(bk+r)=0 at r=0..b-3, 1 at r=b-2, and 1 or 0 at r=b-1 depending on parent-letter equality. Every b-window of the coded transition string 0^(b-2)1e has unique residue phase for b>=3: a single 1 is mandatory, while two 1s identify the mandatory one as first of adjacent pair or last of endpoint pair. Circular (b+1)-windows occur when n>=b+2, so phase increments round the circle force b|n. For n=bm, an aligned circular word decomposes uniquely into mu_b-blocks; rotating one symbol into each block enforces each length-(m+1) periodic source extension and proves both surjection and injection. Short n<=b+1 classification follows from maximal constant-run lengths 1,b-1,b and absence of four-letter alternation, plus explicit base-3 length-four factor enumeration. The three source classes 00,01,11 generate distinct surviving length-2b^k images using 000,010,101,111 source triples and the imbalance (b-2)^k. Independently regenerated fixed points, checked all phases at b=3..8 and Lie values/extension equivalence at n=1..50, plus b=3,4 at n=2b^3; these finite tests corroborate but do not establish all b,n. No nonstandard lemma remains unproved within the stated elementary phase/run argument.

## originality

PASS

Best-of-knowledge distinct theorem: full all-base sharp b-divisibility of rotation-complete factors plus a cyclic one-extra-source-letter desubstitution criterion. General recognizability of the b=3 substitution is known and is explicitly not credited as original; occurrence-preservation, ordinary-square, Abelian-factor and other-word Lie results do not state or imply the full cyclic-factor theorem without additional new cyclic arguments.

## value

PASS

Lie complexity is a natural conjugacy-sensitive invariant of automatic-word languages, strictly different from square counts or Abelian factor counts. The all-base sharp divisibility support and one-symbol source-window bijection settle a motivated infinite structural question, with exceptional boundary b+1, nontrivial mixed class at 2b and an infinite family of nonzero multiples. These nontrivial restrictions are not mechanical consequences of recognizability alone, automaticity or known square spectra. No full numeric formula at all multiples or paper-sized extension is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
