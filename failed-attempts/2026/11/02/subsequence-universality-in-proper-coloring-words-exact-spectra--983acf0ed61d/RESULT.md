# Subsequence universality in proper-coloring words: exact spectra and renewal laws

## Finding
Let \(q\ge2\), \(\Sigma=\{0,\ldots,q-1\}\), and \(\mathcal P_q(n)\) be the indexed words \(w=w_1\cdots w_n\) satisfying \(w_i\ne w_{i+1}\). The empty word is allowed at \(n=0\). The universality index \(\iota(w)\) is the largest \(k\ge0\) such that every \(k\)-letter word over \(\Sigma\) occurs as a scattered subsequence of \(w\). Let \(C_q(n,k)=|\{w\in\mathcal P_q(n):\iota(w)=k\}|\).

**Exact all-alphabet distribution.** Define the rational functions
\[
E_1(z)=1,\qquad E_j(z)=\prod_{i=1}^{j-1}\frac{(q-i)z}{1-(i-1)z}\quad(2\le j\le q),
\]
\[
A(z)=(q-1)zE_q(z),\qquad B(z)=1+(q-1)z\sum_{j=1}^{q-1}\frac{E_j(z)}{1-(j-1)z}.
\]
Then the following identity holds as a formal power series for every \(q\ge2\):
\[
\boxed{\sum_{n,k\ge0}C_q(n,k)z^nu^k
=1+\frac{q}{q-1}(B(z)-1)
+\frac{q}{q-1}\frac{uA(z)B(z)}{1-uA(z)}.}
\]

**Ternary closed form and exact binomial tails.** At \(q=3\), this reduces to
\[
\boxed{\sum_{n,k\ge0}C_3(n,k)z^nu^k
=\frac{1+2z+3z^2+2uz^3}{1-z-4uz^3}.}
\]
For a uniform member of \(\mathcal P_3(n)\), let \(I_n=\iota(w)\). For every \(n\ge1\) and \(k\ge1\),
\[
\boxed{\Pr(I_n\ge k)=
\begin{cases}
2^{-(n-2k)}\displaystyle\sum_{j=k}^{n-2k}\binom{n-2k}{j},&n\ge3k,\\
0,&n<3k.
\end{cases}}
\]
The exact-index probability follows by subtracting consecutive tails, and the corresponding number of labeled words is obtained by multiplying by \(3\cdot2^{n-1}\).

**Renewal limit theorem.** Put \(H_m=\sum_{r=1}^m1/r\) and \(H_m^{(2)}=\sum_{r=1}^m1/r^2\). For a uniform proper-coloring word on \(q\ge3\) letters define
\[
\mu_q=1+(q-1)H_{q-1},\qquad
v_q=(q-1)^2H_{q-1}^{(2)}-(q-1)H_{q-1}>0.
\]
As \(n\to\infty\) with fixed \(q\ge3\),
\[
\mathbb E I_n=\frac n{\mu_q}+O_q(1),\quad
\operatorname{Var}(I_n)=\frac{v_q}{\mu_q^3}n+O_q(1),\quad
\frac{I_n-n/\mu_q}{\sqrt{v_qn/\mu_q^3}}\Rightarrow\mathcal N(0,1).
\]
In particular at \(q=3\), the mean is \(n/4+O(1)\), the variance is \(n/32+O(1)\), and the Gaussian normalization is \(\sqrt{n/32}\).

**Shortest hosts.** The shortest proper-coloring words of index at least \(k\ge1\) have length \(qk\). For every \(q\ge2\), the exact number of such indexed labeled shortest hosts is
\[
\boxed{q!\bigl((q-1)(q-1)!\bigr)^{k-1}.}
\]
At \(q=2\), every nonempty proper-coloring word alternates, its index equals \(\lfloor n/2\rfloor\), and the Gaussian statement is intentionally excluded.

