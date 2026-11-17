# A moving-time extinction crossover in a three-type stochastic mixture

## Finding
Consider the three-type stochastic map of Jamilov–Mukhamedov–Mukhamedova–Souissi, Example 3.9, at its maximal interaction parameter \(2b=1\). Denote the third type's mass at generation \(n\) by \(s_n\). The map has two sharply different extinction laws: when the mixing parameter \(\alpha\) vanishes, extinction is doubly exponential, whereas for any fixed interior mixing parameter it is asymptotically geometric. The singular crossover admits an explicit universal profile.

Fix any strictly positive initial state \((a_0,a_1,a_2)\) with \(a_0+a_1+a_2=1\); set \(q=a_0a_2\in(0,1/4)\), and fix \(c>0\). For each sufficiently large integer \(N\), choose
\[
r_N=cq^{2^{N-1}},\qquad
\alpha_N=\frac{1-\sqrt{1-2r_N}}2.
\]
Run a separate trajectory with parameter \(\alpha_N\), always from the same initial state, and call its third coordinate \(s_j^{(N)}\). Then
\[
\boxed{\lim_{N\to\infty}\frac{s_N^{(N)}}{r_N}=\frac1c,\qquad
\lim_{N\to\infty}\frac{s_{N+\ell}^{(N)}}{r_N^{\ell+1}}=\frac{1+c}{c^2}\quad(\ell=1,2,\ldots\ \text{fixed}).}
\]
For the endpoint map \(\alpha=0\), its exact law is \(s_n=q^{2^{n-1}}\) for \(n\ge1\). For every fixed \(0<\alpha<1\), setting \(r=2\alpha(1-\alpha)\), one has \(s_{n+1}/s_n\to r\) and, more strongly, \(s_n/r^n\to L(\alpha,a_0,a_1,a_2)\in(0,\infty)\). Thus the moving-time theorem resolves the nonuniform transition between these two fixed-parameter laws. The crossover is at roughly the double-logarithmic time \(\log_2 |\log r|\); no uniform claim for offsets growing with \(N\) is made.

## Assumptions and scope
For \(0\le\alpha\le1\) and \((x_0,x_1,x_2)\) in the probability simplex, one step of the explicitly studied map is
\[
\begin{aligned}
x_0'&=\alpha+[(1-\alpha)x_0-2\alpha x_1]x_2,\\
x_1'&=1-\alpha+[\alpha x_1-2(1-\alpha)x_0]x_2,\\
x_2'&=[\alpha x_1+(1-\alpha)x_0]x_2.
\end{aligned}
\]
The parameter \(b\) is fixed at \(1/2\), and the orbit's simplex constraints are preserved because this map is the convex combination of two simplex-preserving quadratic maps in the source. The initial state is strictly interior and fixed as \(N\to\infty\), with \(q\in(0,1/4)\). The scalar \(c>0\) is fixed. Within each trajectory \(\alpha_N\) does not vary with time. The claims cover this exact family and make no assertion about arbitrary stochastic operators, perturbations of the map, boundary states with \(q=0\), or offsets \(\ell\) tending to infinity.

## Proof
**1. Reduction to a two-step recurrence.** Put \(s_n=x_{2,n}\), \(u_n=(1-\alpha)x_{0,n}+\alpha x_{1,n}\), and \(r=2\alpha(1-\alpha)\). Direct substitution, using \(x_{0,n}+x_{1,n}=1-s_n\), gives the exact identities
\[
s_{n+1}=u_ns_n,\qquad
u_{n+1}=s_{n+1}+rB(s_n),\qquad B(z)=1-\tfrac32z(1-z).
\]
Consequently, for every \(n\ge1\),
\[
\boxed{s_{n+1}=s_n^2+rB(s_{n-1})s_n,\qquad\frac58\le B(z)\le1\ (0\le z\le1).}
\]
Here \(s_1=[\alpha a_1+(1-\alpha)a_0]a_2\); the dependence on \(\alpha\) is affine. We have \(s_n>0\) for strictly interior initial data and all finite \(n\). In particular, \(s_1=q+O(r)\) as \(\alpha\to0\), since \(r/\alpha\to2\).

