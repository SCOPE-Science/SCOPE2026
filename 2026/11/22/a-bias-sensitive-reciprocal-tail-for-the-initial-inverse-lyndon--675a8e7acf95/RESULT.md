# A bias-sensitive reciprocal tail for the initial inverse Lyndon array entry

## Finding
Let \(\Sigma=\{a_1<\cdots<a_q\}\), where \(q\ge2\), and let \(W_\infty\) have independent letters with fixed positive probabilities \(p_a\). Let \(p_\top=p_{a_q}\) be the probability of the **lexicographically greatest** letter, and let \(\rho=\max_a p_a<1\). Define \(T\) to be the largest length of a nonempty initial inverse Lyndon word (equivalently, the first inverse Lyndon-array entry of a length-\(N\) prefix, stopped at \(N\)). A nonempty word is inverse Lyndon when it is strictly greater in lexicographic order than each proper nonempty suffix.

Then \(T<\infty\) almost surely, and there exists \(\delta>0\), depending only on the positive source probabilities, such that
\[
\boxed{\Pr(T\ge n)=\frac{1}{(1-p_\top)n}+O_{\boldsymbol p}(n^{-1-\delta}).}
\]
Consequently, for \(T_N=\min(T,N)\), a finite constant \(C_{\boldsymbol p}\) exists for which
\[
\boxed{\mathbb E[T_N]=\frac{\log N}{1-p_\top}+C_{\boldsymbol p}+O_{\boldsymbol p}(N^{-\delta}),\qquad
\operatorname{Var}(T_N)=\frac{2N}{1-p_\top}+o_{\boldsymbol p}(N).}
\]
Moreover \(\mathbb E[T^s]<\infty\) holds exactly for \(0<s<1\); in particular \(T\) has infinite mean. The leading coefficient depends only on the probability of the greatest *ordered* letter, not on the other probabilities individually. For the uniform source it reduces to \(q/(q-1)\), the constant also obtainable from classical prenecklace counts. The new claim is the general nonuniform law and its moment consequences, not uniform enumeration.

## Assumptions and scope
The alphabet is finite and totally ordered, with \(q\ge2\); probabilities \(p_a\) are fixed, positive, and sum to one. Lexicographic comparison uses the convention that a proper prefix is smaller than the longer word. The random variables \(T\) and \(T_N\) are defined on the *same infinite iid word* for all \(N\). Prefix closure of inverse Lyndon words makes \(\Pr(T\ge n)\) equal to the probability that the first \(n\) letters form an inverse Lyndon word. The error constant and exponent are not asserted to be uniform as probabilities approach zero. The statement concerns **a prefix**, not longest inverse Lyndon factors anywhere in the whole word or the number of inverse Lyndon factors.

## Proof
**1. Primitive-root partition.** Call \(u\) anti-Lyndon if it is lexicographically greatest among all its nontrivial cyclic rotations; such a word is primitive. The standard strict-sesquipower characterization identifies inverse Lyndon words exactly with prefixes of repetitions of anti-Lyndon words. The corresponding primitive anti-Lyndon root is unique: equivalently, it is the longest anti-Lyndon prefix of the inverse Lyndon word, and the rest is its periodic continuation. Thus each inverse Lyndon word \(w\) of length \(n\) has one root length \(d\in\{1,\ldots,n\}\) and the representation \(w=u^\infty[1..n]\), where \(u\) is anti-Lyndon of length \(d\). Uniqueness can also be obtained from the ordinary fundamental prenecklace extension lemma after reversing the alphabet order.

**2. Rotation-weight identity.** For \(d\ge1\) let \(X_d\) be an iid length-\(d\) word with the source law. Let \(M_d\) be its greatest cyclic rotation, and let \(B_d\) denote the event that \(X_d\) is primitive. For a word \(v\) and integer \(m\ge0\), write
\[
F_m(v)=\prod_{j=1}^{m}p_{v_{1+((j-1)\bmod |v|)}},\qquad F_0(v)=1.
\]
All \(d\) rotations of a primitive word have the same iid probability. Each primitive rotation orbit has exactly one anti-Lyndon representative. Therefore the probability \(H_n=\Pr(T\ge n)\) satisfies the exact finite identity
\[
\boxed{H_n=\sum_{d=1}^{n}\frac1d\,\mathbb E\big[\mathbf1_{B_d}\,F_{n-d}(M_d)\big].}\tag{1}
\]
Here \(F_{n-d}\) is precisely the probability of the forced continuation of the length-\(d\) root, including repeated cycles when \(n-d>d\). No independence between \(B_d\) and \(M_d\) is assumed.

