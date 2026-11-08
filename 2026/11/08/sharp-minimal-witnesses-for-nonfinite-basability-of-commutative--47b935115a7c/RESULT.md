# Sharp minimal witnesses for nonfinite basability of commutative nilpotent power semirings

## Finding

For every integer \(d\ge5\), among all **finite commutative nilpotent semigroups** \(S\) of nilpotency index exactly \(d\) whose **full power semiring** \(\mathcal P(S)\) has no finite equational basis, the least possible number of elements is
\[
\boxed{\min |S|=2d-2.}
\]
Here \(\mathcal P(S)\) contains **all** subsets, including the empty set, with union and setwise multiplication, in the constant-free binary semiring signature. In addition, for every odd \(d\ge5\) there are at least **two nonisomorphic semigroups** attaining the minimum, distinguished by whether a member of the unique minimal generating pair has square zero. Both types have the exact nilpotency-layer cardinalities
\[
\bigl(|S^k\setminus S^{k+1}|\bigr)_{k=1}^{d-1}=(2,\ldots,2,1).
\]
The necessary lower bound is implied by earlier structural lemmas of Distler, not claimed as new on its own. New is the sharp attainment for every unbounded index and the second parity-dependent extremal family combined with the recent full-power-semiring finite-basis criterion.

## Assumptions and scope

A nilpotent semigroup has an absorbing zero \(0\), and \(S^j\) denotes all products of \(j\) elements. Nilpotency index \(d\) means \(S^d=\{0\}\) and \(S^{d-1}\ne\{0\}\). The full power semiring is \(\mathcal P(S)=(2^S,\cup,\cdot)\), where \(AB=\{ab:a\in A,b\in B\}\); the empty subset is included, with no designated constants in the equational signature. Finitely based means that all valid semiring identities follow from finitely many such identities.

Set \(c=d-1\). Wang–Yin–Wang's Corollary 1.2 [1], proved for every finite commutative nilpotent semigroup, states the criterion
\[
\mathcal P(S)\text{ is not finitely based}\quad\Longleftrightarrow\quad s^c=0\ \text{for every }s\in S.
\]
Only this known criterion is imported into the power-semiring part of the result; all semigroup claims below are proved independently.

## Proof

**1. Lower bound from the nilpotency filtration.** Define \(L_k=S^k\setminus S^{k+1}\), for \(1\le k\le c\). These are disjoint and partition \(S\setminus\{0\}\). Choose \(a_1,\ldots,a_c\in S\) with \(w=a_1\cdots a_c\ne0\). Every product of any \(k\) of these factors belongs to \(L_k\): it belongs to \(S^k\), and if it belonged to \(S^{k+1}\), multiplication by the other \(c-k\) factors would put \(w\) in \(S^{c+1}=\{0\}\). Here \(S^{c+1}=\{0\}\) follows from nilpotency index \(d=c+1\).

Suppose \(L_k\) is a singleton for some \(1\le k\le c-1\). Given two positions \(i\ne j\), choose \(k-1\) other positions disjoint from both (possible since \(k-1\le c-2\)), and let \(v\) be the product at these positions, with \(v\) the empty product only as notation when \(k=1\). Both \(a_i v\) and \(a_j v\) are in \(L_k\), so they agree. Factoring the full commutative product as \(a_i(a_jv)\) times the remaining factors permits replacing \(a_j\) by \(a_i\) without changing the nonzero product. This property remains valid after any replacement, since the resulting product is still nonzero. Repeating with \(i=1\) produces \(a_1^c=w\ne0\), contrary to the nonfinite-basis criterion. Therefore \(|L_k|\ge2\) for every \(k<c\). Also \(|L_c|\ge1\). Hence
\[
|S|=1+\sum_{k=1}^c|L_k|\ge1+2(c-1)+1=2c=2d-2.
\]
This filtration lower bound can alternatively be deduced from Distler [2], Lemmas 2.1(iii) and 2.4 (which force a maximal nonzero power if a preterminal layer is a singleton); the displayed argument makes the relevant implication self-contained, without claiming it as original.

**2. A sharp family for every index.** Let \(H_c\) be the commutative semigroup of nonconstant formal monomials in \(a,b\), subject to the zero relations \(a^c=0\) and \(b^2=0\), with all words divisible by either relation identified with the absorbing zero. Its nonzero elements have the uniquely represented forms
\[
a^i\ (1\le i<c),\qquad a^i b\ (0\le i<c).
\]
Therefore \(|H_c|=(c-1)+c+1=2c\). Any product of \(c+1\) elements is zero. The \(c\)-fold product \(a^{c-1}b\) is nonzero, so the index is exactly \(c+1=d\). Every \(c\)-th power is zero: the powers of pure \(a\)-monomials are divisible by \(a^c\), and the square of any monomial containing \(b\) vanishes. By [1], \(\mathcal P(H_c)\) is not finitely based. Its layers are \(L_k=\{a^k,a^{k-1}b\}\) for \(1\le k<c\) and \(L_c=\{a^{c-1}b\}\). This attains the bound for every \(c\ge2\).

