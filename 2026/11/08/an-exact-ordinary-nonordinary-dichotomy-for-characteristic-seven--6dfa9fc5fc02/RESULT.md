# An exact ordinary/nonordinary dichotomy for characteristic-seven Picard curves

## Finding
Let \(k=\overline{\mathbb F}_7\). For each \((a,b)\in k^2\), put
\[
f_{a,b}(x)=x^4+a x^2+b x+1,\qquad
\Delta(a,b)=2a^4+3a^3b^2-2a^2-3ab^2+b^4-3.
\]
Whenever \(\Delta(a,b)\ne0\), the smooth projective model \(C_{a,b}\) of \(y^3=f_{a,b}(x)\) is a genus-three Picard curve. Its Jacobian has the following *complete* \(a\)-number and \(7\)-rank classification:

| Condition (always \(\Delta\ne0\)) | \(a(C_{a,b})\) | \(7\)-rank |
| --- | ---: | ---: |
| \(a\ne0\) | \(0\) | \(3\) |
| \(a=0\), \(b^4\ne4\) | \(2\) | \(1\) |
| \(a=0\), \(b^4=4\) | \(2\) | \(0\) |

In the second row smoothness also forces \(b^4\ne3\). In particular, there are no smooth members of \(7\)-rank \(2\), nor any members of \(a\)-number \(1\), in this normalized two-parameter family. The nonordinary locus is precisely the smooth part of the straight line \(a=0\); its zero-\(7\)-rank sublocus consists of exactly four geometric parameter values (the roots of \(b^4=4\)).

## Assumptions and scope
The ground field is algebraically closed of characteristic \(7\). The affine polynomial is monic, has no cubic term, and its constant coefficient is \(1\); the theorem does not assert a classification of all genus-three curves or of all unnormalized cyclic triple covers. All equalities of parameters are in \(k\). The \(7\)-rank means the dimension over \(\mathbb F_7\) of the geometric \(7\)-torsion group of the Jacobian, equivalently the stable rank of its Frobenius-semilinear Hasse–Witt operator. The \(a\)-number equals three minus the rank of the Hasse–Witt matrix.

