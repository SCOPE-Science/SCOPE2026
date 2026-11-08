# Almost-ordinary Jacobians for both smooth degree-ten plane-filling curves in a characteristic-seven pencil

## Finding

Over \(\mathbb F_7\), consider the Asgarli--Ghioca plane-filling pencil \(C_k=V(F_k)\subset\mathbb P^2\), indexed by \(k\in\mathbb F_7\), where
\[
F_k=X^2(X^7Y-XY^7)+Y^2(Y^7Z-YZ^7)+(Z^2+kX^2)(Z^7X-ZX^7).
\]
**The geometrically smooth members are exactly \(C_1\) and \(C_3\).** Each has degree \(10\), genus \(36\), exactly \(57\) rational points over \(\mathbb F_7\), Jacobian \(7\)-rank \(35\), and Cartier \(a\)-number \(1\). Their Newton polygons have slopes \(0\) with multiplicity \(35\), \(1/2\) with multiplicity \(2\), and \(1\) with multiplicity \(35\).

The two curves have different extension-field counts:
\[
\#C_1(\mathbb F_{49})=103,\qquad \#C_3(\mathbb F_{49})=107.
\]
Thus their Jacobians are not isogenous over \(\mathbb F_7\), and in particular the curves are not \(\mathbb F_7\)-isomorphic. For the numerator \(P_k(T)=\prod_{i=1}^{72}(1-\alpha_iT)\) of the Hasse--Weil zeta function, the first coefficients are \(1+49T+1227T^2+\cdots\) and \(1+49T+1229T^2+\cdots\), respectively.

## Assumptions and scope

The base field is exactly \(\mathbb F_7\); the parameter \(k\) ranges over its seven elements. Geometric smoothness means smoothness after passage to the algebraic closure. The \(7\)-rank of the Jacobian is the dimension of its étale \(7\)-torsion, and the \(a\)-number is the dimension of the kernel of Cartier on holomorphic differentials. The isogeny distinction is over \(\mathbb F_7\), **not** a claim of nonisomorphism over the algebraic closure. A genus-\(36\) Jacobian with \(7\)-rank \(35\) is almost ordinary; the stated Newton slopes follow from the unique height-two one-dimensional residual \(7\)-divisible factor.

## Proof

**1. Completeness and smoothness.** Each summand of \(F_k\) is a multiple of \(U^7V-UV^7\), which vanishes at every \(\mathbb F_7\)-rational projective point. Thus \(C_k(\mathbb F_7)=\mathbb P^2(\mathbb F_7)\) set-theoretically, and the point count is \(7^2+7+1=57\). The published rational-point criterion for this very pencil states that \(C_k\) is smooth at its rational points precisely when \(t^7+kt^3-1\) has no root \(t\in\mathbb F_7\). Direct substitution yields the entire list of root-bearing parameters and witnesses:
\[
(k,t)=(0,1),(2,3),(4,4),(4,5),(5,6),(6,2).
\]
Therefore the five parameters \(k\in\{0,2,4,5,6\}\) give singular curves, and only \(k=1,3\) could be geometrically smooth.

For \(k=1,3\), compute the homogeneous partial derivatives \(\partial_XF_k,\partial_YF_k,\partial_ZF_k\), dehomogenize in each chart \(X=1\), \(Y=1\), \(Z=1\), and perform exact polynomial reductions in \(\mathbb F_7[u,v]\). The three partials generate the unit ideal in each of the six chart calculations. This can be reconstructed using the standalone Buchberger implementation `verify_smoothness.py`: in each case an exact S-polynomial remainder is \(1\), an explicit ideal-membership certificate (not a search over rational points). The smooth-projective degree-genus formula gives \(g=(10-1)(10-2)/2=36\). Smoothness of a projective plane curve of positive degree implies geometric irreducibility.

**2. Hasse--Witt and Cartier.** Let \(B\) be the 36 triples \((a,b,c)\in\mathbb Z_{\ge0}^3\) satisfying \(a+b+c=7\), in lexicographic enumeration by \(a\), then \(b\). Write \(h_{e_1,e_2,e_3}\) for the coefficient of \(X^{e_1}Y^{e_2}Z^{e_3}\) in \(F_k^6\) modulo \(7\). The classical smooth-plane-curve formula yields the Hasse--Witt matrix, with rows and columns indexed by \(B\):
\[
A_{(a,b,c),(u,v,w)}=h_{7(a+1)-(u+1),\;7(b+1)-(v+1),\;7(c+1)-(w+1)}.
\]
An index containing a negative exponent has coefficient zero. Up to transpose and inverse-Frobenius convention, this is also the Cartier matrix; those conventions do not alter ranks. Here the coefficient field is the prime field, so the Frobenius twist on matrix coefficients is the identity.

