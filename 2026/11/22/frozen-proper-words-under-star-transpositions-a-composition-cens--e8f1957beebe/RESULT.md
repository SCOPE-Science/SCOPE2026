# Frozen proper words under star transpositions: a composition census and a sharp balanced threshold

## Finding
Let \(\Sigma\) be a named alphabet with \(q\ge3\) symbols. A word of length \(n\ge3\) is **proper** if every two consecutive symbols differ. Its **star-swap neighbors** are the distinct proper words obtained by exchanging its first symbol with one symbol in a later position. A proper word is **frozen** if it has no star-swap neighbor. Swaps preserve every symbol multiplicity, so the same definition applies in each fixed-composition multiset-permutation graph.

All frozen words admit the unique block decomposition proved below. In indeterminates \(\{z_s:s\in\Sigma\}\), their exact all-composition enumerator is
\[
\mathcal F_{\Sigma}(\mathbf z)=\sum_{a\ne b}
\frac{z_a^2z_b\bigl(1+S_a+z_bT_{a,b}\bigr)}
{1-z_a\bigl(S_a+P_a+z_bT_{a,b}^{2}\bigr)},
\]
where
\[
S_a=\sum_{s\ne a}z_s,\qquad
P_a=\sum_{\substack{s,t\ne a\\s\ne t}}z_sz_t,\qquad
T_{a,b}=\sum_{c\notin\{a,b\}}z_c.
\]
In particular, the coefficient of \(\prod_{s\in\Sigma}z_s^{m_s}\) is the exact number of frozen words with the prescribed symbol counts \((m_s)\), without dividing by alphabet permutations or rotation.

Writing \(I_{q,n}\) for the number of frozen proper words of length \(n\), the corresponding ordinary generating function simplifies to
\[
\boxed{\sum_{n\ge3}I_{q,n}z^n
=\frac{q(q-1)z^3(1+(q-2)z)}
{1-z-(q-2)z^2-(q-2)^2z^3}.}
\]
Thus the ternary counts begin \(6,12,18,36,66,120,\ldots\) at lengths \(3,4,5,6,7,8\) and obey a shifted tribonacci recurrence. More generally, the characteristic growth root is the unique positive solution of \(\lambda^3=\lambda^2+(q-2)\lambda+(q-2)^2\); for \(q\ge3\) it lies strictly between \(1\) and \(q-1\). Frozen words are exponentially rare among all proper words but exist at arbitrarily large lengths.

There is also a **sharp composition obstruction**. Every frozen word of length \(n\) whose first symbol occurs \(k\) times satisfies
\[
\boxed{n\le4k-3,}
\]
and this length bound is attained for every integer \(k\ge2\) on any alphabet of at least three symbols. Consequently, among proper words in which all \(q\) symbols occur exactly \(m\) times, a frozen word exists **if and only if** \(q=3\) and \(m\ge3\), for \(q\ge3\) and \(m\ge1\). In the ternary equal-composition classes the **exact number** is \(0\) at \(m=1\), and for every \(m\ge2\) it is
\[
\boxed{6\binom{2m-3}{m}.}
\]
The initial values at \(m=1,2,3,4,5,6\) are \(0,0,6,30,126,504\).

## Assumptions and scope
Positions are labeled, indexed \(0,1,\ldots,n-1\). The allowed move exchanges positions \(0\) and \(j\), for \(1\le j<n\), only when the resulting word is proper and distinct. This is **not** the adjacent-position-swapping rule and is not a cyclic-word convention. All words and alphabets are labeled. The theorem concerns single legal moves and isolated vertices of their reconfiguration graph; it does not assert that a graph without isolated vertices is connected or Hamiltonian.

The multivariate series is interpreted formally: each term has total degree at least three and each coefficient is finite. In the equal-composition statement every symbol of the specified alphabet is required to occur exactly \(m\) times.

