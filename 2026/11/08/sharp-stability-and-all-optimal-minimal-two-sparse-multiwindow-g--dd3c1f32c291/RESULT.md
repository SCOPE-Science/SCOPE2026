# Sharp stability and all optimal minimal two-sparse multiwindow Gabor tomography designs

## Finding
Let \(N\ge3\), let \(m=\lfloor N/2\rfloor\), and let \(g_1,\ldots,g_m\in\mathbb C^N\) be unit vectors, each with exactly two nonzero entries. Set \(T_a f(j)=f(j-a)\), \(M_b f(j)=e^{2\pi i bj/N}f(j)\), and \(W_{a,b}=M_bT_a\). On the real Hilbert space \(\operatorname{Herm}(N)\) with Hilbert--Schmidt norm define the full, labelled intensity lifting
\[
\mathcal A_{\mathbf g}(X)=\left(\operatorname{tr}\big(XW_{a,b}g_rg_r^*W_{a,b}^*\big)\right)_{r=1,\ldots,m;\ a,b\in\mathbb Z_N},
\]
with the ordinary Euclidean norm on the \(mN^2\) real measurements. Every such injective design satisfies the sharp inequality
\[
\boxed{\kappa(\mathcal A_{\mathbf g})\ge 2\sqrt m},
\qquad
\boxed{\max_{\mathbf g}\lambda_{\min}(\mathcal A_{\mathbf g}^*\mathcal A_{\mathbf g})=N/4}.
\]
Both bounds are attained for every \(N\), and the following is the **complete equality classification** (allowing arbitrary global phases, window order, and cyclic translations of individual windows).

Associate with a support pair \(\{u,v\}\) its *unoriented displacement* \(\{v-u,u-v\}\subset\mathbb Z_N\). For any injective minimal-window design these \(m\) classes are exactly the \(m\) distinct nonzero unoriented displacement classes, each occurring once.

If \(N\) is odd, equality holds if and only if **every** window has two entries of equal modulus \(1/\sqrt2\); every relative phase is allowed. If \(N=2m\) is even, equality holds if and only if every window with non-antipodal displacement is equal-modulus, while the antipodal window, written after translation and global phase as
\[
g_{\mathrm{opp}}=\sqrt p\,e_0+\sqrt{1-p}\,e^{i\phi}e_m,
\qquad 0<p<1,
\]
satisfies exactly
\[
\boxed{4p(1-p)\min\{\cos^2\phi,\sin^2\phi\}\ge\tfrac14.}
\]
In particular, \(p=1/2\), \(\phi=\pi/4\) always works. The antipodal powers need not be equal: the equality condition is feasible precisely when \(p(1-p)\ge1/8\), with a corresponding restricted phase range. Every optimal design has
\[
\sigma_{\max}=\sqrt{Nm},\quad \sigma_{\min}=\sqrt N/2,\quad \kappa=2\sqrt m.
\]
For \(N\ge3\), fewer than \(m\) two-sparse windows cannot give injective full Hermitian tomography. This minimal-window threshold itself is previously established; the sharp stability bound and complete equality family above are the subject of the finding.

## Assumptions and scope
All windows have exactly two nonzero complex coordinates and unit Euclidean norm; the measurement family contains all \(N^2\) time--frequency shifts of every window, without rescaling across windows and with multiplicities retained. The operator acts on **all** complex Hermitian \(N\)-by-\(N\) matrices, not just rank-one positive matrices, and uses the full Hilbert--Schmidt norm and raw, unweighted Euclidean measurement norm. An uninvertible design has infinite condition number. Phases refer to the ratio of the second and first nonzero coordinates after translating the antipodal support to \(\{0,m\}\). Different signal-to-noise models or nonunit window weights need not obey the same optimality classification.

## Proof
**Weyl spectral diagonalization.** The normalized Weyl matrices \(W_{u,v}/\sqrt N\) form an orthonormal basis of complex matrices. Conjugating a Weyl matrix by \(W_{a,b}\) multiplies it by a character of \(\mathbb Z_N^2\). The Fourier orthogonality of these characters implies that the frame operator \(\mathcal S_{\mathbf g}=\mathcal A_{\mathbf g}^*\mathcal A_{\mathbf g}\), complex-linearly extended from Hermitian matrices, has eigenvalues, counted with multiplicity,
\[
\Lambda(u,v)=N\sum_{r=1}^{m}|\langle g_r,M_vT_u g_r\rangle|^2,
\quad (u,v)\in\mathbb Z_N^2.\tag{1}
\]
A direct derivation is to expand \(g_rg_r^*\) in the Weyl basis, average its rank-one operator outer products over conjugation, and use character orthogonality; no assumption of informational completeness is needed. The resulting operator preserves adjoints, so its complex-matrix eigenvalues give the same spectral multiset on the real Hermitian space. Equation (1) is consistent with the published one-window Gabor-POVM Gram spectrum and extends by summing the independent window contributions.

