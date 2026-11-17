# A square-root acute-angle transition after one edge deletion in bipartite Laplacian simplices

## Finding
Let \(p,q\ge2\) be integers, \(n=p+q\), and \(G_{p,q}=K_{p,q}-\{a_0b_0\}\), where \(a_0\) and \(b_0\) lie in opposite shores. Regard the columns of the combinatorial Laplacian \(L(G_{p,q})\) as points of the standard Euclidean hyperplane \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\), and let \(T_{p,q}\) be their convex hull. Facets are labeled by omitted graph vertices. Put
\[
F(p,q)=(n-1)(n-2)^2+(3n-4)pq-p^2q^2.
\]
For any distinct facet labels \(i,j\), the *interior* dihedral angle is obtuse precisely when \(F(p,q)>0\) and exactly one of the following holds: \(i=a_0\) and \(j\) is a vertex of the \(q\)-shore other than \(b_0\), or \(j=b_0\) and \(i\) is a vertex of the \(p\)-shore other than \(a_0\), with the order of \(i,j\) interchangeable. If \(F(p,q)=0\), these \(n-2\) angles are right angles; if \(F(p,q)<0\), all interior dihedral angles are strictly acute. Every other angle is strictly acute in all cases. Thus the obtuse-angle ridge count is exactly \(n-2\) or zero, even though deletion never alters the simplex face lattice.

In contrast, every interior dihedral angle of the undeleted \(K_{p,q}\) Laplacian simplex is strictly acute. With
\[
 t_+(n)=\frac{3n-4+\sqrt{(3n-4)^2+4(n-1)(n-2)^2}}2,
\]
obtuse angles occur exactly when \(pq<t_+(n)\). Fixing \(n\), this is an initial interval of the smaller shore size \(\min(p,q)\). The first order allowing a non-obtuse-only deleted-edge simplex is \(n=25\), with \((p,q)=(11,14)\) giving \(F=-86\). For all sufficiently large \(n\), the real shore-size threshold satisfies \(p_*(n)=\sqrt n+5/2+O(n^{-1/2})\), where \(p_*(n)\) solves \(p_*(n)(n-p_*(n))=t_+(n)\) in \((0,n/2)\); hence when \(p\sim c\sqrt n\) and \(q=n-p\), the deleted-edge simplex has \(n-2\) obtuse angles for fixed \(0<c<1\) and no obtuse angles for fixed \(c>1\), for all sufficiently large \(n\).

## Assumptions and scope
All graphs are simple and unweighted, all parts have at least two vertices, and the metric is inherited from the full \(n\)-coordinate Euclidean space; deleting a coordinate before measuring is not isometric. The graph \(G_{p,q}\) is connected, so its Laplacian has rank \(n-1\), and \(T_{p,q}\) is an \((n-1)\)-simplex. There is exactly one ridge for each unordered pair of its \(n\) facet labels. Angles refer to the usual convex interior angle, not its supplementary exterior angle. The asymptotic statements use the indicated joint integer limits, not fixed-dimensional limits.

## Proof
Write \(J=\mathbf1\mathbf1^{\mathsf T}\), \(G=L(K_{p,q})^+\) and \(K_0=G^2\), with Moore--Penrose pseudoinverse. The eigenvalues of the complete-bipartite Laplacian on within-shore zero-sum contrasts are \(q\) and \(p\), and its eigenvalue on the one-dimensional between-shore contrast is \(n\). Consequently, if \(A\) and \(B\) denote the two shores,
\[
G=\frac1q(I_A-J_A/p)+\frac1p(I_B-J_B/q)+\frac1n P_{\rm between},
\]
where \(P_{\rm between}=I-J/n-(I_A-J_A/p)-(I_B-J_B/q)\) is an orthogonal projector. Squaring replaces \(1/q,1/p,1/n\) by their squares. In particular, for distinct vertices in the same \(p\)-shore, \((K_0)_{ij}=-1/(pq^2)+q/(pn^3)<0\); in the \(q\)-shore it is \(-1/(qp^2)+p/(qn^3)<0\); for opposite shores it is \(-1/n^3<0\). This proves the assertion about the undeleted simplex.

