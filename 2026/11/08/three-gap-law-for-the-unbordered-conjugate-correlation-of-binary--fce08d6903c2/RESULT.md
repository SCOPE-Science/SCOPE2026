# Three-gap law for the unbordered-conjugate correlation of binary words

## Finding

A *border* of a nonempty word is a nonempty proper prefix that is also a suffix; a word without a border is *unbordered*. A *conjugate* is a cyclic rotation. For every binary word \(w\) containing exactly three occurrences of \(1\), read its three \(1\)-positions cyclically, and let \(g_0,g_1,g_2\geq0\) be the numbers of \(0\)'s immediately after those successive occurrences (indices modulo \(3\)).

For each marker \(i\), the rotation cut immediately **before** its \(1\) is unbordered if and only if \(g_i<g_{i-1}\). The rotation cut immediately **after** its \(1\) is unbordered if and only if \(g_i>g_{i-1}\). All remaining cuts are bordered. These rules specify the complete cyclic border-correlation pattern, including the exact positions of every unbordered rotation; when two markers are adjacent, coincident cuts never satisfy either criterion.

Consequently the number \(\nu(w)\) of unbordered indexed rotations, or equivalently distinct unbordered conjugates, is
\[
\nu(w)=\sum_{i=0}^2\mathbf1_{\{g_i\ne g_{i-1}\}}=
\begin{cases}
0,&g_0=g_1=g_2,\\
2,&\text{exactly two gaps are equal},\\
3,&\text{the three gaps are pairwise distinct}.
\end{cases}
\]
No three-one binary word has exactly one unbordered conjugate; three first occurs at length \(6\).

For every \(n\ge3\), let \(M_j(n)\) be the number of indexed *linear* binary words of length \(n\) with exactly three ones and \(\nu(w)=j\). Set \(K_n=\lfloor(n-1)/2\rfloor\) and \(\delta_n=\mathbf1_{\{3\mid n\}}\). Then
\[
M_0(n)=\frac{n\delta_n}{3},\qquad
M_2(n)=n(K_n-\delta_n),\qquad
M_3(n)=\binom n3-nK_n+\frac{2n\delta_n}{3},
\]
with \(M_j(n)=0\) for all other \(j\). In terms of cyclic necklaces, the respective numbers are \(\delta_n\), \(K_n-\delta_n\), and \((\binom{n-1}{2}-3K_n+2\delta_n)/3\).

For a uniformly sampled indexed length-\(n\) three-one binary word, the exact moments are
\[
\mathbb E\nu=3-\frac{6K_n}{(n-1)(n-2)},\qquad
\operatorname{Var}(\nu)=\frac{6(K_n+2\delta_n)}{(n-1)(n-2)}-
\left(\frac{6K_n}{(n-1)(n-2)}\right)^2.
\]
In particular, \(\Pr(\nu=3)=1-3/n+O(n^{-2})\), \(\mathbb E\nu=3-3/n+O(n^{-2})\), and \(\operatorname{Var}(\nu)=3/n+O(n^{-2})\).

## Assumptions and scope

Every word has exactly three \(1\)'s and any nonnegative number of \(0\)'s, including zero. A cut is a boundary between adjacent positions on the indexed cyclic word; rotating at a cut means beginning at the symbol immediately after it. There are \(n=3+g_0+g_1+g_2\) indexed cuts, including when the word has a nontrivial period. Equal-gap words have period \(n/3\) and hence no unbordered rotations. All other three-gap words are primitive (a nontrivial power with exactly three ones must be a third power).

The claim concerns *ordinary exact* prefix-suffix borders, not Abelian borders, cyclic factors shorter than the whole word, or the unrestricted alphabet/Hamming-weight setting. Necklaces are counted modulo rotations alone, not reversal or symbol complement.

## Proof

Fix an index \(i\) and abbreviate \(a=g_i\), \(b=g_{i+1}\), \(c=g_{i-1}\).

**A cut immediately after marker \(i\).** Its rotated word is \(U=0^a1\,0^b1\,0^c1\). If \(a\le c\), the word \(0^a1\) is a proper prefix and suffix of \(U\), so \(U\) is bordered. Suppose \(a>c\). Any proper border must begin in an initial zero run and end in \(1\). If it contains exactly one \(1\), its initial zero run would be \(c<a\), incompatible with the prefix of \(U\). If it contains two \(1\)'s, comparing initial zero runs and the intervening zero run forces \(a\le b=c\), contradicting \(a>c\). If it contains all three \(1\)'s, it cannot be a proper prefix-suffix match: a proper suffix has fewer than \(a\) leading zeros, while any prefix containing three \(1\)'s has exactly \(a\) leading zeros. Hence no border exists and \(U\) is unbordered exactly when \(a>c\).

