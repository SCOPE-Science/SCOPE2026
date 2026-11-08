# Complete nil-clean decomposition-fiber distributions for two-dimensional finite-field matrices

## Finding

Let \(k=\mathbb F_q\) be **any** finite field and let
\[
\nu(A)=\#\{P\in M_2(k):P^2=P,\ (A-P)^2=0\}.
\]
Every nilpotent two-by-two matrix is square-zero, so \(\nu(A)\) is the exact number of decompositions of \(A\) as an idempotent plus a nilpotent (with ordered, intrinsically distinguished summands). The theorem gives \(\nu(A)\) for every \(A\) and the complete histogram of these fibers.

Let \(t=\operatorname{tr}(A)\), \(d=\det(A)\) and \(e(A)\) be the number of one-dimensional \(k\)-subspaces invariant under \(A\). Write \(\mathbf1_S\) for the indicator of a condition \(S\), and put
\[
\epsilon_0(A)=\mathbf1_{\{t=0,\ d=0\}},\qquad
\epsilon_1(A)=\mathbf1_{\{t=2,\ d-t+1=0\}}.
\]
Here \(0,1,2\) denote field elements, so the indicators are allowed to have the same trace in characteristic two. Then the **complete prescribed-matrix fiber formula** is
\[
\boxed{\nu(A)=\epsilon_0(A)+\epsilon_1(A)+
\begin{cases}
2q-1,&t=1,\ d=0,\\
q+1-e(A),&t=1,\ d\ne0,\\
0,&t\ne1.
\end{cases}}
\]
In particular, if \(t=1\) and \(d\ne0\), the four possibilities for \(e(A)\) are \(0\) (irreducible quadratic: fiber \(q+1\)), \(1\) (nonscalar repeated eigenvalue: fiber \(q\)), \(2\) (two distinct eigenvalues: fiber \(q-1\)), and \(q+1\) (scalar matrix: fiber zero). These classifications apply with the obvious empty cases in characteristic two.