Let \(b=e_{a_0}-e_{b_0}\), so \(L'=L(K_{p,q})-bb^{\mathsf T}\). The projector decomposition gives \(b^{\mathsf T}Gb=(n-1)/(pq)<1\). In the zero-sum hyperplane the rank-one inverse formula gives
\[
 (L')^+=G+c uu^{\mathsf T},\qquad u=Gb,\qquad c=\frac{pq}{(p-1)(q-1)}.
\]
The four values of \(u\), on \(a_0\), the other \(p-1\) vertices of \(A\), \(b_0\), and the other \(q-1\) vertices of \(B\), respectively, are
\[
\left(\frac{n-1}{nq},-\frac1{nq},-\frac{n-1}{np},\frac1{np}\right).
\]
Put \(v=Gu=K_0b\) and \(s=u^{\mathsf T}u=b^{\mathsf T}K_0b\). Then
\[
K'=((L')^+)^2=K_0+c(vu^{\mathsf T}+uv^{\mathsf T})+c^2suu^{\mathsf T}.
\]
This is an exact identity; the four values of \(v\) are \((D_A-X,O_A-X,X-D_B,X-O_B)\), where
\[
\begin{aligned}
D_A&=(p-1)/(pq^2)+q/(pn^3),&O_A&=-1/(pq^2)+q/(pn^3),\\
D_B&=(q-1)/(qp^2)+p/(qn^3),&O_B&=-1/(qp^2)+p/(qn^3),\\
X&=-1/n^3, &s&=D_A+D_B-2X.
\end{aligned}
\]
For any ordinary \(b\in B\setminus\{b_0\}\) and any ordinary \(a\in A\setminus\{a_0\}\), direct substitution gives the identical mixed entries
\[
 K'_{a_0b}=K'_{ab_0}=\frac{F(p,q)}{(p-1)^2(q-1)^2n^3}.
\]
All other off-diagonal entries are negative. Here is a finite symbolic positivity certificate for this last assertion. Set \(D=(p-1)^2(q-1)^2n^3\), \(P=p-2\ge0\), and \(Q=q-2\ge0\). For the types \(a_0a\), \(a_0b_0\), and \(ab\) with ordinary \(a,b\) in opposite shores, \(-DK'_{ij}\) equals respectively the following three polynomials; all displayed coefficients are positive:
\[
\begin{aligned}
H_1={}&P^4+P^3(3Q+11)+P^2(3Q^2+21Q+42)\\
&+P(6Q^2+38Q+64)+4Q^2+24Q+36,\\
H_2={}&P^4+P^3(4Q+12)+P^2(7Q^2+36Q+53)\\
&+P(4Q^3+36Q^2+102Q+102)+Q^4+12Q^3+53Q^2+102Q+76,\\
H_3={}&P^2(Q^2+2Q+2)+P(2Q^2+8Q+10)+2Q^2+10Q+12.
\end{aligned}
\]
For two distinct ordinary vertices within \(A\), which requires \(p\ge3\), use \(P=p-3\ge0\), \(Q=q-2\ge0\); now \(-q^2DK'_{ij}\) is
\[
\begin{aligned}
H_4={}&P^4(Q^2+2Q+1)+P^3(3Q^3+22Q^2+33Q+13)\\
&+P^2(3Q^4+39Q^3+156Q^2+186Q+57)\\
&+P(12Q^4+120Q^3+387Q^2+393Q+87)\\
&+12Q^4+107Q^3+304Q^2+262Q+26.
\end{aligned}
\]
Swapping the shores covers \(b_0b\) and two ordinary vertices of \(B\). These identities are obtained by inserting the displayed four-group values into \(K'\); an exact polynomial-identity and positive-coefficient checker is supplied in `CHECK.py`. The positivity of every coefficient is an all-parameter algebraic proof, not numerical extrapolation.

For \(x\in H\) the barycentric-coordinate function of the facet omitting vertex \(i\) is \(\lambda_i(x)=1/n+((L')^+x)_i\), since \(x=L'\lambda\) and \(\sum_i\lambda_i=1\). Thus its inward normal is \((L')^+e_i\), and its angle satisfies
\[
\cos\theta_{ij}=-\frac{K'_{ij}}{\sqrt{K'_{ii}K'_{jj}}}.
\]
The diagonal factors are positive and every unordered facet pair defines one ridge. The sign classifications above prove all acute/obtuse/right assertions and the multiplicity \((p-1)+(q-1)=n-2\).

For fixed \(n\), the polynomial \(F(n,t)=(n-1)(n-2)^2+(3n-4)t-t^2\) has precisely one positive root \(t_+(n)\), is positive below that root, and \(t=p(n-p)\) strictly increases for \(2\le p\le n/2\). Checking \(4\le n\le24\) at the largest possible \(t=\lfloor n^2/4\rfloor\) shows positivity, while \(n=25,p=11,q=14\) yields \(F=-86\). Beyond this, the balanced values are strictly negative: for \(n=2m\), they equal \(-m^4+14m^3-24m^2+16m-4<0\) for \(m\ge13\); for \(n=2m+1\), they equal \(-m(m^3-12m^2+4m-1)<0\) for \(m\ge12\). Finally, expansion of the exact root gives \(t_+(n)=n^{3/2}+3n/2+O(\sqrt n)\), whence \(p_*(n)=\sqrt n+5/2+O(n^{-1/2})\). This completes the proof.

## Verification
`CHECK.py` uses exact SymPy rationals to verify the two mixed-entry formulas, all four positive-coefficient certificates, and an independent direct inversion of the deleted-edge graph Laplacian for every pair \(2\le p,q\le7\) (36 graph profiles). It additionally checks the first balanced-sign transition through order 400. Run `python CHECK.py` with Python 3 and SymPy installed. These computations verify symbolic identities and corroborate finite graph instances; the all-order result follows from the rank-one identity and polynomial positivity displayed above.

## Relationship to prior work
Braun and Meyer introduced Laplacian simplices and studied their lattice/Ehrhart geometry. Balletti, Hibi, Meyer and Tsuchiya extended the construction to directed graphs. Devriendt surveys Fiedler's correspondence between graph Laplacians and a *different* resistance simplex whose vertex Gram matrix is the Laplacian pseudoinverse; that resistance-simplex hyperacuteness does not cover the angle signs for the columns-of-Laplacian simplex, whose facet-normal Gram matrix is the **square** of the pseudoinverse. Prior analyses of random supporting directions and circumspheres of complete-bipartite Laplacian simplices do not imply the one-edge-deletion sign classification. The sharp threshold in \(pq\), the first dimension 25, and the \(\sqrt n\)-scale stability transition are the contribution tested here.

## Limitations
The theorem concerns one deleted cross-edge and does not classify arbitrary bipartite edge-deletion patterns or a fully weighted graph. It does not claim all Euclidean angles or intrinsic volumes explicitly, only their sign classification and its complete multiplicity. The claim of historical originality is conditional on the literature and overlap searches performed and is not an independent priority certification.

## References
- B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085v1 (first public June 21, 2017), https://arxiv.org/html/1706.07085v1.
- G. Balletti, T. Hibi, M. Meyer and A. Tsuchiya, *Laplacian simplices associated to digraphs*, arXiv:1710.00252v1 (September 30, 2017), https://arxiv.org/html/1710.00252v1.
- K. Devriendt, *Effective resistance is more than distance: Laplacians, Simplices and the Schur complement*, arXiv:2010.04521 (October 9, 2020), https://arxiv.org/abs/2010.04521.
