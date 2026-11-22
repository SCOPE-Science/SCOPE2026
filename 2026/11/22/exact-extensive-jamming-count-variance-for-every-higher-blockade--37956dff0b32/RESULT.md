# Exact extensive jamming-count variance for every higher-blockade square ladder

## Finding

Let \(N_{b,L}\) be the terminal number of accepted sites in uniform-priority random sequential adsorption on the open two-row square ladder of \(L\) rungs. Two sites may both be accepted only if their shortest-path distance in the *original* ladder exceeds the integer blockade range \(b\). For every fixed integer \(b\geq2\),
\[
\operatorname{Var}(N_{b,L})=\nu_b L+o(L),\qquad 0<\nu_b<\infty.
\]
The coefficient \(\nu_b\) is specified **exactly**, without a thermodynamic extrapolation, by the positive convergent quadrature and recursion below. For blockade two,
\[
\boxed{\nu_2=0.0267945787085631864907625185535\ldots}.
\]
The corresponding mean per rung is the previously established constant \(\mu_2=0.381675958258806\ldots\), giving \(\nu_2/\mu_2\approx0.0702\). The finding concerns the **dynamically selected** jammed configuration, not a uniformly sampled maximal independent set. It does not assert a new central limit theorem.

## Assumptions and scope

At each vertex independently draw a continuous uniform priority. Inspect vertices in increasing priority and accept a vertex exactly if no previously accepted vertex lies at graph distance at most \(b\). This is equivalent to repeated uniformly choosing an available vertex until saturation. Both horizontal ladder edges and vertical rung edges count as unit graph distance, including paths through vertices that have become unavailable. There are two vertices per rung. The range \(b\) is fixed as \(L\to\infty\); the asserted coefficient has no varying-range interpretation.

Write \(A_{b,k}\) and \(B_{b,k}\) for the terminal counts on the two staggered boundary geometries introduced by Došlić, Puljiz, Šebek and Žubrinić (their Figure 3): the \(A\) geometry contains top positions \(0,\ldots,k-1\) and bottom positions \(1,\ldots,k\); the \(B\) geometry contains top positions \(1,\ldots,k-1\) and bottom positions \(0,\ldots,k\), with distances measured in the ambient square ladder. Thus each nonempty geometry contains \(2k\) sites. Define an empty \(A\) geometry of size zero by deterministic count zero, and a singleton \(B\) geometry of size zero by deterministic count one. For negative indices both counts are deterministically zero. The following recursion is an exact specification of all quantities in the coefficient.

For \(k\geq1\), let \(m^A_k=\mathbb E A_{b,k}\), \(m^B_k=\mathbb E B_{b,k}\), initialized by \(m^A_0=0,m^B_0=1\) and zero at negative indices. Form two multisets of exactly \(2k\) numbers:
\[
\begin{aligned}
\mathcal Y^A_k={}&\{m^A_{j-b}+m^B_{k-j-b}:0\leq j<k\}\\
&\mathbin{\cup}\{m^B_{j-b}+m^A_{k-j-b}:1\leq j\leq k\},\\
\mathcal Y^B_k={}&\{m^A_{j-b}+m^A_{k-j-b}:0\leq j\leq k\}\\
&\mathbin{\cup}\{m^B_{j-b}+m^B_{k-j-b}:1\leq j<k\}.
\end{aligned}
\]
Here \(\cup\) means **multiset concatenation**, so repeated values retain multiplicity. Define for \(S\in\{A,B\}\)
\[
 m^S_k=1+\frac1{2k}\sum_{y\in\mathcal Y^S_k}y,\qquad
 T^S_k=\frac1{2k}\sum_{y\in\mathcal Y^S_k}y^2-\left(m^S_k-1\right)^2,
\qquad T_k=\frac{T^A_k+T^B_k}{2}.
\]
The \(T^S_k\) are nonnegative variances of finite multisets and are computable using *only first moments*, which themselves are determined sequentially by the displayed recurrence.

Put
\[
 P_b(z)=\frac{z^b}{b}+2\sum_{j=1}^{b-1}\frac{z^j}{j},\qquad
 H_b'(z)=\sum_{k\geq1}kT_k z^{k-1}.
\]
The promised exact coefficient is
\[
\boxed{\displaystyle
\nu_b=e^{-P_b(1)}\int_0^1e^{P_b(t)}(1-t)^2H_b'(t)\,dt
=e^{-P_b(1)}\sum_{k\geq1}kT_k\int_0^1 e^{P_b(t)}(1-t)^2t^{k-1}\,dt.}
\]
Both formulas converge absolutely, give the same positive number, and require no choice of finite-size extrapolation.

