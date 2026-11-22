# Two-phenotype drug-order rigidity and a sharp three-phenotype duration reversal

## Finding

In a linear phenotypically switching microbial population exposed once to each of two drugs, the **sign** of the difference in final total abundance between the two drug orders is independent of both positive exposure durations whenever there are at most two phenotypes. For two phenotypes, the sign is exactly the sign of
\[
\bigl[(a_1-a_2)-(b_1-b_2)\bigr](r x_2-s x_1),
\]
where \(a_i,b_i\) are phenotype-specific drug-induced losses, \(r,s>0\) are switching rates, and \(x_i\geq0\) are initial abundances. Equality of either factor forces identical total abundance for every pair of durations, including the case where the initial phenotype ratio is the stationary ratio of untreated switching.

Three phenotypes are necessary and sufficient for a reversal **caused solely by changing the common duration of the same two drug pulses**. Explicit three-phenotype matrices, a fixed initial state and two rational exposure durations exhibit strictly opposite drug-order preferences.

## Assumptions and scope

A population abundance column vector \(x(t)\) satisfies \(\dot x=Mx\) between instantaneous drug changes, with constant linear phenotype transitions, phenotype-specific net growth and nonnegative phenotype-specific drug-induced loss. Each drug is administered for one contiguous positive-duration interval, with the order reversed for comparison, but without a gap, dose adaptation or cumulative-state feedback. The readout is final **total** abundance, not the abundance of a designated phenotype, long-run periodic growth, or patient outcome.

For two phenotypes, define
\[
Q=\begin{pmatrix}-s&r\\s&-r\end{pmatrix},\quad
G=\operatorname{diag}(g_1,g_2),\quad
A=Q+G-\operatorname{diag}(a_1,a_2),\quad
B=Q+G-\operatorname{diag}(b_1,b_2),
\]
with \(s,r>0\), \(g_i\in\mathbb R\), \(a_i,b_i\geq0\), and \(x=(x_1,x_2)^\top\geq0\), nonzero. Drug A acts for \(u>0\), and drug B for \(v>0\). Let
\[
N_{AB}(u,v)=\mathbf1^\top e^{vB}e^{uA}x,\qquad
N_{BA}(u,v)=\mathbf1^\top e^{uA}e^{vB}x.
\]
The matrix exponentials are mean-population propagators. They do not specify a stochastic extinction probability.

## Proof

**Exact two-phenotype factorization.** A real two-by-two matrix \(M\) of the above form has strictly positive off-diagonal entries \(r,s\), hence distinct real eigenvalues \(\lambda_+(M)>\lambda_-(M)\): the discriminant is the sum of a square and \(4rs>0\). Cayley–Hamilton interpolation gives
\[
e^{tM}=\alpha_M(t)I+\beta_M(t)M,\qquad
\beta_M(t)=\frac{e^{t\lambda_+(M)}-e^{t\lambda_-(M)}}{\lambda_+(M)-\lambda_-(M)}>0\quad(t>0).
\]
Consequently
\[
e^{vB}e^{uA}-e^{uA}e^{vB}
=\beta_A(u)\beta_B(v)(BA-AB).
\]
Writing \(D=B-A=\operatorname{diag}(a_1-b_1,a_2-b_2)\), we have
\[
BA-AB=DA-AD
=\bigl[(a_1-a_2)-(b_1-b_2)\bigr]
\begin{pmatrix}0&r\\-s&0\end{pmatrix}.
\]
Multiplication by \(\mathbf1^\top\) and \(x\) proves the exact identity
\[
\boxed{N_{AB}(u,v)-N_{BA}(u,v)
=\beta_A(u)\beta_B(v)\bigl[(a_1-a_2)-(b_1-b_2)\bigr](r x_2-s x_1).}
\]
Both duration factors are strictly positive. Thus the sign or equality is independent of \(u,v>0\) and the common phenotype-specific growth rates; the latter affect only the strictly positive multiplier. If \(x\) is proportional to \((r,s)^\top\), the two drug orders have exactly equal final total abundance for every \(u,v\). For one phenotype, scalar propagators commute, so no preference is possible.

