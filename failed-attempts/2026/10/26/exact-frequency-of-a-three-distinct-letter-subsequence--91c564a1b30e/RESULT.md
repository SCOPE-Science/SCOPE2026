# Exact frequency of a three-distinct-letter subsequence

## Finding

Let \(\Sigma\) be a finite alphabet with \(|\Sigma|=m\ge3\), and let \(p=p_1p_2p_3\) consist of three pairwise distinct symbols of \(\Sigma\). An occurrence of \(p\) in a word \(w=w_1\cdots w_n\) is a triple of indices \(i<j<k\) with \((w_i,w_j,w_k)=(p_1,p_2,p_3)\). Let \(B_{n,p}(2)\) be the number of words in \(\Sigma^n\) with exactly two such occurrences. Then

\[
\boxed{\sum_{n\ge0}B_{n,p}(2)x^n=
\frac{x^4\bigl(3-(3m-8)x\bigr)}{(1-(m-3)x)(1-(m-1)x)^2(1-(m-2)x)^3}.}
\]

In particular, the answer depends on \(p\) only through the condition that its three symbols are distinct, and on the alphabet only through \(m\). The coefficient is zero for \(n<4\).

## Assumptions and scope

Occurrences are literal subsequences: symbols must match in the order \(p_1,p_2,p_3\), with arbitrary gaps allowed. They are not occurrences defined by relative order or by consecutive factors. The alphabet is finite, \(m\ge3\), and the three pattern symbols are distinct. No claim is made for repeated-symbol patterns, longer patterns, or occurrence counts other than two.

## Proof

Relabel the three pattern symbols as \(0,1,2\). First count words over \(\{0,1,2\}\). For each position \(j\) carrying a \(1\), let \(Z_j\) be the number of zeros before \(j\), and let \(T_j\) be the number of twos after \(j\). Then

\[
c_{012}(w)=\sum_{j:w_j=1} Z_jT_j.
\]

If this sum equals two, precisely one of the following disjoint cases occurs: (A) one position contributes two, with \((Z_j,T_j)=(1,2)\) or \((2,1)\); or (B) two positions each contribute one, so both have \((Z_j,T_j)=(1,1)\). In case B, the two ones must be adjacent: a zero between them would raise the later zero-count, and a two between them would raise the earlier two-count.

For case A with \((Z_j,T_j)=(1,2)\), every such word has the unique form
\[
u\,0\,2^a\,1\,0^i2\,0^j2\,v,
\]
where \(u\in\{1,2\}^*\), \(v\in\{0,1\}^*\), and \(a,i,j\ge0\). Its generating function is \(x^4/((1-2x)^2(1-x)^3)\). The case \((Z_j,T_j)=(2,1)\) has the unique form
\[
u\,0\,2^a\,0\,2^b\,1\,0^c2\,v,
\]
with \(u\in\{1,2\}^*\), \(v\in\{0,1\}^*\), and \(a,b,c\ge0\), giving the same generating function. In case B the unique form is
\[
u\,0\,2^a\,11\,0^b2\,v,
\]
with \(u\in\{1,2\}^*\), \(v\in\{0,1\}^*\), and \(a,b\ge0\), giving \(x^4/((1-2x)^2(1-x)^2)\). Therefore the ternary generating function is
\[
F_3(x)=\frac{2x^4}{(1-2x)^2(1-x)^3}+\frac{x^4}{(1-2x)^2(1-x)^2}
=\frac{x^4(3-x)}{(1-2x)^2(1-x)^3}.
\]

For an alphabet of size \(m\), the \(m-3\) symbols outside the pattern cannot occur in an occurrence of \(p\). Delete them from a word to obtain its unique ternary core. If the core has length \(t\), arbitrary strings of neutral symbols may be inserted in its \(t+1\) gaps, contributing a factor \((1-(m-3)x)^{-(t+1)}\). Hence
\[
F_m(x)=\frac{1}{1-(m-3)x}F_3\!\left(\frac{x}{1-(m-3)x}\right),
\]
which simplifies to the boxed formula. This also proves the coefficient vanishes for \(n<4\).

## Verification

The proof partitions every word with exactly two occurrences according to the positive summands \(Z_jT_j\); the three cases are disjoint and their displayed word forms are unique. The file `verify.py` independently enumerates words and checks the generating-function coefficients for \(m=3,4\) through length eight. Those finite checks are consistency tests, not the proof for all lengths; the all-length result follows from the case classification and gap-insertion argument above.

## Relationship to prior work

Menon and Singh study exact subsequence frequencies for binary words, including explicit formulas for up to four occurrences, and identify extension to larger alphabets as a natural direction. The present statement is a specific exact formula for a three-symbol literal subsequence over an arbitrary alphabet size. Bruda gives a later structural theorem for binary words and discusses an \(m\)-ary frequency conjecture; the accessible statement concerns the polynomial-exponential form and does not state this exact generating function. An in-preparation automaton treatment mentioned there may contain overlapping special cases, so novelty beyond the accessible published statements remains subject to that limitation. Some other work on patterns in words uses order-isomorphic occurrences, which is a different counting convention.

## Limitations

The formula is restricted to a length-three pattern with three distinct symbols and exactly two literal subsequence occurrences. It does not resolve the general \(m\)-ary frequency problem. The cited in-preparation work is not publicly inspectable here, and the novelty assessment is therefore provisional pending independent review.

## References

1. K. Menon and A. Singh, “Subsequence frequency in binary words,” arXiv:2306.07870v1 (first public version, 2023-06-13); published in *Discrete Mathematics* 347 (2024), 113928. https://arxiv.org/abs/2306.07870
2. G. Bruda, “Enumerating binary words restricted by subsequence frequency,” arXiv:2607.02578v1 (2026-06-30), especially §4.1 on the proposed \(m\)-ary extension. https://arxiv.org/abs/2607.02578
3. T. Mansour, R. Rastegar, and A. Roitershtein, “Finite automata, probabilistic method, and occurrence enumeration of a pattern in words and permutations,” arXiv:1905.05646 (2019). Its occurrence convention is order-isomorphism, unlike the literal subsequences counted here. https://arxiv.org/abs/1905.05646
4. T. Mansour and R. Rastegar, “Pattern occurrences in \(k\)-ary words revisited: A few new and old observations,” *Journal of Combinatorial Theory, Series A* 188 (2022), 105596. https://doi.org/10.1016/j.jcta.2022.105596
