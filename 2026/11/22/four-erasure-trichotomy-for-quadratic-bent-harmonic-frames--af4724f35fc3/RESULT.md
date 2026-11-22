# Four-erasure trichotomy for quadratic-bent harmonic frames

## Finding

Let \(m\geq2\) be an integer, \(G=\mathbb F_2^{2m}\), \(n=|G|=2^{2m}\), and \(r=2^m\). Define the hyperbolic quadratic form
\[
q(x)=\sum_{j=1}^{m}x_{2j-1}x_{2j}\pmod2,
\qquad D=\{x\in G:q(x)=1\},\qquad k=|D|=(n-r)/2.
\]
Form the \(k\)-by-\(n\) real Parseval harmonic frame \(V\) with entries
\[
V_{d,t}=n^{-1/2}(-1)^{d\cdot t}\quad(d\in D,\ t\in G).
\]
For every four-point erasure set \(E\subset G\), denote its four-column Gram matrix by \(P_E=V_E^*V_E\). Its unordered eigenvalue multiset is **exactly one of the following three**, with the stated number of distinct labelled four-point sets:

| Type | Spectrum of \(P_E\) | Multiplicity |
|---|---|---|
| A | \(\{(r+2),(r-2),(r-2),(r-2)\}/(2r)\) | \(n^3(n-1)/192\) |
| B | \(\{r-1+\sqrt5,r-1-\sqrt5,r,r-2\}/(2r)\) | \(n^2(n-1)(n-4)/32\) |
| C | \(\{r,r,r,r-4\}/(2r)\) | \(n(n-1)(n-4)(n-12)/192\) |

Define the alternating nondegenerate symplectic bilinear form
\[
B(u,v)=q(u+v)+q(u)+q(v)=\sum_{j=1}^{m}(u_{2j-1}v_{2j}+u_{2j}v_{2j-1})\pmod2.
\]
Writing any four distinct points as \(E=\{x,x+u,x+v,x+w\}\), type A holds exactly when \(B(u,v)=B(u,w)=B(v,w)=1\), type C exactly when all three values vanish, and type B otherwise. This criterion is independent of the chosen root \(x\).

Deleting the four columns indexed by \(E\) leaves the frame operator \(V_{G\setminus E}V_{G\setminus E}^*=I_k-V_EV_E^*\). Its least eigenvalue, equivalently the exact lower reconstruction-frame bound, is
\[
\ell_A=\frac{r-2}{2r},\qquad
\ell_B=\frac{r+1-\sqrt5}{2r},\qquad
\ell_C=\frac12
\]
for types A, B and C, respectively. Thus the sharp bound under **every** four erasures is \(1/2-2^{-m}\), attained on exactly \(n^3(n-1)/192\) masks. In particular, no four erasures destroy reconstruction for any \(m\geq2\).

At \(m=2\), the type multiplicities are \((320,1440,60)\); at \(m=3\), they are \((86016,483840,65520)\). At \(m=2\) the 60 type-C erasure-column quartets are linearly dependent; for every \(m\geq3\), all four-column Gram matrices are positive definite.

## Assumptions and scope

All vectors and scalar products are over the real numbers. The frame is *Parseval normalized*: its rows are orthonormal and the un-erased frame operator is the identity, while each column has squared norm \(k/n\), not one. The four erasures are **distinct labelled positions** from the character group. The theorem concerns exactly the hyperbolic quadratic-form difference sets displayed above, or their images under invertible linear changes of coordinates. It does not assert an analogous statement for arbitrary nonlinear bent functions or arbitrary difference sets.

## Proof

