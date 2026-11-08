# Sharp affine projection on biased Boolean cubes: resonant norming corners and a Gaussian–Poisson crossover

## Finding
Let \(d\ge2\), \(0<p<1\), and give \(\{0,1\}^d\) the probability measure under which the coordinates are independent Bernoulli variables of success probability \(p\). Let \(P_{d,p}\) be the real \(L^2\)-orthogonal projector onto the affine functions \(y\mapsto a_0+\sum_{i=1}^d a_i y_i\), regarded as an operator on \(L^\infty\) of this finite probability space. Put \(u=\min\{p,1-p\}\), \(v=1-u\), and
\[
 k=\lceil(d-1)u\rceil-1,\qquad
 B_{m,u}(j)=\binom mj u^jv^{m-j},\qquad
 F_{d,u}(k)=\sum_{j=0}^k B_{d,u}(j).
\]
Then the exact sharp norm is
\[
 \boxed{\|P_{d,p}\|_{L^\infty\to L^\infty}=1+2\left[dvB_{d-1,u}(k)-F_{d,u}(k)\right].}
\]
Here \(k\ge0\) and \(k\le d-2\) for the stated domain. The norm is attained by the corner with all coordinates equal to the rarer Bernoulli outcome. When \(u<1/2\), that corner is the unique norming corner unless \((d-1)u\) is an integer; at exactly those resonances all \(d\) corners differing from it in precisely one coordinate are norming as well, and no others are. When \(p=1/2\), every corner is norming. For each norming corner the signs of the affine reproducing kernel supply an \(L^\infty\)-unit extremizer (arbitrary values are permitted where the kernel vanishes).

The norms display two sharp distinct large-dimension regimes. For each fixed \(0<p<1\), with \(u\) as above,
\[
 \boxed{\lim_{d\to\infty}\frac{\|P_{d,p}\|}{\sqrt d}=\sqrt{\frac{2(1-u)}{\pi u}}.}
\]
For each fixed \(\lambda>0\), setting \(p_d=\lambda/d\) for all sufficiently large \(d\),
\[
 \boxed{\lim_{d\to\infty}\frac{\|P_{d,p_d}\|}{d}
 =2e^{-\lambda}\frac{\lambda^{\lfloor\lambda\rfloor}}{\lfloor\lambda\rfloor!}.}
\]
The latter limit is continuous and strictly decreasing in \(\lambda\), smooth between positive integers, and has an upward derivative jump of size \(2e^{-m}m^{m-1}/m!\) at each integer \(m\ge1\). [Equivalently this jump equals the common function value divided by \(m\).]

## Assumptions and scope
All spaces are real, all measures assign strictly positive mass to every vertex, and the \(L^\infty\) operator norm is with respect to the same Bernoulli-product probability on both input and output. The projection is onto the entire \((d+1)\)-dimensional first Walsh band, including the constant, not solely the homogeneous first chaos. The rare-corner statements are interpreted after relabeling success/failure when \(p>1/2\). The claim is finite-dimensional for each \(d\), and the limiting statements are separately quantified.

## Proof
**Kernel.** The constant and standardized coordinates \(\psi_i(y)=(y_i-p)/\sqrt{p(1-p)}\) form an orthonormal basis for the affine subspace. Hence the exact reproducing kernel is
\[
 K_{d,p}(x,y)=1+\sum_{i=1}^d\frac{(x_i-p)(y_i-p)}{p(1-p)}.
\]
For any evaluation point \(x\), the evaluation norm is \(\mathbb E_y|K_{d,p}(x,y)|\), with equality attained by \(f(y)=\operatorname{sgn}K_{d,p}(x,y)\). Taking the largest evaluation norm therefore gives the operator norm without an approximation argument.

**Which corners are norming.** By swapping labels if necessary assume \(0<p\le1/2\), and put \(q=1-p\). Conditional on \(x_i=1\), the random term \((x_i-p)(Y_i-p)/(pq)\) is \(-1\) with probability \(q\), or \(q/p\) with probability \(p\). Conditional on \(x_i=0\), it is \(-1\) with probability \(p\), or \(p/q\) with probability \(q\). For any fixed sum \(z\) from the constant and other coordinates, replacing \(x_i=0\) by \(1\) changes the expected absolute kernel by
\[
 \Delta_p(z)=q|z-1|+p|z+q/p|-p|z-1|-q|z+p/q|.
\]
Directly splitting at \(-q/p\), \(-p/q\) and \(1\) gives
\[
 \Delta_p(z)=\begin{cases}
 2p(z+q/p),&-q/p<z<-p/q,\\
 2(q-p)(1-z),&-p/q\le z<1,\\
 0,&\text{otherwise}.
 \end{cases}
\]
The two positive pieces match at their common boundary. Thus every replacement weakly increases the norm, and the all-ones corner is norming. At \(p=1/2\) every corner is equivalent under a measure-preserving cube symmetry.

