# Exact sparse non-overlapping code capacity over arbitrary alphabets

## Finding

Fix an alphabet \(\Sigma=\{0,1,\ldots,q-1\}\), with a distinguished zero, and write \(\Sigma^*=\Sigma\setminus\{0\}\). Let \(q\ge2\) and \(n\ge2\) be integers. Among all length-\(n\) codes whose words have exactly two nonzero letters, let \(M_q(n,2)\) denote the largest cardinality subject to **non-overlap**: for every two codewords (including equal codewords), no nonempty proper prefix of the first equals the same-length suffix of the second.

**Theorem.** Put \(s=q-1\). Then the exact optimum, for all alphabet and block lengths in the stated domain, is

\[
M_q(n,2)=
\begin{cases}
\dfrac{n-1}{2}s^2,&n\text{ odd},\\[4pt]
\dfrac{n-2}{2}s^2+\left\lfloor\dfrac{s^2}{4}\right\rfloor,&n\text{ even}.
\end{cases}
\]

A constructive maximum code is provided in the proof. For odd \(n\) it contains one representative of every admissible primitive cyclic necklace of weight two. For even \(n\), the primitive-necklace packing bound exceeds the optimum by exactly

\[
\binom{s}{2}-\left\lfloor\frac{s^2}{4}\right\rfloor.
\]

This deficit is positive precisely when \(q\ge4\). In an even-length optimum, every primitive necklace having unequal intervening zero gaps must be represented; the equal-gap codewords necessarily use disjoint sets of first and last nonzero colors. These statements concern the optimum, not a claimed classification of all optimal codebooks.

## Assumptions and scope

A *proper prefix* has length in \(\{1,\ldots,n-1\}\), and a *proper suffix* has the same length. All nonzero symbols are distinct labeled letters, not field elements, and no algebraic operations on the alphabet are assumed. A word has *weight two* if exactly two of its positions contain members of \(\Sigma^*\). The code may be empty (at \(q=n=2\)); a codeword may not have a border, because self-overlap is forbidden. Circular rotation is employed only for the upper bound and is **not** an allowed equivalence in the definition of code size.

## Proof

### 1. The cyclic-necklace packing constraint

If a word \(w=uv\), with both \(u\) and \(v\) nonempty, belongs to a non-overlapping code, its nontrivial cyclic rotation \(vu\) cannot also belong: the proper prefix \(u\) of \(w\) is the proper suffix \(u\) of \(vu\). Likewise, a periodic word has a proper prefix equal to a suffix of itself, and cannot belong. Consequently, each primitive cyclic necklace supplies **at most one** codeword.

Record a cyclic weight-two word by its two positive-colored markers \(a,b\in\Sigma^*\) and the two intervening zero-gap lengths \(g,h\ge0\), with \(g+h=n-2\). Changing the starting marker interchanges \((g,h,a,b)\) with \((h,g,b,a)\). When \(g\ne h\), there is a unique orientation with \(g>h\). All such necklaces are primitive, and their number is

\[
U=\left\lfloor\frac{n-1}{2}\right\rfloor s^2.
\]

When \(n\) is odd, these are **all** the weight-two necklaces. When \(n=2m+2\) is even, one additional class has \(g=h=m\). If its colors agree, the word is a twofold repetition and is not eligible. Otherwise, each primitive equal-gap necklace is determined by an unordered pair of distinct colors, yielding \(\binom{s}{2}\) additional necklace classes. A plain necklace bound would therefore be \(U+\binom{s}{2}\); the next step sharpens it.

### 2. The equal-gap obstruction

Fix even \(n=2m+2\), with \(m\ge0\). Every possible codeword from an equal-gap necklace can be written

\[
u=0^i a\,0^m b\,0^{m-i},\qquad 0\le i\le m,\quad a,b\in\Sigma^*,\quad a\ne b.
\]

Let \(v=0^j c\,0^m d\,0^{m-j}\) be another such word. If \(a=d\), the prefix of \(u\) and the suffix of \(v\) of length

\[
\ell=m+i-j+1
\]

coincide: each consists of \(i\) zeros, the common letter \(a=d\), and \(m-j\) zeros. The bounds \(0\le i,j\le m\) ensure \(1\le\ell\le2m+1=n-1\). This is a forbidden overlap, including when \(u=v\).

Thus, if \(A\) is the set of first-marker colors and \(B\) the set of last-marker colors among the equal-gap codewords, then \(A\cap B=\varnothing\). There is at most one selected representative for each ordered color pair, since two equal-gap words with the same ordered pair are cyclic rotations. Therefore

\[
|\mathcal C_{\mathrm{equal}}|\le |A||B|
\le\left\lfloor\frac{s^2}{4}\right\rfloor.
\]

Together with the \(U\) unequal-gap necklace classes, this proves the claimed universal upper bound, in both parities.

### 3. A sharp construction

For every \(q,n\), include all words

