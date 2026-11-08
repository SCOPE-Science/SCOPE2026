# Sharp log-concavity transition in a Gorenstein Cayley family

## Finding
For each positive integer \(m\), construct the \((6m+3)\)-dimensional lattice polytope \(R_m\) by the Cayley construction in the next section. Write \(h_m^*(z)=\sum_{j=0}^{6m}h_{m,j}^*z^j\) for its Ehrhart numerator. Then
\[
\boxed{\ h_m^*\text{ is strictly log-concave exactly when }1\le m\le11.\ }
\]
More precisely, for every \(m\ge12\), \((h_{m,2}^*)^2<h_{m,1}^*h_{m,3}^*\); for every \(1\le m\le11\), all \(6m-1\) internal adjacent-minor inequalities are strict. The first non-log-concave member of this canonical one-parameter family therefore occurs at dimension \(75\). Each member is Gorenstein of index four and admits a regular unimodular flag triangulation.

## Assumptions and scope
Let \(e_0,e_1,e_2,e_3\) be the standard coordinate vectors in \(\mathbb Z^4\). Form the \(6m\times4\) nonnegative integer matrix \(A_m\) with \(m\) copies of each of the six rows \(e_0+e_i\) and \(2e_i\), for \(i=1,2,3\). For each column \(j\), let \(D_j\subset\mathbb R^{6m}\) be the coordinate box with side lengths given by that column, and put
\[
R_m=\operatorname{conv}\left((D_0\times\{0\})\cup\bigcup_{j=1}^3(D_j\times\{e_j\})\right)\subset\mathbb R^{6m+3}.
\]
The ambient lattice is the standard integer lattice. The Ehrhart numerator is defined by
\[\sum_{k\ge0}|kR_m\cap\mathbb Z^{6m+3}|z^k=\frac{h_m^*(z)}{(1-z)^{6m+4}}.\]
Strict log-concavity means \((h_{m,j}^*)^2>h_{m,j-1}^*h_{m,j+1}^*\) for all integers \(1\le j<6m\). The proof uses the known Gorenstein symmetry of this concrete family to reduce the finite verification to one half of its numerator.

## Proof
**1. Exact coefficients and symmetry.** The lattice-point counting formula is obtained by choosing nonnegative barycentric integers \(b_0,b_1,b_2,b_3\) summing to \(k\), then independently counting the fiber coordinates:
\[
E_m(k):=|kR_m\cap\mathbb Z^{6m+3}|=\sum_{b_0+b_1+b_2+b_3=k}\prod_{i=1}^3((b_0+b_i+1)(2b_i+1))^m.\tag{1}
\]
All four summation indices are nonnegative integers. The general Cayley-chimney theorem, or the direct reflexivity argument in the reference, gives index-four Gorensteinness, regular unimodular flag triangulation, and an Ehrhart numerator of degree \(6m\) with nonnegative, palindromic coefficients: \(h_{m,j}^*=h_{m,6m-j}^*\). Writing \(M=6m+4\), the binomial transform of (1) is
\[
h_{m,r}^*=\sum_{k=0}^r(-1)^{r-k}\binom{M}{r-k}E_m(k),\qquad 0\le r\le6m.\tag{2}
\]

**2. All smaller parameters.** For each of the eleven integers \(1\le m\le11\), evaluate (1) and (2) for \(0\le k,r\le3m\). By palindromicity it suffices to check the \(3m\) differences
\[
\delta_{m,j}=(h_{m,j}^*)^2-h_{m,j-1}^*h_{m,j+1}^*,\quad1\le j\le3m,\tag{3}
\]
where at the central index \(j=3m\) the right neighbor is \(h_{m,3m-1}^*\). The complete exact-arithmetic enumeration yields strictly positive values for all these differences. Indeed, the minimum is always attained at \(j=1\); its values for successive \(m=1,\ldots,11\) are
\[
\begin{array}{c|rrrrrr}
m&1&2&3&4&5&6\\\hline
\min_j\delta_{m,j}&183&17788&1010589&52760098&2765430459&148195690504
\end{array}
\]
\[
\begin{array}{c|rrrrr}
m&7&8&9&10&11\\\hline
\min_j\delta_{m,j}&8144441026617&458722736365054&26426960677346631&1553232651166059076&92874673606309040421
\end{array}
\]
These are exact integers, not floating-point estimates. The accompanying standalone finite enumeration implements every composition and every relevant minor in (1)–(3); all loops have explicit finite bounds and establish strict log-concavity for the eleven parameters without an extrapolation.

