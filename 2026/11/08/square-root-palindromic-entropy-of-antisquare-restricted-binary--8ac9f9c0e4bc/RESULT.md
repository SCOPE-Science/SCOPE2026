# Square-root palindromic entropy of antisquare-restricted binary words

## Finding

Call a finite binary word **good** if it has no contiguous antisquare of order at least two: no factor of the form \(u\overline{u}\), where \(u\in\{0,1\}^m\), \(m\ge 2\), and the bar exchanges zero and one. Thus the length-two antisquares `01` and `10` are permitted. Let \(G_n\) be the number of good binary words of length \(n\), and \(P_n\) the number of those that equal their reversals. Let \(\psi\) be the unique real root greater than one of \(\psi^3=\psi^2+1\) (approximately \(1.465571231876768\)).

**Theorem.** There are absolute positive constants \(c,C\) such that for every integer \(n\ge1\),
\[
c\psi^{n/2}\le P_n\le C\psi^{n/2}.
\]
Consequently,
\[
\lim_{n\to\infty}\frac{\log P_n}{n}=\frac{\log\psi}{2},
\qquad
\frac{P_n}{G_n}=\Theta(\psi^{-n/2}).
\]
In particular, the exponential growth base for palindromic good words is \(\sqrt{\psi}\approx1.210607794406086\), exactly the square root of that for all good words.

An explicit lower-bound family is supplied: for each \(h\ge0\), there are at least \(2T_h\) good palindromes of each length \(2h+7\) and \(2h+8\), where
\[
\sum_{h\ge0}T_hz^h=\frac1{1-z-z^4-z^6}.
\]

## Assumptions and scope

The alphabet is precisely the labeled binary alphabet \(\{0,1\}\), reversal fixes each letter, and factors are contiguous. The count includes the constant palindromes. All lengths are positive integers. The result is a two-sided growth-rate statement and does not claim a closed formula for the individual values of \(P_n\).

For a nonempty binary word \(w=w_0\cdots w_{n-1}\), its **change code** \(\Delta(w)=p_0\cdots p_{n-2}\) is defined by \(p_i=1\) precisely when \(w_i\ne w_{i+1}\). It has exactly two preimages, distinguished by their first letter. Put
\[
\mathcal Q=\{010,101,11111,01110\}.
\]

## Proof

**Step 1: finite forbidden core.** Baranwal, Currie, Mol, Ochem, Rampersad and Shallit [1, Theorem 11 and Section 7] prove that any binary word avoiding

`0011`, `1100`, `0110`, `1001`, `010101`, `101010`, `001011`, `110100`

is good. The eight forbidden factors are exactly the two first-letter preimages under \(\Delta\) of the four words in \(\mathcal Q\): respectively the pairs corresponding to `010`, `101`, `11111` and `01110`. Therefore every binary word whose change code avoids \(\mathcal Q\) is good. This is a sufficient condition, not asserted to be necessary for goodness.

**Step 2: an exponentially large reversible code.** Consider the three-block prefix code
\[
\mathcal B=\{0,1100,111100\}.
\]
Each concatenation \(v\in\mathcal B^*\) has maximal runs of ones of length two or four, and any two such runs are separated by at least two zeros. Consequently it avoids \(\mathcal Q\): `010` and `101` demand an isolated one or zero, `11111` demands five consecutive ones, and `01110` demands an interior run of exactly three ones. The same argument holds for the reversal \(v^R\).

For \(r\in\{6,7\}\), set \(p(v,r)=v0^rv^R\). The central run of at least six zeros ensures that no forbidden factor in \(\mathcal Q\) can cross between \(v\) and \(v^R\); none is created at either junction. Hence \(p(v,r)\) avoids \(\mathcal Q\). This code is a palindrome and contains an even number of ones. Let \(w(v,r,a)\) be the unique binary word with change code \(p(v,r)\) and initial letter \(a\in\{0,1\}\). Its first and last letters agree because the total number of changes is even. Reversal preserves its change code, so the initial-letter uniqueness implies \(w(v,r,a)=w(v,r,a)^R\). By Step 1, it is good.

