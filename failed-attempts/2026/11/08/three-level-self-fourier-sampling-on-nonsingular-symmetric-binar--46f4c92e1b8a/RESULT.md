# Three-level self-Fourier sampling on nonsingular symmetric binary forms

## Finding

Let \(q\) be any odd prime power, \(\mathbb F_q\) its finite field, and \(\psi:\mathbb F_q\to\mathbb C^\times\) any nontrivial additive character. Let \(V=\operatorname{Sym}_2(\mathbb F_q)\) and \(S=\{X\in V:\det X\ne0\}\). Index the unnormalized square Fourier sampling matrix by \(S\) on **both** axes:
\[
H_{X,Y}=\psi(\operatorname{tr}(XY)),\qquad X,Y\in S.
\]
There are \(N=q^2(q-1)\) rows and columns. Its **entire singular-value multiset** is
\[
\begin{array}{c|c}
\text{singular value}&\text{multiplicity}\\\hline
q^{3/2}&q^2(q-2)+1\\
q&q^2-q-1\\
q^{1/2}&q
\end{array}.
\]
In particular, \(H\) is invertible for every such field and character, and its exact Euclidean condition number is \(\kappa_2(H)=q\). Equivalently, signals supported on invertible symmetric binary forms are recovered uniquely from Fourier measurements indexed by the same set, with optimal squared sampling constants \(q\) and \(q^3\).

## Assumptions and scope

Write \(X=\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)\) and identify \(V\) with \(\mathbb F_q^3\). The determinant form is \(Q(a,b,c)=ac-b^2\) and the Fourier pairing is
\[
B((a,b,c),(u,v,w))=au+2bv+cw.
\]
It is nondegenerate because \(q\) is odd. Put \(C=\{x\in V:Q(x)=0\}\); this includes the origin. For \(z\in\mathbb F_q\), let \(\eta(z)\) be the quadratic character, with \(\eta(0)=0\). All vector spaces in the proof have complex coefficients and ordinary counting-measure norms. No claim is made in characteristic two.

## Proof

**1. The cone and its Fourier transform.** For \(t\in\mathbb F_q\) put \(v_t=(1,t,t^2)\), and put \(v_\infty=(0,0,1)\). The null cone is the disjoint union
\[
C=\{0\}\ \sqcup\ \bigsqcup_{t\in\mathbb P^1(\mathbb F_q)}\{r v_t:r\in\mathbb F_q^\times\}.
\]
Thus \(|C|=1+(q+1)(q-1)=q^2\), and \(|S|=q^3-q^2\). If \(z=(u,v,w)\ne0\), the number \(k(z)\) of projective cone directions \(v_t\) satisfying \(B(z,v_t)=0\) is the number of projective roots of \(u+2vt+wt^2\), including its root at infinity. The discriminant is \(4(v^2-uw)=-4Q(z)\). Counting simple, double, or absent roots gives
\[
k(z)=1+\eta(-Q(z)).
\]
For each projective direction the character sum over its nonzero scalar multiples equals \(q-1\) when orthogonal to \(z\), and \(-1\) otherwise. Hence, *without assuming a special choice of* \(\psi\),
\[
\sum_{y\in C}\psi(B(z,y))=
\begin{cases}
q^2,&z=0,\\
q\eta(-Q(z)),&z\ne0.
\end{cases} \tag{1}
\]

**2. A low-rank exact cone Gram matrix.** Define \(T_{x,y}=\psi(B(x,y))\) for \(x,y\in C\). By (1),
\[
T^*T=q^2 I_{q^2}+q A,\qquad A_{x,y}=\eta(-Q(x-y)). \tag{2}
\]
The row and column at the origin are zero in \(A\). If \(x=r v_t\), \(y=s v_u\) with \(r,s\ne0\), then for distinct projective directions \(t\ne u\) the quantity \(-Q(v_t-v_u)\) is a nonzero square: it equals \((t-u)^2\) for finite distinct indices, and \(1\) if one index is infinity. Therefore
\[
A_{r v_t,s v_u}=\begin{cases}
0,&t=u,\\
\eta(r)\eta(s),&t\ne u.
\end{cases} \tag{3}
\]
For each of the \(q+1\) cone lines, take the unit vector supported on its nonzero points with entries \(\eta(r)/\sqrt{q-1}\). On their span, \(A\) is exactly \((q-1)(J_{q+1}-I_{q+1})\), while \(A\) vanishes on its orthogonal complement. Thus its eigenvalues are \(q(q-1)\) once, \(-(q-1)\) exactly \(q\) times, and \(0\) exactly \(q^2-q-1\) times. Equation (2) gives the exact squared singular values of \(T\): \(q^3\) once, \(q\) with multiplicity \(q\), and \(q^2\) with multiplicity \(q^2-q-1\).

