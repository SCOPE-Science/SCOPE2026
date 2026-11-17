# Exact minimax Ishikawa tuning for orthogonal maps with a residual error bound

## Finding
For real Hilbert-space isometries with a quantitative residual error bound, a single constant-parameter Ishikawa iteration admits a **globally sharp, uniquely attained minimax contraction factor**. If \(\kappa>1/2\) is the allowed error-bound constant, the minimax one-step factor is
\[
q_\kappa=\frac{4\kappa^2-1}{4\kappa^2+1},\qquad
\alpha_*=\frac{2\kappa^2+1}{4\kappa^2+1},\qquad
\beta_*=\frac{2\kappa^2}{2\kappa^2+1}.
\]
The same tuning is minimax for every finite iteration horizon when the two parameters are held fixed. The result gives the exact worst-case rate rather than merely a qualitative linear convergence guarantee.

## Assumptions and scope
Let \(H\) be any real Hilbert space, \(U:H\to H\) a *surjective linear isometry*, \(F=\operatorname{Fix}U\), and \(P_F\) the orthogonal projection onto \(F\). Fix \(\kappa>1/2\) and assume the global residual error bound
\[
\operatorname{dist}(x,F)\le\kappa\|x-Ux\|\quad\text{for every }x\in H.
\]
Given \(\alpha,\beta\in[0,1]\), define one Ishikawa step by
\[
y=(1-\beta)x+\beta Ux,\qquad \mathcal I_{\alpha,\beta}x=(1-\alpha)x+\alpha Uy.
\]
For constant parameters let \(x_{n+1}=\mathcal I_{\alpha,\beta}x_n\). The worst-case factor is the supremum of the operator norm of \(\mathcal I_{\alpha,\beta}\) restricted to \(F^\perp\), over all real Hilbert spaces and admissible isometries with nontrivial \(F^\perp\). The minimization is over \([0,1]^2\), and the theorem claims *uniqueness* only in this constant-parameter class. The case \(\kappa=1/2\) is excluded because its spectral endpoint degenerates, and equality tunings cease to be unique.

## Proof
**1. Spectral reduction.** Since \(U\) is orthogonal, \(F\) and \(F^\perp\) are reducing subspaces. Set
\[
h=1-\frac1{2\kappa^2},\qquad -1<h<1.
\]
On \(F^\perp\), expanding the residual gives
\[
\|e-Ue\|^2=2\|e\|^2-2\langle Ue,e\rangle.
\]
Thus the error bound is equivalent to \(\langle Ue,e\rangle\le h\|e\|^2\) for all \(e\in F^\perp\). The complexification of \(U|_{F^\perp}\) is unitary and normal, so its spectrum lies in the circular arc \(\{z:|z|=1,\operatorname{Re}z\le h\}\). Conversely the arc bound implies the residual inequality.

**2. Polynomial representation.** One Ishikawa step is the polynomial in \(U\)
\[
p(U)=aI+bU+cU^2,\quad a=1-\alpha,\quad b=\alpha(1-\beta),\quad c=\alpha\beta,
\]
where \(a,b,c\ge0\) and \(a+b+c=1\). Conversely every such triple is attainable, using \(\alpha=b+c\) and, when \(\alpha>0\), \(\beta=c/(b+c)\). The minimax problem therefore equals the minimum, over all probability triples, of \(\max_{|z|=1,\operatorname{Re}z\le h}|a+bz+cz^2|\).

**3. A two-endpoint lower certificate.** Put \(u=\operatorname{Re}z\). Because \(a+c=1-b\), on the unit circle
\[
|a+bz+cz^2|^2=[b+(1-b)u]^2+(a-c)^2(1-u^2).
\]
At \(u=-1\) the modulus is \(|1-2b|\). At \(u=h\) it is at least \(|h+(1-h)b|\). Consequently, for every admissible polynomial,
\[
\max_{|z|=1,\operatorname{Re}z\le h}|p(z)|\ge
\max\{|1-2b|,|h+(1-h)b|\}.
\]
Set \(b_*=(1-h)/(3-h)\) and \(q_h=(1+h)/(3-h)\). For \(b<b_*\), the first term is \(1-2b>q_h\); for \(b>b_*\), the second term is \(h+(1-h)b>q_h\). At \(b=b_*\), both have modulus exactly \(q_h\). Hence any minimizer has \(b=b_*\). Since \(-1<h<1\), equality at \(u=h\) forces \(a=c\), by the strictly positive coefficient \(1-h^2\) in the displayed identity.

