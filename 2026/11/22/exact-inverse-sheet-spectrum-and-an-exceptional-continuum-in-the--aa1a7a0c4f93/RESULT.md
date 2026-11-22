# Exact inverse-sheet spectrum and an exceptional continuum in the three-dimensional simple intertwining logistic map

## Finding

For the three-dimensional modular map introduced by Zhao and Ma, an entire natural integer-gain subfamily admits a **complete one-step inverse-fiber classification on the full half-open unit cube**, not merely on an invariant coordinate face. For the integer-gain parameter \(\mu=m/64\), \(m\in\{1,\ldots,255\}\), every target has an explicitly computed finite number of predecessors except on one one-dimensional exceptional locus of continuum-sized fibers. The map is onto the half-open cube for every \(m\ge2\) and is not onto at \(m=1\). At the paper's reference parameter \(\mu=1\), every target outside the exceptional curve has between \(106848\) and \(114400\) distinct real one-step predecessors.

For a target \((U,V,W)\in[0,1)^3\), put
\[
 A=\frac m{64}(64+U+V),\quad
 s=\max\left\{0,\left\lceil\frac{5A}{6}-W\right\rceil\right\}.
\]
For \(k=0,\ldots,s-1\), let \(w_k\in[0,1)\) be the unique solution of
\[
 w_k-\frac{w_k^3}{6}=\frac{W+k}{A},
\]
and set \(\delta_k=\{V-w_k(1+U^2)\}\), \(\tau_k=\{U-w_k\}\), where \(\{t\}=t-\lfloor t\rfloor\in[0,1)\). The exceptional set is the parameterized locus
\[
 \Gamma_m=\left\{\left(
 t,\ \{t(1+t^2)\},\ 
 \left\{\frac m{64}\bigl(64+t+\{t(1+t^2)\}\bigr)
 \left(t-\frac{t^3}{6}\right)\right\}
 \right):0\le t<1\right\}.
\]
For \((U,V,W)\notin\Gamma_m\), the **exact number** of predecessors is
\[
 \boxed{N_m(U,V,W)=\frac{m(m-1)}2s+
 m\sum_{k=0}^{s-1}\mathbf 1_{\{0<\tau_k\le\delta_k\}}.}
\]
For \((U,V,W)\in\Gamma_m\), the fiber is uncountable (indeed it contains a full interval parameterized by an arbitrary first input coordinate). No target has any other infinite-fiber mechanism. On every smooth modular branch, the Jacobian determinant vanishes exactly at inputs with \(v=0\), linking this exceptional locus to genuine rank collapse.

## Assumptions and scope

The state space is the half-open cube \(Q=[0,1)^3\); \(\{t\}\) denotes reduction modulo one, including the convention that integer values reduce to zero. The exact published map is
\[
 \begin{aligned}
 U&=\{64\mu v(1-u)+w\},\\
 V&=\{64\mu v+w(1+U^2)\},\\
 W&=\{\mu(64+U+V)(w-w^3/6)\}.
 \end{aligned}
\]
The integer-gain slice \(m=64\mu\in\{1,2,\ldots,255\}\) is within the published range \(0<\mu\le3.999\). Inputs and outputs use exact real arithmetic; no floating-point or cryptographic security assertion is made. This is a one-step inverse statement, not an assertion about long-run invariant measures or the number of periodic orbits.

## Proof

**Step 1: the cubic inverse sheets.** The polynomial \(\psi(w)=w-w^3/6\) has derivative \(1-w^2/2\ge1/2\) on \([0,1)\). It maps that interval strictly increasingly onto \([0,5/6)\). At a fixed target, the third map equation becomes \(A\psi(w)=W+k\), where \(k\) is a nonnegative integer. Exactly the \(s=\max(0,\lceil5A/6-W\rceil)\) integers \(k=0,\ldots,s-1\) occur. Each gives precisely one \(w_k\).

**Step 2: the second-coordinate residues.** For one such \(w=w_k\), let \(\delta=\{V-w(1+U^2)\}\). The second equation is \(\{mv\}=\delta\), and because \(m\) is an integer, its exact solutions in \([0,1)\) are
\[
 v_j=\frac{\delta+j}{m},\qquad j=0,1,\ldots,m-1.
\]
There are exactly \(m\) of them, whether or not \(\delta=0\).

**Step 3: first-coordinate integer intervals.** Put \(t=U-w\). For \(v_j>0\), the first equation is equivalent to \(mv_j(1-u)=t+\ell\), with \(\ell\in\mathbb Z\) and \(0\le u<1\). The exact constraints are
\[
 0<t+\ell\le\delta+j.
\]
Thus \(u=1-(t+\ell)/(\delta+j)\) is a valid distinct solution exactly for the integers \(\ell\in(-t,\delta+j-t]\), and their number is
\[
 \lfloor\delta+j-t\rfloor-\lfloor-t\rfloor
 =j+\mathbf1_{\{0<\{t\}\le\delta\}}.
\]
This identity includes all equality boundaries: the lower inequality is strict because \(u=1\) is excluded, whereas equality at the upper end allows \(u=0\). Summing over \(j=0,\ldots,m-1\) yields \(m(m-1)/2+m\mathbf1_{\{0<\tau\le\delta\}}\). Summing over the \(s\) cubic sheets proves the stated finite formula.

