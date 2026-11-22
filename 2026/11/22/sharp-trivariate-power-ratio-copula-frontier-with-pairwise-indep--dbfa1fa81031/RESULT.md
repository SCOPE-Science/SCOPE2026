# Sharp trivariate power-ratio copula frontier with pairwise independence

## Finding
For every real \(p>0\) and \(\theta\in\mathbb R\), consider the three-variable ratio-type candidate
\[
C_{p,\theta}(u,v,w)=\frac{uvw}{1-\theta(1-u^p)(1-v^p)(1-w^p)},\qquad (u,v,w)\in[0,1]^3,
\]
where removable boundary values are assigned by continuous extension whenever possible. This candidate is a trivariate copula **if and only if**
\[
\boxed{-p^{-2}\le\theta\le\min\{1,p^{-3}\}.}
\]
In the entire admissible range every two-dimensional margin is the product copula, even though the joint law is non-independent for every \(\theta\ne0\). At \(p=1\), the parameter interval is \([-1,1]\); at \(p=2\), it is \([-1/4,1/8]\). The upper threshold changes form at \(p=1\).

## Assumptions and scope
Here \(p>0\), \(\theta\) is finite, and all copulas are distribution functions on \([0,1]^3\) with uniform one-dimensional marginals. A nonnegative Lebesgue mixed density is sufficient for three-increasingness when the CDF is grounded and continuous. At the isolated singular point \((0,0,0)\) when \(\theta=1\), define the CDF as zero. The theorem makes no assertion that this is a uniquely preferred parametric model for higher-order dependence.

## Proof
Put \(X=u^p\), \(Y=v^p\), \(Z=w^p\), and \(h=1-\theta(1-X)(1-Y)(1-Z)\). Whenever \(h>0\), the mixed density is \(c=N/h^4\), where the polynomial \(N\) is defined by
\[
N=h^4(1+pX\partial_X)(1+pY\partial_Y)(1+pZ\partial_Z)h^{-1}.
\]
This identity follows from \(\partial_u\{uF(u^p)\}=(1+pX\partial_X)F(X)\) and analogous identities for the other two coordinates. The numerator has coordinate degree at most three and parameter degree at most three. Evaluating the exact numerator at four vertices yields
\[
N(0,0,0)=(1-\theta)^3,\quad N(1,0,0)=1-p\theta,\quad
N(1,1,0)=1+p^2\theta,\quad N(1,1,1)=1-p^3\theta.
\]
If \(\theta>1\), the denominator vanishes at an interior point, so the candidate is not a copula. If \(\theta\le1\), the last two vertices show the necessary restrictions \(\theta\ge-p^{-2}\) and \(\theta\le p^{-3}\), since an interior nonnegative continuous density cannot have a negative limiting vertex value. These inequalities together give the asserted necessary interval.

For sufficiency it remains to prove \(N\ge0\) throughout the full four-dimensional parameter rectangle, without numerical sampling. Set \(\theta=-p^{-2}+s(b+p^{-2})\), where \(0\le s\le1\) and \(b=1\) for \(0<p\le1\), whereas \(b=p^{-3}\) for \(p\ge1\). Write \(p=(1+r)^{-1}\) in the first regime and \(p=1+r\) in the second, with \(r\ge0\).

Apply the degree-three tensor Bernstein transform to \(N\) in its four variables \((X,Y,Z,s)\). Explicitly, if \(N=\sum_{a,b,c,d=0}^3 n_{abcd}X^aY^bZ^cs^d\), the Bernstein coefficient at indices \((i,j,k,m)\) is
\[
B_{ijkm}=\sum_{a\le i,b\le j,c\le k,d\le m}n_{abcd}
\frac{\binom ia\binom jb\binom kc\binom md}
{\binom3a\binom3b\binom3c\binom3d}.
\]
Each Bernstein basis function is nonnegative and the basis functions sum to one on \([0,1]^4\). Symmetry in \(X,Y,Z\) reduces the coefficient check from 256 to \(20\times4=80\) distinct coefficients in each of the two regimes. The accompanying standalone `checker.py` derives \(N\) symbolically, computes these **160 rational coefficients in exact arithmetic**, and verifies that, on inserting the designated parameterization, each can be written as a quotient of two polynomials in \(r\) with nonnegative rational coefficients and strictly positive denominator. This finite exhaustive rational-polynomial certificate proves \(N\ge0\) for every admissible parameter. In particular the density is nonnegative wherever defined.

For \(\theta<1\), the denominator is positive throughout the cube and the grounded formula has continuous margins \(C(u,v,1)=uv\), \(C(u,1,w)=uw\), and \(C(1,v,w)=vw\). Therefore the density integrates to the prescribed CDF and it is a copula. If \(\theta=1\), the admissibility criterion forces \(p\le1\). In this case
\[
h=1-\prod_{i=1}^3(1-u_i^p)\ge \max(u^p,v^p,w^p)\ge\max(u,v,w),
\]
so \(0\le C(u,v,w)\le\min(u,v,w)\). Thus the extension to the origin/axes is continuous; the interior positivity argument plus continuity gives three-increasingness. All bivariate margins equal independence because setting the third coordinate to one annihilates the interaction factor. If \(\theta\ne0\), any interior triple gives \(C_{p,\theta}(u,v,w)\ne uvw\), so joint independence fails. This proves every assertion.

## Verification
Run `python checker.py` with SymPy. The program independently reconstructs the mixed-density numerator by differentiation, verifies the four boundary expressions, checks its finite tensor degree, and exhaustively checks all \(80+80\) Bernstein coefficients after the two parameter substitutions. Each polynomial-coefficient comparison is exact, and the run prints `PASS`. This computation certifies a finite symbolic identity/sign problem; the preceding argument converts that certificate into a theorem over the continuous parameter domain. No numerical optimization or finite grid is used as a substitute for an infinite-domain proof.

## Relationship to prior work
El Ktaibi, Bentoumi and Mesfioui (2024) analyze the **bivariate** ratio-type form \(uv/(1-\theta f(u)g(v))\). Their results provide the natural motivation, but their bivariate criteria do not determine three-dimensional mixed-volume nonnegativity. Chesneau (2024) studies other explicit three-dimensional copula families. A related earlier description of the special \(p=1\) ratio expression means the unpowered functional form alone is **not claimed as novel**. The contribution assessed here is the complete power-dependent sharp three-dimensional admissibility phase diagram and its proof, jointly with the pairwise-independent, non-independent regime. Neither a bivariate copula theorem nor a three-dimensional copula for one fixed parameter implies the sharp all-\(p\), all-\(\theta\) statement.

## Limitations
The theorem concerns only the displayed one-parameter power-symmetric three-way ratio family. It does not classify arbitrary asymmetric exponent triples, higher dimensions, or all pairwise-independent copulas. The symbolic certificate is reproducible but depends on the standard correctness of the exact rational-arithmetic engine. Historical priority of the complete parameter theorem has not been independently established. An earlier source gives the special unpowered case, so originality must not be inferred merely from the rational formula. Independent mathematical validation has not been performed.

## References
- F. El Ktaibi, R. Bentoumi and M. Mesfioui, *On the Ratio-Type Family of Copulas*, Mathematics 12(11), 1743 (2024), https://doi.org/10.3390/math12111743 (first published 3 June 2024).
- C. Chesneau, *Three-Dimensional Copulas: A Generalized Convex Mixture Copulas Strategy* (2024), https://doi.org/10.21608/CJMSS.2024.272790.1042.
