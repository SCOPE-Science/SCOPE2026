# Exact subsequence-universality distribution of binary run-limited languages

## Finding
Fix an integer \(r\ge1\). Let \(\mathcal L_r\) be the language of all finite binary words with no contiguous occurrence of \(1^{r+1}\). The empty word is included. For a word \(w\), let \(\iota(w)\) be the largest integer \(k\ge0\) such that **every** binary word of length \(k\) appears in \(w\) as a (not necessarily contiguous) subsequence; the ambient alphabet is always \(\{0,1\}\), even for a unary or empty source. Let
\[
a_r(n,k)=\#\{w\in\mathcal L_r: |w|=n,\ \iota(w)=k\}.
\]
The full two-parameter enumerator is the rational function
\[
\boxed{\sum_{n,k\ge0}a_r(n,k)z^nu^k=
\frac{1+z-z^{r+1}-uz^{r+2}}{1-z-2uz^2+uz^{r+2}+u^2z^{r+3}}.}
\]
The identity holds as a formal power series in \(z\), with polynomial coefficients in \(u\), for **every** integer \(r\ge1\). In particular, for all integer \(n,k\), adopting \(a_r(n,k)=0\) for \(n<0\) or \(k<0\),
\[
\begin{aligned}
a_r(n,k)={}&a_r(n-1,k)+2a_r(n-2,k-1)\\
&-a_r(n-r-2,k-1)-a_r(n-r-3,k-2)\\
&+\mathbf1_{(n,k)=(0,0)}+\mathbf1_{(n,k)=(1,0)}\\
&-\mathbf1_{(n,k)=(r+1,0)}-\mathbf1_{(n,k)=(r+2,1)}.
\end{aligned}
\]
All coefficients are therefore exactly computable with integer arithmetic. The zero-universality layer is \(a_r(0,0)=1\) and, for \(n\ge1\), \(a_r(n,0)=1+\mathbf1_{n\le r}\).

Every \(k\)-universal binary word has length at least \(2k\), and this bound is attained in every \(\mathcal L_r\). The exact number at that shortest length has a sharp transition:
\[
\boxed{a_r(2k,k)=\begin{cases}k+1,&r=1,\\2^k,&r\ge2,\end{cases}\qquad k\ge1.}
\]
For \(r=1\), the \(k+1\) shortest witnesses are precisely
\[
(10)^j(01)^{k-j},\qquad 0\le j\le k.
\]

There is also a quantitative asymptotic consequence. If \(W_{r,n}\) is uniform among \(\mathcal L_r\cap\{0,1\}^n\), let \(\rho_r\in(0,1)\) be the unique positive solution of
\[
\rho_r+\rho_r^2+\cdots+\rho_r^{r+1}=1.
\]
For each fixed \(r\),
\[
\mathbb E[\iota(W_{r,n})]=\mu_r n+O_r(1),
\]
with the explicit rate
\[
\boxed{\mu_r=
\frac{-2\rho_r^2+\rho_r^{r+2}+2\rho_r^{r+3}}
{\rho_r\bigl(-1-4\rho_r+(r+2)\rho_r^{r+1}+(r+3)\rho_r^{r+2}\bigr)}.}
\]
For orientation, \(\mu_1=0.2763932022\ldots\), \(\mu_2=0.3589040973\ldots\), and \(\mu_r\to1/3\) as \(r\to\infty\). Thus bounding one-runs at length two yields a higher typical subsequence-universality rate than does forbidding adjacent ones, even though the latter gives fewer possible source words.

## Assumptions and scope
All words are finite and all enumerations are of distinct words, not automaton paths with multiplicities. The alphabet is the fixed binary set, independent of which letters occur in an individual word. A subsequence preserves relative order but may delete arbitrarily many positions. The forbidden pattern \(1^{r+1}\) is contiguous, and \(r\) is held fixed when taking \(n\to\infty\) in the expectation statement. For the generating-function identity, \(z\) counts length and \(u\) counts the universality index, not the number of ones.

