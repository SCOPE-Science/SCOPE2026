# Three rank phases in principal-unit orbits of cubic matrix radicals

## Finding

Let \(q\ge2\) be a prime power, \(m\ge1\), and let
\[
J_m=tM_m(\mathbb F_q)[t]/(t^3)
=\{tC+t^2D:C,D\in M_m(\mathbb F_q)\}.
\]
Its circle group \(G_m=(J_m,\circ)\) has \(x\circ y=x+y+xy\); its left brace action is \(\lambda_x(y)=y+xy\). Independently, the principal-unit group \(1+J_m\) acts on \(J_m\) from both sides, with the two-sided action \((g,h)\cdot y=gyh^{-1}\) for \((g,h)\in(1+J_m)^2\). Both actions preserve the leading matrix \(C\) in \(y=tC+t^2D\).

For \(0\le r\le m\), put
\[
N_{m,r}(q)=\frac{\prod_{i=0}^{r-1}(q^m-q^i)^2}{\prod_{i=0}^{r-1}(q^r-q^i)},\qquad N_{m,0}(q)=1.
\]
Then the exact numbers of **distinct orbits** having leading coefficient of rank \(r\) are
\[
\boxed{L_{m,r}=N_{m,r}(q)q^{m(m-r)},\qquad T_{m,r}=N_{m,r}(q)q^{(m-r)^2}.}
\]
Here \(L\) denotes the left/\(\lambda\) action, and \(T\) the two-sided action. Every orbit in these respective strata has size exactly \(q^{mr}\) and \(q^{2mr-r^2}\). In particular, these formulas include all singleton orbits with \(C=0\), and every \(m\ge1\).

Fix \(q\) and let \(m\to\infty\). Three intrinsically natural sampling conventions have three different limiting **leading-matrix rank laws**:

* Uniformly sample an element of \(J_m\): \(\operatorname{rank}(C)/m\to1\) in probability.
* Uniformly sample a distinct left/\(\lambda\) orbit: \(\operatorname{rank}(C)/m\to1/2\), with a parity-dependent discrete-Gaussian fluctuation of bounded order.
* Uniformly sample a distinct two-sided principal-unit orbit: \(\operatorname{rank}(C)/m\Rightarrow\operatorname{Uniform}[0,1]\), with total-variation error \(O_q(m^{-1})\) relative to the uniform distribution on \(\{0,1,\ldots,m\}\).

More precisely, write \(\epsilon=m\bmod2\) and \(\Theta_\epsilon(q)=\sum_{j\in\mathbb Z+\epsilon/2}q^{-j^2}\). If \(R_L\) is the leading rank of a uniformly sampled left orbit, then
\[
\left\|\mathcal L(R_L-m/2)-\left(\frac{q^{-j^2}}{\Theta_\epsilon(q)}\right)_{j\in\mathbb Z+\epsilon/2}\right\|_{\mathrm{TV}}=O_q(q^{-m/4}).
\]
If \(R_T\) is the rank of a uniformly sampled two-sided orbit, then
\[
\left\|\mathcal L(R_T)-\operatorname{Uniform}\{0,1,\ldots,m\}\right\|_{\mathrm{TV}}=O_q(m^{-1}).
\]
The orbit totals have the asymptotics
\[
\boxed{\sum_r L_{m,r}=\frac{q^{5m^2/4}\Theta_\epsilon(q)}{P_\infty(q)}(1+O_q(q^{-m/4})),\qquad
\sum_r T_{m,r}=\frac{(m+1)q^{m^2}}{P_\infty(q)}(1+O_q(m^{-1})),}
\]
where \(P_\infty(q)=\prod_{i=1}^\infty(1-q^{-i})\).

One further measurable distinction is that the base-\(q\) logarithm of a uniformly chosen two-sided orbit size, divided by \(m^2\), converges in distribution to \(2U-U^2\), with \(U\sim\operatorname{Uniform}[0,1]\), hence its limiting expectation is \(2/3\). For uniformly sampled left orbits the analogous normalized logarithm converges to \(1/2\); for uniformly sampled **elements** and their left-orbit sizes it converges to \(1\). Thus the three sampling models exhibit a point concentration, a half-rank discrete-Gaussian phase, and a continuum-uniform rank phase, respectively.

## Assumptions and scope

The ground field \(\mathbb F_q\) can have any characteristic and any prime-power order. The polynomial indeterminate \(t\) is central over the full matrix algebra; the quotient truncates at degree three. The ring \(J_m\) is nonunital and satisfies \(J_m^3=0\) but \(J_m^2\ne0\). The two-sided action is the ordinary left-right action of **principal units in the unitalization**, not a claim that both sides separately constitute the standard left-brace \(\lambda\)-action. The pair-action uses the inverse on the right so it is a genuine group action; replacing \(h^{-1}\) by \(h\) yields the same orbits. The leading rank is well-defined on each orbit. Asymptotic estimates are for fixed field order \(q\) and growing matrix size \(m\); error constants may depend on \(q\).