**2. Fixed-parameter rates.** For \(\alpha=0\), \(r=0\), \(s_1=q\), and the recurrence yields \(s_{n+1}=s_n^2\) for all \(n\ge1\); hence \(s_n=q^{2^{n-1}}\). If \(0<\alpha<1\), let \(\lambda=\max\{\alpha,1-\alpha\}<1\). Since \(u_n\le\lambda(1-s_n)\le\lambda\), \(0<s_n\le\lambda^n s_0\). The two-step recurrence gives
\[
\frac{s_{n+1}}{r s_n}=1+\frac{s_n}{r}-\frac32s_{n-1}(1-s_{n-1})=:1+e_n.
\]
The series \(\sum_{n\ge1}|e_n|\) converges by geometric decay; also \(1+e_n\ge5/8\). Thus the product \(\prod_{n\ge1}(1+e_n)\) has a strictly positive finite limit. The exact product representation \(s_n=s_1r^{n-1}\prod_{j=1}^{n-1}(1+e_j)\) proves \(s_n/r^n\to L>0\) and the limiting ratio.

**3. Quantified endpoint approximation until the critical generation.** Consider the trajectory with \(r=r_N\) and \(\alpha=\alpha_N\), suppressing the superscript. Define \(v_j=s_1^{2^{j-1}}\) and \(h_j=\log(s_j/v_j)\) for \(j\ge1\). Because \(rB\ge0\), induction gives \(s_j\ge v_j\) and \(h_j\ge0\). The recurrence yields
\[
h_{j+1}=2h_j+\log\left(1+\frac{rB(s_{j-1})}{s_j}\right)
\le2h_j+\frac{r}{v_j}.
\]
For \(N\ge2\), repeated substitution implies
\[
0\le h_N\le r\sum_{j=1}^{N-1}\frac{2^{N-1-j}}{v_j}
\le\frac{r\,2^{N-1}}{s_1^{2^{N-2}}}.
\]
As \(s_1=q+O(r_N)\), eventually \(s_1\ge q/2\), and thus
\[
0\le h_N\le c\,2^{N-1}(2q)^{2^{N-2}}\longrightarrow0
\]
(using \(0<q<1/4\)). Furthermore \(2^{N-1}|\log(s_1/q)|=O(2^{N-1}r_N)\to0\). Therefore
\[
\log\left(\frac{s_N}{q^{2^{N-1}}}\right)
=h_N+2^{N-1}\log(s_1/q)\longrightarrow0,
\]
so \(s_N/r_N\to1/c\). Replacing \(N\) by \(N-1\) in the bound, while keeping the same \(r_N\), shows \(s_{N-1}\to0\) as well.

**4. The nonlinear crossover and post-crossover profile.** The recurrence at \(N\) reads
\[
\frac{s_{N+1}}{r_N^2}
=\left(\frac{s_N}{r_N}\right)^2+B(s_{N-1})\frac{s_N}{r_N}
\longrightarrow\frac1{c^2}+\frac1c=\frac{1+c}{c^2}=:K.
\]
For a fixed \(\ell\ge1\), assume \(s_{N+\ell}/r_N^{\ell+1}\to K\). The next recurrence gives
\[
\frac{s_{N+\ell+1}}{r_N^{\ell+2}}
=r_N^{\ell}\left(\frac{s_{N+\ell}}{r_N^{\ell+1}}\right)^2
+B(s_{N+\ell-1})\frac{s_{N+\ell}}{r_N^{\ell+1}}.
\]
Because \(0\le s_j\le1\), and \(s_{N+\ell-1}\to0\) (the base cases \(s_{N-1},s_N\to0\) and subsequent recurrence suffice), the right side tends to \(K\). Induction completes the theorem for every fixed offset. All displayed coefficients are nonzero for \(c>0\), so the powers are sharp.

