# Maximal common-subsequence spectrum of adjacent-swap permutation powers

## Finding

Let \(q\ge4\), let \(P=AxyB\) be a permutation of \(q\) distinct symbols, where \(x\) and \(y\) are consecutive, and set \(Q=AyxB\). For every integer \(k\ge1\) put \(X=P^k\) and \(Y=Q^k\). A *maximal common subsequence* (MCS) is a scattered subsequence of both inputs that is not itself a proper scattered subsequence of another common subsequence.

**Complete classification.** The MCS words are exactly the distinct concatenations
\[
    A s_1 B\, A s_2 B\cdots A s_r B,
    \qquad 1\le r\le k,
\]
where each \(s_i\) is a nonempty alternating word over \(\{x,y\}\), and the total numbers of occurrences of the adjacent transitions \(xy\) and \(yx\) *inside* these \(s_i\) are both exactly \(k-r\). The decomposition is unique, including when one of \(A,B\) is empty (since \(q\ge4\), at least one is nonempty).

Consequently, every integer \(r\in[1,k]\) occurs and the MCS length spectrum is
\[
     \{2k+(q-3)r:1\le r\le k\}.
\]
The number with parameter \(r\) is
\[
 C_{k,r}=\sum_{t=0}^{\min(k-r,\lfloor r/2\rfloor)}
 \frac{r!\,2^{r-2t}}{t!^2(r-2t)!}\binom{k-t-1}{r-1},
\]
and, remarkably, the *total* is independent of both the alphabet size and swap position:
\[
 \sum_{r=1}^k C_{k,r}=\binom{2k}{k}.
\]
In particular, the shortest MCS has length \(q+2k-3\), every longest common subsequence has length \((q-1)k\), and there are exactly \(2^k\) longest common subsequence words. The gap \((q-3)(k-1)\) is unbounded when \(q\ge4\).

## Assumptions and scope

The alphabet has exactly \(q\) distinct letters used once per period. The words \(A,B\) are possibly empty and have disjoint alphabets, all disjoint from \(\{x,y\}\). No restriction on the position of the adjacent swap is imposed. Powers are finite with \(k\ge1\). Subsequence means scattered, not contiguous. Different MCS words are counted as distinct by spelling rather than by their embeddings. The result does not assert anything for repeated-letter periods or nonadjacent swaps.

## Proof

**1. Greedy budgets.** For a permutation \(R\), write \(a\prec_R b\) when letter \(a\) occurs before \(b\) in \(R\), and define
\[
 d_R(w)=\#\{i:w_i\succeq_R w_{i+1}\}
\]
for nonempty \(w\) (weak descents count equal consecutive letters); set \(d_R(\varepsilon)=0\). Greedy embedding scans each increasing stretch of \(w\) into one copy of \(R\), and must begin a fresh copy at each weak descent. Thus for nonempty words
\[
    w\preceq R^k\quad\Longleftrightarrow\quad d_R(w)\le k-1.
\]
When a letter is inserted anywhere, the weak-descent count never decreases and increases by at most one: for insertion between \(a,b\), the increment is \(\mathbf1_{a\succeq_R t}+\mathbf1_{t\succeq_R b}-\mathbf1_{a\succeq_R b}\in\{0,1\}\); analogous statements hold at endpoints.

Every MCS is nonempty and must have *both* budgets saturated:
\[
       d_P(w)=d_Q(w)=k-1.
\]
Indeed, if both are unsaturated, append any alphabet letter. If exactly one is unsaturated, say \(Q\), then \(w\) is a proper subsequence of \(P^k\): equality would force \(w=P^k\), which cannot be a subsequence of the different word \(Q^k\) of the same length. Choose any unused position in an embedding of \(w\) into \(P^k\) and insert that position's letter. This stays a subsequence of \(P^k\) and raises \(d_Q\) by at most one, so it stays a subsequence of \(Q^k\). This contradicts maximality. Conversely, at saturation, an extending insertion is common if and only if its descent-count increment is zero in *both* orders. (Any proper common supersequence admits a chain of one-letter insertions, so testing single insertions suffices.)

**2. Exact no-insertion transition graph.** Regard both orders as chains differing solely by the adjacent transposition of \(x,y\). At the left endpoint, an insertion has zero cost in both orders precisely when a letter lies below the first letter in both; hence an MCS begins at a minimal element of their common-order intersection. Dually, it ends at a maximal element.

For two consecutive different letters \(a,b\) of a saturated MCS, an insertion of \(t\) has zero cost in an order if either (i) \(a\prec b\) and \(a\prec t\prec b\), or (ii) \(a\succ b\) and \(t\succ a\) or \(t\prec b\). A repeated-letter pair always has a zero-cost insertion in both orders (take a different letter), so repeats are excluded. For a pair increasing in both orders, an insertion works in both exactly when the pair is not a cover in the intersection order (the two chains have only one adjacent incomparable pair). For the incomparable pair \(x,y\), insertion is impossible because that pair is adjacent in both linear orders. A pair decreasing in both orders permits no insertion exactly when its source is maximal and its target minimal in the common-order intersection. This last assertion follows directly from (ii): any letter above the source or below the target in the common-order intersection gives a joint insertion; with one adjacent swap there is no mixed inequality exception for a pair comparable in both orders.

