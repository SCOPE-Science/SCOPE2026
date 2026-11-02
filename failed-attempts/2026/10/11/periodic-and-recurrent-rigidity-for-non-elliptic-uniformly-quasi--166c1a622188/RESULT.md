# Periodic and recurrent rigidity for non-elliptic uniformly quasiregular ball maps

## Finding

Let
\[
n\ge2
\]
and let
\[
f:\mathbb B^n\to\mathbb B^n
\]
be uniformly quasiregular.

Fletcher's recent Denjoy--Wolff theorem equips
\[
\mathbb B^n
\]
with an invariant chain metric
\[
d
\]
for which
\[
f
\]
is non-expanding and gives a complete bounded-versus-escaping dichotomy.

That dichotomy has the following periodic-orbit consequence.

If
\[
f
\]
has a periodic point of prime period
\[
q\ge2,
\]
then
\[
f
\]
must be a uniformly quasiconformal homeomorphism of
\[
\mathbb B^n
\]
onto itself. Moreover,
\[
f
\]
is a
\[
d
\]
-isometry and there is a sequence
\[
k_j\to\infty
\]
such that
\[
f^{k_j}\to\operatorname{id}
\]
locally uniformly.

Therefore, if
\[
f
\]
is not a uniformly quasiconformal homeomorphism of the ball onto itself -- in particular, if
\[
f
\]
is non-injective -- then no cycle of length greater than one can occur.

In that non-elliptic regime exactly one of two alternatives remains.

Either there is a unique fixed point
\[
x_0\in\mathbb B^n,
\]
it is attracting or super-attracting, and
\[
f^m\to x_0
\]
locally uniformly. Then every orbit is relatively compact and
\[
\operatorname{Per}(f)
=
\operatorname{Rec}(f)
=
\{x_0\}.
\]

Or there is a unique boundary point
\[
w\in\partial\mathbb B^n
\]
such that
\[
f^m\to w
\]
locally uniformly. Then no orbit is relatively compact and
\[
\operatorname{Per}(f)
=
\operatorname{Rec}(f)
=
\varnothing.
\]

Here
\[
\operatorname{Per}(f)
\]
denotes the set of periodic points, and
\[
\operatorname{Rec}(f)
=
\left\{
x\in\mathbb B^n:
f^{m_j}(x)\to x
\text{ for some }m_j\to\infty
\right\}.
\]

Equivalently, for a non-elliptic uniformly quasiregular ball self-map, the following four conditions are equivalent:

\[
f
\text{ has a fixed point},
\]
\[
f
\text{ has a periodic point},
\]
\[
f
\text{ has a recurrent point},
\]
and
\[
\text{some orbit is relatively compact in }\mathbb B^n.
\]

Whenever they hold, all iterates converge locally uniformly to the same unique attracting or super-attracting fixed point.

## Assumptions and scope

Uniform quasiregularity means that the maximal dilatations of all positive iterates of
\[
f
\]
are bounded by one common constant.

The phrase non-elliptic is used only as shorthand here for excluding the second branch in the bounded case of Fletcher's theorem: namely, excluding uniformly quasiconformal homeomorphisms of
\[
\mathbb B^n
\]
onto itself for which the invariant chain metric is preserved and a subsequence of iterates converges to the identity.

No properness, surjectivity, or boundary extension is assumed.

The result concerns self-maps of the unit ball. It does not assert a comparable periodic classification for arbitrary globally defined uniformly quasiregular maps, whose Julia dynamics can contain many periodic points.

## Proof

Fletcher's Denjoy--Wolff theorem says that exactly one of the following holds for a uniformly quasiregular self-map of
\[
\mathbb B^n.
\]

In the bounded case, every orbit is relatively compact. Then either
\[
f^m\to x_0\in\mathbb B^n
\]
locally uniformly, where
\[
x_0
\]
is the unique fixed point and is attracting or super-attracting, or
\[
f
\]
is a uniformly quasiconformal homeomorphism of the ball onto itself,
\[
f
\]
is a
\[
d
\]
-isometry, and some subsequence of iterates converges locally uniformly to the identity.

In the escaping case, there is
\[
w\in\partial\mathbb B^n
\]
such that
\[
f^m\to w
\]
locally uniformly throughout the ball.

Now suppose
\[
x
\]
has prime period
\[
q\ge2.
\]
Its orbit is finite, hence relatively compact. Therefore the escaping case is impossible.

If the first bounded branch held, then
\[
f^m(x)\to x_0.
\]
But the sequence
\[
f^m(x)
\]
is periodic with at least two distinct values, so it cannot converge. Hence the first bounded branch is also impossible. The only remaining possibility is the uniformly quasiconformal homeomorphism branch, including the
\[
d
\]
-isometry and subsequential-identity conclusions.

