# Sharp linear shadowing for one-way affine interval gateways

## Finding
For parameters \(1<k\le 2\), \(0\le\lambda<1\), and \(1<\mu\le 2-\lambda\), define the self-map \(f:[0,2]\to[0,2]\) by
\[
f(x)=\begin{cases}kx,&0\le x<1,\\ \mu+\lambda(x-1),&1\le x\le2.\end{cases}
\]
For \(\delta>0\), let \(\mathcal P_\delta\) be the infinite sequences \((x_j)_{j\ge0}\subset[0,2]\) satisfying \(|f(x_j)-x_{j+1}|<\delta\), and define the optimal shadowing error
\[
E_f(\delta)=\sup_{(x_j)\in\mathcal P_\delta}\ \inf_{y\in[0,2]}\ \sup_{j\ge0}|f^j(y)-x_j|.
\]
**Theorem.** Whenever \(0<\delta<\tfrac12\min\{k-1,\mu-1\}\),
\[
\boxed{E_f(\delta)=\delta\max\!\left\{\frac1{k-1},\frac1{1-\lambda}\right\}.}
\]
The shadowing constant is independent of the jump height \(\mu\) inside its admissible parameter range. The two fixed-point lower-bound mechanisms exchange dominance at \(k+\lambda=2\): the repelling fixed point controls the exact constant for \(k+\lambda<2\), while the attracting fixed point controls it for \(k+\lambda>2\). Both lower bounds coincide at equality.

In particular, on the surjective discontinuous family \(\lambda=2-\mu\), \(1<\mu<k<2\), the exact constant is \(1/(\mu-1)\), sharpening the qualitative shadowing result and its nonoptimal quantitative estimates previously established for that family.

## Assumptions and scope
The state metric is ordinary Euclidean distance, initial points of exact orbits lie in \([0,2]\), and pseudo-orbits are **forward infinite** with uniform one-step error strictly smaller than \(\delta\). The supremum and infimum in the definition of \(E_f\) need not be attained. The parameter conditions ensure both branches map into \([0,2]\), and the right-hand branch maps \([1,2]\) into itself. No continuity at the cut is assumed. All asserted identities apply simultaneously to every admissible real parameter triple and every indicated \(\delta\).

## Proof
Put \(C=\max\{1/(k-1),1/(1-\lambda)\}\). Observe that \(C\ge1\), since \(k\le2\). The map's right interval is forward invariant, and the right-hand fixed point is \(r=(\mu-\lambda)/(1-\lambda)\in(1,2]\). Every exact orbit from a positive initial point reaches the right interval in finite time and converges to \(r\), whereas the zero orbit is fixed.

**Upper bound.** Let \((x_j)\in\mathcal P_\delta\). Since \(f([1,2])=[\mu,\mu+\lambda]\) and \(\delta<\mu-1\), the pseudo-orbit cannot leave \([1,2]\) once it enters. If it stays below \(1\) forever, repeated use of \(x_{j+1}>kx_j-\delta\), together with \(x_{j+n}<1\), gives
\[
0\le x_j\le k^{-n}x_{j+n}+\frac{\delta}{k-1}(1-k^{-n})\to\frac{\delta}{k-1}.
\]
Thus the exact zero orbit shadows it within \(C\delta\).

Otherwise let \(N\) be the first index with \(x_N\ge1\). If \(N=0\), take exact initial point \(y=x_0\). For \(N\ge1\), we have \(1\le x_N<k+\delta\); hence we may choose \(b\in[1,k)\) such that \(|x_N-b|<\delta\), and set \(y=k^{-N}b\). Its exact trajectory is \(f^j(y)=k^{j-N}b\) for \(j\le N\), with exactly the same first entry time into \([1,2]\) as the pseudo-orbit. Writing \(e_j=x_{j+1}-kx_j\), so \(|e_j|<\delta\) for \(j<N\), backward telescoping yields for \(0\le j\le N\)
\[
\left|x_j-k^{j-N}b\right|\le k^{j-N}|x_N-b|+\frac{\delta}{k-1}(1-k^{j-N})\le C\delta.
\]
From time \(N\) onward, both sequences are in the contracting right branch. Therefore, for every \(t\ge0\),
\[
|x_{N+t}-f^{N+t}(y)|\le\lambda^t|x_N-b|+\frac\delta{1-\lambda}(1-\lambda^t)\le C\delta.
\]
This proves \(E_f(\delta)\le C\delta\).

