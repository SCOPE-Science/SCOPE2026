# Constant-weight necklace factorization of primitive-core Toeplitz recurrence polynomials
## Finding
Let \(Q\) be a prime power, let \(d\ge 2\), and let \(f\in\mathbb F_Q[z]\) be a monic primitive polynomial of degree \(d\). For \(1\le k\le d-1\), consider the canonical recurrence polynomial \(\chi_{f,k}(t)\) attached to exterior degree \(k\) in Alekseyev--Khomovsky's graded Toeplitz recurrence profile.

Choose a root \(\alpha\) of \(f\) in \(\mathbb F_{Q^d}\). Then the roots of \(\chi_{f,k}\) are
\[
(-1)^k\alpha^{E_I},\qquad E_I=\sum_{i\in I}Q^i,
\]
where \(I\) runs through the \(k\)-subsets of \(\mathbb Z/d\mathbb Z\). These roots are pairwise distinct, and the \(Q\)-Frobenius sends the root indexed by \(I\) to the root indexed by the cyclic rotation \(I+1\). Therefore the irreducible factors of \(\chi_{f,k}\) over \(\mathbb F_Q\) are indexed exactly by cyclic-rotation orbits of constant-weight binary words of length \(d\) and weight \(k\), with factor degree equal to orbit size.

For each \(h\mid\gcd(d,k)\), the number of irreducible factors of degree \(d/h\) is
\[
N_h=\frac{h}{d}\sum_{r\mid\gcd(d/h,k/h)}\mu(r)\binom{d/(hr)}{k/(hr)}.
\]
Thus if \(\gcd(d,k)=1\), all factors have degree \(d\), and there are exactly \(\binom{d}{k}/d\) of them. Moreover, \(\chi_{f,k}\) is irreducible over \(\mathbb F_Q\) if and only if \(k=1\) or \(k=d-1\).

## Assumptions and scope
A monic polynomial \(f\in\mathbb F_Q[z]\) is called primitive here when any root \(\alpha\) generates \(\mathbb F_{Q^d}^\times\), so \(\alpha\) has multiplicative order \(Q^d-1\). The canonical polynomial \(\chi_{f,k}\) is the characteristic polynomial of the normalized \(k\)-th compound of the companion matrix, equivalently the polynomial whose roots are the fixed-cardinality products specified in Equation (2) and Proposition 2.1 of arXiv:2609.27268.

The conclusion is a factorization theorem for this canonical annihilator. It does not assert that every specialized scalar Toeplitz determinant sequence has minimal recurrence polynomial equal to \(\chi_{f,k}\); the source explicitly allows the specialized minimal polynomial to be a proper divisor.

## Proof
Because \(f\) is monic and primitive, its roots are
\[
\alpha,\alpha^Q,\ldots,\alpha^{Q^{d-1}}.
\]
The defining root-product formula for \(\chi_{f,k}\) therefore gives one mode
\[
\lambda_I=(-1)^k\alpha^{E_I},\qquad E_I=\sum_{i\in I}Q^i,
\]
for each \(k\)-subset \(I\subseteq\mathbb Z/d\mathbb Z\).

For \(1\le k\le d-1\), every \(E_I\) is an integer strictly between \(0\) and \(Q^d-1\). Distinct subsets have distinct base-\(Q\) expansions with digits only \(0\) and \(1\), so \(E_I\ne E_J\) whenever \(I\ne J\). Since \(\alpha\) has order \(Q^d-1\), the modes \(\lambda_I\) are pairwise distinct. Hence \(\chi_{f,k}\) is squarefree.

The \(Q\)-Frobenius fixes \((-1)^k\) and satisfies
\[
\lambda_I^Q=(-1)^k\alpha^{Q E_I}=\lambda_{I+1},
\]
because reduction modulo \(Q^d-1\) replaces the term \(Q^d\) by \(1\). Thus a Frobenius orbit of modes is exactly a cyclic-rotation orbit of \(k\)-subsets. Over \(\mathbb F_Q\), the minimal polynomial of a mode has as roots its Frobenius orbit, so each rotation orbit gives one irreducible factor and its degree is the orbit size.

