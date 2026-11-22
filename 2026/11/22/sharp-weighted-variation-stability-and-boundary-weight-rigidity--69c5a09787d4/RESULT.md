# Sharp weighted-variation stability and boundary-weight rigidity of the three-point midrange filter

## Finding

For any integer \(n\ge2\), define the endpoint-truncated three-point *midrange* map \(M_n:\mathbb R^n\to\mathbb R^n\) by
\[
(M_nf)_i=\frac12\left(\min_{j\in W_i}f_j+\max_{j\in W_i}f_j\right),\qquad W_i=\{\max(1,i-1),\ldots,\min(n,i+1)\}.
\]
For arbitrary positive variation-edge weights \(w=(w_1,\ldots,w_{n-1})\), put \(V_w(h)=\sum_{j=1}^{n-1}w_j|h_{j+1}-h_j|\). Define the sharp two-input Lipschitz coefficient
\[
L_n(w)=\sup_{V_w(f-g)>0}\frac{V_w(M_nf-M_ng)}{V_w(f-g)}.
\]
This supremum is attained by an arbitrarily close pair of distinct input signals. Its exact value is \(L_2(w)=0\); for \(n=3\),
\[
L_3(w)=\frac{\max(w_1,w_2)}{2\min(w_1,w_2)};
\]
and for every \(n\ge4\),
\[
\boxed{L_n(w)=\max\left\{\frac{\max(w_1,w_2)}{2w_1},\ \frac{\max(w_{n-2},w_{n-1})}{2w_{n-1}},\ \max_{2\le j\le n-2}\frac{F_j}{w_j}\right\},}
\]
where
\[
F_j=\max\left\{w_j,\ \frac{w_{j-1}+w_j}{2},\ \frac{w_j+w_{j+1}}2,\ \frac{w_{j-1}+w_{j+1}}2\right\}.
\]
Consequently, the *complete classification* of \(L_n(w)\le1\) is: all positive weights if \(n=2\); precisely \(1/2\le w_1/w_2\le2\) if \(n=3\); and for \(n\ge4\), precisely
\[
\boxed{w_2=\cdots=w_{n-2}=c>0,\qquad c/2\le w_1,w_{n-1}\le c.}
\]
Thus a common interior variation weight with *independently tapered boundary weights*, down to half the interior weight, is nonexpansive. In particular, for uniform weights, the sharp coefficient is \(0\) for \(n=2\), \(1/2\) for \(n=3\), and exactly \(1\) for every \(n\ge4\).

## Assumptions and scope

Signals are arbitrary real vectors on a finite ordered path. Windows are the closed, *truncated* radius-one windows written above; endpoints are not artificially duplicated or preserved unchanged. Variation weights are strictly positive and independent of the filter's data values. Constant vectors are annihilated by \(V_w\), and \(M_n\) commutes with addition of constants, so the two-input quotient is meaningful. All suprema run over every pair of real inputs with positive denominator; no generic-position assumption is imposed on inputs. This is a statement about the variation of **differences of two outputs**, not just the variation of a single filtered signal.

## Proof

**1. Local affine and step-column reduction.** On every open chamber where all input coordinates have pairwise distinct values, the minimum and maximum in each window select two fixed input coordinates. Hence \(M_n\) agrees locally with a real linear map \(B\), each of whose rows has coefficients \(1/2\) at its selected minimum and maximum; when the two selectors coincide, the coefficients add to one. In every case \(B\mathbf1=\mathbf1\). For each cut \(1\le j\le n-1\), let \(H^{(j)}\) be zero in coordinates through \(j\) and one afterward. Every perturbation \(h\) has the exact decomposition
\[
h=h_1\mathbf1+\sum_{j=1}^{n-1}(h_{j+1}-h_j)H^{(j)}.
\]
The triangle inequality proves
\[
V_w(Bh)\le\left(\max_{1\le j<n}\frac{V_w(BH^{(j)})}{w_j}\right)V_w(h).
\]
Conversely any step attains its own displayed ratio, so this is the *exact* norm of the local linear map, not merely an upper bound.

