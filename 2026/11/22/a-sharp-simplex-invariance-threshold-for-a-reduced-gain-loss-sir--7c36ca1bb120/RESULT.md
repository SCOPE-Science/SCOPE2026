# A sharp simplex-invariance threshold for a reduced gain–loss SIR step

## Finding

Consider the closed susceptible–infected–recovered (SIR) equations with constant infection and recovery parameters \(\beta,\gamma>0\) and total population \(N>0\). Specialize the explicit, componentwise gain–loss update of Zinihi–Ehrhardt–Sidi Ammi to the **exact physical rate functions** (not independently fitted neural rate functions), update susceptible and infected populations separately, and reconstruct recovered population as the residual of the fixed total. With a positive denominator value \(\phi>0\), its normalized map is
\[
s_+=\frac{s}{1+\tau\rho i},\qquad
 i_+=\frac{i(1+\tau\rho s)}{1+\tau},\qquad
 r_+=1-s_+-i_+,
\]
where \(s=S/N\), \(i=I/N\), \(r=R/N\), \(\tau=\gamma\phi>0\) and \(\rho=\beta N/\gamma>0\). The physical simplex is \(\Sigma=\{(s,i,r)\in\mathbb R_{\ge0}^3:s+i+r=1\}\).

**Sharp complete theorem.** For every \(\rho>0\) and \(\tau>0\), the map sends **every** point of \(\Sigma\) back into \(\Sigma\) if and only if
\[
\boxed{\ \tau\rho(\rho-4)\le4.\ }
\]
Thus for \(0<\rho\le4\) it is simplex-preserving for all positive denominator values. For \(\rho>4\) it is simplex-preserving exactly for
\[
0<\tau\le\tau_c(\rho):=\frac4{\rho(\rho-4)}.
\]
For the admissible standard denominator \(\phi(h)=h\), this is the sharp physical step-size restriction
\[
0<h\le h_c=\frac{4\gamma}{\beta N(\beta N-4\gamma)}\qquad(\beta N>4\gamma).
\]
For a general positive NSFD denominator \(\phi(h)\), the criterion is applied to \(\tau=\gamma\phi(h)\); a bounded denominator may retain simplex invariance even when \(\rho>4\).

There is an exact failure geometry when \(\rho>4\) and \(\tau>\tau_c(\rho)\): on the face \(r=0\), the output \(r_+\) is negative precisely at
\[
i_-<i<i_+,\quad i_\pm=\frac{1\pm\sqrt{1-4/\rho-4/(\tau\rho^2)}}2,\quad s=1-i.
\]
For any \(i\in[0,1]\), the full simplex interior is unsafe precisely if \(s>s_*(i)\) subject to \(s+i\le1\), where
\[
s_*(i)=\frac{(1+\tau-i)(1+\tau\rho i)}{1+\tau+\tau\rho i(1+\tau\rho i)}.
\]
Such unsafe states exist only when \(i\in(i_-,i_+)\). At the threshold \(\tau=\tau_c\), the boundary state \((s,i,r)=(1/2,1/2,0)\) is mapped to a state with \(r_+=0\); immediately above it the same input has \(r_+<0\). For example, \(\rho=5\), \(\tau=1\) and \((s,i,r)=(1/2,1/2,0)\) give \((s_+,i_+,r_+)=(1/7,7/8,-1/56)\).

## Assumptions and scope

The claim concerns one **completed deterministic numerical step** and all initial states in the closed simplex. Parameters \(N,\beta,\gamma\) are strictly positive and constant. The same positive scalar denominator is used for both modeled components. The gain and loss outputs are exactly \(G_S=0\), \(L_S=\beta I\), \(G_I=\beta SI\), and \(L_I=\gamma\), evaluated as prescribed by the diagonal gain–loss rule. It does **not** cover independently trained rate networks whose outputs differ from these functions.

The result concerns the set preservation of the full three-component reconstructed state. The two directly updated components \(s_+,i_+\) remain nonnegative for all \(\rho,\tau>0\), even in the failure region. Conservation \(s_++i_++r_+=1\) holds by residual definition but is not, by itself, a positivity guarantee.

## Proof

**1. Positive modeled coordinates.** The denominator of each rational expression is strictly positive. Because \(s,i\ge0\), both \(s_+,i_+\ge0\). Thus the sole remaining constraint is \(r_+\ge0\).

**2. The boundary is the worst case.** At fixed \(i\in[0,1]\), write
\[
r_+(s,i)=1-\frac{i}{1+\tau}-s\left[\frac1{1+\tau\rho i}+\frac{\tau\rho i}{1+\tau}\right].
\]
The bracket is strictly positive. Every point in \(\Sigma\) satisfies \(0\le s\le1-i\); consequently, for each fixed \(i\), \(r_+\) is minimized at the boundary input \(s=1-i\) (equivalently \(r=0\)). This reduction is exact, not a numerical approximation.