Direct multinomial expansion and Gaussian elimination over \(\mathbb F_7\) give for **both** \(k=1,3\)
\[
\operatorname{rank}(A)=35,\qquad\operatorname{rank}(A^2)=35.
\]
The rank is supported by small exact minors: with zero-based indices in the stated triple ordering, deleting row \(34\) and column \(35\) for \(k=1\) gives a \(35\)-square minor of determinants \(6\) in \(A\) and \(1\) in \(A^2\); for \(k=3\), deleting row \(33\), column \(34\) gives determinants \(6\) and \(6\). Both full \(36\)-determinants vanish. All entries and certificates are reconstructed by `verify_cartier.py`, using only integer arithmetic modulo seven.

Since \(\operatorname{rank}(A^2)=\operatorname{rank}(A)\), the image is stable and the Frobenius-stable rank is \(35\), hence the Jacobian has \(7\)-rank \(35\). The Cartier kernel has dimension \(36-35=1\), so \(a=1\). A principally polarized \(36\)-dimensional abelian variety of \(7\)-rank \(35\) has \(35\) slopes \(0\), \(35\) slopes \(1\), and a remaining symmetric height-two pair, necessarily \(1/2,1/2\).

**3. Rational points over the quadratic extension.** The standalone `verify_points.py` represents \(\mathbb F_{49}\) in each of two independent quadratic bases, \(\mathbb F_7[u]/(u^2-6)\) and \(\mathbb F_7[v]/(v^2-3)\). In either representation, exact evaluation of \(F_k(X,Y,1)\) at all \(49^2\) affine pairs gives \(95\) points for \(k=1\) and \(99\) for \(k=3\). The line \(Z=0\) contributes eight points in each case. The totals are \(103\) and \(107\), respectively; this enumerates every projective point exactly once, hence is exhaustive. By the Weil zeta formula, \(S_1=8-57=-49\), \(S_2=50-\#C_k(\mathbb F_{49})\), and the second coefficient is \((S_1^2-S_2)/2\); it is \(1227\) or \(1229\). Different zeta numerators imply the Jacobians cannot be isogenous over \(\mathbb F_7\).

## Verification

From a directory containing all three scripts, run `python3 verify_smoothness.py`, `python3 verify_cartier.py`, and `python3 verify_points.py`. All three use only the Python standard library. The smoothness verifier explicitly constructs Buchberger reductions of the three homogeneous gradient generators in all three affine charts. The Cartier verifier expands \(F_k^6\), reconstructs the full \(36\times36\) matrices and squares, checks zero full determinants and nonzero \(35\)-minors, and computes ranks. The point-count verifier performs exhaustive enumeration in two inequivalent presentations of the same extension field. The scripts are exact finite proofs of their stated computational assertions, not heuristic sampling or an appeal to finite tests for an infinite-field claim.

## Relationship to prior work

Asgarli and Ghioca defined this degree-\(q+3\) plane-filling pencil and proved the criterion for smoothness at rational points (Theorem 1.2), while proposing geometric smoothness equivalence as Conjecture 1.5. They reported geometric smoothness checks for odd prime powers below \(200\), so neither the pencil nor the underlying smoothness claim is new. This result addresses different arithmetic questions: the exact Hasse--Witt rank, stable \(7\)-rank, Newton polygon, \(a\)-number, and the second extension-field counts for **all** smooth parameters at \(q=7\). Adolphson--Sperber's classical Hasse--Witt formula supplies a general computational tool, not this specialization. Relevant prior literature and indexed mathematical records were compared by mathematical implication, not by title matching; see the separate review for priority limitations.

## Limitations

The result is specific to the Asgarli--Ghioca pencil at \(q=7\); it does not classify every degree-ten plane-filling curve over \(\mathbb F_7\), determine full zeta functions, or show that the two curves are geometrically nonisomorphic. The special field \(q=7\) is natural as the characteristic coincides with the exponent seven in the published rational-singularity criterion; this result does not extend the calculation to all characteristics. Independent historical-priority review is pending.

## References

1. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072, first posted 2023-07-06. https://arxiv.org/abs/2307.03072
2. A. Adolphson and S. Sperber, *A generalization of the Hasse--Witt matrix of a hypersurface*, arXiv:1701.04509 (2017). https://arxiv.org/abs/1701.04509
3. K.-O. Stöhr and J. F. Voloch, *A formula for the Cartier operator on plane algebraic curves*, Journal für die reine und angewandte Mathematik 377 (1987), 49--64. (Standard Cartier-formula background, not used for priority.)
