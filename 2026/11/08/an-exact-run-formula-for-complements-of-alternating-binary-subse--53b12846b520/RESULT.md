# An exact run formula for complements of alternating binary subsequences

## Finding

For nonnegative integers \(k,r\), put \(W=(01)^{k+r}\) and \(U=(01)^k\). Let \(C(W,U)\) be the set of **distinct** words obtained by deleting the positions of any scattered-subsequence embedding of \(U\) in \(W\) (the empty word is allowed). Denote the two length-two blocks by \(A=01\) and \(B=10\). For a word \(x\in\{A,B\}^{r}\), let \(b(x)\) be the number of maximal nonempty consecutive runs of \(B\) among its \(r\) blocks.

**Theorem.** For all integers \(k,r\geq0\),
\[
C((01)^{k+r},(01)^k)=\{x_1\cdots x_r:x_i\in\{01,10\},\ b(x_1\cdots x_r)\leq k\}.
\]
Consequently,
\[
\boxed{\left|C((01)^{k+r},(01)^k)\right|=\sum_{j=0}^{\min(k,\lfloor(r+1)/2\rfloor)}\binom{r+1}{2j}.}
\]
Exactly \(\binom{r+1}{2j}\) distinct remainders have minimum alternating-deletion budget \(j\). All \(2^r\) possible paired words occur if and only if \(r\leq2k\) (including \(r=k=0\)). For \(r>2k\), at least one paired word is absent.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), with distinct symbols. A scattered embedding of \(U\) in \(W\) consists of strictly increasing indices matching \(U\); the complement word consists of the unselected positions of \(W\) in their original order. Distinct embeddings giving the same complement are counted only once. We allow \(k=0\) or \(r=0\), so that the empty pattern and empty remainder are handled consistently. The theorem applies uniformly to all values of both parameters, not merely to a finite census.

## Proof