Define the complete fiber histogram by \(H_q(j)=\#\{A\in M_2(k):\nu(A)=j\}\). For **odd** \(q\), its nonzero entries are

| Fiber \(j\) | Number \(H_q(j)\) |
|:---:|:---:|
| \(0\) | \(q^4-q^3-2q^2+1\) |
| \(1\) | \(2q^2\) |
| \(2q-1\) | \(q(q+1)\) |
| \(q-1\) | \(\frac{q-3}{2}q(q+1)\) |
| \(q+1\) | \(\frac{q-1}{2}q(q-1)\) |
| \(q\) | \(q^2-1\) |

For **even** \(q\), the nonzero contributions are

| Fiber \(j\) | Contribution to \(H_q(j)\) |
|:---:|:---:|
| \(0\) | \(q^4-q^3-2q^2\) |
| \(1\) | \(2q^2\) |
| \(2q-1\) | \(q(q+1)\) |
| \(q-1\) | \((q/2-1)q(q+1)\) |
| \(q+1\) | \((q/2)q(q-1)\) |

**At \(q=2\), the labels \(2q-1\) and \(q+1\) coincide: add their contributions.** Thus \(H_2(1)=H_2(3)=8\), and every other fiber occurs zero times. Unlisted entries are zero, except where coincident entries are explicitly added. The odd-field entries are pairwise distinct for \(q\ge3\).

The maximal fiber is exactly \(\max_A\nu(A)=2q-1\). Moreover the number of nil-clean matrices is
\[
\boxed{\#\{A:\nu(A)>0\}=
\begin{cases}q^3+2q^2-1,&q\text{ odd},\\q^3+2q^2,&q\text{ even}.\end{cases}}
\]
The total mass identity is
\[
\sum_{A\in M_2(k)}\nu(A)=q^2\bigl(q(q+1)+2\bigr).
\]

## Assumptions and scope

The field has arbitrary prime-power cardinality \(q\ge2\); no restriction to prime fields or algebraically closed fields is made. Matrices are all two-by-two matrices over \(k\), including singular, scalar and non-diagonalizable ones. The decomposition count is by distinct idempotent summands \(P\), equivalently distinct ordered pairs \((P,A-P)\). Idempotent and nilpotent summands need not commute.

## Proof

**Step 1 (trace separation).** An idempotent in \(M_2(k)\) is diagonalizable with eigenvalues zero or one and hence has rank and trace in \(\{0,1,2\}\). The rank-zero and rank-two cases are uniquely \(P=0\) and \(P=I\). Since a two-by-two matrix is nilpotent exactly when its trace and determinant vanish, these contribute the two indicators \(\epsilon_0(A)\) and \(\epsilon_1(A)\) shown above. A rank-one idempotent necessarily has trace one, so no rank-one contributions occur unless \(t=1\).

**Step 2 (complementary-line lemma).** Every rank-one idempotent corresponds uniquely to an ordered pair \((L,M)\) of distinct lines in \(k^2\), its image and kernel. Let \(a=1-d\). In a basis adapted to \(L\oplus M\), the upper-left entry of \(A\) is \(a_{11}\); subtracting \(P=\operatorname{diag}(1,0)\) leaves a trace-zero matrix, and
\[
\det(A-P)=d-1+a_{11}.
\]
Consequently \(A-P\) is nilpotent precisely when \(a_{11}=a\). Fix a line \(L=ku\). If \(L\) is not \(A\)-invariant, there is exactly one complementary line \(M=k(A-aI)u\) satisfying this condition: the vector \((A-aI)u\) lies outside \(L\), and choosing it as a complementary basis vector makes the \(L\)-coefficient of \(Au\) equal to \(a\). If \(L\) is an eigenline of eigenvalue \(a\), all \(q\) complementary lines work; if it is an eigenline of a different eigenvalue, none works. Therefore, writing \(e_a(A)\) for the number of eigenlines of eigenvalue \(a\),
\[
\nu_1(A)=(q+1-e(A))+q\,e_a(A).
\]

**Step 3 (exceptional determinant).** At \(t=1\), the characteristic polynomial is \(z^2-z+d\), and evaluating at \(a=1-d\) gives \(d^2\). If \(d\ne0\), then \(e_a(A)=0\), so \(\nu_1(A)=q+1-e(A)\). If \(d=0\), \(A\) has distinct eigenvalues zero and one and is a rank-one idempotent, so \(e(A)=2\), \(e_a(A)=1\) and \(\nu_1(A)=2q-1\). This proves the prescribed-matrix formula. Notice that scalar matrices with trace one (possible only for odd \(q\)) have \(e(A)=q+1\) and no decompositions; no exception has been suppressed.

**Step 4 (conjugacy-class multiplicities).** The number of nonscalar matrices in each fixed characteristic-polynomial stratum is \(q(q+1)\) for a split quadratic with distinct roots, \(q(q-1)\) for an irreducible quadratic, and \(q^2-1\) for a repeated-root nonsemisimple class. These follow from centralizer orders in \(\operatorname{GL}_2(k)\). A repeated-root polynomial also has one scalar matrix.

When \(q\) is odd, the discriminant \(1-4d\), as \(d\) varies over \(k\), is zero at one value, a nonzero square at \((q-1)/2\) values and a nonsquare at \((q-1)/2\) values. The \(d=0\) split class is counted separately; the remaining nonzero-square discriminants number \((q-3)/2\). When \(q\) is even, \(z^2-z+d=z^2+z+d\) has roots in \(k\) exactly if the absolute trace \(\operatorname{Tr}_{k/\mathbb F_2}(d)\) is zero; among nonzero determinants there are \(q/2-1\) split and \(q/2\) irreducible values. There are no repeated roots in characteristic two.

The trace-zero nilpotent locus contains \(q^2\) matrices. Its translate by \(I\) contains another \(q^2\), disjoint in every characteristic, because an eigenvalue cannot be both zero and one. These are also disjoint from the trace-one stratum, including in characteristic two. Thus the two trivial-idempotent contributions each produce exactly \(q^2\) fibers equal to one. Combining the class sizes produces the stated two histograms. The only collision of displayed positive fiber labels occurs at \(q=2\), where the contributions are added.

**Step 5 (totals).** The positive trace-one stratum consists of all \(q^3\) matrices when \(q\) is even, and all except the single scalar \(\frac12 I\) when \(q\) is odd. Together with the two disjoint \(q^2\) nilpotent translates this gives the nil-clean-locus formulas. Since there are \(q(q+1)+2\) idempotents and \(q^2\) nilpotents, counting decompositions directly gives the total mass identity. The maximum follows from the fiber formula and is attained by every rank-one idempotent; at \(q=2\), irreducible trace-one matrices attain it too.

## Verification

The self-contained Python 3 program `verify_nilclean.py` enumerates every two-by-two matrix, every idempotent and every nilpotent over prime fields of sizes \(2,3,5,7\) and the extension field \(\mathbb F_4\) (using the polynomial \(T^2+T+1\)). For each matrix it independently counts actual decompositions by adding every idempotent to every nilpotent, compares the result with the eigenline formula, checks the complete histograms, maximal fiber, positive locus and total mass. The exact recorded console output is `verification_output.txt`.

The small-field enumeration only corroborates the theorem; the finite-to-infinite step is the proof above, not an extrapolation.

## Relationship to prior work

Breaz, Călugăreanu, Danchev and Micu (2013) characterize when a full matrix algebra over a field is nil-clean: the field must be \(\mathbb F_2\). Their full text gives an existence theorem, not the complete decomposition-multiplicity histogram for each finite extension field. Basnet and Bhattacharyya (2014) introduce the nil-clean index and prove it is three for \(M_2(\mathbb F_2)\), together with general lower bounds. Their article does not state the all-\(q\) histogram. Cîmpean and Danchev (2017) compute a **weakly** nil-clean index for \(M_2(\mathbb F_3)\), a distinct invariant allowing subtraction of the idempotent, and the article provides no complete finite-field nil-clean fiber histogram. Călugăreanu (2019) studies integral matrices and Diophantine conditions, not this finite-field distribution.

A related published prescribed-fiber result counts **products** of an idempotent and nilpotent, not their sums; its zero/singular/invertible fiber law neither implies the present trace-and-eigenline law nor settles the additive histogram. A related prescribed-fiber result for commutators of rank-one idempotents has a different map and target. One 2018 dissertation on indices of matrix rings over \(\mathbb Z/n\mathbb Z\) was identified from its abstract but the full text was inaccessible at inspection; it is a residual potential source for some prime-field index or multiplicity cases. Thus the historical-priority conclusion is best-knowledge and provisional, not independent certification.

## Limitations

The theorem is strictly for two-by-two matrices over finite fields; it does not determine analogous histograms for higher matrix sizes or nonfield coefficient rings. The maximum nil-clean index and some existence results were already investigated in the literature; the scientific claim here is the **complete decomposition-fiber distribution**, not the definition of nil-clean index or the known characterization of nil-clean matrix rings. An inaccessible dissertation and possible more general class-counting formulas leave residual historical-priority uncertainty. Independent validation has not been performed.

## References

1. S. Breaz, G. Călugăreanu, P. Danchev, T. Micu, *Nil-clean matrix rings*, Linear Algebra Appl. 439 (2013), 3115–3119; available online 2013-09-06. DOI: 10.1016/j.laa.2013.08.027. Lawful full text: https://arxiv.org/html/1310.0416v1 (preprint submitted 2013-10-01).
2. D. K. Basnet, J. Bhattacharyya, *Nil clean index of rings*, Int. Electron. J. Algebra 15 (2014), 145–156, especially Proposition 4.4. https://www.ieja.net/files/papers/volume-15/12-V15-2014.pdf
3. A. Cîmpean, P. Danchev, *Weakly nil-clean index and uniquely weakly nil-clean rings*, Int. Electron. J. Algebra 21 (2017), 180–197, especially Example 2.26. https://www.ieja.net/files/papers/volume-21/12-V21-2017.pdf
4. G. Călugăreanu, *Nil-clean integral 2 by 2 matrices: The elliptic case*, Bull. Math. Soc. Sci. Math. Roumanie 62 (2019), 239–250. https://ssmr.ro/bulletin/pdf/62-3/articol_3.pdf
5. B. L. Schoonmaker, *Clean Indices of Common Rings*, Brigham Young University dissertation, 2018, abstract https://scholarsarchive.byu.edu/etd/7027/ (full-text access unsuccessful).
