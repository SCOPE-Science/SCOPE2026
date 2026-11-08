# Rank fibers and component intersections of self-adjoint zero-product pairs

## Finding

Let \(k\) be any field, let \(V\) be an \(n\)-dimensional vector space with \(n\geq1\), and let \(g\) be a nondegenerate symmetric bilinear form on \(V\). Write \(A^\dagger\) for the adjoint of an endomorphism with respect to \(g\). Consider the **reduced** algebraic set
\[
\mathcal Z_g=\{(A,B)\in\operatorname{End}(V)^2:A^\dagger=A,\ B^\dagger=B,\ AB=0\}.
\]
Because both operators are self-adjoint, \(AB=0\) also implies \(BA=0\). No assumption of nilpotence, diagonalizability, or semisimplicity is imposed on either operator.

**Geometric rank strata and components.** For all \(s,t\geq0\) with \(s+t\leq n\), the locally closed subvariety \(\mathcal Z_g(s,t)\) of pairs of respective ranks \(s,t\) is nonempty, smooth, and geometrically irreducible. Writing \(d=s+t\), its dimension is
\[
\dim\mathcal Z_g(s,t)=D_n(d):=\frac{d(2n-d+1)}2.
\]
No pair of ranks with \(s+t>n\) occurs. The geometrically irreducible components of \(\mathcal Z_g\) are exactly the following \(n+1\) distinct reduced closed subsets:
\[
\mathcal C_i=\{(A,B)\in\mathcal Z_g:\operatorname{rank}A\leq i,\ \operatorname{rank}B\leq n-i\},\qquad0\leq i\leq n.
\]
Every component has dimension \(n(n+1)/2\). For any nonempty index set \(I\subseteq\{0,\dots,n\}\), with \(i=\min I\) and \(j=\max I\), the reduced intersection \(\bigcap_{h\in I}\mathcal C_h=\mathcal C_i\cap\mathcal C_j\) is geometrically irreducible and has dimension
\[
\dim(\mathcal C_i\cap\mathcal C_j)=D_n(n-j+i).
\]
This classifies every nonempty multiple intersection, not just the components themselves.

**Finite-field rank distribution.** For \(k=\mathbb F_q\), any prime power \(q\), and any nondegenerate symmetric \(g\), define \(S_0(q)=1\) and
\[
S_a(q)=q^{a(a+1)/2}\prod_{j=1}^{\lceil a/2\rceil}(1-q^{-(2j-1)})\quad(a\geq1).
\]
This is the classical number of nonsingular symmetric \(a\)-by-\(a\) matrices over \(\mathbb F_q\), including characteristic two. For \(0\leq s,t\leq n\), the exact number of labeled ordered pairs in \(\mathcal Z_g\) with respective ranks \(s,t\) is
\[
\boxed{F_{n,q}(s,t)=
\begin{cases}
{n\brack s}_q{n-s\brack t}_qS_s(q)S_t(q),&s+t\leq n,\\
0,&s+t>n.
\end{cases}}
\]
Here \({a\brack b}_q=\prod_{h=0}^{b-1}(q^{a-h}-1)/(q^{b-h}-1)\) and \({a\brack0}_q=1\). The count is independent of the Witt type, determinant square class, and (in characteristic two) the alternating or nonalternating type of \(g\).

In particular the total is
\[
Z_n(q)=\sum_{s=0}^n{n\brack s}_qS_s(q)q^{(n-s)(n-s+1)/2}.
\]
Every reduced intersection \(\mathcal C_i\cap\mathcal C_j\) with \(i\leq j\) has exactly
\[
\sum_{a=0}^i\sum_{b=0}^{n-j}{n\brack a}_q{n-a\brack b}_qS_a(q)S_b(q)
\]
\(\mathbb F_q\)-points. For each fixed \(n\), as \(q\) grows over arbitrary prime powers,
\[
Z_n(q)=(n+1)q^{n(n+1)/2}+O_n(q^{n(n+1)/2-1}),
\]
so two uniform independent self-adjoint operators annihilate one another with probability \((n+1)q^{-n(n+1)/2}+O_n(q^{-n(n+1)/2-1})\).

## Assumptions and scope

The form \(g\) is symmetric, nondegenerate, and allowed to be isotropic. The field need not be algebraically closed and may have characteristic two. Geometry means that of the reduced zero locus after base change to an algebraic closure; no assertion is made that the original ideal of coordinate equations is radical. \(S_a(q)\) counts unrestricted-diagonal symmetric matrices, not alternating matrices. The rank-stratum formulas concern labeled operators, not isometry-conjugacy orbits. Although \(g\) may be alternating in characteristic two, \(A\) and \(B\) are defined by the ordinary adjoint \(g(Ax,y)=g(x,Ay)\).

