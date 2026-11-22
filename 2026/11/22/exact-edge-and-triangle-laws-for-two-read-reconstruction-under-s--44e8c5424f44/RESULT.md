# Exact edge and triangle laws for two-read reconstruction under single-triple avoidance

## Finding

Let \(f\in\{001,100,110,011\}\). For each integer \(n\ge0\), let \(\mathcal L_f(n)\) be the set of indexed binary words of length \(n\) containing no contiguous occurrence of \(f\). On \(\mathcal L_f(n)\), join two distinct words exactly when their **sets of distinct one-deletion descendants** have at least two elements in common. Write \(E_f(n)\) for the number of unordered edges, \(T_f(n)\) for the number of unordered triangles, and take both numbers to be zero if no such configurations exist. Then, as formal power series,

\[
E_f(z)=\sum_{n\ge0}E_f(n)z^n=\frac{z^2(1+z)}{(1-z)(1-z-z^2)^2},
\qquad
T_f(z)=\sum_{n\ge0}T_f(n)z^n=\frac{z^4(1+z)}{(1-z)^2(1-z-z^2)^2}.
\]

More strongly, the following exact coefficient identity holds for every \(n\ge0\):

\[
T_f(n)=\sum_{j=2}^{n-2}E_f(j),
\]

where an empty sum equals zero. Thus the first triangle occurs at length four, and \(T_f(n)/E_f(n)\to1\) as \(n\to\infty\); equivalently, the mean number of triangles containing an edge tends to three. For \(f=001\), the initial values at lengths \(n=2,\ldots,12\) are

\[
(E_f(n))_{n=2}^{12}=(1,4,11,26,56,114,223,424,789,1444,2608),
\]
\[
(T_f(n))_{n=2}^{12}=(0,0,1,5,16,42,98,212,435,859,1648).
\]

## Assumptions and scope

Words are linear, labeled, and indexed, not circular words or necklaces. In particular, factor avoidance does not wrap around the ends. For \(w=w_1\cdots w_n\), define \(D_1(w)=\{w_1\cdots w_{i-1}w_{i+1}\cdots w_n:1\le i\le n\}\); **set** semantics distinguish this observation from a multiset of deletion histories. A triangle is a three-element vertex set in which all three pairs are edges. The result holds at every nonnegative integer length. The four forbidden factors in the statement form one orbit under whole-word reversal and bit complementation, both of which preserve deletion-ball intersection sizes; hence it suffices to prove the case \(f=001\).

## Proof

**1. The established edge normal form.** By the single-deletion Type-A characterization of Cai, Kiah, Nguyen, and Yaakobi (Definition 8 and Proposition 9), two different binary words have two distinct common one-deletion descendants if and only if they have a unique expression as the same prefix \(u\), two **opposite phases** \(a,\bar a\) of an alternating binary block of length \(L\ge2\), and the same suffix \(v\):

\[
x=uav,\qquad y=u\bar a v,\qquad a\in\{0101\cdots,1010\cdots\}.
\]

Here the first and last positions of the alternating block are exactly the first and last coordinates where \(x\) and \(y\) differ. Consequently the interval, the two phases (as an unordered pair), and both outside contexts are unambiguously determined by the edge. This known normal form is the only nontrivial external lemma needed for edge enumeration.

**2. Exact boundary admissibility.** Both opposite-phase words avoid `001` precisely when (i) \(u\) avoids `001` and is empty or ends in `1`, and (ii) \(v\) avoids `001` and does not start with `01`. The alternating blocks themselves cannot contain `001`. If \(u\) ends in `0`, one phase begins in `01` and creates `001` crossing the left boundary. If \(v\) begins in `01`, the phase ending in `0` creates `001` crossing the right boundary. Conversely, these are the only possible crossing occurrences: each block begins with one of `01` and `10` and ends with one of those pairs, while an occurrence of `001` requires a `00` immediately before its final `1`. This establishes necessity and sufficiency, including blocks of length two.

A `001`-avoiding word which ends in `1` cannot contain `00`: after any `00`, every later symbol is forced to be `0`. Thus the allowed left contexts are the empty word and words avoiding `00` and ending in `1`. Let \(P(z)\) count them by length. Their numbers are \(F_{m+1}\) at length \(m\ge0\), with \(F_1=F_2=1\), so

\[
P(z)=\frac1{1-z-z^2}.
\]

For completeness, the generating function of all `001`-avoiding words is

\[
A(z)=\frac{1+z}{1-z-z^2}+\frac{z^2P(z)}{1-z}
=\frac1{(1-z)(1-z-z^2)}.
\]

The first term counts words avoiding `00`, and the second counts words whose *first* `00` begins a terminal all-zero suffix (the preceding prefix is empty or ends in `1`). The allowed right contexts are exactly the empty word, a nonempty all-zero word, or a word starting in `1` and otherwise avoiding `001`. Their generating function therefore is

\[
S(z)=\frac1{1-z}+zA(z)=\frac{1+z}{1-z-z^2}.
\]

**3. Edge count.** For each \(L\ge2\), there is one unordered pair of opposite alternating length-\(L\) blocks. Every allowed prefix and suffix pair yields a distinct edge, and every edge arises uniquely this way. Marking length gives

\[
E_{001}(z)=P(z)\left(\sum_{L\ge2}z^L\right)S(z)
=P(z)\frac{z^2}{1-z}S(z)
=\frac{z^2(1+z)}{(1-z)(1-z-z^2)^2}.
\]

