# Sharp fourth-moment geometry of centered quadratic gamma polynomials

## Finding

For every shape \(\kappa>0\), consider the real space \(\mathcal V_\kappa\) of all degree-at-most-two polynomials of a Gamma-distributed random variable, constrained to have zero mean. Its nonzero normalized fourth moments attain one **exact sharp interval** with precisely one minimizing and one maximizing direction. Both directions mix the first and second nonconstant Laguerre modes; neither pure mode is extremal. The entire classification holds uniformly for every positive, not necessarily integer, shape parameter.

Define the explicit polynomials
\[
\begin{aligned}
 B_\kappa(t)={}&\kappa+2+16(\kappa+1)t
 +(20\kappa^2+116\kappa+96)t^2\\
 &+(128\kappa^2+448\kappa+320)t^3
 +(20\kappa^3+296\kappa^2+772\kappa+496)t^4,\\
 Q_\kappa(t)={}&(16\kappa^2+56\kappa+40)t^4
 -(40\kappa+100)t^3\\
 &-(18\kappa+54)t^2-(2\kappa+11)t-1,\\
 K_\kappa(t)={}&\frac{3B_\kappa(t)}{\kappa[1+2(\kappa+1)t^2]^2}.
\end{aligned}
\]

For **every** \(\kappa>0\), the quartic \(Q_\kappa\) has exactly two real roots \(t_-(\kappa)<0<t_+(\kappa)\), both simple. For all nonzero \(f\in\mathcal V_\kappa\),
\[
\boxed{K_\kappa(t_-(\kappa))\le\frac{\mathbb E f(X)^4}{[\mathbb E f(X)^2]^2}\le K_\kappa(t_+(\kappa)).}
\]
The left equality cases are exactly the nonzero scalar multiples of \(P_1+t_-P_2\); the right equality cases are exactly the nonzero scalar multiples of \(P_1+t_+P_2\). Both endpoints, and every number between them, occur. At \(\kappa=2\), \(t_-=-1/6\) and the lower constant is exactly \(15/7\). As \(\kappa\to\infty\), the sharp lower and upper fourth-moment quotients tend respectively to \(3\) and \(15\).

## Assumptions and scope

Let \(X\) have Gamma density \(x^{\kappa-1}e^{-x}/\Gamma(\kappa)\) for \(x>0\), with \(\kappa>0\). Work over **real** coefficients and fourth moments. The polynomials
\[
P_1(x)=x-\kappa,\qquad
P_2(x)=x^2-2(\kappa+1)x+\kappa(\kappa+1)
\]
have zero means and are mutually orthogonal in \(L^2\) of this probability measure. They equal respectively the negative first and twice the second classical generalized Laguerre polynomial of parameter \(\kappa-1\). Hence every mean-zero polynomial of degree at most two is uniquely \(f=aP_1+bP_2\), with \((a,b)\ne(0,0)\).

## Proof

**Exact moments.** The Gamma moment identity \(\mathbb EX^j=(\kappa)_j\) (rising factorial) yields
\[
\mathbb E(P_1+tP_2)^2=\kappa[1+2(\kappa+1)t^2],\quad
\mathbb E(P_1+tP_2)^4=3\kappa B_\kappa(t).
\]
In particular, the normalized quotient for a nonzero direction with \(a\ne0\), written \(t=b/a\), is precisely \(K_\kappa(t)\). Differentiating and simplifying gives the exact identity
\[
K_\kappa'(t)=
-\frac{48(\kappa+1)Q_\kappa(t)}
{\kappa[1+2(\kappa+1)t^2]^3}.
\]

**Exactly two real critical roots.** The quartic discriminant factors as
\[
\operatorname{disc}_t Q_\kappa=-6912(\kappa+2)^2(2\kappa+5)^2 R(\kappa),
\]
where a **strictly positive** algebraic certificate is
\[
\begin{aligned}
R(\kappa)&=4\kappa^4-10\kappa^3-62\kappa^2+168\kappa+441\\
&=\left(2\kappa^2-\tfrac52\kappa-21\right)^2
 +\tfrac{63}{4}\kappa^2+63\kappa>0.
\end{aligned}
\]
For a real quartic with nonzero leading coefficient, negative discriminant means exactly two simple real roots and one nonreal conjugate pair. Since \(Q_\kappa(0)=-1\) and its leading coefficient is positive, \(Q_\kappa\) has at least one root on each of the positive and negative half-lines. Consequently the real roots are uniquely \(t_-<0<t_+\), and the derivative identity shows a strict local minimum at \(t_-\) and a strict local maximum at \(t_+\).

