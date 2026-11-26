# The characteristic-two Frobenius-zero cone of the rank-two truncated Witt algebra

## Finding

Let \(k\) be any algebraically closed field of characteristic \(2\). For the truncated polynomial algebra \(R=k[x,y]/(x^2,y^2)\), write \(W=\operatorname{Der}_k(R)\). It has dimension eight and its restricted square is composition of a derivation with itself, \(D^{[2]}=D^2\). The **reduced height-one nilpotent cone**
\[
\mathcal N_1(W)=\{D\in W:D^{[2]}=0\}_{\mathrm{red}}
\]
is an irreducible, rational affine variety of dimension four. The nonzero-constant-term locus is a dense, smooth, four-dimensional rational open subset. For each finite field \(\mathbb F_q\) of characteristic two,
\[
\boxed{\#\mathcal N_1(W)(\mathbb F_q)=q^4+q^3-q.}
\]
The zero-constant-term subvariety has \(q^3+q^2-q\) rational points, and its complement has \((q^2-1)q^2\) rational points.

## Assumptions and scope

The algebra has basis \(1,x,y,xy\), where \(x^2=y^2=0\). Every derivation is uniquely
\[
D=F\partial_x+G\partial_y,\qquad
F=a+bx+cy+dxy,\qquad G=e+ux+vy+wxy.
\]
The letters \(a,b,c,d,e,u,v,w\) range independently over the ground field before the square-zero condition is imposed. In characteristic two, composition \(D^2\) is a derivation, so \(D^2=0\) if and only if its values on \(x,y\) vanish. The geometric assertion is about the underlying **reduced** zero locus of these equations. The arithmetic assertion is valid for every field size \(q=2^e\), not only prime fields. Nothing here asserts a classification of all nilpotent derivations for which a higher restricted power vanishes.

## Proof

**Step 1: explicit equations.** By the Leibniz rule and \(x^2=y^2=0\), comparison of the coefficients of \(1,x,y,xy\) in \(D^2x=D(F)\) and \(D^2y=D(G)\) gives precisely
\[
\begin{aligned}
ab+ce&=0, & b^2+cu+de&=0,\\
ad+bc+cv&=0, & cw+dv&=0,\\
au+ev&=0, & bu+ew+uv&=0,\\
aw+cu+v^2&=0, & bw+du&=0.
\end{aligned}
\]
No excluded denominator or hypothesis about algebraic closure is used to obtain this system.

**Step 2: open stratum.** The linear coordinate changes of \(R\) act on derivations and transitively on nonzero constant vectors. Thus, for fiber counting and geometric irreducibility, a fixed nonzero vector may be put in the form \((a,e)=(a,0)\) with \(a\ne0\). The equations force \(b=u=0\), while \(c,v\) are unrestricted and
\[
d=cv/a,\qquad w=v^2/a.
\]
Consequently, the projection to the punctured constant-vector plane has affine-plane fibers. On the chart \(a\ne0\), the change \(y\mapsto y+(e/a)x\) removes the second constant coordinate algebraically and gives rational affine-plane coordinates on the fibers. Hence the whole nonzero-constant locus is irreducible, smooth and rational of dimension \(2+2=4\). Over \(\mathbb F_q\) its cardinality is \((q^2-1)q^2\).

**Step 3: closed stratum and its count.** Setting \(a=e=0\) in Step 1 first gives \(b^2=v^2\), hence \(v=b\) in every field of characteristic two. The remaining equations are exactly
\[
cu=b^2,\qquad cw=bd,\qquad bw=ud.
\]
The triples \((b,c,u)\) satisfying \(cu=b^2\) number \(q^2\): for \(c\ne0\), choose \(b\) freely and solve for \(u\); for \(c=0\), necessarily \(b=0\), with \(u\) free. When \((b,c,u)\ne(0,0,0)\), the two remaining equations specify the kernel of a rank-one two-by-two matrix, hence admit exactly \(q\) choices of \((d,w)\). When this triple is zero, the kernel has \(q^2\) choices. Therefore the zero-constant count is
\[
(q^2-1)q+q^2=q^3+q^2-q.
\]
Adding Step 2 gives the stated polynomial.

**Step 4: no hidden components.** On the closed stratum the degree-one coefficient matrix is
\[
L=\begin{pmatrix}b&c\\u&b\end{pmatrix},\qquad L^2=0.
\]
If \(L\ne0\), linear coordinates reduce it to the usual rank-one nilpotent Jordan block. The equations then put the derivation in the form \(D=(c y+dxy)\partial_x\) with \(c\ne0\). Such a derivation is the limit, as \(t\to0\), of square-zero derivations
\[
D_t=(t+cy+dxy)\partial_x+
\left(\frac{td}{c}y+\frac{td^2}{c^2}xy\right)\partial_y,
\]
whose constant vector is nonzero when \(t\ne0\). If \(L=0\), then \(D=(dxy)\partial_x+(wxy)\partial_y\). A linear coordinate change sends any nonzero vector \((d,w)\) to \((d',0)\). That derivation is the limit of the square-zero derivations \((t y+d'xy)\partial_x\), which have nonzero \(L\) for \(t\ne0\) and hence belong to the closure just established. The zero derivation belongs to the closure by scaling. Thus **every** point of the closed stratum belongs to the closure of the irreducible open stratum. The reduced cone is irreducible of dimension four; its dense rational open subset proves rationality.

## Verification

A standalone program, `verify.py`, independently constructs derivation action matrices on \(1,x,y,xy\), squares those matrices, and checks agreement with the eight displayed equations for every element of \(W\) over \(\mathbb F_2\) and \(\mathbb F_4\). It also exhaustively checks the point counts \(22\) and \(316\), respectively, and the open/closed stratum counts. The proof above is uniform in the characteristic-two field and does not infer an infinite theorem from finite experiments.

## Relationship to prior work

Premet's 1992 theorem describes invariant theory and nilpotent varieties for general Cartan-type Witt algebras under the explicit assumption that characteristic exceeds two. It therefore does **not** imply the characteristic-two assertion proved here. Yao and Chang's 2013 investigation treats nilpotent commuting varieties of the **one-variable** Witt algebra in characteristic greater than three, so neither its objects nor its field range include this eight-dimensional rank-two example. The present result concerns the single-derivation height-one \(p\)-nilpotent cone in characteristic two, **not** the nilpotent commuting-pair variety. Existing general results about equidimensionality are not sufficient to give the explicit geometric irreducibility and arithmetic fiber formula. Earlier unlocated specialized work on small-characteristic Cartan-type Lie algebras may implicitly cover this particular example.

## Limitations

The assertion is restricted to characteristic two and the algebra with exactly two truncated generators of square zero. It concerns the reduced \(D^{[2]}=0\) locus; it does not determine the nonreduced scheme structure or the full nilpotent variety \(D^{[2]^s}=0\) for unspecified larger \(s\). The finite-field counts are exact; the geometric argument uses algebraic closure. Historical-priority search was targeted rather than exhaustive, and no independent mathematical audit has been performed.

## References

- A. A. Premet, “The theorem on restriction of invariants, and nilpotent elements in \(W_n\),” *Mathematics of the USSR-Sbornik* **73** (1992), 135–159. DOI: 10.1070/SM1992v073n01ABEH002538. Abstract states the assumption \(p>2\).
- Yu-Feng Yao and Hao Chang, “Nilpotent commuting varieties of the Witt algebra,” arXiv:1301.5667v1 (23 January 2013), subsequently *Journal of Pure and Applied Algebra* (2014). Full open text treats one-variable Witt algebras in characteristic \(p>3\).