**3. A short longest-symbol run controls dominant roots.** Set \(r=p_\top\in(0,1)\) and choose
\[
L_n=\left\lfloor\frac{\log n}{4\log(1/r)}\right\rfloor.
\]
For \(0\le m\le L_n\) and \(d=n-m\ge n/2\), partition the first \(d\) letters of \(X_d\) into disjoint groups of length \(m\) (for \(m=0\), this event is vacuous). The probability that none of the groups consists solely of the greatest symbol is at most
\[
(1-r^m)^{\lfloor d/m\rfloor}\le\exp\left[-\lfloor d/m\rfloor r^m\right]
\le \exp\big(-c n^{3/4}/\log n\big),
\]
for a positive source-dependent \(c\), because \(r^m\ge n^{-1/4}\). If any such group occurs, the greatest cyclic rotation \(M_d\) begins with \(m\) copies of \(a_q\), and \(F_m(M_d)=r^m\). Also \(\Pr(B_d^c)\le d\rho^{d/2}\): for each possible proper period \(h\le d/2\), the first \(h\) letters force the remaining \(d-h\) letters, with probability at most \(\rho^{d-h}\), and a union bound suffices. Hence uniformly for \(m\le L_n\),
\[
\mathbb E[\mathbf1_{B_d}F_m(M_d)]
=r^m+O\left(e^{-c n^{3/4}/\log n}+n\rho^{n/4}\right).\tag{2}
\]

**4. Long-continuation tails.** For any \(m\) and \(d\), \(F_m(M_d)\le\rho^m\). Thus the terms in \(nH_n\) from \(m>L_n\) with \(d>n/2\) are at most \(2\sum_{m>L_n}\rho^m\), while the terms with \(d\le n/2\) sum to at most \(n\rho^{n/2}\sum_{d\le n/2}1/d\). Substitute (2) into (1), put \(d=n-m\), and use \(n/(n-m)=1+O(m/n)\) for \(m\le L_n\). Then
\[
nH_n=\sum_{m=0}^{L_n}r^m+O\left(n^{-\eta}+\frac{\log n}{n}\right)
=\frac1{1-r}+O(n^{-\delta}),
\]
where one may take any sufficiently small positive \(\delta<\min\{1/4,\log(1/\rho)/(4\log(1/r))\}\). This proves the quantitative reciprocal tail and \(T<\infty\) almost surely.

**5. Moments.** Prefix closure yields \(\mathbb E[T_N]=\sum_{n=1}^{N}H_n\) and \(\mathbb E[T_N^2]=\sum_{n=1}^{N}(2n-1)H_n\). The reciprocal tail with summable remainder gives
\[
C_{\boldsymbol p}=\frac{\gamma}{1-r}+\sum_{n\ge1}\left(H_n-\frac{1}{(1-r)n}\right),
\]
a convergent real series. It follows that \(\mathbb E[T_N]=(\log N)/(1-r)+C_{\boldsymbol p}+O(N^{-\delta})\), and \(\mathbb E[T_N^2]=2N/(1-r)+o(N)\). Since \(\mathbb E[T_N]^2=O(\log^2N)=o(N)\), the variance conclusion follows. Finally the tail-sum identity
\[
\mathbb E[T^s]=\sum_{n\ge1}\big(n^s-(n-1)^s\big)H_n
\]
behaves like \(s(1-r)^{-1}\sum n^{s-2}\) and is finite exactly when \(s<1\).