**Projective boundary and globality.** The only coefficient direction not represented by finite \(t\) is \(a=0\), i.e. \(P_2\). In the valid local coordinate \(s=a/b\) near that direction, the normalized quotient is \(K_\kappa(1/s)\) and
\[
\left.\frac{d}{ds}K_\kappa(1/s)\right|_{s=0}
=\frac{3(128\kappa^2+448\kappa+320)}{4\kappa(\kappa+1)^2}>0.
\]
Therefore that boundary direction cannot be an extremizer. Compactness of the real projective coefficient line now forces the two displayed critical roots to be the **global** minimum and maximum; their strictness proves all equality cases. Connectedness of that projective line and continuity give every intermediate value. At \(t=0\), the first pure mode is nonstationary because \(K_\kappa'(0)=48(\kappa+1)/\kappa>0\).

**Exact example and large-shape limit.** Substitution at \(\kappa=2\) shows \(Q_2(-1/6)=0\) and \(K_2(-1/6)=15/7\). For \(\kappa\to\infty\), let \(Y_\kappa=(X-\kappa)/\sqrt\kappa\). Gamma cumulants yield \(Y_\kappa\to Z\) in all fixed moments, where \(Z\) is standard Gaussian. The normalized basis
\[
\frac{P_1(X)}{\sqrt\kappa}=Y_\kappa,\qquad
\frac{P_2(X)}{\sqrt{2\kappa(\kappa+1)}}
=\sqrt{\frac{\kappa}{2(\kappa+1)}}(Y_\kappa^2-1)
 -\sqrt{\frac{2}{\kappa+1}}Y_\kappa
\]
therefore has fourth-order coefficient moments converging to those of \((Z,(Z^2-1)/\sqrt2)\), uniformly on the unit circle of linear-combination coefficients. For \(a^2+b^2=1\), the limiting normalized fourth moment is
\[
3a^4+30a^2b^2+15b^4=3+24b^2-12b^4,
\]
whose attained range is precisely \([3,15]\). Uniform convergence on the compact coefficient circle proves the asserted endpoint limits.

## Verification

Run `python3 check_gamma_laguerre.py` with Python 3 and SymPy; mpmath is optional for direct density integration. The checker reconstructs the Gamma polynomial moments through exact rising-factorial formulas, verifies the derivative, quartic discriminant factorization and positive certificate symbolically, and checks the exact projective boundary derivative. It independently evaluates 49 rational shape/coefficient cases, six parameter root diagnostics, the exact \(\kappa=2\) witness, and three direct-density numerical quadratures. Its Gaussian-limit coefficient polynomial is checked symbolically. Numerical diagnostics corroborate identities but do not replace the discriminant and sign proof for all \(\kappa>0\).

## Relationship to prior work

Generalized Laguerre orthogonality and semigroup theory explain why this two-mode polynomial space is canonical. Nowak and Stempak (2010), in their Laguerre polynomial semigroup section, establish semigroup contractivity and discuss hypercontractivity, not the present exact two-sided fourth-moment interval or its parameter-dependent equality directions. Mohsenipour and Provost (2013) derive moments of quadratic forms in gamma variables for distribution approximation, but their displayed results are not a sharp optimization over the complete centered polynomial plane. Koekoek's Laguerre notes supply standard orthogonality, not fourth-norm extremizers. The new conclusion is the global shape-uniform sharp classification and its explicit real-root rigidity, not the Gamma moment identity or Laguerre basis.

## Limitations

The theorem concerns real centered polynomials of degree at most two under a **single Gamma law with arbitrary positive shape and unit scale**, and fourth moments. Scaling the Gamma variable gives an equivalent statement for arbitrary positive scale. It does not classify all multivariate gamma-chaos polynomials, higher polynomial degrees, non-Gamma weights, complex coefficients, or other exponents. The endpoint constants are algebraically implicit (unique signed quartic roots), not generally expressed by simplified radicals. Priority outside inspected literature cannot be excluded without independent bibliographic review.

## References

- A. Nowak and K. Stempak, *On Lp-contractivity of Laguerre semigroups*, first posted November 24, 2010, arXiv:1011.5437v1, https://arxiv.org/pdf/1011.5437 . Relevant material: Introduction and §2, Laguerre polynomial semigroups.
- A. Akbar Mohsenipour and S. B. Provost, *On Approximating the Distribution of Quadratic Forms in Gamma Random Variables and Exponential Order Statistics*, *Journal of Statistical Theory and Applications* 12 (2013), 173–184, https://www.atlantis-press.com/article/8357.pdf , DOI:10.2991/jsta.2013.12.2.4.
- R. Koekoek, *Special Functions: Orthogonal Polynomials: Laguerre Polynomials*, online teaching notes, last modified May 22, 2021, https://tudelft.roelofkoekoek.nl/teaching/specfunc/orthopoly/laguerre.html . Standard Rodrigues formula and orthogonality relation.
