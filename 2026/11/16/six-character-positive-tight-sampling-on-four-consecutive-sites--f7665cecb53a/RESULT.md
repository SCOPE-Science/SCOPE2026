# Six-character positive tight sampling on four consecutive sites of twice-prime cycles

## Finding
For every odd prime \(p\ge7\), the least number of **distinct** Fourier frequencies in \(\mathbb Z_{2p}\) carrying strictly positive weights that produce a tight frame on the four consecutive time sites \(A=\{0,1,2,3\}\) is exactly **six**. In fact, no formula supported on five or fewer distinct frequencies has the required moments, even if weights are allowed to be signed or complex.

## Assumptions and scope
Let \(N=2p\), with \(p\ge7\) an odd prime, and let \(\xi=e^{2\pi i/N}\). Select distinct frequencies \(\ell_1,\ldots,\ell_m\in\mathbb Z_N\) and strictly positive real weights \(w_1,\ldots,w_m\). The weighted harmonic observation matrix has entries \(H_{j,x}=\sqrt{w_j}\,\xi^{\ell_jx}\), for \(x\in A\) and \(1\le j\le m\). We call it tight when \(H^*H=cI_4\) with \(c>0\). Scaling the weights reduces to \(c=1\), and tightness is then equivalent to the three moment equations \(\sum_jw_jz_j^k=0\) for \(k=1,2,3\), together with \(\sum_jw_j=1\), where \(z_j=\xi^{\ell_j}\). Negative moments vanish by conjugation because weights are real.

## Proof
**A cyclotomic five-node obstruction.** Suppose a quadrature formula on no more than five distinct \(N\)-th roots satisfies the moment equations. Add arbitrary additional distinct roots with zero weights so that it is formally supported on five distinct roots \(z_1,\ldots,z_5\); this is permitted since \(N\ge14\). Write
\[P(z)=\prod_{j=1}^5(z-z_j)=z^5-e_1z^4+e_2z^3-e_3z^2+e_4z-e_5.\]
The integrands \(z^{-2}P(z)\) and \(z^{-3}P(z)\) vanish at each quadrature node. Their Laurent monomials have exponents entirely in \([-3,3]\). All their nonconstant terms integrate to zero under the assumed moment conditions; their constant coefficients are respectively \(-e_3\) and \(e_2\). Therefore \(e_2=e_3=0\).

Every \(N\)-th root has a unique expression \(z_j=\varepsilon_j\zeta^{r_j}\), where \(\varepsilon_j\in\{-1,1\}\), \(r_j\in\mathbb F_p\), and \(\zeta=e^{2\pi i/p}\). For each residue \(r\), define the integer \(c_r=\sum_{i<j:\ r_i+r_j=r}\varepsilon_i\varepsilon_j\). The equality \(e_2=0\) becomes \(\sum_{r=0}^{p-1}c_r\zeta^r=0\). The minimal polynomial \(1+z+\cdots+z^{p-1}\) of \(\zeta\) implies \(c_r=c\) for all \(r\), with one integer \(c\). Summing all coefficients yields
\[pc=\sum_{i<j}\varepsilon_i\varepsilon_j=\frac{(\sum_i\varepsilon_i)^2-5}{2}\in\{-2,2,10\}.\]
None is divisible by a prime \(p\ge7\). Contradiction. This proves \(m\ge6\). The obstruction only assumes vanishing moments of orders \(-3\) through \(3\) and normalization; positivity itself is needed for the geometric definition and the six-node construction.

**Six-node positive construction.** Choose \(a_0=0\), \(a_1=\lfloor p/3\rfloor\), and \(a_2=\lceil2p/3\rceil\). The three distinct points \(\eta_j=e^{2\pi i a_j/p}\) have successive angular gaps strictly less than \(\pi\), for every odd prime \(p\ge7\). Consequently the origin belongs to the strict interior of their triangle. There exist unique positive barycentric coefficients \(\alpha_j>0\) such that \(\sum_j\alpha_j=1\) and \(\sum_j\alpha_j\eta_j=0\). Choose any \(N\)-th root \(z_j\) satisfying \(z_j^2=\eta_j\), and sample the six distinct roots \(z_j,-z_j\) with weights \(\alpha_j/2\) on each member of its pair. Odd moments vanish within each antipodal pair; the second moment is \(\sum_j\alpha_j\eta_j=0\); and total mass is one. Thus \(H^*H=I_4\) using exactly six distinct frequencies. Combined with the obstruction, the optimum is six. \(\square\)

## Verification
The six-node construction was numerically checked from the exact barycentric equations for primes \(7,11,13,17,19,23,29,31\): all six weights are strictly positive, and the first three weighted moments have absolute residual below \(10^{-12}\). The nonexistence proof is exact and applies to all odd primes \(p\ge7\), without finite enumeration. A reproducible standalone checker is embedded as `verify.py`.

## Relationship to prior work
Harmonic and Hadamard tight frame constructions, including Fickus and Schmitt (arXiv:1903.09177), give a broader setting for character-table subframes, but the present **distinct-frequency, positive-weight, four-consecutive-site optimum** is a different finite quadrature question. The nearest published specific results determine positive tight sampling for **three consecutive sites** and for **three sites containing an antipodal pair** in twice-prime cycles. Neither statement gives this four-consecutive-site six-node minimum, nor the five-node cyclotomic obstruction. The connection to positive trigonometric quadrature and minimal vanishing sums of roots of unity is important; broader results in those literatures may overlap and were not exhaustively classified.

## Limitations
The theorem assumes a twice-prime cyclic order, a four-consecutive-site time mask, and strictly positive weights. It does not classify all optimal six-frequency supports or assert numerical robustness of every optimizer. Historical priority remains provisional: a general discrete positive-quadrature theorem might imply this bound under a different formulation. Independent validation has not been performed.

## References
- M. Fickus and C. A. Schmitt, *Harmonic equiangular tight frames comprised of regular simplices*, arXiv:1903.09177 (first submitted 21 March 2019), https://arxiv.org/abs/1903.09177 .
- *Sharp positive Fourier sampling on three consecutive cyclic sites*, published research record 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-positive-fourier-sampling-on-three-consecutive-cyclic-site--29fa16b8c55a .
- *Six-frequency rigidity for positively weighted Fourier frames on antipodal triples*, published research record 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-six-frequency-rigidity-for-positively-weighted-fourier-frames-on--68699c5041e8 .
