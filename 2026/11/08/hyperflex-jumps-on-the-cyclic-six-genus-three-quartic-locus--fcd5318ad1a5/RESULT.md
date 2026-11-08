# Hyperflex jumps on the cyclic-six genus-three quartic locus

## Finding

For every \(r\in\mathbb C\setminus\{-2,2\}\), let \(C_r\subset\mathbb P^2_{\mathbb C}\) be the smooth plane quartic
\[
C_r:\quad X^3Z+Y^4+rY^2Z^2+Z^4=0.
\]
Write \(h(r)\) and \(o(r)\) for the numbers of distinct geometric hyperflexes (tangent contact order four) and ordinary flexes (contact order three), respectively. Set
\[
f(r)=11r^4-1080r^2+3888.
\]
Then the **complete flex-type distribution** in this one-parameter family is
\[
\boxed{
(h(r),o(r))=\begin{cases}
(4,16),&r=0,\\
(7,10),&f(r)=0,\\
(1,22),&\text{otherwise}.
\end{cases}}
\]
The exceptional equation \(f(r)=0\) has four distinct, nonsingular parameters. Up to complex isomorphism these determine exactly **two** curves with seven hyperflexes in the locus whose full automorphism group is cyclic of order six, with parameter invariant
\[
\boxed{r^2=\frac{540+288\sqrt3}{11}\quad\text{or}\quad r^2=\frac{540-288\sqrt3}{11}.}
\]
At either seven-hyperflex parameter the six hyperflexes away from \([1:0:0]\) form a single orbit under the natural order-six automorphism.

## Assumptions and scope

All geometric points and counts are over \(\mathbb C\), hence in characteristic zero. A flex is a point on a smooth plane quartic whose unique tangent intersects the curve with multiplicity at least three at that point. Ordinary means multiplicity exactly three; hyperflex means exactly four. The quartic \(C_r\) is smooth precisely when \(r\ne\pm2\): at infinity \([1:0:0]\) the derivative with respect to \(Z\) is nonzero, and in the affine chart \(Z=1\) simultaneous vanishing of the partials forces \(X=0\) and a common root of \(Y^4+rY^2+1\) and its derivative, occurring only for \(r=\pm2\).

## Proof

**The point at infinity and four ordinary flexes.** The only point of \(C_r\) on \(Z=0\) is \(P_\infty=[1:0:0]\). Its tangent \(Z=0\) cuts \(C_r\) in \(Y^4=0\), so it is a hyperflex for every smooth parameter. In the affine chart \(Z=1\), put \(g(Y)=Y^4+rY^2+1\), so \(X^3=-g(Y)\). For \(r\ne\pm2\), the four roots of \(g\) are distinct. At each point with \(X=0\) the tangent is \(Y=y_0\), and its restriction has equation \(X^3=0\). These are four *ordinary* flexes, never hyperflexes.

**Hyperflex condition away from \(X=0\).** At an affine point \((x,y)\) with \(x\ne0\), parametrize the tangent as \((X,Y)=(x+mu,y+u)\), with
\[
m=-\frac{4y^3+2ry}{3x^2}.
\]
The restriction of the defining equation to this line has vanishing constant and linear terms and is
\[
\left(3xm^2+6y^2+r\right)u^2+
\left(m^3+4y\right)u^3+u^4.
\]
Thus the point is a hyperflex exactly when both displayed parenthesized coefficients vanish.

When \(y=0\), one has \(m=0\); the quadratic coefficient is \(r\). Hence precisely at \(r=0\) there are three additional hyperflexes, given by \(y=0\), \(x^3=-1\). These are distinct from \(P_\infty\).

For \(y\ne0\), put \(t=y^2\) and \(G=t^2+rt+1=-x^3\), which is nonzero. Substituting the expression for \(m\) and clearing nonzero denominators shows that the two contact coefficients vanish if and only if
\[
\begin{aligned}
A(t,r)&=4t(2t+r)^2-3(t^2+rt+1)(6t+r)=0,\\
B(t,r)&=2t(2t+r)^3-27(t^2+rt+1)^2=0.
\end{aligned}
\]
An exact resultant calculation yields
\[
\operatorname{Res}_t(A,B)=324(r-2)^3(r+2)^3\left(11r^4-1080r^2+3888\right).
\]
Because \(r=\pm2\) is excluded, any further hyperflex requires \(f(r)=0\).

