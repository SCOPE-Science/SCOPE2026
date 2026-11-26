# Characteristic-eleven Newton strata on a dihedral genus-three hyperelliptic locus

## Finding
Let \(k\) be an algebraically closed field of characteristic \(11\). For every \(a\in k\) with \(a^2\ne4\), let \(C_a\) be the smooth projective completion of
\[
C_a:\quad y^2=x(x^6+a x^3+1).
\]
Its Jacobian \(J_a\) has the following **complete Newton-polygon, \(11\)-rank, and \(a\)-number stratification**:

| Parameter | \(11\)-rank of \(J_a\) | \(a\)-number | Newton slopes, with multiplicity |
|---|---:|---:|---|
| \(a=0\) | \(0\) | \(3\) | \((1/2)^6\) |
| \(a\ne0\), \(a^2=-1\) or \(a^2=3\) | \(2\) | \(1\) | \(0^2,(1/2)^2,1^2\) |
| all remaining smooth parameters | \(3\) | \(0\) | \(0^3,1^3\) |

In particular, there are exactly four geometric parameter values in the intermediate stratum, no \(11\)-rank-one Jacobian in this family, and one superspecial parameter value \(a=0\). Over \(\mathbb F_{11}\), the nine smooth coefficients \(a\) split into \(1\), \(2\), and \(6\) coefficients of ranks \(0\), \(2\), and \(3\), respectively. These counts refer to coefficients in this normalized family, **not** to geometric isomorphism classes.

## Assumptions and scope
The base field is algebraically closed of characteristic exactly \(11\); all ranks and Newton polygons are geometric. The polynomial \(x(x^6+a x^3+1)\) is squarefree precisely when \(a^2\ne4\): the root \(0\) is simple, and away from it the map \(x\mapsto x^3\) is separable, so the other six roots are distinct exactly when \(u^2+au+1\) has two distinct roots. The smooth completion is therefore hyperelliptic of genus \(3\). The parameter \(a\) denotes coefficients of the displayed model, with no assertion that distinct coefficients always give nonisomorphic curves.

## Proof
**Elliptic quotients.** Fix a primitive cube root \(\zeta\) in \(k\). The transformations \(g:(x,y)\mapsto(\zeta x,\zeta^2 y)\) and \(r:(x,y)\mapsto(x^{-1},y/x^4)\) extend to automorphisms of \(C_a\), and satisfy \(g^3=r^2=1\), \(rgr=g^{-1}\). The quotient by \(\langle g\rangle\) is the smooth elliptic curve
\[
E_0:\quad V^2=u^3+a u^2+u,
\qquad (u,V)=(x^3,xy).
\]
The quotient by \(\langle r\rangle\) is the smooth elliptic curve
\[
E_1:\quad v^2=t^3-3t+a,
\qquad (t,v)=(x+x^{-1},y/x^2).
\]
Indeed \((xy)^2=x^2\,x(x^6+a x^3+1)=u(u^2+au+1)\), and
\((y/x^2)^2=x^3+x^{-3}+a=t^3-3t+a\). Both elliptic curves are nonsingular for \(a^2\ne4\).

The regular differentials of \(C_a\) form the basis \(\omega_j=x^j dx/y\), \(0\le j\le2\). Pullback from \(E_0\) gives \(3\omega_1\); pullback from \(E_1\) gives \(\omega_2-\omega_0\). Conjugating the latter quotient by \(g\) gives the independent differential \(\zeta\omega_2-\zeta^2\omega_0\). Their determinant in the three-dimensional differential space is nonzero because \(\zeta\ne\zeta^2\). Consequently the three elliptic quotient norm maps give an isogeny over \(k\)
\[
J_a\ \sim\ E_0\times E_1^2.
\]
This isogeny is used only for isogeny-invariant Newton polygons; no prime-to-\(11\) degree or descent to \(\mathbb F_{11}\) is asserted.

**Hasse invariants of the quotients.** For a smooth elliptic equation \(v^2=F(u)\) in characteristic \(11\), the coefficient of \(u^{10}\) in \(F(u)^5\) is a Hasse invariant: it is nonzero exactly when the elliptic curve is ordinary. Direct coefficient extraction gives
\[
\begin{aligned}
H(E_0)&=[u^{10}](u^3+a u^2+u)^5
=a^5-2a^3-3a=a(a^2+1)(a^2-3),\\
H(E_1)&=[t^{10}](t^3-3t+a)^5=6a
\end{aligned}
\quad\text{in }k.
\]
Hence \(E_1\) is supersingular precisely at \(a=0\), whereas \(E_0\) is supersingular precisely at \(a=0\) or \(a^2=-1\) or \(a^2=3\). The isogeny proves the three Newton-polygon rows and their \(11\)-ranks. The four nonzero exceptional parameters are smooth, since neither \(-1\) nor \(3\) equals \(4\) in characteristic \(11\).