**Step 4: exact continuum condition.** The only omitted case in Step 3 occurs if \(v_j=0\), which means \(\delta=0\) and \(j=0\). The first equation then becomes \(U=w\), independently of \(u\). Together with the second equation this requires \(V=\{w(1+w^2)\}\), and the third equation forces the stated \(W\). These are precisely the points of \(\Gamma_m\), and every \(u\in[0,1)\) then supplies a predecessor \((u,0,w)\). Off the curve, the finite enumeration from Steps 1–3 is exhaustive. All other \(v_j\)'s yield finitely many \(u\)'s, so no other infinite fiber is possible.

**Step 5: critical Jacobian.** On any open cell where the three reductions modulo one are smooth, differentiate in the triangular coordinates \((U,V,w)\). The upper two-coordinate Jacobian has determinant \(-m^2v\), as the terms through \(U\) in the second component cancel. The final triangular factor is \(A\psi'(w)\). Hence
\[
 \det DF_m=-m^2vA\left(1-\frac{w^2}{2}\right).
\]
Because \(m,A>0\) and \(1-w^2/2>0\), a smooth-branch rank loss occurs precisely at \(v=0\), the source of \(\Gamma_m\). Branch seams are excluded from this differentiability assertion but were handled by the exact half-open integer inequalities in Step 3.

**Step 6: surjectivity and the reference-gain bounds.** For every \(m\ge2\), \(A\ge m\) and \(W<1\), so \(5A/6-W>5m/6-1\ge2/3>0\). Hence \(s\ge1\) and \(N_m\ge m(m-1)/2\ge1\) off the curve, while curve targets already have infinitely many predecessors. Thus the map is onto. When \(m=1\), the target \((0,0,9/10)\) has \(A=1\), \(s=0\), and no predecessor, so the map is not onto. At \(m=64\), \(64\le A<66\) gives \(53\le s\le55\). The formula then gives
\[
 53\cdot2016=106848\le N_{64}\le55\cdot2080=114400
\]
for every target outside \(\Gamma_{64}\). These bounds are asserted as universal, not necessarily attained or optimal.

## Verification

The included self-contained `verify.py` performs exact rational checks of the integer interval identity for \(m=1,\ldots,12\) and many rational threshold positions. It additionally reconstructs every numerical predecessor for selected regular outputs at \(m=2,3,4,7,8,64\) and verifies that the original three-component map returns the target to within floating-point tolerance. At \(m=64\) it enumerates more than \(10^5\) predecessors for each selected target and checks the universal bounds. Finally it verifies that an entire first-coordinate interval has identical outputs when \(v=0\). The numerical reconstructions illustrate rather than replace the exact algebraic proof; the exact formula, boundaries, and infinite-fiber classification follow from Steps 1–6 without numerical assumptions.

## Relationship to prior work

Zhao and Ma introduced the precise three-dimensional map in *Symmetry* **16** (2024), 169, equation (2), and studied numerical chaos, implementation speed, and pseudo-random-number tests. Their documented analysis does not state a full-cube preimage classification, an onto threshold on the integer-gain slice, or a continuum-fiber locus. Ye and Huang's earlier intertwining logistic map contains a sine term in place of the polynomial truncation and does not directly supply these inverse counts. A previously examined fixed-point enumeration on the invariant face \(w=0\) addresses a different question: fixed points of the restriction do not imply counts of predecessors of arbitrary three-dimensional targets. Related inverse-sheet classifications for other noninvertible maps use different equations and do not entail the modular cubic-sheet formula here.

## Limitations

The theorem requires exact real reduction modulo one on the half-open cube and integer \(64\mu\); no statement is made for noninteger gains, finite-precision arithmetic, or the original sine map. On \(\Gamma_m\), fibers are uncountable, so the finite count is not asserted there. The two displayed numerical bounds at \(\mu=1\) are not claimed optimal. An extremely large one-step inverse multiplicity does not itself establish cryptographic weakness or strength, an attractor, hyperchaos, or unusual long-run statistical dynamics. Searches of indexed related work cannot rule out every unindexed equivalent classification, and independent scholarly validation has not been performed.

## References

1. W. Zhao and C. Ma, “Modification of Intertwining Logistic Map and a Novel Pseudo Random Number Generator,” *Symmetry* **16** (2024), article 169, first publicly published January 31, 2024. https://doi.org/10.3390/sym16020169. Source equation (2) and numerical analysis.
2. G. Ye and X. Huang, “An efficient symmetric image encryption algorithm based on an intertwining logistic map,” *Neurocomputing* **251** (2017), 45–53. https://doi.org/10.1016/j.neucom.2017.04.016. Its original sine-based formula is quoted in Zhao–Ma, equation (1).
3. Related but nonidentical inverse problem: “Exact inverse-sheet and observation-window transitions in coupled Gumowski–Mira rings,” 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-inverse-sheet-and-observation-window-transitions-in-couple--370a893f822a. The inverse equations differ from the present modular map.