**Every exceptional root gives exactly six new hyperflexes.** An exact Gröbner-basis computation over \(\mathbb Q\) gives
\[
\operatorname{GB}_{t>r}(A,B,f)
=\left(864t-11r^3+972r,\;f(r)\right).
\]
Consequently, at every root of \(f\), the simultaneous equations have the unique solution
\[
t=\frac{r(11r^2-972)}{864}.
\]
Direct substitution verifies \(A=B=0\). Polynomial gcd calculations verify that \(f\) is squarefree, none of its roots belongs to \(\{0,-2,2\}\), and the displayed \(t\) is nonzero at every root. Moreover \(G\equiv(r^2+12)/12\pmod{f}\), with \(\gcd(f,r^2+12)=1\), so \(G\ne0\). Thus \(y^2=t\) gives two distinct nonzero values of \(y\) and \(x^3=-G\) gives three distinct values of \(x\) for each, yielding exactly six affine hyperflexes. The automorphism \((X:Y:Z)\mapsto(\zeta_3X:-Y:Z)\) acts transitively on them. There are no additional hyperflexes by the exhaustive case split.

**Isomorphism classes and ordinary flexes.** Solving \(f(r)=0\) in \(r^2\) gives \(r^2=(540\pm288\sqrt3)/11\), two distinct values. For this family, \(C_r\cong C_{r'}\) over \(\mathbb C\) if and only if \(r^2={r'}^2\), as established by Lercier–Ritzenthaler–Rovetta–Sijsling and by Ohashi–Kudo–Harashita. The same latter work proves that the full automorphism group is cyclic of order six when \(r\notin\{0,\pm2\}\); therefore exactly two cyclic-six isomorphism classes possess seven hyperflexes. Finally, a smooth plane quartic in characteristic zero has total inflection weight \(24\); an ordinary flex contributes weight one and a hyperflex weight two. Therefore \(o(r)=24-2h(r)\), proving the full distribution.

## Verification

Run `python3 verify_hyperflex.py` with Python 3 and SymPy (version 1.10 or later). It recomputes tangent-contact coefficients, the resultant factorization, the Gröbner basis and the substitution and gcd certificates, along with the affine branch discriminant and the hyperflex at infinity. Successful completion prints `VERIFY_HYPERFLEX_OK`. These are symbolic checks over the rationals; the finite number of computations is sufficient here because the proof reduces the entire parameter family to the explicit polynomial identities above.

## Relationship to prior work

Lercier–Ritzenthaler–Rovetta–Sijsling provide the cyclic-six plane-quartic normal form and classify its isomorphism parameter. Ohashi–Kudo–Harashita prove smoothness and automorphism criteria and study the Hasse–Witt matrix and \(a\)-numbers of this family; their preprint first appeared on November 18, 2021. Those normal-form and automorphism statements are used as established inputs, not claimed here. Girard–Kohel's earlier modular classification of quartics with at least seven hyperflexes gives a broader general stratum, including the one-dimensional seven-hyperflex locus, but does not explicitly determine its intersection with this cyclic-six family by \(f(r)\), or the full \(1,4,7\) jump formula. The new contribution is that explicit arithmetic-algebraic intersection and full flex count within the family.

## Limitations

The theorem is over characteristic zero; in small positive characteristics Hessian/flex counting and the elimination polynomial can behave differently. It does not classify hyperflexes on all plane quartics, recover the full Girard–Kohel modular equations, or assert independent external verification. General earlier moduli equations might allow these specializations to be recovered through additional elimination, creating residual historical-priority uncertainty.

## References

1. R. Ohashi, M. Kudo, S. Harashita, *The \(a\)-numbers of non-hyperelliptic curves of genus three with cyclic automorphism group of order six*, arXiv:2111.09777 (first public version, November 18, 2021), particularly Theorem A and §2.1. https://arxiv.org/abs/2111.09777
2. R. Lercier, C. Ritzenthaler, F. Rovetta, J. Sijsling, *Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields*, arXiv:1403.0562 (2014), particularly Theorems 3.1 and 3.3. https://arxiv.org/abs/1403.0562
3. M. Girard, D. R. Kohel, *Classification of genus 3 curves in special strata of the moduli space*, arXiv:math/0603555 (2006), particularly §§2, 4–6 and the seven-hyperflex stratum \(Z_4\). https://arxiv.org/abs/math/0603555
