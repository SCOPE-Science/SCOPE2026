# Isomorphism spectrum and square-root growth of finite diamond preconditionals

## Finding
Let \(M_m\) be the bounded lattice consisting of a bottom, a top, and exactly \(m\ge2\) incomparable atoms. A preconditional is a binary operation satisfying axioms (P1)–(P5) below. Write \(U_m\) for the number of isomorphism types of expanded algebras \((M_m,\to)\); unlike labeled expansion counts, isomorphisms are permitted to permute all atoms.

For every partition \(\lambda\vdash m\), write \(c_d(\lambda)\) for the multiplicity of part \(d\), and \(z_\lambda=\prod_{d\ge1}d^{c_d(\lambda)}c_d(\lambda)!\). Then the exact isomorphism spectrum is
\[
 U_m=(m+1)^2+\sum_{\lambda\vdash m}\frac1{z_\lambda}
 \prod_{d\ge1}\left(3+\sum_{e\mid d}e\,c_e(\lambda)\right)^{c_d(\lambda)}.
\]
Its first values for \(m=2,3,4,5,6,7,8,9,10\) are respectively
\(24,66,186,533,1562,4592,13532,39778,116724\).

This spectrum has a canonical combinatorial description: apart from \((m+1)^2\) exceptional types, it counts unlabelled finite functional digraphs in which each vertex is either a terminal of one of four colors or points to a *different* vertex. Let \(T(z)\) be the ordinary generating function for unlabelled rooted trees, uniquely specified by
\[
 T(z)=z\exp\left(\sum_{r\ge1}\frac{T(z^r)}r\right).
\]
Set
\[
 C(z)=\sum_{\ell\ge2}\frac1\ell\sum_{d\mid\ell}\varphi(d)T(z^d)^{\ell/d},\qquad
 A(z)=\exp\left(\sum_{r\ge1}\frac{4T(z^r)+C(z^r)}r\right).
\]
Then \(U_m=(m+1)^2+[z^m]A(z)\) for \(m\ge2\).

There is also a sharp asymptotic law. Let \(\rho\) be the dominant Otter singularity of \(T\), so \(\rho\approx0.3383218569\), \(T(\rho)=1\), and \(T(z)=1-b\sqrt{1-z/\rho}+O(1-z/\rho)\) for a positive constant \(b\). Define
\[
 H(z)=\sum_{\ell\ge2}\frac1\ell\sum_{\substack{d\mid\ell\\d\ge2}}\varphi(d)T(z^d)^{\ell/d},\qquad
 R(z)=\sum_{r\ge2}\frac{4T(z^r)+C(z^r)}r.
\]
Both \(H\) and \(R\) are analytic in a disk of radius strictly greater than \(\rho\). With the positive finite constant
\[
 K=\frac{\exp(3+H(\rho)+R(\rho))}{b\sqrt\pi},
\]
we obtain
\[
 U_m\sim K\rho^{-m}m^{-1/2}\quad(m\to\infty).
\]
Thus the isomorphism types exhibit a square-root *pole*, rather than the square-root *zero* characteristic of ordinary rooted-tree counts.

## Assumptions and scope
The carrier is exactly \(M_m=\{0,1,a_1,\ldots,a_m\}\), ordered so that \(0<a_i<1\) and distinct atoms are incomparable. For \(x,y,z\in M_m\), the operation \(\to\) satisfies Holliday's preconditional axioms:
\[
 \begin{aligned}
 (\mathrm{P1})&\quad 1\to x\le x,\\
 (\mathrm{P2})&\quad x\wedge y\le x\to y,\\
 (\mathrm{P3})&\quad x\to y\le x\to(x\wedge y),\\
 (\mathrm{P4})&\quad x\to(y\wedge z)\le x\to y,\\
 (\mathrm{P5})&\quad x\to((x\wedge y)\to z)\le (x\wedge y)\to z.
 \end{aligned}
\]
Only these five axioms are assumed; stronger conditional systems, orthocomplementations, and labeled operation counts are different questions. An isomorphism must preserve \(\wedge,\vee,0,1,\to\), so its underlying lattice map is exactly an atom permutation in \(S_m\).

## Proof
**Reduction to the row parameters.** Axioms (P3) and (P4) imply \(x\to y=x\to(x\wedge y)\) (the reverse inequality follows by (P4)). The top row is the identity by (P1), (P2), and (P4). The bottom row is a constant \(w=0\to0\). For an atomic row \(a_i\), write \(u_i=a_i\to0\) and \(v_i=a_i\to a_i\). Its other entries equal \(u_i\), and its two entries at \(a_i\) and at \(1\) equal \(v_i\). Axiom (P2) forces \(v_i\in\{a_i,1\}\) and \(u_i\le v_i\). Substitution into (P5) gives exactly the two remaining conditions
\[
 a_i\to u_i\le u_i,\qquad a_i\to w\le w.
\]
Conversely, these row parameters and the two displayed inequalities imply all five axioms: (P1)–(P4) are built into the row structure; for (P5), when the first argument is an atom, its meet with the second is either \(0\) or that atom, which are precisely the two inequalities. The top and bottom rows satisfy (P5) automatically under the same conditions.

**Three disjoint families.** If \(w=0\), each atomic row has exactly two choices, \((u_i,v_i)=(0,a_i)\) or \((0,1)\). Up to atom permutations this gives \(m+1\) types, classified by the number of rows of the second kind.

