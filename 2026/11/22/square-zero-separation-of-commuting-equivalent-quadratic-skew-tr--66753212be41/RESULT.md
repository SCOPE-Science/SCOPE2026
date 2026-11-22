# Square-zero separation of commuting-equivalent quadratic skew truncations

## Finding

Let \(k=\mathbb F_q\) have odd cardinality, let \(n=2m+1\ge3\), and let \(\tau\) be the nontrivial involution of either quadratic étale algebra \(E_{\mathrm s}=k\times k\) (factor swap) or \(E_{\mathrm f}=\mathbb F_{q^2}\) (Frobenius conjugation). Form \(A_\bullet=E_\bullet[t;\tau]/(t^n)\), where \(t a=\tau(a)t\).

Although the two algebras are known to have exactly the same commutation predicate under an explicit \(k\)-linear bijection [1], their square-zero loci have different cardinalities:
\[
 \#\{x\in A_{\mathrm s}:x^2=0\}
 =q^{n-1}\left(1+2\left\lfloor\frac{n+1}{4}\right\rfloor(q-1)\right),
 \qquad
 \#\{x\in A_{\mathrm f}:x^2=0\}=q^{n-1}.
\]
Thus the commutation graph, even together with the whole element-centralizer spectrum, does not determine the square-zero census; the ratio is unbounded as odd \(n\) increases for fixed odd \(q\).

The result gives a finer complete valuation census. For nonzero \(x=\sum_{i=0}^{n-1}c_it^i\), let \(\nu(x)\) be the least index with \(c_i\ne0\), and set \(\nu(0)=n\). Both loci contain the zero element once, and for \(m+1\le j<n\) both have exactly \((q^2-1)q^{2(n-j-1)}\) square-zero elements of valuation \(j\). At \(1\le j\le m\), the field-coefficient algebra has none; the split-coefficient algebra has exactly \(2(q-1)q^{n-1}\) at each odd \(j\), and none at even \(j\).

If \(n=p\) is the odd characteristic of \(k\), then \(A_{\mathrm s}\cong k[D_{2p}]\), giving the identical square-zero census for the modular dihedral group algebra of order \(2p\).

## Assumptions and scope

Throughout, \(q\) is an odd prime power and \(n\) is odd. The skew quotient is the finite associative unital algebra with the stated Ore relation; its elements have a unique length-\(n\) coefficient expansion. Square-zero means \(x^2=0\) as an algebra element, not merely that the corresponding regular linear operator is nilpotent. The already-established commutation-graph equivalence [1] is cited as a premise, not reasserted as a new contribution. The new assertions are the full square-zero valuation strata, their totals, and their separation despite commuting equivalence.

## Proof

**Radical reduction.** The ideal \((t)\) is nilpotent, with quotient the quadratic étale algebra \(E_\bullet\). Neither \(k\times k\) nor \(\mathbb F_{q^2}\) contains a nonzero square-zero element, so every square-zero element lies in \((t)\). If \(2\nu(x)\ge n\), then \(x^2=0\) automatically. There are \(q^{2(n-m-1)}=q^{n-1}\) such elements, including zero. The number of nonzero ones of valuation \(j\ge m+1\) is \((q^2-1)q^{2(n-j-1)}\).

**Field-coefficient obstruction.** In \(A_{\mathrm f}\), if \(x\ne0\) has valuation \(j\le m\), its leading square coefficient at degree \(2j\) is \(c_j\tau^j(c_j)\), nonzero because \(E_{\mathrm f}\) is a field. Thus no such element squares to zero, proving the nonsplit formula.

**Split-coefficient calculation.** Write \(E_{\mathrm s}=k[s]/(s^2-1)\), with \(\tau(s)=-s\), so \(st=-ts\). Each element of valuation \(j\) can be written uniquely as \(x=t^j(A(t)+B(t)s)\), where \(A,B\) have length \(n-j\) and at least one constant coefficient is nonzero. Write \(\sigma(F(t))=F(-t)\). Direct multiplication, with the coefficients interpreted modulo \(t^{n-2j}\), shows for \(2j<n\) that
\[
 x^2=0\quad\Longleftrightarrow\quad
 A^2+(-1)^jB\sigma(B)=0,\qquad
 B\bigl(A+(-1)^j\sigma(A)\bigr)=0
 \pmod{t^{n-2j}}.
\]
For even \(j\), the constant equations give \(A_0^2+B_0^2=0\) and \(2A_0B_0=0\). Since the characteristic is odd, both constants must vanish, contradicting \(\nu(x)=j\).

