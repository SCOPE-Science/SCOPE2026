# The complete scattered-palindrome spectrum of cyclic permutation words

## Finding
For every integer \(q\ge3\), let \(\Sigma_q=\{0,1,\ldots,q-1\}\), and let \(W_{q,n}\) be the first \(n\ge0\) symbols of the periodic infinite word \((0\,1\,\cdots\,(q-1))^\omega\). A *scattered subsequence* selects strictly increasing positions; two selections spelling the same word count once. A *palindrome* is a word unchanged by reversal. Let \(P_q(n,\ell)\) count **distinct nonempty palindromes of length \(\ell\ge1\)** occurring as scattered subsequences of \(W_{q,n}\).

The complete bivariate generating function, with \(z\) recording host-prefix length and \(t\) recording palindrome length, is
\[
\boxed{\sum_{n\ge0}\sum_{\ell\ge1}P_q(n,\ell)z^nt^\ell
=\frac{z(1-z^q)t(1+t z^q)}{(1-z)^2(1-t^2z^q(q-1+z^q))}.}
\]
In particular, for \(P_q(n)=\sum_{\ell\ge1}P_q(n,\ell)\),
\[
\boxed{\sum_{n\ge0}P_q(n)z^n
=\frac{z(1-z^{2q})}{(1-z)^2(1-(q-1)z^q-z^{2q})}.}
\]

For \(r\ge0\), the exact odd-length coefficients are
\[
P_q(n,2r+1)=\sum_{a=0}^{q-1}\sum_{e=0}^{r}
\binom re(q-1)^{r-e}\,\mathbf1_{\{n\ge a+1+q(r+e)\}}.
\]
For \(r\ge1\), the exact even-length coefficients are
\[
P_q(n,2r)=\sum_{a=0}^{q-1}\sum_{e=0}^{r-1}
\binom{r-1}e(q-1)^{r-1-e}\,\mathbf1_{\{n\ge a+1+q(r+e)\}}.
\]
The formulas remain valid with zero counts when \(\ell>n\) and with \(P_q(0,\ell)=0\).

As a growth consequence, setting \(\lambda_q=\frac{q-1+\sqrt{(q-1)^2+4}}2\) yields
\[
\lim_{n\to\infty}P_q(n)^{1/n}=\lambda_q^{1/q}.
\]
All statements are invariant under any permutation of the alphabet applied consistently to the periodic block.

## Assumptions and scope
The alphabet is labeled with precisely \(q\ge3\) symbols and the host is the indicated **linear prefix** of a periodically repeated permutation, not a circular host allowing arbitrary rotation. The count is of distinct subsequence strings, **not** indexed occurrences, and excludes the empty palindrome. Parameters are integer \(n\ge0\), \(\ell\ge1\). Formal power series are over the integers for fixed \(q\); no analytic convergence is required to establish the generating identities.

## Proof
**1. Greedy earliest embedding.** For symbols \(x,y\in\Sigma_q\), define \(d_q(x,y)\) as the unique integer in \(\{1,\ldots,q\}\) congruent to \(y-x\pmod q\). A nonempty word \(v=v_1\cdots v_h\) first occurs as a scattered subsequence in the prefix of length
\[
L_q(v)=v_1+1+\sum_{i=1}^{h-1}d_q(v_i,v_{i+1}).
\]
Indeed, the first occurrence of \(v_1\) in the infinite host is at zero-based position \(v_1\), and each next greedy match is exactly \(d_q(v_i,v_{i+1})\) positions later. By induction greedy always finishes no later than any other embedding. Consequently \(v\) occurs in \(W_{q,n}\) if and only if \(L_q(v)\le n\).

**2. Palindromic cancellation.** The two directed distances between distinct symbols sum to \(q\), while \(d_q(x,x)=q\) makes the two distances sum to \(2q\). Every palindrome is uniquely determined by its first half (and middle letter when odd), so its adjacent transitions pair under reflection. For an odd palindrome of length \(2r+1\), let its first \(r+1\) letters start with \(a\), and let \(e\) be the number of equal consecutive pairs among those first \(r+1\) letters. There are \(r\) mirror-pairs of directed transitions, of which \(e\) contribute \(2q\) and the remaining \(r-e\) contribute \(q\). Thus
\[
L_q(v)=a+1+q(r+e).
\]
For an even palindrome of length \(2r\), its first \(r\) letters have \(r-1\) adjacent pairs, of which \(e\) are equal, and the central equal-letter transition contributes another \(q\). Again \(L_q(v)=a+1+q(r+e)\).

