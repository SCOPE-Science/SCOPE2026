# Exact attainable proper-border lengths of Galois words

## Finding

Let \(\Sigma\) be a totally ordered alphabet with at least two symbols, and let \(\mathcal B_\Sigma(n)\) consist of all integers \(b\) for which some length-\(n\) Galois word has a proper border of length \(b\). Then, for every integer \(n\ge2\),

\[
\mathcal B_\Sigma(n)=
\begin{cases}
\{b:1\le b<n,\ b\equiv1\pmod2\}, & n\text{ odd},\\
\{b:1\le b<n/2,\ b\equiv1\pmod2\}, & n\text{ even}.
\end{cases}
\]

In particular the attainable spectrum is independent of the alphabet size once it is at least two. The even-length half-word restriction is sharp, while odd-length Galois words can have a proper border only two symbols shorter than the word.

## Assumptions and scope

Use zero-based positions for symbol indexing. For distinct equal-length words \(x,y\), write \(x\prec_{\rm alt}y\) when, at their first differing zero-based index \(i\), we have \(x_i<y_i\) if \(i\) is even and \(x_i>y_i\) if \(i\) is odd. A word \(w\) is *Galois* when \(w\prec_{\rm alt}\operatorname{rot}_j(w)\) for every rotation by \(1\le j<|w|\). This strict condition implies primitiveness. A border of length \(b\) is a common prefix and suffix of length \(b\); it is proper when \(1\le b<|w|\). A period \(d\) obeys \(w_i=w_{i+d}\) for every index where both sides occur. All words are finite; the alphabet need only contain two ordered symbols.

## Proof

**Step 1: parity of borders.** The known odd-border lemma for Galois words (Reutenauer, Proposition 3.1; Dolce–Restivo–Reutenauer, Lemma 35) rules out even border lengths. For completeness, write a bordered Galois word as \(w=X B=B Y\), where \(|B|=b\) and \(|X|=|Y|=d=n-b\). If \(b\) is even, strict minimality against the rotation \(YB\) of \(BY\) gives \(X\prec_{\rm alt}Y\); here \(X\ne Y\), since otherwise the rotation equals \(w\). Comparing \(BY\) with the rotation \(BX\), after the common prefix \(B\) of even length, gives \(Y\prec_{\rm alt}X\). These inequalities contradict one another. Thus every proper border is odd.

**Step 2: the short odd-period obstruction.** Suppose, towards a contradiction, that a primitive Galois word \(w\) of length \(n\) has an odd period \(d\le n/2\). Write \(n=kd+r\) with \(k\ge2\) and \(0\le r<d\), put \(U=w[0..d-1]\), and write \(U=V T\) with \(|V|=r\), so \(w=U^k V\). If \(r=0\), \(w\) is a proper power and is not Galois. For \(r>0\), set \(R=TV\), a rotation of \(U\). If \(R=U\), then \(U\) is periodic with period \(\gcd(r,d)\), which divides \(n\), making \(w\) a proper power; again a contradiction. Otherwise let \(j<d\) be the first index at which \(R\) and \(U\) differ. Comparing \(w\) with the rotation beginning at position \(kd\) yields the first mismatch at position \(r+j\), between the letters \(R_j\) in \(w\) and \(U_j\) in its rotation. Comparing \(w\) with the rotation beginning at \((k-1)d\) yields the *same directed mismatch* at position \(d+r+j\), after their common prefix \(UV\). The first-mismatch indices differ by the odd integer \(d\), so alternating order demands opposite inequalities. Both rotations therefore cannot be larger than \(w\), a contradiction.

If \(n\) is even and \(b\) is a proper border, Step 1 makes \(b\) odd, hence its complementary period \(d=n-b\) is odd. Step 2 forces \(d>n/2\), equivalently \(2b<n\). For odd \(n\), Step 1 alone gives all necessary exclusions.

