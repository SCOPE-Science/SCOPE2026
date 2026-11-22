# Three-level bracket-fiber law on nilpotent slices of Schrödinger Lie algebras

## Finding

Let \(q\) be an odd prime power and \(n\ge1\). Let \(L=\mathfrak{sch}_n(\mathbb F_q)\) be the \((2n+4)\)-dimensional Lie algebra described below. Every target in the affine slice
\[
C=e+\sum_{i=1}^{n}(r_i x_i+s_i y_i)+c z,
\qquad r_i,s_i,c\in\mathbb F_q,
\]
has an explicitly determined number \(F(C)=|\{(A,B)\in L^2:[A,B]=C\}|\) of **ordered** commutator representations. Define
\[
R_{n,q}(b)=\#\left\{(t_1,\ldots,t_n)\in\mathbb F_q^n:\sum_i t_i^2=b\right\}.
\]
Then
\[
\boxed{F(C)=
\begin{cases}
q^{2n+2}(q^2-1),&\text{some }s_i\ne0,\\
q^{n+3}(q^2-1)\,R_{n,q}\!\left(\sum_i r_i^2-2c\right),&s_1=\cdots=s_n=0.
\end{cases}}
\]

This gives an exact **three-level** distribution on the entire \(q^{2n+1}\)-element slice. Put \(D=q^{n+3}(q^2-1)\), \(U=q^{2n+2}(q^2-1)=Dq^{n-1}\) and let \(\chi\) be the quadratic character on \(\mathbb F_q\), with \(\chi(0)=0\).

For even \(n=2k\ge2\), set \(\epsilon=\chi((-1)^k)\). The three ordered-pair fiber sizes and target multiplicities are:

| Fiber size | Number of targets |
|---|---:|
| \(U+D(q-1)\epsilon q^{k-1}\) | \(q^n\) |
| \(U-D\epsilon q^{k-1}\) | \((q-1)q^n\) |
| \(U\) | \(q^{2n+1}-q^{n+1}\) |

For odd \(n=2k+1\), they are:

| Fiber size | Number of targets |
|---|---:|
| \(U-Dq^k\) | \(q^n(q-1)/2\) |
| \(U\) | \(q^{2n+1}-q^{n+1}+q^n\) |
| \(U+Dq^k\) | \(q^n(q-1)/2\) |

For \(n=1\), exactly \(q(q-1)/2\) targets on this affine slice are **not** individual commutators; for every \(n\ge2\), every target on the slice is a commutator. At all dimensions the three displayed fiber sizes are distinct. For an arbitrary nonzero nilpotent element in the \(\mathfrak{sl}_2\)-projection, the same fiber-size distribution follows by a \(\operatorname{GL}_2\)-change of coordinates, acting on the central coordinate by its determinant.

## Assumptions and scope

The field is \(\mathbb F_q\) with odd \(q\), and \(n\) is any positive integer. Write \(L=\mathfrak{sl}_2(\mathbb F_q)\ltimes (V\oplus\mathbb F_q z)\), where \(V=\bigoplus_{i=1}^n(\mathbb F_q x_i\oplus\mathbb F_q y_i)\). The \(\mathfrak{sl}_2\)-action on each two-space is the standard column action, and \([x_i,y_j]=\delta_{ij}z\) with all other Heisenberg brackets zero. Thus
\[
[(X,u,a z),(Y,v,b z)]
=([X,Y],Xv-Yu,\omega(u,v)z),
\]
where \(\omega((\alpha_i,\alpha_i'),(\beta_i,\beta_i'))=\sum_i(\alpha_i\beta_i'-\alpha_i'\beta_i)\), and \(X,Y\in\mathfrak{sl}_2\). The distinguished matrix is \(e=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\). The theorem counts ordered pairs in the full Lie algebra, including arbitrary central coordinates; it makes no claim about arbitrary semisimple \(\mathfrak{sl}_2\)-projections or characteristic two.

## Proof

**1. The \(\mathfrak{sl}_2\) pairs.** Write
\[
X=\begin{pmatrix}a&b\\c_0&-a\end{pmatrix},\qquad
Y=\begin{pmatrix}d&f\\g&-d\end{pmatrix}.
\]
If \([X,Y]=e\), trace invariance gives \(\operatorname{tr}(Xe)=\operatorname{tr}(Ye)=0\), so \(c_0=g=0\). The remaining equation is \(2(af-db)=1\). Thus \((a,b)\) and \((d,f)\) are ordered bases with fixed determinant \(1/2\), and there are exactly \(|\operatorname{SL}_2(\mathbb F_q)|=q(q^2-1)\) pairs. In particular \((a,d)\ne(0,0)\).

**2. Each Heisenberg block.** Set \(u_i=(\alpha_i,\alpha_i')\) and \(v_i=(\beta_i,\beta_i')\). The requirement that the \(i\)-th two-vector of \([A,B]\) be \((r_i,s_i)\) reads
\[
a\beta_i+b\beta_i'-d\alpha_i-f\alpha_i'=r_i,
\qquad -a\beta_i'+d\alpha_i'=s_i.
\]
These two equations are independent because \((a,d)\ne(0,0)\). Their solution set is an affine two-space: \(q^2\) possibilities for each \(i\), hence \(q^{2n}\) for all blocks. Both central coordinates of the inputs are free, contributing another factor \(q^2\).

**3. Uniform branch.** If some \(s_i\ne0\), simultaneously changing \((\alpha_i,\beta_i)\) to \((\alpha_i+a t,\beta_i+d t)\) preserves the two-vector equations while changing \(\omega(u,v)\) by \(-s_i t\). Therefore every central output occurs exactly \(q^{2n-1}\) times for each fixed \((X,Y)\), giving
\[
F(C)=q^2\,q(q^2-1)\,q^{2n-1}=q^{2n+2}(q^2-1).
\]