**3. Complete enumerations.** For fixed initial letter \(a\), each of \(s\) steps in a first-half string has one repeat choice or \(q-1\) change choices. Exactly \(e\) repeats occur in \(\binom se(q-1)^{s-e}\) such strings. Take \(s=r\) for length \(2r+1\) and \(s=r-1\) for length \(2r\). Since each first half specifies exactly one different palindrome, the two displayed coefficient formulas are exhaustive and have no duplicate strings.

**4. Generating function.** A palindrome first appearing at prefix length \(L\) occurs in every later prefix, and contributes \(z^L/(1-z)\) to the host-length series. Summing over first letters gives
\[
\frac1{1-z}\sum_{a=0}^{q-1}z^{a+1}=\frac{z(1-z^q)}{(1-z)^2}.
\]
Summing independent repeat/change steps gives the block factor \(q-1+z^q\). The odd and even length contributions, respectively, are
\[
\frac{z(1-z^q)}{(1-z)^2}\frac{t}{1-t^2z^q(q-1+z^q)},
\qquad
\frac{z(1-z^q)}{(1-z)^2}\frac{t^2z^q}{1-t^2z^q(q-1+z^q)}.
\]
Adding proves the claimed bivariate identity. Setting \(t=1\) and canceling \((1-z^q)(1+z^q)=1-z^{2q}\) proves the total-count identity.

**5. Exponential growth.** Define \(b_0=1\), \(b_1=q-1\), and \(b_j=(q-1)b_{j-1}+b_{j-2}\) for \(j\ge2\), equivalently \(\sum_{j\ge0}b_jx^j=(1-(q-1)x-x^2)^{-1}\). For each integer \(m\ge1\), all first letters have the same threshold at full-period prefix length \(n=qm\), hence the proved coefficient count specializes to
\[
P_q(qm)=q\left(b_{m-1}+2\sum_{j=0}^{m-2}b_j\right)
\]
(with empty sum zero). The positive recurrence has characteristic roots \(\lambda_q>1\) and \(-1/\lambda_q\), hence \(b_m=\Theta_q(\lambda_q^m)\), and so \(P_q(qm)=\Theta_q(\lambda_q^m)\). Monotonicity \(P_q(n)\le P_q(n+1)\) sandwiches arbitrary lengths between their adjacent multiples of \(q\), proving the stated limit.

## Verification
A standalone dependency-free Python verifier (`verify.py`) directly enumerates all **distinct** subsequences of \(W_{q,n}\), filters palindromes, and compares every palindrome-length cell with the exact coefficient formula. It passed \(56\) host prefixes and \(430\) length cells for \(q\in\{2,3,4,5\}\), with maximal tested host lengths \(17,15,13,11\), respectively. An independent earliest-embedding scan tested \(1{,}915\) palindromes against the derived greedy formula. The \(q=2\) checks test the algebra but are **not part of the originality scope**. For \(q=3\), the total counts at \(n=3,6,9\) are \(3,12,33\); for \(q=4\), at \(n=4,8,12\) they are \(4,20,72\). The infinite statement rests on the proof rather than on finite tests.

## Relationship to prior work
Mahalingam and Pandoh study counts of distinct scattered palindromic subsequences and alphabet-dependent extremal upper bounds, including length-specific bounds. Their August 2021 preprint and Pandoh's June 2021 lecture provide the motivating setting but do not state the present all-length \(q\ge3\) exact spectrum of repeated permutation prefixes. The lecture explicitly treats a binary extremal alternating family; that binary result is not claimed here. Holub and Saari (2009) study primarily binary palindromic-subsequence structure and minimal-palindromic extensions, while Müllner and Ryzhikov (2019) study length bounds and circular hosts, rather than this distinct-string spectrum. The present formula is for one canonical family, not a formula for an unrestricted \(q\)-ary maximum or any universal host language.

## Limitations
The result does not count positional embeddings, arbitrary periodic blocks with repeated letters, arbitrary hosts, or circular rotations. It does not resolve the unrestricted maximum-count problem. Searches and inspected sources cannot rule out an unindexed prior equivalent. No independent scientific audit has been performed.

## References
- P. Pandoh, *Counting scattered palindromes in finite words*, seminar slides, 21 June 2021. https://www.i2m.univ-amu.fr/wiki/Combinatorics-on-Words-seminar/_media/seminar2021%3A20210621pandoh.pdf
- K. Mahalingam and P. Pandoh, *Counting scattered palindromes in a finite word*, arXiv:2108.02729v1, 5 August 2021. https://arxiv.org/abs/2108.02729
- Š. Holub and K. Saari, *On highly palindromic words*, Discrete Applied Mathematics 157 (2009), 953–959. https://www.karlin.mff.cuni.cz/~holub/soubory/subpal.pdf
- C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502v1, 22 January 2019. https://arxiv.org/abs/1901.07502