## Proof
**Arch lemma.** Scan a binary word left to right, repeatedly cutting immediately after the first occurrence of both alphabet symbols since the preceding cut. The number of such completed *arches* is \(\iota(w)\). To see the lower bound, every target length-\(k\) binary word embeds by choosing its successive symbols from \(k\) successive arches. To see the upper bound, every completed arch is the shortest prefix of the remaining word containing both symbols, and the leftover rest is unary or empty. A length-one target equal to the symbol absent from the rest cannot be completed beyond the last arch; recursively choosing absent symbols at each arch boundary yields a length-\(k+1\) target missing from the word when only \(k\) arches were completed. This is the standard greedy arch-factorization characterization; see the references.

**Exact finite-state decomposition.** Track the trailing run of ones, whose length \(j\) must satisfy \(0\le j\le r\). Also track whether, after the most recently completed arch, no new symbol has been seen (state \(E_j\)), only zero has been seen (state \(Z\)), or only one has been seen (state \(O_j\), \(1\le j\le r\)). A completed arch contributes the weight \(u\); every input letter contributes \(z\). Define \(E_j,Z,O_j\) to be the generating functions for all possible admissible completions from those respective states, including stopping immediately. A letter completing an arch resets the unfinished-symbol state but retains the correct trailing one-run. Directly reading the two possible next letters gives
\[
\begin{aligned}
E_j &=1+zZ+\mathbf1_{j<r}\,zO_{j+1} &&(0\le j\le r),\\
Z &=1+zZ+zuE_1,\\
O_j &=1+zuE_0+\mathbf1_{j<r}\,zO_{j+1} &&(1\le j\le r).
\end{aligned}
\]
All these equations are identities in formal power series, uniquely determined recursively by degree in \(z\). A forbidden transition (appending another one after \(r\) ones) is absent, not a terminating word.

Write \(S_t(z)=1+z+\cdots+z^t\) for \(t\ge0\). Backward substitution yields \(O_j=S_{r-j}(z)(1+zuE_0)\), and hence
\[
E_0-E_1=z^r(1+zuE_0),\qquad
E_1=(1-uz^{r+1})E_0-z^r,
\]
while \(Z=(1+zuE_1)/(1-z)\). Substituting these identities into \(E_0=1+zZ+zO_1\) and clearing the harmless factor \(1-z\) yields
\[
(1-z-2uz^2+uz^{r+2}+u^2z^{r+3})E_0
=1+z-z^{r+1}-uz^{r+2}.
\]
Since initially no arch is in progress and the trailing one-run is zero, \(E_0=\sum a_r(n,k)z^nu^k\), proving the boxed generating function and its coefficient recurrence. The constant term of the denominator is one, so its formal inverse exists. Index zero means a word is unary or empty, yielding the stated \(a_r(n,0)\).

**Shortest possible universality and its phase transition.** Each completed binary arch must contain both symbols, hence has length at least two. The witnesses \((01)^k\) have exactly \(k\) arches and avoid \(11\), so the lower bound \(2k\) is attained for every \(r\). Any length-\(2k\), index-\(k\) word consists of exactly \(k\) two-letter arches, each either \(01\) or \(10\). There are \(2^k\) such words and none contains \(111\), since their one-runs have length at most two. When \(r=1\), the only forbidden adjacent pair of arches is \(01\mid10\), which creates \(11\). Therefore all \(10\) arches must precede all \(01\) arches, and there are precisely \(k+1\) possibilities. For \(r\ge2\), no pair is forbidden. This proves the sharp threshold and witness classification.

