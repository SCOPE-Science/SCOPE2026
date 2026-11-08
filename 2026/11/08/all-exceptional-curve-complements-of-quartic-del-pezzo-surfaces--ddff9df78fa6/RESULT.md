# All exceptional-curve complements of quartic del Pezzo surfaces: Frobenius zeta functions and a nonsplit full example over \(\mathbb F_3\)

## Finding
Let \(X\) be a smooth degree-four del Pezzo surface over \(k=\mathbb F_q\), with \(q\) any prime power. Let \(D\) be the *reduced union of all sixteen geometric exceptional curves* (which is Galois-stable), and put \(U=X\setminus D\). For the geometric Frobenius conjugacy class \(g\in W(D_5)\), let \(L_g\), \(P_g\), \(F_g\) denote its permutation actions on the sixteen exceptional curves, the forty pairwise intersection points, and the eighty branches through those points, respectively. Let \(V_g\) be the natural five-dimensional signed-permutation representation. For every integer \(n\geq1\),

\[
\#U(\mathbb F_{q^n})=q^{2n}+q^n\!\left(1+\operatorname{tr}(V_g^n)-\#\operatorname{Fix}(L_g^n)\right)+1-\#\operatorname{Fix}(L_g^n)+\#\operatorname{Fix}(F_g^n)-\#\operatorname{Fix}(P_g^n).
\]

In particular, this expression and the algorithm below determine the complete Hasse–Weil zeta function for each of the eighteen signed cycle types of \(W(D_5)\). The eighteen *formal zeta expressions* are pairwise different; the provided exhaustive verifier distinguishes their symbolic extension-count profiles in degrees at most twelve.

**Sharp nonemptiness result.** There exists a smooth degree-four del Pezzo surface \(X/\mathbb F_q\) satisfying \(U(\mathbb F_q)=\varnothing\) if and only if \(q=3\) or \(q=5\). For \(q=3\), an example is the blow-up of \(\mathbb P^2\) at one rational point and two closed points of degree two, with Frobenius cycle type \((1,2,2)\) on the blown-up geometric points; this is not a split surface. For \(q=5\), a split example is the blow-up at five rational points in general position. The split \(q=5\) case was already known (Hirschfeld, recorded explicitly by Knecht–Reyes), and is **not** a novelty claim. The nonsplit \(q=3\) case and the full eighteen-type arithmetic formula are the assessed contributions.

The following table gives every first-extension point-count polynomial. Each comma-separated cycle list gives the cycle lengths and the size is the number of elements of that signed cycle type in the Weyl group. A blank positive/negative list is indicated by an em dash. The negative-cycle count is always even. A class listed below need not be realizable over each *small* field, so a formally negative point-count polynomial simply excludes its realization there.

