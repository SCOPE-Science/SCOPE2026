# Expected distinct palindrome-pair factors in uniform random words grow as square root times logarithm

## Finding

Fix an integer \(q\ge2\). Let \(W_N\) be uniformly sampled from the \(q^N\) words of length \(N\), and let \(Z_{N,q}\) be the number of **distinct nonempty contiguous factors** of \(W_N\) expressible as \(uv\), where \(u\) and \(v\) are palindromes and either may be empty. Then

\[
\mathbb{E}Z_{N,q}=\Theta_q\bigl(\sqrt{N}\log_q N\bigr)\qquad(N\longrightarrow\infty).
\]

The constants implicit in \(\Theta_q\) may depend on the fixed alphabet size \(q\). In contrast, the classical expectation for distinct factors that are themselves palindromes is \(\Theta_q(\sqrt N)\) [2].

## Assumptions and scope

The alphabet \(\Sigma\) has exactly \(q\) symbols. The letters of \(W_N\) are independent and uniformly distributed. A factor is a contiguous substring; factors with the same literal sequence are counted only once, irrespective of occurrence locations. The empty factor is not counted, but the empty palindrome is allowed as one component. Define \(\mathcal P_{q,m}\subseteq\Sigma^m\) to be the words that are products of at most two palindromes (equivalently, two with empty components permitted), for \(m\ge1\).

## Proof

**1. An upper bound for the palindrome-pair language.** For a fixed split position \(s\in\{0,1,\dots,m\}\), choose a palindromic prefix of length \(s\) and a palindromic suffix of length \(m-s\). Their independent free-letter counts are \(\lceil s/2\rceil\) and \(\lceil(m-s)/2\rceil\). Thus the corresponding set has precisely

\[
q^{\lceil s/2\rceil+\lceil(m-s)/2\rceil}\le q^{\lceil m/2\rceil+1}
\]

members, and taking a union over splits yields

\[
|\mathcal P_{q,m}|\le(m+1)q^{\lceil m/2\rceil+1}.
\tag{1}
\]

**2. A matching lower bound along odd lengths.** Suppose \(m\) is odd. Consider the \(m\) distinct split positions \(s\in\{0,\dots,m-1\}\), omitting the redundant split at \(m\). At each position the number of words having two palindromic pieces is exactly \(q^{(m+1)/2}\). Index the letters cyclically by \(\mathbb Z/m\mathbb Z\). Such a splitting forces invariance under the reflection \(\rho_s(i)=s-1-i\pmod m\): this reverses the first piece within itself and the second piece within itself. If the same word admits two distinct splits \(s,t\), then composing \(\rho_s\) and \(\rho_t\) gives a nonidentity cyclic rotation fixing the word. Therefore a *primitive word*, meaning one that is not an integer power of a shorter word, can appear in at most one of these \(m\) split classes.

A nonprimitive word of odd length \(m\) has a period \(d\) which is a proper divisor of \(m\). Since its repetition exponent is an odd integer at least \(3\), we have \(d\le m/3\). Summing over possible divisors gives at most \(m q^{m/3}\) nonprimitive words of length \(m\). Every split class therefore contains at least \(q^{(m+1)/2}-mq^{m/3}\) primitive words. These are disjoint across the \(m\) split positions; hence

\[
|\mathcal P_{q,m}|\ge m\bigl(q^{(m+1)/2}-mq^{m/3}\bigr)
\ge \tfrac12 m q^{(m+1)/2}
\tag{2}
\]

for all sufficiently large odd \(m\) (depending only on \(q\)). This supplies a self-contained growth bound; the exact census and factorization theory of the language were studied earlier by Kemp [1] and Guo--Shallit--Shur [3].

**3. Uniform occurrence probability, including overlapping matches.** Fix any \(w\in\Sigma^m\) and \(N\ge m\). Write \(M=N-m+1\) and \(\mu=Mq^{-m}\). Let \(X\) count occurrences of \(w\) beginning at the \(M\) eligible positions. Then \(\mathbb E X=\mu\). For starts at distance \(d\ge m\), the match events are independent. At distance \(1\le d<m\), simultaneous matches are either impossible or force \(m+d\) specified letters, so their joint probability is at most \(q^{-(m+d)}\). Thus, including both orders of each pair,

\[
\mathbb E X^2\le \mu^2+\mu\left(1+2\sum_{d=1}^{m-1}q^{-d}\right)
\le \mu^2+\mu\left(1+\frac{2}{q-1}\right).
\]

Cauchy--Schwarz applied to \(X\mathbf1_{X>0}\) then implies the bound, uniform in the pattern \(w\),

\[
\frac{\mu}{\mu+1+2/(q-1)}
\le\mathbb P(w\text{ occurs in }W_N)
\le\min\{1,Nq^{-m}\}.
\tag{3}
\]

