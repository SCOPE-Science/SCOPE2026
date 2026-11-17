# Divisor-valued ambiguity fibres of binary two-gapped decks at four runs

## Finding
For a nonempty finite binary word \(w=w_1\cdots w_n\), observe the multiset of its one-letter subsequences and the multiset of its length-two subsequences \(w_iw_j\) for \(1\le i<j\le n\) and \(j-i\ge2\). This is the full *two-gapped two-deck*. Write \(G_{xy}(w)\) for the multiplicity of the pair \(xy\), and \(A=|w|_0\), \(B=|w|_1\). A *fibre* is the set of all binary words, with no prior restriction on their number of runs, having the same observation.

**Theorem.** If \(w\) has at most three maximal constant runs, its fibre has size one, except that `01` and `10` form a single two-word fibre. Suppose instead that \(w\) has exactly four runs. Define, for every integer \(h\),
\[
R_{A,B}(h)=\#\{(u,v)\in\mathbb Z^2:1\le u<A,\ 1\le v<B,\ uv=h\}.
\]
Then its *exact* fibre size is
\[
\boxed{\ F(w)=R_{A,B}(G_{10}(w)+1)+R_{A,B}(G_{01}(w)+1).\ }
\]
Every word in this fibre has exactly four runs. Both summands count disjoint sets of strings, separated by their first letter.

For fixed \(A,B\ge2\), put
\[
P_{A,B}=\{uv:1\le u<A,\ 1\le v<B\},\qquad M=AB-1.
\]
The number of distinct two-gapped two-decks among all four-run words with these letter counts is exactly
\[
\boxed{\ 2|P_{A,B}|-|P_{A,B}\cap(M-P_{A,B})|,\ }
\]
where \(M-P_{A,B}=\{M-p:p\in P_{A,B}\}\). In particular, the reconstruction code taking one representative from each such deck can attain precisely this size.

Finally, if \(\tau(K)\) is the number of positive divisors of \(K\), then **for every \(K\ge1\)** there exists a four-run binary two-gapped-two-deck fibre of size exactly \(\tau(K)\), at composition \(A=B=K+1\). Thus four runs permit unbounded ambiguity, although three runs do not (apart from the length-two exception).

## Assumptions and scope
All words are *linear*, not cyclic, and their symbols are labeled \(0\) and \(1\). Both lengths one and two belong to the observed gapped deck; in particular, \(A\) and \(B\) are known. A pair is included if and only if its two positions are separated by at least two, so adjacent pairs are excluded. A constant run means a nonempty maximal contiguous block of one symbol. No assumption of known run count is supplied to the decoder: the proof reconstructs the run counts from the deck. The formula counts distinct words, not distinct subsequence embeddings.

## Proof
**1. Run counts are observables.** Let \(r_0\) and \(r_1\) be the respective numbers of zero-runs and one-runs, with a missing symbol having zero runs. Among all \(\binom A2\) unordered pairs of zero positions, precisely \(A-r_0\) pairs consist of adjacent positions, because every zero-run of length \(\ell\) contains exactly \(\ell-1\) such pairs. Therefore
\[
G_{00}=\binom A2-A+r_0,\quad
G_{11}=\binom B2-B+r_1,
\]
and hence
\[
r_0=A-\binom A2+G_{00},\qquad
r_1=B-\binom B2+G_{11}.
\]
Thus the total number \(t=r_0+r_1\) of runs and the numbers of runs of each symbol are uniquely fixed by the observed deck, even among unrestricted candidate reconstructions. Each of the \(AB\) pairs involving opposite symbols is oriented either \(01\) or \(10\). Exactly \(t-1\) of those pairs is adjacent, so
\[
G_{01}+G_{10}=AB-t+1.\tag{1}
\]

**2. At most three runs.** A one-run word is determined by its singleton deck. Two-run words are \(0^A1^B\) and \(1^B0^A\), whose cross-pair counts are respectively \((G_{01},G_{10})=(AB-1,0)\) and \((0,AB-1)\). The only equality occurs when \(A=B=1\), giving `01` and `10`.

If there are three runs, the already recovered \((r_0,r_1)\) determines which symbol occupies the two outside runs. For a word \(0^a1^B0^c\) with \(a,c\ge1\), the observed count \(G_{01}=aB-1\) gives \(a=(G_{01}+1)/B\) and then \(c=A-a\). The other orientation \(1^b0^A1^d\) has \(G_{01}=Ad-1\), giving \(d=(G_{01}+1)/A\) and \(b=B-d\). Thus every three-run word is uniquely reconstructible, including against candidate words of any run count by step 1.

