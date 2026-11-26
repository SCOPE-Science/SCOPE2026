# Exact universality-index law for homopolymer-free ternary words

## Finding
Fix an alphabet \(\Sigma=\{0,1,2\}\). A nonempty word is *homopolymer-free* if adjacent letters differ. Its *subsequence-universality index* \(\iota(w)\) is the largest integer \(k\ge0\) such that **every** word in \(\Sigma^k\) is a scattered subsequence of \(w\). The ambient alphabet is fixed to all three symbols, even when \(w\) uses fewer symbols.

Let \(N_{n,k}\) count homopolymer-free ternary words of length \(n\) with index exactly \(k\), with \(N_{0,0}=1\). Then the exact bivariate generating function is
\[
 F(z,u)=\sum_{n,k\ge0}N_{n,k}z^nu^k
 =1+\frac{3z+3z^2+6uz^3}{1-z-4uz^3}.
\]
For every integer \(n\ge1\) and \(k\ge1\), the number \(U_{n,k}\) with index **at least** \(k\) is zero when \(n<3k\), and otherwise
\[
 U_{n,k}=3\,2^{2k-1}\sum_{j=k}^{n-2k}\binom{n-2k}{j}.
\]
Thus \(N_{n,k}=U_{n,k}-U_{n,k+1}\) for \(k\ge1\), while \(N_{n,0}=3\,2^{n-1}-U_{n,1}\).

For a uniformly random length-\(n\) homopolymer-free ternary word, let \(I_n=\iota(W_n)\). Its consecutive complete greedy-arch lengths are independent and distributed as \(2+G\), where \(\Pr(G=g)=2^{-g}\) for integers \(g\ge1\). Consequently,
\[
 \frac{I_n}{n}\longrightarrow\frac14\quad\text{in probability},\qquad
 \frac{I_n-n/4}{\sqrt{n/32}}\ \xrightarrow{\ d\ }\ \mathcal N(0,1).
\]
Its mean and variance satisfy
\[
 \mathbb E I_n=\frac n4-\frac5{16}+O(2^{-n/2}),\qquad
 \operatorname{Var}(I_n)=\frac n{32}+\frac{13}{256}+O(n2^{-n/2}).
\]

## Assumptions and scope
All words are finite, linear, and over the fixed three-letter alphabet. A scattered subsequence retains relative order, not contiguity. Adjacent equal letters are forbidden but the first and last letters need not differ. The random model assigns equal probability to all \(3\cdot2^{n-1}\) admissible words of length \(n\). Coefficient identities hold formally in \(z,u\); asymptotics are for positive integers \(n\to\infty\).

## Proof
**1. Greedy arches measure subsequence universality.** Scan left to right, ending an arch upon its first acquisition of all three symbols, then reset the seen-symbol set. If there are \(r\) complete arches, every length-\(r\) ternary sequence embeds by choosing its successive letters in successive arches. Conversely, in each complete arch choose the *last first-appearing* symbol \(c_i\), and choose \(a\) missing from the final incomplete suffix (arbitrary if empty). The sequence \(c_1\cdots c_ra\) cannot embed: the earliest greedy occurrence of each \(c_i\), after the previous chosen position, is exactly the end of arch \(i\), and no \(a\) follows the last arch. If \(r=0\), \(a\) alone is absent. Therefore \(\iota(w)=r\).

**2. Arch waiting times.** In the uniform adjacent-distinct random process, the first two symbols of an arch are necessarily different. Thereafter the next letter is one of the two symbols different from its predecessor: exactly one is the as-yet-unseen third symbol, and each is equiprobable. Hence the number of further draws until that symbol appears is geometric with success probability \(1/2\), independently after each reset by the Markov property. Thus the lengths are independent copies of \(2+G\), with probability generating function
\[
 A(z)=\sum_{\ell\ge3}\Pr(T=\ell)z^\ell
      =\frac{z^3}{2-z},\qquad
 \mathbb E T=4,\quad\operatorname{Var}(T)=2.
\]
For \(k\ge1\), the condition \(I_n\ge k\) is that the sum of the first \(k\) arch lengths is at most \(n\). Writing \(G_i=1+H_i\) with \(\Pr(H_i=h)=2^{-h-1}\) for \(h\ge0\), the sum of the \(H_i\) has the negative-binomial distribution
\[
 \Pr\bigl(\sum_{i=1}^kH_i=h\bigr)
 =\binom{h+k-1}{k-1}2^{-h-k}.
\]
Its CDF is equivalently the binomial tail
\[
 \Pr(I_n\ge k)=2^{-(n-2k)}\sum_{j=k}^{n-2k}\binom{n-2k}{j}
\]
for \(n\ge3k\), and zero otherwise. Multiplication by the total \(3\cdot2^{n-1}\) admissible words proves the formula for \(U_{n,k}\).