**The \(a\)-number.** If \(f(x)=x^7+a x^4+x=\sum c_jx^j\), the Hasse–Witt matrix in the standard genus-three basis is \((c_{11i-j})_{1\le i,j\le3}\), with coefficients taken from \(f(x)^5\). Expansion gives
\[
M(a)=\begin{pmatrix}
0&0&5a\\
0&a(a^2+1)(a^2-3)&0\\
5a&0&0
\end{pmatrix}.
\]
The Cartier rank is \(0\) at \(a=0\), \(2\) on the four nonzero exceptional parameters, and \(3\) elsewhere. Since the \(a\)-number equals genus minus Cartier rank, the displayed values follow. In particular \(a(J_0)=3\), so \(J_0\) is superspecial, not merely supersingular. The nonzero entries in each surviving antidiagonal block remain nonzero under semilinear Frobenius iteration, consistently giving \(11\)-ranks \(2\) or \(3\).

**Rational coefficient counts.** The excluded parameters in \(\mathbb F_{11}\) are \(a=\pm2\). The polynomial \(a^2+1\) has no root in \(\mathbb F_{11}\), while \(a^2-3\) has the two roots \(a=\pm5\). Among the nine smooth coefficients, \(a=0\) has rank \(0\), \(\pm5\) have rank \(2\), and the remaining six have rank \(3\).

## Verification
The standalone, standard-library-only `verify.py` recomputes all nine entries of the Cartier/Hasse–Witt matrix and the two elliptic Hasse invariants as coefficient identities in \(\mathbb F_{11}[a]\), verifies their factorizations, and enumerates every \(\mathbb F_{11}\)-coefficient together with the smoothness restriction. Execute `python3 verify.py` from this package; the program prints `VERIFY_OK` only after all assertions succeed. The derivation above, rather than a finite sample, establishes the result for **every** geometric parameter.

## Relationship to prior work
Fuertes–Streit (2006, Section 6, equation (6.1)) already gives the precise dihedral pencil, automorphism actions and complex moduli; it does not calculate characteristic-eleven Newton strata. Gutiérrez–Sevilla–Shaska's 2012 treatment explicitly identifies the one-parameter complex automorphism locus with normal form \(y^2=x(x^6+a x^3+1)\), and discusses its extra involutions and elliptic quotients. The normal form and existence of splitting are **prior work**, not newly discovered here. Achter–Pries (2009) prove broad geometric results on the \(p\)-rank strata of hyperelliptic moduli; Pries's later survey describes generic Newton polygons. Those results do not specify the complete characteristic-\(11\) Newton restriction on this particular dihedral curve locus. Ohashi et al. (2025) include the known superspeciality of the isolated curve \(y^2=x^7-x\) when the characteristic is \(3\) modulo \(4\), which encompasses the \(a=0\) case up to algebraic-closure isomorphism. Earlier superspecial-parameter calculations on this same classical pencil also cover the characteristic-eleven marked parameter \(a=0\), but do not determine the intermediate rank-two Newton stratum. Thus superspeciality of the isolated endpoint is **not** claimed as new. The assessed exact contribution is the classification of all three Newton and \(a\)-number strata across the entire smooth one-dimensional locus, especially the four rank-two parameters and exclusion of rank one.

## Limitations
The claim is confined to the displayed characteristic-\(11\) family, not to all genus-three hyperelliptic curves. Isogeny preserves Newton polygons but need not preserve \(a\)-number; that invariant was verified separately from the full Cartier matrix. No assertion is made about equality of polarized Jacobians, fields of definition of the isogeny, uniqueness of geometric isomorphism classes, or complete Ekedahl–Oort types. Historical priority is provisional: an equivalent arithmetic tabulation in earlier literature not indexed by the searches might still exist. No independent scientific audit has been performed.

## References
1. Y. Fuertes, M. Streit, *Genus 3 normal coverings of the Riemann sphere branched over 4 points*, Revista Matemática Iberoamericana 22 (2006), 413–454, published 2006-08-31, DOI:10.4171/RMI/462, Section 6, equation (6.1).
2. J. Gutiérrez, D. Sevilla, T. Shaska, *Hyperelliptic curves of genus 3 with prescribed automorphism group*, arXiv:1209.2938v1 (first public 2012-09-13), especially Section 3, Table 1, case 8, and the discussion of the dihedral sublocus.
3. J. D. Achter, R. Pries, *The p-rank strata of the moduli space of hyperelliptic curves*, arXiv:0902.4637v1 (first public 2009-02-26), introduction and main stratification theorems.
4. R. Pries, *Generic Newton polygons for curves of given p-rank*, arXiv:1311.5846 (first public 2013-11-22), discussion of genus-three Newton polygons and the hyperelliptic stratification.
5. R. Ohashi et al., *Listing superspecial curves of genus three using Richelot isogeny graphs*, Research in Number Theory 11 (2025), article 76, DOI:10.1007/s40993-025-00657-3, Section 4.2, Theorem 4.4 (prior isolated superspecial example).
