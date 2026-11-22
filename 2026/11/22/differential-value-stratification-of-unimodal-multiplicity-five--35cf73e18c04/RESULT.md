# Differential-value stratification of unimodal multiplicity-five space curves

## Finding

Let \(k\) be an algebraically closed field of characteristic zero, and let \(R=k[[x(t),y(t),z(t)]]\subset k[[t]]\) be the completed local ring of a multiplicity-five unimodal parametrized space-curve singularity in the classification of Greuel, Mehmood and Pfister. Define
\[
\Gamma(R)=\{\operatorname{ord}_t f:0\ne f\in R\},\qquad
\Lambda(R)=\{1+\operatorname{ord}_t h:0\ne h(t)\,dt\in R\,dx+R\,dy+R\,dz\}.
\]
The differential-value set \(\Lambda(R)\) is unchanged by analytic reparametrization or an analytic change of ambient coordinates. Write \(\Gamma^+=\Gamma\setminus\{0\}\). For all multiplicity-five unimodal normal forms, the complete classification is:

| Numerical semigroup \(\Gamma\) | Extra differential values \(\Lambda\setminus\Gamma^+\) | Colength \(\dim_k(k[[t]]dt/(Rdx+Rdy+Rdz))\) |
|---|---|---|
| \(\langle5,6,7\rangle\) | none | \(6\) |
| \(\langle5,6,8\rangle\) | none | \(6\) |
| \(\langle5,6,9\rangle\) | \(\{13\}\) on the locus described below; otherwise none | \(6\) on that locus; otherwise \(7\) |
| \(\langle5,7,8\rangle\) | none | \(7\) |

For \(\Gamma=\langle5,6,9\rangle\), the exact criterion is:

1. For \((x,y,z)=(t^5,t^6+t^7+b t^8,t^9)\), \(b\in k\), one has \(13\in\Lambda\) **if and only if** \(b\ne13/12\).
2. For \((x,y,z)=(t^5,t^6+c t^8,t^9)\), \(c\in\{0,1\}\), one has \(13\in\Lambda\) **if and only if** \(c=1\).

In particular, within the first normal-form family the differential colength jumps by exactly one at the unique marked modulus \(b=13/12\), although its numerical semigroup stays fixed.

## Assumptions and scope

The assertion is over an algebraically closed characteristic-zero coefficient field and concerns completed reduced unibranch local space-curve rings with parametrizations analytically equivalent to the multiplicity-five entries in Table 2 and Section 5 of Greuel--Mehmood--Pfister (2026). Derivatives are formal derivatives. The valuation of a nonzero differential \(h(t)\,dt\) is \(1+\operatorname{ord}_t h\), rather than \(\operatorname{ord}_t h\). The image of the Kähler differential module, not its torsion submodule, is being valued. The classification applies to every parameter permitted in those normal forms, not just tested numerical examples. The paper's multiplicity-four forms are outside this theorem.

## Proof

**1. Invariance and baseline.** The image of \(\Omega_{R/k}\to k[[t]]dt\) is precisely \(M=Rdx+Rdy+Rdz\). Ambient analytic coordinate changes preserve this module, and reparametrizations \(t\mapsto u(t)\) with \(\operatorname{ord}_t u=1\) preserve differential orders. For any nonzero \(f\in R\) with \(\operatorname{ord}_t f=n>0\), characteristic zero implies \(\operatorname{ord}_t df=n-1\). Hence \(\Gamma^+\subseteq\Lambda\). A possible extra differential value must therefore be a positive gap of \(\Gamma\).

**2. All semigroups except \(\langle5,6,9\rangle\).** The source's four order-five semigroups have respective positive gap sets
\[
\begin{array}{rcl}
\langle5,6,7\rangle &: & \{1,2,3,4,8,9\},\\
\langle5,6,8\rangle &: & \{1,2,3,4,7,9\},\\
\langle5,6,9\rangle &: & \{1,2,3,4,7,8,13\},\\
\langle5,7,8\rangle &: & \{1,2,3,4,6,9,11\}.
\end{array}
\]
In all forms the least differential order is five. For \(\langle5,6,7\rangle\), \(dx,dy,dz\) have distinct values \(5,6,7\), while a nonconstant ring coefficient has value at least five and thus makes the product differential value at least ten; the possible gaps eight and nine cannot be introduced by cancellation. The same argument applies to \(\langle5,6,8\rangle\), with basic values \(5,6,8\) and possible gaps seven and nine. For \(\langle5,7,8\rangle\), the basic values are \(5,7,8\); the only contribution with differential value ten from a nonconstant coefficient is \(x\,dx\). Every other nonconstant-coefficient term has value at least twelve; no cancellation at value ten can create the sole remaining candidate gap eleven. Consequently, \(\Lambda=\Gamma^+\) in all three semigroups.

