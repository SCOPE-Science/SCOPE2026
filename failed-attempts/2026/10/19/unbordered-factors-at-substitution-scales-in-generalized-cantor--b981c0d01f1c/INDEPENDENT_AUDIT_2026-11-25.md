# Independent mathematical audit

## correctness

PASS

The substitution recurrence W_(j+1)=W_j 0^[(q-2)q^j] W_j gives palindromic prefixes with 2^j ones and no adjacent ones. At length n=q^k, the fixed point is partitioned into W_k and all-zero n-blocks; each W_k is followed by a zero block. A factor beginning at one-position p of W_k is W_k[p:n] followed by p zeros. At p=0 the endpoints give a one-letter border. For 0<p<m=q^(k-1) the prefix and suffix of length m both equal A[p:m] followed by p zeros. For a start in the second copy of A, the last one is at t<m in the proposed word. Any proper border gives period d, so the first one gives a one at d<=t, and the last one gives another at t+d<2m<=n, a contradiction. Reversal is closed because the prefixes are palindromes, and the number of ones distinguishes all listed starts. This exhausts both endpoint orientations. An independent finite test found the exact sets rather than just their sizes.

## originality

FAIL

The distinct indexed finite ternary-Cantor language theorem gives the exact q=3 power slice, and its border criterion transports mechanically to every q>=3. The key observation is that any candidate border of a factor beginning with 1 and ending in t zeros tests only equality of internal complete gaps and whether a candidate terminal gap is long enough for t zeros. Generalized Cantor gap lengths are (q-2)q^v for the same ruler ranks v=nu_2(i) used in the indexed result. If h is the first rank whose gap is at least t, replacing complete gaps by 3^v and the terminal length by 3^h preserves all these tests, hence preserves borderedness. Applying the indexed classification and selecting length q^k forces rank h=k: lower ranks have length at most (q-1)q^(k-1), while ranks above k require more than (q-2)q^k trailing zeros. At rank k a suffix starting at offset p has t=p, which exceeds (q-2)q^(k-1) exactly at the ones of the second copy. This yields the exact listed factors and count with no additional border analysis. The scientific finding thus has equivalent coverage at q=3 and is a mechanical consequence of the indexed criterion for other bases, though it is not explicitly stated for those bases in that source. No provenance or priority conclusion follows.

## value

PASS

As a mathematical fact the complete power-scale set, rather than a few data points, is useful for understanding how the word's natural substitution dilation constrains its unbordered factors. The correct direct argument is concise. There is no independent surviving distinct theorem here after the originality comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