**2. Internal step-column geometry.** Suppose \(n\ge4\) and \(2\le j\le n-2\). A window at an output site at most \(j-1\) lies entirely to the left of the input cut; a window at an output site at least \(j+2\) lies entirely to its right. Thus \(BH^{(j)}\) is zero through output site \(j-1\), equals one from site \(j+2\) onward, and has only two potentially mixed values \(a\) and \(b\) at sites \(j\) and \(j+1\). At site \(j\), two of the three input indices are on the left and one is on the right, giving \(a\in\{0,1/2\}\). At site \(j+1\), the right side has two indices and the left has one, giving \(b\in\{1/2,1\}\). Therefore the possible weighted variations are exactly
\[
\begin{array}{c|c}
(a,b)&V_w(BH^{(j)})\\\hline
(0,1/2)&(w_j+w_{j+1})/2\\
(0,1)&w_j\\
(1/2,1/2)&(w_{j-1}+w_{j+1})/2\\
(1/2,1)&(w_{j-1}+w_j)/2
\end{array}
\]
where each row arises at a strictly ordered input. To verify attainability for all four rows, respectively assign the four adjacent input values \((f_{j-1},f_j,f_{j+1},f_{j+2})\) to \((0,2,1,1/2)\), \((0,2,1,3)\), \((0,1,2,3)\), and \((1,2,0,3)\). The remaining input entries can be chosen distinctly, avoiding these values, without affecting the local selectors. Hence the exact largest internal step-column variation is \(F_j\).

**3. Boundary steps.** At cut \(j=1\) and \(n\ge3\), the first output is exactly \(1/2\) when the input is replaced by \(H^{(1)}\) within any fixed selector chamber. The second output is either \(1/2\) (when input value \(f_1\) is extreme in the three-point window) or \(1\) (when it lies between \(f_2\) and \(f_3\)); all outputs from site three onward equal one. Thus the exact boundary-column variations are \(w_2/2\) and \(w_1/2\), and both are realizable by strict input orders. Reflection gives \(w_{n-2}/2\) and \(w_{n-1}/2\) at cut \(j=n-1\). For \(n=3\), both cuts have these two options, leading to the stated \(L_3\); for \(n=2\), both output windows contain both coordinates, giving a spatially constant output and \(L_2=0\).

**4. Global pairs and exact attainment.** The map is continuous and piecewise linear, with finitely many order chambers. Along a generic line segment from \(f\) to \(g\), the derivative of \(M_n\) is one of the chamber maps \(B\), apart from finitely many parameters. Every such \(B\) obeys the same sharp bound from parts 1–3; integrating the derivative and using the triangle inequality for \(V_w\) proves the global upper estimate. Nongeneric segments follow by continuity. Conversely, for each strict chamber and step \(H^{(j)}\) attaining one listed ratio, choose an input \(f\) interior to that chamber and \(g=f+\varepsilon H^{(j)}\) with any sufficiently small \(\varepsilon>0\). The entire pair lies in the same chamber and
\[
\frac{V_w(M_ng-M_nf)}{V_w(g-f)}=\frac{V_w(BH^{(j)})}{w_j}.
\]
Thus the finite maximum is attained by actual distinct input pairs, with arbitrarily small separation. This also handles all boundary-weight choices and completes the coefficient proof.

**5. Rigidity of contractive weights.** For \(n\ge4\), requiring every internal \(F_j\le w_j\) forces \(w_{j-1}\le w_j\) and \(w_{j+1}\le w_j\) for every internal cut \(2\le j\le n-2\). Applying these inequalities from both sides at each neighboring pair of interior edges gives \(w_2=\cdots=w_{n-2}=c\). The same inequalities at the ends force \(w_1,w_{n-1}\le c\). The boundary-column ratios are at most one precisely when \(w_1,w_{n-1}\ge c/2\). Conversely, these bounds make all four internal branches and both boundary branches no larger than their input-edge weights; hence they are sufficient. The special cases \(n=2,3\) follow directly from their exact coefficients.

