# Exact Padé positivity horizons for finite directed Markov cycles

## Finding

Let \(P_n\) be the permutation matrix with \((P_n)_{i,i+1\pmod n}=1\), and let \(Q_n=P_n-I_n\). For the two-stage, fourth-order Gauss–Legendre Runge–Kutta end-step map
\[
T_n(h)=r(hQ_n),\qquad r(z)=\frac{12+6z+z^2}{12-6z+z^2},\qquad h\ge0,
\]
the following is an exact entrywise-positivity classification over all integer dimensions \(n\ge2\):

1. For \(n=2,3\), \(T_n(h)\) is row-stochastic for every \(h\ge0\).
2. For each \(n=4,5,6,7\), there is exactly one finite \(H_n>0\) such that \(T_n(h)\) is row-stochastic **if and only if** \(0\le h\le H_n\). Here \(H_n\) is the unique positive root of the polynomial \(F_n\) below.
3. For every \(n\ge8\), \(T_n(h)\) has a negative entry at every sufficiently small positive stepsize (the small-step obstruction is already covered at the general finite-Markov-generator level by earlier work). Moreover, for every \(n\ge4\), the first-neighbor entry is negative at all sufficiently large stepsizes.

The four sharp finite thresholds are defined by
\[
\begin{aligned}
F_4(h)&=h^4-24h^2-72h-72,\\
F_5(h)&=5h^6+30h^5-432h^3-1584h^2-2592h-1728,\\
F_6(h)&=3h^7+26h^6+60h^5-120h^4-1152h^3\\
&\quad-3456h^2-5184h-3456,\\
F_7(h)&=7h^{10}+105h^9+630h^8+1764h^7-21168h^5\\
&\quad-95040h^4-233280h^3-352512h^2-311040h-124416.
\end{aligned}
\]
The root brackets, certified by exact rational sign evaluations, are
\[
\begin{array}{c|c}
n&\text{unique }H_n\text{ belongs to}\\ \hline
4&(6.135720,\;6.135721)\\
5&(4.314322,\;4.314323)\\
6&(3.808010,\;3.808011)\\
7&(3.611919,\;3.611920)
\end{array}
\]
This yields a natural three-regime dimension law: unconditional stochasticity in dimensions two and three, a single sharp positive stepsize window in dimensions four through seven, and failure arbitrarily close to zero in dimensions at least eight.

## Assumptions and scope

Throughout, \(n\in\mathbb Z\), \(n\ge2\), and \(P_n\) is the unit-rate directed cyclic shift as defined above. A row-stochastic matrix means entrywise nonnegative with all row sums exactly one. The generator \(Q_n\) has off-diagonal nonnegative entries and \(Q_n\mathbf1=0\). All claims concern the exact real rational matrix \(T_n(h)\), not floating-point implementation or internal Runge–Kutta stage positivity. The nonnegative step range includes \(h=0\). The first-neighbor entry is indexed by \((0,1)\) with cyclic indices.

## Proof

**Invertibility and mass conservation.** Write \(B_n(h)=I-hQ_n/2+h^2Q_n^2/12\) and \(A_n(h)=I+hQ_n/2+h^2Q_n^2/12\). The scalar denominator \(12-6z+z^2\) has roots \(3\pm i\sqrt3\) with positive real part, while \(Q_n\) has eigenvalues in the closed left half-plane. Thus \(B_n(h)\) is invertible for every real \(h\ge0\), and \(T_n=B_n^{-1}A_n\). Both \(A_n\) and \(B_n\) send \(\mathbf1\) to \(\mathbf1\), so \(T_n\mathbf1=\mathbf1\). By cyclic commutation \(T_n\) is circulant; it suffices to inspect row zero.