**Mean universality rate.** Put \(Q_r(z,u)=1-z-2uz^2+uz^{r+2}+u^2z^{r+3}\) and \(N_r(z,u)=1+z-z^{r+1}-uz^{r+2}\). At \(u=1\),
\[
Q_r(z,1)=(1-z^2)\bigl(1-z-z^2-\cdots-z^{r+1}\bigr).
\]
The unique positive root \(\rho_r\in(0,1)\) of the latter second factor is a simple root and the unique smallest-modulus root: the exponents \(1\) and \(2\) make the usual triangle-inequality equality condition strict away from the positive axis. The numerator does not cancel it, since \(N_r(\rho_r,1)=(1+\rho_r)(1-\rho_r^{r+1})>0\). By isolation of this simple pole and analytic perturbation, the dominant root \(\rho_r(u)\) is analytic for \(u\) near one, and uniform coefficient extraction gives
\[
\frac{[z^n]F_r(z,u)}{[z^n]F_r(z,1)}
=C_r(u)\left(\frac{\rho_r(1)}{\rho_r(u)}\right)^n(1+O_r(\theta_r^n)),
\]
for some analytic \(C_r\) satisfying \(C_r(1)=1\) and some \(0<\theta_r<1\). Differentiating at \(u=1\) gives \(\mathbb E[\iota(W_{r,n})]=-n\rho_r'(1)/\rho_r+O_r(1)\). Implicit differentiation of \(Q_r(\rho_r(u),u)=0\) gives \(-\rho_r'(1)/\rho_r=Q_{r,u}(\rho_r,1)/(\rho_r Q_{r,z}(\rho_r,1))\), exactly the displayed rational expression in \(\rho_r\). For fixed \(z\) with \(|z|<1\), \(\sum_{j=1}^{r+1}z^j\to z/(1-z)\), so \(\rho_r\to1/2\) and the rate formula tends to \(1/3\). No uniform-in-\(r\) estimate is claimed.

## Verification
The included standalone `verify.py` uses only the Python standard library. It independently calculates the generating-function coefficients from the rational identity and counts the same statistic with a digit-by-digit, run-bounded arch-state dynamic program for every \(1\le r\le8\), \(0\le n\le44\). It also exhaustively lists all admissible binary words of length at most twelve for those eight bounds, independently implements the greedy arch index and the literal fixed-alphabet subsequence definition, verifies both definitions agree, checks the coefficient counts, checks total constrained-language counts via a separate first-run recurrence, and checks the shortest-length formulas through \(k=19\). Its observed result is:

`VERIFY_OK r=1..8 n=0..44 cells=4232 direct_words=49872 full_alphabet=true minimal_profiles=true`

The executable checks are finite diagnostics, not infinite proofs. The all-parameter rational identity, sharp boundary, and asymptotic rate follow from the arguments above.

## Relationship to prior work
The greedy-arch notion and subsequence-universality criterion are established in Kosche, Koß, Manea, and Siemer's *Absent Subsequences in Words* and related work. Adamson's 2023 ranking and unranking paper counts fixed-length universal words in the **unconstrained** full alphabet. Adamson and collaborators' 2023 *k-Universality of Regular Languages* gives general algorithms for counting universal words accepted by finite automata, so each fixed \(r\) is algorithmically tractable in principle. Those inspected results do **not** state this parameter-uniform bivariate rational formula, its zero/universality layers, the exact \(k+1\)-versus-\(2^k\) extremal transition, or the explicit asymptotic rate. A separate published analysis of the unrestricted full binary language yields \((1+z)/(1-z-2uz^2)\), which this formula approaches coefficientwise as \(r\to\infty\) but which cannot count the run-limited source words. Counting absent subsequences or near-universal Dyck excursions is a distinct invariant or domain and does not imply the run-limited enumerator.

## Limitations
The result is for a fixed binary alphabet and the single forbidden contiguous run \(1^{r+1}\); it is not an enumeration of general forbidden-factor codes. Its asymptotic expectation is proved only with \(r\) fixed. Generic regular-language enumeration algorithms may compute the same coefficients for any chosen fixed \(r\) without giving this closed form. The relevant full-text comparisons and searches did not locate a parameter-uniform equivalent; an overlooked formulation in constrained coding, weighted automata, or probabilistic pattern matching remains a bibliographic risk. The diagnostic program cannot establish novelty or replace proof.

## References
1. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658v1, first public 2023-11-17, https://arxiv.org/abs/2311.10658.
2. D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1, first public 2023-04-10, https://arxiv.org/abs/2304.04583.
3. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968v1, first public 2021-08-31, https://arxiv.org/abs/2108.13968.
