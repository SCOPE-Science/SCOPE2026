# Two-chain parameter bases have a rigid incomparable-pair type law

## Finding
Let \(\mathbb P\) be the countable universal homogeneous strict partial order. Let \(A=C_a\sqcup C_b\) be the disjoint union of individually named chains of lengths \(a,b\geq0\), with no relations between them. Count complete types of *ordered pairs of distinct points outside* \(A\). Write \(N\) for the number of complete nonalgebraic one-point types, \(C\) for the number of ordered pair types specifying \(x<y\), \(I\) for the number specifying \(x\perp y\), and \(T=2C+I\). Put
\[
N=\frac{a^2+b^2+4ab+3a+3b+2}{2},\qquad
H=a^3+b^3+6ab(a+b)+5(a^2+b^2)+14ab+8(a+b)+4.
\]
Then for all nonnegative integers \(a,b\),
\[
\boxed{C=\frac{2N^2+H}{6},\qquad I=\frac{N(2N+1)}3,\qquad T=\frac{4N^2+N+H}{3}.}
\]
In particular, the incomparable-pair count is determined *solely* by the one-type count, independently of the two chain lengths. The fraction \(2C/T\) of comparable ordered-pair types is strictly greater than \(1/2\) for every finite base, and approaches \(1/2\) whenever \(a+b\to\infty\) (with no required ratio or balance between the lengths).

## Assumptions and scope
Here a chain length is its number of vertices; an empty chain is permitted. All vertices of \(A\) are individually named. The structure is the Fraïssé limit of all finite strict posets, and extension diagrams are counted without quotienting by automorphisms of the named base. The two new variables are unequal and distinct from all parameters. The numbers count complete orbit/type diagrams, not the number of realising pairs in the infinite model. Exactly one of \(x<y\), \(y<x\), and \(x\perp y\) is recorded in each diagram.

## Proof
**Finite extension criterion.** Every one-point type over a finite poset is a pair \((L,U)\) with \(L\) an old down-set, \(U\) an old up-set, \(L\cap U=\varnothing\), and \(l<u\) for every \(l\in L,u\in U\). These describe precisely the predecessors and successors of the new point. Given two such types \((L,U)\) and \((K,V)\), a consistent finite extension with \(x<y\) exists exactly when \(L\subseteq K\) and \(V\subseteq U\). A consistent finite extension with \(x\perp y\) exists exactly when \(U\cap K=\varnothing\) and \(V\cap L=\varnothing\). Necessity is transitivity. For sufficiency, take the transitive closure of the prescribed finite relations: the conditions rule out unwanted new comparisons, and the ideal/filter conditions preserve the named induced subposet. The Fraïssé extension property then realises the diagram.

**Cut encoding.** On a named chain of length \(m\), the lower set of each new vertex is a prefix of length \(p\in\{0,\ldots,m\}\), and its upper set is the suffix after a cut \(q\in\{0,\ldots,m\}\). Disjointness means \(p\le q\). The cross-chain condition is that a type cannot have a nonempty lower set on one named chain and a nonempty upper set on the other. The elementary division into one-sided types and genuinely two-sided types yields
\[
N=2(a+1)(b+1)-1+\binom{a+1}{2}+\binom{b+1}{2}.
\]
For each pair of new points, introduce four cut coordinates \((p_x,q_x,p_y,q_y)\) on each old chain. The \(x<y\) condition is \(p_x\le p_y\) and \(q_x\le q_y\) in **both** chains. The \(x\perp y\) condition is \(p_y\le q_x\) and \(p_x\le q_y\) in **both** chains. Cross-chain restrictions on each unary type are solely endpoint/emptiness conditions. Thus all compatibility decisions are Boolean combinations of comparisons among four cuts and tests for the two boundary values.

