# Four-per-degree phaseless sampling on a noncircular ellipse and exact angular resonance

## Finding

**Theorem (finite ellipse sampling).** Fix an integer \(d\ge1\), real \(a>b>0\), a complex center \(z_0\), and a rotation \(e^{i\varphi}\). Parametrize the noncircular ellipse by
\[
 Z(w)=z_0+e^{i\varphi}(aw+bw^{-1}),\qquad |w|=1.
\]
For any \(4d\) distinct unit numbers \(w_1,\ldots,w_{4d}\) satisfying \(\prod_{j=1}^{4d}w_j\ne1\), the intensities \(\bigl(|p(Z(w_j))|^2\bigr)_{j=1}^{4d}\) determine **every** complex polynomial \(p\) of degree at most \(d\), up to a single unimodular scalar. There is an explicit linear interpolation formula recovering the entire angular intensity profile.

**Exact equispaced-grid dichotomy.** If \(w_j=\exp(i(\theta_0+2\pi j/(4d)))\), \(0\le j<4d\), then these samples are phaselessly injective for all degree-\(d\) polynomials **if and only if** \(\exp(4di\theta_0)\ne-1\). For every exceptional offset, an explicit nonconstant degree-\(d\) polynomial and a constant polynomial have the same intensities at every node.

**Optimality of complete-profile linear interpolation.** The real-linear span of the degree-\(d\) intensity profiles on the ellipse has dimension exactly \(4d\). Thus fewer than \(4d\) samples cannot linearly reconstruct **every full profile**. This is not a universal lower bound for arbitrary nonlinear phaseless reconstruction.

## Assumptions and scope

The ellipse is noncircular and nondegenerate: \(a>b>0\); the limit \(b=0\) is a circle and \(a=b\) is a segment, neither covered. Its semiaxes are \(a+b\) and \(a-b\). The angular parameters are distinct modulo \(2\pi\). Two polynomials are equivalent only when one is a common complex multiple of modulus one of the other. The data are *squared* magnitudes. All results hold uniformly as a logical statement for every integer \(d\ge1\); no uniform noise condition number is claimed. Translation and rotation reduce the proof to \(Z(w)=aw+bw^{-1}\), replacing \(p(z)\) by \(p(z_0+e^{i\varphi}z)\) without changing its degree.

## Proof

