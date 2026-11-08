# Sharp finite-period inverse resolution for full tent dynamics

## Finding

Let \(T:[0,1]\to[0,1]\) be the full tent map, \(T(x)=2\min\{x,1-x\}\). For an integer \(N\ge2\), put
\[
P_N=\bigcup_{k=1}^{N}\{x\in[0,1]:T^k(x)=x\}.
\]
Fix \(0<\delta<1\), and let \(\mathcal F_{\delta,N}\) consist of all continuous maps \(g:[0,1]\to[0,1]\) with \(g(0)=g(1)=0\), \(g(1/2)=1\), absolutely continuous on each of \([0,1/2]\) and \([1/2,1]\), satisfying
\[
|g'(x)-T'(x)|\le\delta\quad\text{for almost every }x\ne1/2,
\qquad g(p)=T(p)\quad(p\in P_N).
\]
Then the exact optimal-recovery ambiguity is
\[
\boxed{\max_{g\in\mathcal F_{\delta,N}}\|g-T\|_\infty
=\frac{\delta}{2^N+1}.}
\]
The maximum is attained by a piecewise-affine perturbation. Every \(g\in\mathcal F_{\delta,N}\) has **exactly the same geometric periodic orbits, with the same orbit actions**, as \(T\) through least period \(N\). In particular, the conclusion is an obstruction even when the finite orbit data are given with their cyclic ordering, not merely as unlabelled orbit sets.

If the class is further restricted to maps that equal \(T\) on a neighborhood of **every** point in \(P_N\), the **supremum** is still \(\delta/(2^N+1)\). Its approximating maps can be chosen smooth on each monotonicity branch. Consequently, all derivatives and all periodic multipliers at every orbit of least period at most \(N\) may agree exactly while the \(C^0\) discrepancy approaches the sharp finite-data bound.

## Assumptions and scope

The slope constraint is an almost-everywhere bound on each monotonicity branch; the interval endpoints and critical height are fixed. It implies \(g'\ge2-\delta>1\) almost everywhere on the left branch and \(g'\le-(2-\delta)<-1\) on the right. Thus every admissible map is a uniformly expanding, two-full-branch interval map. The word "smooth" refers to smoothness on each branch; the turning point remains a corner. The data are **geometric positions and actions** of all periodic points through the cutoff, not only counts of cycles. The exact extremal statement has domain \(N\in\mathbb Z\), \(N\ge2\), and \(0<\delta<1\).

## Proof

**1. Exact periodic-position mesh.** Let \(m=2^N\) and \(\pi(t)=2\min\{t,1-t\}\) on the circle \(\mathbb R/\mathbb Z\). If \(D(t)=2t\pmod1\), then \(T\circ\pi=\pi\circ D\). Since \(\pi(s)=\pi(t)\) exactly when \(s\equiv\pm t\pmod1\), the fixed points of \(T^N\) form the union of the two rational grids
\[
A_N=\left\{\frac{2j}{m+1}:0\le j\le m/2\right\},\qquad
B_N=\left\{\frac{2j}{m-1}:0\le j\le m/2-1\right\}.
\]
There are exactly \(m\) distinct points: the denominators are coprime odd integers, the two grids meet only at zero, and every point in the union is a fixed point by the semiconjugacy. In increasing order these points are
\[
0=a_0<a_1<b_1<a_2<b_2<\cdots<a_{m/2-1}<b_{m/2-1}<a_{m/2},
\]
where \(a_j=2j/(m+1)\) and \(b_j=2j/(m-1)\). The endpoint \(1\) is added after \(a_{m/2}\). For \(1\le j\le m/2-1\), the inner gaps are
\[
b_j-a_j=\frac{4j}{m^2-1},\qquad
 a_{j+1}-b_j=\frac{2(m-1-2j)}{m^2-1}.
\]
The first gap has length \(a_1=2/(m+1)\), and the final gap from \(a_{m/2}\) to \(1\) has length \(1/(m+1)\). The displayed formulas show that the first gap is uniquely longest. The turning point \(1/2\) is not in this first gap when \(N\ge2\). For each \(1\le k<N\), the smallest positive fixed point of \(T^k\) is \(2/(2^k+1)>2/(2^N+1)\), so adding all lower-period points cannot split the first gap. Therefore, after adding \(0,1/2,1\), the largest gap between consecutive points of \(P_N\cup\{1/2,1\}\) is **exactly**
\[
\ell_N=\frac{2}{2^N+1},
\]
attained uniquely between \(0\) and \(\ell_N\).

