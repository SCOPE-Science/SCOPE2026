# Exact distance-channel spectra and stochastic ordering over equilateral bases in the forbidden-triangle metric limit

## Finding

Let \(M\) be the countable homogeneous metric structure whose age is all finite metric spaces with positive distances in \(\{1,2,3\}\) omitting triangle patterns \((1,1,1)\) and \((1,2,2)\). The metric triangle inequality also excludes \((1,1,3)\). For \(n\ge2\), let \(A_{\delta,n}\) be a pointwise-named equilateral set of \(n\) vertices of mutual distance \(\delta\in\{2,3\}\). For \(s\in\{1,2,3\}\), let \(N_{\delta,s}(n)\) be the number of complete types of **ordered, distinct** new vertices \((x,y)\), neither a named parameter, for which \(d(x,y)=s\). Then the exact six distance-channel counts are

\[
\begin{aligned}
N_{2,1}(n)&=3\cdot3^n-2\cdot2^n,\\
N_{2,2}(n)&=2\cdot4^n+2\cdot3^n-4\cdot2^n+1,\\
N_{2,3}(n)&=3\cdot4^n+3^n-4\cdot2^n+1,\\
N_{3,1}(n)&=3^{n-2}(n^2+5n+9),\\
N_{3,2}(n)&=4^{n-2}(n^2+11n+16),\\
N_{3,3}(n)&=4^{n-1}(n^2+3n+4).
\end{aligned}
\]

Let \(p_{\delta,s}(n)=N_{\delta,s}(n)/\sum_{j=1}^{3}N_{\delta,j}(n)\) be the probability of channel \(s\) when uniformly sampling **one complete ordered-pair type** over \(A_{\delta,n}\). For every \(n\ge2\) the two distributions are strictly stochastically ordered:

\[
p_{3,1}(n)<p_{2,1}(n),\qquad p_{3,3}(n)>p_{2,3}(n).
\]

Consequently, in the first-order stochastic order, the distribution over a base with distance \(3\) strictly exceeds the distribution over a base with distance \(2\). Their respective limits are

\[
(p_{2,1},p_{2,2},p_{2,3})\longrightarrow(0,2/5,3/5),\qquad
(p_{3,1},p_{3,2},p_{3,3})\longrightarrow(0,1/5,4/5).
\]

The rare short-distance channels obey the sharp exponential equivalents

\[
p_{2,1}(n)\sim\frac35\left(\frac34\right)^n,\qquad
p_{3,1}(n)\sim\frac{16}{45}\left(\frac34\right)^n.
\]

## Assumptions and scope

All spaces are undirected, integer-valued metrics with distinct points at distance \(1\), \(2\), or \(3\). A forbidden triangle is specified by its sorted three distances. The Fraïssé limit \(M\) realizes every finite admissible extension over an embedded finite subspace. Counting complete types over an **individually named** parameter set is therefore exactly counting admissible labelled finite extension diagrams, with fixed order for \((x,y)\). No two new vertices are identified with named points or with each other. An equilateral set of distance \(1\) has at most two points because \((1,1,1)\) is forbidden, whereas arbitrary finite equilateral sets of distances \(2\) and \(3\) exist. Thus these are exactly the two equilateral base families with unbounded size.

For the one-point comparison used in the proof, the numbers of nonalgebraic unary types are respectively \(2^{n+1}-1\) for \(\delta=2\) and \(2^n+n2^{n-1}\) for \(\delta=3\). The theorem does not claim that all finite distance-one/metric graph configurations behave alike, nor that uniform sampling of types is a spatially defined probability measure on \(M\).

## Proof

**Local triangle compatibility.** For any \(s\in\{1,2,3\}\), write \(M_s(a,b)=1\) precisely when the triangle with side lengths \((a,b,s)\) is metric and avoids the two additionally forbidden configurations. Rows and columns in the following matrices run through \(a,b=1,2,3\) in that order:

\[
M_1=\begin{pmatrix}0&1&0\\1&0&1\\0&1&1\end{pmatrix},\quad
M_2=\begin{pmatrix}1&0&1\\0&1&1\\1&1&1\end{pmatrix},\quad
M_3=\begin{pmatrix}0&1&1\\1&1&1\\1&1&1\end{pmatrix}.
\]

A pair of distance vectors \((a_i)_{i=1}^n\), \((b_i)_{i=1}^n\) yields a valid type of channel \(s\) exactly when each vector is compatible with all original pair distances and \(M_s(a_i,b_i)=1\) at every original coordinate. The assumption that forbidden configurations are triangles means these local tests are sufficient for the complete finite diagram.

**Base distance \(2\).** The forbidden \((1,2,2)\) triangle ensures that each one-point vector takes values either only in \(U=\{1,3\}\) or only in \(V=\{2,3\}\); their intersection is \(Z=\{3\}\). Write \(c_s(E,F)\) for the number of allowed entries of \(M_s\) in \(E\times F\). Inclusion-exclusion gives the independent-coordinate identity

\[
N_{2,s}(n)=c_s(U,U)^n+2c_s(U,V)^n+c_s(V,V)^n
-2c_s(U,Z)^n-2c_s(V,Z)^n+c_s(Z,Z)^n.
\]

For \(s=1,2,3\), the six local-count vectors in the displayed order are respectively

\[
(1,3,3,1,2,1),\quad (4,3,4,2,2,1),\quad (3,4,4,2,2,1).
\]

Substitution yields the three formulas for \(N_{2,s}(n)\).

**Base distance \(3\).** The metric inequality forbids two entries equal to \(1\) in the same one-point vector, because \(1+1<3\). Entries \(2\) or \(3\) have no other cross-coordinate restriction. Introduce formal variables \(X,Y\) to mark occurrences of value \(1\) in the first and second new distance vectors. The local compatibility polynomials read directly from the three matrices:

