# Complete endomorphism and retraction ranks of the \(E_\lambda\) evolution-algebra family

## Finding
Let \(K\) be any field and \(\lambda\in K^\times\). In the three-dimensional evolution algebra \(E_\lambda\) with natural basis \(e_1,e_2,e_3\) and products
\[
e_1^2=-e_1-e_3,\qquad e_2^2=-2e_1+\lambda e_2+(\lambda-2)e_3,\qquad e_3^2=e_1+e_3,\qquad e_i e_j=0\ (i\ne j),
\]
all \(K\)-linear algebra endomorphisms are classified by the two disjoint normal-form families below. Put \(u=e_1+e_3\), \(v=e_2+e_3\), \(w=e_3\), so that \((u,v,w)\) is a basis.

**Family A:**
\[
T(u)=T(v)=0,\quad T(w)=s u+r w,\quad r(2s+r)=0.
\]
**Family B:**
\[
T(u)=a u,\quad T(v)=c u+v,\quad T(w)=s u+r w,
\]
where
\[
a=1+(\lambda-2)c,\qquad a(r-1)=0,\qquad cr+s+r=a,\qquad 2sr+r^2=a.
\]
All scalar parameters belong to \(K\). These equations are necessary and sufficient, without assumptions on characteristic or algebraic closure.

For \(K=\mathbb F_q\), define the endomorphism rank polynomial
\[
R_{\lambda,q}(z)=\sum_{T\in\operatorname{End}_K(E_\lambda)} z^{\operatorname{rank}_K T}.
\]
It is exactly
\[
\boxed{R_{\lambda,q}(z)=
\begin{cases}
1+qz+z^3,&\operatorname{char}K=2,\\
1+(2q-2)z+z^3,&\operatorname{char}K\ne2,\ \lambda=2,\\
1+(2q-1)z+(q-1)z^2+(q-1)z^3,&\operatorname{char}K\ne2,\ \lambda=4,\\
1+(2q-1)z+z^3,&\operatorname{char}K\ne2,\ \lambda\notin\{2,4\}.
\end{cases}}
\]
Consequently rank-two endomorphisms exist **if and only if** \(\lambda=4\), and then there are exactly \(q-1\) of them. The numbers of composition-idempotent endomorphisms in the same four cases are respectively \(3,3,5,4\). Thus the noninvertible part of the monoid detects an additional parameter boundary not visible from the automorphism count alone.

## Assumptions and scope
An algebra homomorphism is \(K\)-linear and preserves multiplication, but is not required to be unital or invertible; this algebra is not assumed associative or unital. The value \(\lambda\) is nonzero in \(K\). The integers \(2,4\) in case distinctions mean their images in \(K\); in characteristic two, \(\lambda=2\) and \(\lambda=4\) cannot occur. All ranks are vector-space image dimensions. The finite-field formula holds for every prime-power \(q\), not merely prime fields.

The multiplication table in the basis \((u,v,w)\) is
\[
u^2=0,\quad uv=uw=vw=w^2=u,\quad v^2=-u+\lambda v.
\]
In particular \(S=E_\lambda^2=Ku+Kv\), since \(\lambda\ne0\), and \(S^2=S\).

## Proof
**Step 1: restriction to the square.** Any homomorphism \(T\) satisfies \(T(S)\subseteq S\). If \(x=bu+dv\in S\), then
\[
x^2=(2bd-d^2)u+\lambda d^2v.
\]
Thus \(x^2=0\) implies \(d=0\) over every field. As \(u^2=0\), write \(T(u)=a u\). Write \(T(v)=c u+d v\). Preservation of \(uv=u\) gives \(a(d-1)=0\). Preservation of \(v^2=-u+\lambda v\) gives \(d^2=d\) and \(a+(2d-\lambda)c=d^2\). Since a field has only the idempotent scalars \(0,1\), either \(d=0\) with \(a=c=0\), or \(d=1\) with \(a=1+(\lambda-2)c\). These are precisely the two indicated restrictions.

**Step 2: lifting the restriction.** In either case write \(T(w)=s u+t v+r w\). The \(v\)-coordinate of \(T(w)^2\) is \(\lambda t^2\), but \(T(w^2)=T(u)=a u\). Hence \(t=0\). The relations \(uw=vw=w^2=u\) now give, respectively,
\[
a(r-1)=0,\quad cr+d(s+r)=a,\quad 2sr+r^2=a.
\]
If \(d=0\), all of \(a,c,d\) vanish and these reduce to \(r(2s+r)=0\), giving A. If \(d=1\), they yield B. Conversely, A or B preserves each of the six displayed basis products; bilinearity then proves that it is a homomorphism. The normal forms are disjoint because the coefficient of \(v\) in \(T(v)\) differs.

**Step 3: resolving the scalar equations.** In A, if \(\operatorname{char}K=2\) then \(r^2=0\) forces \(r=0\), with arbitrary \(s\). In other characteristics, either \(r=0\) with arbitrary \(s\), or \(r\ne0\) and \(s=-r/2\).

In B, if \(a\ne0\) then \(r=1\), hence \(s=a-c-1\), and the last equation becomes \(a=1+2c\). Comparison with \(a=1+(\lambda-2)c\) gives \((\lambda-4)c=0\). For \(\lambda\ne4\), the only such map is the identity. For \(\lambda=4\), all \(c\) with \(a=1+2c\ne0\) give distinct automorphisms \(T(u)=a u, T(v)=v+c u,T(w)=w+c u\).