**Polynomial certificate for all lengths.** Fix one possible weak order and boundary pattern of the four cuts in a chain of length \(m\ge1\). If it uses \(k\) distinct interior cut values, its number of realisations is \(\binom{m-1}{k}\), with \(0\le k\le4\). There are finitely many such patterns, independent of \(m\). Therefore \(C\) and \(I\) are bivariate polynomials of degree at most four *in each variable* on the positive quadrant \(a,b\ge1\); the same argument gives degree at most four on either positive coordinate axis when the other chain is empty. The finite program `verify.py` enumerates all valid cut patterns for the \(5\times5\) grid \(1\le a,b\le5\), and also for each axis length \(1,\ldots,5\) and the empty base, testing their values against the displayed polynomials. A bivariate polynomial of degree at most four in each variable is uniquely determined by its values on that grid; a degree-at-most-four univariate polynomial is determined by five values. Hence the formulas follow for **all** nonnegative integral chain lengths, not merely for the enumerated cases. The full finite loops and the degree argument together form the proof.

Finally, \(H-N\) has strictly positive coefficients when expanded in \(a,b\) (including a positive constant), so
\[
\frac{2C}{T}-\frac12=\frac{H-N}{2(4N^2+N+H)}>0.
\]
Since \(N\) grows quadratically and \(H\) cubically in \(a+b\), this difference tends to zero for every sequence with \(a+b\to\infty\).

## Verification
The standalone pure-Python certificate enumerates all 36 prescribed interpolation/boundary pairs and checks the three integer formulas, additionally checking seven outside-grid parameter pairs. An independent transitive-closure implementation checks 2,367 individual finite pair-diagram feasibility decisions for all \(0\le a,b\le2\), confirming that the cut tests neither create nor omit feasible diagrams. Executing `python3 verify.py` prints `VERIFICATION_OK`; `verification_output.txt` records the complete run. The finite computations become a general proof only in conjunction with the polynomial-degree argument above.

As examples, \((a,b)=(1,1)\) gives \((N,C,I,T)=(7,26,35,87)\), and \((a,b)=(2,2)\) gives \((19,161,247,569)\). For an empty base, there is one one-point type and exactly three ordered two-point types.

## Relationship to prior work
The generic partial order and its homogeneity are classical; Pach–Pinsker–Pluhár–Pongrácz–Szabó (2011) provide a modern model-theoretic treatment. Previously indexed results provide the one-type extremality of disjoint unions of at most two chains and the complete pair-type spectrum over a **single** named chain. The latter agrees with this theorem upon setting one chain length to zero, but does not by itself constrain the mixed cross terms for two nonempty chains. An indexed complete-height-two spectrum concerns a different family and does not imply the displayed factorisation. The new claim is the two-chain bivariate pair spectrum, particularly \(I=N(2N+1)/3\) and the uniform comparable-type limit, not Fraïssé homogeneity, the elementary unary-type encoding, or polynomial interpolation as a general method.

## Limitations
No assertion is made for arbitrary width-two posets: already the three-vertex fork has a different incomparable-pair law. The uniform probabilities refer to types, not to a probability measure on the infinite poset. The result is an exact enumeration, not an independence theorem for randomly realised elements. Published mathematical priority remains subject to further specialist literature comparison; no independent audit has been carried out.

## References
- P. P. Pach, M. Pinsker, G. Pluhár, A. Pongrácz, C. Szabó, *Reducts of the random partial order* (first arXiv version November 30, 2011), https://arxiv.org/abs/1111.7109.
- R. P. Stanley, order-polynomial theory, in *Enumerative Combinatorics, Volume 1* (1997), chapter on posets and order-preserving maps.
- Published online research record, *Order-polynomial spectra of tuple types over chains in the generic partial order* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-order-polynomial-spectra-of-tuple-types-over-chains-in-the-gener--67a71af3c8ab.
- Published online research record, *An incomparability-sensitive lower bound for one-point types of the generic poset* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-an-incomparability-sensitive-lower-bound-for-one-point-types-of--00a0cbd4584a.
