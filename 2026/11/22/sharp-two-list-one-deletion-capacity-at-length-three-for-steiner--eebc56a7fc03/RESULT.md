# Sharp two-list one-deletion capacity at length three for Steiner-admissible alphabets

## Finding

Let \(X\) be an alphabet of size \(q\ge2\). For any word \(w=(w_1,w_2,w_3)\in X^3\), define its **distinct single-deletion shadow** by
\[
D(w)=\{(w_1,w_2),(w_1,w_3),(w_2,w_3)\}.
\]
A code \(C\subseteq X^3\) is **two-list one-deletion decodable** when
\[
\bigl|\{w\in C:y\in D(w)\}\bigr|\le2\quad\text{for every }y\in X^2.
\]
Denote the maximum cardinality by \(M_2(q,3,1)\). Then, for all \(q\ge2\),
\[
M_2(q,3,1)\le q+\left\lfloor\frac{2q^2}{3}\right\rfloor.
\]
**Theorem.** For every \(q\ge3\) satisfying \(q\equiv1,3\pmod6\), this upper bound is attained. Consequently,
\[
\boxed{M_2(q,3,1)=q+\left\lfloor\frac{2q^2}{3}\right\rfloor\qquad(q\ge3,\ q\equiv1,3\pmod6).}
\]

## Assumptions and scope

Exactly one position is deleted adversarially. Different deletion positions producing the same received word contribute only one distinct output to \(D(w)\). The receiver must have no more than two possible source codewords for each received word. The codewords are distinct and need not be linear. The alphabet labels are arbitrary; the numerical labels in the finite certificates are merely names. The formula is not asserted to be sharp at other alphabet sizes.

## Proof

**1. Universal upper bound.** Classify selected codewords according to their shadow cardinality. Let \(c,d,e\) count those with exactly \(1,2,3\) distinct received words, respectively; hence \(|C|=c+d+e\). The only one-output words are the \(q\) constant words, so \(c\le q\). Every two-output word is of the form \(aab,baa,abb\), or \(bba\), with \(a\ne b\), and its shadow contains a diagonal word \(aa\) or \(bb\). Every constant word also contributes one diagonal word. Since there are \(q\) diagonal received words and each can be covered at most twice, \(c+d\le2q\). The total number of codeword/received-word incidences is
\[
I=c+2d+3e=3|C|-2c-d\le2q^2.
\]
It follows that
\[
3|C|\le2q^2+2c+d\le2q^2+2q+c\le2q^2+3q.
\]
Taking the integer part gives \(|C|\le q+\lfloor2q^2/3\rfloor\).

**2. A design-to-code transformation.** Suppose a Steiner triple system \((X,\mathcal B)\) exists: each unordered pair of different symbols lies in exactly one block \(B\in\mathcal B\) of size three. Suppose further that \(\mathcal P\subseteq\mathcal B\) consists of \(m\) pairwise disjoint blocks.

For each block, choose an ordering \(a<b<c\) (using any total order on the alphabet), and select the four distinct words
\[
abc,\qquad cba,\qquad acb,\qquad bca.
\]
Here a juxtaposition means concatenation, not multiplication. The first two words form a reversal pair; so do the last two. Each reversal pair covers each of the six ordered **off-diagonal** received pairs on \(\{a,b,c\}\) exactly once. Since every unordered symbol pair belongs to a unique Steiner block, these four-word selections cover every ordered off-diagonal received word precisely twice. Add the \(q\) constant codewords \(aaa\). Each diagonal received pair is then covered once.

For each block \(\{a,b,c\}\in\mathcal P\), delete the selected word \(abc\) and insert exactly the three distinct words
\[
aab,\qquad bbc,\qquad acc.
\]
Their deletion shadows are respectively \(\{aa,ab\}\), \(\{bb,bc\}\), and \(\{ac,cc\}\); hence they replace precisely the three off-diagonal pairs \(ab,bc,ac\) formerly covered by \(abc\), leaving every off-diagonal multiplicity unchanged. They add one extra diagonal incidence for each of \(a,b,c\). Since the blocks in \(\mathcal P\) are disjoint, no diagonal receives more than one extra incidence. All codewords remain different, since old words have three distinct symbols, inserted words have two, constant words have one, and each inserted word belongs to its unique original Steiner block. Thus the resulting code is two-list decodable, and it has
\[
|C|=q+4\cdot\frac{q(q-1)}6-m+3m
=q+\frac{2q(q-1)}3+2m.
\]

