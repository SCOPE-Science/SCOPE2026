# Quadratic state blow-up is sharp for two-agent proper S5 covers
## Finding

Bjorndahl and Sink give a finite properization construction for relational models: an \(m\)-state model is replaced by a proper model on
\[
X\times X,
\]
so the constructed model has
\[
m^2
\]
states, and projection to the first coordinate is a surjective bounded morphism. Their construction preserves equivalence relations, so it applies directly to S5 epistemic models.

For two agents, this quadratic size is unavoidable in the worst case.

Let
\[
U_m=(X,R_1,R_2)
\]
be the \(m\)-world frame with
\[
R_1=R_2=X\times X.
\]
Thus both agents have universal S5 accessibility.

Suppose
\[
P=(Y,S_1,S_2)
\]
is any **proper** two-agent S5 frame and
\[
f:Y\to X
\]
is a surjective bounded morphism from \(P\) onto \(U_m\).

Then
\[
\boxed{|Y|\ge m^2.}
\]

Bjorndahl--Sink's construction gives a proper S5 cover of \(U_m\) with exactly
\[
m^2
\]
states, so the lower bound is attained.

Consequently:
\[
\boxed{
\min\{
|Y|:
Y\text{ is a proper two-agent S5 bounded-morphic cover of }U_m
\}
=
m^2.
}
\]

Hence the quadratic state blow-up of the general finite properization procedure is worst-case sharp already in the simplest maximally uninformative two-agent epistemic frames.

## Assumptions and scope

A two-agent frame
\[
(Y,S_1,S_2)
\]
is called proper when there are no distinct points \(y,z\in Y\) such that
\[
yS_1z
\quad\text{and}\quad
yS_2z.
\]
When \(S_1,S_2\) are equivalence relations, this is equivalent to saying that the intersection of every \(S_1\)-equivalence class with every \(S_2\)-equivalence class has size at most one.

A bounded morphism
\[
f:(Y,S_i)\to(X,R_i)
\]
satisfies the usual forth and back conditions. Only the back condition is needed for the lower bound.

The theorem concerns **proper S5 covers**: both source relations are equivalence relations. It does not claim that \(m^2\) states are necessary if one allows arbitrary non-S5 source relations.

The target frame \(U_m\) has two agents and both target relations are universal. The theorem therefore establishes a worst-case lower bound for the general properization theorem, not a lower bound for every \(m\)-state epistemic frame.

Valuations play no role in the counting argument. Any valuation on \(U_m\) can be pulled back along the bounded morphism.

## Proof

Fix
\[
m\ge1
\]
and let
\[
U_m=(X,X\times X,X\times X),
\qquad
|X|=m.
\]

Let
\[
P=(Y,S_1,S_2)
\]
be a proper two-agent S5 frame and let
\[
f:Y\to X
\]
be a surjective bounded morphism.

We first show that every equivalence class of either \(S_1\) or \(S_2\) contains at least \(m\) points.

Fix
\[
i\in\{1,2\}
\]
and
\[
y\in Y.
\]
Let
\[
C=[y]_{S_i}.
\]

Take any target world
\[
x\in X.
\]
Because the target relation \(R_i=X\times X\) is universal,
\[
f(y)R_i x.
\]
By the bounded-morphism back condition, there exists
\[
z\in Y
\]
such that
\[
yS_i z
\quad\text{and}\quad
f(z)=x.
\]
Thus
\[
z\in C.
\]

Since \(x\in X\) was arbitrary,
\[
f[C]=X.
\]
Therefore
\[
|C|\ge|X|=m.
\]

Now fix one \(S_1\)-equivalence class
\[
C\subseteq Y.
\]
We have
\[
|C|\ge m.
\]

Distinct points of \(C\) must belong to distinct \(S_2\)-equivalence classes. Indeed, suppose
\[
y,z\in C
\]
and \(y\ne z\). Since \(C\) is an \(S_1\)-class,
\[
yS_1z.
\]
If \(y,z\) also belonged to the same \(S_2\)-class, then
\[
yS_2z,
\]
contradicting properness.

Hence the points of \(C\) meet at least
\[
|C|
\]
different \(S_2\)-equivalence classes.

