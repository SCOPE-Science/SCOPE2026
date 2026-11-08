# Two-level cyclic autocorrelation is equivalent to signed doubling symmetry of subset-sum generators

## Finding

Let \(n\ge3\) be any **odd** integer and let \(A\) be a finite multiset of units of \(\mathbb Z/n\mathbb Z\), with cardinality \(N\) and multiplicity \(m(a)\) at \(a\). Let \(b(r)\) count *all* subsets of \(A\), including the empty subset, whose sum is congruent to \(r\pmod n\); multiplicities are counted as distinguishable occurrences. Define its periodic autocorrelation by \(H(s)=\sum_{r\bmod n}b(r)b(r+s)\), and the unsigned multiplicity \(c(a)=m(a)+m(-a)\).

**Theorem.** The following assertions are equivalent, for every odd \(n\ge3\), without any prime-power or restriction on its factorization:

1. \(H(0)=(4^N+n-1)/n\) and \(H(s)=(4^N-1)/n\) for every \(s\not\equiv0\pmod n\).
2. For every \(1\le t<n\), \(\big|\prod_{a\in A}(1+\exp(2\pi i ta/n))\big|=1\).
3. For every \(a\in(\mathbb Z/n\mathbb Z)^\times\), \(c(2a)=c(a)\).

Thus the exact two-level correlation property holds if and only if the multiplicities **after identifying signs** are constant on every orbit of multiplication by \(2\). The statement concerns arbitrary finite multisets of unit residues, not necessarily sets or equidistributed subset sums.

As an application, if the **nonempty** subset sums of \(A\) are equally distributed across all \(n\) residues, then \(c(2a)=c(a)\) at every unit \(a\), for every odd modulus. The converse to that last implication is not asserted: in modulus \(9\), the multiset \(A=\{1,1,2,2,4,4\}\) has the two-level autocorrelation but its subset-sum counts, ordered by residues \(0,1,\ldots,8\), are \((7,7,7,7,7,7,7,8,7)\), so its nonempty subset sums are not equidistributed. Another illustrative composite modulus outside the prime-power case is \(n=65\), with \(A=\{1,2,4,8,16,32\}\): its subset-sum counts are \(1\) on residues \(0,\ldots,63\) and \(0\) on residue \(64\), so its autocorrelation is \(64\) at shift \(0\) and \(63\) at every other shift.

## Assumptions and scope

Throughout, \(n\) is an odd integer at least \(3\). Every element of \(A\) is invertible modulo \(n\); the multiset may be empty and may contain repeated residues. Put \(U=(\mathbb Z/n\mathbb Z)^\times\). Write \(m:U\to\mathbb Z_{\ge0}\) for the multiplicity function, with \(\sum_{a\in U}m(a)=N\), and extend it by zero to nonunits only when convenient. The count \(b\) includes the empty subset, unlike the convention in the motivating paper. All equalities are exact integers or complex-number equalities as indicated. No assertion is made for nonunit generators or even moduli.

We use the classical Dirichlet nonvanishing theorem \(L(1,\chi)\ne0\) for every nonprincipal Dirichlet character \(\chi\), and elementary facts about primitive-character Gauss sums. They are external established mathematical theorems, not inferred from numerical experiments.

## Proof

**Step 1: the autocorrelation/Fourier equivalence.** Set \(\zeta=\exp(2\pi i/n)\) and \(B(t)=\sum_{r\bmod n}b(r)\zeta^{tr}\). Choosing each occurrence of a generator or omitting it gives
\[
B(t)=\prod_{a\in U}(1+\zeta^{ta})^{m(a)},\qquad B(0)=2^N.
\]
The discrete Fourier transform of \(H(s)=\sum_r b(r)b(r+s)\) is \(|B(t)|^2\). Hence assertion 2 is equivalent, by inverse Fourier transformation, to the exact formulas in assertion 1. This also proves the integrality of the expressions whenever assertion 3 holds, rather than assuming divisibility of \(4^N-1\) by \(n\).

