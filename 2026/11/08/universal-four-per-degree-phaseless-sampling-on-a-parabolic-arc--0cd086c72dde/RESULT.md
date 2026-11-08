# Universal four-per-degree phaseless sampling on a parabolic arc

## Finding

**Theorem (arbitrary-node parabolic sampling).** Fix an integer \(d\ge1\). Let \(t_1,\ldots,t_{4d}\in\mathbb R\) be pairwise distinct and assume
\[
\sum_{j=1}^{4d}t_j\ne0.
\]
For every complex polynomial \(p\) of degree at most \(d\), the \(4d\) real numbers
\[
y_j=\left|p(t_j+i t_j^2)\right|^2,\qquad 1\le j\le4d,
\]
determine \(p\) up to multiplication by a constant of modulus one. Every choice of \(4d\) distinct **positive** parameters satisfies the condition, including parameters lying in an arbitrarily short positive interval.

More precisely, the measurements determine by a single invertible real linear system the complete univariate intensity polynomial
\[
I_p(T)=p(T+iT^2)\,p^*(T-iT^2),\qquad
p^*(z)=\overline{p(\overline z)},
\]
whose degree is at most \(4d\) and whose \(T^{4d-1}\) coefficient vanishes. This full intensity polynomial in turn determines the polynomial's global phase class.

For \(d=1\), the nonzero-sum hypothesis is also *necessary* for four distinct real parameters to identify every linear polynomial: whenever their sum vanishes, there exist two non-phase-equivalent linear polynomials having the same four squared magnitudes. No necessity claim is made for degrees greater than one.

## Assumptions and scope

The unknown is a complex polynomial \(p(z)=\sum_{k=0}^{d}a_kz^k\) and the observations are exact pointwise squared absolute values, without derivative samples, additional arcs, or adaptations to \(p\). All \(t_j\) are real and known. The parabola is the image of \(\phi(T)=T+iT^2\) on real \(T\); its real coordinate makes the sites distinct. The zero polynomial is allowed and is determined uniquely. Polynomial degree may be less than \(d\).

The assertion is deterministic for **every** permitted set of nodes; it is not a genericity statement. For numerical data the conditioning depends on the chosen nodes, and no uniform lower bound over all admissible node sets is claimed.

## Proof

**Step 1: The missing penultimate intensity coefficient.** Put \(\phi(T)=T+iT^2\) and \(\psi(T)=T-iT^2\). For real \(T\), \(\psi(T)=\overline{\phi(T)}\). With \(p^*(z)=\overline{p(\overline z)}\), the polynomial
\[
I_p(T)=p(\phi(T))p^*(\psi(T))
\]
has real coefficients because its values are real on the real axis. It has degree at most \(4d\). Every term \(a_k\overline{a_l}\phi(T)^k\psi(T)^l\) except \(k=l=d\) has total degree at most \(4d-2\): indeed \(k+l\le2d-1\) for the other pairs. The remaining term is
\[
|a_d|^2\phi(T)^d\psi(T)^d
=|a_d|^2(T^2+T^4)^d,
\]
which has only even degrees. Therefore
\[
[T^{4d-1}]I_p(T)=0.
\]
This also holds when the leading coefficient vanishes.

**Step 2: Exact interpolation from arbitrary admissible nodes.** Write \(N=4d\). The intensity lies in the \(N\)-dimensional real vector space
\[
\mathcal V_N=\operatorname{span}_{\mathbb R}\{1,T,T^2,\ldots,T^{N-2},T^N\}.
\]
The \(N\times N\) evaluation matrix is
\[
V=\bigl(t_j^{e_k}\bigr)_{1\le j,k\le N},
\qquad(e_1,\ldots,e_N)=(0,1,\ldots,N-2,N).
\]
Its generalized Vandermonde determinant is
\[
\det V=\left(\sum_{j=1}^{N}t_j\right)
\prod_{1\le i<j\le N}(t_j-t_i).
\]
For completeness, the determinant is alternating in the nodes, so it is divisible by the usual Vandermonde product. Its quotient is a symmetric homogeneous polynomial of degree one, hence a multiple of the node sum. Comparing the coefficient of \(t_N^N\) identifies the multiple as one. Thus \(V\) is invertible under exactly the stated sufficient node hypotheses. Solving \(V\boldsymbol c=\boldsymbol y\) gives every coefficient of \(I_p\).

