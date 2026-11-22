# Frobenius splitting of 52 bitangent contacts on six octahedral quartics over \(\mathbb F_9\)

## Finding
Let \(k=\mathbb F_9=\mathbb F_3(i)\), where \(i^2=-1\), and consider the characteristic-three smooth quartics
\[
C_\lambda:\quad Y^4-X^3Z-XZ^3-\lambda(Y^2-2XZ)^2=0,
\qquad \lambda=a+bi,\quad a\in\mathbb F_3,\ b\in\mathbb F_3^\times.
\]
These are all six non-Hermitian, nonexceptional rational parameters of this pencil over the first quadratic extension of \(\mathbb F_3\). Their geometric 28 bitangents have exactly four hyperflex lines, and the remaining 24 lines have two distinct contacts each. Consequently the reduced bitangent-contact support \(S_\lambda\) has 52 points. Its **entire Frobenius permutation** is:

| \(a\) | \(b\) | Frobenius cycles on 52 contacts | Bitangents over \(k\) | Rational bitangents with nonsplit contact pair |
|:---:|:---:|:---:|---:|---:|
| 0 | 1 or 2 | \(1^4 2^{24}\) | 4 | 0 |
| 1 | 1 or 2 | \(1^4 2^{12}4^6\) | 4 | 0 |
| 2 | 1 or 2 | \(1^4 2^{24}\) | 16 | 12 |

The exact Hasse–Weil zeta function of this **finite reduced point scheme** (not of the quartic curve) is
\[
Z(S_\lambda/k,T)=
\begin{cases}
(1-T)^{-4}(1-T^2)^{-24},&a\in\{0,2\},\\
(1-T)^{-4}(1-T^2)^{-12}(1-T^4)^{-6},&a=1.
\end{cases}
\]
All 28 bitangent lines are defined over \(\mathbb F_{81}\), but when \(a=1\) the 24 contacts belonging to the twelve nonsplit contact pairs over \(\mathbb F_{81}\) first become rational over \(\mathbb F_{6561}=\mathbb F_{9^4}\). The contact splitting therefore distinguishes quartics beyond the field of definition of their bitangent **lines**.

## Assumptions and scope
The ground field is \(k=\mathbb F_9\). The parameter \(\lambda\notin\mathbb F_3=\{0,1,-1\}\) ensures smoothness by the nonsingularity criterion for this pencil. A geometric bitangent line is a line whose intersection with the smooth plane quartic is twice a degree-two effective divisor; a hyperflex has one contact of multiplicity four. The **contact support** is the set of geometric tangency points with reduced scheme structure, not the length-56 nonreduced contact divisor. The uniqueness of the tangent to a smooth curve ensures that contacts from distinct bitangent lines cannot coincide. Arithmetic Frobenius is \(x\mapsto x^9\).

## Proof
The originating invariant-pencil smoothness criterion and unique-contact-line theorem (Borges–Korchmáros–Speziali, Lemma 4.23) imply smoothness and show that the four tangents to the invariant conic at its \(\mathbb F_3\)-points are hyperflexes. The explicit exhaustive calculation below proves that these are the only hyperflexes and classifies the remaining geometric contact points.

First, expanding in characteristic three gives
\[
F_\lambda=(1-\lambda)Y^4+\lambda XZY^2-\lambda X^2Z^2-X^3Z-XZ^3.
\]
Every projective line is uniquely either \(Z=uX+vY\), \(Y=tX\), or \(X=0\). On \(Y=tX\), the restricted quartic has coefficient \(-1\) at \(XZ^3\) and zero at \(Z^4\), so it cannot be a square of a quadratic: a quadratic with zero \(Z^4\)-square coefficient has no \(Z^2\)-term, hence its square has zero \(XZ^3\)-coefficient. On \(X=0\), the section is \((1-\lambda)Y^4\), a rational hyperflex.

For \(L_{u,v}:Z=uX+vY\), the restricted binary quartic is
\[
A X^4+B X^3Y+C X^2Y^2+D XY^3+E Y^4,
\]
with coefficients in the ground field or any extension:
\[
\begin{aligned}
&A=-\lambda u^2-u-u^3,&&B=\lambda uv-v,\\
&C=\lambda(u-v^2),&&D=\lambda v-v^3,&&E=1-\lambda\ne0.
\end{aligned}
\]
Write \(K=2(EC-D^2)\), working in characteristic three. Comparing all five coefficients with \(E(Y^2+\eta XY+\theta X^2)^2\) proves the **necessary and sufficient** bitangency criterion
\[
E^2B=DK,\qquad E^3A=K^2,\qquad
\eta=\frac{2D}{E},\quad \theta=\frac{K}{E^2}.
\]
Its reduced geometric contact divisor has one support exactly when \(\delta=\eta^2-\theta=0\), and otherwise two distinct supports. Over a finite field of characteristic three the two contacts are individually rational if and only if the nonzero discriminant \(\delta\) is a square.