Suppose an orbit has size \(e=d/h\). Its word is a repetition of \(h\) copies of an aperiodic binary word of length \(e\) and weight \(k/h\); hence necessarily \(h\mid k\). The standard Möbius count of aperiodic constant-weight necklaces gives
\[
\frac1e\sum_{r\mid\gcd(e,k/h)}\mu(r)\binom{e/r}{(k/h)/r},
\]
which becomes the stated \(N_h\) after substituting \(e=d/h\).

If \(\gcd(d,k)=1\), only \(h=1\) can occur, so every orbit has size \(d\) and their number is \(\binom{d}{k}/d\). For \(k=1\) and \(k=d-1\), cyclic rotation is transitive, so \(\chi_{f,k}\) is irreducible of degree \(d\). If \(1<k<d-1\), then \(\binom{d}{k}>d\), while every irreducible factor has degree at most \(d\); therefore \(\chi_{f,k}\) is reducible.

## Verification
A standalone exact checker accompanies this note. It verifies the necklace orbit-count formula for every \(2\le d\le10\) and every \(1\le k<d\), and then performs explicit finite-field calculations for primitive binary cores in degrees \(4\), \(5\), and \(6\). It constructs each Frobenius-orbit factor directly in \(\mathbb F_{2^d}[t]\), checks that its coefficients lie in \(\mathbb F_2\), and confirms that its degree equals the corresponding rotation-orbit size.

For example, for the primitive core \(f(z)=z^4+z+1\) and \(k=2\), the factor degrees are \(4\) and \(2\). For the primitive core \(f(z)=z^6+z+1\), the factor degrees are \(6,6,3\) at \(k=2\), and \(6,6,6,2\) at \(k=3\). The checker terminates with `CHECK_OK`.

The computations are finite consistency checks, not the proof of the arbitrary-\(Q\), arbitrary-\(d\) statement; the proof above is symbolic.

## Relationship to prior work
Alekseyev and Khomovsky define the canonical exterior-degree recurrence polynomial by fixed-cardinality products of the roots of a polynomial core and identify it with the characteristic polynomial of a normalized compound companion matrix. They also emphasize that the canonical annihilator need not be the specialized minimal scalar recurrence. Their companion preprint develops the same root-product/compound representation for banded Toeplitz determinants.

Standard finite-field theory identifies irreducible factors through Frobenius cyclotomic cosets, and constant-weight binary necklaces encode cyclic-shift orbits. The present finding applies that machinery to the newly introduced graded Toeplitz recurrence profile and obtains the complete factor-degree distribution, the coprime uniform-degree case, and the exact irreducibility boundary for primitive cores. Targeted searches in the two inspected Toeplitz preprints found no finite-field, primitive-polynomial, cyclotomic-coset, or necklace treatment.

## Limitations
The theorem assumes that the core polynomial is primitive, not merely irreducible. For a merely irreducible core, different constant-weight subset sums can become congruent modulo the multiplicative order of a root, so the squarefreeness and orbit description above need modification. The theorem classifies the canonical annihilator; it does not determine which factors survive in every specialized scalar determinant recurrence. The literature search did not establish global uniqueness of the observation, and an equivalent statement could exist in finite-field compound-matrix language outside the sources inspected.

## References
1. Max A. Alekseyev and Dmitry I. Khomovsky, *Toeplitz multiplication and graded factorization of determinant recurrences*, arXiv:2609.27268, 2026.
2. Max A. Alekseyev and Dmitry I. Khomovsky, *Constructive recurrences for determinants and permanents of banded Toeplitz matrices*, arXiv:2609.13674, 2026.
3. Niko Rebenich, *Topics in the Theory of Finite Fields*, PhD dissertation, University of Victoria, 2016; see the discussion of cyclotomic cosets, minimal polynomials, and necklaces.