## Proof

**1. Fixed-image self-adjoint operators.** Nondegeneracy gives a perfect pairing between \(U\) and \(V/U^\perp\) for any subspace \(U\subseteq V\). In particular \(V/U^\perp\cong U^*\). A self-adjoint \(A\) with image contained in \(U\) annihilates \(U^\perp\), because \(g(Ax,v)=g(x,Av)=0\) for \(v\in U^\perp\). Conversely every symmetric linear map \(U^*\to U\), interpreted via this perfect pairing and the quotient map \(V\to V/U^\perp\), gives such a self-adjoint \(A\). Thus this space is naturally a vector space modeled on \(\operatorname{Sym}^2U\), of dimension \(\dim U(\dim U+1)/2\). Its full-image locus is the open set of nonsingular symmetric forms on \(U^*\).

**2. Orthogonal image incidence.** Self-adjointness gives \(\ker A=(\operatorname{im}A)^\perp\). Hence \(AB=0\) is equivalent to \(\operatorname{im}B\subseteq(\operatorname{im}A)^\perp\), and \(BA=(AB)^\dagger=0\). Put \(U=\operatorname{im}A\) and \(W=\operatorname{im}B\). Necessarily \(g(U,W)=0\), so \(\dim U+\dim W\leq n\). Conversely every orthogonal pair \((U,W)\) of dimensions \((s,t)\), together with nonsingular symmetric maps \(U^*\to U\) and \(W^*\to W\), yields a unique pair \((A,B)\) in the corresponding rank stratum.

**3. Smooth irreducible rank strata.** The incidence base of orthogonal \((s,t)\)-subspaces is the relative Grassmannian \(\operatorname{Gr}(t,\mathcal U^\perp)\) over \(\operatorname{Gr}(s,V)\), where \(\mathcal U\) is the tautological subbundle. Every fiber is \(\operatorname{Gr}(t,n-s)\); the base is smooth and geometrically irreducible and has dimension \(s(n-s)+t(n-s-t)\). Above it, the self-adjoint maps with these image containments form a vector bundle of rank \(s(s+1)/2+t(t+1)/2\). The full-rank-in-each-factor subset is nonempty open and is isomorphic to \(\mathcal Z_g(s,t)\), so that stratum is smooth and geometrically irreducible. Adding the dimensions yields
\[
s(n-s)+t(n-s-t)+\frac{s(s+1)+t(t+1)}2=\frac{(s+t)(2n-s-t+1)}2.
\]

**4. All reduced component intersections.** Fix \(i\leq j\). Consider incidence data \((U,W,A,B)\) with \(\dim U=i\), \(\dim W=n-j\), \(g(U,W)=0\), \(\operatorname{im}A\subseteq U\), and \(\operatorname{im}B\subseteq W\). The base is a relative Grassmannian over \(\operatorname{Gr}(i,V)\); over it the operator choices form a vector bundle. Therefore the incidence space is irreducible, and its image in the pair space is irreducible. The image is precisely \(\mathcal C_i\cap\mathcal C_j\): for any pair in that set, write \(U_0=\operatorname{im}A\), \(W_0=\operatorname{im}B\); extend \(U_0\) to an \(i\)-space inside \(W_0^\perp\), and then extend \(W_0\) to an \((n-j)\)-space inside \(U^\perp\). The inequalities on ranks guarantee both extensions. Its dense open set has ranks \((i,n-j)\) and thus dimension \(D_n(n-j+i)\). This proves irreducibility and the intersection dimension. The case \(i=j\) shows every \(\mathcal C_i\) is irreducible and has dimension \(D_n(n)=n(n+1)/2\). Every pair belongs to at least one such component by choosing \(i\) with \(\operatorname{rank}A\leq i\leq n-\operatorname{rank}B\). Components are distinct because their open rank profiles \((i,n-i)\) differ and the upper-semicontinuity of rank prevents one such component from containing another. Every nonempty multiple intersection reduces to its extreme indices, completing the classification.

