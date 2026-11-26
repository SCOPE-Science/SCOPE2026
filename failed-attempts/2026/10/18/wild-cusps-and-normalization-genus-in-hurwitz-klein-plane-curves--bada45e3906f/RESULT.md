# Wild cusps and normalization genus in Hurwitz–Klein plane curves

## Finding
Let \(k\) be algebraically closed of prime characteristic \(p>0\), and let \(n\ge2\). Put
\[
 m=n^2-n+1,\qquad C_n=V(x^ny+y^nz+z^nx)\subset\mathbb P^2_k.
\]
Then \(C_n\) is geometrically integral. If \(p\nmid m\), it is nonsingular with genus \((m-1)/2\). If \(p\mid m\), let \(q=p^{v_p(m)}\) and \(r=m/q\). Then:

1. There are exactly \(r\) geometric singular points, all in the coordinate torus. On \(y=1\), they are precisely
\[
 [u:1:v],\qquad u=-\frac{1}{nv^{n-1}},\qquad v^m=(-1)^n n^{2-n}.
\]
2. Each is unibranch of multiplicity two, formally equivalent to \(U^2-V^q=0\), with local value semigroup \(\langle2,q\rangle\) and \(\delta=(q-1)/2\).
3. The normalization has function field \(k(\tau,v)\) defined by
\[
 v^r=(-1)^n\frac{(1+\tau)^n}{\tau}.
\]
For \(r>1\), its map to the \(\tau\)-line is a tame cyclic degree-\(r\) cover, totally ramified at the three points \(0,-1,\infty\) and unramified elsewhere. Thus the geometric normalization genus is
\[
 g(\widetilde C_n)=\frac{r-1}{2}.
\]
When \(r=1\), the displayed function field is rational, and the same formula gives genus zero.

Consequently the singularity contribution to the arithmetic genus is exactly \(r(q-1)/2\). For example, the Klein quartic plane equation with \(n=3\) in characteristic seven is rational with one multiplicity-two cusp of delta three; with \(n=5\) in characteristic seven, the degree-six model has three such cusps and normalization genus one.

## Assumptions and scope
All geometric claims concern the indicated reduced plane curve over an algebraically closed field in characteristic \(p>0\). No claim concerns stable models or potential good reduction of its characteristic-zero counterpart. In the exceptional case \(p\mid m\), the integer \(m\) is odd, hence \(p\ne2\), and the congruences \(m\equiv1\pmod n\) and \(m\equiv1\pmod{n-1}\) imply \(p\nmid n(n-1)\). The plane curve has degree \(n+1\), with arithmetic genus \(n(n-1)/2=(m-1)/2\).

## Proof
**Integral function-field model.** No coordinate variable divides \(x^ny+y^nz+z^nx\), so every irreducible component meets the torus \(xyz\ne0\). Set \(u=x/y\), \(v=z/y\) and \(t=u^n/v\) there. The defining equation becomes \(u^n+v+uv^n=0\), equivalent to \(uv^{n-1}=-(1+t)\). Eliminating \(u\) yields
\[
 v^m=(-1)^n\frac{(1+t)^n}{t}=:R(t),\qquad u=-\frac{1+t}{v^{n-1}}.
\]
At \(t=0\), the rational function \(R(t)\) has valuation \(-1\). A root of \(T^m-R(t)\) therefore has valuation \(-1/m\), forcing its extension degree over \(k(t)\) to be divisible by \(m\). Since the polynomial has degree \(m\), it is irreducible. The birational inverse above proves geometric integrality of \(C_n\) and identifies its function field with \(k(t,v)\).

**Complete singular-locus equations.** The only points with a zero coordinate are \([1:0:0]\), \([0:1:0]\), and \([0:0:1]\), and each is smooth because at least one partial derivative of the homogeneous polynomial equals one at that point. On \(y=1\), put \(f(u,v)=u^n+v+uv^n\). Its partial derivatives are
\[
 f_u=nu^{n-1}+v^n,\qquad f_v=1+nuv^{n-1}.
\]
If \(p\mid n\), then \(f_v=1\); otherwise at a critical point \(v\ne0\) and \(u=-1/(nv^{n-1})\). Substituting into \(f_u=0\) gives \(v^m=(-1)^n n^{2-n}\). The same two critical equations give \(u^n=v/n^2\) and \(uv^n=-v/n\); hence \(f(u,v)=mv/n^2\). Thus points on \(C_n\) are singular precisely when \(p\mid m\) and the displayed equations hold. If \(p\mid m\), \(m=qr\), and \(T^m-c=(T^r-c^{1/q})^q\) has exactly \(r\) distinct nonzero geometric roots because \(p\nmid r\). In particular there are no omitted singular points and \(C_n\) is smooth whenever \(p\nmid m\).

**Normalization and geometric genus.** Suppose \(p\mid m\), and write \(m=qr\), \(q=p^e\), \(p\nmid r\). The rational function \(R(t)=(-1)^n(1+t)^n/t\) has valuation \(-1\) at zero, hence is not a \(p\)-th power in \(k(t)\). The purely inseparable degree-\(q\) subextension \(k(t,v^r)\) is therefore \(k(t^{1/q})\). Indeed, with \(\tau=t^{1/q}\), the Frobenius identity over the perfect field \(k\) gives
\[
 v^r=R(t)^{1/q}=(-1)^n\frac{(1+\tau)^n}{\tau}.
\]
As \(m\equiv1\) modulo both \(n\) and \(n-1\), \(r\) is coprime to \(n(n-1)\). Thus the function on the right has valuation \(-1,n,1-n\) at \(0,-1,\infty\), respectively; all three are coprime to \(r\). If \(r>1\), Kummer theory shows that the extension of \(k(\tau)\) is separable, cyclic of degree \(r\), and totally and tamely ramified over exactly these three points. Riemann–Hurwitz gives \(2g-2=-2r+3(r-1)=r-3\), hence \(g=(r-1)/2\). If \(r=1\), the normalization has field \(k(\tau)\), so \(g=0\).

