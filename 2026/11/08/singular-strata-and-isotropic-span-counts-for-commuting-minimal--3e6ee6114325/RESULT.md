# Singular strata and isotropic-span counts for commuting minimal symplectic nilpotents

## Finding
Let \(n,r\ge1\), \(V\) a \(2n\)-dimensional symplectic vector space over a field \(k\) of characteristic different from two, and \(\omega\) its nondegenerate alternating form. Define the reduced affine variety \(\mathcal M_{n,r}\) to consist of ordered tuples \((X_1,\dots,X_r)\) in \(\mathfrak{sp}(V)^r\) with \(\operatorname{rank}X_i\le1\) and \([X_i,X_j]=0\) for all indices. Every nonzero such operator automatically has square zero and belongs to the minimal nonzero nilpotent orbit over an algebraic closure.

For a point set \(t=\#\{i:X_i\ne0\}\) and \(s=\dim\sum_i\operatorname{im}X_i\). One always has \(0\le s\le\min(n,t)\), with \(s=0\) iff \(t=0\). The variety is geometrically irreducible, of dimension
\[
 d_{n,r}=\begin{cases}2nr-\binom{r}{2},&r\le n,\\nr+\frac{n(n+1)}2,&r>n.\end{cases}
\]
Its *geometric Zariski tangent dimension* at a point of invariants \((t,s)\) is
\[
 \boxed{\dim T=r(2n-s)+\binom{s+1}{2}+(r-t)\binom{2n-s}{2}.}
\]
It is smooth precisely when:

- \(n=1\) and \(t\ge1\);
- \(n\ge2\), \(r\le n\), \(t=r\) and \(s\ge r-1\);
- \(n\ge2\), \(r>n\), \(t=r\) and \(s=n\).

The geometry is particularly sensitive to *zero coordinates*: for \(n\ge2\), a single zero entry forces singularity even when the nonzero operators span a maximal isotropic space.

For every odd prime power \(q\), define \(I_{n,0}(q)=1\) and
\[
 I_{n,s}(q)=\prod_{j=0}^{s-1}\frac{q^{2(n-j)}-1}{q^{s-j}-1}.
\]
Then the exact number of rational tuples having image-span dimension \(s\) is
\[
 \boxed{I_{n,s}(q)\prod_{j=0}^{s-1}(q^r-q^j)}
\]
for \(0\le s\le\min(n,r)\) and zero otherwise; empty products are one. This is a span-refined count, not merely a total point count.

## Assumptions and scope
The underlying scheme is always **reduced**. The geometric tangent and smoothness statements are made after extension to an algebraic closure and are invariant under base change. No assertion is made about the nonreduced scheme defined naively by all minors and commutators. For finite-field enumeration, \(k=\mathbb F_q\) with \(q\) odd; the form is alternating and nondegenerate. The integer \(r\) is independent of the symplectic half-dimension \(n\).

## Proof
**1. Parametrizing minimal symplectic nilpotents.** The symplectic Lie algebra identifies with symmetric bilinear tensors via \(X\mapsto\omega(X\cdot,\cdot)\). A nonzero rank-one member has the form \(X=a\,u\otimes\omega(u,\cdot)\), where \(u\ne0\) and \(a\ne0\). Every such operator has square zero. Direct multiplication gives \(X_uX_v=\omega(u,v)u\otimes\omega(v,\cdot)\), and the commutator vanishes exactly when \(\omega(u,v)=0\). When \(u,v\) are independent, the two opposite rank-one terms cannot cancel unless \(\omega(u,v)=0\); when dependent the pairing already vanishes. Geometrically, over an algebraic closure, the map \(u\mapsto X_u\) realizes the rank-at-most-one cone as the quotient of \(V\) by \(u\mapsto-u\). The multituple variety is the coordinatewise sign quotient of the symplectic isotropy nullcone
\[
 Z_{n,r}=\{(u_1,\ldots,u_r)\in V^r:\omega(u_i,u_j)=0\text{ for all }i,j\}.
\]
Since the sign group has order \(2^r\), invertible in \(k\), its invariant ring commutes with passing to this reduced closed subscheme. This proves the claimed quotient description, including its reduced structure.

**2. Irreducibility and dimension.** Fix an isotropic \(s\)-plane \(U\subset V\). Tuples of rank-one operators with images in \(U\) form a product of the quadratic Veronese cones of \(U\); the locus of tuples whose images span \(U\) is a nonempty open subset, irreducible of dimension \(rs\). The isotropic Grassmannian of \(s\)-planes has dimension \(s(2n-s)-\binom{s}{2}\). Thus the span-\(s\) stratum is irreducible of dimension \(rs+s(2n-s)-\binom{s}{2}\). This increases strictly up to \(s=\min(n,r)\). Every isotropic span is contained in a Lagrangian, so the image of the proper incidence space over the Lagrangian Grassmannian, with irreducible Veronese-cone fibers, is all of \(\mathcal M_{n,r}\). The incidence space is irreducible; hence so is its image. Taking the maximum stratum dimension gives the displayed \(d_{n,r}\). The irreducibility and dimension of the unquotiented vector isotropy nullcone are also part of established symplectic-nullcone theory [3], [4]; they are not asserted as a novel independent result.

**3. Tangent dimension at points with zero coordinates.** Let \(t\) coordinates be nonzero, spanning an isotropic subspace \(U\) of dimension \(s\), and let \(z=r-t\). For each nonzero coordinate, the quadratic Veronese covering is étale in odd characteristic. Linearizing the \(\binom t2\) pairings on the nonzero lifting vectors gives rank exactly \(st-\binom{s+1}2\): after choosing \(s\) independent vectors, the only free first-order pairings among the selected vectors form a skew-symmetric matrix, and the remaining \(t-s\) columns contribute \(s(t-s)\) independent constraints. Thus the nonzero-coordinate tangent dimension is \(t(2n-s)+\binom{s+1}2\).

At a zero coordinate, the rank-one cone has tangent space the entire space of symmetric tensors on \(V\), of dimension \(n(2n+1)\); the linearized commutators with nonzero coordinates force the first-order operator to annihilate \(U\). Under the \(\mathfrak{sp}(V)\cong\operatorname{Sym}^2V\) identification, this is \(\operatorname{Sym}^2(U^\perp)\), of dimension \(\binom{2n-s+1}2\). Equivalently, rank-one tangent directions \(w\otimes\omega(w,\cdot)\) with \(w\in U^\perp\) span that space, so the linearized directions genuinely belong to the reduced variety, not only to an overly large presentation scheme. Linearized constraints between two zero coordinates vanish. Tangent contributions are therefore independent, giving
\[
 \dim T=t(2n-s)+\binom{s+1}2+z\binom{2n-s+1}2
       =r(2n-s)+\binom{s+1}2+z\binom{2n-s}2.
\]

**4. Smoothness inequalities.** If \(z=0\) and \(r\le n\), subtraction from the global dimension gives \(\dim T-d_{n,r}=\binom{r-s}2\), which vanishes exactly for \(s\ge r-1\). If \(z=0\) and \(r>n\), the difference is \((n-s)(r-(n+s+1)/2)\), zero exactly at \(s=n\). When \(n\ge2\) and \(z>0\), the extra term \(z\binom{2n-s}2\) is strictly positive and the baseline difference is nonnegative, so the point is singular. When \(n=1\), every tuple having a nonzero entry has \(s=1\) and tangent dimension \(r+1\), equal to \(d_{1,r}\); the all-zero tuple has tangent dimension \(3r>r+1\) except for a vacuous excluded range, and is singular. Since the variety is geometrically irreducible and reduced, equality of tangent and local dimensions characterizes smoothness here.

**5. Finite fields.** The number of totally isotropic \(s\)-planes is \(I_{n,s}(q)\), obtained by counting ordered isotropic independent frames and dividing by \(|\operatorname{GL}_s(q)|\). In a fixed \(j\)-space \(W\), there are exactly \(q^j\) symplectic rank-at-most-one operators with image in \(W\): one zero and \(q-1\) operators for each of \((q^j-1)/(q-1)\) projective lines. Möbius inversion on the subspace lattice shows that the number of \(r\)-tuples whose images span a fixed \(s\)-plane is \(\prod_{j=0}^{s-1}(q^r-q^j)\). Multiplication by \(I_{n,s}(q)\) proves the formula. This counts operators directly and does not assume that every finite-field scalar has a square root.

## Verification
The standalone programs `checks/finite_counts.py` and `checks/tangent_rank.py` use explicit symplectic forms and finite-field matrix multiplication. The first exhausts all permitted rank-at-most-one operators in each stated test and compares commuting tuples, supports, and exact predictions. The second forms actual first-order commutator matrices and independently measures tangent ranks. Recorded reproducible outputs are `checks/finite_counts.txt` and `checks/tangent_rank.txt`. The tests are finite consistency checks; all-characteristic and all-size statements rely on the proof above.

## Relationship to prior work
Premet [1] proves equidimensionality for the **full** nilpotent commuting variety of pairs in reductive Lie algebras; restricting both entries to the minimal rank-one symplectic cone is not a statement of that theorem. Ngo [2] investigates mixed commuting varieties in low-rank simple Lie algebras, different from the present uniform \(\mathfrak{sp}_{2n}\) all-tuple smooth-locus classification. Pandey–Tarasova–Walther [3,4] explicitly treat symplectic isotropy **vector** nullcones, whose irreducibility and dimension are prior coverage here; passing to the coordinatewise rank-one endomorphism quotient creates new singular strata at zero coordinates. Ngo–Levy–Šivic [5] treats unrestricted nilpotent commuting tuples in matrix Lie algebras; the minimal symplectic endomorphism quotient and its tangent strata are not directly given. Classical isotropic Grassmannian counts and subspace-lattice inversion are also used as known tools, rather than claimed as new results. No independent historical-priority audit has been performed.

## Limitations
The result is for the reduced variety, characteristic different from two, and rank-at-most-one elements in a symplectic Lie algebra; neither higher-rank nilpotents nor the nonreduced commutator scheme are covered. The arithmetic support distribution is derived from classical finite geometry and is an accompanying exact interpretation, not claimed separately as an unprecedented enumerative identity. A broad theorem about singular strata of sign quotients of symplectic nullcones might imply the main new smooth-locus statement; the searched sources did not settle this possibility. Only the explicitly listed finite-field instances were exhaustively checked.

## References
[1] A. Premet, *Nilpotent commuting varieties of reductive Lie algebras*, arXiv:math/0302204v1 (18 February 2003), https://arxiv.org/html/math/0302204v1.

[2] N. V. Ngo, *Mixed Commuting Varieties over simple Lie algebras*, arXiv:1301.2712v1 (12 January 2013), https://arxiv.org/abs/1301.2712.

[3] V. Pandey, Y. Tarasova and U. Walther, *On the natural nullcones of the symplectic and general linear groups*, arXiv:2310.01816v1 (3 October 2023), https://arxiv.org/abs/2310.01816.

[4] V. Pandey, Y. Tarasova and U. Walther, *On the natural nullcones of the symplectic and general linear groups*, Journal of the London Mathematical Society 111 (2025), e70078, https://doi.org/10.1112/jlms.70078.

[5] N. V. Ngo, P. D. Levy and K. Šivic, *Commuting varieties and cohomological complexity*, arXiv:2105.07918v1 (2021), https://arxiv.org/abs/2105.07918.
