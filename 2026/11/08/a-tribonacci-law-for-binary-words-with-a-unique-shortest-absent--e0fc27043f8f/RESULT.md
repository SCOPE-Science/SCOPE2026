# A tribonacci law for binary words with a unique shortest absent subsequence

## Finding
Fix the alphabet \(\Sigma=\{0,1\}\), including for words using only one symbol. For a finite word \(w\), a *subsequence* is an order-preserving, not necessarily contiguous selection of positions. Write \(\iota(w)\) for the largest integer \(k\ge0\) such that every member of \(\Sigma^k\) occurs as a subsequence, and write \(\operatorname{SAS}(w)\) for all shortest absent subsequences. They have length \(\iota(w)+1\). For all \(n\ge1\) and \(k\ge0\), put
\[
U_{n,k}=\bigl|\{w\in\Sigma^n:\iota(w)=k,\ |\operatorname{SAS}(w)|=1\}\bigr|.
\]
Then the **complete length-and-universality census** is
\[
\boxed{\sum_{n\ge1}\sum_{k\ge0}U_{n,k}z^nu^k=\frac{2z}{1-z-uz^2-uz^3}.}
\]
Explicitly, for \(n\ge2k+1\),
\[
U_{n,k}=2\sum_{j=0}^{\min(k,n-2k-1)}\binom{k}{j}\binom{n-k-1-j}{k},
\]
and \(U_{n,k}=0\) otherwise. The total \(U_n=\sum_kU_{n,k}\) satisfies \(U_1=2\), \(U_2=2\), \(U_3=4\) and
\[
U_n=U_{n-1}+U_{n-2}+U_{n-3}\qquad(n\ge4).
\]
The initial totals are \(2,2,4,8,14,26,48,88,162,298,548,1008\). If \(\lambda>1\) is the real root of \(\lambda^3=\lambda^2+\lambda+1\), the probability that a uniformly random binary length-\(n\) word has exactly one SAS is
\[
\frac{U_n}{2^n}\sim\frac{2}{1+2/\lambda+3/\lambda^2}\left(\frac{\lambda}{2}\right)^n,
\]
so uniqueness becomes exponentially rare. The scalar tribonacci sequence itself occurs in unrelated enumerations; the claim concerns its fixed-alphabet SAS interpretation and, especially, the bivariate distribution.

## Assumptions and scope
Words are indexed linear words, not rotation classes. The alphabet is fixed to \(\{0,1\}\), so the words \(0^r\) and \(1^r\) each have the one-letter missing subsequence consisting of the opposite bit. The empty source word is excluded: it has two SAS of length one. A word with both symbols and a shortest absent length of \(k+1\) has universality index exactly \(k\). All claims are exact for every positive integer length, not an extrapolation from finite data.

## Proof
**1. First-occurrence recurrence.** For a word \(s\), let \(L(s)\) be the minimum length of an absent binary subsequence and \(c(s)\) the number of absent subsequences at that length. In particular \(L(\varepsilon)=1\), \(c(\varepsilon)=2\). Every nonunary word can be written uniquely as \(w=x^ry t\), where \(x,y\in\Sigma\) are opposite symbols, \(r\ge1\), and the displayed \(y\) is the first occurrence of the symbol opposite to \(x\).

For each possible initial symbol of an absent subsequence, remove its *first* occurrence in \(w\): a subsequence beginning with \(x\) is absent precisely when its tail is absent from \(w[2..]\), whereas one beginning with \(y\) is absent precisely when its tail is absent from \(t\). Since \(t\) is a suffix of \(w[2..]\), we have \(L(w[2..])\ge L(t)\), and therefore
\[
L(w)=1+L(t),\qquad
c(w)=c(t)+\mathbf1_{L(w[2..])=L(t)}c(w[2..]).
\]
This follows from a partition by the first symbol and uses **distinct** subsequences, not counts of embeddings.

**2. Unique-SAS grammar.** If \(r\ge2\), the suffix \(w[2..]=x^{r-1}yt\) still has both symbols, so \(L(w[2..])=1+L(t)>L(t)\); thus \(c(w)=c(t)\). If \(r=1\), the suffix is \(yt\). If \(c(t)=1\) with unique missing shortest word \(v\), then \(L(yt)>L(t)\) holds precisely when \(v\) starts with \(y\): every word of length \(L(t)-1\) occurs in \(t\), so prepending \(y\) can supply the formerly missing word exactly when its first symbol is \(y\). If \(t\) has two or more shortest absent subsequences, then \(c(w)\ge c(t)>1\), independently of the prefix.

For every *nonempty* word with \(c(t)=1\), its unique SAS begins with the bit opposite to its own first bit. This is immediate for unary words. Inductively, the recurrence above shows that for a nonunary unique-SAS word \(t=x^ry s\), the only shortest absent subsequence begins with \(y\), opposite the first symbol of \(t\). Hence in the \(r=1\) case for \(w=xyt\), the condition that the unique SAS of \(t\) starts with \(y\) is equivalent to the first bit of \(t\) being \(x\).

