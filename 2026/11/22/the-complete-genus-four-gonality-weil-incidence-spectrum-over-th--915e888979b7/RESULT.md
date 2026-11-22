# The complete genus-four gonality–Weil incidence spectrum over the binary field

## Finding

Let \(\mathcal C_4(\mathbb F_2)\) be the set of \(\mathbb F_2\)-isomorphism classes of smooth, projective, geometrically connected curves of genus four. For a Jacobian \(\mathbb F_2\)-isogeny class \(W\) represented by such a curve, define its *gonality support* by
\[
G(W)=\{\operatorname{gon}_{\mathbb F_2}(C):[C]\in\mathcal C_4(\mathbb F_2),\ [J(C)]_{\rm isog}=W\}.
\]
The complete incidence distribution is

| \(G(W)\) | Number of Jacobian isogeny classes |
|---|---:|
| \(\{2\}\) | 99 |
| \(\{3\}\) | 230 |
| \(\{4\}\) | 112 |
| \(\{5\}\) | 1 |
| \(\{2,3\}\) | 68 |
| \(\{2,4\}\) | 29 |
| \(\{3,4\}\) | 60 |
| \(\{2,3,4\}\) | 21 |

Consequently, **178 of the 620 Jacobian isogeny classes contain curves of different ground-field gonalities**, and **21 classes contain curves of three different gonalities**. Across the 1,044 curve isomorphism classes, the numbers with gonalities \(2,3,4,5\) are respectively \(264,526,253,1\). These are numbers of abstract curves, not coefficient-marked equations. The existence of nonisogenous curves with equal gonality, or of isogenous curves with unequal gonality, is not itself claimed as new.

## Assumptions and scope

All curves and morphisms are defined over \(\mathbb F_2\); gonality always means the minimum degree of a nonconstant morphism to \(\mathbb P^1_{\mathbb F_2}\), not geometric gonality. Isogeny is over \(\mathbb F_2\), and the precise equivalence relation on curves is \(\mathbb F_2\)-isomorphism. The classified universe is all genus-four curves over this field, using the published exhaustive 2020 census of Xarles, and the published ground-field gonality criterion of Faber–Grantham–Howe. The primary published census groups curves into 620 Jacobian Weil classes with four extension-field point counts each. The supporting compact certificate retains, in their source order, those first two counts and the number of hyperelliptic, nonsplit-quadric, cone-quadric, and split-quadric models in each class.

## Proof

**Geometric gonality rule.** A hyperelliptic genus-four curve has gonality two. For every nonhyperelliptic genus-four curve, its canonical model is the smooth complete intersection of a unique quadric \(Q\) and a cubic in \(\mathbb P^3\). A degree-three pencil is equivalent to a ground-field ruling of \(Q\): its degree-three fibers are canonical hyperplane sections minus a moving residual point, and their spans sweep one of the ruling families. Conversely, projection along a rational ruling of \(Q\) restricts to a degree-three map. The three quadric forms occurring in the census have the following arithmetic rulings:
\[
\begin{aligned}
Q_{\rm split}&:XY+ZT=0 &&\text{(two rational rulings)},\\
Q_{\rm cone}&:XY+T^2=0 &&\text{(one rational ruling)},\\
Q_{\rm nonsplit}&:X^2+XY+Y^2+ZT=0 &&\text{(no rational ruling)}.
\end{aligned}
\]
Because the canonical curve is smooth, it avoids the cone vertex; thus a cone ruling gives a base-point-free map. Therefore split-quadric and cone-quadric members have ground-field gonality three, while nonsplit-quadric members have gonality at least four.

**The nonsplit boundary.** For genus four, the Riemann–Roch criterion of Faber–Grantham–Howe states that a curve admits a degree-four map to \(\mathbb P^1\) if and only if it possesses a rational effective divisor of degree two. Such a divisor exists exactly when the curve has an \(\mathbb F_2\)-point or an \(\mathbb F_4\)-point: in the first case take twice the rational point; otherwise the Frobenius orbit of a quadratic point. For a nonsplit-quadric curve, this characterizes gonality four, because it already has no degree-two or degree-three map. If both point counts vanish, gonality exceeds four and is five by the finite-field Schmidt bound \(\operatorname{gon}(C)\leq g+1=5\). This is a conclusion about actual rational morphisms, not merely the existence of abstract linear systems. In the complete original list, exactly one nonsplit-quadric curve has both point counts zero. Its Weil-class record is first in the published order and has the extension count tuple \((0,0,0,4)\). The other two curves in the same point-count category have cone or split quadrics and hence gonality three.

