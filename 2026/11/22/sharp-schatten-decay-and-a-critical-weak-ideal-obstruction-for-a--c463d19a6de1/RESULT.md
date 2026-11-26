# Two-term Schatten and operator-norm asymptotics for Aluthge iterates of power-law shifts

## Finding

Fix \(0<t<1\) and \(\alpha>0\). On \(\ell^2(\mathbb N)\) with indexing starting at 1 let \(W_\alpha e_j=j^{-\alpha}e_{j+1}\). For the polar decomposition \(T=U|T|\) use \(\Delta_t(T)=|T|^tU|T|^{1-t}\), and put \(m=nt\). For every fixed \(p>1/\alpha\) and \(s=\alpha p\), as integers \(n\to\infty\),
\[
\begin{aligned}
\|\Delta_t^n(W_\alpha)\|_{\mathcal S_p}^p
 &=\frac{m^{1-s}}{s-1}-\frac{1+st}{2(1+s)}m^{-s}+O_{\alpha,p,t}(m^{-s-1}),\\
\|\Delta_t^n(W_\alpha)\|
 &=m^{-\alpha}\left(1-\frac{\alpha(1+t)}{2m}+O_{\alpha,t}(m^{-2})\right).
\end{aligned}
\]
The first correction to the Schatten mass combines the lattice endpoint term \(-1/2\) with the binomial variance term \(s(1-t)/(2(s+1))\). In particular one cannot absorb both displayed corrections into the same additive shift of \(m\) in the leading equivalents: the required shifts are \((1+st)/(2(1+s))\) for the Schatten mass and \((1+t)/2\) for the operator norm.

## Assumptions and scope

Here \(\mathcal S_p\) is defined by the sum of the \(p\)th powers of the decreasing singular values, including the quasi-norm range \(0<p<1\). All asymptotics refer to fixed admissible parameters and exact power weights. No uniform theorem as \(t\) approaches either endpoint or as \(\alpha p\downarrow1\) is asserted. The new claim is the second term with its order of remainder, not the leading equivalences or persistence of a weak-ideal obstruction.

## Proof

For a positive unilateral weighted shift with weights \(w_j\), the polar isometry is the unweighted forward shift; the transformed weights are \(w_j^{1-t}w_{j+1}^t\). Thus iteration of the linear recurrence on log weights gives the weights
\[
a_{n,j}=\exp\bigl(-\alpha\,\mathbb E\log(j+X)\bigr),\qquad X\sim \operatorname{Bin}(n,t).
\]
These are positive and decreasing in \(j\); the modulus is diagonal, so these are the singular values in order. For each fixed \(n\) they are bounded above by \(j^{-\alpha}\), so the stated Schatten mass is finite.

For \(q=j+m\) and \(Y=X-m\), one has \(\mathbb EY=0\), \(\mathbb EY^2=m(1-t)\), \(\mathbb EY^3=m(1-t)(1-2t)\), and \(\mathbb EY^4=O_t(m^2)\) by independence of the Bernoulli summands. On \(|Y|\le m/2\) expand \(\log(1+Y/q)\) through the cubic term, with error bounded by \(C|Y|^4/q^4\). On the complementary event the binomial Chernoff bound is \(O_t(e^{-c_tm})\). The logarithm relative to \(q\) is bounded there in absolute value by \(\max(\log(1+m),\log(1/t))\), since
\[
(1+m)^{-1}\le\frac{j+X}{j+m}\le 1/t.
\]
In extending the Taylor terms to the full probability space the extra terms are also exponentially negligible, because \(|Y|/q\) is bounded by a constant depending only on \(t\). The cubic expectation is \(O_t(m/q^3)\) and the fourth-order bound is \(O_t(m^2/q^4)\). Since \(q\ge m+1\), uniformly over \(j\ge1\) this yields
\[
\mathbb E\log(j+X)=\log q-\frac{m(1-t)}{2q^2}+O_t(m^{-2}),\qquad
a_{n,j}^p=q^{-s}\left(1+\frac{sm(1-t)}{2q^2}+O_{s,t}(m^{-2})\right).
\]

For \(s>1\), the first trapezoidal correction gives
\[
\sum_{j\ge1}(m+j)^{-s}=\frac{m^{1-s}}{s-1}-\tfrac12m^{-s}+O_s(m^{-s-1}).
\]
Indeed the sum of the unit-interval trapezoidal errors is bounded by \(\tfrac18\int_0^\infty |((m+x)^{-s})''|\,dx\), by integrating against the unit-interval quadratic error kernel. Integral comparison likewise gives \(\sum_{j\ge1}(m+j)^{-s-2}=m^{-s-1}/(s+1)+O_s(m^{-s-2})\). The uniform relative remainder sums to \(O_{s,t}(m^{-s-1})\), and the second coefficient is \(-1/2+s(1-t)/(2(s+1))\), as stated.

For the largest singular value set \(j=1\). Now \(\log(m+1)=\log m+1/m+O(m^{-2})\) and \(m/(m+1)^2=1/m+O(m^{-2})\), giving \(\mathbb E\log(1+X)=\log m+(1+t)/(2m)+O_t(m^{-2})\). Exponentiation proves the operator-norm formula. Expanding each leading equivalent at \(m+d\) gives the two different shifts stated above.

## Relationship to prior work

The binomial iteration formula and qualitative convergence of compact Aluthge iterates belong to the prior weighted-shift theory; see Stanković, Proposition 5.8, arXiv:2611.07728v1. The published finding *A universal linear singular-value boundary layer for regularly varying Aluthge shifts* (2026-11-17, record `948fb95b2a1e`) gives the first-order normalized profile for monotone regularly varying weights and its Schatten mass law. Its scales \(w_n\) and \(n\) give the same leading equivalents on rewriting them in terms of \(w_{\lfloor nt\rfloor}\) and \(nt\). The published finding *Strong Lorentz-ideal convergence and a sharp weak endpoint for compact Aluthge iterates* (2026-11-17, record `94c988f93c7b`) gives the obstruction of a power-decaying shift with weak quasi-norm 1 throughout iteration. Neither the regularly varying leading result nor the weak-endpoint obstruction is advanced here as new. The comparison to these two findings is based on their indexed statements; it is not a claim to have excluded all second-order results in their full texts.

## Verification and limitations

`verify.py` tests the two correction coefficients at finitely many parameters by summing the initial binomial-geometric singular values and bounding the remaining mass analytically up to ordinary floating-point rounding. The proof, not these diagnostics, establishes the all-parameter error orders. No second-order result for general slowly varying factors, no claim for other operator families, and no absolute priority claim is made.