If \(a=0\), then necessarily \(\lambda\ne2\) and \(c=-1/(\lambda-2)\). The remaining equations give \(s=-(c+1)r\) and
\[
\frac{\lambda-4}{\lambda-2}r^2=0.
\]
Thus for \(\lambda\ne4\), the only solution has \(r=s=0\), yielding one rank-one map. For \(\lambda=4\), there are arbitrary \(r\), with \(c=-1/2\), \(s=-r/2\). Their ranks are one for \(r=0\) and two for \(r\ne0\). This also proves that all rank-two maps have the same image \(K(v-u/2)+K(w-u/2)\) and exist only at \(\lambda=4\).

**Step 4: finite-field ranks and retractions.** Family A has \(q\) members in characteristic two and \(2q-1\) otherwise, always zero plus rank-one maps. Family B contributes one rank-one map for every \(\lambda\ne2,4\), and the identity; it contributes only the identity at \(\lambda=2\). At \(\lambda=4\), B consists of \(q-1\) invertible maps and \(q\) singular maps, one of rank one and \(q-1\) of rank two. Summing proves the displayed rank polynomial.

For \(T\) in A, the identity \(T^2(w)=rT(w)\) shows that the only composition-idempotents are zero and, in odd characteristic, the map \(T(w)=w-u/2\), \(T(u)=T(v)=0\). In B, the rank-one map at \(a=0,r=0\) is idempotent; at \(\lambda=4\), the rank-two map \(r=1\) is also idempotent; and among automorphisms only the identity is idempotent. These lists are exhaustive and yield the four retraction counts \(3,3,5,4\) in the stated order.

## Verification
The two included scripts `verify.py` and `verify_f4.py` implement multiplication in a fixed three-vector basis independently of the displayed rank-polynomial formula. `python verify.py` checks all \(23\) nonzero parameters over prime fields of orders \(2,3,5,7,11\); it checks every candidate against all six products, checks the rank distribution, and, for orders \(2,3\), searches **every** \(3\times3\) matrix and verifies equality with the normal-form list. `python verify_f4.py` independently searches all \(4^9=262144\) matrices for each of the three nonzero parameters over \(\mathbb F_4\), built as \(\mathbb F_2[X]/(X^2+X+1)\). Both scripts have been run successfully and print `VERIFY_OK` and `F4_EXHAUSTIVE_OK`, respectively. These finite tests support the calculation; the proof above establishes all fields and ranks.

## Relationship to prior work
Hu and Wen introduce the family, prove its non-solvability and compute its element-idempotents, including the exceptional value \(\lambda=2\). The present theorem instead determines **all algebra endomorphisms**, including singular maps, and counts composition-idempotent endomorphisms; these are different objects from element-idempotents.

The published result *A single symmetry jump in the \(E_\lambda\) evolution-algebra family* determines only invertible homomorphisms, showing that automorphism groups are trivial off \(\lambda=4\) and are \(K^\times\) at \(\lambda=4\). Those invertible maps agree with the rank-three stratum above, but do not imply the other strata, retraction counts or characteristic-two endomorphism law. The published *Complete subalgebra lattices and two distributivity transitions in a non-solvable evolution-algebra family* classifies potential images as subalgebras, but neither counts nor classifies the maps onto them. Its exceptional two-dimensional subalgebra at \(\lambda=4\) is exactly the image of the rank-two endomorphisms constructed here.

Cabrera Casado, Siles Molina and Velasco classify three-dimensional evolution algebras up to isomorphism; their classification (including the two-dimensional-square cases and change-of-basis analysis) is relevant, but does not provide this complete noninvertible endomorphism census. Related studies of endomorphisms of *perfect*, *one-dimensional-square* or *nilpotent chain* evolution algebras do not cover these stable-square, non-solvable algebras, for which \(\dim E_\lambda^2=2<3\) and \((E_\lambda^2)^2=E_\lambda^2\).

## Limitations
The theorem concerns only this specified three-dimensional family, not all evolution algebras. It is a classification of ordinary linear algebra maps, not of endomorphism schemes or non-linear maps. Although the relevant paper and published nearby findings were compared with their full mathematical statements, an unindexed case-by-case calculation or a general endomorphism theorem with an implicit specialization could affect historical priority. No independent mathematical audit has been performed.

## References
1. X.-Y. Hu and R. Wen, *Idempotent-free non-solvable evolution algebras over \(\mathbb C\)*, arXiv:2609.25023v1, first posted 2026-08-12, https://arxiv.org/abs/2609.25023.
2. *A single symmetry jump in the \(E_\lambda\) evolution-algebra family*, published mathematical record (2026), https://github.com/published-finding corpus/2026.
3. *Complete subalgebra lattices and two distributivity transitions in a non-solvable evolution-algebra family*, published mathematical record (2026), https://github.com/published-finding corpus/2026.
4. Y. Cabrera Casado, M. Siles Molina and M. V. Velasco, *Classification of three-dimensional evolution algebras*, Linear Algebra Appl. 524 (2017), 68–108, https://doi.org/10.1016/j.laa.2017.02.015.