**Step 3: A single parabolic arc has no nonconstant rational modulus-one quotient.** Suppose \(I_p=I_q\) for two nonzero complex polynomials of degree at most \(d\). In the rational-function field \(\mathbb C(T)\), define \(R(z)=p(z)/q(z)\) and \(R^*(z)=p^*(z)/q^*(z)\). The intensity identity yields
\[
F(T):=R(\phi(T))=\frac1{R^*(\psi(T))}.
\]
These are identities of rational functions, so poles and zeros pose no problem. The quadratic maps satisfy the exact reflection identities
\[
\phi(i-T)=\phi(T),\qquad
\psi(-i-T)=\psi(T).
\]
Using the first expression for \(F\), we obtain \(F(i-T)=F(T)\); using the second, \(F(-i-T)=F(T)\). Composing the two reflections gives
\[
F(T+2i)=F(T).
\]
A rational function on \(\mathbb C\) with a nonzero period is constant: a finite pole would have infinitely many translates, impossible for a rational function; hence it is a polynomial, and a nonconstant polynomial has no nonzero period. Therefore \(F\) is constant. The polynomial \(\phi\) maps \(\mathbb C\) onto \(\mathbb C\), so \(R\) itself is constant. We have \(p=cq\). Inserting into the intensity equality gives \(|c|=1\).

If one polynomial is zero and all its observations agree with another polynomial \(q\), then \(q\) vanishes at the \(4d\) distinct complex sampling points. Since \(4d>d\), this forces \(q=0\). This completes phase retrieval in all cases.

**Step 4: Sharp node-sum boundary for \(d=1\).** When \(d=1\), every intensity polynomial has the form \(c_0+c_1T+c_2T^2+c_4T^4\), and the map from Hermitian \(2\times2\) matrices \(H\) to
\[
(1,\overline{\phi(T)})H(1,\phi(T))^{\mathsf T}
\]
is a real-linear isomorphism onto this four-dimensional space (its four coefficients separately recover the four real Hermitian entries). For four distinct nodes with zero sum the generalized Vandermonde is singular, so there is a nonzero Hermitian \(H\) whose associated real polynomial vanishes at all four nodes. Such an \(H\) cannot be positive or negative semidefinite: four distinct vectors \((1,\phi(t_j))\) span \(\mathbb C^2\), and a nonzero semidefinite form cannot vanish on their span. Thus \(H\) is indefinite and admits a spectral decomposition \(H=aa^*-bb^*\) with nonzero \(a,b\in\mathbb C^2\), yielding the required distinct polynomial intensity representations. They are not unimodular multiples because \(H\ne0\).

For example, at \(t=-3,-1,1,3\), take
\[
H=\begin{pmatrix}9&11i/2\\-11i/2&1\end{pmatrix},
\qquad \det H=-85/4<0.
\]
Its quadratic form along the parabola equals
\[
(1,\overline{\phi(T)})H(1,\phi(T))^{\mathsf T}
=(T^2-1)(T^2-9),
\]
which vanishes at the four nodes, explicitly certifying ambiguity.

**Step 5: Stability for fixed nodes.** For the coefficient vector \(a\in\mathbb C^{d+1}\), let \(\mathcal M(aa^*)\) denote the vector of squared magnitudes. Extend \(\mathcal M\) linearly to Hermitian matrices through the rank-one evaluation forms. Step 3 proves that the kernel of \(\mathcal M\) contains no nonzero difference \(aa^*-bb^*\). The kernel also contains no nonzero positive or negative semidefinite matrix, because the evaluation vectors span \(\mathbb C^{d+1}\). Every Hermitian matrix of rank at most two is either semidefinite or a difference of two rank-one positive semidefinite matrices. Hence the kernel contains no nonzero Hermitian matrix of rank at most two. By compactness,
\[
\sigma_{\boldsymbol t}:=
\min_{\substack{H=H^*,\ \operatorname{rank}H\le2\\ \|H\|_F=1}}
\|\mathcal M(H)\|_2>0,
\]
and consequently
\[
\bigl\|\bigl(|p(\phi(t_j))|^2-|q(\phi(t_j))|^2\bigr)_{j=1}^{4d}\bigr\|_2
\ge\sigma_{\boldsymbol t}\|aa^*-bb^*\|_F.
\]
This is a finite-dimensional fixed-design stability statement; \(\sigma_{\boldsymbol t}\) can deteriorate under clustering or as the node sum tends to zero.