**Exhaustive finite reduction.** Xarles's complete source consists of aligned lists indexed by the 620 distinct Weil polynomials: a four-entry point-count vector, a list of hyperelliptic representatives, and a list of pairs of canonical quadric and cubic equations. Reading all entries (and not merely their existence flags) gives, respectively, 264 hyperelliptic, 254 nonsplit-quadric, 274 cone-quadric, and 252 split-quadric curves. The preceding geometry maps these to \(264,253,274+252,1\) in gonalities \(2,4,3,5\). For each of the 620 ordered Weil classes, form the set of nonzero gonality-count categories. Tallying these sets yields the eight values in the table, totaling exactly 620. The executable `verify_gonality_census.py` checks all 620 entries of `weil_gonality_certificate.hex`, confirms independent published one-field point-count subtotals, and recomputes all eight incidence categories. Its optional second input verifies every compact record against the original published Magma text.

**A concrete three-gonality Weil class.** At published Weil-class index 67 (zero-based), the hyperelliptic curve
\[
H:\quad y^2+(x^3+x+1)y=x^9+x+1
\]
shares its Weil polynomial with both canonical curves \(C_3\) and \(C_4\) defined respectively by
\[
\begin{aligned}
C_3:\quad &XY+T^2=0,\\
&X^3+X^2Y+Y^3+X^2Z+XYZ+Z^3+X^2T+XYT+XZT=0;
\end{aligned}
\]
\[
\begin{aligned}
C_4:\quad &X^2+XY+Y^2+ZT=0,\\
&X^3+X^2Y+Y^3+X^2Z+Y^2Z+XZ^2+Z^3+XYT+XT^2=0.
\end{aligned}
\]
Their gonalities are \(2\), \(3\), and \(4\), respectively. The attached independent finite-field enumerator checks all three have exactly \((1,5,10,17)\) points over extension degrees \(1,2,3,4\). By the genus-four functional equation, these four counts determine the same complete Hasse–Weil numerator
\[
L(T)=1-2T+2T^2-T^3-2T^5+8T^6-16T^7+16T^8.
\]
Tate's finite-field isogeny theorem identifies their Jacobian isogeny class. Thus a *single* arithmetic isogeny class realizes all three possible non-excessive gonalities over \(\mathbb F_2\).

## Verification

Run `python3 verify_gonality_census.py weil_gonality_certificate.hex` and `python3 verify_explicit_witness.py` from the same directory. The first script checks 620 source-indexed records, total curve and quadric counts, the point-count census, the unique nonsplit zero-point boundary and the entire gonality–Weil incidence spectrum. The second independently enumerates projective points of the two canonical models and affine points plus the unique point at infinity of the hyperelliptic model, in extensions of degrees one through four, using explicit irreducible field polynomials. Both checks completed successfully. The optional source-to-certificate comparison accepts a lawfully obtained original Magma data text as the second argument to the first script. The provided certificate is a compact derived table, not a republication of the original equations.

## Relationship to prior work

Xarles (2020) established the exhaustive 1,044-curve census and 620 Jacobian isogeny classes, including the raw canonical-quadric models and extension point counts. His published tables classify numbers of curves by point counts and include specific shared-isogeny examples, including two Weil classes containing hyperelliptic curves and curves on all three quadric types (Section 4, Example 18). They do not tabulate the complete *gonality support* of every isogeny class. Faber–Grantham–Howe (first released 2022) provide the genus-four effective-divisor gonality criterion and the classification of excessive curves; in their Question 1.4 they specifically ask whether zeta functions determine gonality and exhibit counterexamples. Hence the existence of counterexamples and the single binary-field excessive curve are prior work. The asserted additional fact is the *complete eight-bin joint incidence classification*, showing exactly 178 mixed classes and 21 triple-gonality classes, with a directly checked triple witness. Related studies of binary split-quadric and nonsplit-quadric geometry concern restricted loci and different invariants.

## Limitations

The exhaustive step inherits the completeness and isomorphism/Weil-grouping correctness of Xarles's underlying primary enumeration; this note does not independently re-enumerate all curves. The compact certificate verifies a numerical projection of that source, not the uniqueness of all original curve equations. The three explicit witnesses have independent point counts, but no separate formal smoothness certificate is supplied beyond their inclusion in the primary exhaustive smooth-curve census. Searches cannot establish global historical priority, and unindexed exact joint counts could predate this report. No extension of these counts to other base fields or higher genera is asserted.

## References

- Xavier Xarles, *A census of all genus 4 curves over the field with 2 elements*, arXiv:2007.07822, first public 2020-07-15; Theorem 10, Section 3 and source census. https://arxiv.org/html/2007.07822v1
- Xander Faber, Jon Grantham and Everett W. Howe, *On the Maximum Gonality of a Curve over a Finite Field*, arXiv:2207.14307, first public 2022-07-28; Question 1.4, Lemma 2.1 and Theorem 1.1. https://arxiv.org/html/2207.14307v2
- Xavier Xarles, primary supplementary genus-four census. https://github.com/XavierXarles/Censusforgenus4curvesoverF2
- Accessible mirror of the original three aligned lists: https://github.com/kedlaya/same-class-number/blob/main/Shared/ListCurvesGenus4p2.txt