Now assume instead that
\[
f
\]
is not such a homeomorphism. The bounded case can then only be the attracting or super-attracting fixed-point branch.

If the bounded case holds, local-uniform convergence gives
\[
f^m(x)\to x_0
\]
for every
\[
x\in\mathbb B^n.
\]
A periodic point has a finite periodic orbit, so convergence forces it to equal
\[
x_0.
\]
Likewise, if
\[
x
\]
is recurrent, some subsequence satisfies
\[
f^{m_j}(x)\to x,
\]
while the full sequence converges to
\[
x_0.
\]
Therefore
\[
x=x_0.
\]
Thus
\[
\operatorname{Per}(f)
=
\operatorname{Rec}(f)
=
\{x_0\}.
\]

If the escaping case holds, the full orbit of every interior point converges to
\[
w\in\partial\mathbb B^n.
\]
Such an orbit cannot be relatively compact in the open ball. It cannot be periodic, and it cannot have an interior recurrent subsequence. Hence
\[
\operatorname{Per}(f)
=
\operatorname{Rec}(f)
=
\varnothing.
\]

Finally, a fixed point is both periodic and recurrent and has a relatively compact orbit. Conversely, any one of a periodic point, recurrent point, or relatively compact orbit excludes the escaping alternative. Under the non-elliptic assumption, the remaining bounded branch supplies the unique attracting or super-attracting fixed point. This proves all stated equivalences.

## Verification

The proof was checked directly against the exact alternatives in Fletcher's Theorem 1.2.

The only compactness input is that a finite periodic orbit is relatively compact in
\[
\mathbb B^n.
\]
For recurrence, no compactness theorem is needed: local-uniform convergence of the full orbit sequence in each of the two Denjoy--Wolff alternatives is already incompatible with an interior recurrent subsequence unless the point is the unique interior limit.

The conclusion about a nontrivial periodic cycle uses every branch of the source dichotomy. It does not assume that non-injectivity produces strict contraction at every pair; that stronger Schwarz--Pick equality question is explicitly left open in the source.

The argument is qualitative and exact. No finite experiment or numerical computation is used.

## Relationship to prior work

Fletcher's 2026 theorem is the first ball-wide Denjoy--Wolff statement in this setting without properness, surjectivity, or a boundary-extension hypothesis. It gives the two global alternatives from which the present periodic and recurrent classification follows, but the inspected full text does not state periodic-point, recurrent-point, or cycle-rigidity corollaries.

Fletcher and Macclure previously proved a Denjoy--Wolff theorem in
\[
\mathbb B^3
\]
under the substantially stronger assumptions of properness and surjectivity. Their theorem separates an automorphism semigroup from compact convergence to one interior point, but it does not provide the present all-dimensional non-proper classification.

The broader quasiregular-dynamics literature contains many results on repelling periodic points for globally defined maps and on local periodic Fatou dynamics. Those results do not cover arbitrary self-maps of the ball under the hypotheses here and therefore do not imply the stated absence of nontrivial cycles in the non-elliptic ball regime.

Targeted searches for periodic-cycle, recurrence, non-injective, and Denjoy--Wolff formulations did not locate an implication-equivalent statement.

## Limitations

The result is a structural corollary of the source's new global dichotomy; it does not sharpen the invariant metric or the convergence rate.

For the uniformly quasiconformal homeomorphism branch, no attempt is made to classify its periodic or recurrent sets. The theorem only says that a nontrivial periodic cycle forces that branch.

The classification is specific to ball self-maps. Globally defined uniformly quasiregular maps on
\[
\mathbb R^n
\]
or
\[
\mathbb S^n
\]
can have rich periodic dynamics.

The source's open question about whether every distinct pair is strictly contracted by a non-injective map remains untouched.

## References

1. A. N. Fletcher, *Schwarz-Pick and Denjoy-Wolff for uniformly quasiregular maps*, arXiv:2610.00312v1, first posted 28 September 2026.
2. A. Fletcher and D. Macclure, *Strongly automorphic mappings and Julia sets of uniformly quasiregular mappings*, Journal d'Analyse Mathématique 141 (2020), 483--520, DOI: 10.1007/s11854-020-0107-6.
3. A. Hinkkanen, G. J. Martin, and V. Mayer, *Local dynamics of uniformly quasiregular mappings*, Mathematica Scandinavica 95 (2004), 80--100, DOI: 10.7146/math.scand.a-14450.
4. Y. Okuyama and P. Pankka, *Accumulation of periodic points for local uniformly quasiregular mappings*, Mathematical Research Letters 21 (2014), 337--356.
