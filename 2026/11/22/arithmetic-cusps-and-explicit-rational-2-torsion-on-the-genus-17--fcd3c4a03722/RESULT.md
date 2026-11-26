# Arithmetic cusp fields and an explicit two-torsion divisor for the genus-1777 modular cover

## Finding

Let \(N=4800\), \(H=\{d\in(\mathbb Z/N\mathbb Z)^\times:d\equiv\pm1\pmod5\}\), \(Y=X_0(N)\) and \(X=X_H(N)=X_1(N)/H\) over \(\mathbb Q\). Let \(\nu:Y\to X_0(5)\) forget to the order-five subgroup, and on \(X_0(5)\) let
\[
t=\left(\eta(z)/\eta(5z)\right)^6,\qquad Q(t)=t^2+22t+125.
\]
The canonical double cover has function field \(\mathbb Q(Y)(w)\), where \(w^2=5Q(t)\) and \(t\) denotes the pullback. It is geometrically connected and étale. The constant factor matters: \(w^2=Q(t)\) defines a different rational cover, even though both covers have the same complex curve and the same cusp-degree histogram.

For \(d\mid N\), the closed cusp of \(Y\) of denominator \(d\) has field \(K_d=\mathbb Q(\zeta_{\gcd(d,N/d)})\). Its fiber on the canonical \(X\) consists of two closed cusps of field \(K_d\) when \(v_5(d)=0,1\), and one closed cusp of field \(K_d(\sqrt5)\) when \(v_5(d)=2\). In particular \(d=1\) has two rational lifts, whereas \(d=25\) has one quadratic lift. In residue degrees \(1,2,4,8,16\), the numbers are respectively \(16,16,24,10,4\) (70 closed and 288 geometric cusps).

Let \(D\) be the reduced inverse image on \(Y\) of the two zeros of \(Q\) on \(X_0(5)\), and \(B=\nu^*(\infty)\). Each has degree 1920 and \(D\) has 1920 distinct geometric points. On \(Y\), \(\operatorname{div}(5Q(t))=2D-2B\). The class \([D-B]\) is nonzero rational two-torsion in \(\operatorname{Jac}(Y)\); the double-cover algebra is obtained from this line bundle using the trivialization given by the canonical radicand (up to the convention of taking its inverse).

## Proof

**Canonical normalization.** Away from the cusps an \(H\)-structure on a cyclic subgroup of order \(N\) is a generator of its order-five subgroup up to sign. In fact multiplication by \(N/5\) sends generators of the order-\(N\) subgroup to generators at level five, and the subgroup of changes of generator preserving the latter up to sign is exactly \(H\). This description works over \(\mathbb Q\) and identifies the function-field cover with the pullback from the standard \(X_1(5)\) of a point of order five.

One can compute the rational twist directly using the Tate normal form for this marked point, with rational parameter \(b\):
\[
E_b:\quad y^2+(1-b)xy-by=x^3-bx^2,\qquad P=(0,0).
\]
Indeed for a point of order five, move the point to the origin and its tangent to \(y=0\); then \(a_4=a_6=0\). Since the point has neither order two nor three, \(a_3\ne0\) and \(a_2\ne0\), so a unique scaling makes \(a_2=a_3=-b\). If \(a_1=1-c\) at this step, the doubling tangent gives \(2P=(b,bc)\), and the line through \(P,2P\) has third intersection at abscissa \(c\) (its three abscissas are \(0,b,c\)). Thus \(3P=-2P\) is equivalent to \(c=b\), with the tangent interpretation when the intersection is repeated. This gives the parameter of the ordinary marked-point curve over \(\mathbb Q\).