## Verification
Run \(\texttt{python3 check.py}\) with Python 3, SymPy, and mpmath installed. It checks exact barycentric conservation and both recurrence identities symbolically, then directly iterates the original three-coordinate operator with 500 decimal digits to test the critical generations and several post-critical offsets at \(N=3,\ldots,7\). It also tests fixed positive mixing ratios. This is a finite corroboration of the stated algebra; the infinite asymptotics follow from the explicit inequalities and induction above, not the experiments.

## Relationship to prior work
Jamilov–Mukhamedov–Mukhamedova–Souissi (2024), Example 3.9 and equation (3.10), introduce exactly this convex mixture and establish its limiting fixed point at interior parameters. They do not state a moving-time asymptotic or sharp post-crossover coefficient. Jamilov (2022) studies a different Volterra/cubic mixture and its regularity partition. Jamilov–Mukhitdinov (2025) study another non-Volterra mixture with pure-square terms, not a reparametrization of this map.

A closely related 2026 published research record establishes a moving-time crossover for the **invariant edge of a five-phase permuted-Volterra operator**, where the scalar return is an iterate of \(T_q(t)=qt+(1-q)t^2\); it also uses a logarithmic perturbation bound and obtains a two-term coefficient. That result provides a very relevant proof analogue and **limits claims about methodological novelty**, but it does not apply by direct substitution to the present two-dimensional dynamical mixture: its map, ambient simplex, parameterized recurrence, time clock, and state-dependent multiplier are different. Here the coefficient \(B(s_{n-1})\) evolves with the full nonlinear state, and the proof controls it along the singularly tuned trajectory. Other records on permutation stochastic maps have different exact factorizations and Poisson boundary windows. A general unpublished perturbation theorem might encompass both models, which remains a priority risk.

## Limitations
Only \(2b=1\), fixed interior initial conditions, a fixed positive scaling constant, and fixed integer post-critical offsets are established. The theorem gives a sharp nonuniform crossover, not a uniform asymptotic for all mixing parameters or all growing time offsets. The fixed-parameter prefactor \(L\) is shown to exist but is not evaluated in closed form. General one-dimensional quadratic crossover methods are known; the specific contribution is the coupled stochastic-mixture realization and its exact coefficient, not discovery of the quadratic mechanism. An equivalent statement or a stronger applicable theorem in unindexed literature remains possible. No independent mathematical audit has been performed.

## References
1. U. Jamilov, F. Mukhamedov, F. Mukhamedova, and A. Souissi, *Dynamics of nonlinear stochastic operators and associated Markov measures*, *Mathematical Methods in the Applied Sciences* 47 (2024), 13300–13312, DOI: https://doi.org/10.1002/mma.10191; first publicly published 2024-05-16; full text: https://onlinelibrary.wiley.com/doi/full/10.1002/mma.10191 (especially Example 3.9).
2. U. Jamilov, *On the convex combination of Volterra operators*, *Journal of Convex Analysis* 29 (2022), 1065–1082, https://journalofconvexanalysis.com/articles/jca29060/jca29060.pdf?v=2.
3. U. Jamilov and R. T. Mukhitdinov, *Dynamics of a Convex Combination and Superposition of Non-Volterra Quadratic Stochastic Operators*, *Journal of Convex Analysis* 32 (2025), 975–988, https://journalofconvexanalysis.com/articles/jca32052/jca32052.pdf?v=2.
4. *A moving-time critical crossover on the five-phase quadratic edge cycle*, research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-moving-time-critical-crossover-on-the-five-phase-quadratic-edg--5c88a7aabfc3 (RESULT.md inspected for the specific theorem and proof).
5. *Exact two-clock relaxation and Poisson boundary windows for permutation quadratic stochastic maps*, research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-two-clock-relaxation-and-poisson-boundary-windows-for-perm--8730f007ff17.
