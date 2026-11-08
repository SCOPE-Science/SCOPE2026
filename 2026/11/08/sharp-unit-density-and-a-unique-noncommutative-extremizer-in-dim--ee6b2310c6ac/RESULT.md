# Sharp unit density and a unique noncommutative extremizer in dimension seven

## Finding
For every prime \(p\), every **noncommutative associative unital** algebra \(R\) of dimension exactly \(7\) over \(\mathbb F_p\) satisfies
\[
\frac{|R^\times|}{|R|}\leq
(1-p^{-2})(1-p^{-3}).
\]
Equality holds **if and only if** \(R\) is isomorphic as an \(\mathbb F_p\)-algebra to \(T_p\times\mathbb F_{p^3}\), where \(T_p\) is the Frobenius-skew square-zero extension of \(\mathbb F_{p^2}\), namely
\[
T_p=\mathbb F_{p^2}\oplus\mathbb F_{p^2}u,
\qquad u^2=0,\quad ua=a^pu\quad(a\in\mathbb F_{p^2}).
\]
Equivalently, the greatest possible unit count is \(p^2(p^2-1)(p^3-1)\), and the least possible number of **nonunits including zero** is \(p^7-p^2(p^2-1)(p^3-1)\); both extrema have this unique ring as extremizer. For \(p=2\), this ring has \(128\) elements, exactly \(84\) units and \(44\) nonunits.

This is a natural early odd-dimensional transition: in dimension \(5\), the unit density of a noncommutative unital \(\mathbb F_p\)-algebra is at most \(1-p^{-1}\), and this latter bound is attained; by contrast the displayed dimension-seven maximum is strictly larger than \(1-p^{-1}\). The dimensional comparison motivates the sharp seven-dimensional problem but is not a claim about higher dimensions.

## Assumptions and scope
All algebras are finite-dimensional, associative, and possess a two-sided identity distinct from zero. Their base field is exactly the prime field \(\mathbb F_p\); \(p\) is an arbitrary prime. Dimension refers to vector-space dimension over this field, not the number of generators. The group of invertible elements is \(R^\times\). The zero element counts as a nonunit, not as a nonzero zero divisor. For a finite unital ring every nonunit is a two-sided zero divisor (allowing zero), so the statement is also a sharp nonunit/zero-divisor count under that convention. Isomorphism means an identity-preserving algebra isomorphism over \(\mathbb F_p\).

## Proof
**1. Unit density is a semisimple invariant.** Let \(J\) be the Jacobson radical of \(R\), and \(S=R/J\). The radical is nilpotent and the unit map onto \(S^\times\) has kernel \(1+J\) of cardinality \(|J|\). Therefore
\[
\frac{|R^\times|}{|R|}=\frac{|S^\times|}{|S|}.
\]
The Artin–Wedderburn theorem writes
\[
S\cong\prod_{i=1}^{t}M_{d_i}(\mathbb F_{p^{f_i}}),
\qquad \dim_{\mathbb F_p}S=\sum_i d_i^2f_i\le7.
\]
The unit density of a matrix factor is \(\prod_{j=1}^{d_i}(1-p^{-f_i j})\). If some \(d_i\ge2\), then necessarily \(d_i=2,f_i=1\), so the density of the entire algebra is at most \((1-p^{-1})(1-p^{-2})\), strictly less than the proposed bound.

**2. Reduction to products of fields.** Hence it suffices to consider \(S=\prod_i\mathbb F_{p^{f_i}}\). A factor with \(f_i=1\) likewise forces density at most \(1-p^{-1}\), and for every \(p\ge2\),
\[
1-p^{-1}<(1-p^{-2})(1-p^{-3}).
\]
If \(t=1\), then the separability of finite fields and the Wedderburn–Malcev complement theorem provide a coefficient field \(\mathbb F_{p^{f_1}}\subseteq R\). Consequently \(f_1\) divides \(7\). The possibility \(f_1=7\) gives \(J=0\) and a commutative field; the possibility \(f_1=1\) was already bounded. We may therefore assume \(t\ge2\), every \(f_i\ge2\), and \(J\ne0\) (otherwise \(R=S\) is commutative).

A semisimple complement \(S\subseteq R\) exists by the same separability theorem. Thus \(J\), as a left \(S\)-module, splits under the primitive central idempotents of the complement: its \(\mathbb F_p\)-dimension is a nonnegative integral linear combination of the field degrees \(f_i\). Since \(\dim S<7\) and the degrees are at least two, there are only five candidate unordered lists:
\[
(2,2),\quad (2,3),\quad (2,4),\quad(3,3),\quad(2,2,2).
\]
The corresponding radical dimensions are \(3,2,1,1,1\). For the four lists other than \((2,3)\), the required radical dimension cannot be a nonnegative combination of the displayed degrees. Thus
\[
S\cong\mathbb F_{p^2}\times\mathbb F_{p^3},
\qquad\dim_{\mathbb F_p}J=2.
\]
This forces precisely the bound \((1-p^{-2})(1-p^{-3})\). In particular, **equality implies this semisimple quotient**.