Consequently the complete unambiguous recursive grammar for \(c(w)=1\) is: (i) every nonempty unary word qualifies; (ii) for the unique first-arch decomposition \(w=x^ryt\), the tail \(t\) must be a nonempty qualifying word and either \(r\ge2\), or \(r=1\) and \(t\) starts with \(x\). An empty tail never qualifies because \(c(\varepsilon)=2\). The first-arch recurrence also shows that \(\iota(w)=1+\iota(t)\) for each nonunary word, while unary words have index zero.

**3. Weighted enumeration.** Let \(F(z,u)\) enumerate qualifying nonempty words whose first symbol is a fixed bit, with \(z\) marking word length and \(u\) marking universality index. Complementation gives the same series for both first bits. The unary words contribute \(z/(1-z)\). For \(r=1\), the first arch has length two and the tail must start with the same initial bit, contributing \(uz^2F\). For \(r\ge2\), the first arch has length at least three and the qualifying tail may start with either bit, contributing \(2uz^3F/(1-z)\). The decomposition is disjoint and exhaustive, hence
\[
F=\frac{z}{1-z}+uz^2F+\frac{2uz^3}{1-z}F,
\qquad 2F=\frac{2z}{1-z-uz^2-uz^3}.
\]
This proves the bivariate formula. Extracting \(u^k\) yields \(2z^{2k+1}(1+z)^k/(1-z)^{k+1}\), whose binomial expansion gives the displayed coefficient formula. Setting \(u=1\) gives the scalar tribonacci recurrence. The dominant simple pole at \(z=1/\lambda\) gives the asymptotic coefficient constant stated above; the other two characteristic roots have smaller modulus.

## Verification
`verify.py` independently enumerates all \(8190\) nonempty binary words through length \(12\); it tests the occurrence of **each** binary subsequence candidate, constructs the literal set of shortest absent words, and compares every outcome against the recursive grammar and every length/index coefficient. The successful check prints `DIRECT_GRAMMAR_VERIFY_OK`.

`verify_fast.cpp` performs independent shortest-absent dynamic programming by position and first-occurrence indices, not the combinatorial grammar. It exhaustively enumerates all binary words at every length \(1\) through \(22\) and compares every bivariate coefficient with the recurrence from the rational function. The successful check prints `DYNAMIC_CENSUS_VERIFY_OK`. These finite checks corroborate the proof; the all-length result follows from the first-occurrence recurrence and bijective grammar, not from experimental extrapolation.

To reproduce: `python3 verify.py`; `g++ -std=c++17 -O3 verify_fast.cpp -o verify_fast && ./verify_fast`.

## Relationship to prior work
Abraham, Brockman, Sapp and Godbole introduced and counted omnibus subsequence properties and studied expected numbers of missing words; their paper includes exact counts of fully universal words. It does not enumerate words with exactly one shortest missing subsequence. Kosche, Koß, Manea and Siemer developed shortest absent subsequences and algorithms to compute them for a **given** word.

Fleischmann, Haschke, Huch, Mayrock and Nowotka gave a full characterization of **1-nearly \(k\)-universal words** and their Simon-congruence classes. In particular their Theorem 16 is a stronger general-alphabet membership characterization for the underlying objects, so this work does **not** claim the existence or membership structure of 1-nearly universal words as new. Its distinct claim is the all-length binary enumeration of individual source words, refined by their universality index; the cited characterization does not state these coefficients or the bivariate series. Related work on universality-index distributions counts all words by index, without conditioning on a unique SAS. Adamson and collaborators establish shortest feasible lengths and extremal missing-count properties, not the present full length distribution.

The scalar totals coincide, after an index shift, with pre-existing tribonacci sequences such as OEIS A135491 and A354784. Their published meanings concern other combinatorial objects, and the integer sequence or its standard recurrence is **not** claimed as a discovery. The binary unique-SAS interpretation, its recursive grammar and the refined rational generating function are the substantive statements compared here.

## Limitations
The proof is specific to fixed-alphabet binary linear words and counts a unique **shortest** absent subsequence, not arbitrary minimal absent subsequences. It does not provide a general \(q\)-ary series. The pre-existing general-alphabet characterization makes historical priority for any concise binary reformulation a meaningful risk; an indexed search cannot exclude other independently derived counting formulas. No external scientific audit has been conducted.

## References
1. S. Abraham, G. Brockman, S. Sapp, A. P. Godbole, *Omnibus Sequences, Coupon Collection, and Missing Word Counts*, arXiv:0905.4517v1, first public 2009-05-27. https://arxiv.org/abs/0905.4517
2. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968v1, 2021-08-31. https://arxiv.org/abs/2108.13968
3. P. Fleischmann, L. Haschke, A. Huch, A. Mayrock, D. Nowotka, *m-Nearly k-Universal Words — Investigating Simon Congruence*, arXiv:2202.07981v1, 2022-02-16. https://arxiv.org/abs/2202.07981
4. D. Adamson and collaborators, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599v1, 2024-07-26. https://arxiv.org/abs/2407.18599
5. *Closed-form law for binary subsequence universality*, published mathematical research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37
6. *Fibonacci extremals for shortest absent subsequences of binary words*, published mathematical research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-fibonacci-extremals-for-shortest-absent-subsequences-of-binary-w--1a6556f14d28
7. OEIS A135491, https://oeis.org/A135491; OEIS A354784, https://oeis.org/A354784.
