# Two exact polarity reversals at fixed disorder contrast in a four-site exclusion chain

## Finding
For every fixed contrast \(r>1\), a four-site, open, site-disordered symmetric exclusion process with **two** independently heterogeneous interior hopping rates \(rh\) and \(h\) undergoes exactly two reversals of its *stationary full-reservoir-bias rectification polarity* as the common hopping-rate scale \(h\) runs from zero to infinity. If \(J_+(c,d)\) denotes the stationary left-to-right current with fully occupied left reservoir, empty right reservoir, and interior departure rates \((c,d)\), define
\[
\mathcal D_r(h)=J_+(rh,h)-J_+(h,rh).
\]
There are exactly two distinct, simple positive numbers \(h_-(r)<1/r<h_+(r)\) such that \(\mathcal D_r(h)<0\) for \(0<h<h_-(r)\), \(\mathcal D_r(h)>0\) for \(h_-(r)<h<h_+(r)\), and \(\mathcal D_r(h)<0\) for \(h>h_+(r)\). Equivalently, for the same ordered disorder realization, \(J(1,0)+J(0,1)\) changes sign exactly twice under this rate scaling, with the two boundary configurations denoting reservoir densities.

For example, at \(r=2\), the two thresholds are approximately \(0.251206144606\) and \(2.113641039357\). The statement is for **saturated reservoir driving**; it does not assert the same number of reversals at every weaker imposed density difference.

## Assumptions and scope
States are binary occupancy vectors \(\eta\in\{0,1\}^4\), with exclusion. At site \(i\), a particle can jump to a vacant nearest neighbor at departure-site rate \(q_i\), where \((q_1,q_2,q_3,q_4)=(1,c,d,1)\). At the left boundary, particles enter an empty site at rate \(\rho_L\) and leave an occupied site at rate \(1-\rho_L\); at the right boundary the analogous rates are \(\rho_R\) and \(1-\rho_R\). For the forward experiment, \((\rho_L,\rho_R)=(1,0)\). All rates \(c,d>0\); for the theorem \(c=rh\), \(d=h\), \(r>1\), \(h>0\).

These are precisely the boundary and nearest-neighbor transition prescriptions of the site-disordered open exclusion model in [1] after multiplying all its rates by two and choosing boundary residence and exchange times equal to one. The positive rates are not restricted to one side of the clean boundary rate, allowing both fast and slow interior sites. The finite-state chain is irreducible even with extreme reservoirs: particles can exit at the right after moving rightward, and arbitrary configurations can be built by entries at the left. Therefore each of its two driving orientations has a unique stationary law and strictly positive forward current magnitude.

## Proof
**1. Exact finite-chain rational current.** Label states by \(s=\sum_{i=1}^4 2^{i-1}\eta_i\), so there are sixteen states. Construct the column-generator \(Q(c,d)\) by adding the allowed occupation swaps at their departure-site rates, insertion into vacant site 1 at rate one and deletion from occupied site 4 at rate one. Every column sums to zero. Replace its final row by ones to form \(M(c,d)\). If \(b\) is the vector with final entry one and other entries zero, then the stationary vector satisfies \(M p=b\), and the current is
\[
J_+(c,d)=1-\sum_{s:\,\eta_1(s)=1}p_s.
\]
Reflection exchanges \((c,d)\) and \((d,c)\) while reversing the reservoirs and oriented current. Hence the stated \(\mathcal D_r\) equals the physical forward-plus-reverse stationary current. The Markov-chain tree theorem makes every stationary probability a ratio of positive rooted-tree sums; algebraic denominators can be chosen strictly positive for \(c,d>0\).

**2. Exact numerator and signs.** Exact rational elimination of the above specified sixteen-state linear system gives
\[
\mathcal D_r(h)=-\frac{r(r-1)h\,P_r(h)}{H_r(h)},\qquad H_r(h)>0,
\]
where \(P_r(h)=\sum_{k=0}^{16}p_k(r)h^k\). The complete exact integer arrays defining the seventeen coefficient polynomials are in `COEFFICIENTS.json`; `verify.py` independently reconstructs all of them from the transition generator and verifies the positive rational denominator. Inspection of these explicit polynomials gives, for every \(r>1\),
\[
\begin{array}{c|c}
 k & \operatorname{sgn}p_k(r)\\\hline
 0,1,2,3 & +\\
 4,5,6,7,8,9,10 & -\\
 11 & -\operatorname{sgn}A(r)\\
 12 & -\operatorname{sgn}B(r)\\
 13,14,15,16 & +
\end{array}
\]
with the two exceptional factors
\[
\begin{aligned}
A(r)={}&150r^8+3776r^7+11771r^6-9379r^5-39888r^4\\
&-9379r^3+11771r^2+3776r+150,\\
B(r)={}&141r^8-333r^7-13951r^6-54997r^5-83115r^4\\
&-54997r^3-13951r^2-333r+141.
\end{aligned}
\]
For \(r\ge2\), \(A(r)>0\): after writing \(u=r-2\ge0\), its coefficients in descending powers of \(u\) are exactly
\[
(150,6176,81435,516257,1797862,3563077,3879177,2016856,316490),
\]
all positive. For \(1<r\le2\), \(B(r)<0\): its only positive terms are \(141(r^8+1)\), and \(141(r^8+1)\le141(2r^7+r)<333(r^7+r)\), strictly dominated by two of its negative terms. Thus at \(r\le2\), the coefficient of \(h^{12}\) is positive, while at \(r\ge2\), the coefficient of \(h^{11}\) is negative. Consequently the coefficient sequence of \(P_r\), from low to high degree and ignoring zeros, has exactly two sign changes: initially positive, then negative, then positive, with no possible extra alternation between degrees 11 and 12. By Descartes' rule of signs, \(P_r\) has at most two positive roots counted with multiplicity.