| Positive cycle lengths | Negative cycle lengths | Class size | \(\#U(\mathbb F_q)\) |
|:--|:--|--:|:--|
| — | 1,1,1,2 | 20 | \(q^2-2q+1\) |
| — | 1,4 | 240 | \(q^2+1\) |
| — | 2,3 | 160 | \(q^2+q+1\) |
| 1 | 1,1,1,1 | 5 | \(q^2-2q-7\) |
| 1 | 1,3 | 160 | \(q^2+q-1\) |
| 1 | 2,2 | 60 | \(q^2+2q+1\) |
| 1,1 | 1,2 | 60 | \(q^2+2q+1\) |
| 1,1,1 | 1,1 | 10 | \(q^2+2q+1\) |
| 1,1,1,1,1 | — | 1 | \(q^2-10q+25\) |
| 1,1,1,2 | — | 20 | \(q^2-4q+5\) |
| 1,1,3 | — | 80 | \(q^2-q+1\) |
| 1,2 | 1,1 | 60 | \(q^2-3\) |
| 1,2,2 | — | 60 | \(q^2-2q-3\) |
| 1,4 | — | 240 | \(q^2-1\) |
| 2 | 1,2 | 120 | \(q^2+1\) |
| 2,3 | — | 160 | \(q^2-q-1\) |
| 3 | 1,1 | 80 | \(q^2-q+1\) |
| 5 | — | 384 | \(q^2\) |

## Assumptions and scope
The ground field \(\mathbb F_q\) is arbitrary, including characteristic two. Geometric exceptional curves mean the sixteen smooth rational \((-1)\)-curves on \(X_{\overline{k}}\); the divisor \(D\) need not be a union of individually \(k\)-defined curves. No claim is made that all eighteen arithmetic types exist over every particular finite field. "Full" means that *every rational point of the complete surface* is on \(D\), i.e. \(U(k)=\varnothing\), even if some exceptional components are not individually defined over \(k\). The rational-point classification concerns all smooth degree-four del Pezzo surfaces, not just split ones.

## Proof
**1. Geometric incidence model.** Over an algebraic closure, a smooth degree-four del Pezzo surface is \(\mathbb P^2\) blown up at five points with no three collinear. Its sixteen exceptional curves are the five exceptional divisors \(E_i\), the ten strict transforms \(L_{ij}\) of joining lines, and the strict transform \(C\) of the conic through all five points. Their nonzero pairwise intersections are exactly \(E_i\cdot C=1\), \(E_i\cdot L_{ij}=1\), and \(L_{ij}\cdot L_{ab}=1\) when \(\{i,j\}\cap\{a,b\}=\varnothing\). There are \(5+20+15=40\) such pairs. The incidence graph is triangle-free: the two curves meeting a fixed third curve cannot also meet each other at that same point. More directly, two different joining lines cannot meet on the blow-up if they share a base point; the remaining intersections are transverse at points disjoint from the base locus, and the conic meets only the exceptional curves. Hence the forty nodes are distinct and ordinary, with exactly eighty geometric branches.

Index the sixteen curves by the even-parity sign vectors in \(\{\pm1\}^5\): the all-plus vector corresponds to \(C\); vectors with two minus signs indexed by \(\{i,j\}\) correspond to \(L_{ij}\); vectors with four minus signs and missing coordinate \(i\) correspond to \(E_i\). Two curves intersect exactly when their vectors have Hamming distance four. The automorphism group preserving the intersection pairing and canonical class is the Weyl group \(W(D_5)\), acting as the even signed permutations on five coordinates. Its order is \(2^4 5!=1920\), and the signed cycle types are pairs of partitions \((\lambda_+,\lambda_-)\) of total size five with an even number of negative cycles, giving eighteen types. This identifies Galois actions on curves, nodes and branches without any genericity assumptions beyond smoothness of \(X\).

**2. Frobenius counts.** The geometric Picard group decomposes as the fixed canonical class plus the signed five-dimensional root representation. Because \(X\) is geometrically rational, its other odd étale cohomology vanishes, so
\[
\#X(\mathbb F_{q^n})=q^{2n}+q^n\bigl(1+\operatorname{tr}(V_g^n)\bigr)+1.
\]
Let \(\widetilde D\) be the normalization of \(D\). Its components are the disjoint union of sixteen smooth genus-zero curves. Over any finite extension on which a component is fixed by Frobenius, it is isomorphic to \(\mathbb P^1\) and contributes \(q^n+1\) points. At the forty nodes, the normalization has eighty preimages. Stratification over the smooth locus of \(D\) gives, for all \(n\geq1\),
\[
\#D(\mathbb F_{q^n})=(q^n+1)\#\operatorname{Fix}(L_g^n)-\#\operatorname{Fix}(F_g^n)+\#\operatorname{Fix}(P_g^n).
\]
The distinction between **nodes and their branches is essential**: a rational node may have two conjugate branches, so simply subtracting the forty-node fixed-point count from normalized components is incorrect. Subtracting this formula from the smooth-projective count proves the claimed extension-count identity.

If \(c_M(d)\) denotes the number of length-\(d\) cycles of the permutation \(M\), define \(\Pi_M(T)=\prod_{d\geq1}(1-T^d)^{c_M(d)}\). For signed cycles \((\lambda_+,\lambda_-)\), put
\[
Q_g(Z)=\prod_{a\in\lambda_+}(1-Z^a)\prod_{b\in\lambda_-}(1+Z^b).
\]
Then exponential summation over all extension fields gives the complete rational-function formula
\[
\boxed{Z(U/\mathbb F_q,T)=\frac{\Pi_L(T)\,\Pi_L(qT)\,\Pi_P(T)}{(1-T)(1-q^2T)(1-qT)Q_g(qT)\,\Pi_F(T)}.}
\]
Here \(\Pi_L(qT)=\prod_d(1-q^dT^d)^{c_L(d)}\) and similarly for other terms. The formula is valid even when Frobenius exchanges the two local branches at a rational node. All cycle multisets are obtained by acting on the 16 even sign vectors, on the 40 Hamming-distance-four unordered pairs, and on the 80 oriented incidences; this is a finite complete algorithm with no geometric choices.

**3. Eighteen first-extension polynomials.** Running through all even signed permutations gives exactly the eighteen rows above. For fixed \(n\), a permutation cycle of length \(d\) contributes \(d\) fixed points to its \(n\)-th power precisely when \(d\mid n\). A positive signed cycle of length \(d\) contributes \(d\) to \(\operatorname{tr}(V_g^n)\) when \(d\mid n\), while a negative one contributes \(d(-1)^{n/d}\). Thus the displayed table is a direct finite application of the two preceding identities. Comparing the pairs of \(q^n\)- and constant-term coefficients for \(1\le n\le12\) distinguishes all eighteen symbolic zeta functions. This is a *finite exhaustive Weyl-group check*, not a finite-field experiment standing in for the all-\(q\) proof.

**4. Only two finite fields can support full surfaces.** Among the eighteen polynomials, the only zero for a prime power \(q\ge2\) occurs in the split identity type at \(q=5\) (polynomial \((q-5)^2\)) or the all-positive cycle type \((1,2,2)\) at \(q=3\) (polynomial \(q^2-2q-3\)). This follows by direct inspection: for \(q\ge6\), every polynomial is positive; at \(q=2,3,4,5\), the integer roots are exactly those two pairs. Some other class formulas are negative at very small fields, proving those classes cannot occur there rather than creating exceptions to nonemptiness.

For \(q=5\), take five distinct rational points on a smooth rational conic, which has six \(\mathbb F_5\)-points. No three lie on a line, so their blow-up is a smooth split degree-four del Pezzo surface. The corresponding identity action gives \(\#U(\mathbb F_5)=0\).

For \(q=3\), choose \(\alpha\in\mathbb F_9\) with \(\alpha^2=-1\) and define the five geometric points
\[
P_0=[0:0:1],\quad A=[1:\alpha:0],\quad A^3=[1:-\alpha:0],\quad B=[1:1+\alpha:\alpha],\quad B^3=[1:1-\alpha:-\alpha].
\]
The notation \(A^3,B^3\) means coordinatewise cubic Frobenius, not projective exponentiation of points. All ten determinants of triples are nonzero in \(\mathbb F_9\), as checked explicitly by the standalone exact-arithmetic verifier. The resulting Frobenius-stable five-point set is in general position and has orbit partition \((1,2,2)\). Its blow-up is a smooth degree-four del Pezzo surface with \(\#U(\mathbb F_3)=3^2-2\cdot3-3=0\), proving the genuinely nonsplit case. More concretely, \(\#X(\mathbb F_3)=13+3=16\) by the blow-up point count. Exactly four exceptional curves are individually rational: the exceptional divisor over \(P_0\), the conic through all five points, and the joining lines of the two conjugate pairs. Their union has \(4(3+1)-2=14\) rational points. Exactly two additional rational nodes have their two branches exchanged by Frobenius, supplying the remaining two points. This explicitly illustrates why the eighty-branch term in the formula cannot be discarded.

## Verification
The provided `dp4_verify.py` is dependency-free Python. It enumerates every element of the order-1920 even signed permutation group; constructs the 16 curves, 40 nodes and 80 branches directly; checks the geometric blow-up intersection model; partitions the group into its eighteen signed cycle types and calculates their exact first-extension polynomials; compares symbolic extension-count profiles through degree twelve; checks all possible small-field zeros and positivity for \(q\ge6\); and verifies the explicit five-point arc in \(\mathbb F_9\). Its complete recorded output is in `dp4_verification_output.txt`; execution finishes `ALL_CHECKS_PASSED`. The proof for arbitrary \(q\) follows from geometric stratification and the complete finite Weyl-group computation; small-field enumerations are not treated as exhaustive over all fields.

## Relationship to prior work
Rybakov (2005) classifies zeta functions of the **complete** degree-four del Pezzo surfaces and their conic-bundle birational models. Banwait–Fité–Loughran (first preprint 2016) give Frobenius-trace and finite-field inverse-Galois information for complete del Pezzo surfaces. Knecht–Reyes (first preprint 2015), recording Hirschfeld's earlier classification, explicitly give the split quartic count \(\#U(\mathbb F_q)=(q-5)^2\) and the split \(q=5\) fullness result. These are all prior statements, **not** new assertions here. The added question is the arithmetic of the full reduced exceptional boundary for *every* Frobenius form, where rational nodes may have non-rational branches; the result gives its complete eighteen-type open zeta classification and a nonsplit full quartic surface at \(q=3\). Contemporary work on the complex complement concerns topology rather than finite-field Frobenius profiles.

## Limitations
The Weyl-class classification is conditional on the class realized by a given surface; no assertion that every class appears over each small finite field is made. The split \(q=5\) case is already known. Although checks against several primary works and mathematical research records found no directly covering eighteen-type open zeta classification or nonsplit \(\mathbb F_3\) fullness construction, historical priority remains provisional: classical papers on rational points on Segre surfaces or unpublished tables may contain equivalent formulas. 
## References
1. A. Knecht and K. Reyes, *Full Degree Two del Pezzo Surfaces over Small Finite Fields*, arXiv:1510.04621 (first public version 2015-10-15), §1, including Hirschfeld's theorem and the split degree-four count. https://arxiv.org/html/1510.04621v2
2. S. Rybakov, *Zeta Functions of Conic Bundles and Del Pezzo Surfaces of Degree 4 over Finite Fields*, Moscow Mathematical Journal 5 (2005), 919–926, especially §§1 and 3. https://doi.org/10.17323/1609-4514-2005-5-4-919-926
3. B. Banwait, F. Fité, D. Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, arXiv:1606.00300 (first public version 2016-06-01). https://arxiv.org/abs/1606.00300
4. M. Bright, N. Bruin, E. V. Flynn, A. Logan, *The Brauer–Manin obstruction and Sha[2]*, LMS Journal of Computation and Mathematics 10 (2007), 354–377, classical degree-four exceptional-curve incidence geometry. https://research-information.bris.ac.uk/en/publications/the-brauer-manin-obstruction-and-sha2/
5. J. W. P. Hirschfeld, results on full split del Pezzo surfaces as quoted in [1].