**4. Attainment and uniqueness.** Taking
\[
a_*=c_*=\frac1{3-h},\qquad b_*=\frac{1-h}{3-h}
\]
gives \(p_*(z)=(1+(1-h)z+z^2)/(3-h)\). For \(|z|=1\),
\[
|p_*(z)|=\frac{|1-h+2\operatorname{Re}z|}{3-h}.
\]
Over \(-1\le\operatorname{Re}z\le h\), this is bounded by \(q_h\), with equality at both endpoints. Thus \(q_h\) is the exact minimum and the optimal probability triple is unique. The map from triples with \(b_*+c_*>0\) to \((\alpha,\beta)\) is injective, giving the unique parameters
\[
\alpha_* = \frac{2-h}{3-h},\qquad \beta_* = \frac1{2-h}.
\]
Substituting \(h=1-(2\kappa^2)^{-1}\) yields the stated formulas.

**5. Uniform rate and sharpness.** Since \(p_*(U)\) is normal on \(F^\perp\), the spectral calculus gives \(\|p_*(U)^n\|\le q_h^n\). On \(F\), \(p_*(U)\) acts as identity. Thus \(x_n-P_Fx_0=p_*(U)^n(x_0-P_Fx_0)\), establishing the estimate for all \(n\ge0\). For sharpness, choose \(H=\mathbb R^2\) and the rotation through \(\theta=\arccos h\). Its unique fixed point is zero, its residual constant is exactly \(\kappa\), and \(p_*(U)\) is a scalar multiple of a rotation of modulus \(q_h\). Hence \(\|p_*(U)^n\|=q_h^n\) for every positive integer \(n\). For any nonoptimal coefficients, a rotation at \(u=h\) or the scalar map \(U=-I\) realizes at least the two-endpoint lower bound. This proves the minimax assertion at every fixed horizon for constant parameters.

For comparison only, a one-evaluation Mann step \((1-\alpha)I+\alpha U\) has minimax rate \(\sqrt{(1+h)/2}\), attained at \(\alpha=1/2\): its squared modulus is \(1-2\alpha(1-\alpha)(1-u)\). It is strictly larger than \(q_h\) for every \(-1<h<1\). This comparison is an elementary benchmark, not an assertion of priority.

## Verification
The accompanying standalone `verify.py` uses Python's standard library to check exact rational identities at many spectral-gap parameters and finite numerical samples of the unit circle and competing convex coefficients. Run `python3 verify.py` in the directory containing this document and `verify.py`. These finite calculations corroborate normalization, endpoint sharpness and optimization; the proof above establishes the infinite-dimensional and continuum statements.

## Relationship to prior work
Hamid, Patterson, Nuray and Basarır (2026) give general Ishikawa residual and linear convergence results under metric subregularity. Their accessible abstract does not assert a sharp worst-case constant or unique parameter tuning for linear isometries. Bravo, Cominetti and Pavez-Signé (2017) treat inexact Krasnosel'skii–Mann and Ishikawa residual estimates in a different generality. These convergence statements alone do not supply the two-endpoint optimization or exact rotation witnesses proved here. The 2026 paper's full text could not be obtained through the accessible routes, leaving a priority-comparison risk; no claim is made that its complete contents have been ruled out. Earlier polynomial filtering and spectral approximation theory may contain equivalent formulations under other names.

## Limitations
The theorem concerns *surjective linear isometries* of **real Hilbert spaces**, a uniform global residual bound, and *fixed* Ishikawa parameters. It does not optimize time-varying parameters, nonnormal or merely nonexpansive nonlinear maps, inexact iterations, or costs per operator evaluation. The minimax class includes rotations realizing its worst case; a particular operator whose spectrum stays farther from the arc endpoint may converge faster. Primary-paper full text was not accessible for a conclusive whole-document originality comparison. No independent validation has been performed.

## References
1. S. M. Hamid, R. F. Patterson, F. Nuray and M. Basarır, *Convergence rates and applications of Ishikawa iteration under metric subregularity*, J. Nonlinear Sci. Appl. **19** (2026), 170–184, DOI: 10.22436/jnsa.019.02.06, first published September 9, 2026. https://isr-publications.com/jnsa/articles-16511-convergence-rates-and-applications-of-ishikawa-iteration-under-metric-subregularity
2. M. Bravo, R. Cominetti and M. Pavez-Signé, *Rates of convergence for inexact Krasnosel'skii–Mann iterations in Banach spaces*, arXiv:1705.09340 (2017). https://arxiv.org/abs/1705.09340
3. S. Ishikawa, *Fixed points by a new iteration method*, Proc. Amer. Math. Soc. **44** (1974), 147–150.
