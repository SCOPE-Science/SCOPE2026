# A uniform genus-four curve of gonality four over every finite field

## Finding

**Theorem.** For every prime power \(q\), there exists a smooth, projective, geometrically integral genus-four curve \(C/\mathbb F_q\) with an \(\mathbb F_q\)-rational point and \(\mathbb F_q\)-gonality exactly \(4\). A uniform construction uses the nonsplit quadratic twist of \(\mathbb P^1\times\mathbb P^1\) and one of two integer-coefficient symmetric curves of bidegree \((3,3)\). This gives an affirmative answer for genus four to Question 1.3 of Faber--Grantham--Howe [1], including characteristic two.

## Assumptions and scope

The \(k\)-gonality of a curve is the minimum degree of a nonconstant \(k\)-morphism to \(\mathbb P^1_k\); it is not the gonality over the algebraic closure. Let \(q\) range over **all prime powers**, put \(k=\mathbb F_q\), \(K=\mathbb F_{q^2}\), and let \(\sigma\) be the nontrivial element of \(\operatorname{Gal}(K/k)\). Fix the affine coordinates \(u=U_0/U_1\), \(v=V_0/V_1\) on \(\mathbb P^1\times\mathbb P^1\). Define

\[
\begin{aligned}
f_A(u,v)&=u^3v^3+u^3+v^3+u+v,\\
f_B(u,v)&=f_A(u,v)+u^2+v^2.
\end{aligned}
\]

Write \(D_A,D_B\) for their **bihomogenized bidegree-\((3,3)\) divisors** on \(\mathbb P^1\times\mathbb P^1\) over \(\mathbb Z\). In particular, \(f_A,f_B\) are symmetric under \((u,v)\leftrightarrow(v,u)\), and each has the simple point \((0,0)\). All statements concern the smooth projective curves obtained by descent, not merely affine equations.

## Proof

**1. At least one smooth divisor in each characteristic.** For \(f\in\{f_A,f_B\}\), form the integer

\[
R(f)=\operatorname{Res}_{u}\!\bigl(\operatorname{Res}_{v}(f,f_u),\operatorname{Res}_{v}(f,f_v)\bigr).
\]

A common affine zero of \(f,f_u,f_v\) over an algebraic closure of characteristic \(p\) forces \(R(f)\equiv0\pmod p\). Exact integer polynomial arithmetic (reproducible by `verify_resultants.py`) gives

\[
\begin{aligned}
R(f_A)&=982087492035469593396623616,\\
R(f_B)&=5838078345771419602547015726577988403024765030400,\\
\gcd(R(f_A),R(f_B))&=338688=2^8\cdot3^3\cdot7^2.
\end{aligned}
\]

Thus, for every prime \(p\notin\{2,3,7\}\), **at least one** of \(D_A,D_B\) has no affine singularity. For the three exceptional primes, exact reduced Gröbner bases of the ideals \((f,(f)_u,(f)_v)\subset\mathbb F_p[u,v]\) are the unit ideal: use \(f_B\) for \(p=2,3\), and \(f_A\) for \(p=7\). These assertions are separately checked by the same program, using the Gröbner basis \([1]\) in each case. No enumeration over a finite extension is used as an infinite-field smoothness argument.

Now check the boundary. In the chart \(t=1/u\) with \(v\) finite, the local equations are respectively

\[
\begin{aligned}
t^3f_A(1/t,v)&=v^3+1+t^2+t^3(v^3+v),\\
t^3f_B(1/t,v)&=v^3+1+t+t^2+t^3(v^3+v^2+v).
\end{aligned}
\]

At \(t=0\), any point has \(v^3=-1\), in particular \(v\ne0\). When \(p\ne3\), the derivative in \(v\) is \(3v^2\ne0\). In characteristic three the selected equation is \(f_B\), whose derivative in \(t\) is \(1\) at \(t=0\). The other boundary is symmetric. At \((u,v)=(\infty,\infty)\), the bihomogeneous equation evaluates to its leading coefficient \(1\), so the corner does not lie on either divisor. Hence the selected divisor \(D\) is everywhere smooth over an algebraic closure in *every* characteristic. The boundary and marked-point identities are independently checked in `verify_boundary.py`.

**2. Genus and canonical model.** A smooth effective divisor of bidegree \((3,3)\) on \(\mathbb P^1\times\mathbb P^1\) is geometrically connected (it is ample); smooth connected implies geometrically integral. Adjunction gives