Write \(\Delta(z)=|z|_0-|z|_1\) for the zero-minus-one balance of a binary word. Every prefix of \(W\) has balance in \(\{0,1\}\), and every prefix of \(U\) has balance in \(\{0,1\}\). Consider any deletion embedding and any prefix \(W'\) of \(W\). The letters assigned to \(U\) and those assigned to its complement form respective prefixes \(U'\) and \(V'\), and satisfy
\[
\Delta(V')=\Delta(W')-\Delta(U')\in\{-1,0,1\}.
\]
At the end, \(\Delta(V)=0\), and \(V\) has \(r\) zeros and \(r\) ones. Starting at balance zero, any pair of consecutive symbols of \(V\) must return the balance to zero: at an even position the balance is zero and at an odd position it is either \(1\) or \(-1\), because stepping from \(\pm1\) further in the same direction would violate the bound. Thus \(V\) decomposes uniquely into \(r\) blocks each equal to \(A=01\) or \(B=10\).

When the complement prefix is halfway through a \(B\) block, its balance is \(-1\); the displayed balance equality forces \(\Delta(U')=1\), so the embedding is midway through an open \(01\) pair of \(U\). When the complement prefix is halfway through an \(A\) block, its balance is \(+1\); the same equality forces \(\Delta(U')=0\). Every maximal \(B\)-run therefore needs at least one distinct \(0\) of \(U\) to open before its first negative-balance prefix, and a subsequent distinct \(1\) to close before the next \(A\)-run or the end of the word. Different \(B\)-runs cannot share such an open pair, because an intervening \(A\) block forces the embedding balance back to zero. Thus \(b(V)\leq k\). This proves necessity, including the cases where the word begins or ends with a \(B\)-run.

For sufficiency, take any concatenation \(V=x_1\cdots x_r\) of \(A\) and \(B\) blocks with \(j=b(V)\leq k\). For each maximal \(B\)-run of length \(\ell\), insert a \(0\) immediately before the run and a \(1\) immediately after it, declaring these inserted symbols part of \(U\). The resulting segment is
\[
0(10)^\ell1=(01)^{\ell+1}.
\]
All untouched \(A\)-runs are already powers of \(01\); concatenating the transformed segments therefore produces exactly \((01)^{r+j}\). The inserted symbols, read in order, are \((01)^j\). Insert another \(k-j\) complete \(01\) pairs at the end, assigned to \(U\). The final word is \((01)^{r+k}=W\), the assigned subsequence is \((01)^k=U\), and the unassigned letters read \(V\). Hence \(V\in C(W,U)\) and the structural identity holds.

A block word of length \(r\) with \(j\) maximal \(B\)-runs is uniquely specified by choosing its \(2j\) transition boundaries among the \(r+1\) gaps before, between and after the blocks. Conversely, any \(2j\) chosen ordered boundaries delimit \(j\) nonempty, mutually separated \(B\) intervals. Therefore precisely \(\binom{r+1}{2j}\) words have \(j\) \(B\)-runs; summing up to \(k\) proves the formula. Finally the largest possible number of disjoint \(B\)-runs in \(r\) blocks is \(\lfloor(r+1)/2\rfloor\), so every paired word is attainable exactly when \(k\geq\lfloor(r+1)/2\rfloor\), equivalently \(r\leq2k\). This completes the proof.

## Verification

The standalone standard-library program `verify_alt_complements.py` implements two structurally different finite checks. First, explicit position-subset enumeration computes the complete set of distinct remainders for every \(0\leq k\leq n\leq8\), compares the entire set with the run criterion, and compares cardinalities with the displayed sum (45 parameter pairs). Second, a shuffle-membership dynamic program walks both component words with independent pointers; it checks all balanced remainder candidates for \(0\leq r\leq7\) and \(0\leq k\leq4\) (23,535 candidate/parameter comparisons). Both tests passed. The symbolic proof above, not the bounded checks, establishes the unbounded quantifiers.

For example, for \(r=5\) the successive counts at \(k=1,2,3\) are \(16,31,32\). The unique remainder missing at \(k=2\) is \(1001100110=(10)(01)(10)(01)(10)\), whose three \(B\)-runs require three deleted \(01\) pairs.

## Relationship to prior work

Adamson, Fleischmann, and Huch introduced and studied complement scattered-factor sets and algorithms for computing them, using the same definition of \(C(W,U)\). Their March 2026 paper treats general algorithms, special singleton phenomena, the relationship to shuffles, and self-shuffle questions; Section 5 explicitly leaves a closed formula in particular cases open. Their algorithm can compute each individual instance of the present family, but none of the inspected statements supplies the two-parameter run criterion, binomial sum, or sharp saturation boundary.

Classical Gilbreath-style alternating-riffle results imply a *paired-letter output property* when the two shuffled input streams have suitable opposing alternating phases. This is related to, but does not establish, which of the paired remainders can be obtained by deleting exactly \(k\) alternating pairs from an already alternating host. The sharp \(B\)-run budget and corresponding cardinality formula require an additional argument.

## Limitations

This is a classification only for an alternating host and alternating deleted pattern of the same phase. It is not a universal upper bound for \(C(W,U)\) over arbitrary words, an enumeration of embedding multiplicities, or a result for other alphabets, phase reversals, or nonalternating patterns. Verification computations are finite corroboration, not an independent infinite proof. Historical priority remains subject to possible unindexed work in shuffle quotients and deletion channels; independent mathematical validation has not been performed.

## References

1. D. Adamson, P. Fleischmann, and A. Huch, "(Sets of) Complement Scattered Factors," arXiv:2603.20790v1, first publicly posted 2026-03-21. Full text: https://arxiv.org/html/2603.20790v1 ; manuscript record: https://arxiv.org/abs/2603.20790 .
2. The Gilbreath alternating-riffle property, for background comparison rather than a source of the stated enumeration: https://nuitp.webs.upv.es/examples/gilbreath.html ; see also the public mathematical exposition https://mathworld.wolfram.com/GilbreathPrinciple.html .
