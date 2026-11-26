# Dual class, inflection divisor, and projective boundary of generic Lissajous curves

## Finding

Fix coprime integers \(1\le m<n\) and a complex number \(c\in\mathbb C^*\) transcendental over \(\mathbb Q\). Let \(C_{m,n,c}\subset\mathbb P^2_{\mathbb C}\) be the projective closure of
\[
 x=\frac{u^m+u^{-m}}2,\qquad
 y=\frac{cu^n+c^{-1}u^{-n}}2,\qquad u\in\mathbb C^*.
\]
Then \(C_{m,n,c}\) is an irreducible rational plane curve of degree \(2n\). It has exactly \(2mn-m-n\) ordinary nodes in the affine chart; this affine count is background, not the new contribution. Its projective boundary consists of a single point \(Q=[0:1:0]\), with exactly two branches. If \(n-m>1\), each has one Puiseux pair \((n-m,n)\); if \(n-m=1\), both branches are smooth and have no Puiseux pairs. In both cases their mutual intersection number is \(n(n-m)\). Consequently,
\[
\delta(C_{m,n,c},Q)=(n-m-1)(n-1)+n(n-m).
\]
The projectively dual curve has degree
\[
\deg C_{m,n,c}^{\vee}=2(m+n).
\]
There are precisely \(2(m+n)\) distinct ordinary flex points in the affine smooth locus, and each of the two normalization points above \(Q\) has ramification weight \(2n-m-3\) for the hyperplane linear series. In particular, the complete flex/Wronskian divisor is explicitly accounted for.

## Assumptions and scope

All geometry is over \(\mathbb C\). The parameter \(u\) lies in \(\mathbb P^1\) after compactification, and the term 'ordinary flex' means that the tangent line has contact exactly three with a smooth branch. The transcendence hypothesis is a convenient sufficient genericity condition: the exclusions arise from nonzero polynomials with rational coefficients. No claim is made for special algebraic phase parameters (notably the unshifted Chebyshev locus). The dual is the Zariski closure of embedded tangent lines at smooth points. The local \(\delta\)-invariant is the length of the normalization quotient. For a vanishing sequence \((a_0,a_1,a_2)\), the Wronskian weight is \(\sum_{i=0}^2(a_i-i)\).

## Proof

**1. Normalization, degree, and the affine comparison.** The degree-\(2n\) basepoint-free parametrization on \(\mathbb P^1\), with homogeneous coordinates \([s:t]\) and \(u=s/t\), is
\[
[s:t]\longmapsto
\left[s^{n+m}t^{n-m}+s^{n-m}t^{n+m}:\;c s^{2n}+c^{-1}t^{2n}:\;2s^nt^n\right].
\]
For distinct finite nonzero parameters \(u,v\), equality of the first affine coordinate is equivalent to \(u^m=v^m\) or \((uv)^m=1\). Equality of the second is equivalent to \(u^n=v^n\) or \(c^2(uv)^n=1\). The two simultaneous 'same-power' alternatives imply \(u=v\), while two simultaneous 'inverse-product' alternatives force \(c^2\) to be a root of unity. Thus for transcendental \(c\), the only nontrivial coincidences have exactly one same-power and one inverse-product alternative. Such coincidences are finite, hence the parametrization is generically one-to-one and is the normalization. The image has degree \(2n\).

For reference, the two types of affine coincidences can be enumerated. For type A, \(v=\xi u\), where \(\xi^m=1\), \(\xi\ne1\), and \(c^2u^{2n}\xi^n=1\). There are \(n(m-1)\) unordered pairs. For type B, \(v=\eta u\), where \(\eta^n=1\), \(\eta\ne1\), and \(u^{2m}\eta^m=1\). There are \(m(n-1)\) unordered pairs. The congruence \(\gcd(m,n)=1\) rules out three distinct parameters with a common image within either type; mixing types would force \(c\) algebraic. Differentiating the affine coordinates shows that the two branch tangents at every collision are transverse: they differ by flipping precisely one of the two nonzero derivative components, and simultaneous derivative vanishing would again force \(c\) algebraic. Hence these are \(2mn-m-n\) ordinary nodes, with no other affine singularities. This affine enumeration also supplies a direct consistency check for the boundary calculation.