**3. Existence for the claimed congruence classes.** When \(q\equiv3\pmod6\), the classical Kirkman triple-system existence theorem supplies a resolvable Steiner triple system, hence a parallel class of \(m=q/3\) disjoint blocks. The construction gives \(q+2q^2/3\), equal to the universal bound.

When \(q\equiv1\pmod6\) and \(q\ge13\), established factor-critical Steiner triple-system existence supplies a Steiner system with an almost parallel class, that is, \(m=(q-1)/3\) disjoint blocks covering all but one point. The existence is documented in Bryant, Davies and Neubecker (2026), which also credits earlier results. In this case the code size is
\[
q+\frac{2q(q-1)}3+\frac{2(q-1)}3
=q+\frac{2(q^2-1)}3
=q+\left\lfloor\frac{2q^2}{3}\right\rfloor.
\]

The remaining case \(q=7\) has no disjoint matching of two triples in its Fano Steiner system, so this replacement construction is not invoked. The following explicit set of 39 length-three words attains the bound (digits denote the seven alphabet symbols):

```text
000 001 022 036 042 054 063 111 120 134 136 144 150
165 222 231 246 251 254 260 305 311 332 333 352 401
423 444 453 461 530 551 555 562 566 612 640 645 666
```

The standalone checker counts every one of its 49 possible received words and confirms its inverse list never exceeds two. The bound gives \(7+\lfloor98/3\rfloor=39\), completing the proof.

## Verification

The supplied `CHECK.py` generates the designs and codewords for \(q=3,9,13\), independently checks every unordered-pair incidence and every specified matching, and verifies the explicit \(q=7\) code. It enumerates every length-three source word to check the shadow-type lemma for \(2\le q\le9\). Its recorded output is `CHECK_OUTPUT.txt`. These are finite spot checks for the general construction; the all-parameter result follows from the proof above and the cited design-existence theorems, not from the finite computations.

## Relationship to prior work

Lin (2026) and Kiah, Wei and Zeng (2026) develop asymptotic insertion/deletion list-decoding bounds, mainly in a different block-length regime; the exact length-three nonbinary list-two capacity is a separate question. Chee, Ge and Ling (2010) classify *perfect uniquely deletion-correcting* codes of length three, whose shadows are disjoint rather than allowed multiplicity two. Their directed-packing theory motivates the underlying combinatorial language but does not state the formula above. The Kirkman existence theorem and factor-critical Steiner systems supply the designs; the four-permutation encoding and one-block-to-three-word replacement are the additional coding argument. Nearby studies of one-deletion **covering** and adjacent-burst codes do not imply a maximum under a two-list packing constraint.

## Limitations

The value of \(M_2(q,3,1)\) for even alphabet sizes and for \(q\equiv5\pmod6\) is not determined here, although the universal upper bound applies. No conclusion is drawn for codeword lengths other than three, larger deletion budgets, or different list sizes. The existence portion depends on established design-existence theorems; the supplied checker is not a standalone proof of those infinite existence results. An unindexed equivalent coding formulation could affect priority. No independent audit has been performed.

## References

1. A. D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650v1, first public 2026-09-22, https://arxiv.org/abs/2609.26650.
2. D. Bryant, S. Davies, J. Neubecker, *Partial Steiner Triple Systems With an Almost Parallel Class Missing Any Given Point*, *Journal of Combinatorial Designs*, first published 2026-09-27, https://doi.org/10.1002/jcd.70038. See the introduction and Section 3 for existence of factor-critical Steiner triple systems at orders congruent to one modulo six, at least 13.
3. Y. M. Chee, G. Ge, A. C. H. Ling, *Spectrum of Sizes for Perfect Deletion-Correcting Codes*, *SIAM Journal on Discrete Mathematics* 24 (2010), 33–55, https://arxiv.org/abs/1008.1343.
4. S. A. Vanstone et al., *Hanani triple systems*, *Israel Journal of Mathematics* 83 (1993), 305–319, https://doi.org/10.1007/BF02784058.
5. S. Bonvicini et al., *The first families of highly symmetric Kirkman triple systems whose orders fill a congruence class*, *Designs, Codes and Cryptography* (2021), https://doi.org/10.1007/s10623-021-00952-x; background on the classical Kirkman existence theorem.