**3. Every larger parameter.** Put \(a=E_m(1)\), \(b=E_m(2)\), \(c=E_m(3)\). Grouping the compositions in (1) gives
\[
a=8^m+3\cdot6^m,\qquad b=27^m+6\cdot36^m+3\cdot15^m,
\]
\[
c=64^m+3\cdot108^m+3\cdot80^m+3\cdot162^m+3\cdot28^m+6\cdot90^m+216^m.
\tag{4}
\]
Equation (2) yields \(h_1^*=a-M\), \(h_2^*=b-Ma+\binom M2\), and \(h_3^*=c-Mb+\binom M2a-\binom M3\). Hence the failure at index two is equivalent to
\[
Q_m:=h_1^*h_3^*-(h_2^*)^2>0.\tag{5}
\]
The exact integer formulas (4)–(5) give \(Q_m>0\) for each \(12\le m\le20\). In particular,
\[
Q_{12}=33767772755382700161244430421001196588>0.\tag{6}
\]
For all \(m\ge21\), observe that \(a\ge8^m\), \(b\le10\cdot36^m\), and \(c\ge216^m\). Also \(h_2^*\ge0\) (it is an Ehrhart numerator coefficient), \(a\ge(M-2)/3\), and \(a\ge(M-1)/2\). Consequently \(h_2^*\le b\) and \(h_3^*\ge c-Mb\). The elementary integer estimates
\[
8^m\ge2M,\qquad 6^m\ge20M,\qquad4^m>400\cdot3^m\qquad(m\ge21)\tag{7}
\]
hold at \(m=21\) and persist by elementary induction (exponential growth factors exceed the growth of \(M\)). They imply
\[
h_1^*\ge\frac{8^m}{2},\quad h_3^*\ge\frac{216^m}{2},\quad0\le h_2^*\le10\cdot36^m.
\]
Therefore
\[
Q_m\ge\frac{1728^m}{4}-100\cdot1296^m>0\qquad(m\ge21),\tag{8}
\]
the last strict inequality being equivalent to the third estimate in (7). This covers every positive integer \(m\), with no unverified infinite-range inference.

## Verification
Run the standalone standard-library Python certificate using `python3 verify_phase_transition.py`. It independently enumerates the source's compositions at low dilations, checks the closed formulas (4), evaluates all \(3m\) distinct minors for every \(1\le m\le11\), evaluates the obstruction (5) for every \(12\le m\le20\), reproduces the exact value (6), and checks the three integer base cases for the induction (7). All checks passed in the supplied execution. The analytic estimate (8) handles the infinite tail: a finite run is not used as evidence for infinitely many parameters.

## Relationship to prior work
Ferroni, *Unimodality shenanigans in Ehrhart theory*, arXiv:2609.10513, originally posted September 9, 2026, introduces the precise Gorenstein Cayley family \(R_m\), establishes formulas (1), (4), the palindromic structure, and exhibits the non-log-concave member \(R_{12}\) to disprove Brenti's conjecture. The new assertion is the **two-sided complete threshold**: every earlier member has *all* numerator minors positive, and every later member has a negative index-two minor. Neither conclusion follows from the isolated \(m=12\) witness without further proof. The general unimodality theorem for Gorenstein IDP polytopes is strictly weaker than log-concavity and does not imply the positive half of this classification. No claim is made about the minimal dimension among *all* Gorenstein IDP counterexamples.

## Limitations
The sharp index \(m=12\) and dimension \(75\) are optimal **only within the specified one-parameter family**. The finite table is a complete exact enumeration of that finite range, not a classification of arbitrary Cayley matrices, arbitrary Gorenstein polytopes, or all smooth polytopes. The reviewed primary source contains the example at \(m=12\), so the value of the refinement is the exhaustive two-sided regime statement, not a new example at the same parameter. The literature comparison does not constitute independent historical-priority certification.

## References
1. L. Ferroni, *Unimodality shenanigans in Ehrhart theory*, arXiv:2609.10513v2 (first posted 2026-09-09), Sections 2, 3, and 6. https://arxiv.org/html/2609.10513v2
2. K. A. Adiprasito, S. A. Papadakis, V. Petrotou and J. K. Steinmeyer, *Beyond positivity in Ehrhart theory*, arXiv:2210.10734 (2022). https://arxiv.org/abs/2210.10734
3. L. Ferroni and A. Higashitani, *Examples and counterexamples in Ehrhart theory*, EMS Surveys in Mathematical Sciences, DOI 10.4171/EMSS/86 (2024). https://ems.press/journals/emss/articles/14298122