## Proof

**1. Explicit actions and fibers.** In coordinates \((C,D)\leftrightarrow tC+t^2D\), multiplication is \((U,V)(C,D)=(0,UC)\), so \(\lambda_{(U,V)}(C,D)=(C,D+UC)\). Since \(J_m^3=0\), multiplying from the right by a principal unit or its inverse adds an arbitrary term \(CV\) to the second coefficient. Consequently the left and two-sided orbit fibers above a fixed \(C\) are precisely the additive cosets of
\[
\mathcal L_C=\{UC:U\in M_m(\mathbb F_q)\},\qquad
\mathcal T_C=\{UC+CV:U,V\in M_m(\mathbb F_q)\}
\]
in the full space \(M_m(\mathbb F_q)\). For \(r=\operatorname{rank}C\), the first space has dimension \(mr\): its rows lie in the \(r\)-dimensional row space of \(C\). To determine the second, apply invertible changes of coordinates on the source and target to put \(C\) into \(\operatorname{diag}(I_r,0)\). The sum \(\mathcal T_C\) is exactly the block matrices whose lower-right \((m-r)\times(m-r)\) block is zero. Thus \(\dim\mathcal T_C=m^2-(m-r)^2=2mr-r^2\). The overlap \(\mathcal L_C\cap\{CV\}\) is the upper-left \(r\times r\) block, of dimension \(r^2\). Every coset has the corresponding power-of-\(q\) size and there are exactly \(q^{m^2-mr}\) or \(q^{(m-r)^2}\) cosets above fixed \(C\).

**2. Exact rank enumeration.** A rank-\(r\) matrix is a surjection of \(\mathbb F_q^m\) onto an \(r\)-dimensional image, followed by embedding that image in \(\mathbb F_q^m\). Choosing the image subspace and then the surjection gives
\[
{m\brack r}_q\prod_{i=0}^{r-1}(q^m-q^i)=N_{m,r}(q).
\]
Multiplying by the fixed-\(C\) coset counts of step 1 gives the exact \(L_{m,r}\) and \(T_{m,r}\) formulas.

**3. Uniform bounds for the finite-field rank factor.** Put \(P_j=\prod_{i=1}^j(1-q^{-i})\), with \(P_0=1\) and positive limit \(P_\infty\). Elementary rearrangement yields
\[
N_{m,r}(q)=q^{2mr-r^2}H_{m,r},\qquad
H_{m,r}=\frac{P_m^2}{P_rP_{m-r}^2}.
\]
For every \(j\ge0\), the product-tail estimate \(|P_j-P_\infty|\le C_q q^{-j}\) follows by bounding the omitted factors by their convergent geometric sum. Since \(P_\infty\le P_j\le1\), the functions \(H_{m,r}\) are bounded above and below by constants depending only on \(q\); moreover
\[
H_{m,r}=\frac1{P_\infty}+O_q(q^{-\min(r,m-r)}).
\]
These estimates are uniform in \(m,r\), including endpoints \(r=0,m\).

**4. Left-orbit theta law.** Complete the square:
\[
L_{m,r}=q^{5m^2/4-(r-m/2)^2}H_{m,r}.
\]
On \(m/4\le r\le3m/4\), step 3 gives \(H_{m,r}=P_\infty^{-1}(1+O_q(q^{-m/4}))\). Outside this interval the Gaussian factor is at most \(q^{-m^2/16}\) times a uniformly bounded prefactor, so its full tail is negligible compared with the lattice theta sum. Normalize the weights on the integer or half-integer lattice according to the parity of \(m\). Summation proves both the stated theta total and the total-variation error. In particular, \(R_L/m\to1/2\) in probability.

**5. Two-sided uniform rank law.** The quadratic terms cancel exactly:
\[
T_{m,r}=q^{m^2}H_{m,r}.
\]
By step 3,
\[
\sum_{r=0}^{m}\left|H_{m,r}-P_\infty^{-1}\right|
\le C_q\sum_{r=0}^{m}q^{-\min(r,m-r)}=O_q(1).
\]
Consequently \(\sum_r H_{m,r}=(m+1)P_\infty^{-1}+O_q(1)\); dividing each weight by this total gives total variation \(O_q(m^{-1})\) from the uniform distribution on the \(m+1\) ranks. After scaling by \(m\), discrete uniform converges weakly to continuous uniform on \([0,1]\). The logarithm of the two-sided orbit size is \(2mR_T-R_T^2\), so continuity and boundedness of \(u\mapsto2u-u^2\) give the asserted limiting distribution and expectation \(\int_0^1(2u-u^2)\,du=2/3\).

