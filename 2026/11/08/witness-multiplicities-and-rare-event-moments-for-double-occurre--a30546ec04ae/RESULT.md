# Witness multiplicities and rare-event moments for double-occurrence shuffle squares

## Finding

Fix an alphabet of \(q\geq1\) distinct letters. Let \(\mathcal{D}_q\) be the words of length \(2q\) in which every letter occurs exactly twice. A *shuffle-square witness* of \(w\in\mathcal{D}_q\) is an **unordered** bipartition of its positions into two \(q\)-element sets inducing the same subsequence. Let \(m(w)\) be the number of witnesses, allowing \(m(w)=0\).

If the first and second occurrence orders of the letters differ, then \(m(w)=0\). Otherwise the word determines a Dyck path \(P_w\): write an up-step at each first occurrence and a down-step at each second occurrence. Let \(r(w)\) be the number of nonempty primitive Dyck excursions (equivalently, the number of returns of this path to height zero). Then

\[
m(w)=2^{r(w)-1}.
\]

Consequently **the complete, exact multiplicity distribution** is, for \(1\le r\le q\),

\[
\#\{w\in\mathcal{D}_q:m(w)=2^{r-1}\}
=q!\,\frac{r}{2q-r}\binom{2q-r}{q}.
\]

No other positive multiplicities occur. In particular exactly \(q!C_{q-1}\) words have a unique witness, where \(C_j=\frac1{j+1}\binom{2j}{j}\), and exactly \(q!C_q\) words are shuffle squares (the latter count is already known).

For a uniformly random shuffle-square word from \(\mathcal{D}_q\), let \(M_q=m(w)\). For each nonnegative integer \(s\),

\[
\mathbb E[M_q^s]=\frac{[z^q]\bigl(1-2^s z C(z)\bigr)^{-1}}{2^s C_q},
\qquad C(z)=\frac{1-\sqrt{1-4z}}{2z}.
\]

In particular,

\[
\mathbb E[M_q]=\frac{q+1}{2},\qquad
\mathbb E[M_q^2]\sim\frac{\sqrt\pi}{6}\,q^{3/2}\left(\frac43\right)^q.
\]

For every fixed \(r\geq1\),

\[
\lim_{q\to\infty}\Pr\bigl(M_q=2^{r-1}\bigr)=\frac{r}{2^{r+1}}.
\]

Thus the witness count remains bounded in probability even though its expectation grows linearly and its second moment grows exponentially.

## Assumptions and scope

The letter alphabet has precisely \(q\) distinguishable symbols, each of multiplicity exactly two; the positions are linearly ordered, not cyclic. Distinct words mean distinct labeled strings. A witness is an unordered partition of **positions**, not just the underlying repeated subsequence. The empty word is excluded, and \(q=1\) is included. Probability is uniform over qualifying words, not over all \(\mathcal{D}_q\).

## Proof

**1. Occurrence-order criterion.** In a witness each letter must contribute one of its occurrences to each subsequence. For two distinct letters \(a,b\), both subwords must order \(a,b\) consistently. The nested restriction \(abba\) or \(baab\) makes this impossible: regardless of how the two copies are assigned, one subword reads \(ab\) and the other \(ba\). Thus the order of first occurrences must agree with the order of second occurrences. Conversely, if these two orders agree, assign the first occurrence of each letter to one subword and the second to the other. Both then read the common occurrence-order permutation. This gives the criterion. It is the known nonnesting characterization, not a newly claimed existence result.

**2. Every witness and the crossing graph.** Suppose the orders agree. For each letter choose the color assigned to its first occurrence; its second occurrence must receive the other color. For two distinct letters, their occurrence intervals are either disjoint or interlaced: nesting is excluded by Step 1. If interlaced, say \(a_1<b_1<a_2<b_2\), both subwords have the same order only when the first occurrences of \(a,b\) have the same color. When disjoint, their relative order is identical for any assignment. Form the simple crossing graph on the \(q\) letters, with an edge for each interlaced pair. The valid assignments are therefore exactly colorings constant on each connected component. If the graph has \(r\) components, there are \(2^r\) ordered colorings and \(2^{r-1}\) unordered witnesses, because global interchange of colors has no fixed assignment.

**3. Graph components are primitive Dyck excursions.** Each prefix of a word has at least as many first as second occurrences, so the first/second occurrence encoding is a Dyck path. When the two occurrence orders agree, the closing events obey first-in-first-out order. No two intervals cross between distinct excursions, so distinct excursions lie in distinct graph components. Inside a primitive excursion, each newly opened interval after the first begins while a previous interval remains open. Its closure follows the closure of that earlier interval, by first-in-first-out order, hence it crosses that earlier interval. Each new vertex therefore links to a previously opened vertex in the same excursion. Induction proves that its crossing graph is connected. Thus \(r=r(w)\) and Step 2 proves the multiplicity formula.