The resulting allowed edges, including initial and final conditions, are precisely paths traversing the fixed chain \(A\), then a nonempty alternating sequence of the incomparable letters \(x,y\), then the fixed chain \(B\), possibly followed by a reset edge from a maximal element to a minimal element and repetition. This yields exactly the claimed concatenations \(A s_1 B\cdots A s_r B\). When \(A=\varepsilon\) or \(B=\varepsilon\), the two incomparable letters themselves are the minimal or maximal elements, respectively; the same path description holds. As \(q\ge4\), the fixed nonempty part of \(A\) or \(B\) separates consecutive excursions, ensuring uniqueness.

**3. Budgets and lengths.** Every reset contributes one weak descent in each order, for \(r-1\) each. Each \(xy\) transition in an alternating sequence contributes a descent to \(Q\) only; each \(yx\) contributes a descent to \(P\) only. Thus budget saturation is equivalent to having exactly \(k-r\) of each transition type. The total number of transitions inside the \(s_i\) is \(2(k-r)\), giving \(\sum_i|s_i|=r+2(k-r)=2k-r\). The fixed blocks contribute \(r(q-2)\) letters, hence length \(2k+(q-3)r\). To realize any \(r\), take \(r-1\) singleton alternating blocks and one alternating block of length \(2(k-r)+1\); all budget equations hold. For \(q\ge4\) the lengths strictly increase with \(r\). At \(r=k\) all alternating blocks are singletons, independently chosen in two ways, giving \(2^k\) longest words and length \((q-1)k\).

**4. Exact enumerator.** With variables \(u,v\) marking transitions \(xy,yx\), respectively, the generating series for a nonempty alternating block is
\[
 H(u,v)=\frac{2+u+v}{1-uv}.
\]
Therefore \(C_{k,r}=[u^{k-r}v^{k-r}]H(u,v)^r\). Expanding the numerator and the geometric denominator gives the stated finite sum.

For the total, rewrite \([u^{k-r}v^{k-r}]H^r=[u^{k-1}v^{k-1}](uv)^{r-1}H^r\), obtaining
\[
 F(u,v)=\sum_{r\ge1}(uv)^{r-1}H(u,v)^r
      =\frac{2+u+v}{1-uv(3+u+v)}.
\]
The diagonal is
\[
 \sum_{n\ge0}[u^nv^n]F(u,v)z^n
  =\frac{1}{z}\left(\frac1{\sqrt{1-4z}}-1\right).
\]
For an explicit formal-residue derivation, substitute \(u=z/t,v=t\), and take the constant term in \(t\). The integrand \(F(z/t,t)/t\) has residues \(-1/z\) at \(t=0\) and \(1/(z\sqrt{1-4z})\) at the root of \(t(1-3z)-z^2-zt^2=0\) that is a power series of order two in \(z\). The other root has negative \(z\)-valuation and does not enter the formal small-contour expansion. The discriminant is \((1-z)^2(1-4z)\). Extracting the coefficient of \(z^{k-1}\) gives \(\binom{2k}{k}\).

## Verification

The accompanying dependency-free `verify.py` constructs every common subsequence for 46 exact pairs of periods, compares the maximal elements by exhaustive single-symbol extension with the stated structural language, and checks their lengths and multiplicities. It examined 170625 common words and 494 maximal words. It also checked the greedy embedding equivalence independently on 106600 finite candidate words and verified the symbolic sum for \(1\le k\le25\). Run `python3 verify.py`; the expected output begins with `VERIFY_OK`. The proof above, not finite testing, establishes the universal quantifiers.

## Relationship to prior work

Sakai (2018) and Hirota–Sakai (2023) give algorithms and characterizations for maximal common subsequences of general string pairs. Conte and collaborators (2023) build a compact DAG for MCS enumeration. Those general tools can enumerate particular cases but the inspected primary text did not give the present adjacent-swap powers classification, unbounded maximality gap, or full symbolic length enumerator. A previously established ternary swapped-power case has \(\binom{2k}{k}\) longest maximal words; the present result shows why the same total persists for larger alphabets even though shorter maximal words appear, and provides the finer distribution. Related reversed-permutation-power and disjoint-block conjugate-power families have different input relations and cannot imply this classification.

## Limitations

Only a single *adjacent* transposition of a distinct-letter permutation is covered. This does not classify general permutation pairs, nonuniform multiplicities, or strings outside this family. The generating-function equality also has conventional formal-power-series interpretations; no analytic convergence assertion is required. Mathematical novelty is assessed against inspected sources and accessible prior statements, not certified universally; unindexed equivalent work remains possible. No independent mathematical audit has been performed.

## References

- K. Sakai, *Maximal Common Subsequence Algorithms*, 29th Annual Symposium on Combinatorial Pattern Matching (CPM 2018), LIPIcs 105, Article 1 (2018), DOI: 10.4230/LIPIcs.CPM.2018.1, https://doi.org/10.4230/LIPIcs.CPM.2018.1.
- R. Hirota and K. Sakai, *A Fast Algorithm for Enumerating Maximal Common Subsequences*, arXiv:2307.10552 (2023), https://arxiv.org/abs/2307.10552.
- A. Conte et al., *A Compact DAG for Storing and Searching Maximal Common Subsequences*, arXiv:2307.13695 (2023), https://arxiv.org/abs/2307.13695.