\[
P_1(X,Y)=3+X+Y,\quad
P_2(X,Y)=4+X+Y+XY,\quad
P_3(X,Y)=4+2X+2Y.
\]

Each valid vector uses value \(1\) at most once. Hence

\[
N_{3,s}(n)=\sum_{i,j\in\{0,1\}}[X^iY^j]P_s(X,Y)^n.
\]

Expanding the indicated coefficients yields exactly the three asserted polynomial-exponential formulas. These equalities hold for every \(n\ge2\), without any unbounded finite enumeration assumption.

**Strict stochastic ordering.** Put \(A_i=N_{2,i}(n)\), \(B_i=N_{3,i}(n)\), and \(T_A=\sum_iA_i\), \(T_B=\sum_iB_i\). The exact totals are

\[
T_A=5\cdot4^n+6\cdot3^n-10\cdot2^n+2,\qquad
T_B=3^{n-2}(n^2+5n+9)+4^{n-2}(5n^2+23n+32).
\]

First, \(A_3/T_A<3/5\), because

\[
5A_3-3T_A=-13\cdot3^n+10\cdot2^n-1<0.
\]

Let \(t=(3/4)^n\). For \(n\ge6\), since \(t<1/5\),

\[
\frac{5B_3-3T_B}{4^{n-2}}
=5n^2-9n-16-\frac{16}{3}t(n^2+5n+9)
>\frac{59n^2-215n-384}{15}>0.
\]

Thus \(B_3/T_B>3/5>A_3/T_A\) for \(n\ge6\).

For the other inequality, let \(P=n^2+5n+9\), \(Q=5n^2+23n+32\), \(u=(1/2)^n\), and \(v=4^{-n}\). For \(n\ge2\), \(Q-4P=(n+4)(n-1)>0\), whence

\[
\frac{B_1}{T_B}<\frac{16}{9}\frac P Q t<\frac49t.
\]

For \(n\ge6\), use \(u/t=(2/3)^n\le64/729\), \(t\le729/4096\), and \(v\le1/4096\) to obtain

\[
\frac{A_1}{T_A}=\frac{3t-2u}{5+6t-10u+2v}
\ge\frac{1{,}054{,}208}{2{,}265{,}003}t>\frac49t>\frac{B_1}{T_B}.
\]

For \(n=2,3,4,5\), the exact pairs of positive cross-products \((A_1T_B-B_1T_A,\ B_3T_A-A_3T_B)\) are

\[
(91,294),\ (4399,13804),\ (122919,409350),\ (2663485,9937452).
\]

These establish both strict inequalities for the remaining cases. Because the variable \(s\) has only three ordered values, comparing the lower tail at \(1\) and upper tail at \(3\) is precisely strict first-order stochastic dominance.

**Asymptotics.** The leading bases in the exact formulas are \(4^n\) for \(\delta=2\) and \(n^2 4^{n-2}\) for \(\delta=3\); taking ratios yields the limiting vectors. Keeping the leading \(3^n\) terms in the short channel yields the two displayed sharp equivalents.

## Verification

The included standalone program `check.py` enumerates all valid one-point distance vectors and ordered pairs, directly testing every triangle and every original-base constraint for \(n=1,\ldots,6\) and \(\delta\in\{2,3\}\). It compares complete channel counts with the derived formulas and checks exact cross-product order inequalities for \(n=2,\ldots,200\). Recorded output appears in `checks.txt`. These finite checks independently support the calculations but the unbounded identities and all-size inequalities are proved above.

## Relationship to prior work

Cherlin's *Two problems on homogeneous structures, revisited* describes the primitive diameter-three metric case with the three omitted triangles \((1,1,1),(1,1,3),(1,2,2)\), the middle one being metrically impossible. Amato, Cherlin, and Macpherson's *Metrically homogeneous graphs of diameter three* gives the later classification framework. Both are structural sources rather than the above fixed-base distance-channel enumerations.

The published *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space* develops unary Katětov enumerations for the **unrestricted** generic \(\{1,2,3\}\)-metric space. That is not this forbidden-triangle class and does not imply these six two-point formulas, the two different limiting laws, or their uniform stochastic comparison. Searches for equivalent formulations under metric homogeneous structures, forbidden triangle lists, finite-parameter type spectra and distance-resolved ordered pair orbits found no covering claim, but cannot certify historical priority.

## Limitations

All statements concern only equilateral pointwise-named parameter sets of size at least two, complete types of injective ordered pairs of genuinely new vertices, and this particular constrained Fraïssé class. There is no claim for other finite bases or higher arities. The probability measure is uniform on finitely many logical types, not on points of the infinite structure. A comprehensive priority review of nonindexed older multicoloured-graph enumeration literature has not been completed. Independent validation of this proof has not been performed.

## References

1. Gregory Cherlin, *Two problems on homogeneous structures, revisited*, in *Model Theoretic Methods in Finite Combinatorics*, Contemporary Mathematics 558 (2011), pp. 319–415, DOI:10.1090/conm/558/11055; §10 discusses the omitted triangles. The dated bibliographic record is 2012-03-02. https://janos.cs.technion.ac.il/RESEARCH/AMS-Book-files/pdfs/09_Cherlin.pdf .
2. Daniela Amato, Gregory Cherlin, H. Dugald Macpherson, *Metrically homogeneous graphs of diameter three*, manuscript dated November 2019, journal 2021, DOI:10.1142/S0219061320500208. https://sites.math.rutgers.edu/~cherlin/Paper/diameter3.pdf .
3. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, publicly available mathematical result, 2026; comparison with the unrestricted class. https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989/RESULT.md .
