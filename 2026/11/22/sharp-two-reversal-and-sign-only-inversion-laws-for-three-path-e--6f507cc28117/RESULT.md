# Sharp two-reversal and threshold-position inversion laws for three-path estuarine salinity attenuation

## Finding and scope

Consider the idealized discharge parameter \(Q\ge 0\), uncoupled junction salinities
\[
S_A(Q)=a e^{-\alpha Q}+c e^{-\gamma Q},\qquad S_B(Q)=b e^{-\beta Q},
\]
and a signed weak-overspill diagnostic \(T(Q)=K(Q)[S_A(Q)-S_B(Q)]\), where \(a,b,c>0\), \(0<\alpha<\beta<\gamma\), and \(K(Q)>0\). The rates are constant and have units reciprocal to those of discharge. Only the sign of the diagnostic is used; no differentiability of \(K\) is assumed. This is a three-independent-pathway exponential attenuation benchmark, not a hydrodynamic model or an empirical prediction for a particular estuary.

Write \(p=\beta-\alpha\), \(q=\gamma-\beta\), \(H(Q)=a e^{pQ}+c e^{-qQ}\), and \(H_0=a+c\). When \(cq>ap\), define
\[
Q_*={\log(cq/(ap))\over p+q},\qquad B_*=H(Q_*).
\]
There are two strictly positive direction reversals if and only if \(cq>ap\) and \(B_*<b<H_0\). The two thresholds satisfy \(0<Q_-<Q_*<Q_+\), are simple zeros of the normalized diagnostic \(H-b\), and have signs \(+,-,+\) on the three successive discharge intervals. All other root counts, including the boundary at zero, are given below.

With calibrated \(p,q\), the two positions determine \(a/b,c/b\), without knowing \(K\) or measuring a salinity or overspill magnitude. If \(U_\pm=e^{pQ_\pm}\), \(V_\pm=e^{-qQ_\pm}\), and \(D=U_+V_- - U_-V_+\), the ratios are \((V_--V_+)/D\) and \((U_+-U_-)/D\), respectively. Every ordered pair of strictly positive thresholds is realized by exactly one positive pair of ratios. Neither one location alone nor the two locations with uncalibrated rate gaps suffice in general; an absolute common salinity scale is never recovered from directions alone.

At fixed \(a,c,p,q\) with \(cq>ap\), as \(b=B_*+\varepsilon\downarrow B_*\), put \(t=\sqrt{2\varepsilon/(pqB_*)}\). Then
\[
Q_\pm=Q_*\pm t-{p-q\over6}t^2+O(t^3),\qquad Q_+-Q_-=2t+O(t^3).
\]
For \(p=q\) the midpoint is exactly \(Q_*\) throughout the two-reversal regime. **Although the matrix of the two threshold equations becomes singular at coalescence, the inverse as a map of two supplied threshold positions does not develop a singularity there.** Write \(m=(Q_-+Q_+)/2\) and \(d=(Q_+-Q_-)/2\). The amplitudes are
\[
\frac{a}{b}=e^{-pm}\frac{\sinh(qd)}{\sinh((p+q)d)},\qquad
\frac{c}{b}=e^{qm}\frac{\sinh(pd)}{\sinh((p+q)d)}.
\]
They extend analytically in \((m,d)\) through \(d=0\) by taking the ratios of the corresponding linear coefficients. At each finite midpoint the sensitivity to small absolute errors in supplied positions remains bounded as the thresholds merge. At fixed midpoint the ratios differ from their zero-gap limits by \(O(d^2)\), and their derivatives with respect to the half-gap are \(O(d)\). This is not a guarantee that noisy sign observations resolve two nearby switches.

## Proof

**Phase classification.** The sign of \(T(Q)\) is that of \(H(Q)-b\), since \(T(Q)=K(Q)e^{-\beta Q}[H(Q)-b]\). We have \(H'=ap e^{pQ}-cq e^{-qQ}\) and \(H''=ap^2 e^{pQ}+cq^2 e^{-qQ}>0\). If \(cq\le ap\), then \(H\) increases strictly on \([0,\infty)\) toward infinity, with \(H'(Q)>0\) for \(Q>0\). There is no strictly positive threshold for \(b\le H_0\) (equality gives a zero at \(Q=0\)); for \(b>H_0\) there is exactly one simple positive threshold with a negative-to-positive reversal.

If \(cq>ap\), the unique minimum \(Q_*\) is positive. The left branch falls strictly from \(H_0\) to \(B_*\), and the right branch rises strictly from \(B_*\) to infinity. For \(b<B_*\) there are no zeros, and for \(b=B_*\) there is one tangential positive zero of the normalized diagnostic with no reversal. For \(B_*<b<H_0\) there are exactly two simple positive zeros and the indicated sign pattern. For \(b=H_0\) there is a boundary zero and one simple positive reversal; for \(b>H_0\) there is just the latter. If \(\beta\le\alpha\) or \(\beta\ge\gamma\) instead, the two exponential terms remaining after normalization are monotone in the same sense, so there is at most one reversal. With one positive exponential on each branch the normalized difference is an exponential minus a constant, again allowing at most one reversal.

