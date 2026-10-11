# Exact Euclidean Banach--Mazur distance for mixed \(\ell_p\)-\(\ell_q\) planes
## Finding
For \(\lambda>0\) and either \(2\le p\le q\le\infty\) or \(1\le p\le q\le2\), let \(X_{\lambda,p,q}=(\mathbb R^2,N_{\lambda,p,q})\), where \(N_{\lambda,p,q}(x,y)=\bigl(\|(x,y)\|_p^2+\lambda\|(x,y)\|_q^2\bigr)^{1/2}\). Then \(d_{\mathrm{BM}}(X_{\lambda,p,q},\ell_2^2)^2=C_{\mathrm{NJ}}(X_{\lambda,p,q})\), and this common value is \(\frac{2(1+\lambda)}{2^{2/p}+\lambda2^{2/q}}\) when \(2\le p\le q\le\infty\), while it is \(\frac{2^{2/p}+\lambda2^{2/q}}{2(1+\lambda)}\) when \(1\le p\le q\le2\), with the convention \(2^{2/\infty}=1\).

## Assumptions and scope
All spaces are real. The Banach--Mazur distance is
\[
d_{\mathrm{BM}}(X,\ell_2^2)
=
\inf_T \|T\|\,\|T^{-1}\|,
\]
where the infimum runs over linear isomorphisms \(T:X\to\ell_2^2\).

For \(1\le r<\infty\),
\[
\|(x,y)\|_r=(|x|^r+|y|^r)^{1/r},
\]
and \(\|(x,y)\|_\infty=\max\{|x|,|y|\}\). The parameter range is exactly the two same-side regimes \(1\le p\le q\le2\) and \(2\le p\le q\le\infty\), with \(\lambda>0\). No claim is made here when \(p<2<q\).

The source paper rescales \(N_{\lambda,p,q}\) by \(\sqrt{1+\lambda}\) to obtain an absolute normalized norm. This scalar rescaling changes neither the Banach--Mazur distance nor \(C_{\mathrm{NJ}}\).

## Proof
We first prove a symmetry lemma.

Let \(N\) be any norm on \(\mathbb R^2\) invariant under sign changes of the coordinates and under swapping the coordinates. Let
\[
S_N=\{x\in\mathbb R^2:N(x)=1\},
\qquad
r_-=\min_{x\in S_N}\|x\|_2,
\qquad
r_+=\max_{x\in S_N}\|x\|_2.
\]
Then
\[
d_{\mathrm{BM}}((\mathbb R^2,N),\ell_2^2)=\frac{r_+}{r_-}.
\]

Indeed, fix an invertible linear map \(T\) and put \(Q=T^\mathsf{T}T\). On \(S_N\), define
\[
m=\min_{x\in S_N}x^\mathsf{T}Qx,
\qquad
M=\max_{x\in S_N}x^\mathsf{T}Qx.
\]
The squared distortion of \(T\) is \(M/m\). Let \(G\) be the eight signed coordinate permutations. Since \(S_N\) is \(G\)-invariant,
\[
\overline Q=\frac1{|G|}\sum_{g\in G}g^\mathsf{T}Qg
\]
satisfies
\[
m\le x^\mathsf{T}\overline Qx\le M
\]
for every \(x\in S_N\). The only symmetric matrices commuting with all sign changes and the coordinate swap are scalar matrices, hence \(\overline Q=cI\) for some \(c>0\). Applying the last inequality to points of Euclidean radii \(r_-\) and \(r_+\) gives
\[
m\le cr_-^2,
\qquad
cr_+^2\le M,
\]
and therefore
\[
\frac M m\ge\frac{r_+^2}{r_-^2}.
\]
The identity map attains equality, proving the lemma. Equivalently,
\[
d_{\mathrm{BM}}((\mathbb R^2,N),\ell_2^2)
=
\frac{\max_{\|u\|_2=1}N(u)}{\min_{\|u\|_2=1}N(u)}.
\]

