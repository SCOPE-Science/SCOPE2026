# The high-multiplicity inverse family for cross-number-one zero sums in twice-prime cyclic groups

## Finding

Let \(p\geq3\) be an odd prime and \(G=C_{2p}=\mathbb Z/(2p)\mathbb Z\). A sequence is an unordered multiset of elements of \(G\). Call it *cross-one-free* if no nonempty subsequence has both sum zero in \(G\) and cross number exactly \(1\), where the cross number of a subsequence \(U\) is \(\operatorname{k}(U)=\sum_{x\in U}1/\operatorname{ord}(x)\).

**Theorem (dominant-generator inverse classification).** Among all cross-one-free sequences \(S\) of sharp length \(3p-2\) that have a term of multiplicity at least \(2p-1\), there are exactly
\[
(p-1)^2(p-2)
\]
*distinct unordered sequences*. Precisely \(2(p-1)(p-2)\) of them have support of cardinality two, and \((p-1)(p-2)(p-3)\) have support of cardinality three. None has larger support.

The complete family is as follows. Choose a generator \(g\in G\), a nonzero residue \(h\in\mathbb Z/p\mathbb Z\), and a multiset \(R\) of length \(p-1\) whose elements are drawn from
\[
E_{g,h}=\{(2h+1)g,\ (2h+2)g\}\setminus\{0,pg\},
\]
where coefficients are reduced modulo \(2p\) and \(h\) is represented by an integer between \(1\) and \(p-1\). Then, and only then, the corresponding sequence has the form
\[
 S=\underbrace{g\cdot\ldots\cdot g}_{2p-1\text{ copies}}\cdot R.
\]
Distinct choices of \((g,h,R)\) produce distinct sequences, except that the choice of a multiset on a one-element \(E_{g,h}\) is of course unique. Every sequence displayed is cross-one-free. Its length is one below the general sharp threshold \(\mathsf T(C_{2p})=3p-1\) proved by Gao and Mu.

## Assumptions and scope

The prime \(p\) is odd; no size cutoff is imposed. Distinct sequences mean distinct multisets on the *fixed labelled additive group* \(\mathbb Z/(2p)\mathbb Z\), not automorphism orbits. A generator means an element of additive order \(2p\). The dominant-multiplicity hypothesis is essential to the stated classification: it is **not** asserted that every extremal sequence of length \(3p-2\) has such a term. The threshold itself and the basic two-symbol witness are prior results, not contributions of this theorem.

For any \(x\in G\), let \(d(x)=\gcd(\widetilde x,2p)\), using any integer representative \(\widetilde x\). Then \(\operatorname{ord}(x)=2p/d(x)\). A subsequence has cross number one exactly when the sum of its \(d(x)\)-weights equals \(2p\).

## Proof

**Step 1: dominant terms are forced generators.** Let \(S\) be as in the theorem and let \(g\) occur at least \(2p-1\) times. If \(g\) had additive order \(d<2p\), then the \(d\) copies of \(g\) form a zero-sum subsequence with cross number \(1\). Hence \(g\) has order \(2p\). Similarly \(2p\) copies of \(g\) would be forbidden. It follows that \(g\) occurs exactly \(2p-1\) times, so \(S=g^{[2p-1]}R\) with \(|R|=p-1\). The notation \(g^{[m]}\) indicates \(m\) copies, not exponentiation in the group.

A zero element cannot occur in \(R\): it has cross number one by itself. Nor can \(pg\) occur: it has order two, and \(pg\) together with \(p\) copies of \(g\) has sum zero and total cross number \(1\). All elements of \(R\) therefore have \(d(x)=1\) (odd normalized residue) or \(d(x)=2\) (nonzero even normalized residue).

**Step 2: exact reduction to a prime-order zero-sum-free problem.** Apply the group automorphism multiplying each term by \(g^{-1}\), the inverse of the unit representing \(g\) modulo \(2p\). This makes the dominant generator equal to \(1\). For a residual term \(x\), normalized in \(\mathbb Z/(2p)\mathbb Z\), put
\[
 a(x)=\frac{\widetilde x-d(x)}2\pmod p.
\]
The quotient is an integer because \(\widetilde x\) and \(d(x)\) have the same parity. For each nonempty residual submultiset \(U\), its total \(d\)-weight \(D(U)\) satisfies \(1\leq D(U)\leq2p-2\). Consequently a subsequence consisting of \(U\) together with \(t\) dominant copies has cross number one if and only if \(t=2p-D(U)\); this integer lies between \(2\) and \(2p-1\) and hence the dominant supply suffices. Its group sum is then
\[
\sum_{x\in U}\widetilde x+(2p-D(U))
\equiv2\sum_{x\in U}a(x)\pmod{2p}.
\]
Thus **a cross-one zero sum exists in \(S\) if and only if** the length-\(p-1\) sequence \((a(x))_{x\in R}\) contains a nonempty zero-sum subsequence modulo \(p\). Conversely, every cross-one subsequence must involve at least one residual term, because at most \(2p-1\) dominant copies are present. This proves both directions of the reduction.

**Step 3: prime-order inverse lemma.** A zero-sum-free sequence of length \(p-1\) in \(C_p\) consists of \(p-1\) copies of a single nonzero element. To see this, no term is zero. Suppose two terms \(a,b\) are distinct. If \(a+b=0\), the sequence is not zero-sum-free. Otherwise their four subset sums \(\{0,a,b,a+b\}\) are distinct. For each additional nonzero term \(c\), the set of subset sums becomes \(A\cup(A+c)\). If \(A\ne C_p\), then \(A+c\ne A\), because nonzero translation generates the prime-order cyclic group, and hence its cardinality increases by at least one. Starting from four subset sums and adding the remaining \(p-3\) terms therefore gives at least \(p+1\) subset sums, impossible in \(C_p\). Hence all terms coincide, and the common value is nonzero. The converse is immediate because no sum of between \(1\) and \(p-1\) copies of a nonzero residue is zero.