**2. The unique point at infinity and its two branches.** The homogenized map shows that only \(s=0\) and \(t=0\) lie over the line at infinity, and both map to \(Q=[0:1:0]\). In the chart \(Y=1\) use coordinates \((\xi,\zeta)=(X/Y,Z/Y)\). At \(u=s/t=0\),
\[
\xi=c\,u^{n-m}(1+O(u^{2m}))(1+O(u^{2n})),\quad
\zeta=2c\,u^n(1+O(u^{2n})).
\]
At \(v=t/s=0\), the leading coefficients are instead \(c^{-1}\) and \(2c^{-1}\). Put \(a=n-m\). A local change of parameter that makes \(\xi\) an exact \(a\)-th power preserves the order \(n\) of \(\zeta\). For \(a>1\), the first exponent \(n\) is coprime to \(a\), so there is exactly one Puiseux pair \((a,n)\) and the branch has \(\delta=(a-1)(n-1)/2\). For \(a=1\), \(\xi\) is a local parameter, so the branch is smooth with \(\delta=0\), the same value given by the formula.

The weighted initial equations of the two branches are, respectively,
\[
\zeta^a-2^a c^{-m}\xi^n=0,\qquad
\zeta^a-2^a c^m\xi^n=0.
\]
They are distinct because \(c^{2m}\ne1\). Substituting the parameter of one branch into an equation for the other therefore gives order \(an\), and the two branches have intersection multiplicity \(an=n(n-m)\). The additivity formula for \(\delta\) at a two-branch singularity yields
\[
\delta_Q=2\cdot\frac{(a-1)(n-1)}2+an=(n-m-1)(n-1)+n(n-m).
\]
As a check, \((2mn-m-n)+\delta_Q=(2n-1)(n-1)\), the arithmetic genus of a degree-\(2n\) plane curve, so the singularity accounting is complete.

**3. The exact projective-dual class.** A tangent line at a smooth affine parameter is represented by
\[
[\,y'(u): -x'(u): x'(u)y(u)-y'(u)x(u)\,].
\]
Multiplying by \(4u^{m+n+1}\) produces the polynomial triple
\[
\begin{aligned}
A(u)&=2n(cu^{m+2n}-c^{-1}u^m),\\
B(u)&=-2m(u^{2m+n}-u^n),\\
C(u)&=(m-n)cu^{2(m+n)}+(m+n)c^{-1}u^{2m}\\
&\quad -(m+n)cu^{2n}+(n-m)c^{-1}.
\end{aligned}
\]
The three sections have degree at most \(2(m+n)\), with \(C(0)=(n-m)c^{-1}\ne0\) and highest coefficient \((m-n)c\ne0\). At a nonzero parameter, a common zero would require \(x'(u)=y'(u)=0\), equivalently \(u^{2m}=1\) and \(c^2u^{2n}=1\); this contradicts transcendence. Thus the triple defines a basepoint-free morphism \(\mathbb P^1\to(\mathbb P^2)^\vee\) with degree-\(2(m+n)\) hyperplane pullback. In characteristic zero, biduality gives that the Gauss map of a non-linear irreducible plane curve is birational onto the dual. Therefore \(\deg C^\vee=2(m+n)\).

**4. All flexes and their weights.** The affine curvature determinant is
\[
 x'y''-y'x''=\frac{mn}{4u^{m+n+3}}P_{m,n,c}(u),
\]
where
\[
\begin{aligned}
P_{m,n,c}(u)={}&c(n-m)u^{2(m+n)}-c(m+n)u^{2n}\\
&+c^{-1}(m+n)u^{2m}+c^{-1}(m-n).
\end{aligned}
\]
After multiplying by \(c\), this is \(c^2F(u)+G(u)\), with
\[
F=u^{2n}\bigl((n-m)u^{2m}-(m+n)\bigr),\qquad
G=(m+n)u^{2m}-(n-m).
\]
The polynomials \(F\) and \(G\) are coprime: \(G(0)\ne0\), and at a nonzero zero of the second factor of \(F\), one has \(G=4mn/(n-m)\ne0\). Hence the rational function \(-G/F\) is nonconstant and separable in characteristic zero. Its critical values form a finite algebraic set, so at a transcendental value \(c^2\), the polynomial \(c^2F+G\) has exactly \(2(m+n)\) distinct roots, all in \(\mathbb C^*\).