**Identification and realizability.** Put \(A=a/b,C=c/b\). The two equations \(A U_\pm+C V_\pm=1\) have nonzero determinant because \(U_+>U_->0\) and \(V_->V_+>0\). Cramer's rule gives the two strictly positive ratios above. Conversely the formulas for any \(0<Q_-<Q_+\) produce positive ratios, and strict convexity excludes further zeros, gives a unique minimum between them, and makes both zeros simple. Since this construction works for every positive pair of rate gaps, two root positions cannot determine the gaps. A single root position without another observation imposes one linear equation, leaving a positive segment. Common rescaling leaves all signs invariant.

**Fold and structured conditioning.** At \(Q_*\), set \(L=a e^{pQ_*}\) and \(J=c e^{-qQ_*}\). Then \(pL=qJ\), so \(H''(Q_*)=pqB_*\) and \(H'''(Q_*)=pq(p-q)B_*\). Thus the local equation for \(x=Q-Q_*\) is \(t^2=x^2+(p-q)x^3/3+O(x^4)\). The signed square root of the right side is analytic near zero with derivative one, giving \(x=\pm t-(p-q)t^2/6+O(t^3)\) by local inversion. For equal gaps the profile around the minimum is \(2\sqrt{ac}\cosh(px)\), giving exact midpoint symmetry.

In midpoint and half-gap coordinates, \(D=2e^{(p-q)m}\sinh((p+q)d)\). The two numerators vanish at the same order; their exact cancellation gives the displayed hyperbolic-sine ratios. For \(r>0\), \(\sinh(rd)/\sinh((p+q)d)\) extends as an even analytic function with value \(r/(p+q)\) at zero, by division of the analytic series after canceling \(d\). Hence the limit coefficients are \(q e^{-pm}/(p+q)\), \(p e^{qm}/(p+q)\), the unique ones giving both \(H(m)/b=1\) and \(H'(m)=0\). Their positive limits and the bounded derivatives of the extension give bounded absolute and relative amplitude sensitivity locally for fixed gaps and bounded midpoint. This statement is about perturbing the two positions with right-hand side fixed at \((1,1)\). Unstructured perturbations of the two equation levels can be amplified by the inverse matrix: its determinant is linear in \(d\), and its adjugate tends to a nonzero matrix. A lone observed zero does not provide a double-root constraint unless tangency is independently known.

## Verification

For \((\alpha,\beta,\gamma)=(1,2,3)\), \((a,b,c)=(1,9/2,4)\), we have \(Q_*=\log 2\), \(B_*=4\), and \(H_0=5\). The thresholds are \(\log((9\mp\sqrt{17})/4)\), approximately \(0.198214257465\) and \(1.188080103654\). The supplied `check.py` gives finite diagnostics of the root counts, distinct-threshold inversions and fold width. The analytic proof supplies the all-parameter theorem, including the extension at zero gap. Near zero gap the hyperbolic-sine expressions, evaluated using \(\sinh(u)/u\) and its continuous value at zero, avoid subtracting two nearly equal exponentials.

## Prior work and limitations

Biemond, de Swart and Dijkstra (2023) motivate the weak-overspill salinity-difference sign proxy in a seaward-flow regime; their hydrodynamic salinities do not assert this additive fixed-rate exponential law. Cai et al. (2023) study spatial salinity-profile inference from measured salinities, and Dijkstra et al. (2023) study stochastic intrusion statistics. Classical generalized Descartes rules cover the short exponential sum's zero-count bound; the inversion and fold use standard interpolation and local inversion. The contribution is the discharge-constrained phase diagram and the exact threshold-position interpretation, notably what is and is not singular when two switches approach. The accessible abstract of Chauveau et al. (1996) treats signed mixtures using function or noisy value data; it does not settle historical priority for this particular threshold-position formulation.

The model does not validate additive pathways, constant rates, or two direction reversals in a real estuary. It addresses deterministic calibrated gaps and supplied thresholds, not the statistical task of detecting the thresholds or distinguishing two close sign changes from a tangency. In particular no estimate is given for the effects of changing tides, stratification, nonadditive transport, unknown rates, or a sign-changing overspill factor.

## References

1. B. Biemond, H. E. de Swart, H. A. Dijkstra (2023), *Mechanisms of Salt Overspill at Estuarine Network Junctions Explained With an Idealized Model*, https://doi.org/10.1029/2023JC019630.
2. H. Cai, B. Li, J.-F. Zhao, E. Garel (2023), *Extension of the general unit hydrograph theory for the spread of salinity in estuaries*, https://doi.org/10.5194/os-19-603-2023.
3. H. A. Dijkstra, B. Biemond, J. Lee, H. E. de Swart (2023), *Explaining the Statistical Properties of Salt Intrusion in Estuaries Using a Dynamical Modeling Approach*, https://doi.org/10.1029/2023WR034454.
4. G. J. O. Jameson (2006), *Counting zeros of generalised polynomials: Descartes’ rule of signs and Laguerre’s extensions*, https://doi.org/10.1017/S0025557200179628.
5. D. Chauveau, C. F. Martin, A. C. M. van Rooij, F. H. Ruymgaart (1996), *Discrete signed mixtures of exponentials*, https://doi.org/10.1080/15326349608807383.