For full reproducibility, represent \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\) and \(\mathbb F_{81}=\mathbb F_3[t]/(t^4+t^3+t^2+1)\). In each field choose either root of \(i^2=-1\); changing the root simply exchanges \(b=1\) and \(b=2\). Enumerate all \(q^2\) pairs \((u,v)\) for each parameter, applying the two coefficient identities and the discriminant test, then include \(X=0\). This is a finite exhaustive proof, not a sample or a heuristic. It yields the following numbers of (hyperflex, split two-contact, nonsplit two-contact) bitangent lines:
\[
\begin{array}{c|cc}
a&\mathbb F_9&\mathbb F_{81}\\\hline
0&(4,0,0)&(4,24,0)\\
1&(4,0,0)&(4,12,12)\\
2&(4,0,12)&(4,24,0)
\end{array}
\]
for both \(b\). The full finite-field arithmetic and complete loops are in `verify_bks_contacts.py`, including direct reconstruction of all five coefficients of every accepted square.

There are 28 bitangents over \(\mathbb F_{81}\) for every parameter. Since a smooth plane quartic in characteristic different from two has exactly 28 distinct geometric bitangents, the enumeration is **geometrically complete**. Its four hyperflexes and 24 ordinary bitangents give 52 distinct reduced contact supports. For \(a=0\) or \(2\), all 52 contacts are defined over \(\mathbb F_{81}\), exactly four over \(\mathbb F_9\), hence Frobenius cycle type \(1^4 2^{24}\). For \(a=1\), exactly 12 nonhyperflex bitangents have both contacts defined over \(\mathbb F_{81}\); the other 12 have their conjugate contacts in \(\mathbb F_{81^2}\). Since all 28 bitangent lines are defined over \(\mathbb F_{81}\), Frobenius squared exchanges the two contacts of each nonsplit line, producing six 4-cycles on those 24 points. The remaining 24 ordinary contacts form twelve 2-cycles and the four hyperflexes are fixed. This proves the listed partitions and finite-scheme zeta functions.

## Verification
The self-contained, dependency-free Python 3 program `verify_bks_contacts.py` constructs finite fields by exact polynomial residues and exhaustively inspects every rational projective line over \(\mathbb F_9\) and \(\mathbb F_{81}\), for every one of the six parameters. It tests both necessary-and-sufficient square identities, recomposes the resulting binary-quartic coefficients, and classifies the contact quadratic discriminant. Its successful terminal output is `BKS_CONTACT_FROBENIUS_CLASSIFICATION_PASS`. The enumeration checks all 91 rational projective lines per parameter over \(\mathbb F_9\) and all 6,643 per parameter over \(\mathbb F_{81}\); no random sampling or interpolation is used.

## Relationship to prior work
Borges–Korchmáros–Speziali determine this invariant pencil, its geometric smoothness and its four distinguished hyperflexes; these are not newly claimed. Auer–Top identify elliptic-cube Jacobian decompositions for octahedral quartics; the quartics' isogeny spectra are not the present claim. Janasz–Pokora–Zieliński and Bethea–Brazelton study the geometric Ciani/octahedral bitangent arrangements and their symmetry-orbits. Existing finite-field results on the **rational bitangent-line** census of the Ciani pencil show only the possible counts 4, 16, and 28; they do not provide the field-of-definition partition of the 52 distinct **contact supports**. The published finite-field contact census for the larger Ciani family addresses \(\mathbb F_5\), rather than these \(\mathbb F_9\) members. The new determination is the full Frobenius splitting of this intrinsic finite 52-point scheme on the six natural small-extension members.

## Limitations
This classification concerns the six given coefficient-marked \(\mathbb F_9\) members, not the complete pencil over every extension and not a moduli-classification statement. Neither the classical 28-bitangent count nor the already known line-descent criteria are independent novelty claims. The proof uses an exhaustive *finite* calculation for exactly these six parameters over the two specified finite fields, together with the classical bound of 28 geometric bitangents; it is not an assertion obtained by extrapolating numerical samples. Historical or unindexed equivalent contact arithmetic remains possible. No independent external mathematical validation is asserted.

## References
- H. Borges, G. Korchmáros, P. Speziali, *Plane curves with a large linear automorphism group in characteristic p*, arXiv:2202.05765v1 (first public 2022-02-11), §4.8, Lemma 4.23, https://arxiv.org/abs/2202.05765.
- R. Auer, J. Top, *Some genus 3 curves with many points*, arXiv:math/0201320v1, §1.2, https://arxiv.org/abs/math/0201320.
- M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, §3, https://arxiv.org/abs/2308.16514.
- C. Bethea, T. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242, §4.4, https://arxiv.org/abs/2410.09242.
- *Quadratic Frobenius splitting and an exact rational-bitangent census for Ciani's quartic pencil*, published record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-quadratic-frobenius-splitting-and-an-exact-rational-bitangent-ce--94af6b732234.
- *Rational bitangent-contact spectrum of smooth Ciani quartics over \(\mathbb F_5\)*, published record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-rational-bitangent-contact-spectrum-of-smooth-ciani-quartics-ove--86374f95f5d5.
