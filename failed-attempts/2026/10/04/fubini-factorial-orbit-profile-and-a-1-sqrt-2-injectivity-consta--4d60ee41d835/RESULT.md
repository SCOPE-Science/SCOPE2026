# Fubini-factorial orbit profile and a \(1/\sqrt2\) injectivity constant for Braunfeld's exceptional homogeneous permutation structure

## Finding
Let \(M\) be the Fraïssé limit of Braunfeld's Example 2.7. Its finite structures have an equivalence relation \(E\), a linear order \(<_1\), and an \(E\)-convex linear order \(<_2\) that agrees with \(<_1\) on each \(E\)-class. Equivalently, one may use a global linear order and an independent linear order on the set of \(E\)-classes.

Write \(F_n\) for the ordered Bell (Fubini) number, \(a_n\) for the number of \(\operatorname{Aut}(M)\)-orbits on injective ordered \(n\)-tuples, and \(b_n\) for the number of orbits on all ordered \(n\)-tuples. Then
\[
\boxed{a_n=n!F_n=n!\sum_{k=0}^{n} k!{n\brace k}}
\]
and
\[
\boxed{b_n=\sum_{k=0}^{n}{n\brace k}a_k}.
\]
The first values are
\[
a_n=1,1,6,78,1800,64920,3371760,238356720,22008067200,\ldots
\]
and
\[
b_n=1,1,7,97,2311,84961,4469767,318906337,29650247431,\ldots.
\]
Most notably,
\[
\boxed{\lim_{n\to\infty}\frac{a_n}{b_n}=\frac1{\sqrt2}}.
\]
Thus, unlike many oligomorphic structures in which repeated-coordinate orbit types are asymptotically negligible or overwhelming, this homogeneous permutation structure has a nontrivial limiting injective fraction.