**3. Four-run fibres.** Here \(r_0=r_1=2\) and \(A,B\ge2\). If the word starts in zero, it has the unique form \(0^a1^b0^c1^d\) with \(a+c=A\), \(b+d=B\), and all run lengths positive. The only ordered \(10\) scattered pairs come from the first one-run and second zero-run. Of these \(bc\) pairs, exactly one is adjacent, whence
\[
G_{10}=bc-1.\tag{2}
\]
Conversely, every divisor pair \(1\le c<A\), \(1\le b<B\) satisfying \(bc=G_{10}+1\) gives exactly one such word: \(a=A-c\), \(d=B-b\). Equation (1) and the fixed values of \(r_0,r_1,A,B\) imply that all other observed pair counts are then automatically correct. Thus precisely \(R_{A,B}(G_{10}+1)\) zero-starting words realize the deck.

If the word starts in one, it has form \(1^d0^c1^b0^a\), with the middle zero-run and middle one-run now contributing exactly \(bc-1\) nonadjacent \(01\) pairs. The identical argument yields \(R_{A,B}(G_{01}+1)\) one-starting reconstructions. These families cannot overlap, proving the fibre formula.

**4. Number of observable four-run profiles.** Let \(p=G_{10}+1\) and \(M=AB-1\). By equation (1), \(G_{01}+1=M-p\). A zero-starting reconstruction exists exactly when \(p\in P_{A,B}\), while a one-starting reconstruction exists exactly when \(M-p\in P_{A,B}\). Other deck coordinates are fixed by \(A,B,r_0,r_1\). Consequently, distinct four-run observations correspond bijectively to the union \(P_{A,B}\cup(M-P_{A,B})\). Inclusion-exclusion gives the second boxed formula.

**5. Arbitrarily large fibres.** Choose any \(K\ge1\), set \(A=B=K+1\), and select a profile with \(p=G_{10}+1=K\). Such a profile is attainable because \(K=K\cdot1\), with both factors smaller than \(K+1\). Every positive divisor of \(K\) supplies exactly one permissible factor pair and vice versa, so \(R_{K+1,K+1}(K)=\tau(K)\). Its reflected parameter is
\[
M-p=(K+1)^2-1-K=K(K+1)>K^2,
\]
whereas every factor pair in \(P_{K+1,K+1}\) has product at most \(K^2\). Hence the reflected contribution is zero, and the fibre contains exactly \(\tau(K)\) words. Since the divisor function is unbounded, the ambiguity is unbounded.

## Verification
A standalone standard-library Python program `verify.py` enumerates the *literal* observed deck, from all position pairs of separation at least two, independently of the proof's run-algebra formulas. For all binary source lengths \(1\le n\le18\) it groups every word with at most four runs by its actual deck, checks that each group's size equals the stated fibre formula, and checks that the deck recovers both run counts. In total the program compares **8,094 words** in **5,611** observed low-run classes. It also checks the multiplication-table class-count identity for all \(2\le A,B\le24\) and the divisor-family fibre formula for every \(1\le K\le120\). A successful execution prints `VERIFY_OK`.

These finite tests independently corroborate the theorem; they are not used to infer the infinite result, which follows from the full run decomposition and arithmetic bijections above.

## Relationship to prior work
Golm, Nahvi, Gabrys, and Milenkovic introduced the same two-gapped deck observation, including both singleton and separated-pair counts (their \(\mathcal B^{(2)}\)), and gave constructions and bounds for general gapped reconstruction. Their arXiv full text explicitly reports the smallest confusable binary length \(G(2)=6\) and a confusable six-letter pair. That already-known threshold and its example are **not** claimed as new here. The present result is a different, exact inverse classification: all fibres at up to four constant runs, a divisor-pair formula, an exact multiplication-table code size, and an unbounded-multiplicity family; the inspected statements of their paper do not imply those formulae.

Related published binary read-length-two classifications address the multiset of *adjacent* ordered pairs, or the compositions of *contiguous* substrings of lengths at most two. Those observation models differ: the present gapped deck subtracts adjacency from all scattered pairs while also retaining one-letter counts. Their run-count formulas do not determine the multiplicative middle-run invariant in equation (2), and they do not state the fibre expression above.

## Limitations
This theorem does not classify fibres with five or more runs, higher gaps, longer scattered subsequences, nonbinary alphabets, or noise. The multiplication-table formula is exact but does not claim a new asymptotic evaluation of its intersection term. The first confusable length six is previously known. An unindexed exact low-run inversion formula may exist; the literature and published-record searches cannot prove uniqueness of a claim. Independent scientific validation has not been performed.

## References
1. J. Golm, M. Nahvi, R. Gabrys and O. Milenkovic, *The Gapped \(k\)-Deck Problem*, arXiv:2201.12671v1 (first public 2022-01-29), full-text version arXiv:2201.12671v2, 2022. https://arxiv.org/html/2201.12671v2 ; DOI:10.1109/ISIT50566.2022.9834537.
2. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548, 2018; IEEE Transactions on Information Theory 65(12), 2019. https://arxiv.org/abs/1804.04548.
3. Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963, 2022. https://arxiv.org/abs/2208.14963.
