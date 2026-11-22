# Full Frobenius spectra and quadratic rank detection for minimum-degree space-filling hypersurfaces

## Finding
Let \(q\) be a prime power, \(N\ge 2\), and \(X\subset\mathbb P^{N-1}_{\mathbb F_q}\) a nonzero degree-\(q+1\) hypersurface containing every \(\mathbb F_q\)-rational point of its ambient projective space. Its alternating coefficient matrix has even rank \(2r\), where \(1\le r\le\lfloor N/2\rfloor\). Put \(k=N-2r\) and
\[
 b_r=\frac{q^{2r}+q}{q+1},\qquad
 u_r=\frac{b_r+q^r}{2},\qquad
 v_r=\frac{b_r-q^r}{2}.
\]
Then the entire Hasse–Weil zeta function is
\[
 Z(X,T)=\left(\prod_{j=0}^{k-1}(1-q^jT)^{-1}\right)
 \left(\prod_{i=0}^{2r-2}(1-q^{k+i}T)^{-1}\right)
 (1-q^{k+r-1}T)^{-u_r}(1+q^{k+r-1}T)^{-v_r}.
\]
Products with empty index sets equal one. In particular,
\[
 \#X(\mathbb F_{q^2})=\sum_{j=0}^{N-2}q^{2j}
 +\frac{q^{2N-2}+q^{2N-2r-1}}{q+1}.
\]
The quadratic-extension count determines \(r\) uniquely for fixed \(q,N\), and hence determines the \(\mathbb F_q\)-projective equivalence class among degree-\(q+1\) space-filling hypersurfaces. In contrast, all these hypersurfaces have the same \(\mathbb F_q\)-point set, namely all of \(\mathbb P^{N-1}(\mathbb F_q)\).

## Assumptions and scope
The finite field has order \(q=p^a\), with no characteristic restriction. The ambient projective space has dimension \(N-1\ge1\); the hypersurface may be singular or reducible. Its defining polynomial is nonzero, homogeneous of degree \(q+1\), and vanishes at every base-field projective point. The coefficient matrix is the unique alternating matrix of the form \(F(x)=x^{(q)t}Ax\), up to the chosen sign convention and an overall nonzero scalar. The rank \(2r\) is independent of coordinates. The claim describes ordinary point-count zeta functions, not scheme-theoretic or motivic zeta functions.

## Proof
**1. Alternating normal form and cone geometry.** The degree-\(q+1\) component of the homogeneous ideal of \(\mathbb P^{N-1}(\mathbb F_q)\) is spanned by \(x_i^qx_j-x_ix_j^q\), as recorded in the initiating paper, Section 3. Consequently \(F=x^{(q)t}Ax\) with \(A\) alternating over \(\mathbb F_q\). Standard alternating-form congruence produces an \(\mathbb F_q\)-linear coordinate change under which
\[
 F=\sum_{j=1}^{r}(x_{2j-1}^q x_{2j}-x_{2j-1}x_{2j}^q),
\]
with \(k=N-2r\) unused coordinates. The hypersurface is the projective cone over the smooth hypersurface \(H_r\subset\mathbb P^{2r-1}\) given by the displayed expression using its first \(2r\) variables; the vertex is \(\mathbb P^{k-1}\) if \(k>0\). For every finite extension \(\mathbb F_Q/\mathbb F_q\), decomposing cone points according to their nonzero base block gives the exact count
\[
 \#X(\mathbb F_Q)=\sum_{j=0}^{k-1}Q^j+Q^k\#H_r(\mathbb F_Q).
\tag{1}
\]
The base \(H_r\) is smooth because its gradient is \(A(x_1^q,\ldots,x_{2r}^q)^t\), which cannot vanish at a projective point for nonsingular \(A\). This remains true when \(r=1\), when \(H_1\) comprises \(q+1\) distinct base-field points.