**3. Reduction of the remaining case to finite jets.** Let \(\Gamma=\langle5,6,9\rangle\), whose conductor is fourteen. Its only possible new differential value is thirteen: values seven and eight cannot appear since the basic derivatives have distinct orders five, six, nine and coefficients from the maximal ideal have order at least five. Every coefficient \(r\in R\) is, modulo terms of \(t\)-order at least nine, a unique \(k\)-linear combination of \(1,x,y\); there are no ring elements of valuation seven or eight. Any term whose coefficient has valuation at least nine, multiplied by a derivative of value at least five, has differential value at least fourteen. Thus the image of \(M\), modulo coefficient terms of order at least thirteen, is spanned by
\[
dx,\ dy,\ dz,\ x\,dx,\ x\,dy,\ y\,dx,\ y\,dy.
\]
Their possible leading differential values are \(5,6,9,10,11,11,12\), so value thirteen is present exactly when the last three forms produce a third independent coefficient jet in degrees ten, eleven and twelve.

**4. The one-parameter family.** For \(x=t^5\), \(y=t^6+t^7+bt^8\), \(z=t^9\), the coefficient vectors of \(x\,dy\), \(y\,dx\), \(y\,dy\), in positions \((t^{10},t^{11},t^{12})dt\), are respectively
\[
(6,7,8b),\qquad(5,5,5b),\qquad(0,6,13).
\]
Their determinant is \(60b-65\). Equivalently,
\[
6(5x\,dy-6y\,dx)-5y\,dy=(60b-65)t^{12}dt+O(t^{13})dt.
\]
Therefore there is a differential of value thirteen precisely when \(b\ne13/12\). When \(b=13/12\), the seven displayed jets have exactly six pivot values \(5,6,9,10,11,12\), so there is no other source of value thirteen.

**5. The discrete family.** For \(y=t^6+ct^8\), the analogous coefficient vectors are
\[
(6,0,8c),\qquad(5,0,5c),\qquad(0,6,0),
\]
whose determinant is \(60c\). Thus value thirteen appears if and only if \(c\ne0\), equivalent to \(c=1\) on the allowed parameter set.

**6. Exhaustiveness and colengths.** The conductor and characteristic zero give \(t^{n}\in R\) and \(n t^{n-1}dt\in M\) for every \(n\ge14\) in the \(\langle5,6,9\rangle\) case, so there are no missing differential values beyond those checked. The other three semigroups have conductors ten, ten, and twelve, respectively, and the same argument applies. For a finite-codimensional \(k\)-subspace of \(k[[t]]dt\), its colength is the number of missing filtration-leading valuations. Counting the displayed positive gaps, with value thirteen removed from the missing set exactly on the specified locus, gives the table. This exhausts the source's multiplicity-five unimodal classification.

## Verification

`VERIFY.py` is a standalone Python 3 rational-arithmetic checker. It constructs all coefficient monomials whose orders are at most eight and multiplies them by the three formal derivatives, then performs exact rational Gaussian elimination of the coefficient jets through \(t^{12}dt\). The script checks both types and multiple parameter values for each source normal form, including the exceptional rational value \(b=13/12\). These finite tests are independent consistency checks, **not** the proof for all parameters; the symbolic determinants and the conductor argument supply that proof. Run with `python3 VERIFY.py`.

## Relationship to prior work

Greuel--Mehmood--Pfister (arXiv:2611.13377v1, first posted 2026-11-09) supply the complete multiplicity-five normal forms and semigroups. Their Table 2 and Section 5 do not state the image-of-differentials valuation sets or the exceptional value \(13/12\). Carvalho--Hernandes (arXiv:1903.04696; Journal of Algebra 551, 2020) develop general standard-basis algorithms for semimodules and describe differential-value calculations. That methodology is wider, but their inspected article gives no explicit values for the later multiplicity-five unimodal forms; its Section 4 examples focus on plane curves. The present claim is the direct complete evaluation for the newly classified space-curve family, rather than a new general algorithm. Relevant analytic classifications of plane branches do not imply these space-curve-specific parameter conditions.

## Limitations

This is not a classification of multiplicity-four or higher-modality space curves, of arbitrary parametrizations, or of the torsion in the abstract Kähler differential module. Characteristic zero is needed for the derivative valuation argument and constants. The differential-value set does not distinguish all analytic classes; it separates the indicated strata only. An accessible literature/index search did not locate this exact evaluation, but cannot establish absolute publication priority; independent expert review has not occurred.

## References

1. Gert-Martin Greuel, Khawar Mehmood and Gerhard Pfister, *Unimodal Singularities of Parametrized Space Curves*, arXiv:2611.13377v1 (2026-11-09), Table 2 and Section 5. https://arxiv.org/html/2611.13377v1
2. Emilio Carvalho and Marcelo Escudeiro Hernandes, *Standard Bases for Fractional Ideals of the Local Ring of an Algebroid Curve*, arXiv:1903.04696 (2019), *Journal of Algebra* **551** (2020), 342--361, especially Sections 3--4. https://arxiv.org/abs/1903.04696