## Proof
Fix a proper word \(w=w_0w_1\cdots w_{n-1}\), with \(a=w_0\) and \(b=w_1\ne a\). Exchanging positions \(0\) and \(1\) preserves properness if and only if \(w_2\ne a\). Hence a frozen word necessarily starts with \(aba\), where \(w_2=a\). For a later position \(j\ge2\), a nontrivial star swap is proper exactly when
\[
w_j\notin\{a,b\},\quad w_{j-1}\ne a,\quad
\bigl(j=n-1\text{ or }w_{j+1}\ne a\bigr).
\]
The first condition keeps the new first symbol different from \(b\), and the remaining conditions keep the inserted \(a\) different from its neighbors at position \(j\). These conditions are exhaustive because no other positions change.

Let \(C=\Sigma\setminus\{a,b\}\) and \(L=\Sigma\setminus\{a\}\). Look at maximal factors between successive occurrences of \(a\), starting from the third position. An internal block of letters other than \(a\) can have length one (any member of \(L\)), length two (two distinct members of \(L\)), or length three (necessarily \(cbd\) with \(c,d\in C\)). In a longer block two adjacent interior positions would both have to be \(b\), contradicting properness. Conversely, every indicated block has no star-swappable letter. After the last \(a\), the tail has length zero, length one (any member of \(L\)), or length two (necessarily \(cb\), with \(c\in C\)); a longer tail is impossible by the same local test. Therefore **every and only** frozen word has the unique form
\[
aba\ \bigl[(La)\ \cup\ (\{st a:s,t\in L,\ s\ne t\})\ \cup\ (CbCa)\bigr]^*\
\bigl(\{\varepsilon\}\cup L\cup Cb\bigr).
\]
Here \(La\), \(CbCa\), and \(Cb\) are sets of concatenations of the indicated letters, not products in an algebra, and the repeated block begins immediately after the compulsory prefix \(aba\). Uniqueness follows from cutting at occurrences of \(a\).

The prefix contributes \(z_a^2z_b\). The possible tails contribute \(1+S_a+z_bT_{a,b}\). Each complete block ending in the next \(a\) contributes, respectively, \(z_aS_a\), \(z_aP_a\), or \(z_a z_bT_{a,b}^2\). Summing the geometric series of independent complete blocks and then summing over distinct initial symbols \(a,b\) proves the multivariate formula.

When all \(z_s=z\), the prefix has \(q(q-1)\) choices and the tail has enumerator \(1+(q-1)z+(q-2)z^2\). The three complete-block weights are \((q-1)z^2\), \((q-1)(q-2)z^3\), and \((q-2)^2z^4\). The resulting length series is
\[
\frac{q(q-1)z^3\bigl(1+(q-1)z+(q-2)z^2\bigr)}
{1-(q-1)z^2-(q-1)(q-2)z^3-(q-2)^2z^4}.
\]
The numerator factor \(1+z\) cancels with the same factor in the denominator, yielding the stated cubic rational series. Its denominator gives the weighted-tribonacci recurrence. The polynomial \(x^3-x^2-(q-2)x-(q-2)^2\) has exactly one positive root by Descartes' rule; its values at \(1\) and \(q-1\) have opposite signs. Primitivity of the positive three-step recurrence gives the stated exponential growth order, strictly below \((q-1)^n\).

For the length bound, if \(a\) occurs \(k\) times, its first two occurrences occupy positions \(0\) and \(2\). Each of the remaining \(k-2\) occurrences requires at most four additional positions, and the final tail has at most two positions. Thus \(n\le3+4(k-2)+2=4k-3\). Equality is realized, for any distinct \(a,b,c\), by
\[
aba\ (cbca)^{k-2}\ cb.
\]
For a balanced word of length \(qm\), the bound would require \(qm\le4m-3\). This excludes all \(q\ge4\), and it excludes \(q=3\) for \(m=1,2\). Conversely, for every \(m\ge3\), the ternary word
\[
aba\ cbca\ (cba)^{m-3}\ cb
\]
is proper, frozen by the block classification, and has exactly \(m\) occurrences of each of \(a,b,c\). This proves the sharp equal-composition threshold.