## Assumptions and scope
The language and Fraïssé class are exactly those in Example 2.7 of Braunfeld's *Homogeneous 3-dimensional permutation structures*. Braunfeld also gives an interdefinable presentation in which \(<_1'\) is a global linear order and \(<_2'\) is a subquotient order from \(E\) to the universal relation, hence a linear order on the \(E\)-classes. The orbit counts below use ordered tuples; \(a_n\) requires distinct coordinates, while \(b_n\) allows repetitions.

The asymptotic statement uses the classical Fubini-number estimate
\[
F_n=\frac{n!}{2(\log 2)^{n+1}}(1+O(\theta^n))
\]
for some \(0<\theta<1\). Only the combination of this standard estimate with the exact model-theoretic orbit transform is claimed here.

## Proof
Because the Fraïssé limit is homogeneous, two injective ordered \(n\)-tuples lie in the same automorphism orbit exactly when the labeled finite structures they induce on their coordinates are isomorphic via the coordinate-preserving map.

Use Braunfeld's interdefinable presentation. On the labeled set \([n]\), choose the equivalence relation \(E\). If it has \(k\) classes, there are \({n\brace k}\) possibilities. Independently choose the global linear order, giving \(n!\) possibilities, and choose a linear order of the \(k\) equivalence classes, giving \(k!\) possibilities. Every such choice belongs to the age, and it uniquely determines the original \(E\)-convex order by ordering distinct classes according to the quotient order and ordering points inside each class according to the global order. Therefore
\[
a_n=n!\sum_{k=0}^{n}{n\brace k}k!=n!F_n.
\]

For an arbitrary ordered \(n\)-tuple, let its equality pattern have \(k\) blocks. There are \({n\brace k}\) possible equality patterns. After replacing each block by its distinct value, the remaining orbit datum is exactly an injective ordered \(k\)-tuple orbit. Equality patterns are invariant under coordinatewise automorphisms, so no two different patterns merge. Hence
\[
b_n=\sum_{k=0}^{n}{n\brace k}a_k.
\]

It remains to extract the limiting ratio. Put \(L=\log 2\). From the Fubini asymptotic,
\[
a_m=\frac{(m!)^2}{2L^{m+1}}(1+O(\theta^m)).
\]
Write \(j=n-k\). For every fixed \(j\),
\[
{n\brace n-j}=\frac{n^{2j}}{2^j j!}+O(n^{2j-1}),
\qquad
\frac{a_{n-j}}{a_n}=\frac{L^j}{n^{2j}}(1+O(n^{-1})),
\]
so
\[
{n\brace n-j}\frac{a_{n-j}}{a_n}\longrightarrow \frac{(L/2)^j}{j!}.
\]
The interchange of limit and summation is controlled as follows. A partition of \([n]\) into \(n-j\) blocks has a canonical spanning forest with \(j\) edges (join the least element of each non-singleton block to every other element of that block), so
\[
{n\brace n-j}\le \binom{\binom n2}{j}.
\]
For \(j\le n/2\), the displayed Fubini estimate therefore gives a summable majorant of the form \(C(2L)^j/j!\). For \(k<n/2\), the elementary bound \({n\brace k}\le k^n/k!\), together with the same factorial-scale estimate for \(a_k/a_n\), shows that the whole remaining tail is superexponentially small. Consequently dominated convergence yields
\[
\frac{b_n}{a_n}\longrightarrow
\sum_{j\ge0}\frac{(L/2)^j}{j!}
=e^{L/2}=\sqrt2,
\]
which proves \(a_n/b_n\to 1/\sqrt2\).

## Verification
The bundled `verify.py` performs two independent finite replays. First, for \(n\le5\), it generates every set partition, every global order, and every quotient order, converts each choice into the actual relation matrices \((E,<_{1},<_{2})\), and checks that the number of distinct injective labeled structures is exactly \(n!F_n\). Second, it generates every equality pattern of an arbitrary tuple, pulls back all injective relation structures along that pattern, includes coordinate equality in the signature, and checks that the number of distinct signatures is exactly the Stirling transform \(b_n\).

The script also computes the exact sequences by integer recurrence through larger \(n\) and numerically confirms convergence of \(a_n/b_n\) toward \(2^{-1/2}\). The expected final line is `VERIFY_OK`.

## Relationship to prior work
Braunfeld's Example 2.7 supplies the homogeneous Fraïssé structure and its equivalent subquotient-order presentation; the source does not enumerate its finite tuple orbits. The Fubini numbers themselves are classical: they count ordered set partitions or weak orders, with exponential generating function \(1/(2-e^x)\) and the standard factorial/logarithmic asymptotic used above. Those combinatorial facts are not claimed as new.

The broader permutation-group literature studies orbit growth on sets and tuples, including Merola's work on orbits on \(n\)-tuples and Braunfeld's later work on growth rates of \(\omega\)-categorical structures. Targeted searches for this particular Example 2.7 structure, the exact \(n!F_n\) profile, its repeated-coordinate Stirling transform, and the constant \(1/\sqrt2\) did not locate a prior statement. The contribution claimed here is the structural identification of this catalogued homogeneous permutation structure with these exact orbit counts and the resulting nontrivial injectivity constant.

## Limitations
The originality conclusion is literature-based and cannot exclude unindexed folklore or a calculation hidden under a different presentation of the same automorphism group. The limiting argument depends on a classical asymptotic for Fubini numbers rather than deriving that asymptotic from first principles. The result concerns this specific homogeneous structure and does not assert a universal law for homogeneous permutation structures.

## References
Samuel Braunfeld, *Homogeneous 3-dimensional permutation structures*, Electronic Journal of Combinatorics 25(2) (2018), P2.52. arXiv:1710.05138; DOI:10.37236/7506.

OEIS A000670, *Fubini numbers / ordered Bell numbers*, including the interpretation as ordered partitions and standard generating-function/asymptotic references.

Francesca Merola, *Orbits on n-tuples for infinite permutation groups*, European Journal of Combinatorics 22 (2001), 225–241.

Samuel Braunfeld, *Monadic stability and growth rates of omega-categorical structures*, Proceedings of the London Mathematical Society 124 (2022), 373–386. DOI:10.1112/plms.12429.