## Assumptions and scope
The alphabet labels and host positions are fixed; words are not quotiented by reversal, alphabet permutations, or cyclic rotation. A scattered subsequence uses increasing host positions. The no-equal-neighbors restriction is an ordinary contiguous constraint on hosts, not on targets. The bivariate series is formal, so no analytic convergence assumption is used for its coefficient identities. The random model is exactly uniform on the \(q(q-1)^{n-1}\) proper words of positive length, equivalently a uniform first letter followed by uniform choices among letters different from the preceding letter. The asymptotics hold for fixed \(q\ge3\), not uniformly in growing alphabet size.

## Proof
**1. Greedy arches compute the index.** Starting at the first letter, cut at the earliest position where the current segment has seen all \(q\) symbols; repeat and leave an incomplete suffix. Suppose this produces \(m\) complete arches, with completion symbols \(a_1,\ldots,a_m\). Choosing the required symbol from each of the first \(k\le m\) arches embeds any prescribed \(k\)-letter target. Conversely choose \(b\) absent from the final incomplete suffix. For the pattern \(a_1\cdots a_mb\), greedy subsequence matching must choose \(a_1\) at the end of the first arch, because its completion symbol appears nowhere earlier in that arch. Inductively it chooses \(a_i\) at the end of arch \(i\), then fails to find \(b\) in the suffix. As greedy matching succeeds whenever any embedding exists, this pattern is absent. Thus \(\iota(w)=m\), including the empty word.

**2. Count an arch after a fixed preceding letter.** Before a new arch, fix the immediately preceding letter \(c\) (which is not included in that arch). The next letter has \(q-1\) choices and contributes \((q-1)z\). Once exactly \(j\) distinct symbols have appeared in the arch, the last symbol is among them: at each next position there are \(j-1\) legal already-seen symbols and \(q-j\) unseen symbols. The generating function for any number of legal repeats followed by the first new symbol is
\[
\frac{(q-j)z}{1-(j-1)z}.
\]
Multiplying these stages gives \(A(z)=(q-1)zE_q(z)\) for the first completed arch. Stopping with exactly \(j\in\{1,\ldots,q-1\}\) seen symbols and allowing any number of additional already-seen legal symbols gives \((q-1)zE_j(z)/(1-(j-1)z)\). Adding the empty continuation gives \(B(z)\). By permuting alphabet labels, these generating functions do not depend on the fixed preceding symbol. For the first segment of the whole word there is no preceding symbol, giving \(q\) rather than \(q-1\) options initially. Accordingly, the first-arch series is \(A_0=qA/(q-1)\), and the no-complete-arch initial-suffix series is \(B_0=1+q(B-1)/(q-1)\).

Each word has a unique greedy arch decomposition. Words with index zero contribute \(B_0\); words with index \(k\ge1\) contribute \(A_0A^{k-1}B\). Summing over \(k\) proves the all-alphabet bivariate identity. Substituting \(q=3\) gives \(A=4z^3/(1-z)\), \(B=(1+z+2z^2)/(1-z)\), \(A_0=6z^3/(1-z)\), \(B_0=(1+2z+3z^2)/(1-z)\); cancellation yields the stated cubic-denominator formula.

**3. Probability and renewal.** Generate an infinite word by a uniform initial symbol and independent uniform legal transitions among the other \(q-1\) symbols. Let \(L\) be the number of new positions needed to complete an arch. On first acquiring its \(j\)-th distinct letter, the probability that any following position first acquires a new symbol is \(p_j=(q-j)/(q-1)\), independent of the particular last symbol. The waiting time \(G_j\) (counting the successful acquisition) is geometric on positive integers with parameter \(p_j\). The strong Markov property and label symmetry make these waiting times independent within and between arches. The first letter occupies one position, so
\[
L\overset d=1+\sum_{j=1}^{q-1}G_j,
\qquad G_j\sim\operatorname{Geom}\bigl((q-j)/(q-1)\bigr)
\quad\text{independently}.
\]
All successive complete-arch lengths are identically and independently distributed, including the initial one. Their partial sums are renewal epochs; \(I_n\) counts epochs no later than \(n\). Therefore the geometric mean/variance identities give \(\mathbb EL=\mu_q\) and \(\operatorname{Var}(L)=v_q\).