**3. The sharp global criterion.** Elementary common-denominator algebra at that boundary yields
\[
r_+(1-i,i)=\frac{\tau i\bigl(1+\tau\rho-\tau\rho^2 i(1-i)\bigr)}{(1+\tau)(1+\tau\rho i)}.
\]
For \(i=0\) the quantity is zero. For \(0<i\le1\), its sign is the sign of the numerator in parentheses. Since \(0\le i(1-i)\le1/4\), with equality precisely when \(i=1/2\), that numerator is nonnegative for **all** \(i\in[0,1]\) if and only if
\[
1+\tau\rho-\frac{\tau\rho^2}{4}\ge0.
\]
This is exactly \(\tau\rho(\rho-4)\le4\). The equality case is included. When the inequality fails, \(i=s=1/2\) is a concrete counterexample; direct substitution gives
\[
r_+(1/2,1/2) =\frac{\tau\left[4-\tau\rho(\rho-4)\right]}{4(1+\tau)(2+\tau\rho)}.
\]
The strict sign and sharpness follow without any compactness approximation.

**4. Full unsafe region.** If \(\rho>4\) and \(\tau>4/[\rho(\rho-4)]\), the boundary numerator is negative exactly when
\[
i(1-i)>\frac1\rho+\frac1{\tau\rho^2}.
\]
The discriminant \(1-4/\rho-4/(\tau\rho^2)\) is then strictly positive, giving exactly \(i_-<i<i_+\). In the whole simplex, the strictly decreasing affine dependence of \(r_+\) on \(s\) gives the exact threshold \(s_*(i)\) displayed above. The intersection with \(s\le1-i\) is nonempty exactly for those infected fractions between the two boundary roots. Strictly interior counterexamples exist by taking \(s\) slightly smaller than \(1-i\), since \(r_+\) is continuous.

**5. Uniform iterates.** If the global criterion holds for fixed \(\rho,\tau\), every step maps \(\Sigma\) into itself, so induction proves nonnegativity of all reconstructed components at every iteration. Conversely, failure of this global one-step criterion already produces a negative recovered population after one step from a nonnegative initial state, so no all-initial-data all-step guarantee is possible. The result does not say that every trajectory fails when the criterion fails.

## Verification

Run the standard-library-only `verify.py` embedded alongside this text. It checks the symbolic rational factorization via polynomial coefficient comparisons using exact fractions, the sharp boundary example \((\rho,\tau)=(5,1)\), equality at the threshold, the exact unsafe-interval endpoints for a rational square-discriminant case, and representative rational grid values on each side of the proven threshold. Its finite tests corroborate the algebra; the universal quantifiers are established exclusively by the proof above.

The explicit example is \(s_+=1/7\), \(i_+=7/8\), so \(r_+=1-1/7-7/8=-1/56\). On the other hand, the source paper's physical demonstration parameters \(\beta=0.4\), \(\gamma=0.1\), \(N=1\) give \(\rho=4\), which lies **exactly** on the all-denominator-safe side for the **physical-rate specialization**. Its independently trained gain/loss networks need not obey these physical identities, so any negative recovered values from such networks do not contradict this theorem.

## Relationship to prior work

Zinihi, Ehrhardt and Sidi Ammi (2026), Sections 3–5, introduce the diagonal rational gain–loss update, establish nonnegativity of the explicitly modeled components, and explain in Remark 2 that algebraically reconstructed recovered population is **not** guaranteed nonnegative. They do not give this sharp rate–step simplex-invariance criterion or the unsafe-state interval. The construction and the warning are credited; the contribution here is their exact necessary-and-sufficient quantitative resolution **under the specified physical-rate specialization**.

Earlier SIR-specific NSFD methods, including the sequential incidence update in the 2014 vaccination study and the 2022 predictor–corrector schemes, use the **updated susceptible** component in the newly infected gain and often update the recovered component directly or construct a conserving flux. Their positivity and conservation assertions are not statements about the different, diagonally evaluated gain term \(\beta S^n I^n\) used here. The known coupled-flux repair is not claimed as a discovery.

Searches of mathematical research records and published literature for the exact source, formula, reproduction-ratio threshold, and equivalent simplex-cone formulations did not identify a theorem implying the displayed criterion. This is a best-knowledge originality assessment, not a guarantee against unindexed equivalent derivations.

## Limitations

The threshold guarantees every-state simplex invariance only for exact constant SIR rates. It is **not** a guarantee for fitted, approximate, time-dependent or independent learned gain/loss functions. It establishes no convergence rate, statistical learning guarantee, nonlinear epidemic-model result beyond this exact specialization, or behavior of negative components after departure from the physical simplex. In particular, the usual continuous-time epidemic threshold \(\rho=1\) is a different concept from the numerical feasibility boundary \(\rho=4\). The analysis is deterministic and exact-arithmetic; finite-precision implementation may incur small rounding violations near equality.

## References

1. A. Zinihi, M. Ehrhardt and M. R. Sidi Ammi, *Structure-Preserving Neural ODEs via Nonstandard Finite Difference Discretization*, arXiv:2607.10858v1 (first public 2026-07-12), Sections 3–5 and Remark 2. https://arxiv.org/abs/2607.10858
2. *An NSFD scheme for SIR epidemic models of childhood diseases with constant vaccination strategy*, *Advances in Difference Equations* 2014, article 172, Section 3 equations (3.1)–(3.2). https://doi.org/10.1186/1687-1847-2014-172
3. *Efficient Numerical Solutions to a SIR Epidemic Model*, *Mathematics* 2022, 10(18), 3299, Sections 3 and 6. https://doi.org/10.3390/math10183299
4. *Nonstandard Finite Difference Schemes for an SIR Epidemic Model*, *Mathematics* 2021, 9(23), 3082, Sections 3–4. https://doi.org/10.3390/math9233082