Set \(k=b-11-1/b\). The invariants of \(E_b\) satisfy
\[
c_4=b^2(k^2+10k+5),\qquad \Delta=b^6 k,\qquad j(E_b)=(k^2+10k+5)^3/k.
\]
Thus the \(j\)-poles at \(b=0,\infty\) have order five and those at the two zeros of \(k\) have order one. On \(X_0(5)\) the formula \(j=(t^2+250t+3125)^3/t^5\) gives pole orders five at \(t=0\) and one at \(t=\infty\). In the degree-two forgetful map the poles of order five therefore lie over \(t=0\), the simple poles over \(t=\infty\); all four are unramified. Thus the pulled-back \(t\) is a constant times \(1/k\). Comparing the leading terms \(j\sim t\) and \(j\sim125/k\) at \(k=0\) gives \(t=125/k\). Since \(b-1/b=k+11\), the element \(w=(t/5)(b+1/b)\) generates the level-five quadratic extension and satisfies
\[
w^2=(t/5)^2\big((125/t+11)^2+4\big)=5Q(t).
\]
In particular the standard marked-point model is not normalized by just requiring rational coefficients in an analytic \(q\)-series at infinity. Its infinity cusp is the marked Tate point \(\zeta_5\) up to sign, of field \(\mathbb Q(\sqrt5)\).

**Divisors and étaleness.** The character on \(\Gamma_0(4800)\) given by the bottom-right entry modulo five and modulo sign is surjective (for example take a matrix with bottom row \((4800,7)\) and top-left entry 2743; the determinant can be made one), so the pulled-back cover is geometrically connected. The level-five \(j\)-formula gives
\[
(t^2+250t+3125)^3-1728t^5=(t^2-500t-15625)^2Q(t).
\]
The two simple preimages of \(1728\) are the two order-two elliptic points. Since \(4\mid N\), \(Y\) has no order-two elliptic points, so \(\nu\) has ramification index two at each point above them. The index formula gives \(\deg \nu=(4800(1+1/2)(1+1/3)(1+1/5))/6=1920\), hence 960 geometric points over each zero. The pole of \(Q(t)\) on \(X_0(5)\) is twice \(\infty\). Therefore the divisor on \(Y\) is \(2D-2B\) and every order is even, proving étaleness in characteristic zero. If \(D-B\) were principal over \(\overline{\mathbb Q}\), the radicand would be a square there, contradicting geometric connectedness. Both divisors are rational, which proves the stated rational two-torsion.

**Cusp fibers.** The level-five image of denominator \(d\) is \(t=0\) for \(5\nmid d\), and \(t=\infty\) otherwise. At zero the residual equation is \(w^2=625\), which splits. At infinity divide \(w\) by \(t\) to obtain the residual equation \((w/t)^2=5\). For \(v_5(d)=1\), \(5\mid\gcd(d,N/d)\), so \(K_d\) contains \(\mathbb Q(\sqrt5)\); for \(v_5(d)=2\) the gcd is a power of two and its cyclotomic field cannot contain the quadratic field of discriminant five. The residual equations are separable and describe the entire étale fiber. For \(v_5(d)=0,2\) the base degree histogram is \((8,4,2)\) in degrees \((1,2,4)\); for \(v_5(d)=1\) it is \((8,4,2)\) in degrees \((4,8,16)\). Doubling the number of cusps in the first and middle strata and doubling the degrees in the last yields the claimed table. The noncanonical twist exchanges the splitting in the outside strata, which explains why the aggregate is unchanged.

## Context and reproducibility

R. Auffarth, [*A completely decomposable modular Jacobian of dimension 1777*](https://arxiv.org/html/2611.16963v1), §2, supplies the standard model, the étale covering structure and the geometric cusp count. B. Cais and B. Conrad, [*Modular curves and Ramanujan's continued fraction*](https://virtualmath1.stanford.edu/~conrad/papers/J5final.pdf), §§2–5, give the Tate-cusp descriptions and a twisted level-five model; rational \(q\)-coefficients on that model do not fix the rational descent for the ordinary \(X_1(5)\) quotient. The concrete normalization above locates the cusp fields on the named canonical model rather than just determining an aggregate count on a complex curve. The argument specifies an actual divisor representing the cover line bundle, not the full torsion of the Jacobian or the full set of rational points.

Run `python3 check_modular_cusps.py` with SymPy to check the invariant calculations, the polynomial identities, the local residual constants, the degree and the per-denominator arithmetic enumeration. The modular interpretation of the standard model, the divisor description and nontriviality are proved above, not inferred from the finite program.