\[
K_D\cong\mathcal O_D(1,1),\qquad g(D)=(3-1)(3-1)=4.
\]

The Segre embedding defined by \(\mathcal O(1,1)\) restricts to the complete canonical embedding of \(D\) in \(\mathbb P^3\): both the ambient sections and \(H^0(D,K_D)\) have dimension four. Its unique containing quadric is the smooth Segre quadric. (Equivalently, the canonical curve is the intersection of this quadric with a cubic.)

**3. Nonsplit descent and a rational point.** Start with \(D_K\subset\mathbb P^1_K\times\mathbb P^1_K\). Descend via the semilinear involution obtained by composing coefficient Frobenius \(\sigma\) with exchange of the factors. Because all coefficients lie in \(\mathbb F_p\) and \(f\) is symmetric, this descent datum stabilizes \(D_K\). It gives a smooth geometrically integral curve \(C/k\) on the nonsplit smooth quadric \(Q/k\) that becomes \(\mathbb P^1\times\mathbb P^1\) over \(K\). The point \((u,v)=(0,0)\) is fixed by the descent datum and is smooth (both first partial derivatives are \(1\)), so it descends to \(P\in C(k)\).

**4. Gonality.** Over an algebraic closure the two degree-three pencils of this canonical genus-four curve are precisely the two projections along the rulings of its **unique** containing smooth quadric. This is the standard canonical-curve description of genus-four trigonal pencils: a \(g^1_3\) sweeps out a rational normal scroll of degree two, necessarily the containing quadric. The two ruling classes are interchanged by the chosen \(k\)-Frobenius descent. No degree-three pencil can therefore be defined over \(k\). As the curve is canonically embedded, it is nonhyperelliptic and has no degree-one or degree-two map. Hence \(\operatorname{gon}_k(C)\ge4\).

Conversely, since \(P\in C(k)\), Riemann--Roch for the \(k\)-rational divisor \(K_C-2P\) of degree four gives

\[
h^0(K_C-2P)=1+h^0(2P)\ge2.
\]

Taking two independent \(k\)-sections and removing any common base divisor yields a \(k\)-morphism to \(\mathbb P^1\) of degree at most four. Therefore \(\operatorname{gon}_k(C)=4\) as claimed. \(\square\)

## Verification

Run `python verify_resultants.py` and `python verify_boundary.py` from the same directory; SymPy is the only nonstandard Python dependency. The first program reconstructs both nested integer resultants and their gcd, plus the three exceptional characteristic Gröbner certificates; the second reconstructs both boundary charts, the factor-swap invariance, and the smooth marked point. Both were run successfully on the exact attached programs. The standard genus/canonical-scroll/descent and Riemann--Roch arguments are mathematical proofs, not experimental extrapolations.

## Relationship to prior work

Faber, Grantham, and Howe [1, Question 1.3] explicitly ask for a curve of genus \(g\) and gonality \(g\) over each finite field. For \(g=4\), they report small fields and propose finding a suitable cubic section of a nonsplit quadric over odd fields; they do not give a uniform explicit solution. The present symmetric bidegree-\((3,3)\) equations, integral resultant certificate, and characteristic-two-compatible descent supply that missing uniform construction. The geometry of the two genus-four trigonal rulings is classical, not claimed as new. Xarles's finite-field census [2] addresses \(\mathbb F_2\) alone; Looijenga [3] concerns geometric moduli and related trigonal curves rather than this all-finite-field existence statement.

## Limitations

The theorem asserts existence of at least one pointed curve of \(k\)-gonality four for each finite field, not classification of all genus-four curves or their point-count maxima. The coefficient selection depends on the field characteristic. The Frobenius-swapped quadric mechanism is a known geometric construction; the claimed new part is the **explicit uniform smooth existence proof** resolving the stated genus-four instance. Priority against an unindexed equivalent construction cannot be independently certified, and no independent mathematical audit has been performed.

## References

[1] X. Faber, J. Grantham, E. W. Howe, *On the Maximum Gonality of a Curve over a Finite Field*, arXiv:2207.14307, first public 2022-07-28, especially Question 1.3 and the genus-four construction discussion. https://arxiv.org/html/2207.14307v2

[2] X. Xarles, *A census of all genus 4 curves over the field with 2 elements*, arXiv:2007.07822. https://arxiv.org/abs/2007.07822

[3] E. Looijenga, *A ball quotient parametrizing trigonal genus 4 curves*, arXiv:2211.09941. https://arxiv.org/abs/2211.09941