**Step 3: witnesses for every permitted length.** Choose two alphabet symbols \(0<1\); all constructions below use only this ordered pair. For every odd \(n=2m+1\) with \(m\ge1\), take \(w=(01)^m0\). Its prefix and suffix agree for every odd length \(1,3,\ldots,2m-1\). This \(w\) is Galois: a rotation beginning with \(1\) loses immediately, while every nonidentity rotation beginning with \(0\) crosses the unique circular junction \(00\) before \(w\) does. At the first discrepancy, the rotated word has \(0\) and \(w\) has \(1\) at an odd zero-based index, so \(w\) is strictly smaller in alternating order.

For even \(n\ge4\), the word \(w=01\,0^{n-2}\) is Galois and has a border of length one. Indeed, every nonidentity rotation either starts with \(1\), or starts with \(00\), losing to \(w\) at the first or second symbol respectively. If \(b\ge3\) is odd and \(2b<n\), write \(d=n-b\), which is odd with \(d\ge b+2\), and take

\[
w=01\,0^{d-1}\,1\,0^{b-2}.
\]

This has length \(n\), begins and ends with \(01\,0^{b-2}\), and therefore has border \(b\). Every nonidentity rotation loses at position zero (if it starts with \(1\)) or position one (if it starts with \(00\)), except the rotation starting at the zero immediately preceding the second \(1\), namely shift \(d\). That rotation agrees with \(w\) up to and including zero-based position \(b\), but at position \(b+1\) it has \(1\), while \(w\) has \(0\), because \(b+1<d+1\). Since \(b+1\) is even, \(w\) is smaller. All nonidentity rotations are thus strictly larger. The case \(n=2\) has no permitted proper border and requires no witness.

Together the exclusion and constructions prove the claimed spectrum for all \(n\) and every such alphabet.

## Verification

The self-contained script `verify_border_spectrum.py` independently compares every binary word of each length from \(2\) through \(16\) against all cyclic rotations, records its proper-border lengths and checks the asserted set. It also verifies that no found Galois word has an odd period of at most half its length. Separately, it constructs and checks every explicit witness for all admissible pairs with \(2\le n\le256\). Execute `python3 verify_border_spectrum.py` using only the Python standard library. The finite checks cover 131,068 candidate words, 8,798 Galois words and 12,224 explicit witness instances. These checks are not a replacement for the proof for unbounded \(n\).

## Relationship to prior work

Reutenauer's Proposition 3.1 (2006) proves the necessary oddness of every proper Galois-word border. Dolce, Restivo and Reutenauer (2019, Lemma 35) reproduce this obstruction and develop generalized Lyndon characterizations. Hendrian, Köppl, Yoshinaka and Shinohara (2024) derive linear-time detection, factorization and rotation methods and analyze odd and even periods, but do not state a complete attainable border-length spectrum. Bannai et al. (2023) identify the distinction between bordered and unbordered Galois words when discussing subsequence algorithms. The present result combines an additional sharp even-length half-word obstruction with explicit realizations of *all* allowed border lengths. It does not claim novelty for the odd-border parity lemma.

## Limitations

This is an existence classification of possible border lengths, not a count of Galois words or of their simultaneous border sets. It does not solve the longest bordered Galois subsequence problem. Its correctness proof is self-contained, but an equivalent classification in unindexed prior literature is still possible.

## References

- C. Reutenauer, *Mots de Lyndon généralisés*, Séminaire Lotharingien de Combinatoire **54**, B54h (2006), Proposition 3.1. https://www.mat.univie.ac.at/~slc/wpapers/s54reut.pdf
- F. Dolce, A. Restivo and C. Reutenauer, *On generalized Lyndon words*, Theoretical Computer Science **777**, 232–242 (2019), Lemma 35. https://arxiv.org/abs/1812.04515
- H. Bannai, T. I, T. Kociumaka, D. Köppl and S. J. Puglisi, *Computing Longest Lyndon Subsequences and Longest Common Lyndon Subsequences*, Algorithmica **86**, 735–756 (2024), first online 2023. https://doi.org/10.1007/s00453-023-01125-z
- D. Hendrian, D. Köppl, R. Yoshinaka and A. Shinohara, *Algorithms for Galois Words: Detection, Factorization, and Rotation*, CPM 2024, Article 18. First publicly posted 2024-03-05. https://arxiv.org/abs/2403.02636
