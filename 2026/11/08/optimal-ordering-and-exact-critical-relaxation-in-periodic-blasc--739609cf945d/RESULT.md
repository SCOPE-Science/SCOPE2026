# Optimal ordering and exact critical relaxation in periodic Blaschke switching

## Finding
Let \(B_a(x)=\bigl((x+a)/(1+ax)\bigr)^2\), with \(0\le a<1\) and \(0\le x\le1\). The time-periodic composition of these finite Blaschke products has a *critical* boundary multiplier when the product of its derivatives at \(x=1\) over one switching block is exactly one. At this criticality, the rate of radial relaxation is not determined by switching frequencies alone: **ordering the same maps changes its sharp coefficient**. An explicit formula gives the extremal schedules, along with a two-term inverse-square asymptotic including a logarithmic correction.

For every integer \(m\ge1\), let the repeated driving word be \(a_0,\ldots,a_{m-1}\in[0,1)\). Define
\[
\lambda_j=\frac{2(1-a_j)}{1+a_j},\qquad
P_0=1,\qquad P_j=\prod_{i=0}^{j-1}\lambda_i,
\qquad \prod_{j=0}^{m-1}\lambda_j=1.
\]
Put \(C=\frac14\sum_{j=1}^m P_j^2\) and \(D=\frac1{16}\sum_{j=1}^m P_j^4\). For every \(x_0\in[0,1)\), let \(x_{n+1}=B_{a_{n\bmod m}}(x_n)\) and \(w_n=(1-x_n)/(1+x_n)\). Then \(x_n\to1\), and for some finite \(\Gamma(x_0)\),
\[
\boxed{w_{mk}^{-2}=2Ck+\frac{D}{2C}\log k+\Gamma(x_0)+o(1)}\quad(k\to\infty).
\]
For each \(0\le j<m\), the phase-resolved limit is
\[
\boxed{\lim_{k\to\infty}\sqrt{k}\,(1-x_{mk+j})=\sqrt{\frac2C}\,P_j}.
\]
For any fixed multiset of critical multipliers, \(C\) is smallest when the multipliers are nondecreasing and largest when they are nonincreasing; strict differences hold whenever a genuine adjacent inversion is exchanged. Thus the descending word has the fastest critical relaxation when observed at the same word phase. Ties are precisely the repeated equal multipliers.

For example, the same three maps with parameters \(0,1/3,3/5\), corresponding to multipliers \(2,1,1/2\), give \(C=9/4\) in descending order and \(C=3/8\) in ascending order. The coefficients of \(\log k\) in their inverse-square laws are \(11/24\) and \(3/32\), respectively. At an identical starting phase, the leading boundary deficit in the descending schedule is \(1/\sqrt6\) of that in the ascending schedule. Another exact critical pair, parameters \((0,3/5)\), gives \(w_{2k}^{-2}=\frac52k+\frac{17}{40}\log k+\Gamma(x_0)+o(1)\).

## Assumptions and scope
All statements concern **real radial initial states** \(x_0\in[0,1)\), the given order repeated periodically, and finite \(m\). The excluded endpoint \(x_0=1\) is an exact fixed point of every map, where the inverse-square coordinate is undefined. Parameters are real with \(0\le a_j<1\), so every \(\lambda_j\) is positive; criticality is the exact product-one condition, rather than an expectation or approximate equality. The extremal-order statement compares words at the same first observation phase, with the same multiset of multipliers and the same number of steps per block.

## Proof
**Exact conjugation.** Put \(q_j=(1-a_j)/(1+a_j)=\lambda_j/2\). For \(w=(1-x)/(1+x)\), direct rational simplification yields
\[
\frac{1-B_{a_j}(x)}{1+B_{a_j}(x)}
=\frac{2q_jw}{1+q_j^2w^2}
=\frac{\lambda_jw}{1+q_j^2w^2}.
\]
Since \(0<w\le1\) and \(q_j>0\), every subsequent \(w\) stays positive. Define \(L_n=P_{n\bmod m}\). Criticality implies \(P_m=P_0=1\), so \(L_{n+1}=\lambda_{n\bmod m}L_n\), including at block boundaries. With \(v_n=w_n/L_n\),
\[
v_{n+1}=\frac{v_n}{1+c_{n\bmod m}v_n^2},\qquad
c_j=(q_jP_j)^2=\frac14P_{j+1}^2>0.
\]
For \(Z_n=v_n^{-2}\) this gives the **exact positive recurrence**
\[
\boxed{Z_{n+1}=Z_n+2c_{n\bmod m}+\frac{c_{n\bmod m}^2}{Z_n}}.
\]
No asymptotic approximation has been used so far. Because \(c_j>0\), \(Z_n\) increases at least linearly and \(v_n\to0\). The finitely many \(L_n\) are bounded, hence \(w_n\to0\), which is equivalent to \(x_n\to1\).