## Verification

The supplied `verify.py` runs exact SymPy calculations for degrees \(1,2,3,4\), using deterministic complex Gaussian-integer coefficients and distinct positive integer nodes. It verifies the missing \(T^{4d-1}\) coefficient, the generalized Vandermonde determinant, and exact recovery of the complete intensity polynomial. It also verifies the displayed indefinite Hermitian obstruction for the symmetric four-node set. The expected output is `PARABOLIC_PHASE_RETRIEVAL_EXACT_CHECKS_PASS 22`. These are finite checks; Steps 1–5 are the proofs for all degrees and all admissible real nodes. The checker has no internet access or external files apart from its SymPy dependency.

## Relationship to prior work

Pohl, Li and Boche (2017, presentation slides 13--18) obtain a four-per-degree design using two concentric circles, not arbitrary sites on a single parabolic arc. Przybyłek and Siedlecki (2019, Theorem 4.2) construct nonadaptive phase retrieval of a degree-\(d\) complex polynomial using \((2d+1)^2\) intensity measurements distributed across multiple radii and angles. Their construction does not imply the present all-node theorem with \(4d\) observations confined to a single connected parabola. Liehr (2023, Theorem 1.1) studies phase uniqueness of much larger spaces of entire functions on unions of parallel lines indexed by arithmetic-progression conditions; this does not give a finite all-node quadratic-arc interpolation identity. Chalendar and Partington (2024, Theorem 2.1 and §2) give line-intersection and circle-based uniqueness results for holomorphic functions, as well as finite samples on a circle under additional hypotheses; these are not the single-parabola finite theorem. General dimension-based phase retrieval criteria do not establish that **every** permitted parabolic node tuple is injective.

The interpolation determinant and the rational-periodicity argument are the two substantive additional ingredients. The result concerns exact finite-dimensional polynomial recovery, not arbitrary holomorphic functions. The possibility of implicit coverage by other algebraic-curve or rational-reflection results remains a historical-priority risk.

## Limitations

The node-sum condition is sufficient for every degree and necessary only in the linear case as proved; the case of zero-sum node configurations at degree at least two is not classified here. The four-per-degree count is not asserted to be information-theoretically minimal for all polynomial degrees or arbitrary complex measurement frames. Full-intensity interpolation is explicit, while extraction of coefficient phases from it can require polynomial factorization or finite nonlinear algebra. The theorem assumes exact observations; no uniform stability constant over all admissible node sets is claimed. General holomorphic/meromorphic signals and other algebraic arcs are outside the scope.

## References

1. M. R. Przybyłek and P. Siedlecki, *A note on the complexity of a phaseless polynomial interpolation*, arXiv:1907.09371 (first posted 2019-07-22), §4 and Theorem 4.2. https://arxiv.org/abs/1907.09371
2. L. Liehr, *Arithmetic progressions and holomorphic phase retrieval*, arXiv:2308.05722 (first posted 2023-08-10), Theorem 1.1. https://arxiv.org/abs/2308.05722
3. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (first posted 2024-03-24), §2, Theorems 2.1 and 2.11. https://arxiv.org/abs/2403.16255
4. V. Pohl, N. Li and H. Boche, *Phase retrieval in spaces of analytic functions on the unit disk*, SampTA 2017; publicly accessible author presentation, slides 13--18. https://www.ce.cit.tum.de/fileadmin/w00cgn/lti/pdf/vortraege/Pohl-Phase_Retrieval_in_Spaces_of_Analytic_Functions_on_the_Unit_Disk.pdf
5. F. J. Király and M. Ehler, *The algebraic approach to phase retrieval and explicit inversion at the identifiability threshold*, arXiv:1402.4053 (first posted 2014-02-17), algebraic background. https://arxiv.org/abs/1402.4053
