# Three-limited packings of squared cycles: a rational census and five-residue optimum laws

## Finding
For every integer \(n\ge5\), let \(G_n=C_n^2\) be the simple graph on \(\mathbb Z/n\mathbb Z\) in which distinct vertices are adjacent exactly when their cyclic distance is at most two. Let \(p_{n,k}\) count the \(k\)-vertex subsets \(S\) satisfying \(|S\cap N_{G_n}[v]|\le3\) for every vertex \(v\). Put \(d=3n-5k\).

Define polynomials
\[
D(t,u)=1-tu^3-t^2u-t^4u^2-2t^5+t^7u+t^{10},
\]
\[
N(t,u)=tu^3+2t^2u+4t^4u^2+10t^5-7t^7u-10t^{10}.
\]
Then the **complete labelled-subset enumeration**, with all sizes retained, is
\[
p_{n,k}=[t^nu^{3n-5k}]\frac{N(t,u)}{D(t,u)}\qquad (n\ge5,\ 0\le k\le n).
\]
In particular,
\[
L_3(C_n^2)=\left\lfloor\frac{3n}{5}\right\rfloor.
\]
The number \(A_n=p_{n,\lfloor3n/5\rfloor}\) of maximum packings has the following exact five-residue law. For \(n=5q+r\) with \(q\ge1\) and \(0\le r\le4\):
\[
A_{5q+r}=\begin{cases}
10, & r=0,\\
(5q+1)(q+1)(2q+3)/3, & r=1,\\
5q+2, & r=2,\\
(5q+3)(q+1)(q+2)(7q+12)/24, & r=3,\\
3(5q+4)(q+1)/2, & r=4.
\end{cases}
\]
Counts concern indexed vertices, with no quotient by rotations or reflections. The complete enumeration includes the empty packing.

## Assumptions and scope
The power \(C_n^2\) is the simple second graph power and does not mean a Cartesian product. The five vertices \(v-2,v-1,v,v+1,v+2\) are distinct for \(n\ge5\) and constitute the closed neighborhood of \(v\). Only this closed-neighborhood, at-most-three notion is asserted, not an open-neighborhood or total-limited variant. All coefficients in the theorem are exact integers.

## Proof
Encode a subset by an indexed circular binary word \(x_0,\ldots,x_{n-1}\). It is admissible exactly when each length-five window contains at most three ones. Summing window sizes gives \(5k\le3n\). Its nonnegative *window deficit* is
\[
\sum_{i=0}^{n-1}\left(3-\sum_{j=0}^{4}x_{i+j}\right)=3n-5k.
\]
All indices here are modulo \(n\).

Construct the explicit sixteen-state directed weighted graph whose states are four-bit words \(a=(a_0,a_1,a_2,a_3)\). For a bit \(b\in\{0,1\}\), put \(w=a_0+a_1+a_2+a_3+b\). If \(w\le3\), a transition \(a\to(a_1,a_2,a_3,b)\) has weight \(u^{3-w}\); otherwise there is no transition. Write \(M(u)\) for this sixteen-by-sixteen matrix, adding weights if transitions coincide. Overlapping four-bit states give a bijection between indexed length-\(n\) admissible circular words and closed directed walks of length \(n\). Thus
\[
\operatorname{tr}(M(u)^n)=\sum_{k=0}^n p_{n,k}u^{3n-5k}\qquad(n\ge5).
\]
As a formal power series,
\[
\sum_{n\ge1}t^n\operatorname{tr}(M(u)^n)=-t\frac{\partial}{\partial t}\log\det(I-tM(u)).
\]
The *finite exact determinant identity* is
\[
\det(I-tM(u))=D(t,u).
\]
This equality is certified using exact integer Bareiss determinants: both sides have degree at most sixteen in \(t\) and at most forty-eight in \(u\); the 833 evaluations on the entire Cartesian grid \(t=0,1,\ldots,16\), \(u=0,1,\ldots,48\) agree. Successive univariate interpolation proves equality in \(\mathbb Q[t,u]\), not merely numerical agreement on selected instances. `verify_determinant.py` specifies every state, weight, grid point and exact determinant computation.