To exclude node parameters, set \(X=u^{2m}\) and \(Y=c^2u^{2n}\), so that
\[
cP=Y((n-m)X-(m+n))+(m+n)X-(n-m).
\]
At a type A collision, \(Y=\xi^{-n}\) is a root of unity and \(X\) is transcendental: if \(X\) were algebraic, so would \(u\) and then \(c\). The coefficient \((n-m)Y+(m+n)\) of \(X\) is nonzero since \(|Y|=1\); the other term is algebraic, so \(cP\ne 0\). At a type B collision, \(X=\eta^{-m}\) is a root of unity and \(Y\) is transcendental. Now the coefficient \((n-m)X-(m+n)\) of \(Y\) is nonzero, again giving \(cP\ne0\). A simple zero of the curvature determinant at a smooth immersed parameter gives an ordinary flex. Thus there are exactly \(2(m+n)\) distinct ordinary affine flexes.

At either parameter above \(Q\), the three-dimensional hyperplane linear series has vanishing orders \((0,n-m,n)\). Its ramification weight is therefore \((n-m-1)+(n-2)=2n-m-3\). The total weight
\[
2(m+n)+2(2n-m-3)=6n-6=3(2n-2)
\]
agrees with the Wronskian degree of a \(g^2_{2n}\) on \(\mathbb P^1\), verifying that no ramification remains unaccounted for.

## Verification

Run `python checker.py` with Python 3 and SymPy. The included standalone checker performs exact symbolic differentiation, polynomial gcd/squarefreeness, absence of basepoints in the dual parametrization, arithmetic-genus conservation, and the flex-weight identity for ten coprime frequency pairs at \(c=2\). It is a finite sanity check; the quantifiers for arbitrary coprime \((m,n)\) and transcendental \(c\) are established by the preceding proofs, not by test coverage. The public proof requires no external software to define or verify the mathematical claim.

## Relationship to prior work

Mascarin (2026), Section 5, classifies affine singular loci of Lissajous varieties and characterizes curves via collision conditions, but does not state the projective boundary branches, their intersection number, the dual class, or the complete flex divisor. Mascarin and Telen (2025/2026), Section 2, provide the degree formula for Lissajous varieties; the degree here is compatible and not claimed original. Erb's account of real Lissajous curves gives the generic affine node count \(2mn-m-n\); it is included only as an independently familiar comparison and as a consistency check. Yuran's Plücker formulas assume a generic curve among all equations with a Newton polygon, whereas this is a special rational one-parameter Laurent-parametrized family. The previously recorded result on *unshifted Chebyshev curves* uses a different, degree-halved specialization with a different dual degree and a single point above infinity; it does not imply the generic two-branch statement here.

## Limitations

The theorem excludes algebraic special-phase values, including zero-phase specializations; no universal exceptional-set parametrization is claimed. The full singularity type and dual geometry at all special phases, and the number of real flexes for real phase choices, remain outside scope. The affine node formula and generic degree were known previously and are not claimed as new. The full analytic type of the dual curve, such as its bitangencies and singularity basket, is not determined. The novelty comparison depends on accessible source text and indexed research records, so absolute publication priority is not certified. No independent mathematical audit has been performed.

## References

1. Francesco Maria Mascarin, *Intersections, Equations, and Singularities of Lissajous Varieties*, arXiv:2611.15725v1 (first public 2026-11-11), https://arxiv.org/html/2611.15725v1, especially Section 5.
2. Francesco Maria Mascarin and Simon Telen, *Lissajous Varieties*, arXiv:2509.06844v2, https://arxiv.org/html/2509.06844v2, especially Section 2.
3. Wolfgang Erb, *Lissajous curves*, https://www.lissajous.it/Lissajous.html (generic affine node count).
4. Aliaksandr Yuran, *Plucker Formulas for Plane Algebraic Curves with a Given Newton Polygon*, arXiv:2204.04626, https://arxiv.org/abs/2204.04626 (related but different genericity assumptions).