**4. Square-form branch.** If all \(s_i=0\), put \(r=\sum_i r_i x_i\) and \(t=-\sum_i r_i y_i\). The map
\[
\Phi_t(X+v+c z)=X+(v-Xt)+\left(c+\omega(t,v)-\tfrac12\omega(t,Xt)\right)z
\]
is a Lie automorphism. Indeed its bracket compatibility follows from \(\omega(Xv,w)+\omega(v,Xw)=0\) and \(\omega(t,[X,Y]t)=-2\omega(Xt,Yt)\); it is invertible with inverse \(\Phi_{-t}\). It sends \(e+c'z\) to \(e+r+(c'+\tfrac12\sum_i r_i^2)z\). Thus the desired fiber is equal to that at \(e+c'z\) for \(c'=c-\tfrac12\sum_i r_i^2\).

For the latter target, the second component equations imply \(\alpha_i'=a t_i,\ \beta_i'=d t_i\) with one freely chosen \(t_i\). The first equation becomes \(a\beta_i-d\alpha_i=t_i/2\), leaving one free field coordinate in \((\alpha_i,\beta_i)\). Consequently \(\omega(u_i,v_i)=-t_i^2/2\), and each solution of \(\sum_i t_i^2=-2c'\) lifts to \(q^n\) choices of \((u,v)\). Multiplying by \(q^2\) for central input coordinates and by \(q(q^2-1)\) for \((X,Y)\) yields \(D R_{n,q}(-2c')\), the formula claimed.

**5. Explicit square-form fibers.** The classical additive-character identity for the nondegenerate form \(\sum_i t_i^2\), with quadratic Gauss sum \(G\) satisfying \(G^2=\chi(-1)q\), gives
\[
R_{2k,q}(b)=
\begin{cases}
q^{2k-1}+(q-1)\chi((-1)^k)q^{k-1},&b=0,\\
q^{2k-1}-\chi((-1)^k)q^{k-1},&b\ne0,
\end{cases}
\]
and
\[
R_{2k+1,q}(b)=
\begin{cases}
q^{2k},&b=0,\\
q^{2k}+\chi((-1)^k b)q^k,&b\ne0.
\end{cases}
\]
As \(c\) varies at fixed \(r_i\), the argument \(\sum_i r_i^2-2c\) runs bijectively over \(\mathbb F_q\); the targets with \((s_i)\ne0\) number \(q^{2n+1}-q^{n+1}\). Combining these counts proves both three-level tables, including the \(n=1\) zero-fiber statement. As a checksum, the weighted sum of all target-fiber sizes is \(q^{4n+3}(q^2-1)\), equal to the number of pairs whose \(\mathfrak{sl}_2\) brackets equal \(e\).

Finally, any nonzero nilpotent matrix in \(\mathfrak{sl}_2(\mathbb F_q)\) is \(\operatorname{GL}_2\)-conjugate to \(e\). For \(g\in\operatorname{GL}_2\), the map \((X,v,c z)\mapsto(gXg^{-1},gv,\det(g)c z)\) is an automorphism, so the fiber-size multiset is unchanged.

## Verification

The standalone file `check_schrodinger_fibers.py` independently enumerates the original matrix-bracket equations over prime fields; it does not use the theorem's formulas in its enumeration step. It checks every target in the indicated affine slice and both central input coordinates for \((q,n)=(3,1),(3,2),(3,3),(5,1),(5,2),(7,1)\). The reported distinct-level/multiplicity data include \((q,n)=(3,1)\): \((0,3),(648,21),(1296,3)\) and \((5,2)\): \((300000,100),(375000,3000),(675000,25)\). The program also confirms that the sum of all fiber sizes equals \(q^{4n+3}(q^2-1)\). These finite tests are not the proof for arbitrary prime powers; that proof is Steps 1–5 above.

## Relationship to prior work

G. Sosnov, *Uniqueness of addition in Schrödinger algebras* (arXiv:2611.16812v1, first submitted 12 November 2026), proves the qualitative bracket-width criterion and, in Lemma 3.3, identifies a sum-of-squares obstruction for targets \(e+c z\). That lemma supplies the natural gap: it neither counts ordered pairs nor classifies the full affine slice with arbitrary Heisenberg coordinates. The present theorem derives every such fiber and its three-level distribution, rather than claiming the elementary finite-field quadratic-form counts themselves as new.

Earlier exact central-target calculations for the same finite Lie algebra concern outputs whose \(\mathfrak{sl}_2\)-projection is zero, which is disjoint from the slice treated here. Earlier centralizer spectra determine the zero-commutator fiber, not fixed noncentral fibers. Fulman and Guralnick's finite-field commuting-pair enumeration treats classical Lie algebras rather than these prescribed nonzero fibers of a Heisenberg extension. The standard character-sum identity for nondegenerate quadratic forms is used as established background.

## Limitations

The result is restricted to odd characteristic and nonzero nilpotent \(\mathfrak{sl}_2\)-projections; it is not a full classification of bracket fibers over arbitrary targets. Prime-field computations are checks, not a replacement for the symbolic all-prime-power proof. A claim of historical first discovery beyond the inspected indexed literature would require broader specialist review. No independent mathematical audit has been performed.

## References

1. G. Sosnov, *Uniqueness of addition in Schrödinger algebras*, arXiv:2611.16812v1 (2026-11-12), https://arxiv.org/html/2611.16812v1.
2. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499 (2016), https://arxiv.org/abs/1611.05499.
3. R. Lidl and H. Niederreiter, *Finite Fields*, second edition, Cambridge University Press, 1997, Theorems 6.26–6.27 (standard quadratic-form counts).
