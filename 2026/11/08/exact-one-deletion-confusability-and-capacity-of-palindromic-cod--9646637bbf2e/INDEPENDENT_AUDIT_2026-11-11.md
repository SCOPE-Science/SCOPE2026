# Independent mathematical audit

## correctness

PASS

For q>=2, all-length one-symbol deletion shadows restricted to palindromes: inserting a FIXED letter into a word yields at most one palindrome. Therefore even palindromes form an edgeless graph, and distinct odd palindromes sharing a descendant have different central symbols. Fixed central-symbol families provide q^m codes at length 2m+1, while cliques of q words with identical m-letter half force <=q^m; even length 2m gives q^m all palindromes. Different outer symbols in an odd conflict force two opposite-phase alternating palindromes; equal outer symbols reduce to length n-2. Thus the graph recursion is q smaller copies and one bridge for each unordered outer pair, giving e_m=q e_(m-1)+C(q,2) and e_m=q(q^(m+1)-1)/2. Independent word-shadow construction corroborated every graph edge and formula for q=2 n<=13, q=3 n<=9 and q=4 n<=7. The lemmas, not those finite tests, establish arbitrary n,q.

## originality

PASS

PASS for q-ary extension and complete one-deletion confusability graph when q>=3, with the full binary q=2 capacity and binomial-tree graph explicitly prior/covered; no novelty is claimed for the binary specialization.

## value

PASS

Natural source-constrained deletion-coding classification for all alphabets: exact whole confusability graph rather than only capacity, with cross-symbol bridges and all-length edge counts not obtained from the earlier binary tree result. The binary graph itself is correctly credited to prior work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
