# Field-dependent local automorphisms of the three-dimensional null-filiform associative algebra

## Finding

Let \(k\) be any field and let \(B=t k[t]/(t^4)\) be the three-dimensional, nonunital, commutative associative algebra with ordered basis \((t,t^2,t^3)\). A *linear local automorphism* is a \(k\)-linear map \(T:B\to B\) such that for every \(x\in B\) some \(k\)-algebra automorphism \(\phi_x\) satisfies \(T(x)=\phi_x(x)\). Its matrix is necessarily lower triangular, and the following is a complete classification.

When \(\operatorname{char}k\ne 2\), the local automorphisms are exactly
\[
T=\begin{pmatrix}a&0&0\\ b&c&0\\ d&e&f\end{pmatrix},\qquad
 a\in k^\times,\quad b,d,e\in k,\quad c\in(k^\times)^2,\quad f\in(k^\times)^3.
\]
Here \((k^\times)^j=\{u^j:u\in k^\times\}\). When \(\operatorname{char}k=2\), the local automorphisms are exactly
\[
T=\begin{pmatrix}a&0&0\\ b&u^2&0\\ d&0&u^3\end{pmatrix},\qquad
 a,u\in k^\times,\quad b,d\in k.
\]
In either characteristic, the genuine automorphisms are exactly
\[
\phi_{u,v,w}=\begin{pmatrix}u&0&0\\ v&u^2&0\\ w&2uv&u^3\end{pmatrix},\qquad
 u\in k^\times,\quad v,w\in k.
\]
These sets are groups under composition. The local-automorphism group has a lower-unitriangular normal subgroup with diagonal subgroup \(k^\times\times(k^\times)^2\times(k^\times)^3\) when \(\operatorname{char}k\ne2\); in characteristic two it is \(k^2\rtimes(k^\times\times k^\times)\), with the diagonal parametrized by \((a,u)\mapsto(a,u^2,u^3)\).

For every finite field \(k=\mathbb F_q\), writing \(g=\gcd(3,q-1)\), the number of local automorphisms is
\[
|\operatorname{LAut}(B)|=
\begin{cases}
\displaystyle q^3(q-1)^3/(2g),&q\text{ odd},\\
q^2(q-1)^2,&q\text{ even}.
\end{cases}
\]
The genuine automorphism group has size \(q^2(q-1)\). Consequently, \(\operatorname{LAut}(B)=\operatorname{Aut}(B)\) **if and only if** \(k=\mathbb F_2\), among *all* fields \(k\). This is a sharp field-dependent local-to-global boundary for the fixed three-dimensional algebra.

## Assumptions and scope

All maps in this theorem are \(k\)-linear. The algebra is nonunital; its multiplication is \(t\cdot t=t^2\), \(t\cdot t^2=t^3\), and products of total degree at least four vanish. The classification is valid for arbitrary fields, including imperfect fields and characteristic two. The cardinality statements require a finite field.

## Proof

Every algebra automorphism is determined by the image \(\phi(t)=ut+vt^2+wt^3\) with \(u\ne0\); products give \(\phi(t^2)=u^2t^2+2uvt^3\) and \(\phi(t^3)=u^3t^3\). This proves the displayed automorphism normal form. Evaluating a local map on each basis element forces its matrix to be lower triangular with nonzero diagonal, say \(T=\bigl(\begin{smallmatrix}a&0&0\\b&c&0\\d&e&f\end{smallmatrix}\bigr)\).

For a vector \(x=x_1t+x_2t^2+x_3t^3\), equality \(T(x)=\phi_{u,v,w}(x)\) is precisely
\[
ux_1=ax_1,\quad vx_1+u^2x_2=bx_1+cx_2,\quad
wx_1+2uvx_2+u^3x_3=dx_1+ex_2+fx_3.
\]
If \(x_1\ne0\), choose \(u=a\), solve the second equation uniquely for \(v\), and solve the third uniquely for \(w\); there is no additional restriction in any characteristic.

