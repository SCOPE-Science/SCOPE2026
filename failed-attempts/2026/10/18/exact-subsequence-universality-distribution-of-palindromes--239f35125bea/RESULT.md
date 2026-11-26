# Exact subsequence-universality distribution of palindromes

## Finding

Fix a labeled alphabet \(\Sigma\) of size \(q\ge2\). For a word \(w\), let \(I(w)\) be the largest integer \(k\ge0\) for which every word in \(\Sigma^k\) is an order-preserving (not necessarily contiguous) subsequence of \(w\). Define the number of palindromes of length \(n\) and index \(k\) by
\[
P_q(n,k)=\#\{w\in\Sigma^n:w=w^R,\ I(w)=k\}.
\]
Set \(t=z^2\), and define rational functions
\[
A_q(t)=\frac{q!t^q}{\prod_{j=1}^{q-1}(1-jt)},\qquad
R_{q,j}(t)=\frac{(q)_jt^j}{\prod_{h=1}^{j}(1-ht)}\quad(0\le j<q),\qquad
R_q(t)=\sum_{j=0}^{q-1}R_{q,j}(t),
\]
where \((q)_j=q!/(q-j)!\), and the empty product is one. The complete bivariate generating function is
\[
\boxed{\displaystyle
\sum_{n,k\ge0}P_q(n,k)z^nu^k
=\frac{R_q(z^2)+z\big(qR_q(z^2)+(u-1)R_{q,q-1}(z^2)\big)}{1-u^2A_q(z^2)}.}
\]
In particular, the exact shortest length \(L_q(k)\) of a palindromic word containing all \(k\)-letter subsequences, and the number \(M_q(k)\) of palindromes attaining that length, are, for \(k\ge1\),
\[
\boxed{L_q(k)=\begin{cases}qk&k\text{ even},\\q(k+1)-1&k\text{ odd},\end{cases}\qquad
M_q(k)=\begin{cases}(q!)^{k/2}&k\text{ even},\\(q!)^{(k+1)/2}&k\text{ odd}.\end{cases}}
\]
(The empty palindrome has index zero.) Finally, choose \(W_n\) uniformly among the \(q^{\lceil n/2\rceil}\) palindromes of length \(n\). Write \(H_q=\sum_{j=1}^q1/j\), \(H_q^{(2)}=\sum_{j=1}^q1/j^2\), \(\mu_q=qH_q\), and \(v_q=q^2H_q^{(2)}-qH_q\). Then
\[
\mathbb E I(W_n)=\frac{n}{\mu_q}+O_q(1),\qquad
\operatorname{Var} I(W_n)=\frac{2v_q}{\mu_q^3}n+o_q(n),
\]
\[
\boxed{\frac{I(W_n)-n/\mu_q}{\sqrt{(2v_q/\mu_q^3)n}}\ \xrightarrow{\ \mathrm d\ }\ \mathcal N(0,1).}
\]
For \(q=2\), the variance coefficient equals \(4/27\), twice that of an unconstrained uniform binary word.

## Assumptions and scope

All counts concern *labeled, linear* palindromes, including the empty word, without quotienting by rotation or relabeling. Subsequence universality is relative to the fixed full alphabet \(\Sigma\), even when a particular word omits a letter. The generating-function identities are formal power-series identities for arbitrary fixed integer \(q\ge2\). The probability statement lets \(n\) tend to infinity for fixed \(q\).

## Proof

**1. Unique greedy arches.** Scan a word left to right and close a segment as soon as all \(q\) letters have appeared. Repeat, leaving a final segment with fewer than \(q\) different letters. If \(h\) arches close, then the word has index exactly \(h\): each arch can supply one arbitrary subsequence symbol, whereas a word of length \(h+1\) formed from the terminal newly encountered arch letters followed by a letter missing in the remainder is absent. This characterization also holds when there are no complete arches.

The generating function for one arch follows by fixing the order in which its \(q\) distinct letters first appear (\(q!\) possibilities). Before the second new letter there are arbitrary repeats of the first, before the third there are repeats of the first two, and so on; the final position is the first occurrence of the last letter. Therefore one arch contributes \(A_q(t)\). For a remainder using exactly \(j<q\) letters, choose its first-appearance order (\((q)_j\) choices), then allow arbitrary repetitions of previously encountered symbols. Its series is \(R_{q,j}(t)\). Equivalently this counts words using exactly \(j\) letters by a Stirling-number expansion. Unique arch factorization gives the joint half-word series
\[
\sum_{x\in\Sigma^*}t^{|x|}v^{I(x)}s^{|\operatorname{alph}(r(x))|}
=\frac{\sum_{j=0}^{q-1}s^jR_{q,j}(t)}{1-vA_q(t)}.
\]

