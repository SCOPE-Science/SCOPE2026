# Integral Euler lattice of scalar cyclic quotient planes

## Finding

Let \(n\geq3\), let \(\mu_n\) act on \(\mathbb A^2_{\mathbb C}\) by \(\zeta\cdot(x,y)=(\zeta x,\zeta y)\), and let \(Q_n\) be the Euler quadratic form of the quotient stack \(\mathcal A_n=[\mathbb A^2/\mu_n]\) in the character-multiplicity basis. Denote by \(H_n\) its integral **polar matrix**, defined by \(u^T H_n v=Q_n(u+v)-Q_n(u)-Q_n(v)\) for \(u,v\in\mathbb Z^n\). Then the full integral cokernel is
\[
\operatorname{coker}_{\mathbb Z}(H_n)\cong
\begin{cases}
\mathbb Z\oplus\mathbb Z/n\mathbb Z,&n\text{ odd},\\
\mathbb Z\oplus\mathbb Z/(2n)\mathbb Z,&n\equiv2\pmod4,\\
\mathbb Z^3\oplus\mathbb Z/(n/2)\mathbb Z,&n\equiv0\pmod4.
\end{cases}
\]
The inertia \((\nu_+,\nu_-,\nu_0)\) of the real symmetric polar matrix is, with \(m\) a nonnegative integer and \(n\geq3\),
\[
\begin{array}{c|c}
n&(\nu_+,\nu_-,\nu_0)\\ \hline
4m+1&(2m,2m,1)\\
4m+2&(2m+1,2m,1)\\
4m+3&(2m+2,2m,1)\\
4m\ (m\geq1)&(2m-1,2m-2,3).
\end{array}
\]
In particular, the radical jumps from dimension one to dimension three precisely when \(4\mid n\), and the form is indefinite for every \(n\geq5\). The small positive-semidefinite cases are \(n=3,4\).

## Assumptions and scope

All coefficient modules and cokernels are over \(\mathbb Z\); the inertia is over \(\mathbb R\). The polar matrix is **twice** the symmetric matrix representing \(Q_n\) as \(u^T A_nu\), so the Smith invariants specify the normalization without ambiguity. The theorem concerns the canonical scalar action, not all cyclic weight pairs, all planar quotient stacks, or connected components of Hilbert schemes. It does not assert that the Euler lattice's torsion classes correspond to geometric torsion sheaves.

## Proof

**Euler form and polar matrix.** The coefficient formula in Bachhuber--Gholampour, Theorem 4.6, specializes to
\[
Q_n(a)=\sum_{j\bmod n}(a_j-a_{j+1})^2-\frac12\sum_{j\bmod n}(a_j-a_{j+2})^2.
\]
The formula holds also at \(n=3,4\) when steps coincide modulo \(n\), because the sums are taken with their indicated multiplicities. Expanding gives
\[
Q_n(a)=\sum_j a_j^2-2\sum_j a_ja_{j+1}+\sum_j a_ja_{j+2}.
\]
Let \(S\) act on \(\mathbb Z^n\) by cyclic shift. Polarization yields
\[
H_n=2I-2(S+S^{-1})+(S^2+S^{-2})
       =S^{-2}(S-1)^2(S^2+1).
\]
The last factorization is an identity in the integral group algebra of the cyclic group, including at small \(n\).

**Integral Smith calculation.** Put \(f(t)=(t-1)^2(t^2+1)=t^4-2t^3+2t^2-2t+1\). The automorphism \(S^{-2}\) is integral unimodular. Therefore
\[
\operatorname{coker}(H_n)\cong\mathbb Z[t]/(t^n-1,f(t)).
\]
Since \(f\) is monic of degree four, \(\mathbb Z[t]/(f)\) is free of rank four with basis \(1,t,t^2,t^3\). Multiplication by \(t\) has companion matrix
\[
C=\begin{pmatrix}0&0&0&-1\\1&0&0&2\\0&1&0&-2\\0&0&1&2\end{pmatrix}.
\]
Thus \(\operatorname{coker}(H_n)\cong\operatorname{coker}(C^n-I_4)\). Direct multiplication gives
\[
B=C^4-I_4=2vw^T,\qquad v=(-1,1,-1,1)^T,\quad w=(1,1,1,1)^T,
\]
and \(B^2=0\). Hence for \(n=4m+r\), \(0\leq r\leq3\),
\[
C^n-I_4=(C^r-I_4)+mC^rB.
\]
For \(r=0\), this is \(2m v w^T\), with Smith form \(\operatorname{diag}(2m,0,0,0)\).