**5. Exact finite-field fibers.** Over \(\mathbb F_q\), choose \(U\) in \({n\brack s}_q\) ways, and \(W\subseteq U^\perp\) in \({n-s\brack t}_q\) ways. The fixed-image correspondence from Step 1 gives \(S_s(q)S_t(q)\) choices of self-adjoint operators. This proves \(F_{n,q}(s,t)\). The standard nonsingular symmetric-matrix formula \(S_a(q)\) is the full-rank case of the MacWilliams rank formula, reproduced as Equation (4.5) by Lewis et al. [2]. Equivalently, \(S_a(q)=q^{a(a+1)/2}\prod_{j\leq\lceil a/2\rceil}(1-q^{-(2j-1)})\). Summing the rank fibers gives the intersection count. Alternatively, for fixed \(A\) of rank \(s\), the admissible \(B\) form a vector space of dimension \((n-s)(n-s+1)/2\), yielding the single-sum total. In each complementary-rank stratum \(s+t=n\) the point-count degree is \(n(n+1)/2\) with leading coefficient one; all smaller rank sums have lower degree by the geometric dimension formula. There are \(n+1\) complementary-rank strata, giving the stated asymptotic.

## Verification

The standalone scripts `verify_zero_product.py` and `verify_incidence.py` are supplied with recorded standard output. The first directly enumerates symmetric matrices and all their ordered zero-product pairs for \((n,q)=(1,2),(2,2),(3,2),(4,2),(2,3),(3,3),(2,5)\); it also tests nonstandard symmetric forms over \(\mathbb F_2\) and \(\mathbb F_3\), and uses explicit polynomial-basis arithmetic for \(\mathbb F_4\) at \(n=2\). Every individual rank fiber agrees. The second independently checks all component-set incidence formulas and their intersections for \(1\leq n\leq3\) over \(\mathbb F_2\). The scripts are finite corroboration, not a substitute for the proof of the all-field geometry or the all-prime-power enumeration.

Some total counts: \(Z_2(2)=18\), \(Z_3(2)=204\), \(Z_4(2)=4392\), \(Z_2(3)=69\), \(Z_3(3)=2601\), \(Z_2(4)=172\), and \(Z_2(5)=345\).

## Relationship to prior work

The decomposition of **unrestricted** mutually annihilating matrix pairs was known, as explicitly recalled by Schröer [1, introduction], who then classifies the more specialized nilpotent pairs. Huang [5, Theorem 1.2 and Section 3] later gives a generating function for the unrestricted finite-field counts, without a self-adjoint constraint. Neither his decomposition of the full matrix pair space nor his nilpotent-pair theorem determines the self-adjoint fixed locus, its intersections, or the associated finite-field rank fibers. The individual symmetric-matrix rank formula is classical (MacWilliams; see [2]); no novelty is claimed for that factor alone. Brouwer, Gow, and Sheekey [3] enumerate **individual nilpotent self-adjoint** operators, whose counts may depend on the bilinear-form type; their theorem does not enumerate arbitrary self-adjoint zero-product pairs. Basili [4] treats commuting varieties with rank bounds, mentioning reducibility for symmetric matrices, but does not explicitly assert this product-zero rank stratification in the accessible abstract. Its complete text was not available for comparison. The contribution assessed here is the combined complete all-rank fiber census, all multiple-component intersections, and form-independent asymptotic for the product-zero self-adjoint locus. General zero-product matrix facts and classical symmetric-matrix counts are treated as prior knowledge.

## Limitations

No scheme-theoretic reducedness, singular-locus classification, individual isometry-conjugacy orbit classification, or mixed simultaneous Jordan-form classification is claimed. The algebraic geometry concerns the **reduced** variety. Full-text access to Basili [4] was unavailable, creating a specific historical-priority risk; a more general unpublished or unlocated self-adjoint incidence theorem could also imply the result. All scientific conclusions have been checked within the present argument, but no independent mathematical audit has been performed.

## References

[1] J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, first public preprint 2002-11-19, arXiv:math/0211293, introduction and Theorem 1.1. https://arxiv.org/abs/math/0211293

[2] J. B. Lewis, R. I. Liu, A. H. Morales, G. Panova, S. V. Sam, Y. X. Zhang, *Matrices with restricted entries and \(q\)-analogues of permutations*, first public preprint 2010-11-20, arXiv:1011.4539, Equation (4.5). https://arxiv.org/abs/1011.4539

[3] A. E. Brouwer, R. Gow, J. Sheekey, *Counting Symmetric Nilpotent Matrices*, Electronic Journal of Combinatorics 21(2) (2014), #P2.4, published 2014-04-01. https://doi.org/10.37236/3810

[4] R. Basili, *On the number of irreducible components of commuting varieties*, Journal of Pure and Applied Algebra 149 (2000), 121–126, DOI:10.1016/S0022-4049(99)00036-5. Abstract inspected; complete article not available.

[5] Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, first public preprint 2021-10-29, arXiv:2110.15566. https://arxiv.org/abs/2110.15566