**2. Palindromic symmetry.** Write an even palindrome as \(w=xx^R\), and an odd one as \(w=xax^R\), where \(a\in\Sigma\). The exact palindrome-index lemma is Proposition 15 of Barker, Fleischmann, Harwardt, Manea and Nowotka (2020): if \(h=I(x)\), then
\[
I(xx^R)=2h,\qquad
I(xax^R)=2h+\mathbf 1_{\{\operatorname{alph}(r(x))\cup\{a\}=\Sigma\}}.
\]
Its proof compares the greedy arches from the two ends; no additional arch can be completed in the reflected central remainder unless that remainder together with the center includes every alphabet symbol. In particular, since the remainder has at most \(q-1\) symbols, the odd indicator is one exactly when it contains \(q-1\) symbols and the center is the unique missing symbol. For \(h=0\), the same identities follow directly: the even palindrome omits a letter of \(\Sigma\), and the odd palindrome is universal exactly when the center supplies the only letter missing from the half. This lemma is **prior work**, not a new theorem here.

At half length \(m\), every half-word with \(h\) arches contributes \(u^{2h}\) to its even palindrome. For an odd palindrome its \(q\) choices of center contribute \(q u^{2h}\) except that for a remainder containing \(q-1\) symbols, one center instead contributes \(u^{2h+1}\). Multiplying by the independent complete-arch and remainder series and substituting \(t=z^2\) proves the stated rational function without any parity or empty-half exceptions.

**3. Sharp minimum lengths.** Each complete arch has length at least \(q\). For an even palindrome with \(I=2h\), its length is at least \(2qh\); equality forces exactly \(h\) permutation arches in the half-word, giving \((q!)^h\) possibilities. For odd target \(2h+1\), even palindromes need at least \(2q(h+1)\) positions, while an odd palindrome has \(2h+1\) universality with half-length at least \(qh+q-1\) and its center the missing remainder letter. Equality forces \(h\) permutation arches and a permutation of \(q-1\) distinct remaining letters, with the uniquely forced missing center, giving \((q!)^{h+1}\) possibilities. If a word has a larger index than the target, the arch lower bound makes it strictly longer. These constructions and lower bounds prove both formulas.

**4. Uniform random palindromes.** The left half of a uniformly random palindrome is an independent uniform \(q\)-ary word. The waiting time \(T\) for one complete arch is a sum of independent geometric waiting times with success probabilities \(1,(q-1)/q,\ldots,1/q\), whence \(\mathbb ET=\mu_q\) and \(\operatorname{Var}T=v_q>0\). Successive arch lengths are independent copies of \(T\). If \(N(m)\) is the number of completed arches in the first \(m\) uniform letters, standard renewal laws give
\[
\mathbb EN(m)=m/\mu_q+O_q(1),\quad
\operatorname{Var}N(m)=(v_q/\mu_q^3)m+o_q(m),\quad
\frac{N(m)-m/\mu_q}{\sqrt{(v_q/\mu_q^3)m}}\Rightarrow\mathcal N(0,1).
\]
For even \(n=2m\), the palindrome index equals \(2N(m)\). For odd \(n=2m+1\), it is \(2N(m)+B\) with \(0\le B\le1\); its bounded perturbation leaves the normal limit and leading variance unchanged (the covariance is at most of order \(\sqrt n\)). Replacing \(m\) by \(n/2+O(1)\) proves the limits.

## Verification

The accompanying standalone `verify.py` independently determines each small palindrome's universality index by testing **every** candidate subsequence, not by using the greedy index rule. For alphabet sizes \(q=2,3,4,5\), it exhaustively checks all palindromes through lengths \(15,11,9,7\), respectively, against coefficients expanded from the displayed rational functions. It also verifies the sharp minimum-length multiplicities for small \(q\) and \(k\). The checker uses Python's standard library and runs as `python verify.py` in the directory containing this document. Finite computations serve as a consistency check, not as a proof of the formulas or limit theorem.

## Relationship to prior work

Barker et al., *Scattered Factor-Universality of Words* (2020), Proposition 15, explicitly proves the palindrome-index reduction used in Step 2. The new contribution is the all-alphabet **bivariate enumeration**, its exact minimum-length multiplicities and the random-palindrome limit law, not the reduction itself. Schnoebelen and Veron (2023) analyze arch factorizations algorithmically; Adamson et al. (2023) count universality properties of regular languages. General finite-word or regular-language counts do not, by themselves, determine the length-index distribution for the nonregular class of palindromes. These literature comparisons do not exclude an equivalent formula in an unlocated source.

## Limitations

The findings give no refined count by individual symbol frequencies and no uniform asymptotics when \(q\) grows with \(n\). The normal approximation is asymptotic for fixed \(q\), not a finite-size error bound. The underlying palindrome-index characterization was known in 2020; priority of the new enumeration remains subject to discovery of equivalent literature.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea and D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629, first posted 2020-03-10. Especially Proposition 15 (palindromic index).
2. P. Fleischmann, S. B. Germann and D. Nowotka, *Scattered Factor Universality — The Power of the Remainder*, arXiv:2104.09063, first posted 2021-04-19.
3. P. Schnoebelen and J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932, first posted 2023-04-24.
4. D. Adamson and coauthors, *k-Universality of Regular Languages*, arXiv:2311.10658, first posted 2023-11-17.