The plane quartic model is
\[
F(X,Y,Z)=Y^3Z-X^4-aX^2Z^2-bXZ^3-Z^4=0.
\]
It is smooth if and only if the quartic polynomial \(f_{a,b}\) is separable: on the affine chart \(Z=1\), singularities require \(y=0\) and \(f=f'=0\), while at infinity \([0:1:0]\) the partial derivative \(\partial F/\partial Z\) equals \(1\). The discriminant computed below is \(\Delta\), up to the usual unit, and has precisely this nonvanishing criterion. A smooth plane quartic has genus \(3\).

## Proof
We compute Frobenius on \(H^1(C_{a,b},\mathcal O_{C_{a,b}})\) directly by the standard plane-curve exact sequence
\[
0\longrightarrow\mathcal O_{\mathbb P^2}(-4)
\xrightarrow{\,F\,}\mathcal O_{\mathbb P^2}
\longrightarrow\mathcal O_{C_{a,b}}\longrightarrow0.
\]
Under the residue realization inside \(H^2(\mathbb P^2,\mathcal O(-4))\), use the ordered Laurent-monomial basis
\[
(X^{-2}Y^{-1}Z^{-1},\ X^{-1}Y^{-2}Z^{-1},\ X^{-1}Y^{-1}Z^{-2}).
\]
Frobenius takes a basis monomial to its seventh power and multiplies it by \(F^6\). Consequently, if the positive exponent triples of the source and target basis vectors are \(u_i,u_j\), the coefficient from source \(i\) to target \(j\) is extracted at exponent \(7u_i-u_j\) in \(F^6\). Direct multinomial extraction modulo \(7\) yields the transpose of the source-column Frobenius matrix
\[
H(a,b)=\begin{pmatrix}
-a^2-3&0&-3b\\
0&2a&0\\
-2a^2b-3ab^3-2b&0&-3a^3-a^2b^2-2a-2b^2
\end{pmatrix}.
\]
An independent calculation from the Kummer differential basis \(\{dx/y^2,x\,dx/y^2,dx/y\}\) extracts the \(x\)-coefficients in \(f_{a,b}^4\) of degrees \(5,6,12,13\), and the degree-six coefficient in \(f_{a,b}^2\), yielding the same rank conditions.

Transposing this displayed matrix does not change its rank or determinant. For \(a=0\), both the displayed matrix and its transpose have rank-one Frobenius iterations vanishing precisely when \(3+2b^8=0\); hence the stable-rank conclusions below hold for the actual source-column convention as well. A direct polynomial identity over \(\mathbb F_7[a,b]\) is
\[
\det H(a,b)=3a^2\Delta(a,b).
\]
Thus when \(\Delta\ne0\) and \(a\ne0\), the Frobenius matrix is invertible: \(a(C)=0\) and the \(7\)-rank is \(3\). For \(a=0\), it specializes to
\[
H(0,b)=\begin{pmatrix}-3&0&-3b\\0&0&0\\-2b&0&-2b^2\end{pmatrix},
\]
which has rank exactly one for every \(b\) (because the upper left entry is nonzero). Hence \(a(C_{0,b})=2\).

To determine stable rather than first-iterate Frobenius rank, note the factorization
\[
H(0,b)=\begin{pmatrix}1\\0\\(2/3)b\end{pmatrix}
\begin{pmatrix}-3&0&-3b\end{pmatrix}.
\]
For the Frobenius-semilinear map \(v\mapsto H(0,b)v^{[7]}\), the second iterate is zero exactly when the scalar product of the row with the seventh powers of the column is zero, i.e.
\[
-3-2b^8=0\quad\Longleftrightarrow\quad b^8=2.
\]
Otherwise every iterate retains rank one, since Frobenius is an automorphism of \(k\). On the line \(a=0\), smoothness is \(b^4-3\ne0\). In characteristic \(7\), \(b^8=2\) holds precisely when \(b^4\in\{3,4\}\); the singular possibility \(b^4=3\) is excluded, leaving exactly \(b^4=4\). These four distinct parameter values yield \(7\)-rank zero. This proves all cases, including the gaps in attainable ranks.

## Verification
Two standalone exact programs are included. `verify_plane_hasse_witt.py` obtains all nine matrix entries independently from the expansion of \(F^6\) on plane cohomology, checks the determinant identity symbolically, and proves the square-zero factorization of the boundary Frobenius operator. `verify_picard_coefficients.py` extracts coefficients from \(f^4\) and \(f^2\), checks the independent determinant-discriminant relation \(5a\Delta\) for its two-by-two block, and exhaustively verifies the resulting smooth/rank cases for all \(49\) pairs in \(\mathbb F_7^2\). Both are exact symbolic checks; the proof above is valid over the algebraic closure, not merely over \(\mathbb F_7\).

The expected completion markers are `PICARD7_PLANE_FROBENIUS_PASS` and `PICARD7_COEFFICIENT_PASS`; both were observed on re-execution from these source files.

## Relationship to prior work
Nourozi–Rahmati, *The Rank of the Cartier operator on Picard Curves* (first available June 13, 2023; arXiv:2306.07823), develops the differential-basis coefficient formula. Its Theorem 3.1, as literally worded with a nonzero constant coefficient, states a constant \(a\)-number for characteristic \(p\equiv1\pmod3\). The present exact characteristic-seven stratification, especially the smooth example \(y^3=x^4+1\) with \(a\)-number \(2\), is incompatible with that literal general statement. Any additional implicit maximal-curve hypothesis in that work would need separate interpretation; no claim about maximal Picard curves is made here.

Bouw–Koutsianas–Sijsling–Wewers, *Conductor and discriminant of Picard curves* (2020), provides general Picard-curve normal forms; its results do not state this characteristic-seven \(a\)-number/\(7\)-rank stratification. Cavalieri–Pries, *Mass formula for non-ordinary curves in one dimensional families* (arXiv:2308.14891, first available August 28, 2023), gives general family mass formulas and detailed four-branch-point cases rather than these two-parameter, five-branch-point rank loci. Older general Hasse–Witt formulas permit a calculation in principle, so historical priority for the distilled rank classification requires independent examination.

## Limitations
The theorem concerns the specified normalized family, not all Picard curves or all plane quartics. No Ekedahl–Oort final-type classification beyond the proved \(a\)-number and \(7\)-rank is asserted. The four zero-rank parameter values are not counted as four pairwise nonisomorphic curves. No conclusion about maximality, supersingularity of the whole Jacobian, or lifts to characteristic zero is drawn. Independent mathematical audit and exhaustive historical-priority review have not been performed.

## References
1. V. Nourozi and F. Rahmati, *The Rank of the Cartier operator on Picard Curves*, arXiv:2306.07823 (first public June 13, 2023), https://arxiv.org/abs/2306.07823 .
2. I. Bouw, A. Koutsianas, J. Sijsling and S. Wewers, *Conductor and discriminant of Picard curves*, Journal of the London Mathematical Society 102 (2020), https://doi.org/10.1112/jlms.12323 .
3. R. Cavalieri and R. Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891 (first public August 28, 2023), https://arxiv.org/abs/2308.14891 .
4. J. Estrada Sarlabous, *On the Jacobian varieties of Picard curves defined over fields of characteristic \(p>0\)* (1991), cited for the general Cartier–Manin coefficient formula in Reference 1.