**Sharpness.** Fix any \(0<\varepsilon<\delta\). The constant sequence \(x_j=a\) with \(a=\varepsilon/(k-1)\) lies in \([0,1)\) and has one-step defect exactly \(\varepsilon\). The zero orbit has uniform error \(a\); every other exact orbit converges to \(r\), whose distance from \(a\) is at least \(a\), since \(a<1/2\) and \(r>1\). Its optimal uniform shadowing error is exactly \(a\).

Likewise, the constant sequence \(x_j=r-b\), where \(b=\varepsilon/(1-\lambda)\), lies in \([1,2]\), because \(b<1/2\) and \(r-1=(\mu-1)/(1-\lambda)>b\). Its one-step defect is \(\varepsilon\). Every positive exact orbit converges to \(r\), forcing uniform shadowing error at least \(b\); the zero orbit has error \(r-b>b\). The exact fixed orbit at \(r\) attains error \(b\). Letting \(\varepsilon\uparrow\delta\) proves the matching lower bound \(E_f(\delta)\ge C\delta\) and hence the theorem. The distinct extremizers establish the phase boundary.

## Verification
The proof uses only explicit affine recurrences and exact inequalities. The included standalone `verify.py` checks the upper-bound orbit reconstruction and fixed-point obstruction on 840 finite pseudo-orbit prefixes across six rational parameter triples, with exact rational arithmetic. Run `python verify.py` using standard Python 3. Its finite checks support the algebra, but the universal infinite-sequence claim follows from the analytical argument above; no exhaustive computational claim is made.

## Relationship to prior work
Henrique M. Oliveira, *Homological reduction and entropy of discontinuous interval maps*, arXiv:2611.03287v1 (2026), Section 10.3, Theorem 10.5, introduced the surjective family with \(\lambda=2-\mu\), \(1<\mu<k<2\), and proved qualitative shadowing using a larger nonsharp error estimate. The present result establishes its exact sharp Lipschitz constant and a three-parameter completion with an additional instability-dominated phase.

A. Bura, C. Good, and T. Samuel, *The Shadowing Property for Piecewise Monotone Interval Maps* (2026), establish shadowing obstructions for transitive discontinuous interval maps and exhibit a non-surjective shadowing example, namely the boundary subfamily \(\lambda=0\), \(\mu=2\) for selected \(k\). The present theorem covers this example for every \(1<k\le2\) and computes its exact optimal modulus; their qualitative proof does not imply this constant. The mathematical setting is distinct from uniformly expanding maps with no attracting branch. The exact affine recurrence makes the proof self-contained.

## Limitations
This is a forward-orbit result for one-gateway maps with positive left expansion and invariant contracting right branch. It does not address bilateral pseudo-orbits, structural stability under arbitrary nonlinear perturbations, or parameters outside the stated range. Exact constants for broader piecewise monotone families are not claimed. Historical priority beyond the inspected sources is provisional, and independent mathematical validation has not been performed.

## References
1. H. M. Oliveira, *Homological reduction and entropy of discontinuous interval maps*, arXiv:2611.03287v1, 2 November 2026, especially Theorem 10.5 and its proof. https://arxiv.org/html/2611.03287v1
2. A. Bura, C. Good, and T. Samuel, *The Shadowing Property for Piecewise Monotone Interval Maps*, American Mathematical Monthly (online 16 July 2026), DOI:10.1080/00029890.2026.2686074. https://www.tandfonline.com/doi/full/10.1080/00029890.2026.2686074
