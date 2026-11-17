# Sharp total-variation perturbation constant for sliding median filters

## Finding

Let \(r\ge1\) and \(n\ge8r\) be integers. On the real vector space of \(n\)-periodic sequences, define the running median operator
\[
(M_r f)(i)=\operatorname{med}\bigl(f(i-r),\ldots,f(i+r)\bigr)
\]
and cyclic total variation \(\operatorname{TV}(f)=\sum_{i=0}^{n-1}|f(i+1)-f(i)|\). The exact global perturbation Lipschitz constant of this nonlinear operator in the total-variation seminorm is
\[
\boxed{\sup_{\operatorname{TV}(f-g)>0}\frac{\operatorname{TV}(M_r f-M_r g)}{\operatorname{TV}(f-g)}=2r+1.}
\]
The supremum is attained, not merely approached, by pairs of finite real sequences. The same upper bound holds for every cycle with \(n\ge2r+1\); the stated lower construction uses \(n\ge8r\). No sharpness assertion is made for shorter cycles.

## Assumptions and scope

Indices are read modulo \(n\); each median is the \((r+1)\)-st order statistic of a multiset of \(2r+1\) entries. Real sequences and the *one-step* (not iterated) median are considered. The quotient is over pairs whose nonconstant difference has positive total variation. The median map commutes with addition of constant sequences and hence induces a well-defined map on the quotient by constants, with normed difference distance \(\operatorname{TV}(f-g)\).

## Proof

**1. Universal upper bound.** Put \(h=g-f\) and \(\delta=M_rg-M_rf\). Monotonicity and constant-shift equivariance of the median imply, for every center \(i\),
\[
\min_{i-r\le j\le i+r} h(j)\le\delta(i)\le\max_{i-r\le j\le i+r}h(j).
\]
The two adjacent windows at \(i,i+1\) are contained in the extended interval \([i-r,i+r+1]\) of \(2r+2\) consecutive indices. Therefore both \(\delta(i)\) and \(\delta(i+1)\) lie between the minimum and maximum of \(h\) over that interval. Their difference satisfies
\[
|\delta(i+1)-\delta(i)|\le \max_{i-r\le j\le i+r+1}h(j)-\min_{i-r\le j\le i+r+1}h(j)
\le\sum_{j=i-r}^{i+r}|h(j+1)-h(j)|.
\]
Summing over all \(i\) counts each input edge exactly \(2r+1\) times, proving \(\operatorname{TV}(\delta)\le(2r+1)\operatorname{TV}(h)\).

**2. One sharp jump interface.** For a positive integer \(r\), make two spatially ordered blocks \(L_1,\ldots,L_{2r}\) at positions \(-2r,\ldots,-1\), and \(R_1,\ldots,R_{2r}\) at positions \(0,\ldots,2r-1\). Give these \(4r\) coordinates distinct integer values \(0,\ldots,4r-1\) in the following increasing-value order:
\[
L_1,\ldots,L_r,\ R_1,L_{r+1},\ R_2,L_{r+2},\ldots,\ R_r,L_{2r},\ R_{r+1},\ldots,R_{2r}.
\]
Call this assignment \(v\). Consider the medians of the successive windows centered at \(-r+j\) for \(0\le j\le2r-1\); the \(j\)-th window contains exactly
\[
\{L_{j+1},\ldots,L_{2r}\}\cup\{R_1,\ldots,R_{j+1}\}.
\]
The displayed value order shows that for \(j=2s\) the median is \(R_{s+1}\), whereas for \(j=2s+1\) it is \(L_{r+s+1}\), for the admissible \(s\). Indeed, the selected entry has precisely \(r\) window entries below it and \(r\) above it. Thus the median selector alternates sides \(R,L,R,L,\ldots,L\) across all \(2r\) affected centers.