For odd \(j\), the constant coefficient of the first equation forces \(A_0=\pm B_0\ne0\), so \(B\) is invertible in the truncated polynomial ring. The second equation implies \(A=\sigma(A)\) modulo \(t^{n-2j}\). The first becomes \(A^2=B\sigma(B)\). The right side is an even polynomial unit with square constant \(B_0^2\). There are exactly two even polynomial square roots modulo \(t^{n-2j}\): choose either constant \(\pm B_0\), and then solve its even coefficients successively using the invertible coefficient \(2A_0\). All odd coefficients vanish. Hence, for any choice of \(B\) of length \(n-j\) with \(B_0\ne0\) (\((q-1)q^{n-j-1}\) choices), there are two determinations of \(A\) modulo \(t^{n-2j}\), and \(q^j\) free remaining coefficients. Each odd valuation \(j\le m\) therefore contributes exactly \(2(q-1)q^{n-1}\) square-zero elements.

The odd indices between \(1\) and \(m\) number \(\lfloor(n+1)/4\rfloor\). Summing them with the automatic high-valuation locus proves the formulas.

**Modular dihedral specialization.** For characteristic \(p=n\), write \(D_{2p}=\langle r,s\mid r^p=s^2=1,\ srs=r^{-1}\rangle\). The group algebra \(k[C_p]\) is local and \(1+r\) is a unit (augmentation two). Defining \(t=(r-1)/(r+1)\), one has \(t^p=0\) and \(sts=-t\); conversely \(r=(1+t)/(1-t)\). A basis count then identifies the group algebra with the split skew truncation, so the same square-zero count holds there.

## Verification

The embedded `dual_skew_sqzero_check.py` independently implements Ore multiplication using the quadratic presentation \(k[z]/(z^2-d)\), with \(\tau(z)=-z\), and exhaustively checks every element over the prime fields of orders three and five in specified dimensions. The embedded `dual_skew_sqzero_output.txt` records all six checked configurations, the complete valuation strata, and `ALL_CHECKS_PASS`. This computation does not replace the uniform proof over all odd finite fields.

## Relationship to prior work

The existing result *Indistinguishable commutation graphs of split and nonsplit quadratic skew truncations* [1] establishes the same-object commutation-preserving bijection, the centralizer distributions, and the dihedral realization, but does not state, imply numerically, or count the square-zero fibers. The present distinction expressly uses multiplication information that commutation alone loses. Kaur and Khan [2] study units and unitary units of the modular dihedral group algebra; that full-text treatment motivates its importance but does not provide the all-element square-zero census. Algebraically equivalent zero-product or annihilator classifications remain a plausible historical source of overlap, so publication priority is not independently certified.

## Limitations

The proof requires odd field cardinality and odd truncation length. The nonsplit algebra is the quadratic field coefficient case, not an arbitrary quadratic inseparable extension. No claim is made about the entire power-map distribution, arbitrary nonzero square targets, or characteristics two. Finite exhaustive tests cover only the listed small prime fields. The historical search is not a uniqueness proof, and independent mathematical validation is not performed.

## References

1. *Indistinguishable commutation graphs of split and nonsplit quadratic skew truncations*, published 26 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-indistinguishable-commutation-graphs-of-split-and-nonsplit-quadr--6fa3bd18d928 (full mathematical result inspected).
2. K. Kaur and M. Khan, *Units in \(FD_{2p}\)*, arXiv:1305.1260v1, first posted 6 May 2013, https://arxiv.org/abs/1305.1260 (archival unit-group literature; main proof available in lawful author-shared full text at https://www.researchgate.net/publication/236627855_Units_in_FD_2p).