The right-hand inequality is a direct union bound.

**4. Upper bound for the expected number of distinct factors.** By linearity of expectation,

\[
\mathbb EZ_{N,q}=\sum_{m=1}^N\sum_{w\in\mathcal P_{q,m}}\mathbb P(w\text{ occurs}).
\]

Put \(h=\lfloor\log_q N\rfloor\). Equations (1) and (3) give

\[
\mathbb EZ_{N,q}\le
\sum_{m=1}^{h}(m+1)q^{\lceil m/2\rceil+1}
+N\sum_{m=h+1}^N(m+1)q^{\lceil m/2\rceil+1-m}.
\]

Both geometric sums, with their linear prefactors, are bounded by \(O_q((h+1)q^{h/2})\) and \(O_q(N(h+1)q^{-h/2})\), respectively. Since \(q^h\le N<q^{h+1}\), the total is \(O_q(\sqrt N\log_q N)\).

**5. Matching lower bound.** Let \(m\) be the largest odd integer not exceeding \(h\). For all sufficiently large \(N\), we have \(h-1\le m\le h\), \(N-m+1\ge N/2\), and \(q^m\le N\). Hence \(\mu=(N-m+1)q^{-m}\ge1/2\). The lower bound of (3) is then uniformly bounded away from zero, independently of the selected word \(w\). Applying (2) to every distinct word in \(\mathcal P_{q,m}\), we obtain

\[
\mathbb EZ_{N,q}\ge c_q |\mathcal P_{q,m}|
\ge c'_q m q^{m/2}
=\Omega_q(\sqrt N\log_q N),
\]

because \(m\ge h-1\) and \(q^m\ge q^{h-1}>N/q^2\). This completes the proof for all fixed \(q\ge2\).

## Verification

The complete standalone Python program `verify.py` exhaustively enumerates palindrome-pair words over \(q=2\) at odd lengths \(3,5,7,9,11\), and \(q=3\) at odd lengths \(3,5,7,9\). It checks that every primitive palindrome pair has exactly one split among the \(m\) canonical positions and that each split class has the asserted size. For \(q\in\{2,3\}\), all patterns of lengths \(1\le m\le4\), and sample lengths \(m\le N\le m+3\), the program also checks both inequalities in (3) by enumerating all possible random words and computing exact rational probabilities. The program passed. These finite checks do not establish asymptotics; the proof above does.

Run with `python3 verify.py` from the same directory. No third-party packages are required.

## Relationship to prior work

Kemp [1] and Guo--Shallit--Shur [3] give the enumeration and factorization structure of palindrome-pair words; no novelty is claimed for their word-language census or the primitive split-uniqueness principle. Rubinchik--Shur [2] establish the \(\Theta_q(\sqrt N)\) expectation for **single** palindromic factors in random words and discuss ordinary square factors, not the two-palindrome factor statistic. Borchert--Rampersad [4] study extremal deterministic words and infinite-word conditions for palindrome-pair factor richness. OEIS A007055 [5] records binary palindrome-pair word counts, not their distinct occurrence counts inside uniformly random words. The result here concerns the expected number of distinct **two-palindrome factors**, and obtains its additional logarithmic order by joining the language's splitting multiplicity with a pattern-uniform occurrence estimate that handles overlaps.

## Limitations

The result establishes order of growth only, not a sharp constant or second-order fluctuations. It assumes independent, uniformly distributed letters and alphabet size fixed as \(N\to\infty\); no extension to a nonuniform source or alphabet size growing with \(N\) follows from the proof as written. Although three closely related open-access texts and a relevant sequence-database entry were inspected, Kemp's 1982 full paper was unavailable for direct inspection, leaving a historical-priority risk. 

## References

[1] R. Kemp, "On the number of words in the language \(\{w\in\Sigma^*:w=w^R\}^2\)," *Discrete Mathematics* 40 (1982), 225--234. https://doi.org/10.1016/0012-365X(82)90123-6 (bibliographic information and contributions corroborated by [3], full original not inspected).

[2] M. Rubinchik and A. M. Shur, "The Number of Distinct Subpalindromes in Random Words," arXiv:1505.08043v1, May 29, 2015. https://arxiv.org/abs/1505.08043.

[3] C. Guo, J. Shallit and A. M. Shur, "On the Combinatorics of Palindromes and Antipalindromes," arXiv:1503.09112v1, March 31, 2015, Section 3. https://arxiv.org/abs/1503.09112.

[4] A. Borchert and N. Rampersad, "Words with many Palindrome Pair Factors," arXiv:1509.05396v1, September 17, 2015. https://arxiv.org/abs/1509.05396.

[5] OEIS A007055, "Number of words of length \(n\) in the language of products of two binary palindromes." https://oeis.org/A007055.