If \(x_1=0\) and \(x_2\ne0\), the second equation requires \(c=u^2\). When \(2\ne0\), the third equation can be solved for \(v\) for every value of \(x_3\), with arbitrary \(e,f\). When \(2=0\), the third equation reduces to \((e+(f-u^3)x_3/x_2)x_2=0\); since squaring in a field of characteristic two is injective, \(u\) is uniquely determined by \(c\). Testing \(x_3=0\) and \(x_3=x_2\) yields exactly \(e=0\) and \(f=u^3\). These conditions are also sufficient for every \(x\) with \(x_1=0\), \(x_2\ne0\).

If \(x_1=x_2=0\), \(x_3\ne0\), the third equation is \(u^3=f\). In characteristic different from two this is independent of \(c=u^2\), because the required \(u\) can depend on \(x\). In characteristic two it follows from the previously obtained condition \(f=u^3\). The zero vector imposes no condition. This proves necessity and sufficiency of both classifications.

The local maps form a group: composition is local by composing witnesses, and the inverse of a bijective local map is local by applying a witness at the preimage. The described matrices are invertible and their diagonal and unipotent parts give the stated group decompositions.

For finite odd \(q\), there are \(q-1\) choices for \(a\), \(q^3\) for \((b,d,e)\), \((q-1)/2\) for the square \(c\), and \((q-1)/\gcd(3,q-1)\) for the cube \(f\). For even \(q\), the parameterization has \((q-1)^2q^2\) distinct choices, because the square map is injective. The automorphism normal form has \((q-1)q^2\) choices.

Finally, if \(\operatorname{char}k\ne2\), taking \(a=c=f=1\), \(b=d=0\), \(e=1\) gives a local but nongenuine automorphism. If \(\operatorname{char}k=2\) and \(k\ne\mathbb F_2\), select \(a\in k^\times\setminus\{1\}\) and \(u=1\); \(\operatorname{diag}(a,1,1)\) is local but not a genuine automorphism. Over \(\mathbb F_2\), the characteristic-two normal form is exactly \(\phi_{1,b,d}\). Hence equality of the two groups occurs exactly over \(\mathbb F_2\).

## Verification

The accompanying standalone `verify.py` constructs each algebra automorphism by substitution and, without assuming the classification, computes the orbit of every algebra element. It then checks every invertible lower-triangular linear map against the defining local property for \(q=2,3,4,5\). It uses direct field arithmetic, including an explicit representation of \(\mathbb F_4\), and confirms the respective local/genuine counts \((4,4)\), \((108,18)\), \((144,48)\), and \((4000,100)\). The finite tests corroborate the arbitrary-field proof; they do not establish it on their own. Run `python3 verify.py`; successful execution prints `VERIFY_OK`.

## Relationship to prior work

Arzikulov, Karimjanov, and Umrzaqov developed the structural theory of local and 2-local automorphisms for null-filiform and filiform associative algebras, including the lower-triangular form in the characteristic-zero setting (2023 preprint, 2024 journal version, Theorem 3.2 and its proof). The novelty sought here is the exact classification over **every** ground field in dimension three: the independent square/cube residue constraints in odd characteristic, the coupled constraints caused by vanishing \(2uv\) in characteristic two, the finite-field group orders, and the unique local-to-global field \(\mathbb F_2\). The same prior work supplies the genuine automorphism normal form; that normal form is rederived above for completeness and is not claimed as new. Direct research-record searches and accessible prior-claim comparisons did not reveal a theorem implying these ground-field refinements. This is a best-knowledge comparison, not proof of publication priority.

## Limitations

This result concerns the three-dimensional nonunital null-filiform associative algebra and *linear* local automorphisms. It does not classify nonadditive pointwise-local maps, higher-dimensional null-filiform algebras, or 2-local automorphisms. Its uniqueness assertion concerns equality of the two automorphism groups for the specified algebra, not for all finite-dimensional algebras. Broader unpublished or nonindexed treatments of field-dependent local automorphisms could contain an equivalent result.

## References

1. F. N. Arzikulov, I. A. Karimjanov, S. M. Umrzaqov, *Local and 2-local automorphisms of finite-dimensional nilpotent associative algebras*, arXiv:2305.13720, first posted 2023-05-23.
2. F. Arzikulov, I. Karimjanov, S. Umrzaqov, *Local and 2-local automorphisms of null-filiform and filiform associative algebras*, J. Algebra Comb. Discrete Appl. **11** (2024), 151–164, DOI:10.13069/jacodesmath.v11i3.279; see Theorems 2.1, 3.2.