**Step 2: translate the magnitude condition into a sine-log relation.** Since \(n\) is odd, \(1-\zeta^{ta}\ne0\) and \(1+\zeta^{ta}\ne0\) for every unit \(a\) and every \(1\le t<n\). The identity
\[
1+z=(1-z^2)/(1-z)
\]
implies
\[
\log|B(t)|=\sum_{a\in U}\delta(a)\log|1-\zeta^{ta}|,
\qquad\delta(a)=m(2^{-1}a)-m(a).
\]
Here \(2^{-1}\) denotes the inverse of \(2\) modulo \(n\). If assertion 3 holds, then \(\delta(a)+\delta(-a)=0\) for every \(a\). Since the logarithm on the right is invariant under \(a\mapsto-a\), it follows immediately that \(\log|B(t)|=0\) for every nonzero \(t\). Thus assertion 3 implies assertion 2.

**Step 3: a nonvanishing log-sine character transform.** Let \(d>1\) be an odd positive integer, and let \(\chi\) be a primitive, even, nonprincipal Dirichlet character of conductor \(d\). Then
\[
\sum_{u\in(\mathbb Z/d\mathbb Z)^\times}\chi(u)\log|1-\exp(2\pi i u/d)|
=-\tau(\chi)L(1,\overline\chi)\ne0,
\]
where \(\tau(\chi)=\sum_{u\bmod d}\chi(u)\exp(2\pi i u/d)\) is the Gauss sum. To justify the equality, for \(0<\rho<1\) expand
\[
\log|1-\rho\exp(2\pi i u/d)|
=-\sum_{k\ge1}\frac{\rho^k}{k}\cos(2\pi ku/d).
\]
Sum against the even character \(\chi\). The primitive Gauss-sum identity converts the inner cosine sum to \(\tau(\chi)\overline\chi(k)\); Abel's limiting theorem gives the displayed formula as \(\rho\uparrow1\). The Gauss sum has absolute value \(\sqrt d\), and Dirichlet's nonvanishing theorem ensures that the \(L\)-value is nonzero. This step includes complex-valued even characters; it does not assume that \(\chi\) is real.

**Step 4: recover all signed multiplicities.** Suppose assertion 2 holds, so that the expression in Step 2 vanishes for each \(1\le t<n\). Fix any *nonprincipal even* character \(\psi\) of \(U\). It is induced by a unique primitive even nonprincipal character \(\chi\) of conductor \(d\mid n\). For each \(u\in(\mathbb Z/d\mathbb Z)^\times\), choose \(t=(n/d)u\), which is a nonzero residue modulo \(n\). Summing the vanishing identity in Step 2 over these \(t\), with weights \(\chi(u)\), and substituting \(v\equiv ua\pmod d\), yields
\[
0=\left(\sum_{a\in U}\delta(a)\overline\psi(a)\right)
\left(\sum_{v\in(\mathbb Z/d\mathbb Z)^\times}\chi(v)\log|1-\exp(2\pi i v/d)|\right).
\]
The second factor is nonzero by Step 3; hence the first is zero. For the principal even character, \(\sum_{a\in U}\delta(a)=0\) holds directly from the definition of \(\delta\), since multiplication by \(2\) permutes \(U\). Thus **every even character** of the finite abelian group \(U\) has zero Fourier coefficient against \(\delta\).

An even character means \(\psi(-1)=1\). By character orthogonality on the quotient \(U/\{\pm1\}\), the function \(\delta(a)+\delta(-a)\) must vanish identically. Rewriting this assertion gives
\[
 m(2^{-1}a)+m(-2^{-1}a)=m(a)+m(-a),
\]
which is exactly assertion 3 after replacing \(a\) by \(2a\). This proves assertion 2 implies assertion 3, completing all equivalences.