## Proof

**1. Exact first-split law.** Choose the first accepted vertex uniformly from the \(2k\) candidates in geometry \(A\) or \(B\). Its blockade removes a neighborhood, leaving two disjoint independent subproblems with the index pairs and shape labels displayed in \(\mathcal Y^A_k,\mathcal Y^B_k\). The first vertex contributes one. Independence follows from independent initial priorities after conditioning on the first. This proves the first-moment recursion (the split geometries and mean recurrence themselves are established in the original ladder study). It also proves, by conditional variance,
\[
\begin{aligned}
 v^A_k&=\frac1{2k}\sum_{\mathcal Y^A_k}\left(v^{\mathrm{left}}+v^{\mathrm{right}}\right)+T^A_k,\\
 v^B_k&=\frac1{2k}\sum_{\mathcal Y^B_k}\left(v^{\mathrm{left}}+v^{\mathrm{right}}\right)+T^B_k,
\end{aligned}
\]
where \(v^A_k=\operatorname{Var}(A_{b,k})\), \(v^B_k=\operatorname{Var}(B_{b,k})\) and the child shapes and indices are the same as in the corresponding multiset. Both zero-index variances are zero.

**2. Averaged variance generating function.** Set \(V_k=(v^A_k+v^B_k)/2\) and \(V_0=0\). Summing the two exact conditional-variance equations gives
\[
 V_k=T_k+\frac2k\sum_{j=1}^{k-1}V_{j-b}+\frac1kV_{k-b}\quad(k\geq1),
\]
with negative-index terms zero. Therefore, for \(V(z)=\sum_{k\geq0}V_kz^k\),
\[
 V'(z)=\frac{z^{b-1}(1+z)}{1-z}V(z)+H_b'(z),\qquad V(0)=0.
\]
An integrating factor gives the **exact finite-volume generating function**
\[
 V(z)=\frac{e^{-P_b(z)}}{(1-z)^2}
 \int_0^z e^{P_b(t)}(1-t)^2H_b'(t)\,dt.\tag{1}
\]
No Gaussian or independence approximation was used to derive (1).

