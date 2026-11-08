# Exact two-Engel probabilities and square-adjoint rank spectra of star-graph Lie algebras

## Finding

Let \(m\geq 2\), let \(q\) be any prime power, and let \(L=\mathfrak n_{K_{1,m}}(\mathbb F_q)\) be the class-three Lie algebra associated to the star by Gallo and Videla [1]. Define
\[
 d=2m+1+\binom m2,\qquad a_1=m(q-1),\qquad a_2=\binom m2(q-1)^2,\qquad b=q^m-1-a_1-a_2.
\]
For \(x\in L\), let \(N_x(y)=[x,y]\). The *square-adjoint rank enumerator* is
\[
 \mathcal R_{m,q}(z)=\sum_{x\in L}z^{\operatorname{rank}(N_x^2)}.
\]
It is given exactly by
\[
\boxed{\mathcal R_{m,q}(z)=q^{m+\binom m2}\left[(1+a_1)+(q^m-1-a_1)z+(q-1)\left(1+(a_1+a_2)z^{m-1}+bz^m\right)\right]}
\]
when \(q\) is odd, and by
\[
\boxed{\mathcal R_{m,q}(z)=q^{m+\binom m2}\left[q^m+(q-1)\left(1+(q^m-1)z^{m-1}\right)\right]}
\]
when \(q\) is even. Terms with the same exponent are added (in particular when \(m=2\)).

For independent uniform \(X,Y\in L\), define the two-Engel probability
\[
 \mathsf E_2(L)=\Pr([X,[X,Y]]=0).
\]
Then **every** \(m\ge2\) and finite field are covered by
\[
\boxed{\mathsf E_2(L)=q^{-d}\mathcal R_{m,q}(q^{-1}).}
\]
Equivalently, writing \(S=q^m\),
\[
 \mathsf E_2(L)=\frac{S+(q-1)\left(1+(S-1)q^{1-m}\right)}{q^{m+1}}
 \quad(q\text{ even}),
\]
and
\[
 \mathsf E_2(L)=\frac{(1+a_1)+(S-1-a_1)/q+(q-1)\left(1+(a_1+a_2)/q^{m-1}+b/q^m\right)}{q^{m+1}}
 \quad(q\text{ odd}).
\]
The number of elements \(x\) with \([x,[x,L]]=0\) is
\[
\boxed{q^{m+\binom m2}\begin{cases}
q^m+q-1,&q\text{ even},\\
q+m(q-1),&q\text{ odd}.
\end{cases}}
\]
For any fixed even prime power \(q\), \(\mathsf E_2(L)\to q^{-1}\) as \(m\to\infty\). For any fixed odd prime power \(q\), \(\mathsf E_2(L)\to q^{-2}\). The density of square-zero adjoint operators tends to \(q^{-1}\) in even characteristic and to zero in odd characteristic.

## Assumptions and scope

The result concerns finite fields of any characteristic and the specific three-step graph Lie algebras of [1], **not** arbitrary graph Lie algebras and not finite groups. There is no requirement that \(q\) be prime rather than a prime power. The definition of two-Engel probability fixes the repeated variable as the **left** argument, so its polynomial is \([x,[x,y]]\). In a Lie algebra, up to sign, this is equivalent to the left-normed word \([[y,x],x]\). All formulas count actual vectors of the full algebra \(L\), not merely representatives modulo its center.

Write \(c\) for the hub, \(x_1,\ldots,x_m\) for the leaves, \(a_i=[c,x_i]\), and \(z_{ij}\) for the path \(x_i-c-x_j\) with \(i<j\). Its defining nonzero brackets, besides antisymmetry, are exactly
\[
[c,x_i]=a_i,\qquad[x_i,a_j]=[x_j,a_i]=z_{ij}\quad(i<j).
\]
The \(z_{ij}\) are central, all \([a_i,a_j]\) vanish, and \([x_i,a_i]=0\). These are the source's explicit star relations, including in characteristic two [1, section 3].

## Proof

