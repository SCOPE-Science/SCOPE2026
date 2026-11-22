# Witt-sensitive rank gaps and components of associative Nijenhuis operators on quadratic two-step algebras

## Finding
Let \(k\) have characteristic different from two, let \(V\) be an \(n\)-dimensional vector space, \(n\geq3\), and let \(B:V\times V\to k\) be a nondegenerate symmetric bilinear form. Give \(A=V\oplus kz\) the nonunital commutative associative multiplication
\[
(u+cz)(v+dz)=B(u,v)z.
\]
A linear map \(N:A\to A\) is an associative Nijenhuis operator, meaning
\[
N(x)N(y)=N\bigl(N(x)y+xN(y)-N(xy)\bigr)\quad(x,y\in A),
\]
if and only if there is a **unique** triple \((a,\phi,S)\in k\times V^*\times\operatorname{End}(V)\) such that
\[
N(z)=az,\qquad N(v)=av+Sv+\phi(v)z,\qquad B(Sv,Sw)=0\quad(v,w\in V).
\]
Thus the nontrivial operator parameter is a linear map with totally isotropic image.

Over an algebraically closed field of characteristic different from two, the **reduced** Nijenhuis-operator variety is geometrically irreducible if \(n\) is odd and has exactly two geometric irreducible components if \(n\) is even. For \(n=2m\), these two components meet precisely along \(\operatorname{rank}S\leq m-1\). Their dimension, including the free \(a\) and \(\phi\), is
\[
(n+1)+nm+\frac{m(m-1)}2.
\]
For \(n=2m+1\), the single component has dimension
\[
(n+1)+nm+\frac{m(m+1)}2.
\]

Over an odd finite field \(k=\mathbb F_q\), set \(w\) equal to the Witt index of \(B\). The possible linear ranks of \(N\) are **exactly**
\[
\{0,1,\dots,w+1\}\ \cup\ \{n+1-w,n+2-w,\dots,n+1\}.
\]
Consequently the **only** finite-field rank gap is rank \(m+1\) when \(n=2m\) and \(B\) has nonsplit Witt type (Witt index \(m-1\)); the split even and all odd-dimensional forms have every rank. The gap occurs first for five-dimensional algebras (four-dimensional \(V\)).

Here is an exact formula for the full rank polynomial \(P_{B,q}(t)=\sum_Nt^{\operatorname{rank}N}\). Write \({r\brack s}_q\) for the Gaussian binomial coefficient and let \(I_r\) be the number of totally isotropic \(r\)-subspaces of \((V,B)\), with \(I_0=1\), \(I_r=0\) for \(r>w\). Define
\[
A_r=\prod_{i=0}^{r-1}(q^n-q^i),\qquad
E_{h,j}={h\brack j}_q\prod_{i=0}^{h-j-1}(q^h-q^i),
\]
\[
H_{r,j}=\sum_{h=j}^r(-1)^{r-h}q^{\binom{r-h}{2}}{r\brack h}_q q^{h(n-h)}E_{h,j}.
\]
Empty products equal one. Then
\[
\boxed{\begin{aligned}
P_{B,q}(t)={}&\sum_{r=0}^w I_r A_r\bigl(q^rt^r+(q^n-q^r)t^{r+1}\bigr)\\
&+(q-1)q^n\sum_{j=0}^w\biggl(\sum_{r=j}^w I_r H_{r,j}\biggr)t^{n+1-j}.
\end{aligned}}
\]
This is a numerical closed finite-sum formula, since the isotropic-subspace factors are explicit: put \(\epsilon=\chi_q((-1)^{n/2}\det B)\) for even \(n\), and for every positive integer \(d\) of the same parity as \(n\) define
\[
Z_d=\begin{cases}
q^{d-1}-1,&d\text{ odd},\\
q^{d-1}-1+(q-1)q^{d/2-1}\epsilon,&d\text{ even}.
\end{cases}
\qquad
I_r=\prod_{h=0}^{r-1}\frac{Z_{n-2h}}{q^{h+1}-1}\quad(0\leq r\leq w).
\]
The determinant square class in \(\epsilon\) is invariant under changing basis.

For example, when \(n=4,q=3\), the exact count vectors for ranks \(0,1,2,3,4,5\) are respectively
\[
(1,3920,549120,3699216,3289248,4900338)
\]
for split \(B\), and
\[
(1,2480,62400,0,43740,86022)
\]
for nonsplit \(B\). The missing middle rank distinguishes the two Witt types without recovering an entire operator orbit structure.