## Verification
Two independent Python 3 standard-library programs are included. `check_inverse.py` compares direct exact-rational enumeration using all proper suffixes with the primitive anti-Lyndon-root decomposition for binary distributions through length \(12\) and a nonuniform ternary distribution through length \(8\). `check_fkm.py` independently generates all inverse Lyndon words by the reversed-order Fredricksen–Kessler–Maiorana extension rule and compares their counts with Möbius primitive-necklace enumeration, and checks their rational source probabilities through length \(17\) for binary, \(10\) for ternary, and \(7\) for quaternary alphabets. Both run without third-party dependencies; output is captured in `verification_output.txt`. These finite checks verify the structural enumeration implementation, **not** the infinite limiting theorem, whose proof is above.

## Relationship to prior work
Bonizzoni, De Felice, Zaccagnino and Zizza (arXiv:1705.10277, first public 2017-05-29) provide the strict-sesquipower characterization and prefix closure. Their results and the classical FKM prenecklace extension principle supply the structural decomposition used here; they do not state a biased-source reciprocal tail, the greatest-letter coefficient, or moment thresholds. Bonizzoni and collaborators (arXiv:2404.17969, first public 2024-04-27) also use this equivalence for canonical inverse factorization, not probability tails. Negri, Sica, Zaccagnino and Zizza (arXiv:2603.17537v1, first public 2026-03-18) introduce and construct the inverse Lyndon array and report random-word *runtime* measurements, not the distribution of its first entry. The later expanded inverse-array paper arXiv:2609.23401v1 (first public 2026-09-20) likewise presents structural and algorithmic results.

The uniform \(q\)-ary special case is covered by classical prenecklace counting: the number of length-\(n\) prenecklaces is \(\sum_{d=1}^n L_q(d)\), where \(L_q(d)=d^{-1}\sum_{e\mid d}\mu(e)q^{d/e}\); its uniform asymptotic alone yields \(q/(q-1)\). This uniform case is not claimed original. Chassaing and Zohoorian Azad (arXiv:1004.4062) analyze random Lyndon factorization *factor lengths* and the standard right factor, distinct from the initial inverse-array entry. published-finding corpus's 2026-10-25 bias-sensitive Lyndon-*scattered-subsequence* expectation addresses a different random variable; its 2026-11-08 binary quasinecklace-overhead oscillation addresses a different canonical word class. No earlier source inspected states the general nonuniform \((1-p_\top)^{-1}\) law, but unindexed classical probabilistic work is a residual priority risk.

## Limitations
This is an asymptotic result for fixed strictly positive iid letter probabilities; it makes no uniform rare-letter or growing-alphabet claim. It concerns only the initial inverse Lyndon-array entry, not a full joint array distribution or algorithmic runtime. A finite test cannot establish the infinite asymptotic. The classical root decomposition and uniform count are background, and historical novelty beyond the inspected sources remains subject to independent literature assessment.

## References
1. P. Negri, M. Sica, R. Zaccagnino, R. Zizza, *The Inverse Lyndon Array: Definition, Properties, and Linear-Time Construction*, arXiv:2603.17537v1, first posted 2026-03-18. https://arxiv.org/abs/2603.17537
2. C. De Felice, P. Negri, M. Sica, R. Zaccagnino, R. Zizza, *The Inverse Lyndon Array*, arXiv:2609.23401v1, first posted 2026-09-20. https://arxiv.org/abs/2609.23401
3. P. Bonizzoni, C. De Felice, R. Zaccagnino, R. Zizza, *Inverse Lyndon words and Inverse Lyndon factorizations of words*, arXiv:1705.10277, first posted 2017-05-29. https://arxiv.org/abs/1705.10277
4. P. Bonizzoni, C. De Felice, R. Zaccagnino, R. Zizza, *From the Lyndon factorization to the Canonical Inverse Lyndon factorization: back and forth*, arXiv:2404.17969, first posted 2024-04-27. https://arxiv.org/abs/2404.17969
5. P. Chassaing, E. Zohoorian Azad, *Asymptotic behavior of some factorizations of random words*, arXiv:1004.4062, first posted 2010-04-23. https://arxiv.org/abs/1004.4062
6. Classical FKM prenecklace extension lemma (background), e.g. https://algorithm.tamnd.com/fkm-algorithm/