For an exact coefficient specialization, fixing distinct \(a,b,c\) and writing \(u=z_b,v=z_c\) gives
\[
I_{3,3m}^{\mathrm{balanced}}
=6[u^{m-1}v^m](1+u+v+uv)
(u+v+2uv+uv^2)^{m-2}\quad(m\ge2),
\]
with value zero at \(m=1\). Here \(u+v+2uv+uv^2=v+u(1+v)^2\) and the tail factor is \((1+u)(1+v)\). The target exponent \(u^{m-1}\) forces choosing \(u(1+v)^2\) from **every** one of the \(m-2\) complete blocks and the factor \(u\) from the tail. The remaining coefficient is \(6[v^m](1+v)^{2m-3}=6\binom{2m-3}{m}\), which proves the closed binomial formula and the displayed exact counts.

## Verification
The included `verify_frozen.py` uses standard-library integer arithmetic. It directly generates proper words and tests every possible star swap; separately it expands the unique-block composition grammar. The two independent descriptions have identical complete composition histograms for each length \(3\le n\le9\) at alphabet size \(2\), each length \(3\le n\le10\) at size \(3\), each length \(3\le n\le8\) at size \(4\), and each length \(3\le n\le7\) at size \(5\). The cubic length recurrence agrees with every one of these enumerations. The exact binomial balanced formula through \(m=6\) and the explicit ternary construction through \(m=24\) are also checked. The general theorem is established by the preceding argument, not by extrapolation from finite experiments.

Run `python3 verify_frozen.py` from the folder containing the included files. No network access, third-party packages, or optimization solver is required.

## Relationship to prior work
Gregor, Merino and Mütze study star-transposition Gray codes for **all** permutations of a fixed multiset, without the adjacent-inequality constraint. Their earliest accessible arXiv version is dated 17 August 2021. The current graph is an induced graph after imposing the proper-word constraint, so their connectivity and Hamiltonicity statements do not imply the isolated-vertex classification here. Fuchs et al. study proper-coloring reconfiguration under swaps at **adjacent vertices of the colored graph**. On a path that means adjacent positions, not a first-position-to-arbitrary-position swap; their 2025 article does not imply this census. A separate adjacent-swap degree spectrum for proper words similarly concerns a different edge rule: for example `0102` is frozen under star swaps but allows a proper adjacent swap, while `010121` has the opposite behavior.

The exact rational all-composition enumerator and sharp equal-composition alphabet threshold were not found in the inspected literature and indexed records. This is a bounded literature comparison, not a proof of global bibliographic novelty.

## Limitations
The theorem characterizes isolated configurations; it neither classifies all connected components nor settles existence of Gray codes after removing isolated vertices. In particular, the absence of isolated vertices when \(q\ge4\) with equal symbol multiplicities is not a claim of Hamiltonicity. All proofs concern finite named alphabets and the specified proper-word/star-swap model only. Earlier equivalent statements under another terminology cannot be ruled out by finite literature search.

## References
1. P. Gregor, A. Merino, T. Mütze, *Star transposition Gray codes for multiset permutations*, arXiv:2108.07465 (first submitted 17 August 2021); *Journal of Graph Theory* 103 (2023), 212–270. https://arxiv.org/abs/2108.07465 and https://doi.org/10.1002/jgt.22915
2. J. Fuchs, R. Saito, T. Suga, T. Suzuki, Y. Tamura, *Coloring Reconfiguration under Color Swapping*, arXiv:2511.06473 (9 November 2025), especially Sections 2 and 4.1. https://arxiv.org/abs/2511.06473
3. MSC2020, classification 68R15, *Combinatorics on words*. https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=68R15