**1. Parseval property and character sums.** Distinct binary Walsh characters are orthogonal on \(G\), so \(VV^*=I_k\). For a frequency \(h\in G\), separation into \(m\) disjoint coordinate pairs gives the exact quadratic Walsh sum
\[
W_q(h):=\sum_{d\in G}(-1)^{q(d)+h\cdot d}=r(-1)^{q(h)}.
\]
Indeed, on one pair, \(\sum_{a,b\in\mathbb F_2}(-1)^{ab+\alpha a+\beta b}=2(-1)^{\alpha\beta}\). Because \(1_D(d)=(1-(-1)^{q(d)})/2\), this implies \(|D|=(n-r)/2\), and for \(h\neq0\),
\[
\sum_{d\in D}(-1)^{h\cdot d}=-(r/2)(-1)^{q(h)}.
\]
Consequently the restriction \(2rP_E\) has diagonal entries \(r-1\), and its off-diagonal signs are
\[
S_{st}=-(-1)^{q(s+t)}\quad(s\neq t),\qquad 2rP_E=(r-1)I_4+S_E.
\]
Here \(S_E\) is a real symmetric sign matrix with zero diagonal.

**2. Switching and the three spectra.** Multiplying a row and its matching column of \(S_E\) by the same sign preserves its eigenvalues. With \(E=\{x,x+u,x+v,x+w\}\), the product of the three edge signs on the triangle \((x,x+u,x+v)\) is
\[
S_{x,x+u}S_{x,x+v}S_{x+u,x+v}=-(-1)^{B(u,v)}.
\]
The analogous triangles rooted at \(x\) are controlled by \(B(u,w)\) and \(B(v,w)\). The product of all four triangle signs on any four vertices is \(+1\), because every edge occurs twice. Thus the number of negative triangle products is exactly \(0,2\), or \(4\). The four triangle signs determine the switching class: switching and relabelling yield representatives \(J_4-I_4\), a sign matrix with exactly one negative edge, and \(I_4-J_4\), respectively. Their spectra are
\[
\{3,-1,-1,-1\},\qquad\{\sqrt5,1,-1,-\sqrt5\},\qquad\{-3,1,1,1\}.
\]
The middle representative has characteristic polynomial \(t^4-6t^2+5\); the other two follow immediately from their rank-one form. Adding \(r-1\) and dividing by \(2r\) proves the three asserted Gram spectra, as well as the type tests using \(B\).

**3. Exact multiplicities.** Fix the first point \(x\) in \(n\) ways. The ordered nonzero, distinct differences \(u,v,w\) describe each unordered four-point set exactly \(4!=24\) times, since any of its four points may be selected as root and the other three ordered arbitrarily.

For type A, choose \(u\neq0\) in \(n-1\) ways. Nondegeneracy gives exactly \(n/2\) choices of \(v\) satisfying \(B(u,v)=1\), all different from \(0,u\). Because \(B(u,v)=1\), the linear functionals \(B(u,\cdot)\), \(B(v,\cdot)\) are independent, so exactly \(n/4\) choices of \(w\) satisfy both \(B(u,w)=B(v,w)=1\); none equals \(0,u,v\). Dividing \(n(n-1)(n/2)(n/4)\) by \(24\) gives \(n^3(n-1)/192\).

For type C, after choosing \(u\neq0\), choose \(v\) satisfying \(B(u,v)=0\) and \(v\notin\{0,u\}\), giving \(n/2-2\) choices. The two independent linear forms now have a joint zero space of size \(n/4\). Exactly three elements \(0,u,v\) of it are disallowed for \(w\), leaving \(n/4-3\). Hence the type-C count is \(n(n-1)(n/2-2)(n/4-3)/24=n(n-1)(n-4)(n-12)/192\). Subtracting both counts from \(\binom n4\) yields the type-B number \(n^2(n-1)(n-4)/32\). All three are strictly positive for every permitted \(m\), so the trichotomy is exact.

**4. Sharp erasure stability.** Because \(VV^*=I_k\), the retained frame operator is \(I_k-V_EV_E^*\). Since \(k\ge6>4\), its eigenvalues are \(1-\lambda\) for the four eigenvalues \(\lambda\) of \(P_E\), together with \(k-4\) further ones (counting zeros correctly). The largest Gram eigenvalues of types A, B, C are \((r+2)/(2r)\), \((r-1+\sqrt5)/(2r)\), and \(1/2\). Their strict decreasing order follows from \(3>\sqrt5>1\). Thus the corresponding least retained eigenvalues and unique worst class are exactly as asserted. For \(r\ge4\), the worst bound is positive. The only possible zero Gram eigenvalue in the displayed spectra occurs in type C with \(r=4\), establishing the final rank statements. \(\square\)