**Support-class necessity and universal upper eigenvalue.** For a two-point window with displacement \(d\), its ambiguity coefficient \(\langle g,M_vT_u g\rangle\) vanishes unless \(u\in\{0,d,-d\}\). Therefore injectivity forces all \(m\) nonzero unoriented displacement classes to be represented, exactly once if the number of windows is \(m\). In particular, no fewer than \(m\) such windows span the entire matrix space. For every unit window, the absolute value of its ambiguity coefficient is at most one. The eigenvalue at \((0,0)\) equals \(Nm\), so
\[
\lambda_{\max}(\mathcal S_{\mathbf g})=Nm.\tag{2}
\]

**Universal lower-frame obstruction.** There exists a non-antipodal displacement class for every \(N\ge3\). Its unique window has entries of squared moduli \(p\) and \(1-p\). At its two nonzero lag rows \(u=\pm d\), exactly one support-overlap term survives, and for every \(v\) equation (1) reads
\[
\Lambda(\pm d,v)=Np(1-p)\le N/4.\tag{3}
\]
Thus \(\lambda_{\min}\le N/4\); equations (2)--(3) force \(\kappa^2\ge4m\). Furthermore, equality **forces** both entries of every non-antipodal window to have equal modulus, since their lag rows are distinct and occur in no other window.

**Odd-order equality.** Write \(N=2m+1\) and take one balanced window at each representative distance \(d=1,\ldots,m\), with arbitrary relative phase. For each nonzero lag row, (3) yields precisely \(N/4\), repeated \(N(N-1)\) times. The zero-lag ambiguity of a balanced window is \((1+e^{2\pi i dv/N})/2\) up to a harmless phase; its squared modulus is \((1+\cos(2\pi dv/N))/2\). Summing over \(d\) and using
\[
\sum_{d=1}^{m}\cos(2\pi dv/N)=-1/2\quad(v\ne0),
\]
gives the complete spectrum
\[
\operatorname{spec}(\mathcal S_{\mathbf g})=
\{Nm\}^{[1]}\cup\{N(N-2)/4\}^{[N-1]}\cup\{N/4\}^{[N(N-1)]}.\tag{4}
\]
Here \(\{z\}^{[r]}\) means an eigenvalue with multiplicity \(r\); coincident values are combined. Since \(N(N-2)/4\ge N/4\), equality holds. Necessity of balance follows from (3), and phases never enter (3)--(4). For \(N=3\), all eight nonconstant eigenvalues in (4) coincide at \(3/4\), recovering the known optimal qutrit tight-measurement spectrum as a boundary instance.

**Even-order equality and the flexible antipodal class.** Write \(N=2m\), where \(m\ge2\). Balance all \(m-1\) non-antipodal windows; write the last, antipodal window in the displayed \((p,\phi)\) form. The non-antipodal lag rows contribute \(N/4\), repeated \(N(N-2)\) times. The antipodal lag \(u=m\) has
\[
\big|\langle g_{\mathrm{opp}},M_vT_mg_{\mathrm{opp}}\rangle\big|^2=
\begin{cases}4p(1-p)\cos^2\phi,&v\text{ even},\\4p(1-p)\sin^2\phi,&v\text{ odd}.
\end{cases}\tag{5}
\]
On the remaining zero-lag row, elementary finite geometric sums give one eigenvalue \(Nm\) at \(v=0\), an eigenvalue \(Nm/2\) for each of the \(m-1\) nonzero even \(v\), and \(N[(m-1)/2+(2p-1)^2]\) for each of the \(m\) odd \(v\). All latter eigenvalues are at least \(N/2\). Thus the full spectral multiset is
\[
\begin{split}
\{Nm\}^{[1]}&\cup\{Nm/2\}^{[m-1]}
\cup\{N[(m-1)/2+(2p-1)^2]\}^{[m]}\\
&\cup\{N/4\}^{[N(N-2)]}
\cup\{4Np(1-p)\cos^2\phi\}^{[m]}
\cup\{4Np(1-p)\sin^2\phi\}^{[m]}.\tag{6}
\end{split}
\]
The minimum equals \(N/4\) if and only if both values in (5), multiplied by \(N\), are at least \(N/4\), which is exactly the boxed antipodal inequality. This proves both sufficiency and necessity and establishes all sharp constants and equality cases. The feasible range \(p(1-p)\ge1/8\) follows by maximizing \(\min(\sin^2\phi,\cos^2\phi)\) over \(\phi\), whose maximum is \(1/2\). The proof holds for every allowed dimension without numerical extrapolation.

