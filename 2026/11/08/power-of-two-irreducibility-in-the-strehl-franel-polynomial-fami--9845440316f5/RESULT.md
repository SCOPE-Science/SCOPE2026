# Power-of-two irreducibility in the Strehl–Franel polynomial family

## Finding
For every integer \(m\ge1\), with \(n=2^m\), the Strehl–Franel polynomial
\[
F_n(X)=\sum_{k=0}^{n}\binom nk^2\binom{2k}{n}X^{n-k}
\]
is irreducible over \(\mathbb Q\). More precisely, setting \(d=n/2\), its normalized reciprocal \(G_n(X)=\frac12 X^d F_n(1/X)\) is Eisenstein at \(2\). This proves the power-of-two index subfamily of Sun's 2013 irreducibility conjecture, not the whole conjecture.

## Assumptions and scope
All binomial coefficients have their ordinary nonnegative-integer meaning, with \(\binom ab=0\) if \(b>a\). The integer \(m\ge1\) is arbitrary. Irreducibility is over \(\mathbb Q[X]\); no assertion is made for indices not powers of two. The primary classification is 11B65.

## Proof
Write \(F_n(X)=\sum_{j=0}^{d} c_jX^j\), where
\[
c_j=\binom{n}{j}^{\!2}\binom{2(n-j)}{n}.
\]
Indeed, the term with \(k=n-j\) vanishes when \(k<n/2\), so the degree is at most \(d\); it is exactly \(d\) because \(c_d=\binom{n}{n/2}^2>0\).

For a power of two \(n=2^m\), every intermediate binomial coefficient \(\binom{n}{j}\), \(1\le j<n\), is even. One direct proof in \(\mathbb F_2[X]\) is \((1+X)^{2^m}=1+X^{2^m}\). Thus \(4\mid c_j\) for every \(1\le j\le d\). In particular the coefficients of \(G_n\) below its leading term, which are \(c_j/2\), are even.

The coefficient \(c_0=\binom{2n}{n}\) has exact \(2\)-adic valuation one. For instance, Legendre's formula \(\nu_2(t!)=t-s_2(t)\), where \(s_2\) is binary digit sum, gives
\[
\nu_2\binom{2n}{n}=2s_2(n)-s_2(2n)=1.
\]
Hence \(c_0/2\), the leading coefficient of \(G_n\), is odd.

Finally, \(c_d=\binom n{n/2}^2\). The same factorial identity gives \(\nu_2\binom n{n/2}=2s_2(n/2)-s_2(n)=1\), since both arguments are powers of two. Consequently \(\nu_2(c_d/2)=1\), so the constant term of \(G_n\) is divisible by two but not by four.

The three conditions of Eisenstein's criterion at \(2\) are established for \(G_n\). Therefore \(G_n\) is irreducible over \(\mathbb Q\). Since \(F_n(0)=c_0\ne0\) and \(F_n(X)=2X^dG_n(1/X)\), taking reciprocals preserves irreducibility, proving the assertion. This is an infinite proof, with no use of finite extrapolation.

## Verification
The attached standalone verifier recomputes all coefficients for \(m=1,\ldots,8\), validates their exact valuations, and checks the Eisenstein coefficient pattern. Such finite tests corroborate arithmetic but are not part of the proof for arbitrary \(m\).

## Relationship to prior work
Strehl's binomial identity expresses the ordinary Franel numbers as \(F_n(1)\). Sun explicitly conjectured in his March 21, 2013 OEIS A000172 comment that \(F_n(X)\) is irreducible for every \(n\ge2\). The present result resolves only the infinite index family \(n=2^m\). Published investigations of Franel recurrences and binomial power sums do not by themselves imply this reciprocal-Eisenstein property. Irreducibility of a differently normalized or indexed polynomial cannot be assumed equivalent without a coefficient-level change of variables.

## Limitations
The method uses the complete evenness of intermediate binomial coefficients in a power-of-two row, so it provides no general irreducibility result for non-power-of-two indices. Historical priority is not independently certified: undiscovered results may contain this elementary-looking subcase. The strength is a rigorous infinite subfamily of a named conjecture, not a new irreducibility criterion.

## References
Zhi-Wei Sun, comment dated March 21, 2013, OEIS A000172, https://oeis.org/A000172 .
Volker Strehl, *Recurrences and Legendre transform*, Séminaire Lotharingien de Combinatoire B29b (1992), cited at OEIS A000172.
H. Belbachir and F. Otmani, *A Strehl Version of Fourth Franel Sequence*, arXiv:2012.02563 (2020), https://arxiv.org/abs/2012.02563 .