**4. Enumeration.** For every permutation \(\pi\) of the \(q\) symbols and every Dyck path of semilength \(q\), label its successive up-steps by \(\pi_1,\ldots,\pi_q\), and label its successive down-steps by the same sequence. This is a bijection with qualifying labeled words. Write \(P(z)=zC(z)=(1-\sqrt{1-4z})/2\), the generating function for primitive Dyck excursions. Exactly \(r\) excursions are counted by \([z^q]P(z)^r\). By Lagrange inversion, or the standard Catalan power formula,

\[
[z^q]P(z)^r=[z^{q-r}]C(z)^r
=\frac{r}{2q-r}\binom{2q-r}{q}
\quad(1\le r\le q).
\]

Multiplying by \(q!\) gives the distribution. For \(r=1\), \([z^q]P(z)=C_{q-1}\); summing all \(r\) gives \([z^q](1-P(z))^{-1}=C_q\).

**5. Moments and tails.** Since \(m=2^{r-1}\), weighting each excursion by \(2^s\) gives, for positive \(q\),

\[
\mathbb E[M_q^s]=\frac{2^{-s}}{C_q}[z^q]\sum_{r\geq0}(2^s P(z))^r,
\]

which is the claimed expression. At \(s=1\), \((1-2P(z))^{-1}=(1-4z)^{-1/2}\), hence \(\mathbb E[M_q]=\binom{2q}{q}/(2C_q)=(q+1)/2\).

At \(s=2\), \((1-4P(z))^{-1}=(2\sqrt{1-4z}-1)^{-1}\). Its unique dominant positive pole is at \(\rho=3/16\). Near that pole the denominator equals \((3/2)(1-z/\rho)+O((1-z/\rho)^2)\), and no competing singularity has this modulus, since \(P\) has strictly positive coefficients at all positive degrees. Therefore its \(z^q\) coefficient is asymptotic to \((2/3)(16/3)^q\). Dividing by \(4C_q\) and using \(C_q\sim 4^q/(\sqrt\pi q^{3/2})\) yields the second-moment asymptotic.

For fixed \(r\), the square-root expansion \(P(z)^r=2^{-r}(1-r\sqrt{1-4z}+O(1-4z))\) gives \([z^q]P(z)^r/C_q\to r/2^{r+1}\). This limiting distribution has total mass one, since \(\sum_{r\ge1}r/2^{r+1}=1\); therefore \(M_q\) is tight. The finite mean nevertheless diverges as above.

## Verification

Run `python3 verify_shuffle.py` using standard Python 3. The verifier independently enumerates all \(116017\) labeled candidate words for \(1\le q\le5\), tests all unordered witness partitions, checks the Dyck-excursion statistic, and compares the exact multiplicity histogram with the formula. It finds \(5411\) qualifying words in total. It also verifies \(64\) exact generating-function coefficient identities for \(1\le q\le32\). The enumeration checks finite instances only; Steps 1–5 supply the infinite proof.

## Relationship to prior work

Grytczuk–Pawlik–Pleszczyński, *Variations on shuffle squares* (first public arXiv version 2023-08-26), Proposition 3, proves the absence-of-nesting characterization and the Catalan **number of qualifying words**. The present finding does not claim either as new: it refines each qualifying word by its total number of distinct position-partition witnesses and determines the entire multiplicity distribution and its moments. He–Huang–Nam–Thaper, *Shuffle Squares and Reverse Shuffle Squares* (arXiv 2021), Section 5, relates ordinary shuffle squares to nonnesting perfect matchings and counts large-alphabet words, but its matching-count formulas do not state the witness-multiplicity law for labeled double-occurrence words. Grytczuk–Pawlik–Ruciński, *Shuffle squares and ordered nest-free graphs* (arXiv 2025), gives a graph representation of canonical twins and binary structural results, rather than the refined Catalan witness statistics above. Henshall–Rampersad–Shallit (2011) provides the original shuffle-language framework.

## Limitations

The law is specific to words with **exactly** two copies of each distinct letter; repeated letters of higher multiplicity do not inherit the same simple crossing-graph count. The distribution is for linearly ordered labeled words and unordered witnesses. The known existence criterion and Catalan unrefined census are not new contributions. Although no equivalent refined multiplicity theorem was located in the inspected primary material or searches, an unindexed formulation using nonnesting matchings or Dyck-return statistics is a residual bibliographic risk. The asymptotic statements are for \(q\to\infty\) and do not give a uniform tail approximation in \(r\).

## References

- X. He, E. Huang, I. Nam, R. Thaper, *Shuffle Squares and Reverse Shuffle Squares*, first arXiv public version 2021-09-25, https://arxiv.org/abs/2109.12455 .
- J. Grytczuk, B. Pawlik, M. Pleszczyński, *Variations on shuffle squares*, arXiv version 1, 2023-08-26, https://arxiv.org/abs/2308.13882 .
- J. Grytczuk, B. Pawlik, A. Ruciński, *Shuffle squares and ordered nest-free graphs*, arXiv version 1, 2025-03-27, https://arxiv.org/abs/2503.22043 .
- D. Henshall, N. Rampersad, J. Shallit, *Shuffling and Unshuffling*, arXiv preprint 2011-06-28, https://arxiv.org/abs/1106.5767 .