## Assumptions and scope
The algebra is nonunital, has square \(A^2=kz\), and has annihilator \(kz\). The bilinear form is symmetric and nondegenerate, \(n\geq3\), and \(\operatorname{char}k\ne2\). The geometric assertions concern the underlying reduced variety, not a claimed scheme-theoretic complete intersection or reducedness of its defining ideal. Finite-field enumeration uses odd prime powers, with operators counted as labeled linear maps, not modulo automorphisms. The formula for \(H_{r,j}\) counts image-*exactly*-\(r\) operators by the nullity of \(aI+S\) when \(a\ne0\).

## Proof
**Step 1: the Nijenhuis equation.** Write a general linear operator as
\[
N(v)=Tv+\phi(v)z,\qquad N(z)=u+az
\]
with \(T\in\operatorname{End}V\), \(u\in V\), \(a\in k\), \(\phi\in V^*\). Apply the Nijenhuis equation to \((v,z)\): its vector part on the right is \(B(v,u)u\), while the left side has no vector part. If \(u\ne0\), nondegeneracy of \(B\) yields \(v\) with \(B(v,u)\ne0\), a contradiction. Thus \(u=0\). For \((v,w)\in V^2\), the equation now reads
\[
B(Tv,Tw)=a\bigl(B(Tv,w)+B(v,Tw)-aB(v,w)\bigr).
\]
Put \(S=T-aI\). The displayed equation is equivalent, by expansion, to \(B(Sv,Sw)=0\). Products with \(z\) now give zero on both sides, proving necessity and sufficiency. Uniqueness follows from the block decomposition.

**Step 2: the geometric components.** Over an algebraic closure let \(w=\lfloor n/2\rfloor\). Every totally isotropic image \(\operatorname{im}S\) lies in a maximal totally isotropic \(w\)-plane. Consider the closed incidence correspondence
\[
\mathcal I=\{(U,S): U\in\operatorname{OGr}(w,V),\ \operatorname{im}S\subseteq U\}.
\]
It is the total space of the rank-\(nw\) vector bundle \(\operatorname{Hom}(V,\mathcal U)\) over the orthogonal Grassmannian. Projection to matrices is a closed map because the Grassmannian is projective; it is surjective onto \(\{S:S^*S=0\}\). At a map of rank \(w\), the plane \(U=\operatorname{im}S\) is unique. Thus each connected irreducible component of the maximal orthogonal Grassmannian gives one irreducible component of the matrix variety, and there are no further components. The maximal orthogonal Grassmannian is irreducible in odd dimension and has two irreducible families in even dimension. Its dimensions are \(m(m+1)/2\) for \(n=2m+1\) and \(m(m-1)/2\) for \(n=2m\). In even dimension, each isotropic plane of dimension at most \(m-1\) is contained in maximal planes from both families, while a rank-\(m\) image belongs to precisely one. This gives the stated intersection. Finally \((a,\phi)\) supply \(n+1\) free affine parameters, proving the dimensions and the component counts.

**Step 3: finite-field isotropic subspaces.** For an \(r\)-plane \(U\) with \(B|_U=0\), \(U^\perp/U\) is nondegenerate of dimension \(n-2r\). The standard quadratic-form zero count gives \(Z_d\) nonzero isotropic vectors in each such quotient of dimension \(d\). Count flags of a totally isotropic \((r-1)\)-plane in an isotropic \(r\)-plane in two ways: the extension count is \(Z_{n-2r+2}/(q-1)\) and each \(r\)-plane has \((q^r-1)/(q-1)\) hyperplanes. Hence \(I_r=I_{r-1}Z_{n-2r+2}/(q^r-1)\), proving the product formula. The split even type has \(w=n/2\), the nonsplit even type has \(w=n/2-1\), and odd dimension has \(w=(n-1)/2\).

**Step 4: rank enumeration.** For each fixed totally isotropic \(r\)-plane \(U\), exactly \(A_r\) linear maps \(S:V\twoheadrightarrow U\) have image \(U\). If \(a=0\), then \(N(z)=0\) and \(N|_V=(S,\phi)\). Exactly \(q^r\) functionals \(\phi\) vanish on \(\ker S\), producing rank \(r\); the remaining \(q^n-q^r\) produce rank \(r+1\). This gives the first sum.