**Three-phenotype witness.** Let the same symmetric phenotype-switching generator operate under both drugs,
\[
Q=\begin{pmatrix}-1&1&0\\1&-2&1\\0&1&-1\end{pmatrix},\quad
A=Q-\operatorname{diag}(0,0,1)
=\begin{pmatrix}-1&1&0\\1&-2&1\\0&1&-2\end{pmatrix},
\]
\[
B=Q-\operatorname{diag}(0,1,0)
=\begin{pmatrix}-1&1&0\\1&-3&1\\0&1&-1\end{pmatrix},\quad
x=(1,0,0)^\top.
\]
Both drugs only remove population; no reproduction or mutation is assumed. For equal positive durations \(t\), set
\[
\Delta(t)=\mathbf1^\top\bigl(e^{tB}e^{tA}-e^{tA}e^{tB}\bigr)x.
\]
The exact-rational Taylor calculation supplied in `checker.py` proves
\[
\Delta(1/5)<-0.0161993460152<0,\qquad
\Delta(1)>0.0092842024968>0.
\]
Here the two displayed decimal magnitudes are certified strictly by rational inequalities: the script builds all Taylor terms through degree 40 as `Fraction` and bounds the absolute evaluation error by \(6(512\varepsilon+\varepsilon^2)\), where
\[
\varepsilon=256\cdot5^{41}/41!<4\times10^{-19},
\qquad6(512\varepsilon+\varepsilon^2)<1.1\times10^{-15}.
\]
Indeed \(\lVert A\rVert_\infty\le4\), \(\lVert B\rVert_\infty\le5\), \(0<t\le1\), and \(e^5<256\); the matrix Taylor remainder obeys \(\lVert e^{tM}-\sum_{j=0}^{40}(tM)^j/j!\rVert_\infty\le\varepsilon\). Both product differences and the column sum then have the stated error bound. Strict opposite signs imply a duration-induced order reversal by continuity. Replacing the initial vector by \((1,\delta,\delta)^\top\) for sufficiently small \(\delta>0\) preserves both strict inequalities. Therefore three is the **minimal phenotype count** for this effect.

## Verification

Run `python3 checker.py` using only the Python standard library. It constructs the exact displayed matrices, independently evaluates both ordered products at the two stated rational times, checks the rational remainder bounds, and asserts both strict signs. Its two certified differences are approximately \(-0.016199346015221782\) and \(+0.0092842024968862\); the absolute error bound in either case is less than \(1.1\times10^{-15}\). This computer certificate proves only the two explicit signs. The all-parameter two-phenotype result and its minimality use the preceding analytic factorization.

## Relationship to prior work

Balaban et al. (2004) documented persistence and phenotype switching in microbial populations; the present mathematical framework idealizes that mechanism. Zucca (2012, arXiv version) analyzes persistent/susceptible populations under repeated killing pulses and extinction criteria rather than reversed orders of two different fixed loss profiles. Roemhild et al. (2015) establish experimentally that antibiotic treatment order matters over long evolutionary schedules, a substantially richer mechanism involving adaptation, not the present two-pulse, non-evolving linear calculation. Patra and Klumpp (2015) analyze phenotype switching under fluctuating environments; only their abstract and bibliographic description were accessible for comparison. No claim is made that matrix-exponential identities or the general commutator principle are new: the contribution is the sharp constrained biological minimality and the rigorously certified three-phenotype reversal under the same switching generator.

## Limitations

The model is an exact mechanistic benchmark, not a recommendation for antibiotic prescription. Its two-pulse duration rigidity is specific to two phenotypes with common drug-independent switching and common growth; it does not cover drug-induced phenotype changes, nonconstant dose, time-varying switch rates, density limitation, stochastic extinction, evolution of resistance, or longer sequences of pulses. The three-state witness demonstrates existence, not a universal classification in higher dimension. The original 2004 full text and some related full papers could not be exhaustively compared; historical priority is provisional. Independent scientific audit and experimental validation have not been performed.

## References

1. Balaban, N. Q. et al. (2004), *Bacterial Persistence as a Phenotypic Switch*, *Science* **305**, 1622–1625. First online publication August 12, 2004. https://doi.org/10.1126/science.1099390
2. Zucca, F. (2012), *Persistent and susceptible bacteria with individual deaths*, initial preprint October 15, 2012. https://arxiv.org/abs/1210.4074
3. Roemhild, R. et al. (2015), *Temporal variation in antibiotic environments slows down resistance evolution in pathogenic Pseudomonas aeruginosa*, *Evolutionary Applications* **8**, 945–955. https://doi.org/10.1111/eva.12330
4. Patra, P. and Klumpp, S. (2015), *Emergence of phenotype switching through continuous and discontinuous evolutionary transitions*, *Physical Biology* **12**, 046004. https://doi.org/10.1088/1478-3975/12/4/046004
