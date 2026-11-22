# The sharp mean–variance phase diagram for four-periodic weighted-shift numerical radii

## Finding
For a unilateral weighted shift on \(\ell^2(\mathbb N_0)\) with four-periodic nonnegative weights \((a,b,c,d)\), define its positive mean \(m=(a+b+c+d)/4\) and normalized variance
\[
v=\frac{(a-m)^2+(b-m)^2+(c-m)^2+(d-m)^2}{4m^2},\qquad 0\le v\le3.
\]
At fixed \(m>0\) and \(v\), the **exact minimum** of its numerical radius over every such weight quadruple is
\[
\min w(T)=m\begin{cases}1,&0\le v\le1,\\1+\sqrt{(v-1)/2},&1\le v\le3.\end{cases}
\]
For \(0\le v<1\), all minimizing quadruples, up to cyclic rotation, alternate the two positive weights \(m(1+\sqrt v)\) and \(m(1-\sqrt v)\). At \(v=1\), their limiting pattern is \((2m,0,2m,0)\), up to rotation. For \(1<v\le3\), all minimizers, up to rotation and reversal, have two opposite edges of weights \(m(2+\sqrt{2(v-1)})\) and \(m(2-\sqrt{2(v-1)})\), and the other two weights zero. The range \(v\in[0,3]\) is exact. If every weight is strictly positive, the displayed infimum is attained precisely when \(v<1\); for \(1\le v<3\) it is sharp but unattained.

## Assumptions and scope
The numerical radius is \(w(T)=\sup_{\|x\|=1}|\langle Tx,x\rangle|\), and \(Te_j=w_j e_{j+1}\) for \(j\ge0\) with periodic pattern \(w_{4k},w_{4k+1},w_{4k+2},w_{4k+3}=a,b,c,d\). Complex weights can be replaced by their magnitudes via diagonal unitary conjugacy; all numerical statements concern magnitudes. The nonnegative boundary is included for optimization and necessary to realize the second branch. A zero mean gives only the zero shift, excluded from normalized variance.

## Proof
**Periodic reduction.** A diagonal unitary makes the numerical radius equal to the norm of the symmetric Jacobi matrix \((T+T^*)/2\). Compressing the corresponding four-periodic bilateral Jacobi matrix cannot increase its norm; conversely increasingly long periodic blocks of the positive Perron vector give a Weyl sequence achieving the full-line top norm. The Fourier fiber at phase \(\theta\) has entrywise absolute value bounded by the zero-phase fiber, so its norm is at most that fiber's Perron root. Reordering the two even and two odd vertices in the zero-phase fiber produces the block matrix with off-diagonal block \(B/2\), where
\[
B=\begin{pmatrix}a&d\\b&c\end{pmatrix}.
\]
Consequently \(w(T)=\|B\|_{2\to2}/2\), including zero coefficients by continuity.

**Normalization and first branch.** Scale \(m=1\), and write \(S=a+b+c+d=4\), \(Q=a^2+b^2+c^2+d^2=4(1+v)\). The unit vectors \((1,1)/\sqrt2\) on the two sides yield \(\|B\|\ge S/2=2\), hence \(w(T)\ge1\). Equality forces both uniform vectors to be maximizing singular vectors, so every row and column sum of \(B\) equals \(2\). Thus \(a=c\), \(b=d\), \(a+b=2\). The variance condition then gives precisely \((a,b,c,d)=(1\pm\sqrt v,1\mp\sqrt v,1\pm\sqrt v,1\mp\sqrt v)\), which is nonnegative if and only if \(v\le1\), and attains \(w(T)=1\).

**Second branch.** Let \(s\ge t\ge0\) be the singular values of \(B\). The nuclear norm is bounded by the sum of the nuclear norms of the four matrix units: \(s+t\le S=4\). Also \(s\ge2\). Since \(Q=s^2+t^2\),
\[
4(1+v)=Q\le s^2+(4-s)^2.
\]
For \(v\ge1\), and because the right side increases when \(s\ge2\), this implies \(s\ge2+\sqrt{2(v-1)}\). With \(w(T)=s/2\), the claimed second branch follows. Sharpness is attained at \((a,b,c,d)=(2+\sqrt{2(v-1)},0,2-\sqrt{2(v-1)},0)\), for which \(B\) is diagonal and \(s=\max(a,c)\).

**All equality cases.** Equality on the second branch implies \(\|B\|_*=S\). Directly,
\[
S^2-\|B\|_*^2=2\bigl(ab+ad+bc+cd+2\min(ac,bd)\bigr).
\]
All terms are nonnegative. Its vanishing forces the nonzero entries of \(B\) to lie on at most one diagonal or antidiagonal (including one-point degeneracies). The fixed sum and variance then give the stated two opposite weights. At \(v=1\) the two regimes coincide. Finally, for a nonnegative four-vector of sum \(4\), \(4\le Q\le16\), giving \(0\le v\le3\); every intermediate variance is realized continuously. Strictly positive approximants at fixed \(m,v\) exist for each \(1\le v<3\) by moving the boundary extremizer into the positive simplex along its mean-and-variance sphere.

## Verification
All inequalities are identities or norm estimates in a two-by-two matrix, so the argument is infinite-dimensional without relying on finite-section numerics. Exact examples: \((1,1,1,1)\) has \(v=0\), \(w=1\); \((3/2,1/2,3/2,1/2)\) has \(v=1/4\), \(w=1\); \((2,0,2,0)\) has \(v=1\), \(w=1\); and \((3,0,1,0)\) has \(v=3/2\), \(w=3/2\). The proof identifies all minimizers, including at both endpoints.

## Relationship to prior work
The periodic numerical-radius variational reduction goes back to Ridge and Stout and is used by A. Sharif in the 2023 study of numerical radius versus Banach-limit means. Sharif records equality for two-periodic sequences but does not present the fixed-variance four-period sharp phase diagram. A published analysis of three-periodic weights yields a different two-phase minimum with a positive variance gap; it does not imply the four-period plateau or its nuclear-norm-driven transition. The new point is the joint mean–variance constrained optimum and the complete equality and strict-positivity classification for four-periodic weights, not the foundational spectral reduction.

## Limitations
The assertion concerns periodic scalar Hilbert-space shifts of period four and their nonnegative weight magnitudes. It does not give a general inequality at arbitrary periods or classify all finite-rank perturbations. The boundary minimizers at variance at least one are not attained with strictly positive weights. Prior-art search cannot establish historical uniqueness; broader matrix norm inequalities may provide alternate proofs. No independent mathematical audit has been carried out.

## References
- A. Sharif, *On the numerical radius of weighted shifts on \(\ell^2\) as a norm on \(\ell^\infty\) and connections to Banach limits*, arXiv:2303.00876, first posted 2 March 2023; revised 3 August 2023.
- D. Ridge, periodic weighted-shift numerical-radius variational formula, cited as [17]/[18] in Sharif (2023).
- Q. F. Stout, *The numerical range of a weighted shift*, Proceedings of the American Mathematical Society 88 (1983), 495–502.
- *A sharp mean–variance envelope for three-periodic weighted-shift numerical radii*, published research record, 2 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-mean-variance-envelope-for-three-periodic-weighted-shift--722309e917f5 .