**2. Hermitian comparison and maximal quadratic trace.** Choose a nonzero \(\lambda\in\mathbb F_{q^2}\) with \(\lambda^q=-\lambda\). In odd characteristic take a nonzero trace-zero element; in characteristic two take \(\lambda=1\). Since \(A^{(q)t}=-A\), the matrix \(\lambda A\) is Hermitian over \(\mathbb F_{q^2}\). Thus \(H_r\) becomes a nondegenerate Hermitian hypersurface over the quadratic extension. The classical Hermitian point formula gives
\[
 \#H_r(\mathbb F_{q^2})
 =\frac{(q^{2r}-1)(q^{2r-1}+1)}{q^2-1}.
\]
Subtracting \(\#\mathbb P^{2r-2}(\mathbb F_{q^2})\) simplifies to
\[
 \#H_r(\mathbb F_{q^2})-\sum_{i=0}^{2r-2}q^{2i}=b_r q^{2r-2}.
\tag{2}
\]
The standard smooth-hypersurface cohomology calculation gives precisely \(b_r\) primitive middle étale-cohomology eigenvalues (for \(r=1\), use reduced degree-zero cohomology). Purity bounds the absolute value of every \(q^2\)-Frobenius eigenvalue by exactly \(q^{2r-2}\); equation (2) says their sum equals \(b_r q^{2r-2}\). Equality in the triangle inequality therefore forces each squared \(q\)-Frobenius eigenvalue to be \(q^{2r-2}\). Each primitive \(q\)-Frobenius eigenvalue is consequently \(+q^{r-1}\) or \(-q^{r-1}\).

**3. Recover the two multiplicities.** Every \(\mathbb F_q\)-point lies on \(H_r\), so
\[
 \#H_r(\mathbb F_q)-\#\mathbb P^{2r-2}(\mathbb F_q)=q^{2r-1}.
\]
The primitive eigenvalue trace is therefore \(q^{2r-1}\). If positive and negative multiplicities are \(u_r,v_r\), then \(u_r+v_r=b_r\) and \((u_r-v_r)q^{r-1}=q^{2r-1}\). Solving gives exactly the stated \(u_r,v_r\). Thus
\[
 \#H_r(\mathbb F_{q^s})=\sum_{i=0}^{2r-2}q^{is}
 +q^{(r-1)s}\bigl(u_r+(-1)^s v_r\bigr),\qquad s\ge1.
\tag{3}
\]
Substitute (3) into (1) and exponentiate the formal identity \(Z(Y,T)=\exp(\sum_{s\ge1}\#Y(\mathbb F_{q^s})T^s/s)\) to obtain the announced full zeta function.

**4. Quadratic rank detection.** Use (1) and (2), and separate the ambient projective-space count, to get
\[
 \#X(\mathbb F_{q^2})-\#\mathbb P^{N-2}(\mathbb F_{q^2})
 =q^{2k+2r-2}b_r
 =\frac{q^{2N-2}+q^{2N-2r-1}}{q+1}.
\]
For fixed \(q,N\), the second numerator term is strictly decreasing as integer \(r\) increases; hence no two allowed ranks have the same count. Finally, alternating forms over a finite field are congruent if and only if they have the same rank, proving the projective-class assertion.

## Verification
The accompanying standalone `verify.py` implements finite fields exactly, enumerates unique projective-coordinate representatives, and checks the theorem on 14 finite instances, including smooth cases, singular cones, characteristic two, odd characteristic, and odd/even extension degrees through four. For example, in ambient \(\mathbb P^3_{\mathbb F_2}\), smooth rank-four and singular rank-two models both have 15 base-field points but respectively 45 and 53 quadratic-extension points. For the smooth quartic surface over \(\mathbb F_3\), the quadratic-extension count is 280. These are finite consistency checks, not the proof of the uniform statement.

## Relationship to prior work
Bourgeois-Conti, Moon, Perez and Warren establish the minimal-degree alternating matrix normal form and the smoothness criterion; those are inputs, not claimed discoveries. Homma–Kim previously classified extremal nonsingular examples up to projectivity. Bose–Chakravarti's Hermitian point-count theorem and its degenerate-rank corollary already imply the quadratic-extension count after identification with a Hermitian form. Therefore the quadratic count **alone is not claimed as a new invariant computation**. The additional result here is a unified formula for the **entire base-field Frobenius spectrum and all extension degrees**, across every alternating rank, obtained by combining the Hermitian equality case with purity and the base-field trace; the rank-detection interpretation records an application. The closest inspected literature did not directly state this full zeta stratification. Its derivation from classical inputs means publication priority needs specialized historical confirmation.

## Limitations
Only the minimum possible space-filling degree \(q+1\) is covered, not degree \(q+2\) or arbitrary hypersurfaces. The proof uses standard étale cohomology and the Weil purity theorem; the checker does not independently certify these theorems. The explicit quadratic point formula is already strongly implied by classical Hermitian counting, and the full zeta formula may be known elsewhere under the language of Hermitian descent; novelty is qualified rather than absolute. No independent mathematical audit has been carried out.

## References
1. V. Bourgeois-Conti, H.-B. Moon, E. Perez, A. Warren, *Space-Filling Hypersurfaces*, arXiv:2611.15768v1 (November 11, 2026), Section 3. https://arxiv.org/html/2611.15768v1
2. M. Homma and S. J. Kim, *Number of points of a nonsingular hypersurface in an odd-dimensional projective space*, arXiv:1611.02371 (2016), Theorem 1.1. https://arxiv.org/abs/1611.02371
3. R. C. Bose and I. M. Chakravarti, *Hermitian varieties in a finite projective space PG(N,q²)*, Canadian Journal of Mathematics (1966), Theorem 8.1 and its corollary. https://doi.org/10.4153/CJM-1966-116-0
4. Standard smooth-hypersurface primitive-cohomology calculation and Deligne's purity (Weil conjectures).
