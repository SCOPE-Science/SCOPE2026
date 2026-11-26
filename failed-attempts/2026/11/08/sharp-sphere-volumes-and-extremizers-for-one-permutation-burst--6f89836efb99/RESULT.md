# Sharp sphere volumes and extremizers for one permutation burst

## Finding
Fix an alphabet \(\Sigma\) of size \(q\ge2\), a word \(x\in\Sigma^n\), and integers \(n\ge k\ge2\). Let \(\mathcal B_k(x)\) be the set of length-\(n\) words obtained by permuting symbols in one consecutive block of exactly \(k\) positions; the identity is allowed. Different operation histories giving the same received word are counted once.

For a word \(v=v_1\cdots v_m\), let \(c_a(v)\) be the multiplicity of letter \(a\), let \(M(v)=m!/\prod_{a\in\Sigma}c_a(v)!\), and define
\[
T(v)=M(v)\left[1-\frac{c_{v_1}(v)+c_{v_m}(v)}m
+\frac{c_{v_1}(v)(c_{v_m}(v)-\mathbf{1}_{v_1=v_m})}{m(m-1)}\right],\qquad m\ge2.
\]
This is a nonnegative integer. The **exact volume for every center and alphabet** is
\[
|\mathcal B_k(x)|=1+\sum_{m=2}^{k}\sum_{i=1}^{n-m+1}T(x_i\cdots x_{i+m-1}). \tag{1}
\]
Put \(f_m=m!-2(m-1)!+(m-2)!\). Then
\[
|\mathcal B_k(x)|\le U_k(n):=1+\sum_{m=2}^{k}(n-m+1)f_m. \tag{2}
\]
Equality holds **if and only if every consecutive length-\(k\) factor of \(x\) has pairwise different symbols**. In particular this universal bound is attainable on a \(q\)-letter alphabet exactly when \(q\ge k\); in that case its exact number of attaining centers is
\[
(q)_k(q-k+1)^{n-k},\qquad (q)_k=q(q-1)\cdots(q-k+1). \tag{3}
\]
For the smallest genuinely multiletter case \(k=3\), this yields a sharp alphabet dichotomy for every \(n\ge3\):
\[
\max_{x\in\Sigma^n}|\mathcal B_3(x)|=
\begin{cases}
\lfloor3n/2\rfloor-1,&q=2,\\
4n-6,&q\ge3.
\end{cases} \tag{4}
\]
For \(q=2\), exactly two words maximize (4) when \(n\) is even, while exactly \(n+3\) words maximize when \(n\) is odd. For \(q\ge3\), the number is \(q(q-1)(q-2)^{n-2}\).

The **complete binary sphere-volume distribution**, rather than just its maximum, is given for \(n\ge3\) by
\[
\sum_{x\in\{0,1\}^n}z^{|\mathcal B_3(x)|}
=2z\,(1,z)
\begin{pmatrix}1&z^2\\z&z\end{pmatrix}^{n-2}
\binom{1}{1}. \tag{5}
\]
In particular, for an independent uniform binary source \(X\),
\[
\mathbb E|\mathcal B_3(X)|=n-\tfrac12,\qquad
\operatorname{Var}(|\mathcal B_3(X)|)=\frac{2n-3}{4}. \tag{6}
\]

## Assumptions and scope
An operation chooses one block of exactly \(k\) adjacent positions and replaces its letters by any ordering of that block's multiset. A received word may coincide with the source. The alphabet is an arbitrary labeled finite set, not necessarily a finite field. Equations (1) and (2) hold for all \(q\ge2\) and \(n\ge k\ge2\). Equations (3) and the universal maximum require \(q\ge k\); (4)–(6) concern exactly \(k=3\), with \(n\ge3\). No multiple bursts or changes of word length are allowed.

## Proof
**Canonical minimal changed interval.** For a nonidentity descendant \(y\), let \(i\) and \(j\) be its first and last coordinates differing from \(x\), and put \(m=j-i+1\). The changed interval is contained in the chosen length-\(k\) block, hence \(2\le m\le k\). The multisets of \(x_i\cdots x_j\) and \(y_i\cdots y_j\) coincide because positions in the chosen block outside \([i,j]\) are unchanged. Conversely, whenever \(2\le m\le k\), any multiset permutation of \(x_i\cdots x_j\) with both endpoints changed defines a legal descendant: \([i,j]\) is contained in some length-\(k\) window since \(n\ge k\). The first and last changed coordinates are uniquely determined by \(y\). Thus nonidentity descendants partition disjointly by their minimal changed interval.

**Count for a fixed interval.** There are \(M(v)\) multiset permutations of \(v\). Of these, exactly \(M(v)c_{v_1}/m\) keep the first symbol, and \(M(v)c_{v_m}/m\) keep the last. The fraction keeping both endpoints is \(c_{v_1}(c_{v_m}-\mathbf{1}_{v_1=v_m})/[m(m-1)]\). Inclusion–exclusion gives \(T(v)\), and the disjoint interval partition gives (1).

**Sharp universal bound and all extremizers.** If the \(m\) letters of \(v\) are distinct, exactly \(f_m\) of the \(m!\) permutations change both endpoints. If any letter is repeated, label the positions temporarily. Each admissible *unlabeled* received ordering has at least two distinct labeled realizations, and every realization that changes the endpoint values also changes the corresponding endpoint position labels. There are only \(f_m\) labeled permutations changing both endpoint labels, so \(T(v)<f_m\). Therefore \(T(v)\le f_m\), with equality precisely when \(v\)'s letters are pairwise distinct. Summing proves (2), and equality is equivalent to all factors of length at most \(k\) being injectively letter-labeled, equivalently every length-\(k\) factor being pairwise distinct. This is feasible precisely for \(q\ge k\). Choose \(x_1,\ldots,x_k\) injectively in \((q)_k\) ways; for every later coordinate, exactly \(q-k+1\) letters are different from the preceding \(k-1\). This proves (3).