\[
0^g a\,0^h b,
\qquad g,h\ge0,\quad g+h=n-2,\quad g>h,\quad a,b\in\Sigma^*.
\]

There are exactly \(U\) such words. If \(n\) is even, partition \(\Sigma^*\) into disjoint sets \(A,B\) with \(|A|=\lfloor s/2\rfloor\) and \(|B|=\lceil s/2\rceil\), and additionally include every word

\[
0^m a\,0^m b,\qquad a\in A,\quad b\in B.
\]

This contributes exactly \(\lfloor s^2/4\rfloor\) codewords; for an empty part it contributes zero.

Every constructed word ends with a nonzero symbol, so every proper prefix contains at most one nonzero marker. Every nonempty suffix ends with its final nonzero marker. If a proper prefix equals a suffix, both necessarily contain exactly one nonzero marker. The suffix is therefore of the form \(0^t b\) with \(0\le t\le h\), where \(h\) is the zero gap immediately preceding the last marker of its word; the prefix must be exactly \(0^g a\), where \(g\) is its word's initial zero gap. Equality would require \(g=t\le h\) and \(a=b\). For a word in the unequal-gap family, the first zero gap \(g\) exceeds the last zero gap \(h\); more strongly, all chosen unequal-gap \(g\)'s are strictly larger than all chosen unequal-gap \(h\)'s. In the even case, every such \(g\) is larger than \(m\), and every such \(h\) is smaller than \(m\). The only remaining possibility is an equal-gap prefix and equal-gap suffix, where equality is prevented by \(A\cap B=\varnothing\). Thus **no** proper prefix of a codeword matches a suffix of any codeword, including itself. The upper bound is attained.

### 4. Structural and boundary consequences

An optimal code must saturate both disjoint upper-bound contributions, so it represents all \(U\) unequal-gap necklace classes. In even lengths, its equal-gap first/last color sets are disjoint by the proved obstruction. The exact primitive-necklace deficit is \(\binom{s}{2}-\lfloor s^2/4\rfloor\), zero for \(s\in\{1,2\}\) and positive for \(s\ge3\). At \(n=2\) the construction consists solely of the equal-gap bipartition and gives the same formula; at \(q=2,n=2\) it correctly gives the empty code.

## Verification

A standalone `checker.py` builds the extremal code and directly tests every ordered prefix-suffix comparison. Running `python checker.py` verifies the formula and non-overlap property for all \(2\le q\le7\), \(2\le n\le14\) (91 parameter pairs and 438,536 ordered codeword-pair comparisons). Running `python checker.py --milp` additionally formulates the **full** weight-two candidate conflict graph independently, excludes self-overlapping candidates, and solves its binary maximum-independent-set program to zero optimality gap, for all \(2\le q\le5\), \(2\le n\le6\) (20 instances). The exact optimum values are \((0,1,1,2,2)\), \((1,4,5,8,9)\), \((2,9,11,18,20)\), and \((4,16,20,32,36)\), respectively, by increasing \(q\). This optional computation uses SciPy and HiGHS; the unbounded theorem follows from the preceding proof and does not rely on extrapolating the computation.

## Relationship to prior work

Wang and Wang (2021), Qin, Chen and Luo (2023), and Stanovnik, Moškon and Mraz (2024) study general \(q\)-ary non-overlapping-code constructions, non-expandability and optimization. Their inspected results do not give an all-\(q\), all-\(n\) optimum restricted to exactly two nonzero positions or the even-length colored-necklace deficit. The published binary constant-weight-three necklace results and other restricted-overlap bounds concern different constraints, and no implication to the present two-colored-marker formula was found. The ordinary length-two alphabet-bipartition bound is reflected in the even-gap obstruction, but by itself does not account for the unbalanced necklaces at arbitrary blocklengths.

## Limitations

The theorem concerns *exactly two* nonzero positions and the full set of forbidden proper prefix-suffix overlaps. It does not determine optimal code sizes at weights three or higher, mixed weights, or under deletion noise. The proof is self-contained; the originality comparison is a best-knowledge assessment, not a guarantee against unindexed equivalent work or an unnoticed consequence of a general theory. An independent mathematical audit has not been performed.

## References

1. G. Wang and Q. Wang, *Q-ary non-overlapping codes: a generating function approach*, arXiv:2108.06934v1 (first public 2021-08-16), https://arxiv.org/pdf/2108.06934 .
2. C. Qin, B. Chen and G. Luo, *On non-expandable cross-bifix-free codes*, arXiv:2309.08915v1 (2023), https://arxiv.org/pdf/2309.08915 .
3. L. Stanovnik, M. Moškon and M. Mraz, *In search of maximum non-overlapping codes*, Designs, Codes and Cryptography 92 (2024), https://doi.org/10.1007/s10623-023-01344-z .
4. L. Stanovnik, M. Moškon and M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, arXiv:2410.18458 (2024), https://arxiv.org/abs/2410.18458 .