**6. Uniform-point rank law.** Sampling \((C,D)\) uniformly gives a uniform matrix \(C\). For any fixed \(k\)-dimensional subspace \(W\) of \(\mathbb F_q^m\), the event \(W\subseteq\ker C\) has probability \(q^{-mk}\). Taking a union bound over all \(k\)-subspaces and using \({m\brack k}_q\le P_\infty^{-1}q^{k(m-k)}\) gives
\[
\Pr(m-\operatorname{rank}C\ge k)\le P_\infty^{-1}q^{-k^2}.
\]
The nullity is therefore tight, and \(\operatorname{rank}C/m\to1\) in probability. The normalized base-\(q\) logarithm of its left orbit is \(m\operatorname{rank}C/m^2\to1\). For a uniform left orbit, the analogous expression is \(R_L/m\to1/2\), completing the three-way comparison.

## Verification

The standalone dependency-free `VERIFY.py` carries out direct rank and orbit checks over the prime fields \(\mathbb F_2\) and \(\mathbb F_3\) for \(m=1,2\). For every leading matrix it explicitly constructs the full left- and two-sided translation subspaces, enumerates every coset in the second coefficient, and compares the exact orbit ranks and cardinalities against the formulas, without assuming the claimed orbit count. It additionally enumerates every \(3\times3\) binary leading matrix, independently forms the left/right generator spans over \(\mathbb F_2\), verifies their dimensions and rank strata, and evaluates two asymptotic finite-size checks at \((q,m)=(2,60)\).

| \((m,q)\) | Left orbits | Two-sided orbits |
|---|---:|---:|
| \((1,2)\) | 3 | 3 |
| \((1,3)\) | 5 | 5 |
| \((2,2)\) | 58 | 40 |
| \((2,3)\) | 417 | 225 |
| \((3,2)\) | 6168 | 2052 |

Run `python3 VERIFY.py`; success terminates with `MATRIX_RADICAL_TWO_SIDED_ORBIT_SPECTRA_VERIFIED`. The \(3\times3\) binary test checks generator-space dimensions and all rank totals, whereas the smaller cases also enumerate every orbit coset. All prime-power fields, all matrix dimensions, and both limiting probability laws are established by the proof, **not** by finite testing.

## Relationship to prior work

Properzi and Van Antwerpen [1] introduce the \(\lambda\)-orbit census and common-divisor graph as central invariants of skew braces; their full available preprint develops general orbit constraints and graph structure but does not give the present matrix-radical rank spectra or the three sampling laws. Childs [2] establishes general class-two radical rings as a source of bi-skew braces; this is structural context, not evidence of a rank-census theorem. A published calculation of three-block matrix radical brace/group centralizers [3] likewise involves products of rectangular matrix blocks and their centralizers; its full result concerns centralizer gaps, commutator fibers and widths, not the present principal-unit left/right orbit distributions.

Classical finite-field matrix-rank counts, elementary row/column-space linear algebra, and Gaussian theta-series estimates are **used and credited as standard ingredients**. The assessed statement is the complete *pair of orbit multiplicity spectra in the same class-two radical* together with the rigorous point/left-orbit/two-sided-orbit rank-law trichotomy and its quantitative error. A generic assertion that group-orbit sampling differs from point sampling would not imply the explicit Gaussian-versus-uniform split proved here.

## Limitations

No assertion of novelty is made for the standard number of matrices of a given rank or for basic class-two brace constructions. The classification is specific to the radical of cubic truncated matrix polynomials: different module structures, longer truncations and non-field coefficients require new arguments. No full survey of all literature on Green orbits, two-sided algebra-group actions and radical braces has been completed, and a possible implicit historical equivalence cannot be ruled out. The accessible complete primary preprint [1] and the published full result [3] were inspected; the full text of [2] was not retrieved and its abstract supports only a limited comparison. Finite checks cannot substitute for the exact linear-algebraic proof or the uniform asymptotic estimates.

## References

1. S. Properzi and A. Van Antwerpen, *Common divisor graphs for skew braces*, arXiv:2306.12415v1 (first public 2023-06-21), https://arxiv.org/abs/2306.12415. Accessible full-text transcription: https://www.researchgate.net/publication/371758274_Common_divisor_graphs_for_skew_braces.
2. L. N. Childs, *Bi-skew braces and Hopf Galois structures*, arXiv:1904.08814 (first public 2019-04-18), https://arxiv.org/abs/1904.08814.
3. *Rank-stratified brace and group centralizers in three-block matrix radicals*, published full result (2026-11-02), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-rank-stratified-brace-and-group-centralizers-in-three-block-matr--65007f7be362/RESULT.md.