**Dimensions two and three.** Direct exact elimination gives row zero for \(n=2\):
\[
\left(\frac{h^2+3}{h^2+3h+3},\frac{3h}{h^2+3h+3}\right),
\]
and for \(n=3\):
\[
\left(\frac{h^2-2h+4}{h^2+2h+4},\frac{8h}{(h+2)(h^2+2h+4)},\frac{4h^2}{(h+2)(h^2+2h+4)}\right).
\]
Every denominator is positive for \(h\ge0\), while \(h^2-2h+4=(h-1)^2+3>0\); hence all entries are nonnegative.

**Dimensions four through seven.** Exact rational elimination for each of these four fixed matrices produces, for the nearest-neighbor entry,
\[
[T_n(h)]_{0,1}=-\frac{c_nhF_n(h)}{D_n(h)},\quad
(c_4,c_5,c_6,c_7)=(3,12,1,24),
\]
where each \(D_n\) is the fully reduced denominator in the rational expression (computed with the accompanying exact symbolic verifier). Each denominator has positive constant term and nonnegative polynomial coefficients, hence \(D_n(h)>0\) for \(h\ge0\). In descending coefficient order, each \(F_n\) has *exactly one sign change* among its nonzero coefficients, negative value at zero, and positive leading coefficient. By Descartes' rule and the intermediate value theorem, it has exactly one positive real root \(H_n\), with \(F_n(h)<0\) for \(0\le h<H_n\) and \(F_n(h)>0\) for \(h>H_n\). The neighboring entry is therefore nonnegative precisely through \(H_n\) and negative beyond it.

It remains to prove that no other entry becomes negative before \(H_n\). For \(n=4,5\), symbolic elimination gives positive denominators as above and a numerator with nonnegative coefficients for every \(j\ne1\), hence \([T_n(h)]_{0,j}\ge0\) for all \(h\ge0\). For \(n=6,7\), write the reduced numerator as \(N_{n,j}(h)\) for \(j\ne1\) and let \(d_{n,j}\) be its degree. For every such numerator, the exact-coefficient polynomial
\[
(1+u)^{d_{n,j}}N_{n,j}\!\left(\frac{4u}{1+u}\right)
\]
has nonnegative coefficients and is not identically zero. Consequently \(N_{n,j}(h)>0\) for all \(0<h<4\). The exact sign \(F_6(4)>0\), \(F_7(4)>0\) implies \(H_6,H_7<4\). Hence all the other entries stay positive throughout \(0<h\le H_n\), including the sharp boundary. At \(h=0\), \(T_n(0)=I\). Exact symbolic elimination and the coefficient-positivity certificates are reconstructed independently in `artifacts/verify.py`, rather than assumed from decimal sampling. This completes the four exact-window claims.

**Small steps in every dimension at least eight.** The Taylor series of the rational stability function begins
\[
r(z)=1+z+\tfrac12z^2+\tfrac16z^3+\tfrac1{24}z^4+\tfrac1{144}z^5+0z^6-\tfrac1{1728}z^7+O(z^8).
\]
For \(n\ge8\), \((Q_n^k)_{0,7}=0\) for \(k<7\), while \((Q_n^7)_{0,7}=1\), since reaching state seven takes at least seven forward cyclic edges. Therefore
\[
[T_n(h)]_{0,7}=-\frac{h^7}{1728}+O_n(h^8)<0
\]
for all sufficiently small positive \(h\). This is a special case of the previously established eight-state Padé positivity obstruction and is included to close the dimension classification, **not as an independently original observation**.

**Large steps in every dimension at least four.** Let \(J=\mathbf1\mathbf1^\mathsf T/n\). The group inverse of \(Q_n=P_n-I\) on its zero-sum range is
\[
X_n=\sum_{j=0}^{n-1}\frac{2j-n+1}{2n}P_n^j,
\]
which obeys \(Q_nX_n=X_nQ_n=I-J\) and \(X_n\mathbf1=0\), by cyclic telescoping. As \(z\to\infty\), \(r(z)=1+12/z+O(z^{-2})\). On the constant mode \(r(0)=1\) and on each nonzero cyclic eigenmode \(r(h\lambda)=1+12/(h\lambda)+O(h^{-2})\), giving
\[
T_n(h)=I+\frac{12}{h}X_n+O_n(h^{-2}),\qquad
[T_n(h)]_{0,1}=-\frac{6(n-3)}{nh}+O_n(h^{-2}).
\]
For \(n\ge4\), the coefficient is strictly negative, proving eventual failure. This complements the exact finite-window computation and establishes the all-dimensional large-step boundary.