If \(w=a_j\) is an atom, the distinguished row has exactly two choices, \((0,a_j)\) or \((a_j,a_j)\). Every other row has exactly three choices, \((0,a_i),(0,1),(a_j,1)\). Up to permutations fixing \(a_j\), there are \(2\binom{m+1}{2}=m(m+1)\) types.

If \(w=1\), an atomic row has exactly four terminal forms \((0,a_i),(a_i,a_i),(0,1),(1,1)\), or one arrow form \((a_j,1)\) for a uniquely chosen \(j\ne i\). Thus these operations are bijective with labeled directed functional configurations: each atom is a sink of one of four colors or has exactly one outgoing arrow to another atom. Atom permutations act as graph relabelings, so the isomorphism classes in this family are exactly their unlabelled isomorphism types. The first two families contribute \((m+1)+m(m+1)=(m+1)^2\).

**Burnside formula.** Fix an atom permutation \(\sigma\) with \(c_d\) cycles of length \(d\). A \(\sigma\)-equivariant configuration is specified separately on each domain cycle of length \(d\): it is a sink with any of four colors, or an outgoing arrow whose target is fixed by \(\sigma^d\) and differs from the chosen representative vertex. The latter set has cardinality \(\sum_{e\mid d}e c_e-1\). Hence this cycle contributes \(3+\sum_{e\mid d}e c_e\) independent possibilities. Burnside's lemma, grouping permutations by cycle type, yields the boxed partition formula.

**Component generating function.** An unlabelled connected functional configuration is either a rooted unlabelled tree with one of four terminal colors or a directed cycle of length at least two with a rooted tree attached at each cycle vertex. Rooted-tree decomposition gives \(T(z)\); Pólya's cyclic-index calculation for the latter components gives \(C(z)\). Arbitrary multisets of connected components then have the ordinary generating function \(A(z)\), using the standard multiset exponential formula displayed in the finding.

**Asymptotic singularity.** Split the divisor \(d=1\) from the expression for \(C(z)\). The sum over cycle lengths at least two gives
\[
 C(z)=-\log(1-T(z))-T(z)+H(z).
\]
Consequently,
\[
 A(z)=\frac{\exp(3T(z)+H(z)+R(z))}{1-T(z)}.
\]
The standard Otter analysis gives \(T(\rho)=1\) and a square-root expansion with coefficient \(b>0\), together with a unique dominant singularity and a slit neighborhood suitable for coefficient transfer. Since every composition \(T(z^d)\) in \(H\) has \(d\ge2\), and every composition \(T(z^r),C(z^r)\) in \(R\) has \(r\ge2\), these auxiliary series are analytic beyond \(|z|=\rho\). Therefore
\[
 A(z)=\frac{\exp(3+H(\rho)+R(\rho))}{b}(1-z/\rho)^{-1/2}+O(1).
\]
The transfer theorem gives \([z^m]A(z)\sim K\rho^{-m}m^{-1/2}\). The additive polynomial \((m+1)^2\) is asymptotically negligible.

## Verification
The standalone `verification/exhaustive.py` explicitly enumerates the candidate operations and tests all five axioms on every triple for \(m=2,3,4\), then computes canonical representatives under all lattice automorphisms. It obtains labeled counts \(41,278,2633\) and isomorphism counts \(24,66,186\); it also independently evaluates the Burnside partition formula for \(m=5,\ldots,10\).

A separate computation, `verification/component_series.py`, computes the unlabelled rooted-tree coefficients, cycle-connected components, and the Euler multiset transform using exact rational arithmetic. It recovers via a different method the same isomorphism counts through \(m=10\). These finite checks support the constructive combinatorics but do not replace the Burnside/Pólya or analytic proofs for arbitrary \(m\).

To reproduce, from the directory containing this document run `python verification/exhaustive.py` and `python verification/component_series.py` with a standard Python 3 interpreter. Both scripts terminate with `VERIFY_OK` on success.

## Relationship to prior work
Holliday introduced the preconditional axioms and representation theory; Chen developed their connection with fundamental propositional logic and supplied the recent algebraic motivation. A previous **labeled** row-normal-form classification for finite diamond preconditionals yields the count \((m+3)^m+2^m+2m3^{m-1}\); that labeled classification is treated here as prior mathematics, not as part of the novelty claim. The present claim concerns the isomorphism quotient, the functional-digraph interpretation, the exact cycle-index spectrum, and the resulting asymptotic law. Otter's rooted-tree singularity and standard cycle-index/multiset techniques are classical inputs and are not claimed as new.

## Limitations
Only the five-axiom preconditional class on this particular height-two lattice family is covered. This theorem does not classify arbitrary lattices or stronger conditional axioms. The finite scripts certify only the tested sizes; they do not independently certify the asymptotic transfer. An equivalent quotient enumeration might exist in nonindexed literature; priority has not been independently audited.

## References
1. W. H. Holliday, *Preconditionals*, arXiv:2402.02296 (first posted 2024-02-03), particularly Definition 1 and the five axioms, https://arxiv.org/abs/2402.02296.
2. Z. Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221 (first posted 2026-07-22), https://arxiv.org/abs/2607.20221.
3. R. Otter, *The number of trees*, Annals of Mathematics 49 (1948), 583–599, for the rooted-tree asymptotic and dominant square-root singularity. For a modern treatment of unlabelled tree singularities, see https://www.cs.ubc.ca/sites/default/files/tr/2000/TR-2000-04_0.pdf.