**Binary triple-window extremum.** When \(q=2,k=3\), the only nonidentity rearrangements with minimal changed interval of length two or three respectively are swaps of unequal adjacent or distance-two symbols. Set \(d_i=x_i\oplus x_{i+1}\in\{0,1\}\) for \(1\le i<n\). Equation (1) becomes
\[
|\mathcal B_3(x)|-1
=\sum_{i=1}^{n-1}d_i+\sum_{i=1}^{n-2}(d_i\oplus d_{i+1}). \tag{7}
\]
For bits \(a,b\), the quantity \(a+b+(a\oplus b)\) is \(2\) except when \((a,b)=(0,0)\), when it is zero. When \(n=2m+1\), group the \(2m\) difference bits into \(m\) consecutive pairs. The paired contributions total at most \(2m\), and the \(m-1\) bridging XORs contribute at most \(m-1\). Equality requires no pair to be \((0,0)\) and each bridge to switch bits. There are exactly \(m+2\) such difference words: the all-\((1,0)\) pattern; the all-\((0,1)\) pattern; and one for each of the \(m\) positions at which a \((1,1)\) pair replaces the switch from a prefix of \((1,0)\) pairs to a suffix of \((0,1)\) pairs. Thus the maximum of the right side of (7) is \(3m-1\), achieved by \(2(m+2)=n+3\) source words (two choices of initial source bit).

When \(n=2m\), group the first \(2m-2\) difference bits into \(m-1\) pairs and leave the last difference bit alone. The final contribution \(d_{2m-1}+(d_{2m-2}\oplus d_{2m-1})\) is at most \(2\), attained only when the final pair's second bit is zero and the last bit is one. The \(m-1\) paired contributions are at most \(2(m-1)\) and the \(m-2\) bridges are at most \(m-2\). Equality forces the unique difference word \((1,0)^{m-1}1\), hence exactly two source words. Thus the largest right side of (7) is \(3m-2\). Adding the unchanged source proves the binary case of (4) and its maximizer counts. The \(q\ge3\) case of (4) follows from \(f_2=1,f_3=3\) and (2)–(3).

**Complete distribution and moments.** For uniform binary \(x\), the map \((x_1,d_1,\ldots,d_{n-1})\leftrightarrow x\) is a bijection. The first difference contributes \(z^{d_1}\), and appending a bit \(b\) after \(a\) contributes \(z^{b+(a\oplus b)}\). Hence the transfer matrix in (5), multiplied by two choices of \(x_1\) and one factor \(z\) for the unchanged source. For uniform \(x\), the difference bits are independent fair bits. The \(2n-3\) indicators \(d_i\) and \(d_i\oplus d_{i+1}\) are nonzero, pairwise distinct linear forms over \(\mathbb F_2\), hence pairwise independent fair Bernoulli random variables. Their sum equals (7), proving (6).

## Verification
The standalone \(`checker.py`\) computes descendant sets independently by enumerating actual block permutations and verifies (1) for 24,337 distinct center/window/alphabet instances. It checks (2)–(3) exhaustively in these ranges, including the alphabet threshold. It checks binary maxima and multiplicities for lengths \(3\) through \(16\), and compares the complete transfer-matrix distribution and the exact first two moments for lengths \(3\) through \(12\). Run \(`python3 checker.py`\) with Python 3's standard library. These finite checks corroborate but do not replace the all-parameter proofs above.

## Relationship to prior work
Chen and Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage* (2026), introduces the contiguous-permutation-burst channel and studies code redundancy, including cyclic bursts. This result addresses an exact **single-burst descendant-volume** problem: formula (1), the sharp alphabet threshold and complete extremizer count for all \(k\), and the complete binary \(k=3\) volume distribution. The available abstract and independent review did not establish these statements; the primary full text could not be inspected, leaving historical-priority uncertainty. The limited-permutation channel of Ben Shimon and Zabokritskiy instead allows arbitrary sets of disjoint adjacent swaps, not one rearranged consecutive block; its all-length code results do not imply (1)–(6).

## Limitations
The result does not determine optimal correcting codes or confusability intersections, and does not extend to two permutation bursts. For \(q<k\), (2) is strictly unattainable, but its exact replacement is proved here only for \((q,k)=(2,3)\). The historical-priority assessment is limited by inability to inspect the entire closest 2026 paper; independently repeat the literature comparison before claiming publication priority. Independent mathematical audit has not been performed.

## References
1. Y.-P. Chen and O. Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage* (first publicly posted 2026-10-11), arXiv:2610.15701v1, https://arxiv.org/abs/2610.15701.
2. N. Ben Shimon and A. L. Zabokritskiy, *A \(q\)-ary Local Criterion for the Radius-One Limited Permutation Channel and Almost-Optimal Binary Block-Concatenation Codes* (first publicly posted 2026-06-25), arXiv:2606.26905, https://arxiv.org/abs/2606.26905.
3. Y. Sun, Z. Lu, Y. Zhang and G. Ge, *Asymptotically Optimal Codes for \((t,s)\)-Burst Error* (2024), arXiv:2403.11750, https://arxiv.org/abs/2403.11750.