**3. Existence, positivity and coefficient asymptotics.** Let \(C_k=(m^A_k+m^B_k)/2\). The corresponding established mean recurrence has exact generating function
\[
 \sum_{k\geq0}C_kz^k=\frac{e^{-P_b(z)}}{(1-z)^2}
 \left(\frac12+\int_0^z e^{P_b(t)}\,dt\right).
\]
Writing
\[
 \mu_b=e^{-P_b(1)}\left(\frac12+\int_0^1e^{P_b(t)}\,dt\right),
\]
its entire numerator and the identity \(P_b'(1)=2b-1\) imply
\[
 C_k=\mu_b(k+2b)-1+O_R(R^{-k})
\]
for every fixed \(R>1\), with a constant depending on \(R\). The difference \(d_k=m^A_k-m^B_k\) obeys \(d_k=-d_{k-b}/k\), \(d_0=-1\); hence \(d_k=0\) unless \(k\) is a nonnegative multiple of \(b\), and \(d_{mb}=(-1)^{m+1}/(b^m m!)\) for \(m\geq1\). Thus each auxiliary mean is affine in its index up to factorially small corrections.

For every root split away from the two endpoints, the sum of the two affine child means is constant across roots. Subtracting that common value in the multiset variance leaves endpoint deviations with summable factorial tails. Consequently \(T_k=O(1/k)\), more precisely \(kT_k=K_b+D_b/k+O_R(R^{-k})\) for finite real constants \(K_b,D_b\). This proves the absolute convergence of the displayed integral, including its endpoint \(t=1\). It also yields \(H_b'(z)=K_b/(1-z)-D_b\log(1-z)/z+\text{an analytic remainder}\). Substitution in (1), followed by coefficient extraction at its only unit-circle singularity, proves \(V_k=\nu_b k+O(1)\). (The logarithmic term contributes only lower-order coefficient corrections.) The \(A/B\) variance difference obeys
\[
 v^A_k-v^B_k=-\frac{v^A_{k-b}-v^B_{k-b}}{k}+T^A_k-T^B_k=O(1/k),
\]
so each auxiliary variance separately has asymptotic slope \(\nu_b\).

For \(b\geq2\), at size \(k=b\), the \(A\) multiset has two entries equal to one and \(2b-2\) entries equal to zero, whereas the \(B\) multiset consists entirely of zeros. Hence \(T_b=(b-1)/(2b^2)>0\). All terms of the coefficient integral are nonnegative, so \(\nu_b>0\); finiteness was established above.

**4. Removing the staggered boundaries.** Couple the original length-\(L\) square ladder with \(A_{b,L}\) by assigning identical continuous priorities to their common vertices. Their vertex sets differ only by one terminal vertex at each end. A greedy acceptance discrepancy can propagate from such a local perturbation only along a path of successively *later* priorities in the finite-range conflict graph. With maximal conflict degree bounded by a constant \(D_b\), a prescribed self-avoiding path of length \(r\) has increasing priorities with probability \(1/(r+1)!\), and there are at most \(O(D_b^r)\) such paths from the finitely many affected boundary vertices. The number of differing accepted sites therefore has uniformly bounded second moment, independent of \(L\). Cauchy–Schwarz and \(\operatorname{Var}(A_{b,L})=O(L)\) give
\[
 \operatorname{Var}(N_{b,L})-\operatorname{Var}(A_{b,L})=O(\sqrt L)=o(L).
\]
This transfers the exact asymptotic coefficient from the staggered split geometry to the **original open square ladder**.

## Verification

The supplied standalone `checker.py` computes both auxiliary count distributions by exact rational first-split convolution, checks them against direct random-priority enumeration of the underlying two-row geometry for small sizes, checks the variance recurrence, and recomputes \(\nu_2\) from high-precision dynamic programming. These are finite cross-checks of the preceding infinite proof, not a substitute for its singularity and stabilization arguments. An additional independently implemented random-priority simulation of 30,000 ordinary square ladders at each of \(L=80,160,320\) yielded empirical variance-per-rung values approximately \(0.02696,0.02673,0.02681\), consistent with the exact value but not used as proof.

## Relationship to prior work

Došlić, Puljiz, Šebek and Žubrinić (arXiv:2312.02747, originally public 2023-12-05) establish the higher-blockade square-ladder model, its two boundary recurrences **for the mean**, the dynamic mean per rung, and static jammed-state complexity. Those mean results and their boundary decomposition are used here, not re-presented as new. Chern, Hwang and Tsai (arXiv:1406.0614) derive full counting and limit laws for **nearest-neighbor blockade \(b=1\)**; the present novelty is the exact extensive variance for every fixed higher blockade \(b\geq2\). General stabilization/central-limit theorems for random sequential adsorption already establish existence of Gaussian fluctuations in broad finite-range settings; no new general CLT is claimed. Static generating functions for uniformly sampled jammed configurations are different from the dynamically sampled law and do not give the displayed variance coefficient.

## Limitations

The positive quadrature is an exact convergent characterization, not an elementary closed form. The numerical decimal for \(b=2\) is a high-precision evaluation rather than a formally interval-certified rounding. The result covers fixed blockade range, open boundaries, and uniform independent priorities; it does not describe a growing blockade range, periodic ladders at finite size, time-dependent deposition counts, or the uniform static jammed-state ensemble. The result has not received independent scientific audit. Equivalent unindexed higher-blockade fluctuation calculations remain possible in the broader RSA literature.

## References

- T. Došlić, M. Puljiz, S. Šebek and J. Žubrinić, *A model of random sequential adsorption on a ladder graph*, arXiv:2312.02747 (first public 2023-12-05), https://arxiv.org/abs/2312.02747 . See Section 2, especially equations (2.1)–(2.9) and Figures 3–5, and Sections 3–4 on static complexity.
- H.-H. Chern, H.-K. Hwang and T.-H. Tsai, *Random unfriendly seating arrangement in a dining table*, arXiv:1406.0614 (2014 preprint, 2015 revision), https://arxiv.org/abs/1406.0614 . See the two-row nearest-neighbor probability-generating-function and fluctuation results.
- C. Spahn and D. Zeilberger, *Enumerating Seating Arrangements that Obey Social Distancing*, arXiv:2401.12430, https://arxiv.org/abs/2401.12430 . Static seating enumerations, not the dynamic higher-blockade variance.
- E. Coletti et al., *Fluctuations of the Occupation Density for a Parking Process*, Journal of Statistical Physics (2024), https://doi.org/10.1007/s10955-024-03336-2 . General occupation-density fluctuation and stabilization context.