## Verification
The accompanying standalone `verify_sparse_optimal.py` constructs, directly from the projectors, the real measurement matrix in a Hilbert--Schmidt-orthonormal basis of Hermitian matrices. It compares its entire \(N^2\)-term singular-value-square spectrum to (4) and (6) for all integer \(3\le N\le10\), for 32 configurations incorporating balanced and nonbalanced antipodal powers and several window phases. It checks that optimal examples attain both sharp eigenvalues and the condition number. Reproduce with `python verify_sparse_optimal.py` using Python 3 and NumPy, optionally with `OPENBLAS_NUM_THREADS=1`. This is a finite numerical cross-check; the all-dimension certificate consists of equations (1)--(6) and the finite-character identities in the proof.

## Relationship to prior work
Goldberger, Kang and Okoudjou [1, Theorem 2] established the **general single-window** Gabor projector Gram-spectrum identity. The Weyl diagonalization (1), by summing window contributions, is treated here as an established ingredient, not as a novel spectral method. Han, Hu, Liu and Wang [2] introduced multi-window quantum-injectivity criteria and reported a quantitative stability result for a metric. Bartusel [3] analyzed the sparse-window STFT ambiguity and phase-retrieval mechanisms on cyclic groups. Salanevich [4] constructed efficient multi-window phase-retrieval systems for pure states, with a different sampling objective. The publicly available mathematical finding [5] already determines the **minimum number** of two-sparse complete Gabor windows and is credited for that threshold; its qualitative capacity conclusion alone does not supply sharp condition numbers or a complete equality classification. The proposed new claim is precisely the optimum \(2\sqrt{\lfloor N/2\rfloor}\) and its entire odd/even equality family under the stated normalization, including the nonbalanced antipodal optimizers. It is an optimization over all minimal-window designs, rather than a restatement of one-window spectral identities or rank criteria.

## Limitations
Only full time--frequency orbits, exactly two nonzero coordinates per unit window, and the minimum injective window budget are treated. The condition number is for the linear map on all Hermitian matrices with unweighted raw intensity coordinates; it is not a global inverse-Lipschitz constant for nonlinear phase retrieval and does not guarantee statistical optimality under shot noise or correlated noise. Inaccessible full text of [2] leaves a historical-priority risk concerning its general quantitative-stability metric; no exact two-sparse optimal-design classification was located in the accessible material. A broad published frame-spectrum formula is an important proof input, so the novelty resides only in the constrained sharp optimizer and its full equality classification. Independent mathematical validation has not been performed.

## References
[1] A. Goldberger, S. Kang, K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in* \(\mathbb C^d\), arXiv:2106.01509v1, first public 2021-06-02, https://arxiv.org/html/2106.01509v1 ; Theorem 2 and Section 2 inspected.

[2] D. Han, Q. Hu, R. Liu, H. Wang, *Quantum injectivity of multi-window Gabor frames in finite dimensions*, *Annals of Functional Analysis* 13 (2022), article 59, DOI 10.1007/s43034-022-00208-2, first online 2022-08-05, https://doi.org/10.1007/s43034-022-00208-2 ; accessible abstract and bibliographic material only.

[3] D. Bartusel, *Injectivity conditions for STFT phase retrieval on* \(\mathbb Z\), \(\mathbb Z_d\) *and* \(\mathbb R^d\), arXiv:2206.06729v1, first public 2022-06-14, https://arxiv.org/html/2206.06729v1 ; finite-cyclic Sections 4.2--4.3 inspected.

[4] P. Salanevich, *Injectivity of Multi-window Gabor Phase Retrieval*, arXiv:2307.00834v1, first public 2023-07-03, https://arxiv.org/abs/2307.00834 ; Introduction and Section II inspected.

[5] *Sharp operator-span capacity of two-sparse multi-window Gabor systems*, openly available 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-operator-span-capacity-of-two-sparse-multi-window-gabor-sy--b553eeb756ed ; complete stated capacity theorem and proof inspected.

[6] *Exact local conditioning and optimal weighting for two-tap cyclic spectrograms*, openly available 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-local-conditioning-and-optimal-weighting-for-two-tap-cycli--52be44b25eaa ; complete stated local-Jacobian theorem and proof inspected, with a distinct signal-space target and stability metric.