**3. Rational bivariate enumerator.** Keep only the number \(s\in\{1,2\}\) of distinct symbols in the unfinished current arch; completing an arch increments the index and resets the state to \(s=0\). Let \(B_s\) be the generating series of suffixes whose current arch is in state \(s\), with the empty initial word handled separately. From any state \(s=1\) a new adjacent-distinct symbol always makes \(s=2\); from state \(s=2\) the two allowed next letters either keep \(s=2\) or complete the arch. Directly enumerating initial letters and these transitions gives
\[
 (1-z-4uz^3)(F(z,u)-1)=3z+3z^2+6uz^3,
\]
which gives the displayed rational function. For clarity, another derivation is by renewal: for \(n\ge1\), the exact probability generating series is
\[
 \sum_{n\ge1}\mathbb E[u^{I_n}]x^n
 =\frac{x(2+x+ux^2)}{2-x-ux^3}.
\]
This follows from successive arch durations \(A(x)=x^3/(2-x)\), and the unfinished-tail series \(R(x)=(1-A(x))/(1-x)=(2+x+x^2)/(2-x)\), via \(\sum_{n\ge0}\mathbb E[u^{I_n}]x^n=R(x)/(1-uA(x))\). Replacing \(x\) by \(2z\) and weighting the first nonempty word by \(3/2\) yields \(F\).

**4. Fluctuations and moments.** The index is the renewal count for the independent positive durations \(T_i\). The ordinary renewal law of large numbers gives the limiting proportion \(1/4\). For \(k_n=\lfloor n/4+t\sqrt{n/32}\rfloor+1\),
\[
 \Pr(I_n<k_n)=\Pr(T_1+\cdots+T_{k_n}>n).
\]
The central limit theorem for the independent durations, with mean \(4\) and variance \(2\), makes the right side converge to \(\Phi(t)\), proving the claimed normal limit.

Differentiating the displayed probability generating series at \(u=1\) gives exact generating series for the first and second factorial moments:
\[
 E(x)=\frac{x^3}{(1-x)^2(x^2+x+2)},\qquad
 M_2(x)=\frac{2x^6}{(1-x)^3(x^2+x+2)^2}.
\]
Partial fractions at the pole \(x=1\) give \(\mathbb E I_n=n/4-5/16+O(2^{-n/2})\) and \(\mathbb E[I_n(I_n-1)]=(n^2/16)-(3n/8)+(59/128)+O(n2^{-n/2})\). Combining \(\operatorname{Var}(I_n)=\mathbb E[I_n(I_n-1)]+\mathbb E I_n-(\mathbb E I_n)^2\) gives \(n/32+13/256+O(n2^{-n/2})\). The other poles are roots of \(x^2+x+2\), both of modulus \(\sqrt2\), which establishes the exponential remainders.

## Verification
Run \(\texttt{python3 verify.py}\) using Python's standard library. The program counts distributions by an independent last-symbol/seen-mask dynamic program for all \(1\le n\le80\), and separately enumerates every admissible word up to length \(11\) and tests every candidate scattered subsequence directly. The checks agree with the binomial-tail formula throughout. This finite check is corroboration; the proof above applies to every length.

## Relationship to prior work
Barker and coauthors (2020) introduce and analyze scattered-factor universality and arch factorization; Kosche and coauthors (2021) study absent subsequences and universality. Adamson and coauthors (2023) present general algorithms counting universal words in regular languages, so counting this constrained regular language at any fixed length is algorithmically accessible. The claim here is the explicit ternary adjacent-distinct **all-length** distribution, rational enumerator, independent waiting-time law and asymptotic fluctuation constants; it does not claim to invent universality, greedy arches, or regular-language counting algorithms. Results for unrestricted binary words concern a different alphabet and language.

## Limitations
The formulas concern the three-letter, adjacent-distinct **linear** language and the fixed-alphabet subsequence definition; they do not automatically extend to circular words, arbitrary transition constraints or alphabets of other sizes. A semantically equivalent enumerative formula might occur in literature not indexed or inspected. The normal limit is asymptotic and is not a finite-sample error bound. Independent mathematical audit has not been performed.

## References
1. Barker et al., *Scattered Factor-Universality of Words*, arXiv:2003.04629v1 (2020), https://arxiv.org/abs/2003.04629.
2. Kosche et al., *Absent Subsequences in Words*, arXiv:2108.13968v1 (2021), https://arxiv.org/abs/2108.13968.
3. Adamson et al., *k-Universality of Regular Languages*, arXiv:2311.10658v1 (2023), https://arxiv.org/abs/2311.10658.