Every one of those \(S_2\)-classes has at least \(m\) points by the first part of the proof, and distinct equivalence classes are disjoint. Therefore
\[
|Y|
\ge
|C|\,m
\ge
m^2.
\]

This proves the lower bound.

For the matching upper bound, apply the finite construction of Bjorndahl and Sink to \(U_m\). Its carrier is
\[
X\times X,
\]
so it has exactly
\[
m^2
\]
states. Their Proposition 2.2 proves that the new frame is proper, and Proposition 2.3 proves that first-coordinate projection is a surjective bounded morphism onto the original frame. Their final preservation observation shows that equivalence relations remain equivalence relations under the construction.

Thus the constructed frame is a proper two-agent S5 cover of \(U_m\) of size exactly
\[
m^2.
\]

Combining the lower and upper bounds gives the exact minimum.

## Verification

The bundled checker reconstructs the Bjorndahl--Sink finite cover of the universal two-agent frame.

For each
\[
1\le m\le20,
\]
it builds
\[
Y=\{0,\ldots,m-1\}^2.
\]

The second relation partitions \(Y\) by the second coordinate. The first relation partitions \(Y\) by the residue
\[
k-j\pmod m.
\]
Because the target relations are universal, both source relations are complete inside their partition blocks.

The checker verifies:

\[
|Y|=m^2;
\]

both source relations are equivalence relations;

every intersection of a first-agent class and a second-agent class is a singleton, hence the frame is proper;

first-coordinate projection is surjective;

the forth and back conditions hold for both agents;

and every equivalence class has exactly \(m\) states and projects bijectively onto the \(m\)-state target.

It also checks the lower-bound counting inequalities for all
\[
1\le m\le100.
\]

The computation corroborates the explicit equality construction. The arbitrary-\(m\) lower bound itself is the direct equivalence-class argument above.

## Relationship to prior work

Bjorndahl--Sink's 2025 note was written to remove the properness restriction that appears repeatedly in simplicial semantics. In the finite case, they construct a model on \(X\times X\), prove properness, prove that first-coordinate projection is a surjective bounded morphism, and observe that reflexivity, symmetry, transitivity, seriality, and Euclideanness are preserved. For S5 relations, this preserves equivalence relations.

The paper does not discuss whether the \(m^2\)-state construction is size-optimal.

The later paper *Belief in Simplicial Complexes* reuses the same properization mechanism as a semantic bridge from relational to simplicial models. It explicitly illustrates the phenomenon by replacing a three-world non-proper relational model with a nine-world proper model before passing to simplicial semantics. That application makes the size of properization mathematically relevant, but it likewise does not provide a lower bound.

The present theorem identifies a sharp obstruction: when two agents both have universal S5 accessibility, every equivalence class in a bounded-morphic cover must still see all \(m\) target worlds, while properness forces the two equivalence partitions to intersect in at most one point. These two requirements alone force a square grid of at least
\[
m\times m
\]
states.

Targeted searches for optimal proper covers, quadratic lower bounds, bounded-morphic properization size, and minimum-size proper S5 covers did not locate an equivalent theorem.

## Limitations

The lower bound uses two equivalence relations essentially. If source relations are allowed to leave S5, smaller proper bounded-morphic covers may exist.

The theorem proves a worst-case bound using the universal two-agent S5 frame. It does not classify the minimum proper-cover size of an arbitrary finite epistemic frame.

For three or more agents, properness constrains the intersection of all agent classes rather than every pairwise intersection, so a different extremal problem arises.

The result concerns state count only. It does not optimize the number of accessibility edges, simplicial vertices, or facets produced after translating the proper frame to a simplicial model.

## References

[1] Adam Bjorndahl and Philip Sink, “A Note on Proper Relational Structures,” arXiv:2506.17142, first posted 20 June 2025.

[2] Philip Sink and Adam Bjorndahl, “Belief in Simplicial Complexes,” arXiv:2512.14647, first posted 16 December 2025.

[3] Patrick Blackburn, Maarten de Rijke, and Yde Venema, *Modal Logic*, Cambridge Tracts in Theoretical Computer Science 53, Cambridge University Press, 2001.
