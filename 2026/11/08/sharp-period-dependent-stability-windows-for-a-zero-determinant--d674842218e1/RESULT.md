# Sharp period-dependent stability windows for a zero-determinant border-collision map

## Finding

For the two-dimensional border-collision normal form with a zero left determinant, the family of strict attracting period-\(4k+3\) orbits with symbolic word \(L^2R(LR)^{2k}\) has an exact period-dependent existence threshold. Write \(n=2k+1\) and \(u=d-\ell r\). The sharp necessary-and-sufficient condition for *some* real right-hand parameters \(r,d\) to support the attracting word at fixed \(\ell,k\) is
\[
\ell^{-1/n}>2\ell+\ell^2.
\]
Equivalently, if \(u_k(\ell)>1\) is the unique root of \(u_k^n(u_k-\ell)=1+\ell\), the feasible projected parameter window is
\[
u_k(\ell)<u<\ell^{-1/n}.
\]
Every such strict attracting orbit must lie in this window. For every \(0<\ell\le\sqrt 2-1\), the window is nonempty for every \(k\ge1\). For \(\sqrt 2-1<\ell<1\), only those integers \(k\ge1\) satisfying \(2k+1<\log(1/\ell)/\log(2\ell+\ell^2)\) occur. This is an existence statement over right-hand parameters, not a claim that all values of \(u\) in the window yield the itinerary at every fixed \(r\).

## Assumptions and scope

The map is defined on \(\mathbb R^2\) by
\[
F(x,y)=\begin{cases}(\ell x+y+1,0),&x<0,\\(r x+y+1,-d x),&x>0,\end{cases}
\qquad 0<\ell<1,\quad r,d\in\mathbb R.
\]
The two branches agree on \(x=0\). A **strict** cycle has no switching-line visits; its symbols record signs of \(x\). An **attracting** cycle is asymptotically stable. Here the constructed cycles are hyperbolic and attracting, and their exact period is the length of their strict symbolic word. Neither global uniqueness nor absence of other coexisting attractors is asserted. Set \(n=2k+1\) for integer \(k\ge1\).

## Proof

We cyclically rotate the word to \(RLL(RL)^{2k}\) and put the initial point at \((x_0,0)\), \(x_0>0\), just before its distinguished \(R\). A single \(RL\) block sends an axis point \((x,0)\) to \((B(x),0)\), where
\[
 B(x)=1+\ell-u x,\qquad u=d-\ell r.
\]
The distinguished \(RLL\) block sends \((x,0)\) to \((C(x),0)\), where
\[
 C(x)=1+\ell+\ell^2-\ell u x.
\]
The entire formal cycle therefore solves \(x_0=B^{2k}(C(x_0))\), whose return derivative is \(-\ell u^n\). For \(u>0\), let \(U=u^{2k}\), \(h=1+\ell\), and \(x_*=h/(1+u)\). The unique formal solution in the attracting range is
\[
 x_0=\frac{U(1+\ell+\ell^2)+(1-U)x_*}{1+\ell uU},\quad
 B(x_0)=\frac{h-uU(u-\ell)}{(1+u)(1+\ell uU)}.
\]
The requirement that the second of the two consecutive \(L\) visits has negative first coordinate means \(B(x_0)<0\); when \(u\le0\), this is impossible because \(x_0>0\) gives \(B(x_0)\ge h\). For \(u>0\) the displayed expression implies precisely \(u^n(u-\ell)>h\). This forces \(u>1\), and is equivalent to \(u>u_k(\ell)\), because \(v\mapsto v^n(v-\ell)\) is strictly increasing for \(v\ge1\). Moreover a strict asymptotically stable cycle has the transverse multiplier zero (a left branch has determinant zero) and the nonzero multiplier \(-\ell u^n\); hence necessarily \(\ell u^n<1\). Thus \(u<u_s=\ell^{-1/n}\). This proves necessity independently of \(r,d\).