**3. Transfer to nonsingular forms.** Set \(U_{x,y}=q^{-3/2}\psi(B(x,y))\) on the *whole* of \(V\). Nondegeneracy of \(B\) and additive-character orthogonality make \(U\) unitary. Partition its rows and columns into \(S\) and \(C\), so its diagonal blocks are \(U_S=q^{-3/2}H\) and \(U_C=q^{-3/2}T\). Write its off-diagonal lower-left block as \(R\). Unitarity gives
\[
U_S^*U_S=I_{|S|}-R^*R,\qquad
U_CU_C^*=I_{|C|}-RR^*.
\]
The nonzero eigenvalues of \(R^*R\) and \(RR^*\) coincide with multiplicity. Because \(|S|\ge|C|\) for \(q\ge3\), the squared singular values of \(U_S\) are exactly those of \(U_C\), **plus** \(|S|-|C|=q^3-2q^2\) additional ones. Undoing the normalization adds this many copies of \(q^3\) to the squared singular spectrum from Step 2. The resulting multiplicities are precisely those stated in the Finding, and they add to \(|S|\). All three levels are positive; their extreme ratio is \(q\). This completes the proof.

## Verification

The standalone file `check_symmetric_fourier.py` independently enumerates the conic, checks its finite-field character-root identity by exact point counts, and numerically compares the entire cone Gram spectrum for \(q=3,5,7,9\). It directly forms the nonsingular-form Fourier matrix and checks its whole Gram spectrum for \(q=3,5\). The \(q=9\) implementation uses \(\mathbb F_3[\alpha]/(\alpha^2+1)\) and a trace additive character, checking a nonprime finite field. Tests passed with explicit numerical tolerances. These finite calculations are **not** the justification for the arbitrary-prime-power theorem: Steps 1–3 supply the exact proof.

To reproduce from the directory containing the result and checker, run `OPENBLAS_NUM_THREADS=1 python check_symmetric_fourier.py` with NumPy installed. The script prints `SYMMETRIC_NONDEGENERATE_FOURIER_PASS` when all its tests pass.

## Relationship to prior work

Finite-field Fourier restriction and exact additive character-sum formulas for quadratic surfaces and cones are classical; in particular, Iosevich–Koh and Koh–Shen establish the relevant Fourier analytic foundations. Schmidt computes translation-association-scheme eigenvalues for symmetric bilinear forms. Those results are acknowledged, and their Fourier-transform formulas and ambient association-scheme eigenmatrices are not claimed as new. The contribution asserted here is the **full singular spectrum of the square Fourier operator simultaneously restricted in its input and output to all nonsingular symmetric \(2\times2\) matrices**, obtained by the projective-conic Gram decomposition and complementary-unitary transfer. The inspected papers do not state this three-level restricted spectrum or sharp sampling condition number. Published general finite-field restriction bounds do not imply the listed exact singular multiplicities.

## Limitations

This result concerns linear complex Fourier reconstruction, not phaseless retrieval; it does not claim robustness to missing samples. The trace pairing is degenerate on symmetric matrices in characteristic two, so that case is outside the theorem. The argument does not classify analogous self-Fourier matrices in higher symmetric-matrix dimensions. The novelty assessment is bounded by the inspected literature; a broader unlocated association-scheme or spectral theorem might encompass this instance.

## References

1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505, first public preprint 2008-04-28, https://arxiv.org/abs/0804.4505.
2. D. Koh and C.-Y. Shen, *Extension and averaging operators for finite fields*, arXiv:0908.3266, first public preprint 2009-08-24, https://arxiv.org/abs/0908.3266.
3. K.-U. Schmidt, *Symmetric bilinear forms over finite fields with applications to coding theory*, arXiv:1410.7184, first public preprint 2014-10-27, https://arxiv.org/abs/1410.7184.