## Verification

Run `python artifacts/verify.py` with Python 3 and SymPy. The script builds the actual matrices, performs exact rational simplifications, verifies the neighboring-entry identities and denominator signs, checks each Descartes sign pattern and each root bracket, and establishes the required positivity of every other entry through ordinary coefficients or the exact \(h=4u/(1+u)\) transform. It also verifies the low-order Taylor coefficients and finite-dimensional cases of the group-inverse identity. The recorded run performed 182 exact symbolic/rational assertions and passed. This finite script supports the proof; the claims for all \(n\ge8\) and the large-step all-\(n\) result are proved in the text rather than extrapolated from a finite sweep.

## Relationship to prior work

Nüßlein, Ranocha and Ketcheson (2020, arXiv:2005.06268) study positivity of Runge–Kutta methods with modified weighting strategies, identifying stage/end-step positivity hazards. Blanes, Iserles and Macnamara (2021, arXiv:2102.08242) develop positivity-preserving integrators for graph-Laplacian-type systems. Neither provides the exact four directed-cycle Padé thresholds above.

Zappavigna, Colaneri, Kirkland and Shorten (2012) identify the negative seventh Taylor coefficient of the diagonal Padé map and give higher-dimensional positivity counterexamples for Metzler matrices, but do not classify these conservative directed-cycle end-step transition matrices. A separately published finite-Markov result proves every generator of dimension at most seven has a generator-dependent sufficiently-small positive window and identifies an eight-state pure-birth counterexample. That stronger general small-step statement subsumes our \(n\ge8\) local observation in the appropriate direction; it does **not** imply these globally sharp \(H_4,H_5,H_6,H_7\) or the unconditional two- and three-cycle behavior. A 2026 preprint on rational Fokker–Planck propagators was identifiable from its abstract but not comparably accessible at full-text level; related specialized precedence remains possible.

## Limitations

These are exact-step entrywise claims for a uniform, one-way, finite cyclic Markov generator. They do not imply positivity for general conservative generators of the same size, arbitrary rate inhomogeneity, RK internal stages, nonlinear equations, or implementations with finite-precision arithmetic. The all-dimension small-step observation is not proposed as novel independently of prior general Padé work. The numerical root brackets are rigorously isolated only because the defining polynomials and sign checks are exact, not because decimals by themselves certify positivity.

## References

1. Nüßlein, Ranocha and Ketcheson, “Positivity-preserving Runge-Kutta methods using adaptive weightings,” arXiv:2005.06268, first publicly posted 2020-05-13. https://arxiv.org/abs/2005.06268
2. Blanes, Iserles and Macnamara, “Positivity-preserving methods for ordinary differential equations,” arXiv:2102.08242, first publicly posted 2021-02-16. https://arxiv.org/abs/2102.08242
3. Zappavigna, Colaneri, Kirkland and Shorten, “Essentially negative news about positive systems,” *Linear Algebra and its Applications* 436 (2012), 3425–3442. https://doi.org/10.1016/j.laa.2011.12.021 ; lawful author manuscript https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf
4. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” published mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab
5. Itkin and Kazbek, “Diagonal Frog meets ADI: trading matrix exponentials for rational maps in the Fokker–Planck equation,” arXiv:2608.22703 (2026); relevant as a subsequent comparison, not as the earliest motivating source. https://arxiv.org/abs/2608.22703
