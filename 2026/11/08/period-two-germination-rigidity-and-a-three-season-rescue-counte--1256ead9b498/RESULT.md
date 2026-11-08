# Period-two germination rigidity and a three-season rescue counterexample in an age-two seed bank

## Finding

**Two-season rigidity theorem.** For any two distinct positive seasonal fecundities \(a>b>0\) and dormant-seed survival \(0<s\leq1\), the age-two seed-bank model below, with a fixed young-seed germination fraction \(g\in[0,1]\), has maximal two-season Floquet multiplier
\[
\max_{0\leq g\leq1}\rho\bigl(A(b,g,s)A(a,g,s)\bigr)=a\max\{b,s\}.
\]
Its **complete maximizer classification** is \(g=1\) alone if \(s<b\), \(g=0\) alone if \(s>b\), and exactly the two pure choices \(g=0,1\) if \(s=b\). All interior choices \(0<g<1\) are strictly worse, including at the tie.

**Sharpness with respect to cycle length.** For the same model with three successive fecundities \((4,1/5,1)\) repeated, and \(s=3/4\), both pure choices have a three-season multiplier below one, whereas the mixed choice \(g=1/2\) has a multiplier above one:
\[
\rho(M_3(0))=\frac{3\sqrt{15}}{20}<1,\qquad
\rho(M_3(1))=\frac45<1,\qquad
\rho(M_3(1/2))=\frac{83+\sqrt{7969}}{160}>1.
\]
Thus, in this exact age-two model, a mixed germination policy can prevent asymptotic decline in a three-season environment even though neither pure policy can. No optimality assertion for \(g=1/2\) in the three-season example is made.

## Assumptions and scope

At the start of season \(t\), let \(Y_t\geq0\) count newly produced viable seeds eligible for their **first** germination opportunity, and let \(O_t\geq0\) count the surviving seed cohort deferred from its first opportunity. A fraction \(g\) of young seeds germinates; every old seed germinates; each germinant produces \(f_t>0\) new young seeds, with no density dependence and no adult carryover. Young seeds that do not germinate survive to the old cohort with probability \(s\in(0,1]\). Old seeds leave the system after their germination opportunity. The deterministic expected-abundance recurrence is
\[
\begin{pmatrix}Y_{t+1}\\O_{t+1}\end{pmatrix}
=A(f_t,g,s)\begin{pmatrix}Y_t\\O_t\end{pmatrix},\qquad
A(f,g,s)=\begin{pmatrix}fg&f\\s(1-g)&0\end{pmatrix}.
\]
No birth cost for dormancy other than survival \(s\) is imposed, and the same fraction \(g\) is used in every season. For a season sequence repeated with period \(k\), the \(k\)-season multiplier is the spectral radius of the chronological product \(M_k=A(f_{k-1},g,s)\cdots A(f_0,g,s)\), with per-calendar-season asymptotic growth factor \(\rho(M_k)^{1/k}\). At reducible boundary policies, this spectral quantity represents the maximal asymptotic growth rate over nonnegative initial age states; an initially missing invariant reproductive cohort may grow more slowly. A strictly positive initial vector realizes the maximal spectral growth rate.

The two-season statement applies to every \(a>b>0\), \(0<s\leq1\), and \(0\leq g\leq1\). The three-season witness is a single exact parameter example; it does not classify all longer environmental cycles.

## Proof

**1. Exact two-season characteristic polynomial.** The chronological product, trace, and determinant are
\[
M_2=A(b,g,s)A(a,g,s)
=\begin{pmatrix}
abg^2+bs(1-g)&abg\\
asg(1-g)&as(1-g)
\end{pmatrix},
\]
\[
T(g)=abg^2+s(a+b)(1-g),\qquad
D(g)=abs^2(1-g)^2.
\]
Its eigenvalues are the roots of \(P_g(z)=z^2-T(g)z+D(g)\). The matrix is nonnegative and has real eigenvalues because its characteristic discriminant is \((M_{11}-M_{22})^2+4M_{12}M_{21}\geq0\); its spectral radius is its larger real eigenvalue.

**2. Locate the larger root relative to a single candidate bound.** Put \(L=a\max\{b,s\}\). Since \(T(g)\) is convex in \(g\in[0,1]\),
\[
T(g)\leq\max\{T(0),T(1)\}=\max\{s(a+b),ab\}<2L
\]
(the last strict inequality uses \(a>b>0\), separately for \(s\leq b\) and \(s\geq b\)). Thus \(L>T(g)/2\), so the larger real root is at most \(L\) exactly when \(P_g(L)\geq0\); strict positivity of \(P_g(L)\) gives strict inequality.

For \(s\leq b\), \(L=ab\), and direct factorization yields
\[
P_g(ab)=ab(1-g)\bigl[(a-s)(b-s)+g(ab-s^2)\bigr].
\]
When \(s<b\), the bracket is strictly positive for all \(g\in[0,1]\); at equality \(s=b\), the bracket is strictly positive for \(0<g\leq1\). Therefore \(g=1\) is the unique maximizer when \(s<b\), and no interior choice maximizes when \(s=b\).

For \(s\geq b\), \(L=as\), and the other exact factorization is
\[
P_g(as)=asg\bigl[(1-g)(a-b)s+ga(s-b)\bigr].
\]
When \(s>b\), the bracket is strictly positive for all \(g\in[0,1]\); at equality \(s=b\), it is strictly positive for \(0\leq g<1\). Therefore \(g=0\) is the unique maximizer when \(s>b\), and again no interior choice maximizes at the tie.