## Verification

The included standalone `verify.py` uses Python 3's standard library exclusively. It enumerates every strictly ordered input chamber at sizes \(2\le n\le8\), namely 46,232 permutations in total. For every cut it calculates the *exact* twice-normalized step-column profile, verifies that the only possible profiles are those in the proof, and checks five independent rational/integer weight families at every size against the finite maximum. It also verifies the boundary-taper classification with rational perturbations, then checks 4,950 deterministic rational two-input inequalities and the unweighted one-input variation inequality. The checks are finite corroboration; parts 1–5 prove all dimensions and all positive real weights analytically.

## Relationship to prior work

The 1993 paper by Schulze and Pearce explicitly introduces the midrange as the arithmetic mean of morphological erosion and dilation, and discusses its bias and noise response. Its inspected full text does not state or imply the present sharp two-input weighted variation norm or the boundary-weight classification. Anguelov and Rohwer's 2007 LULU treatment concerns variation preservation and trend properties of *compositions* of morphological operators; a one-input variation inequality does not imply a two-input seminorm Lipschitz inequality. A published finite-path morphology result establishes exact weighted two-input norms of the **individual** erosion and dilation maps, but its separate-component inequalities only give a generally nonsharp upper bound for their mean. In particular, at four sites and edge weights \((1/2,1,1/2)\), the midrange has coefficient one while each constituent erosion/dilation has weighted coefficient at least two. The published endpoint-preserving running-median result uses a different filter, whose best two-input coefficient already exceeds one at four sites, so it neither implies nor dominates this contractive-midrange classification. The uniform-weight contractivity substatement is not claimed as novel: reflecting a finite path to a cyclic signal allows it to follow from a cyclic midrange contraction. What is new here is the exact nonuniform weighted coefficient, the sharp boundary interval, and attainable equality cases.

The midrange is a classical and extensively studied filter, so this comparison does not certify absolute historical priority. A bibliographically older 1993 conference source is known to the year but not to an independently verified first-public *calendar day*; the machine-readable first-public date refers to the earliest precisely dated accessible archival mathematical source in this comparison, the first posting of the 2007 LULU paper, and is not falsely asserted to be the first disclosure of midrange itself.

## Limitations

The theorem concerns a finite real path, radius-one truncated windows, and a fixed positive variation-edge weighting. It does not classify larger windows, other boundary conventions, periodic signals, or multidimensional neighborhoods. Its weighted contractivity is a two-input perturbation statement, not a guarantee of noise removal, edge preservation, or statistical optimality. Earlier morphology books and some publisher full texts were not exhaustively accessible, so an implicit historical equivalence cannot be excluded. The proof makes no claim about numerical stability in finite-precision implementations.

## References

1. M. A. Schulze and J. A. Pearce, *Linear combinations of morphological operators: the midrange, pseudomedian, and LOCO filters*, Proceedings of ICASSP 1993, vol. V, pp. 57–60. DOI: 10.1109/ICASSP.1993.319746. Full conference-paper transcription inspected; specific first public calendar day not established.
2. R. Anguelov and C. Rohwer, *LULU operators for functions of continuous argument*, arXiv:0711.1944v1, submitted 13 November 2007. https://arxiv.org/abs/0711.1944 .
3. *Finite-window morphology: sharp two-input variation and a boundary-weight transition*, 2026, public result and proof at https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-finite-window-morphology-sharp-two-input-variation-and-a-boundar--5f5f2cb7d7b2 .
4. *Sharp two-input variation sensitivity of three-point median smoothing on finite paths*, 2026, public result and proof at https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-two-input-variation-sensitivity-of-three-point-median-smoo--5759b99f2a42 .