**Two-term asymptotic.** Let \(C=\sum_{j=0}^{m-1}c_j\) and \(D=\sum_{j=0}^{m-1}c_j^2\), equal to the displayed expressions in the partial products. The recurrence gives \(Z_{mk}=2Ck+O(\log(k+2))\): its extra positive terms are bounded by a constant multiple of \(\sum_{n<mk}(n+1)^{-1}\), since \(Z_n\) has a positive linear lower bound. For fixed \(0\le j<m\), it also gives \(Z_{mk+j}=2Ck+O(\log(k+2))\). Define the exact block remainder
\[
R_k=Z_{m(k+1)}-Z_{mk}-2C=\sum_{j=0}^{m-1}\frac{c_j^2}{Z_{mk+j}}.
\]
For \(k\ge1\), the preceding bounds imply
\[
R_k=\frac{D}{2Ck}+O\left(\frac{\log(k+1)}{k^2}\right).
\]
The difference is absolutely summable. Comparing the telescoping sum of the block remainders with the harmonic series yields the finite limit
\[
\Gamma(x_0)=\lim_{k\to\infty}\left(Z_{mk}-2Ck-\frac{D}{2C}\log k\right).
\]
At the block start, \(L_{mk}=1\), so \(Z_{mk}=w_{mk}^{-2}\). At phase \(j\), the same estimates give \(w_{mk+j}=P_j/\sqrt{2Ck+O(\log k)}\). Using \(1-x=2w/(1+w)\) proves every phase-resolved limit.

**Optimal order.** The exact formula \(C=\frac14\sum_{j=1}^m P_j^2\) involves squared prefix products, with \(P_m=1\) fixed. If two adjacent multipliers \(\alpha>\beta\) appear after a common prefix product \(L>0\), swapping them changes exactly one summand, from \((L\alpha)^2/4\) to \((L\beta)^2/4\); every later prefix product is unchanged. The swap strictly lowers \(C\). Repeated inversion removal proves the ascending minimum; reversing the swap argument proves the descending maximum. Identical multipliers are the only exchange ties. Since the boundary deficit is proportional to \(C^{-1/2}\), these are respectively slowest and fastest phase-zero schedules. This is a global comparison valid for every radial initial state because the leading constant is initial-state independent.

## Verification
Running `python verify.py` confirms the symbolic Cayley conjugacy and inverse-square algebra; checks the rational coefficients and the partial-product identity in four critical words; exhaustively checks the sorting extremum in three small rational multiplier multisets; and tests 12 real-radial high-precision runs for up to 20,000 complete blocks at 75 decimal-digit precision. The tests establish only finite arithmetic corroboration. The infinite convergence, logarithmic coefficient, and extremal-order assertions follow from the preceding proof, not from extrapolation.

## Relationship to prior work
González-Tokman and Oldfield (2026) analyze random Blaschke compositions, including the exact family above with one map expanding and another contracting at the common boundary fixed point. Their Theorem 3.2 establishes a distribution-dependent transition and a distinct iid critical behavior; Remark 3.8 recalls deterministic parabolic behavior. The present theorem does **not** claim that deterministic parabolic convergence or the exponent \(1/2\) is new. Classical Leau–Fatou theory supplies local power laws, and analytic theory of parabolic germs gives formal power-logarithmic expansions. The new quantitative content is the **explicit global, phase-resolved coefficient formula for arbitrary critical switching words and its sharp rearrangement extremizers at fixed frequencies**, with the exact logarithmic coefficient derived from a positive recurrence. Generic local parabolic theorems and the motivating random-cocycle classification do not state this word-order comparison. The claim is provisional concerning historical priority, pending independent literature examination.

## Limitations
The result does not describe iid or other aperiodic switching, nonreal initial points, or Lebesgue-typical points of the unit circle. A finite block is essential for the partial-product rearrangement. The additive constant \(\Gamma(x_0)\) is proved to exist but not expressed in elementary form. General parabolic-germ theory already implies a leading power-law and qualitative existence of asymptotic logarithmic terms; neither feature in isolation is claimed as novel. Independent mathematical review and historical-priority verification remain outstanding.

## References
1. C. González-Tokman and R. Oldfield, *The transition between synchronization and chaos for random Blaschke products*, arXiv:2607.15488v1 (first submitted 16 July 2026), especially Theorem 3.2 and Remark 3.8. https://arxiv.org/html/2607.15488
2. J. Reppekus, *Small divisors in discrete local holomorphic dynamics*, Boll. Unione Mat. Ital. 16 (2023), 173–202, especially Theorem 14 (Leau–Fatou). https://doi.org/10.1007/s40574-023-00362-y
3. M. Klimeš, P. Mardešić, G. Radunović and M. Resman, *Analytic invariants of a parabolic diffeomorphism from its orbit*, arXiv:2112.14324v1 (2021), Section 1.1 on the power-logarithmic asymptotic expansion. https://arxiv.org/abs/2112.14324