For \(q=3\), the first waiting time is identically one and the second is geometric with success probability one half, so \(L\overset d=2+\operatorname{Geom}(1/2)\). Completing \(k\) arches by time \(n\) is equivalent to observing at least \(k\) successes in \(n-2k\) independent fair Bernoulli trials; this proves the binomial-tail formula. Its edge case \(n<3k\) is impossible because each arch has at least three letters.

For fixed \(q\ge3\), \(L\) has span one, finite exponential moments, and strictly positive variance. The classical arithmetic renewal-count central limit theorem gives the asserted Gaussian limit. Moreover, the rational probability generating function
\[
\sum_{n,k\ge0}\Pr(I_n=k)z^nu^k
=\frac{1-\phi_q(z)}{(1-z)(1-u\phi_q(z))},\qquad
\phi_q(z)=A\bigl(z/(q-1)\bigr)
\]
shows, by differentiation at \(u=1\) and the unique simple dominant pole at \(z=1\), the stated \(O_q(1)\) mean and variance errors. The uniqueness follows from span one and positive coefficients of \(L\) at every sufficiently large integer. The \(q=2\) source is deterministic after the first letter and is treated separately.

**4. Shortest complete universality.** Each complete arch has at least \(q\) symbols. Thus the least host length at index \(k\) is \(qk\), realized by concatenating \(k\) permutations. At that length each arch must be exactly one permutation. The first permutation has \(q!\) choices. At each further arch, the first symbol cannot equal the preceding arch's last symbol: there are \(q-1\) choices for this first symbol and \((q-1)!\) ways to order the remaining symbols. Multiplication proves the shortest-host count.

## Verification
The included standard-library Python program `verify.py` independently expands the rational stage products and checks them against an actual-letter finite-state enumeration, and also enumerates proper words by explicit recursion. It checked \(1{,}130{,}960\) complete hosts across alphabet sizes \(2,3,4,5,6\), with maximum tested lengths respectively \(12,18,10,8,7\), comparing \(228\) index-refined coefficients. It additionally performed \(112{,}420\) literal pattern-embedding tests and checked the ternary rational recurrence, exact binomial tails and shortest-host formula. Output:

`VERIFY_OK proper_hosts=1130960 literal_pattern_checks=112420 parameter_coefficients=228 alphabets=2..6 nmax={2: 12, 3: 18, 4: 10, 5: 8, 6: 7} ternary_binomial_tails=TRUE`

Run with `python3 verify.py`. The finite checks are independent sanity tests of the symbolic arguments, not a substitute for the infinite proof or renewal limit theorem.

## Relationship to prior work
Adamson (2023, arXiv:2304.04583) supplies algorithms for counting unrestricted \(k\)-subsequence-universal words, and Adamson, Fleischmann, Huch, Koß, Manea and Nowotka (2023, arXiv:2311.10658) give counting and ranking algorithms when the host language is regular. Those general algorithms can in principle be applied to the proper-coloring regular language. Neither inspected counting treatment states the present all-alphabet product formula, the ternary cubic-denominator law or binomial survival formula, or the explicit renewal/dispersion constants for uniform proper words. The greedy arch characterization and standard renewal central limit theorem are prior ingredients rather than new claims. The contribution is the explicit solution for the natural non-repeating host language and its exact finite-length/limiting distribution.

## Limitations
The result does not address biased transition matrices, restrictions on longer factors, or alphabets whose size grows with the host length. No independent external mathematical audit has been carried out. An equivalent specialization hidden in a broader published automata or renewal analysis remains possible. Numerical tests cover only the stated finite ranges; symbolic algebra and renewal arguments establish the all-parameter results.

## References
- D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583, first publicly submitted 2023-04-10, sections 2–3.
- D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658, first publicly submitted 2023-11-17, especially section 4.
- Classical arithmetic renewal-count central limit theorem and elementary geometric waiting-time identities (standard probability tools; no priority claimed).