**3. Both roots exist and are simple.** The exact constant and leading terms are
\[
p_0(r)=11664,\qquad p_{16}(r)=3r^6(r+1)^4.
\]
At the physically distinguished scale \(h=1/r\), site 2 matches the clean endpoint hopping rate while site 3 remains slower. Direct substitution in the same exact polynomial gives
\[
P_r(1/r)=-\frac{2}{r^9}T(r)<0,
\]
where
\[
\begin{aligned}
T(r)={}&75600r^9+1221480r^8+4461570r^7+7402041r^6\\
&+6829195r^5+3800385r^4+1306816r^3\\
&+271698r^2+31285r+1530.
\end{aligned}
\]
Every coefficient in \(T\) is positive. Thus \(P_r\) is positive near zero, negative at \(1/r\), and positive for sufficiently large \(h\). The intermediate-value theorem gives at least two distinct positive zeros, one on either side of \(1/r\). The preceding Descartes bound gives exactly two zeros, each with multiplicity one, and the stated sign pattern of \(\mathcal D_r\) follows from the strictly negative prefactor. This completes the proof for every real \(r>1\).

## Verification
Run `python verify.py` with Python 3 and SymPy installed, with `COEFFICIENTS.json` in the same directory. The script reconstructs both exact currents from the full generator, checks normalization and the positive denominator, recomputes all seventeen coefficient polynomials, checks the two exceptional factors and the special-scale identity, and independently solves exact rational stationary chains at three distinct scales. In particular, at \(r=2\) exact rational evaluations show negative polarity for \(h=1/5\), positive polarity for \(h=1\), and negative polarity for \(h=3\). The exact polynomial brackets the first root in \((1/4,1/3)\) and the second in \((2,5/2)\). The arbitrary-parameter theorem follows from the preceding algebraic sign proof, not from numerical sampling.

## Relationship to prior work
Sakai and Akimoto [1] establish the site-disordered, open-reservoir exclusion model; they derive approximate nonlinear current responses, prove a reflection-symmetry obstruction to rectification, and report sample-dependent signs. They do not give a finite-state exact two-reversal theorem under a fixed interior-rate ratio. Their earlier work [2] treats periodic particle-number-conserving dynamics driven by a bulk field, not the present reservoir-driven four-site chain. A separate exact single-defect, four-site local-response computation determines a quadratic coefficient at weak bias, but do not cover two interior rates varied at fixed ratio or the global, fully biased two-threshold classification. Earlier work on rectification of lattice gases in asymmetric ring potentials [3] uses a different geometry and driving protocol. The novelty claim is restricted to the exact two-reversal statement, not to rectification itself or to exact stationary calculations in finite Markov chains.

## Limitations
The result is finite-volume, specifically four sites; no thermodynamic-limit assertion is made. It fixes maximal reservoir density difference and requires the two internal departure rates to change proportionally with fixed ratio \(r>1\). It is not a statement about general boundary densities, random ensembles, monotonicity of the magnitude of rectification, or global dominance of one orientation in larger chains. Its finite-state symbolic calculations are checked exactly, but independent validation and publication-priority review remain outstanding.

## References
[1] I. Sakai and T. Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process*, arXiv:2609.03560v1 (first public 2026-09-03), https://arxiv.org/abs/2609.03560 ; full text https://pdfs.assets.alphaxiv.org/2609.03560v1.pdf . Relevant model and arguments: Sections II, IV–VI and Appendices.

[2] I. Sakai and T. Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316v1 (2025-12-03), https://arxiv.org/abs/2512.03316 ; full text https://pdfs.assets.alphaxiv.org/2512.03316v1.pdf . Relevant model: periodic chain under bulk-field drive.

[3] K. W. Kehr and Z. Koza, *Hopping motion of lattice gases through nonsymmetric potentials under strong bias conditions*, Physical Review E 61, 2319 (2000), DOI:10.1103/PhysRevE.61.2319; ring geometry with bulk bias.