**3. Two independent interfaces on a cycle.** Fix any \(n\ge8r\). Define an integer-valued baseline \(f\) using \(v\) on coordinates \(-2r\) through \(2r-1\) modulo \(n\); on coordinates \(4r+s\), \(-2r\le s\le2r-1\), use the reflected values \(v(-1-s)\). These two groups of \(4r\) coordinates are disjoint and cover all sites if \(n=8r\); set any remaining values to zero. Set \(h(i)=1\) for \(0\le i<4r\) and \(h(i)=0\) otherwise, and \(g=f+\varepsilon h\) for any \(0<\varepsilon<1\). Since the median windows around each interface contain distinct baseline integer values, their order-statistic selection does not change after adding \(\varepsilon h\). At the rising interface, \((M_rg-M_rf)(i)/\varepsilon\) alternates \(1,0,1,0,\ldots,0\) at centers \(-r,\ldots,r-1\), while it equals \(0\) immediately before and \(1\) immediately after these centers. Consequently this interface contributes precisely \((2r+1)\varepsilon\) to output variation. By reflection, the falling interface contributes another \((2r+1)\varepsilon\). Elsewhere the perturbation is constant throughout each window, so the median output perturbation is constant and contributes no other jumps. Therefore
\[
\operatorname{TV}(g-f)=2\varepsilon,
\qquad
\operatorname{TV}(M_rg-M_rf)=2(2r+1)\varepsilon.
\]
This proves attainability of the upper bound for every specified \(n\) and \(r\). For example, \(r=1,n=8\) is attained at \(f=(2,0,0,2,1,3,3,1)\), \(h=(1,1,1,1,0,0,0,0)\) and \(g=f+h/4\).

## Verification

The standalone `CHECK.py` reproduces the explicit integer order constructions with exact rational perturbations, verifying 96 sharp examples for \(1\le r\le16\) and three cycle lengths per radius. It additionally checks the universal bound on 2,400 independently sampled rational pairs. Its terminal marker is `ALL_RUNNING_MEDIAN_BV_CHECKS_PASSED`. The all-parameter result comes from the inequalities and rank argument above; finite tests are diagnostic only. Execute `python3 CHECK.py` using a standard Python 3 interpreter.

## Relationship to prior work

Classical median-filter smoothing theorems establish \(\operatorname{TV}(M_rf)\le\operatorname{TV}(f)\) for one input signal. This does **not** imply a nonexpansive estimate for two-input distances \(\operatorname{TV}(M_rf-M_rg)\), since the median filter is nonlinear. Restrepo and Chacón (1994) explicitly address single-signal variation. Little and Jones (2011, section 4(d), appendix A) treat one-signal variation diminution for three-point medians. Arias-Castro and Donoho (2006 first arXiv version, published 2009) study edge-preservation and statistical performance rather than this sharp nonlinear seminorm perturbation constant. The theorem above quantifies the different, two-input stability question with a sharp and arbitrarily large window-length dependence.

## Limitations

The exact sharpness construction needs cycle length \(n\ge8r\); the upper bound holds also for shorter cycles with \(n\ge2r+1\). This theorem does not claim a sharp constant for shorter cycles, nonuniform order-statistic weights, higher-dimensional medians, boundary-padded finite signals, or iterated median operators. An equivalent older formulation in nonlinear filter stability or stack-filter theory cannot be ruled out by the literature search alone. It should receive independent review before priority is asserted.

## References

1. A. Restrepo and L. P. Chacón, "A smoothing property of the median filter," *IEEE Transactions on Signal Processing* **42** (1994), 1553–1555. DOI: 10.1109/78.286974.
2. E. Arias-Castro and D. L. Donoho, "Does median filtering truly preserve edges better than linear filtering?" arXiv:math/0612422, first version 2006-12-14; *Annals of Statistics* **37** (2009), 1172–1206.
3. M. A. Little and N. S. Jones, "Generalized methods and solvers for noise removal from piecewise constant signals. I. Background theory," *Proceedings of the Royal Society A* **467** (2011), 3088–3114, DOI: 10.1098/rspa.2010.0671, especially §4(d) and Appendix A.