**4. Triangle structure and forbidden splice.** The general two-read triangle normal form says that every triangle has a unique *long* opposite-alternating edge block of length \(L\ge4\) and a third vertex obtained by taking the prefix of one long-edge phase through a cut and the suffix of the opposite phase after the cut. The cut lies at least two positions from either end; thus there are \(L-3\) cut positions and, in the unrestricted binary graph, two splice choices. This published normal form can also be seen directly: at each coordinate, a three-word triangle has either three equal letters or exactly two equal letters; its three pairwise difference intervals therefore cover each coordinate zero or twice, forcing one long interval partitioned into two shorter adjacent intervals, both of length at least two.

At a splice cut, one choice contains `00` and the other contains `11`. In the `00` choice, the immediately following symbol is `1` because the suffix of the alternating block has at least two letters. Hence that choice contains the forbidden `001` and is inadmissible. The `11` choice contains no internal `00`, so is admissible. Moreover, its first two and last two block symbols are those of one of the original phases: the same boundary conditions on \(u,v\) from Step 2 ensure that the third word is admissible. Exactly **one** of the two splice choices survives at every cut. Uniqueness of the long interval and cut prevents overcounting.

**5. Triangle count and identity.** Each allowed context pair and each \(L\ge4\) contributes precisely \(L-3\) triangles, giving

\[
T_{001}(z)=P(z)\left(\sum_{L\ge4}(L-3)z^L\right)S(z)
=P(z)\frac{z^4}{(1-z)^2}S(z)
=\frac{z^4(1+z)}{(1-z)^2(1-z-z^2)^2}.
\]

Dividing the expressions in Steps 3 and 5 gives \(T_{001}(z)=z^2E_{001}(z)/(1-z)\). Extracting coefficients proves the cumulative edge–triangle identity for all lengths. Reversal and bit complementation carry the proof over to all four listed forbidden triples.

**6. Asymptotic consequence.** Set \(\varphi=(1+\sqrt5)/2\) and \(\rho=\varphi^{-1}\). The pole at \(\rho\) dominates all other poles of both rational series. Since \(1-\rho=\rho^2\) and \(1+2\rho=\sqrt5\), elementary double-pole coefficient extraction yields

\[
E_f(n)\sim\frac{\varphi^3}{5}\,n\varphi^n,
\qquad
T_f(n)\sim\frac{\varphi^3}{5}\,n\varphi^n.
\]

Thus \(T_f(n)/E_f(n)\to1\). Counting edge–triangle incidences gives exactly three incidences per triangle, so the mean number of triangles containing a uniformly chosen edge is \(3T_f(n)/E_f(n)\to3\). This limit is an incidence average, not a statement that each edge lies in exactly three triangles.

## Verification

The two reproducibility scripts, `verify_decks.py` and `verify_structural.py`, are standalone Python 3 programs using only the standard library. The first explicitly enumerates **distinct deletion descendant sets** and then computes edge and triangle counts over every `001`-avoiding word at each length from one through twelve. The second independently enumerates alternating intervals and their legal contexts, builds the actual edge and triangle **sets** through length ten, independently reconstructs direct deletion-deck graph sets for comparison, and checks the rational coefficient convolution plus cumulative identity through length thirty-two. Both scripts were executed from the corresponding package source files and reported success. Finite enumeration checks concrete small instances only; the all-length theorem is supplied by Steps 1–6, not by extrapolation from samples.

## Relationship to prior work

Levenshtein's 2001 work introduced exact reconstruction from distinct deletion traces. Cai–Kiah–Nguyen–Yaakobi's 2020 Proposition 9 supplies the alternating-edge equivalence, which is **an established premise** and is not claimed here. A previously published general two-read triangle normal form classifies all triangles in the unrestricted alphabet space; it supplies the general splice geometry, but it does not distinguish allowed contexts or count triangles in the `001`-avoiding induced graph. The unrestricted edge enumeration likewise does not furnish this constrained count. The present result consists of the sharp one-splice survival mechanism, two independent Fibonacci-context factors, explicit constrained edge and triangle generating functions, and the resulting cumulative identity and limiting incidence law. The reverse/complement orbit \(\{001,100,110,011\}\) is not the orbit of `010`, so restricted computations for `010` are neither equivalent nor stronger. The all-run-cap constraints also exclude a different source family. These comparisons concern the mathematical implications, not mere matching titles.

## Limitations

This is a graph census, not an exact maximum independent-set result or an optimal two-read code-size formula. The derivation uses published edge and triangle normal forms, whose hypotheses and applications are stated explicitly. No claim is made for arbitrary forbidden words beyond the specified four-pattern orbit, for a cyclic avoidance rule, or for a channel that retains deletion-history multiplicities. The closest general structural source was read in full; nevertheless, unindexed older restricted-motif enumerations could affect novelty. External independent mathematical validation has not been performed.

## References

1. V. I. Levenshtein, *Efficient Reconstruction of Sequences from Their Subsequences or Supersequences*, Journal of Combinatorial Theory, Series A **93** (2001), 310–332, DOI:10.1006/jcta.2000.3081 (first published February 1, 2001).
2. Kui Cai, Han Mao Kiah, Tuan Thanh Nguyen, Eitan Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376 (first preprint January 6, 2020), Definition 8 and Proposition 9, https://arxiv.org/abs/2001.01376.
3. Johan Chrisnata, Han Mao Kiah, Eitan Yaakobi, *Correcting Deletions With Multiple Reads*, IEEE Transactions on Information Theory **68** (2022), 7141–7160, Section VI, Lemma 28, DOI:10.1109/TIT.2022.3184868.
4. *Exact triangle spectrum of the two-read deletion-confusability graph*, published published-finding corpus research record (2026), available at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-triangle-spectrum-of-the-two-read-deletion-confusability-g--e753c7b5bfd6.
5. *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*, published published-finding corpus research record (2026), available at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91.