## Verification

Two standalone Python 3 scripts provide independent exact finite checks. `verify_direct_walsh.py` computes character sums directly from the quadratic set, constructs integer-scaled Gram matrices of every one of the \(\binom{16}{4}=1820\) erasure masks at \(m=2\), and checks integer characteristic polynomials by Newton identities with independently calculated determinants. `verify_symplectic_counts.py` uses the polarization form only, enumerating all four-subsets at \(m=2\) and \(m=3\), and confirms all symbolic multiplicities. Both were executed from the package and their standard outputs are included. These checks corroborate the displayed formulas; the proof for arbitrarily large \(m\) is the exact finite-field counting argument above, **not** extrapolation from enumeration.

## Relationship to prior work

- Fickus and Mixon, *Numerically erasure-robust frames* (arXiv:1202.4525, first version 2012-02-21), establish the motivation and general stability bounds for adversarially erased frames, including difference-set constructions, but do not give this quadratic-bent four-erasure spectral census.
- Jasper, Mixon and Fickus, *Kirkman Equiangular Tight Frames and Codes* (arXiv:1306.3111, first version 2013-06-13), relate McFarland harmonic frames and Steiner frames and discuss spark/RIP obstructions. Their statements do not determine the three four-mask spectral multiplicities for the present hyperbolic-quadratic family.
- Fickus, Jasper, King and Mixon, *Equiangular tight frames that contain regular simplices* (arXiv:1711.07081, first version 2017-11-19), explicitly identify the **already known 60** regular four-simplices in the \((16,6)\) harmonic frame. The present \(m=2\) type-C count of 60 is a recovery of this prior fact, not a newly claimed discovery. The additional type-A/type-B spectral incidence and the all-\(m\) formulas are the distinguishing claims.
- Brouwer, *Two-graphs*, https://aeb.win.tue.nl/drg/graphs/twographs.html, describes the regular sixteen-point switching class, but not this dimension-dependent erasure spectrum and sharp-multiplicity formula.
- A separately published real Paley harmonic four-column census treats odd-prime quadratic-residue frames, rather than the characteristic-two quadratic bent difference sets treated here. Its special-case formulas cannot be substituted to obtain the present counts.

## Limitations

This is a theorem about one natural infinite harmonic-frame family and exactly four erased coefficients. The classification is not extended to higher erasure cardinalities, arbitrary quadratic forms of opposite Arf sign, arbitrary bent functions, or optimality among all frames with similar dimensions. The exact subgroup and switching structure are classical tools; the claim of distinction from prior work concerns the combined complete erasure spectra, all-parameter multiplicities, and sharp surviving bounds, not the existence of the ETF or the previously known sixteen-point simplex count. A complete historical uniqueness search of every two-graph incidence table is not guaranteed; an unindexed equivalent census remains a priority risk. Independent mathematical audit has not been performed.

## References

1. M. Fickus and D. G. Mixon, *Numerically erasure-robust frames*, arXiv:1202.4525, https://arxiv.org/abs/1202.4525 (2012).
2. J. Jasper, D. G. Mixon and M. Fickus, *Kirkman Equiangular Tight Frames and Codes*, arXiv:1306.3111, https://arxiv.org/abs/1306.3111 (2013).
3. M. Fickus, J. Jasper, E. J. King and D. G. Mixon, *Equiangular tight frames that contain regular simplices*, arXiv:1711.07081, https://arxiv.org/abs/1711.07081 (2017).
4. A. E. Brouwer, *Two-graphs*, https://aeb.win.tue.nl/drg/graphs/twographs.html.
5. P. Xia, S. Zhou and G. B. Giannakis, *Achieving the Welch bound with difference sets*, IEEE Trans. Inf. Theory 51 (2005), 1900–1907, https://doi.org/10.1109/TIT.2005.846411.