**2. Upper bound from the measured mesh.** Put \(h=g-T\). It is absolutely continuous on either branch, has \(|h'|\le\delta\) almost everywhere, and vanishes at \(P_N\cup\{1/2,1\}\). If \(u<v\) are consecutive points of that set, then for every \(x\in[u,v]\),
\[
|h(x)|\le\delta\min\{x-u,v-x\}
\le\frac{\delta}{2}(v-u)\le\frac{\delta\ell_N}{2}
=\frac{\delta}{2^N+1}.
\]
This applies on the whole interval.

**3. Exact extremizer.** Set \(a=\ell_N\) and define
\[
h_*(x)=\begin{cases}
\delta\min\{x,a-x\},&0\le x\le a,\\
0,&a\le x\le1.
\end{cases}
\qquad g_*=T+h_*.
\]
The support lies in the first periodic-position gap. Hence \(h_*(p)=0\) for all \(p\in P_N\). Its left-branch slopes differ from the corresponding slope of \(T\) by \(\pm\delta\); its right branch is unchanged. It is admissible, and at \(x=a/2\) the discrepancy is \(\delta a/2=\delta/(2^N+1)\), proving sharpness.

**4. Identical truncated periodic spectra.** Every admissible \(g\) has two inverse branches \(I_0,I_1:[0,1]\to[0,1]\) with Lipschitz constants no larger than \((2-\delta)^{-1}<1\). For each binary word of length \(k\), its ordered inverse-branch composition is a strict contraction with a unique fixed point. Such fixed points have distinct branch itineraries: the turning point is preperiodic to zero, not periodic. Consequently \(g^k\) has exactly \(2^k\) fixed points. Every point fixed by \(T^k\), with \(1\le k\le N\), lies in \(P_N\); the entire original orbit is unchanged under \(g\) because \(g=T\) on \(P_N\). Thus \(\mathrm{Fix}(T^k)\subseteq\mathrm{Fix}(g^k)\). Both sets have \(2^k\) elements, so they are equal, and each orbit action is the same. Taking minimal periods proves the assertion.

**5. Invisibility even to finite jets.** For \(0<\varepsilon<a/4\), define a smaller triangular Lipschitz bump supported in \([\varepsilon,a-\varepsilon]\), of slopes \(\pm\delta\) and height \(\delta(a-2\varepsilon)/2\). Convolving it with a nonnegative smooth mollifier of support less than \(\varepsilon/2\) produces \(C^\infty\) bumps \(h_\varepsilon\) with \(|h_\varepsilon'|\le\delta\), compact support in \((0,a)\), and \(\|h_\varepsilon\|_\infty\to\delta a/2\). For \(g_\varepsilon=T+h_\varepsilon\), equality with \(T\) holds on neighborhoods of every point of \(P_N\), so the periodic locations, actions, derivatives of all orders at those points and periodic multipliers through the cutoff coincide. The upper bound in Step 2 applies and the lower approximants reach its supremum.

## Verification

The accompanying standard-library Python program independently computes the period-fixed points using affine inverse-branch compositions, compares them with both rational grids, checks the unique largest gap after adding all smaller periods, and reconstructs the periodic spectrum of sample perturbed maps via independently implemented inverse branches. It checks \(10\) cutoff values, \(65\) rational-grid instances and \(27\) deformed inverse-spectrum comparisons. Its output is recorded in `VERIFICATION.md`. These finite tests are not substitutes for the proof above.

## Relationship to prior work

Fuhrmann, Gröger and Passeggi (2026) establish uniqueness of mixing interval maps from their **complete, unlabelled** periodic-orbit spectra. Their full-spectrum theorem and the present finite-horizon result are compatible: the perturbation depends on the cutoff and has a shrinking support. Their accessible theorem statements and proof discussion give no exact finite-cutoff \(C^0\) resolution constant. O'Hare (2024) studies finite **multiplier** data for smooth expanding **circle maps**, obtaining approximate smooth conjugacy, not the exact positional-data extremum for a full-branch tent map. Existing work on symbolic periodic points of tent maps motivates the rational-mesh calculation, which is not claimed as independently new. The contribution assessed here is the sharp inverse-resolution identity and its persistence under agreement of finite-order orbit jets.

## Limitations

This is a one-dimensional, two-full-branch, fixed-critical-point result. Its exact upper bound requires the **marked positional and action data** and the explicit slope constraint. Agreement of unlabelled orbit sets alone is shown insufficient for uniqueness at finite cutoffs, but **no universal upper bound from unlabelled finite data** is claimed. The smooth-jet subclass has the stated supremum, not necessarily a maximizer. The theorem makes no claim for arbitrary nonlinear maps or for estimates from noisy rather than exact periodic data. Historical priority remains provisional because some older tent-map full texts were inaccessible.

## References

1. G. Fuhrmann, M. Gröger, A. Passeggi, *Period spectrum and rigidity of interval maps*, arXiv:2610.07435v1 (first submitted 2026-10-05), https://arxiv.org/html/2610.07435 .
2. T. A. O'Hare, *Finite data rigidity for one-dimensional expanding maps*, *Ergodic Theory and Dynamical Systems* (first published 2024-11-13), DOI:10.1017/etds.2024.83, https://doi.org/10.1017/etds.2024.83 .
3. K. Scheicher, V. F. Sirvent, P. Surer, *Dynamical properties of the tent map*, *Journal of the London Mathematical Society* 93 (2016), 319–340, DOI:10.1112/jlms/jdv071 (abstract inspected; full text unavailable).