Since \(-t\partial_tD=N\), the coefficient-extraction identity follows. For the optimum, write \(z=t^5\) and factor
\[
D=(1-z)^2\left(1-\frac{t^2}{1-z}u-\frac{t^4}{(1-z)^2}u^2-\frac{t}{(1-z)^2}u^3\right).
\]
The first five coefficients of \(-\log D\), with respect to the deficit variable \(u\), are
\[
[u^0](-\log D)=-2\log(1-z),\qquad
[u^1](-\log D)=\frac{t^2}{1-z},
\]
\[
[u^2](-\log D)=\frac{3t^4}{2(1-z)^2},\qquad
[u^3](-\log D)=\frac{t}{(1-z)^2}+\frac{4t^6}{3(1-z)^3},
\]
\[
[u^4](-\log D)=\frac{t^3}{(1-z)^3}+\frac{7t^8}{4(1-z)^4}.
\]
For \(n=5q+r\), the smallest admissible deficit is \(3r\bmod5\), namely \(0,3,1,4,2\) for \(r=0,1,2,3,4\). Coefficient extraction after multiplying these displayed expressions by \(t\partial_t\) gives exactly the five formulas for \(A_n\). Every value is positive for \(q\ge1\), so the original \(5k\le3n\) bound is attained. This proves both the maximum and the complete multiplicity law for all \(n\ge5\).

## Verification
Three self-contained programs provide a reproducible finite proof step and independent checks. `verify_determinant.py` evaluates all 833 determinants with Python integer arithmetic, establishing the bivariate identity by degree bounds. `verify_recurrence.py` expands the rational function through \(n=80\), checks nonnegativity, the maximum size, and all residue formulas. `verify_direct.cpp` enumerates all \(2^n\) indexed subsets for every \(5\le n\le18\), testing each five-neighborhood independently. Its complete outputs for these fourteen orders agree term-for-term with the recurrence output. See the three matching `.txt` output artifacts. Finite exhaustive checks corroborate the symbolic argument; the all-order conclusion is from the transfer identity and exact coefficient extraction, not from finite extrapolation.

## Relationship to prior work
The 2023 work of Ahmadi, Soltankhah and Samadi develops limited-packing partitions and duality, emphasizing capacity two and trees. The 2024 paper of Ahmadi and Soltankhah studies open-neighborhood total limited packings, capacity-two products and partition bounds; its result statements do not give these closed-neighborhood five-window enumerators. The complement of a three-limited packing in this 4-regular graph is a double (two-tuple) dominating set, so the theorem equivalently gives the complete double-domination census of \(C_n^2\) after reversing cardinalities. General transfer-matrix and formal-logarithm identities are standard methods, not claimed as new. The claimed addition is this explicit small rational denominator, all-size coefficient identity and five-residue optimum census for the specified graph family. Related cycle-power, regular-set, and open-packing findings concern distinct properties and do not imply this census.

## Limitations
The results require \(n\ge5\), the simple square of a cycle, and capacity three on closed neighborhoods. Nothing is asserted for other graph powers, capacities, open neighborhoods, or the inclusion-maximal (as opposed to maximum-cardinality) set polynomial. The search for historical priority is necessarily incomplete; no independent external validation has been performed.

## References
1. A. S. Ahmadi, N. Soltankhah and B. Samadi, *Limited packings: related vertex partitions and duality issues*, first posted 2023-08-31, arXiv:2308.16837, https://arxiv.org/abs/2308.16837.
2. A. S. Ahmadi and N. Soltankhah, *On k-(total) limited packing in graphs*, first posted 2024-05-06, arXiv:2405.03237, https://arxiv.org/abs/2405.03237.
3. R. Gallant, G. Gunther, B. L. Hartnell and D. F. Rall, *Limited packing in graphs*, Discrete Applied Mathematics 158 (2010), 1357–1364 (definition and historical context).