If \(|v|=h\), these two choices of \(a\) give different words of length \(2h+r+1\). Different choices of \(v\) also give different words since their change codes have different length-\(h\) prefixes. Thus, with \(T_h\) the number of concatenations from \(\mathcal B\) of length \(h\),
\[
P_{2h+7}\ge 2T_h,\qquad P_{2h+8}\ge 2T_h.
\]

**Step 3: exact growth of the construction.** The blocks in \(\mathcal B\) have lengths one, four and six and are prefix-free, so the concatenations have unique parsing. Therefore \(T_0=1\), \(T_h=0\) for negative \(h\), and
\[
T_h=T_{h-1}+T_{h-4}+T_{h-6}.
\]
The positive dominant growth root satisfies \(\lambda^6=\lambda^5+\lambda^2+1\), and
\[
\lambda^6-\lambda^5-\lambda^2-1
=(\lambda+1)(\lambda^2-\lambda+1)(\lambda^3-\lambda^2-1).
\]
The nonnegative recurrence is aperiodic because its allowed block lengths include one; equivalently the generating function has a unique dominant simple pole on its circle of convergence. Thus \(T_h=\Theta(\psi^h)\), uniformly over the integers \(h\ge0\). Step 2 yields \(P_n=\Omega(\psi^{n/2})\) separately for odd and even \(n\), and positive constants absorb the finitely many smaller values of \(n\).

**Step 4: sharp upper bound and proportion.** Every palindrome of length \(n\) is determined by its first \(\lceil n/2\rceil\) letters. Goodness is inherited by contiguous factors, so this first half must itself be good. Therefore
\[
P_n\le G_{\lceil n/2\rceil}.
\]
The unrestricted enumeration theorem [1, Theorem 19] gives \(G_m=\Theta(\psi^m)\). This supplies \(P_n=O(\psi^{n/2})\). Dividing the two-sided bound by the same published bound for \(G_n\) proves the stated density estimate. Taking logarithms gives the limit. \(\square\)

## Verification

The standalone `verify.py` exhaustively enumerates palindromic good words through length \(24\), checks both change-code/preimage forbidden sets exhaustively through length \(12\), confirms every generated lower-bound witness through block length \(13\), and checks the block recurrence and distinctness. The finite computations are consistency tests; the infinite theorem follows from the proof and the cited unrestricted-growth theorem.

## Relationship to prior work

[1] established the unconstrained \(\Theta(\psi^n)\) count, a minimal-antisquare classification, and the finite forbidden-code reduction. Those facts alone give an upper bound but do not establish the matching palindromic lower bound. The new point is the explicit palindrome-preserving center construction and the resulting sharp asymptotic restriction to reversal-fixed words. The periodic-point enumeration of the same avoidance system concerns words under shift iteration, not finite palindromic words; periodic counts do not determine \(P_n\). General studies of palindromic factor complexity [3] concern palindromic factors inside a fixed infinite word, another invariant.

## Limitations

This result determines the exponential rate and matching constant-factor order, not exact counts \(P_n\), a leading multiplicative asymptotic constant, or a limiting ratio after exponential normalization. Its lower bound uses a regular sublanguage of good words; exceptional finite good words outside that sublanguage are included in the upper bound. The argument relies on the published unrestricted good-word growth theorem [1], while the new lower construction is proved directly. Computational testing is finite and not a substitute for infinite proof. No independent audit has been performed.

## References

[1] A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad, J. Shallit, *Antisquares and Critical Exponents*, arXiv:2209.09223, first public version 2022-09-19, Sections 6–7, especially Theorem 19. https://arxiv.org/html/2209.09223v3

[2] T. Ng, P. Ochem, N. Rampersad, J. Shallit, *New Results on Pseudosquare Avoidance*, arXiv:1904.09157 (2019). https://arxiv.org/html/1904.09157v1

[3] E. Pelantová, Š. Starosta, *Languages invariant under more symmetries: overlapping factors versus palindromic richness*, arXiv:1103.4051 (2011). https://arxiv.org/abs/1103.4051