For \(r=1,2,3\), the common right nullvector is \(v\) and common left nullvector is \(w\); rank is exactly three because \(\gcd(f(t),t^n-1)=t-1\) over \(\mathbb Q[t]\) whenever \(4\nmid n\). The \(3\)-by-\(3\) principal minor on rows and columns \(0,1,2\) equals, respectively,
\[
-(4m+1),\qquad-4(2m+1),\qquad-(4m+3).
\]
All maximal minors have the same absolute value as that principal minor: the adjugate of a rank-three matrix has the form \(dvw^T\), and all entries of \(v,w\) are signs. Moreover, unit \(2\)-by-\(2\) minors are furnished by rows/columns (indexed from zero)
\[
\begin{array}{c|c|c|c}
r&\text{rows}&\text{columns}&\text{determinant}\\\hline
1&(0,2)&(0,1)&-1\\
2&(0,1)&(0,1)&1\\
3&(0,2)&(0,3)&1.
\end{array}
\]
The first two determinantal divisors are thus one, and the third is \(n\), \(2n\), or \(n\) for remainders \(1,2,3\). The fourth is zero. By the determinantal-divisor characterization of Smith normal form, these give the displayed integral cokernels for every \(n\).

**Real inertia.** The Fourier modes \(j\mapsto e^{2\pi i k j/n}\) diagonalize \(H_n\). With \(\theta=2\pi k/n\), its eigenvalue is
\[
2-4\cos\theta+2\cos(2\theta)=4\cos\theta(\cos\theta-1).
\]
For \(k=0\), it vanishes. For \(0<k<n\), the factor \(\cos\theta-1\) is strictly negative. Thus the eigenvalue is negative when \(\cos\theta>0\), positive when \(\cos\theta<0\), and zero when \(\cos\theta=0\). The latter occurs for the two additional modes \(k=n/4,3n/4\) exactly when \(4\mid n\). Counting these three cases in the four residue classes gives the inertia table. This also proves the indicated semidefinite and indefinite boundaries.

## Verification

The accompanying standard-library program `verify_euler.py` checks the exact 4-by-4 Smith determinantal divisors for each \(3\le n\le128\), independently constructs the polar matrices for \(3\le n\le40\), and verifies the polarization identity on integer test vectors. Run `python3 verify_euler.py` from the directory containing this document. It prints `EXACT_VERIFICATION_OK` on success. The infinite statements follow from the symbolic proof above, not from these finite tests.

## Relationship to prior work

Bachhuber--Gholampour, *G-Equivariant Hilbert Schemes and Quadratic Forms*, arXiv:2610.12736 (first public 2026-10-08), derives the Euler form and classifies scalar antidiagonal actions among planar quotient stacks. The results above calculate the **integral polar lattice** and **complete inertia**, rather than restating those coefficient formulas or grouping types. In particular the three-dimensional radical on \(4\)-divisible orders and the cyclic torsion of exact order \(n/2\), \(n\), or \(2n\) are additional integral and real invariants. The general companion-matrix Smith-form methodology studied by Noferini--Williams (arXiv:2408.08662) is related in technique; their general tools do not themselves state the explicit scalar-action formulas derived here. Williams' work on ordinary circulant-graph adjacency Smith forms (DOI:10.1016/j.laa.2013.11.006) addresses different matrices; the present matrix is a signed weighted two-step Laplacian rather than one of the specified unsigned adjacency matrices.

## Limitations

The theorem is confined to scalar cyclic actions and to the Euler polar form. It neither classifies all cyclic representations nor determines connected components or cohomology of equivariant Hilbert schemes. A directly equivalent formula may exist in non-indexed material; the accessible literature comparison cannot establish absolute priority. Finite checks are only supporting tests. The Williams adjacency-matrix PDF could not be read in full; its abstract and introductory extract were inspected and the possibility of an implicit equivalent calculation remains a residual literature risk.

## References

1. S. J. Bachhuber and A. Gholampour, *G-Equivariant Hilbert Schemes and Quadratic Forms* (2026), arXiv:2610.12736, https://arxiv.org/html/2610.12736v1 (Theorem 4.6 and Sections 6--7).
2. V. Noferini and G. Williams, *Smith forms of matrices in companion rings, with group theoretic and topological applications* (2024), arXiv:2408.08662, https://arxiv.org/abs/2408.08662.
3. G. Williams, *Smith forms for adjacency matrices of circulant graphs*, Linear Algebra and Its Applications 443 (2014), 21--33, DOI:10.1016/j.laa.2013.11.006; open repository https://repository.essex.ac.uk/8578/.