Put \(U=\langle x_1,\ldots,x_m\rangle\), \(A=\langle a_1,\ldots,a_m\rangle\), \(W=\langle z_{ij}:i<j\rangle\), and identify \(U\) and \(A\) with \(\mathbb F_q^m\) using their indexed bases. For \(u=(u_i)\), define the linear map \(T_u:A\longrightarrow W\) by
\[
 T_u(v)=\sum_{i<j}(u_i v_j+u_j v_i)z_{ij}.
\]
It is the restriction to \(A\) of the adjoint action of the leaf vector \(u\). For any
\[
 x=t c+u+a+w\quad(t\in\mathbb F_q,\ u\in U,\ a\in A,\ w\in W),
\]
the bracket relations give
\[
N_x(c)=-\sum_i u_i a_i,\qquad
N_x(v)=t\sum_i v_i a_i-T_v(a)\ \ (v\in U),\qquad
N_x(a')=T_u(a')\ \ (a'\in A),\qquad N_x(W)=0.
\]
Consequently,
\[
\boxed{N_x^2(c)=-T_u(u),\quad N_x^2(v)=tT_u(v),\quad N_x^2(A\oplus W)=0.}
\]
The entire square-adjoint operator, therefore, depends only on \((t,u)\), independent of \((a,w)\). If \(t\ne0\), its image is \(\operatorname{im}T_u\); if \(t=0\), its image is the span of the single vector \(T_u(u)\).

We compute \(\operatorname{rank}T_u\) over an arbitrary field. Let \(s\) be the number of nonzero coordinates of \(u\). The kernel conditions for \(v\in A\) are
\[
 u_i v_j+u_j v_i=0\qquad(i<j).
\]
For \(s=0\) the rank is zero. If \(s\ge1\), choosing an index with \(u_i\ne0\) forces every \(v_j\) outside the support to vanish. On the support put \(r_i=v_i/u_i\); then the equations become \(r_i+r_j=0\) for all distinct support indices. For \(s=1\) or \(2\) they leave exactly one free parameter, so the rank is \(m-1\). For \(s\ge3\), the three pair equations force \(2r_i=0\). Thus for odd characteristic the kernel is zero and the rank is \(m\), while for characteristic two it is one-dimensional and the rank is \(m-1\). Explicitly,
\[
\operatorname{rank}T_u=\begin{cases}
0,&s=0,\\
m-1,&1\le s\le2,\\
m,&s\ge3\text{ and }q\text{ odd},\\
m-1,&s\ge3\text{ and }q\text{ even}.
\end{cases}
\]
Furthermore,
\[
T_u(u)=2\sum_{i<j}u_i u_jz_{ij}.
\]
It is zero for every \(u\) in characteristic two. In odd characteristic it is nonzero precisely when at least two coordinates of \(u\) are nonzero. These facts give the rank of \(N_x^2\) for every \(x\) without any genericity assumption.

Exactly \(a_1=m(q-1)\) leaf vectors have support one, exactly \(a_2=\binom m2(q-1)^2\) have support two, and exactly \(b=q^m-1-a_1-a_2\) have support at least three. There are \(q^{m+\binom m2}\) independent choices of \((a,w)\) over each \((t,u)\). Counting the \(t=0\) and the \(q-1\) nonzero choices of \(t\) separately immediately yields both displayed rank-enumerator polynomials.

For each fixed \(x\), the linear map \(N_x^2:L\to L\) has exactly \(q^{d-\operatorname{rank}N_x^2}\) zeros. Uniformly averaging over \(x\) proves
\[
 \mathsf E_2(L)=\frac1{q^d}\sum_{x\in L}q^{-\operatorname{rank}N_x^2}=q^{-d}\mathcal R_{m,q}(q^{-1}).
\]
The constant coefficient of \(\mathcal R_{m,q}\) counts elements with \(N_x^2=0\), proving the two-Engel-element formula. Finally, at fixed \(q\), the odd-characteristic contribution with \(t=0\) has mean \(q^{-1}+o(1)\) conditional probability and occupies a fraction \(q^{-1}\) of \(x\); all other contributions tend to zero. In even characteristic the entire \(t=0\) stratum has rank zero and the other stratum's mean tends to zero. This proves the two limits and the stated zero-rank density limits.

## Verification

The standalone program `verify.py` constructs the exact Lie bracket on the basis \(c,x_i,a_i,z_{ij}\), computes matrix squares of adjoint operators, and independently Gaussian-eliminates their ranks over prime fields of sizes two, three, and five and the nonprime field \(\mathbb F_4\). It exhausts all \((t,u)\) for ten field/star pairs, verifies every rank against the piecewise formula, and checks the complete enumerator and resulting two-Engel probability by exact fractions. This covers 1,477 distinct \((t,u)\) representatives. The full multiplication table is used; the proof explains why the remaining \((a,w)\) do not affect the square-adjoint operator. Recorded output appears in `verify_output.txt`.

An additional direct nested-bracket pair enumeration, separate from the matrix-rank computation, checked \((q,m)=(2,2)\) and \((3,2)\), obtaining exactly 3,328 and 269,001 satisfying pairs among 4,096 and 531,441 possible ordered pairs respectively, matching \(13/16\) and \(41/81\). These finite experiments test the implementation; the theorem for all \(m\) and finite fields follows from the proof.

## Relationship to prior work

Gallo and Videla [1] construct the graph Lie algebras and give the star brackets and lower-central-series dimensions. Their results do not enumerate square-adjoint ranks or two-Engel pairs. Mann and Martínez [2] give general threshold bounds for Engel-law probabilities in finite Lie algebras, and Larsen and Shalev [3] extend a general probabilistic-polynomial-identity threshold. Those bounds do not specify the present probabilities, rank strata, characteristic-two transition, or asymptotics. Other calculations of commuting probabilities and Kirillov-form ranks for star Lie algebras concern different maps: \(\operatorname{ad}_x\) and \(\lambda([-, -])\) respectively, not \(\operatorname{ad}_x^2\). This result makes no claim of novelty for the original Lie brackets or general probabilistic identity theorems.

## Limitations

Literature searching cannot establish absolute historical priority. There may be an unindexed equivalent formula under second-Engel degrees, adjoint nilpotence profiles, or probabilistic identities of nilpotent Lie algebras. The statement is confined to the star family \(K_{1,m}\) with \(m\ge2\) and finite coefficient fields; it does not give the full distribution of nonzero Engel word values or a classification for arbitrary graphs.

## References

[1] Andrea L. Gallo and Denis E. Videla, *Nilpotent Lie algebras of nilpotence class at most three via graphs*, arXiv:2610.33963v1, first posted 2026-10-25, sections 2–3, especially the star relations. https://arxiv.org/html/2610.33963v1

[2] Avinoam Mann and Consuelo Martínez, *Groups nearly of prime exponent and nearly Engel Lie algebras*, Archiv der Mathematik **71** (1998), 5–11, DOI:10.1007/s000130050227.

[3] Michael Larsen and Aner Shalev, *Residually finite dimensional algebras and polynomial almost identities*, arXiv:2005.11594, first posted 2020-05-23, introduction and Theorem 3. https://arxiv.org/abs/2005.11594