**Single branches and cusp types.** Each singular point has \(u,v\ne0\), so \(t=u^n/v\) is finite and nonzero there. From \(uv^{n-1}=-(1+t)\), also \(t\ne-1\). The normalization model above has a unique preimage for the given \(t\) and \(v\): in characteristic \(p\), the root \(\tau=t^{1/q}\) is unique, while the chosen \(v\) fixes a point of the tame affine Kummer curve. Since that curve is smooth whenever \(\tau\notin\{0,-1,\infty\}\) and \(v\ne0\), the plane singularity has precisely one analytic branch.

At any singular point, \(f_{uu}=n(n-1)u^{n-2}\ne0\). As \(p\ne2\), the formal Weierstrass preparation and completion-of-square argument puts the completed plane local equation in the form \(U^2-h(V)=0\). Unibranchedness forces the order \(s=\operatorname{ord}_V h\) to be odd: if it were even, algebraic closure and invertibility of two would make \(h\) a square in \(k[[V]]\), giving two branches. For odd \(s\), \(U^2-h(V)\) has semigroup \(\langle2,s\rangle\) and delta invariant \((s-1)/2\); the unit factor in \(h(V)=V^s\cdot\text{unit}\) can be removed by a square root, so the completed germ is equivalent to \(U^2-V^s\).

The group \(\mu_r\) acts on the plane model by \((u,v)\mapsto(\zeta^{-(n-1)}u,\zeta v)\) for \(\zeta^r=1\), because \(r\mid m\). It permutes the \(r\) singular points transitively, hence their delta invariants are equal. The genus–delta formula and the already established normalization genus give
\[
 \sum_P\delta_P=\frac{m-1}{2}-\frac{r-1}{2}=\frac{r(q-1)}{2}.
\]
Therefore \(\delta_P=(q-1)/2\) and \(s=q\) at every singular point, yielding the stated formal equation, multiplicity, and semigroup. This completes the classification.

## Verification
The accompanying self-contained Python program `verify_hurwitz.py` directly enumerates all \(\mathbb F_p\)-rational projective points for \(2\le n\le16\), for all primes \(p\le29\), and compares the Jacobian singularities with the exact parameter formula. It checks 150 characteristic/degree pairs, including both smooth and exceptional cases, and prints `VERIFY_OK`. For instance, at \((n,p)=(3,7)\) it finds one rational singular point; at \((5,7)\) it finds three. These finite-field tests validate the computational identities but cannot establish the geometric branch count, arbitrary-characteristic theorem, or infinite-family novelty; those rely on the proof above.

Run with `python3 verify_hurwitz.py` (Python standard library only).

## Relationship to prior work
Aguglia–Korchmáros–Torres (2001) study nonsingular plane Hurwitz curves, explicitly assuming \(p\nmid n^2-n+1\) for the same equation (their Introduction, equation (1.2)). Badr–Bars (2015, arXiv:1510.06192v1) classify automorphism-rich *nonsingular* plane Klein-type curves in characteristic zero, including the cyclic trinomial family. Elkies (1998) describes arithmetic and characteristic-seven models of the classical Klein quartic and explains distinctions between plane reductions and potentially good reductions. Our statement concerns the singular reduction of the specified plane trinomial when the excluded characteristic divides \(m\), and classifies its normalization genus and all local cusp types in every such characteristic. The familiar special case of the Klein quartic in characteristic seven does not, by itself, supply the all-parameter statement. Broader equivalence via existing binomial-cover or trinomial-curve techniques is a residual literature risk.

## Limitations
This is an exact claim about the indicated plane model and its geometric normalization, not a stable-model result. The classifier does not determine arithmetic fields of definition of every cusp beyond the displayed defining equation; the count \(r\) is over an algebraically closed field. Positive-characteristic analytic equivalence refers to completed local rings. Computational checks cover only finite prime fields and selected dimensions. The accessible literature comparisons do not prove uniqueness; differently formulated prior derivations of the same result might exist. No independent mathematical audit has been performed.

## References
1. A. Aguglia, G. Korchmáros, F. Torres, *Plane maximal curves*, Acta Arithmetica **98** (2001), 165–179. Full text: https://www.impan.pl/shop/en/publication/transaction/download/product/83712.
2. E. Badr, F. Bars, *Plane non-singular curves with an element of “large” order in its automorphism group*, arXiv:1510.06192v1 (first posted 2015-10-21). https://arxiv.org/abs/1510.06192.
3. N. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way*, MSRI Publications **35** (1998), 51–101. Full text: https://library.slmath.org/books/Book35/files/elkies.pdf.
4. D. Bisogno et al., *The Supersingularity of Hurwitz Curves*, arXiv:1810.01582 (2018), compared as later related work. https://arxiv.org/abs/1810.01582.