**Corollary for equidistributed nonempty sums.** If all nonempty subset sums are equally frequent, then the profile including the empty subset has the form \(b(r)=M+\mathbf1_{r=0}\), with \(nM=2^N-1\). Therefore \(B(t)=1\) for every \(1\le t<n\). Assertion 2 holds, and assertion 3 follows. This is **only a necessary** conclusion about nonempty-sum equidistribution, not a converse.

## Verification

A standalone Python 3 checker (`verify.py`) constructs subset-sum profiles by exact cyclic convolution, forms the complete integer autocorrelation, and checks its equivalence to the signed doubling-invariance condition. It exhausts all binary multiplicity functions on units for odd moduli \(3\le n\le21\) having at most 12 units: \(3,5,7,9,11,13,15,21\). Additional deterministic pseudorandom small-support multiset cases cover \(25,27,33,35,45,65,91,105\). The checker also confirms the explicit counterexample in modulus \(9\). These are finite validation tests, not a substitute for the infinite proof, whose critical nonstandard step is the character inversion in Steps 3–4.

Run `python3 verify.py` from the directory containing that file. It uses only Python's standard library.

## Relationship to prior work

Gaitanas, *On subset sums of \(\mathbb Z_n^\times\) which are equally distributed modulo \(n\)*, arXiv:2304.14141 (first public 2023-04-07), studies exactly uniform **nonempty** subset-sum profiles and shows that, for prime powers and certain other moduli, the generators decompose into signed powers-of-two progressions; it states the general odd-modulus converse as a question. The June 2023 correction to its sufficient-condition theorem is relevant and does not change the distinct Fourier-magnitude statement here. The present theorem is a **different and broader spectral characterization**, including multisets with nonuniform subset sums and arbitrary odd moduli. It does not assert a complete classification of fully uniform nonempty-subset sums.

Ciprietti and Glaudo, *On the Determination of Sets By Their Subset Sums*, arXiv:2301.04635 (first public 2023-01-11), investigate equality of full subset-sum multisets and cyclotomic-unit relations. Their Proposition 4.6 imposes the arithmetic restriction \(n\in O_{\mathrm{FS}}\). Their general Lemma 4.4 concerns finite-index image of a multiplicative cyclotomic map, not the present exact two-level autocorrelation characterization for arbitrary odd \(n\). Both works provide close structural context.

The comparison is between the **mathematical implications**: published subset-sum equality results neither assert nor immediately imply the all-odd-moduli equivalence between a two-level correlation profile and signed doubling-invariant generator multiplicities. The classical Dirichlet \(L(1,\chi)\)-nonvanishing theorem, used as an input here, is not a new result.

## Limitations

The unit-generator and odd-modulus hypotheses are essential to the presented argument. Fourier magnitudes do not determine Fourier phases, so a two-level autocorrelation does not force nonempty subset-sum equidistribution. The theorem does not give a complete phase-based characterization of equidistributed nonempty subset sums for all composite moduli. Originality assessment is limited by possible unidentified equivalent literature, especially in cyclotomic-unit and phase-retrieval work. No independent scientific audit has been performed.

## References

1. K. Gaitanas, *On subset sums of \(\mathbb Z_n^\times\) which are equally distributed modulo \(n\)*, arXiv:2304.14141v1 (2023-04-07), https://arxiv.org/abs/2304.14141; Archiv der Mathematik 121 (2023), 47–54, DOI 10.1007/s00013-023-01853-2.
2. K. Gaitanas, *Correction to: On subset sums of \(\mathbb Z_n^\times\) which are equally distributed modulo \(n\)*, Archiv der Mathematik 121 (2023), 109–110, DOI 10.1007/s00013-023-01864-z, 2023-06-21, https://doi.org/10.1007/s00013-023-01864-z.
3. A. Ciprietti and F. Glaudo, *On The Determination of Sets By Their Subset Sums*, arXiv:2301.04635v2 (2023-01-18), https://arxiv.org/abs/2301.04635.
4. Classical Dirichlet theorem: \(L(1,\chi)\ne0\) for nonprincipal characters; primitive Gauss sum and character orthogonality identities (standard analytic number theory).