The mixed norm \(N_{\lambda,p,q}\) has exactly this signed-permutation symmetry. For every Euclidean unit vector \(u\in\mathbb R^2\) and every \(2\le r\le\infty\),
\[
2^{2/r-1}\le\|u\|_r^2\le1.
\]
The lower endpoint is attained at the two diagonal directions
\[
u=(\pm2^{-1/2},\pm2^{-1/2}),
\]
and the upper endpoint at the coordinate axes. Thus, when \(2\le p\le q\le\infty\),
\[
\max_{\|u\|_2=1}N_{\lambda,p,q}(u)^2=1+\lambda,
\]
while
\[
\min_{\|u\|_2=1}N_{\lambda,p,q}(u)^2
=
2^{2/p-1}+\lambda2^{2/q-1}.
\]
The symmetry lemma therefore yields
\[
d_{\mathrm{BM}}(X_{\lambda,p,q},\ell_2^2)^2
=
\frac{2(1+\lambda)}{2^{2/p}+\lambda2^{2/q}}.
\]

For \(1\le r\le2\), the same Euclidean-sphere bounds reverse:
\[
1\le\|u\|_r^2\le2^{2/r-1},
\]
with the minimum at the axes and the maximum at the diagonals. Hence, for \(1\le p\le q\le2\),
\[
d_{\mathrm{BM}}(X_{\lambda,p,q},\ell_2^2)^2
=
\frac{2^{2/p}+\lambda2^{2/q}}{2(1+\lambda)}.
\]

Mizuguchi and Saito's Example 4.2 gives exactly these two expressions for the von Neumann--Jordan constant \(C_{\mathrm{NJ}}(X_{\lambda,p,q})\). This proves the stated equality with \(d_{\mathrm{BM}}^2\).

## Verification
The symmetry lemma was checked for an arbitrary positive definite matrix \(Q=T^\mathsf{T}T\), so the Banach--Mazur optimization is over all linear isomorphisms, not merely diagonal maps or rotations.

The endpoint cases were also checked. If \(p=q=2\), both formulas give \(1\), as they must for a Euclidean norm up to scale. If \(p=q=1\) or \(p=q=\infty\), both formulas give \(d_{\mathrm{BM}}^2=2\), the classical value for the diamond and square. The convention \(2^{2/\infty}=1\) makes the formula continuous at \(q=\infty\).

No finite numerical experiment is used to establish the quantified statement. The proof uses only the global signed-permutation symmetry and sharp \(\ell_r\)-norm extrema on the Euclidean circle.

## Relationship to prior work
Mizuguchi and Saito introduced the exact mixed family used here and, in Example 4.2, proved the two displayed formulas for \(C_{\mathrm{NJ}}\), the modified von Neumann--Jordan constant, and the Zbăganu constant. Their article does not discuss Banach--Mazur distance; a full-text search of the public article found no occurrence of “Banach-Mazur” or “Mazur”.

Passer's 2013 paper studies the general implication from a von Neumann--Jordan constant close to \(1\) to a Banach--Mazur distance close to Euclidean. In dimension two its Theorem 2.9 gives an asymptotic upper bound depending only on the von Neumann--Jordan constant. It does not state an exact equality for this mixed family and does not imply the formulas above.

A 2017 article on \(\pi/2\)-rotation invariant norms is structurally close because the present norms have that symmetry. Its accessible abstract states that it studies the (modified) von Neumann--Jordan and Zbăganu constants and gives estimates. A readable full text was not obtained in the bounded comparison, so it is retained as an originality risk rather than used as a noncoverage assertion.

## Limitations
The proof requires \(p\) and \(q\) to lie on the same side of \(2\), because only then do the two summands attain their Euclidean-circle extrema in the same directions. The mixed regime \(p<2<q\) is not covered.

The public EMIS archive lists the exact source PDF with timestamp 23 November 2011; this is the earliest exact public-source date verified in the present comparison and is used as the source date. The article itself records receipt on 31 March 2011 and acceptance on 14 June 2011, but those are not treated as public-source dates.

The inaccessible 2017 full text and notation-sensitive older planar Banach--Mazur literature remain residual originality risks. Neither is a proof dependency.

## References
1. H. Mizuguchi and K.-S. Saito, “Some geometric constants of absolute normalized norms on \(\mathbb R^2\),” Annals of Functional Analysis 2 (2011), no. 2, 22--33. DOI: 10.15352/afa/1399900191.
2. B. Passer, “An Approximate Version of the Jordan von Neumann Theorem for Finite Dimensional Real Normed Spaces,” arXiv:1305.3546, first posted 13 May 2013.
3. Y. Tomizawa, K.-I. Mitani, K.-S. Saito, and R. Tanaka, “Geometric constants of \(\pi/2\)-rotation invariant norms on \(\mathbb R^2\),” Annals of Functional Analysis 8 (2017), no. 2, 215--230. DOI: 10.1215/20088752-0000007X.