**Step 1: exact Laurent structure and interpolation.** Write \(p(z)=\sum_{k=0}^dc_kz^k\), allowing \(c_d=0\), and \(p^\#(z)=\sum_{k=0}^d\overline{c_k}z^k\). Set \(\Phi(w)=aw+bw^{-1}\), \(\Psi(w)=bw+aw^{-1}\), and
\[
 H_p(w)=p(\Phi(w))p^\#(\Psi(w)),\qquad P_p(w)=w^{2d}H_p(w).
\]
For \(|w|=1\), \(\Psi(w)=\overline{\Phi(w)}\) and \(H_p(w)=|p(\Phi(w))|^2\). As a Laurent polynomial, \(H_p\) has exponents between \(-2d\) and \(2d\). The only contribution to either extreme exponent is the leading-degree product \(c_d\overline{c_d}\Phi^d\Psi^d\), so
\[
 [w^{4d}]P_p=[w^0]P_p=(ab)^d|c_d|^2.
\]
For measured values \(h_j=|p(\Phi(w_j))|^2\), let \(P_0\) denote the **unique polynomial of degree at most \(4d-1\)** satisfying \(P_0(w_j)=w_j^{2d}h_j\), obtainable by ordinary Lagrange interpolation. Put \(Q(w)=\prod_{j=1}^{4d}(w-w_j)\). Every degree-\(4d\) polynomial interpolating the measurements is \(P_0+C Q\). Since \(4d\) is even, \(Q(0)=\prod_jw_j\). Equality of the constant and leading coefficients forces
\[
 C=\frac{P_0(0)}{1-\prod_jw_j},\qquad P_p=P_0+C Q,\qquad H_p(w)=w^{-2d}P_p(w).
\]
The denominator is nonzero by hypothesis, so all angular intensities are uniquely recovered. In particular, equality of the measured intensities for two polynomials implies equality on the entire ellipse.

**Step 2: rigidity of the full ellipse profile.** Suppose \(p\) and \(q\) are nonzero and satisfy \(H_p=H_q\). In the rational-function field \(\mathbb C(w)\), form
\[
 R(z)=p(z)/q(z),\qquad S(z)=p^\#(z)/q^\#(z).
\]
Then \(A(w)=R(\Phi(w))\) and \(B(w)=S(\Psi(w))\) satisfy \(A(w)B(w)=1\). The rational function \(A\) is fixed by the deck involution \(\tau(w)=b/(aw)\), since \(\Phi(\tau(w))=\Phi(w)\). As \(A=B^{-1}\), it is also fixed by \(\sigma(w)=a/(bw)\), since \(\Psi(\sigma(w))=\Psi(w)\). Consequently \(A\) is invariant under \(\tau\circ\sigma(w)=(b/a)^2w\). A rational function invariant under multiplication by a positive constant strictly between zero and one must be constant: a nonzero finite zero or pole would generate infinitely many such zeros or poles; the remaining possible monomial has exponent zero by scaling invariance. Thus \(A\), hence \(R\), is constant and \(p=\lambda q\). Equality of intensities at nonzero points gives \(|\lambda|=1\). If one input polynomial is zero, its recovered intensity is zero on the ellipse; a nonzero polynomial cannot vanish there, so both are zero.

**Step 3: sharp resonance of equispaced grids.** For \(w_j=\exp(i(\theta_0+2\pi j/(4d)))\), \(\prod_jw_j=-\exp(4di\theta_0)\). The good offsets are therefore precisely \(\exp(4di\theta_0)\ne-1\) by Steps 1–2. For a bad offset define the **generalized Chebyshev polynomials** by
\[
 F_0(z)=2,\quad F_1(z)=z,\quad F_m(z)=zF_{m-1}(z)-abF_{m-2}(z)\ (m\ge2).
\]
Induction yields \(F_d(aw+bw^{-1})=a^dw^d+b^dw^{-d}\). Hence for \(|w|=1\),
\[
 |F_d(\Phi(w))|^2=a^{2d}+b^{2d}+(ab)^d(w^{2d}+w^{-2d}).
\]
When \(\exp(4di\theta_0)=-1\), \(w_j^{2d}=\pm i\) for all sample nodes and the last parenthesis vanishes. The nonconstant polynomial \(F_d\) and the constant \(\sqrt{a^{2d}+b^{2d}}\) thus have identical measured intensities but cannot differ by a unimodular scalar. This proves both directions of the dichotomy, in every degree.

**Step 4: exact dimension of the intensity-profile span.** By polarization, the real span of \(|p(\Phi(w))|^2\) contains the real and imaginary parts of \(\Phi(w)^j\Psi(w)^k\), \(0\le j,k\le d\). Every intensity is a real trigonometric polynomial of degree at most \(2d\) whose top sine coefficient vanishes, since the two extreme Laurent coefficients are equal and real; hence the span has dimension at most \(1+2(2d-1)+1=4d\). Conversely, take each harmonic order \(\ell=1,\ldots,2d-1\) and choose \(j+k=\ell\), \(0\le j,k\le d\), with \(j\ne k\). Its positive and negative extreme coefficients are respectively \(a^jb^k\) and \(b^ja^k\), which have unequal magnitudes because \(a>b>0\). Its real and imaginary parts therefore yield two independent cosine/sine components at harmonic \(\ell\), modulo lower harmonics. The constant is supplied by \(|1|^2\); harmonic \(2d\) cosine is supplied by \(|\Phi|^{2d}\), with top coefficient \((ab)^d\ne0\). Triangular elimination by harmonic order spans all \(4d\) available modes. A linear map from a \(4d\)-dimensional real function space to fewer than \(4d\) point values cannot be injective. (At exceptional equispaced grids the actual two non-equivalent polynomial witnesses in Step 3 are stronger than this dimension obstruction.)

## Verification

The file `ellipse_phase_checker.py` checks the generalized Chebyshev identity and its intensity polynomial exactly for rational noncircular ellipses and degrees \(1\) through \(6\), and tests interpolation, lifted-intensity design rank, and the exceptional-grid witness numerically in degrees \(1\) through \(4\). It prints `ELLIPSE_PHASE_CHECK_PASS 64` on success. The analytical rational-involution proof and the dimension argument establish every degree; the finite checks are not offered as infinite proof. One can reproduce them using Python with NumPy and SymPy by running `python ellipse_phase_checker.py`.

## Relationship to prior work

Chalendar and Partington, *Phase retrieval on circles and lines* (arXiv:2403.16255), analyze analytic-function uniqueness on pairs of lines and circles, and single-circle ambiguity, but not a finite phaseless sampling criterion for one noncircular ellipse. Pohl, Li, and Boche, *Phase retrieval in spaces of analytic functions on the unit disk* (2017), give a distinct four-per-degree two-concentric-circle polynomial measurement geometry. Wellershoff, *Phase retrieval of entire functions and its implications for Gabor phase retrieval* (arXiv:2202.03733), and Liehr, *Arithmetic progressions and holomorphic phase retrieval* (arXiv:2308.05722), examine holomorphic phase retrieval on line-based geometries rather than a single ellipse. The count \(4d\) is not asserted to be new in general; the new subject is the complete noncircular-ellipse criterion, interpolation formula, and good/bad angular-shift dichotomy. These are not formal corollaries of the inspected multiple-circle or multiple-line hypotheses. A general curve theorem not identified in this literature search could subsume the result; that is a historical priority risk.

## Limitations

The theorem does not give a uniform condition number as nodes coalesce or as the ellipse tends to a circle or segment. Linear interpolation recovers the full profile and leaves a possible nonlinear polynomial factorization stage; no noise-optimal factorization algorithm is supplied. The dimension lower bound is for **linear full-profile interpolation**, not for all conceivable nonlinear phase-retrieval schemes. Equispaced resonance is characterized exactly; outside equispaced grids, the product condition is a sufficient criterion and no necessity assertion is made. No claim about general holomorphic functions, higher-dimensional manifolds, or arbitrary real algebraic curves is implied.

## References

1. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (first public 2024-03-24), https://arxiv.org/abs/2403.16255.
2. V. Pohl, N. Li and H. Boche, *Phase retrieval in spaces of analytic functions on the unit disk*, SampTA 2017, DOI:10.1109/SAMPTA.2017.8024411.
3. M. Wellershoff, *Phase retrieval of entire functions and its implications for Gabor phase retrieval*, arXiv:2202.03733, https://arxiv.org/abs/2202.03733.
4. L. Liehr, *Arithmetic progressions and holomorphic phase retrieval*, arXiv:2308.05722, https://arxiv.org/abs/2308.05722.