**A cut immediately before marker \(i\).** Its rotated word is \(V=1\,0^a1\,0^b1\,0^c\). If \(a\ge c\), the word \(1\,0^c\) is a proper prefix and suffix, so \(V\) is bordered. Suppose \(a<c\). A proper border begins with \(1\) and ends with \(0\). If that suffix begins at the final \(1\), its \(c\) trailing zeros cannot match the prefix gap \(a<c\). If it begins at the middle \(1\), equality of the inter-one gaps forces \(a=b\), while matching the trailing \(c\) zeros then requires \(b\ge c\), also impossible. It cannot begin at the first \(1\) and be proper. Thus \(V\) is unbordered exactly when \(a<c\).

Every other cut is inside a constant-symbol run, so the first and last letters of its rotated word coincide, furnishing a one-letter border. If a zero gap vanishes, its coincident boundary cuts are similarly excluded by the strict comparisons. Summing the two strict alternatives for the three consecutive gap pairs proves the complete correlation and the classification of \(\nu\).

For the enumeration, there are \(\binom{n-1}{2}\) ordered triples of nonnegative gaps with sum \(n-3\). All three equal occurs for \(\delta_n\) triples. Exactly two equal occurs for \(3(K_n-\delta_n)\) triples, since their repeated value ranges from \(0\) to \(\lfloor(n-3)/2\rfloor\), excluding the all-equal case. The remaining \(\binom{n-1}{2}-3K_n+2\delta_n\) triples are pairwise distinct. Each ordered triple together with an indexed start position of a distinguished \(1\) determines an indexed word with a distinguished \(1\); every indexed three-one word has three choices of the distinguished \(1\). Therefore each class with \(t\) ordered gap triples contains \(nt/3\) indexed words. This also proves the necklace counts: distinct-gap and two-equal triples have cyclic orbit size \(3\), and all-equal triples orbit size \(1\).

Finally, \(M_0+M_2+M_3=\binom n3\). The first and second raw moments equal \((2M_2+3M_3)/\binom n3\) and \((4M_2+9M_3)/\binom n3\). Substitution and subtraction of the squared first moment give the displayed formulas. The asymptotics follow by \(K_n=n/2+O(1)\).

## Verification

Run `python3 verify_gap_border.py` using Python 3 with no third-party libraries. The verifier constructs every indexed length-\(n\) three-one binary word for \(3\le n\le29\), computes the unbordered cuts by an independent prefix-function algorithm on each literal rotation, tests each predicted cut, then checks all three class counts and both rational moment formulas. For \(n\le17\), it additionally cross-checks the prefix-function method against direct comparison of all proper prefixes and suffixes. Its observed messages include `DIRECT_KMP_BORDER_AND_FULL_POPULATION_OK 27405` and `EXACT_MOMENT_FORMULAS_OK 3..29`. These finite tests corroborate, but do not replace, the proof for arbitrary length.

## Relationship to prior work

Harju and Nowotka introduced the border-correlation function and established general restrictions on unbordered binary conjugates, including the unrestricted \(\lfloor n/2\rfloor\) upper bound. Holub and Müller characterized *fully bordered* words (those with two unbordered conjugates) inductively and related them to products of palindromes. Clokie, Gabrić and Shallit subsequently completed unrestricted binary maximum-spectrum results and studied the expectation for words sampled from the unrestricted uniform alphabet model. The present statement instead determines **every border-correlation position** in the exact three-one slice by three local zero-gap comparisons, and thus its complete conditional distribution. It neither improves the unrestricted bounds nor claims that fixed-weight specialization is independent of all consequences of prior structural results. No equivalent complete three-gap distribution was found among the checked sources; historical priority remains subject to independent literature review.

## Limitations

The cut characterization is special to exactly three occurrences of \(1\); for more markers, longer borders can depend on nonadjacent gaps. The population formulas use a uniform law conditional on exactly three ones, not unrestricted independent Bernoulli letters. Database and literature searching cannot establish absolute uniqueness, and a technical-report PDF was available as extracted text without a successful visual-page retrieval. The derivation has not undergone independent mathematical review.

## References

1. T. Harju and D. Nowotka, *Border Correlation of Binary Words*, TUCS Technical Report 546 (August 2003), and *Journal of Combinatorial Theory, Series A* 108 (2004), 331–341. DOI: https://doi.org/10.1016/j.jcta.2004.07.009 ; report: https://citeseerx.ist.psu.edu/document?doi=912065a268d68bfb1e44494181f636a0c491d9c2&repid=rep1&type=pdf .
2. Š. Holub and M. Müller, *Fully bordered words*, arXiv:1504.02222, first posted 2015-04-09, https://arxiv.org/abs/1504.02222 .
3. T. Clokie, D. Gabrić and J. Shallit, *Circularly squarefree words and unbordered conjugates: a new approach*, arXiv:1904.08187, first posted 2019-04-17, https://arxiv.org/abs/1904.08187 .
4. OEIS A321162, *Maximum number of unbordered conjugates for a binary word of length n*, https://oeis.org/A321162 ; OEIS A091838, *Number of images of the border correlation function for binary words of length n*, https://oeis.org/A091838 .