For sufficiency, assume \(u_k<u_s\) and first place \(u=u_k\) on the border. Here \(B(x_0)=0\), so \(C(x_0)=1\). The subsequent \(2k\) block-input coordinates are \(B^j(1)\) for \(0\le j<2k\), all positive. Indeed, \(B\) has fixed point \(x_*=h/(1+u)\); for even \(j\), \(B^j(1)=x_*+u^j(1-x_*)>0\), and for odd \(j\), the smallest one is
\[
 B^{2k-1}(1)=\frac{h-x_0}u=\frac{h(u-1)}{u^2}>0.
\]
The formal starting coordinate is \(x_0=h/u>0\). Choose \(u>u_k\) sufficiently close to \(u_k\), still below \(u_s\); all the right-block inputs remain positive, while \(B(x_0)<0\) ensures both distinguished \(L\) visits. Choose \(r\) sufficiently negative that \(rx+1<0\) at all these finitely many positive right inputs, and set \(d=\ell r+u\). Then every designated right visit is followed by the required left visit, so the formal periodic sequence is a genuine strict orbit. Its nonzero multiplier satisfies \(-1<-\ell u^n<0\), proving hyperbolic attraction. The strict word has a unique pair of consecutive \(L\) symbols, so its minimal period is exactly \(4k+3\).

The window is nonempty iff \(u_s^n(u_s-\ell)>h\), equivalently \(u_s>2\ell+\ell^2\). Since \(u_s>1\), this holds for every \(n\ge3\) iff \(2\ell+\ell^2\le1\), namely \(\ell\le\sqrt2-1\). If \(\ell>\sqrt2-1\), taking logarithms gives the stated strict cutoff on \(n\). For the asymptotics, define \(\alpha=\log((1+\ell)/(1-\ell))\) and \(\beta=\log(1/\ell)\). Implicit expansion of \(u_k^n(u_k-\ell)=h\) yields
\[
\log u_k=\frac{\alpha}{n}-\frac{\alpha}{(1-\ell)n^2}+O_\ell(n^{-3}),\qquad
\log u_s=\frac{\beta}{n}.
\]
Exponentiating and subtracting proves that \(u_s-u_k=(\beta-\alpha)/n+O_\ell(n^{-2})\) below the threshold. At \(\ell=\sqrt2-1\), \(\beta=\alpha\), so the first-order term cancels and \(u_s-u_k=\alpha/[(1-\ell)n^2]+O(n^{-3})\).

## Verification

The supplementary `verify.py` program checks the affine composition, orbit closure, branch signs, stability multipliers and parameter cutoffs using exact rational arithmetic for selected values of \(\ell,u\), and floating-point checks of boundary examples and complete branch itineraries. These finite checks corroborate but do not establish the parameter-uniform theorem. The proof above is analytic and covers every \(k\ge1\).

## Relationship to prior work

Simpson, *The two-dimensional border-collision normal form with a zero determinant* (arXiv:2408.04790v1, publicly available 2024-08-08), gives the map and reports stable cycles with the word \(L^2R(LR)^{2k}\) in Remark 6.1, explicitly leaving a theory for that structure open. Their observed cycles are prior art; the present contribution is the sharp necessary-and-sufficient existence criterion over the full right-hand parameter plane, the \(\ell=\sqrt2-1\) infinite-period boundary and its shrinking parameter-window laws. The paper's established fixed-period stability boundaries are acknowledged. General rotational word and resonance-tongue theory of Simpson and Meiss (arXiv:0809.3510) does not itself give this threshold. Simpson's later first-return classification (arXiv:2606.08901) assumes a right-hand repelling focus and does not supply this result for the explicitly constructed negative-determinant realizations.

## Limitations

Existence is quantified over real \(r,d\); the proof uses right-hand determinants that may be negative, and it does not claim the constructed parameter points coincide with the positive-\(d\) visualization in the originating article. The threshold rules out this particular strict *attracting* word for all right-hand parameters, not arbitrary period-\(4k+3\) cycles, non-strict border orbits, or arbitrary symbol words. The exact full two-dimensional shape and number of connected periodicity regions are not established. Possible earlier equivalent formulas in unindexed literature, especially the 2008 Simpson–Meiss article whose full text could not be inspected, remain a residual originality risk. No independent mathematical audit has been performed.

## References

1. D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790v1 (2024), https://arxiv.org/abs/2408.04790. Especially §6.4 and Remark 6.1.
2. D. J. W. Simpson and J. D. Meiss, *Shrinking point bifurcations of resonance tongues for piecewise-smooth, continuous maps*, arXiv:0809.3510 (2008), https://arxiv.org/abs/0809.3510.
3. D. J. W. Simpson and J. D. Meiss, *Neimark–Sacker bifurcations in planar, piecewise-smooth, continuous maps*, SIAM J. Appl. Dyn. Syst. 7 (2008), 795–824, DOI 10.1137/070704241.
4. D. J. W. Simpson, *One-dimensional first return maps for the two-dimensional border-collision normal form with a zero determinant*, arXiv:2606.08901 (2026), https://arxiv.org/abs/2606.08901.