**3. A distinct sharp family when \(c\ge4\) is even.** Let \(B_c\) consist of a zero together with labels \((k,\epsilon)\) for \(1\le k<c\), \(\epsilon\in\{0,1\}\), and the additional label \((c,1)\). Define multiplication of nonzero labels by
\[
(k,\epsilon)(\ell,\delta)=
\begin{cases}
(k+\ell,\epsilon+\delta\pmod2),&\text{if this label belongs to }B_c,\\
0,&\text{otherwise}.
\end{cases}
\]
The zero is absorbing. The resulting multiplication is commutative and associative: the degree and parity are additive; once a partial product is absent its degree is at least \(c\), and multiplication by another positive-degree element cannot return to the retained set. This construction has \(2(c-1)+1+1=2c\) elements. Its \(c\)-fold nonzero product \((1,0)^{c-1}(1,1)=(c,1)\) gives index \(c+1\). Each \(c\)-th power vanishes: higher-degree labels overflow, while \((1,0)^c=(c,0)=0\) and \((1,1)^c=(c,0)=0\) because \(c\) is even. Thus [1] makes its full power semiring nonfinitely based. Its \(k\)-th layer consists of the two labels of degree \(k\) for \(k<c\), and its top layer is \(\{(c,1)\}\).

Finally, both families have exactly two indecomposable (degree-one) elements, and \(S\setminus S^2\) is preserved by every semigroup isomorphism. For \(H_c\), exactly one of those elements squares to zero (\(b^2=0\), \(a^2\ne0\)); in \(B_c\), neither squares to zero, since \((1,0)^2=(1,1)^2=(2,0)\ne0\). Therefore \(H_c\not\cong B_c\) whenever \(c\ge4\) is even, proving the asserted multiplicity for odd \(d=c+1\ge5\).

## Verification

The accompanying `verify.py` constructs both finite multiplication tables and tests zero absorption, commutativity, all associative triples, the exact size, the power filtration, index, vanishing \(c\)-th powers, nonzero mixed \(c\)-fold product, and the square-zero-generator distinction. It checks every \(d\) from \(3\) through \(13\) for the first family, and every odd \(d\) from \(5\) through \(13\) for the second, totaling 16 models and 76,824 associativity triples. Run: `python3 verify.py`. The recorded output is in `verification_output.txt`. These tests cover finitely many values and do not establish the theorem for unbounded \(d\); the proof above does.

## Relationship to prior work

Wang, Yin and Wang [1], Corollary 1.2, establish the finite-basis characterization used here, not the all-index minimal cardinality formula or two infinite extremal families. Their Example 4.5 already provides the four-element \(d=3\) member of the first family; **that example is prior work**. Distler [2], Lemmas 2.1 and 2.4, imply the necessary two-elements-per-preterminal-layer lower bound and classify small-coclass semigroups; this implication is **not asserted to be new**. Their low-coclass classification treats coclass at most two, whereas the sharp witnesses here have coclass \(d-2\), growing with \(d\). Distler and Mitchell [3] enumerate degree-three nilpotent semigroups, not this unrestricted variable-index extremal problem. What is asserted is the **sharp attainment for all \(d\ge5\)** and the separate parity family of nonisomorphic minimizers at every odd \(d\ge5\).

## Limitations

The theorem is specific to **commutative** nilpotent semigroups and the **full**, not nonempty, power semiring. It gives a minimum cardinality and at least two nonisomorphic minimizers for odd indices, but does not classify all minimizers, count them, bound the shortest identity obstruction, or address noncommutative semigroups. It uses the published finite-basis criterion [1]; the criterion itself is not reproved here. Earlier work gives the lower bound separately, so value and priority attach to the sharp all-index attainment and nonisomorphic family, not to rediscovering the filtration inequality.

## References

[1] L. Wang, Q. Yin, A. Wang, *Finite bases for full power semirings of finite nilpotent semigroups*, arXiv:2610.01329v1 (first public 2026-10-01), Corollary 1.2, Section 4.3, Example 4.5, https://arxiv.org/abs/2610.01329 .

[2] A. Distler, *Finite nilpotent semigroups of small coclass*, arXiv:1205.2817v1 (2012), Lemmas 2.1 and 2.4 and Theorems 3.2, 4.1–4.2, https://arxiv.org/abs/1205.2817 .

[3] A. Distler, J. D. Mitchell, *The Number of Nilpotent Semigroups of Degree 3*, Electronic Journal of Combinatorics 19(2) (2012), #P51, https://doi.org/10.37236/2441 .