**3. Equality is rigid.** Lift the two central idempotents of \(S\) to orthogonal idempotents \(e_1,e_2\) in the chosen complement. The Peirce components \(e_iJe_j\) have dimensions divisible by \(f_i\) as left field modules and by \(f_j\) as right field modules. Because \(\dim J=2\), any component involving the field of degree \(3\) vanishes; the cross components would have dimension divisible by both \(2\) and \(3\), and so also vanish. Therefore \(J=e_1Je_1\), and the complementary factor \(e_2Re_2\) is just \(\mathbb F_{p^3}\). The other factor \(B=e_1Re_1\) is local of dimension \(4\), with residue field \(\mathbb F_{p^2}\), and its radical \(J\) is one-dimensional as a left \(\mathbb F_{p^2}\)-vector space. Nilpotence forces \(J^2=0\).

Choose any nonzero \(u\in J\). Right multiplication by the coefficient field commutes with its left multiplication, and defines a unital \(\mathbb F_p\)-algebra map \(\sigma:\mathbb F_{p^2}\to\mathbb F_{p^2}\) through \(ua=\sigma(a)u\). This map is an automorphism of the finite field, so it is either the identity or Frobenius \(\sigma(a)=a^p\). The identity case makes \(B\), hence \(R\), commutative. Thus noncommutativity forces Frobenius, and \(B\cong T_p\). Conversely, Frobenius is nontrivial on \(\mathbb F_{p^2}\), so \(T_p\) is noncommutative and the constructed product achieves equality. The two options are not isomorphic because one is commutative and the other is not. This proves both the bound and the unique equality case.

For completeness, the coefficient-field splitting used above is standard Wedderburn–Malcev over the perfect field \(\mathbb F_p\). In the only nontrivial local equality case, it may alternatively be constructed directly: lift a primitive generator of the residue field satisfying a separable irreducible quadratic polynomial \(h\); since \(J^2=0\), replacing the lift \(t\) by \(t-h(t)h'(t)^{-1}\) produces an exact root of \(h\), hence a copy of \(\mathbb F_{p^2}\).

**4. Why seven is the first odd threshold.** For dimension \(3\), the only noncommutative unital algebra is the upper triangular \(2\)-by-\(2\) matrix ring over \(\mathbb F_p\), whose unit density is \((1-p^{-1})^2\) (Raghavendran, Theorem 14). For dimension \(5\), a matrix block or degree-one field factor forces density at most \(1-p^{-1}\), while any radical-bearing product of field factors of degrees at least \(2\) is dimensionally impossible; a sole field factor has degree dividing \(5\), giving the same bound. The bound is realized by the noncommutative local algebra with basis \(1,x,y,z,xy\) and nonzero products among \(x,y,z,xy\) only \(xy\) (all other products of radical-basis elements vanish). Its radical has dimension four, so its unit density is \(1-p^{-1}\). This comparison identifies the first odd dimension in which the maximal unit density exceeds the elementary local bound.

## Verification
The independent executable file `verify.py` checks the quadratic-field constructions, their unit counts for \(p=2,3,5\), noncommutativity, inverses, and associativity (exhaustively for \(p=2\)); it also enumerates every possible product-of-fields semisimple dimension profile with all degrees at least two and nonzero radical in dimension seven, using the proved necessary module divisibility condition. Output is in `verify-output.txt`. It verifies the extremal arithmetic and the key short dimension enumeration, not all possible seven-dimensional algebras. The general upper bound and uniqueness are justified by the symbolic structural proof above.

## Relationship to prior work
Michael Kinyon, *Rings with Finitely Many Zero Divisors* (first public preprint 25 April 2026, arXiv:2604.23423), proves a bound on the size of an arbitrary ring given its zero-divisor count, recounting earlier results of Ganesan, Koh and Hirano. That theorem neither fixes the prime-field dimension nor optimizes unit density within noncommutative rings of dimension seven. R. Raghavendran, *Finite associative rings* (1969), Theorems 10–12 and 14, supplies structural classifications for field extensions of length two or three and extremal small-zero-divisor rings; his local square-zero Frobenius-twist factor is acknowledged as known. The new assertion is the seven-dimensional **global unit-density extremum and uniqueness**, obtained by excluding all other possible semisimple quotient profiles through radical module dimensions. The 1986 article of Kobayashi and Koh on classification by zero divisors could not be examined in full; it is a documented residual historical-priority risk, not evidence of novelty by itself.

## Limitations
This is a statement only for associative unital algebras over prime fields, and only in vector-space dimension seven. It is not a general formula for arbitrary dimensions, higher-characteristic Galois coefficient fields, or algebras without identity. A self-review does not establish independent correctness or historical priority; the most relevant inaccessible 1986 classification remains a source risk. The finite tests are finite tests, not a census of all algebras of the stated order.

## References
1. Michael Kinyon, *Rings with Finitely Many Zero Divisors*, arXiv:2604.23423, first posted 25 April 2026, version 2 posted 28 April 2026. https://arxiv.org/html/2604.23423v2
2. R. Raghavendran, *Finite associative rings*, Compositio Mathematica 21 (1969), 195–229, especially Theorems 10–12 and 14. https://www.numdam.org/item/CM_1969__21_2_195_0/
3. Yuji Kobayashi and Kwangil Koh, *A classification of finite rings by zero divisors*, J. Pure Appl. Algebra 40 (1986), 135–147, DOI:10.1016/0022-4049(86)90036-8 (bibliographic comparison only; full text not examined).
4. David Dolžan, *The probability of zero multiplication in finite rings*, Bull. Aust. Math. Soc. 106 (2022), 83–88, DOI:10.1017/S0004972721001246 (abstract inspected; a distinct probability invariant).