For the strict classification assume \(p<1/2\). Suppose there are \(r\) ones and \(s=d-1-r\) zeros among the other \(d-1\) coordinates. By selecting \(k'\) of their \(r\) rare-coordinate high outcomes and \(\ell\) of their \(s\) common-coordinate high outcomes (each such configuration has positive probability), one realizes
\[
 z=2-d+k'/p+\ell/q.
\]
The strict region \(-q/p<z<1\) is equivalent to
\[
 t-1<k'+(p/q)\ell<t,\qquad t=p(d-1).
\]
If \(s\ge1\), such integers always exist. Indeed \(r+s(p/q)>t\). If \(r<t-1\), fix \(k'=r\) and increase \(\ell\) from zero: the steps have size \(p/q<1\), so the first value above \(t-1\) is below \(t\). If \(r\ge t-1\) and \(t\) is nonintegral, take \(k'=\lfloor t\rfloor,\ell=0\). If \(t\) is integral, take \(k'=t-1,\ell=1\). In the remaining case \(s=0\), all possible middle quantities are integers, and the open interval \((t-1,t)\) contains an integer exactly when \(t\) is not integral. Consequently all replacements are strict except possibly the final replacement, and that one is an equality exactly for integral \(p(d-1)\). This proves the complete norming-corner statement.

**Exact norm.** At the all-ones corner, let \(J\) be binomial with parameters \(d,p\). Then
\[
 K=1-d+J/p,\qquad \mathbb EK=1,
\]
and its negative part occurs precisely when \(J<p(d-1)\), or \(0\le J\le k\) with \(k=\lceil p(d-1)\rceil-1\). Therefore
\[
 \mathbb E|K|=1+2\mathbb E(d-1-J/p)_+.
\]
Using \(\mathbb E[J\mathbf1_{J\le k}]=dp\,\mathbb P(\operatorname{Bin}(d-1,p)\le k-1)\) and the binomial recurrence gives
\[
 \mathbb E(d-1-J/p)_+=d(1-p)B_{d-1,p}(k)-F_{d,p}(k).
\]
This gives the boxed exact norm, with \(u=p\) here and with the label-swap symmetry supplying the general case.

**Large-dimension limits.** At the rare corner, \(K=1+\sum_{i=1}^d Z_i\) with independent identically distributed centered terms of variance \((1-u)/u\). At fixed bias, the ordinary central limit theorem applies and bounded normalized second moments give uniform integrability of absolute values. The limiting mean absolute normal law is \(\sqrt{2(1-u)/(\pi u)}\).

For \(p_d=\lambda/d\), the binomial count converges in law to a Poisson variable \(N_\lambda\) of mean \(\lambda\); the second moments of \(K/d=1/d-1+J/\lambda\) are uniformly bounded. Hence the scaled norms converge to \(\mathbb E|N_\lambda/\lambda-1|\). Splitting the Poisson sum at the integer part of \(\lambda\) and applying \(j\mathbb P(N_\lambda=j)=\lambda\mathbb P(N_\lambda=j-1)\) gives
\[
 \mathbb E|N_\lambda/\lambda-1|=2\mathbb P(N_\lambda=\lfloor\lambda\rfloor).
\]
At an integer, the two adjacent Poisson masses coincide, proving continuity. Differentiating the explicit expression on each open unit interval proves strict decrease there and the one-sided derivative jump. This finishes the proof.

## Verification
Run `python3 check.py` using the standard library only. It independently enumerates complete signed kernels at every corner for a grid of dimensions and exact rational biases (including resonance values), verifies the norming-corner classification on that grid, checks the conditional absolute-value identity at exact-rational points, and corroborates the two distinct limiting regimes. The entire-dimension statements follow from the proof, not the finite tests.

## Relationship to prior work
Keller introduced the normalized biased Fourier–Walsh framework and examined reductions to the fair cube, spectral weights, hypercontractivity, and influences; his main results do not determine the \(L^\infty\) norm of the first-band orthogonal projection. Nayar studied \(L^2\) proximity to the affine Walsh band and structural FKN stability for bounded Boolean functions; these are different objectives from the sharp \(L^\infty\) amplification of the projection itself. Earlier exact results for *second*-degree Hamming projectors and second homogeneous Walsh chaos do not imply the first-band biased Bernoulli formula; the homogeneous and inhomogeneous spaces and/or sampling measures differ. The unbiased specialization is classical Fourier–Walsh material and is not asserted to be new. The present distinctive conclusions are the exact biased norming-corner resonance rule and the sharp rare-event Gaussian-to-Poisson scaling crossover.

## Limitations
The exact formula assumes identically distributed Bernoulli coordinates, product independence, affine rather than quadratic Walsh approximation, and the same probability measure on input and output. It does not provide sharp constants for heterogeneous biases, higher Walsh degrees, nonproduct measures, or continuous cubes. The asymptotics concern specified sequences of biases and do not assert a uniform two-parameter error bound. The source comparison is best-knowledge rather than proof of global literature uniqueness; the full text of all potentially related indexed 2026 results was not available, although their published indexed claims concern different degrees.

## References
1. N. Keller, *A Simple Reduction from a Biased Measure on the Discrete Cube to the Uniform Measure*, arXiv:1001.1167 (initial public version 7 January 2010), https://arxiv.org/abs/1001.1167 .
2. P. Nayar, *FKN Theorem on the Biased Cube*, arXiv:1311.3179 (initial public version 13 November 2013), https://arxiv.org/abs/1311.3179 ; *Colloquium Mathematicum* 137 (2014), 253–261.
3. *Exact Degree-Two Hamming Projection Norms and the Gaussian–Poisson Crossover*, published scientific record (2026), checked by its indexed statement only.
4. *A Lattice-Phase Second Term for Second-Chaos Projection Constants on the Boolean Cube*, published scientific record (2026), checked by its indexed statement only.