If \(a\ne0\), the rank of \(N\) is \(1+\operatorname{rank}(aI+S)\), independent of the \(q^n\) choices of \(\phi\). To count maps of image contained in a fixed \(h\)-plane \(W\) and \(\dim\ker(aI+S)=j\), choose \(V=W\oplus W'\). Relative to this decomposition, \(aI+S\) has block form \(\left(\begin{smallmatrix}C&D\\0&aI\end{smallmatrix}\right)\). There are \(q^{h(n-h)}\) choices of \(D\) and \(E_{h,j}\) choices of \(C\) with nullity \(j\); the latter formula chooses its kernel and an injective map on the quotient. The Möbius function on subspaces \(W\subseteq U\), where \(\dim U-\dim W=r-h\), is \((-1)^{r-h}q^{\binom{r-h}{2}}\). Möbius inversion therefore yields \(H_{r,j}\) maps with image exactly the fixed \(r\)-plane \(U\) and shifted nullity \(j\). Multiplication by \(I_r(q-1)q^n\) and summation give the second sum. No unknown quantities remain.

**Step 5: sharp rank support.** For \(a=0\), choose \(S\) with arbitrary isotropic image rank \(0\le r\le w\) and choose \(\phi\) factoring or not factoring through \(S\); this realizes all ranks \(0\) through \(w+1\). For \(a\ne0\), fix any isotropic \(j\)-plane \(J\), \(0\le j\le w\), and any linear projection \(P_J\) onto \(J\). The choice \(S=-aP_J\) yields nullity \(j\) of \(aI+S\) and hence Nijenhuis rank \(n+1-j\). No other ranks are possible because \(\operatorname{im}S\) is isotropic, and \(\ker(aI+S)\subseteq\operatorname{im}S\) whenever \(a\ne0\). Comparing the two intervals gives the single nonsplit-even missing middle rank and proves attainability of every other rank.

## Verification
The standalone `verify.py` uses only Python's standard library. Run `python3 verify.py`. It exhaustively checks the original Nijenhuis identity **against** the normal-form condition for all \(3^{9}\) linear maps on each of the split and anisotropic three-dimensional examples over \(\mathbb F_3\), and all \(5^9\) maps for the split example over \(\mathbb F_5\). It independently enumerates all \(3^{9}\) candidate generator blocks for the four-dimensional algebra over \(\mathbb F_3\), computes the exact rank distribution by both methods, and checks a sample of 3,000 direct original-identity instances. It also enumerates isotropic subspaces in the four-dimensional split and nonsplit quadratic spaces over \(\mathbb F_3\), obtaining \((I_0,I_1,I_2)=(1,16,8)\) and \((1,10,0)\), respectively. It prints `ISOTROPIC_NIJENHUIS_VERIFIED` if every comparison passes. These finite tests corroborate, but do not replace, the general proof.

## Relationship to prior work
The 2021 classification of Rota-type operators on three-dimensional nilpotent associative algebras by Abdujabborov, Karimjanov, and Kodirova includes Nijenhuis operators on the binary hyperbolic special case (dimension three as an algebra). Its Theorem 5 and subsequent equations concern only three-dimensional algebras over \(\mathbb C\); they do not give the all-dimensional isotropic-image parameterization, the geometric component law, or finite-field Witt-rank census. The 2023 Gao–Kang–Lü–Yu preprint (revised subsequently with another author) likewise classifies Nijenhuis maps on complex associative algebras of dimension three, not the present family in unbounded dimension. The binary case \(n=2\) is **not claimed as new**. Existing general orthogonal-Grassmannian and finite quadratic-form counts are used as standard ingredients, rather than claimed as discoveries. Other published finite-field Nijenhuis classifications address distinct algebras (such as unital radical-square-zero algebras and full matrix algebras); their theorems do not imply this quadratic-socle algebra's Witt-sensitive rank gap without new analysis. The precise generalization beyond the three-dimensional case, including the missing rank in nonsplit even dimension, is the assessed contribution. Absolute priority is not asserted.

## Limitations
No claim is made about characteristic two, degenerate multiplication forms, general noncommutative algebras, or Nijenhuis-operator conjugacy classes. The geometric statements concern reduced varieties; no scheme-theoretic radicality is established. The full-rank polynomial is an exact finite sum, not an asserted factored formula. Searches and relevant primary-text comparisons support an originality assessment but do not establish absence from all literature. A separately conducted independent proof review has not taken place.

## References
1. N. G. Abdujabborov, I. A. Karimjanov, M. A. Kodirova, *Rota-type operators on 3-dimensional nilpotent associative algebras*, Communications in Mathematics 29 (2021), 227–241, DOI: [10.2478/cm-2021-0020](https://doi.org/10.2478/cm-2021-0020), https://cm.episciences.org/9539/pdf.
2. X. Gao, C. Kang, J. Lü, S. Yu, *Nijenhuis operators on low dimensional pre-Lie algebras and solutions of CYBE*, initial arXiv submission 2023-08-23, [arXiv:2308.12121](https://arxiv.org/abs/2308.12121); later versions revise the title/authorship.
3. Standard finite-field quadratic-space counts and orthogonal-Grassmannian geometry (the requisite formulas and deductions are stated explicitly above).