Finally, at \(g=0\) the two-season matrix has eigenvalues \(as,bs\), while at \(g=1\) it has eigenvalues \(ab,0\). Hence the stated bound \(L\) is attained by the indicated pure strategy or strategies, including both when \(s=b\). This proves the full classification and the strict interior exclusion.

**3. A three-season mixed-growth rescue.** Let the chronological fecundity sequence be \((4,1/5,1)\), and set \(s=3/4\). Exact multiplication gives
\[
M_3(0)=\begin{pmatrix}0&3\\9/80&0\end{pmatrix},\quad
M_3(1)=\begin{pmatrix}4/5&4/5\\0&0\end{pmatrix},\quad
M_3(1/2)=\begin{pmatrix}71/80&17/10\\33/320&3/20\end{pmatrix}.
\]
The first two have spectral radii \(\sqrt{27/80}=3\sqrt{15}/20<1\) and \(4/5<1\). The third has trace \(83/80\), determinant \(-27/640\), and characteristic polynomial at \(z=1\) equal to \(-51/640<0\). It therefore has a positive dominant root strictly exceeding one, explicitly \((83+\sqrt{7969})/160\). This establishes a strict change of behavior between periods two and three under exactly the same age and survival rules.

## Verification

The included standalone `verify.py` uses symbolic expressions to verify both factorizations, all trace/determinant identities, and each of the three exact three-season matrices. A separate rational-arithmetic matrix multiplication routine checks the analytical two-season upper bound in 1,235 admissible exact-rational configurations, including boundary policies, and independently reconstructs the three-season witness. Run `python verify.py` with Python and SymPy installed. These finite checks independently corroborate the displayed algebra; the all-parameter proof is the exact characteristic-polynomial sign argument above, not an inference from finite samples.

## Relationship to prior work

Brown and Venable (1986, pp. 33–34) model random year types using scalar geometric-mean annual fitness of the form \(\prod_i[gF_i+s(1-g)]^{p_i}\), in which mixed germination can be optimal. That scalar formulation is **not** the age-two two-dimensional, deterministic-periodic Floquet recurrence here, and its optimum does not imply either part of this theorem. Rees and Long (1992) study plant persistence under environmental variation, including delayed germination and landscape occupancy, with different stochastic/density frameworks. Rees (1994, especially pp. 44–50) develops age/stage-structured invasion matrices, but the inspected constant-environment results and stochastic-environment simulations do not give the fixed three-term age-two recurrence, the period-two exact switching law, or the three-season growth-rescue example. Tielbörger and Valleriani (2005) and Valleriani and Tielbörger (2006) study density-dependent and age-specific germination, respectively; their publicly accessible summaries do not supply the precise period-two comparison. Verin (2018, Supplementary Text S3 to the thesis) studies the influence of the periods of a cycling environment on longer-lived seed banks using numerical simulations with substantially different persistence lengths and cycle periods. No exact two-season rigidity theorem with the displayed three-season counterexample was located in the material inspected, but these literature searches cannot establish historical novelty, particularly for older matrix-projection treatments.

## Limitations

The theorem is for fixed, age-independent first-opportunity fraction \(g\) and compulsory germination at the second opportunity. Germination that adapts to the season, seeds surviving beyond two opportunities, adult carryover, density dependence, environmental stochasticity, and finite-population extinction are outside the statement. Multipliers below one imply deterministic linear decay for generic positive age mixtures, not stochastic extinction probabilities. No ecological field calibration is asserted. The historical-priority comparison is incomplete because potentially relevant older full texts on age-dependent germination and correlated yields were inaccessible; independent literature review remains necessary.

## References

- Brown, J. S. and Venable, D. L. (1986), *Evolutionary Ecology of Seed-Bank Annuals in Temporally Varying Environments*, *The American Naturalist* 127, 31–47. https://doi.org/10.1086/284465 . Full accessible text: https://sciences.ucf.edu/biology/d4lab/wp-content/uploads/sites/23/2017/02/2461645.pdf .
- Rees, M. and Long, M. J. (1992), *Germination Biology and the Ecology of Annual Plants*, *The American Naturalist* 139, 484–508. Accessible author's PDF: https://eprints.whiterose.ac.uk/id/eprint/1403/1/reesm8_Rees_and_Long_1992_Am_Nat.pdf .
- Rees, M. (1994), *Delayed Germination of Seeds: A Look at the Effects of Adult Longevity, the Timing of Reproduction, and Population Age/Stage Structure*, *The American Naturalist* 144, 43–64. https://doi.org/10.1086/285660 . Full accessible text: https://eprints.whiterose.ac.uk/id/eprint/1406/1/reesm11_Rees_1994_Am_Nat.pdf .
- Tielbörger, K. and Valleriani, A. (2005), *Can Seeds Predict Their Future? Germination Strategies of Density-Regulated Desert Annuals*, *Oikos* 111, 235–244. https://doi.org/10.1111/j.0030-1299.2005.14041.x .
- Valleriani, A. and Tielbörger, K. (2006), *Effect of Age on Germination of Dormant Seeds*, *Theoretical Population Biology* 70, 1–9. https://doi.org/10.1016/j.tpb.2006.02.003 .
- Valleriani, A. (2006), *Evolutionarily Stable Germination Strategies with Time-Correlated Yield*, *Theoretical Population Biology* 70, 255–261. https://doi.org/10.1016/j.tpb.2006.07.008 .
- Verin, M. (2018), *Seed Banking Strategies and Host-Parasite Coevolution*, doctoral thesis, Technical University of Munich, Supplementary Text S3, pp. 62–63. https://mediatum.ub.tum.de/download/1439955/1439955.pdf .