**Step 4: invert the two-to-one residue map.** If \(a(x)=h\ne0\), then \(\widetilde x\equiv d(x)+2h\pmod{2p}\). The only possibilities are \(2h+1\), odd, and \(2h+2\), even. The odd candidate is inadmissible exactly when it equals \(p\), namely \(h=(p-1)/2\). The even candidate is inadmissible exactly when it equals \(0\), namely \(h=p-1\). These are two distinct nonzero values of \(h\) for each odd prime \(p\). For each of the other \(p-3\) values, both candidates are allowed. Restoring the generator \(g\) gives exactly \(E_{g,h}\) in the statement. Steps 2 and 3 establish the if-and-only-if classification.

**Step 5: count the sequences without overcounting.** There are \(\varphi(2p)=p-1\) choices for \(g\). For fixed \(g\), each of the two exceptional \(h\)-values permits exactly one residual multiset. Each of the \(p-3\) other values permits exactly \(p\) residual multisets, corresponding to the \(p\) possible multiplicity splits of \(p-1\) terms between two distinct choices. The count for each \(g\) is therefore \(2+p(p-3)=(p-1)(p-2)\). No two choices \(h\) can share a residual multiset because the residue map \(a(x)\) is unambiguous; and no two generators can share a final sequence because \(2(2p-1)>3p-2\). Multiplying gives \((p-1)^2(p-2)\).

For every \(g\), two exceptional \(h\)-values supply one two-supported sequence each. A nonexceptional \(h\) supplies two two-supported sequences (all residual copies on one residue) and \(p-2\) three-supported sequences (both residue types used). Thus the support-two total is \((p-1)(2+2(p-3))=2(p-1)(p-2)\), and the support-three total is \((p-1)(p-3)(p-2)\). This completes the proof.

## Verification

The accompanying standard-library script `check.py` computes the predicted multisets and independently tests the exact cross-number-one condition by dynamic programming in the pair (accumulated \(d\)-weight, group sum). For \(p=3,5,7\), it also enumerates **all** unordered sequences of the sharp length, without imposing the dominant-term condition, and verifies that the surviving sets coincide with the formula. This is a finite observation only, not a proof of a global dominance property.

| \(p\) | Predicted sequences | Two-supported | Three-supported | Exhaustive all-sequence check |
|---:|---:|---:|---:|---|
| 3 | 4 | 4 | 0 | equal to predicted set |
| 5 | 48 | 24 | 24 | equal to predicted set |
| 7 | 180 | 60 | 120 | equal to predicted set |
| 11 | 900 | 180 | 720 | not attempted |
| 13 | 1,584 | 264 | 1,320 | not attempted |

Every generated sequence at all five tested primes is checked for the absence of a cross-number-one zero sum. To reproduce, run `python3 check.py` in the directory containing this manuscript.

## Relationship to prior work

Gao, Hui, Jiang, Li and Wang introduced and investigated the threshold \(\mathsf T(G)\) and supplied the standard extremal sequence in even cyclic groups (their Lemma 3.1). Gao and Mu determined the sharp threshold \(\mathsf T(C_n)\) for every cyclic group, and again give that witness. Their results establish the extremal **length**, while the present theorem classifies and counts a natural, structurally defined family of extremal **sequences** at all twice-odd-prime orders; it does not claim the earlier threshold or witness as new.

Savchev and Chen study long sequences without an ordinary length-\(n\) zero sum. Their structural range is strictly above \(3n/2-1\) and the absence criterion differs when terms of nonmaximal order occur; hence their published characterization does not directly subsume the weighted cross-number-one classification at length \(3p-2\) for \(n=2p\). The prime-order zero-sum-free lemma used above is classical and is not claimed as new.

## Limitations

Only the dominant-multiplicity subfamily is classified for arbitrary \(p\). A full inverse theorem for *all* sharp-length cross-one-free sequences is not proved here, notwithstanding complete small-prime enumerations. Standard full-group automorphism equivalence is not used in the count. The computational checks cover only the stated primes and cannot establish the universal theorem independently of its proof. A literature search and inspection of the most relevant accessible results found no explicit pre-existing version of this formula, but undocumented implicit prior coverage remains possible.

## References

1. W. D. Gao, W. Z. Hui, X. Jiang, Y. L. Li, X. Y. Wang, "On zero-sum subsequences of cross number 1," *Acta Arithmetica* **219** (2025), 347–363, DOI: https://doi.org/10.4064/aa240825-15-11 . Public full text: https://cam.tju.edu.cn/research/downAchiev.php?id=898 (published online 6 June 2025).
2. W. D. Gao, Y. Mu, "Zero-sum subsequences of cross number 1 over cyclic groups," arXiv:2611.23852v1 (18 November 2026), https://arxiv.org/abs/2611.23852 .
3. S. Savchev, F. Chen, "Long \(n\)-zero-free sequences in finite cyclic groups," arXiv:math/0604356 (16 April 2006), https://arxiv.org/abs/math/0604356 .
4. S. Savchev, F. Chen, "Long zero-free sequences in finite cyclic groups," arXiv:math/0602568 (25 February 2006), https://arxiv.org/abs/math/0602568 .
