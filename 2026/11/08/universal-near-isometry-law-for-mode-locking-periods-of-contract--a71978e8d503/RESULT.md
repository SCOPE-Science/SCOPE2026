# Universal near-isometry law for mode-locking periods of contracted rotations

## Finding
For \(0<\lambda<1\) and \(0\leq\delta<1\), consider the contracted circle rotation
\[
T_{\lambda,\delta}(x)=\{\lambda x+\delta\},\qquad x\in[0,1).
\]
Choose \(\delta\) with Lebesgue-uniform law. Write \(\rho_{\lambda,\delta}\) for the rotation number, and \(q_{\lambda,\delta}\) for the least period of the attracting cycle, defined almost surely (the irrational-rotation parameters and rational plateau endpoints are null). Assign \(q=1\) on the zero-rotation plateau. Put \(\tau=-\log\lambda\).

**Theorem.** As \(\lambda\uparrow1\),
\[
\bigl(\rho_{\lambda,\delta},\tau q_{\lambda,\delta}\bigr)
\ \Longrightarrow\ (U,T),
\]
where \(U\) is uniform on \([0,1]\), independent of \(T\), and \(T\) has the nondegenerate probability density
\[
 f_T(t)=\frac{t}{\zeta(2)(e^t-1)}=\frac{6t}{\pi^2(e^t-1)},\qquad t>0.
\]
For every continuously differentiable test function \(F\) on \([0,1]\times[0,\infty)\), supported in \(0\leq t\leq B\) for some fixed \(B<\infty\), the convergence has the effective form
\[
\left|\mathbb E F(\rho_{\lambda,\delta},\tau q_{\lambda,\delta})
-\frac1{\zeta(2)}\int_0^1\int_0^\infty
 F(u,t)\frac{t}{e^t-1}\,dt\,du\right|
\leq C_F\,\tau\bigl(1+|\log\tau|^2\bigr)
\]
for all sufficiently small \(\tau>0\), with a constant depending only on the indicated test function and its compact support.

The same limiting product measure and the same effective order hold when the first coordinate \(\rho_{\lambda,\delta}\) is replaced by the physical parameter \(\delta\). All nonnegative real moments of the rescaled period converge: for every \(s\geq0\),
\[
\lim_{\lambda\uparrow1}\mathbb E[(\tau q_{\lambda,\delta})^s]
=\frac{\Gamma(s+2)\zeta(s+2)}{\zeta(2)}.
\]
In particular the limiting mean equals \(2\zeta(3)/\zeta(2)=12\zeta(3)/\pi^2\), and the limiting second moment equals \(2\pi^2/5\).

## Assumptions and scope
The observation is over one uniformly selected parameter \(\delta\), *not* over random time-dependent maps. The scalar \(\lambda\) is deterministic and tends to one through values below one. Least periods refer to the rational-rotation attracting cycle, rather than arbitrary transient times. Laurent--Nogueira's exact plateau theorem supplies the input period and parameter classification; the joint scaling, effective error and moment law are established below. All statements on exceptional endpoints are interpreted almost everywhere with respect to \(\delta\).

## Proof
**1. Exact finite-parameter weights (previously known).** Laurent and Nogueira, Theorem 3, give the parameter interval of each reduced nonzero rational rotation number \(p/q\), where \(1\leq p<q\), \(q\geq2\), \(\gcd(p,q)=1\). Subtracting its stated endpoints yields the interval length
\[
 w_q(\lambda)=\frac{(1-\lambda)^2\lambda^{q-1}}{1-\lambda^q}.
\]
Crucially, the length depends on \(q\), not on \(p\). Each such plateau has an attracting cycle of least period \(q\) in its interior. The zero-rotation plateau has measure \(1-\lambda\) and least period one. The irrational-rotation parameter set has Hausdorff dimension zero by their Theorem 4 and is consequently Lebesgue-null. Plateau endpoints form a countable null set. Thus the exact law of \((\rho,q)\) is
\[
\Pr\{(\rho,q)=(0,1)\}=1-\lambda,\qquad
\Pr\{(\rho,q)=(p/q,q)\}=w_q(\lambda).
\]
As a consistency check, the Lambert identity
\[
\sum_{q\geq1}\frac{\varphi(q)z^q}{1-z^q}
=\frac{z}{(1-z)^2},\quad 0<z<1,
\]
which follows by exchanging the order of summation and using \(\sum_{d\mid n}\varphi(d)=n\), gives \(\sum_{q\geq2}\varphi(q)w_q=\lambda\), exactly complementing the zero-rotation mass.

**2. Rescaling.** With \(\tau=-\log\lambda\), define
\[
 B_\tau=\frac{e^\tau(1-e^{-\tau})^2}{\tau^2}
=\left(\frac{2\sinh(\tau/2)}\tau\right)^2=1+O(\tau^2).
\]
Then \(w_q=\tau^2B_\tau/(e^{\tau q}-1)\). For a compactly supported \(C^1\) test function as in the theorem, the expectation becomes
\[
(1-e^{-\tau})F(0,\tau)+\tau^2B_\tau
\sum_{q\geq2}\frac1{e^{\tau q}-1}
\sum_{\substack{1\leq p<q\\(p,q)=1}} F(p/q,\tau q).
\tag{1}
\]

**3. Uniform distribution of reduced numerators.** Möbius inversion and ordinary one-dimensional Riemann-sum bounds imply, uniformly in \(q\geq2\) and \(t\geq0\),
\[
\sum_{\substack{1\leq p<q\\(p,q)=1}}F(p/q,t)
=\varphi(q)\int_0^1F(u,t)\,du
+O\bigl(d(q)\|F\|_{C^1}\bigr),
\tag{2}
\]
where \(d(q)\) is the divisor count. Indeed write the coprimality indicator as \(\sum_{d\mid(p,q)}\mu(d)\), apply a Riemann sum with grid size \(q/d\) to each divisor, and use \(\sum_{d\mid q}\mu(d)q/d=\varphi(q)\). For \(F\) supported in \(t\leq B\), the total error after insertion into (1) is at most
\[
 C_F\tau^2\sum_{2\leq q\leq B/\tau}
 \frac{d(q)}{e^{\tau q}-1}
\leq C_F\tau\sum_{q\leq B/\tau}\frac{d(q)}q
=O_F\bigl(\tau(1+|\log\tau|^2)\bigr).
\tag{3}
\]
Here we used \(e^v-1\geq v\) and \(\sum_{q\leq N}d(q)/q=O(1+\log^2 N)\).

**4. Arithmetic averaging of periods.** Put \(h(t)=\int_0^1F(u,t)\,du\) and extend
\[
 g(t)=\frac{t h(t)}{e^t-1},\quad t>0,\qquad g(0)=h(0).
\]
This is a compactly supported \(C^1\) function. The standard elementary totient estimate
\[
 \sum_{q\leq N}\frac{\varphi(q)}q
 =\frac{N}{\zeta(2)}+O(1+\log N)
\tag{4}
\]
follows from \(\varphi(q)/q=\sum_{d\mid q}\mu(d)/d\), since \(\sum_{d\geq1}\mu(d)/d^2=1/\zeta(2)\). Abel summation applied to (4), followed by a Riemann-sum estimate, gives
\[
 \tau\sum_{q\geq1}\frac{\varphi(q)}qg(\tau q)
=\frac1{\zeta(2)}\int_0^\infty g(t)\,dt
+O_F\bigl(\tau(1+|\log\tau|)\bigr).
\tag{5}
\]
The \(q=1\) term in this auxiliary sum contributes only \(O_F(\tau)\). Combining (1)--(5), noting that the initial zero-rotation plateau also contributes \(O_F(\tau)\) and \(B_\tau=1+O(\tau^2)\), proves the claimed effective expectation estimate.

**5. Weak limit and tightness.** By \(\varphi(q)\leq q\) and the expression for \(w_q\), the probability of \(0<\tau q\leq a\) is \(O(a+\tau)\), uniformly for small \(\tau\). For \(R\geq1\), the probability of \(\tau q>R\) is at most \(C(R+1)e^{-R}\), by comparison with \(\tau^2\sum_{q>R/\tau}q e^{-\tau q}\). Hence no mass escapes to either endpoint. The effective estimate on compactly supported test functions yields weak convergence to the measure in the theorem. It has total mass one because
\[
 \int_0^\infty\frac{t}{e^t-1}\,dt
 =\sum_{k\geq1}\int_0^\infty t e^{-kt}\,dt
 =\zeta(2).
\]
The factorization of the limiting expectation proves the asserted independence of \(U\) and \(T\).

**6. Replacing the rotation number by the parameter.** Let \(x_{j+1}=T_{\lambda,\delta}(x_j)\) and set \(e_j=\lfloor\lambda x_j+\delta\rfloor\in\{0,1\}\). Summation of \(x_{j+1}=\lambda x_j+\delta-e_j\) over \(0\leq j<n\) gives
\[
\frac1n\sum_{j<n}e_j
=\delta-(1-\lambda)\frac1n\sum_{j<n}x_j
+\frac{x_0-x_n}{n}.
\]
The left side converges to the rotation number of the monotone degree-one lift, so
\[
0\leq\delta-\rho_{\lambda,\delta}\leq1-\lambda\leq\tau.
\]
For test functions with bounded first derivative in their first coordinate, changing \(\rho\) to \(\delta\) alters the expectation by at most \(\tau\|\partial_uF\|_\infty\). This proves both the physical-parameter limit and its quantitative estimate.

**7. Moments.** The exponential upper tail established in step 5 implies uniform integrability of every fixed power \((\tau q)^s\) for \(s\geq0\). Weak convergence therefore gives convergence of all these moments. Expanding \((e^t-1)^{-1}=\sum_{k\geq1}e^{-kt}\) and integrating termwise yields
\[
\mathbb E[T^s]=\frac1{\zeta(2)}\sum_{k\geq1}\frac{\Gamma(s+2)}{k^{s+2}},
\]
which is the claimed formula. This completes the proof.

## Verification
The standalone standard-library program `verify.py` checks the original rational-plateau endpoints and their numerator-independent exact widths with rational arithmetic, checks finite truncations of the totient Lambert normalization, and numerically compares scaled period moments against the limiting values. It executed successfully, reporting 628 checks. These computations test premises and constants at finite parameters; the infinite and uniform conclusions rely on the preceding proof, not on finite enumeration.

## Relationship to prior work
The parameter family and rational plateaus, including their exact endpoint formulas, are due to the mode-locking literature and are explicitly credited to Laurent--Nogueira, Theorem 3 (2017 preprint; 2018 journal). Their Theorem 4 proves that irrational-rotation parameters have Hausdorff dimension zero. Gaivão--Laurent--Nogueira (2022) generalize rotation-number formulas to broader two-interval affine maps. Guiraud--Hernández--Meyroneinc--Nogueira (2025) extend such dynamics to three intervals. The present result is the joint, effective, near-isometry parameter-distribution theorem, with its independent limiting factors and all-order moment law; it is neither an assertion about the plateau widths themselves nor an irrational-rotation classification. The older mode-locking works of Ding--Hemmer (1987) and Bugeaud--Conze (1999) are relevant historical comparators.

## Limitations
The theorem applies to the one-slope family and uniform choice of the detuning parameter only; no analogous universality is claimed for arbitrary parameter densities, piecewise-affine maps with unequal branch slopes, or randomly switched dynamics. The quantitative bound is for compactly supported continuously differentiable test functions and is not claimed optimal. The singular exceptional parameter set is removed only in the almost-everywhere interpretation; it is not assigned a fictitious periodic orbit. An older, not fully accessible mode-locking derivation of an equivalent limit remains a potential publication-priority risk. No independent audit has been performed.

## References
1. M. Laurent and A. Nogueira, *Rotation number of interval contracted rotations*, arXiv:1704.05130v3 (first public version 2017-04-17), especially Theorems 3 and 4 and Section 5. https://arxiv.org/html/1704.05130v3 ; journal version *Journal of Modern Dynamics* 12 (2018), 175–191, https://doi.org/10.3934/jmd.2018007 .
2. J. P. Gaivão, M. Laurent and A. Nogueira, *Rotation number of 2-interval piecewise affine maps*, arXiv:2212.10944v1 (2022), especially Sections 5 and 8. https://arxiv.org/html/2212.10944v1 .
3. P. Guiraud, M. Hernández, A. Meyroneinc and A. Nogueira, *Rotation number and dynamics of 3-interval piecewise lambda-affine contractions*, arXiv:2501.16263 (2025), introduction and main results. https://arxiv.org/abs/2501.16263 .
4. E. J. Ding and P. C. Hemmer, *Exact treatment of mode locking for a piecewise linear map*, *Journal of Statistical Physics* 46 (1987), 99–110, https://doi.org/10.1007/BF01010333 (abstract consulted; full text not inspected).
5. Y. Bugeaud and J.-P. Conze, *Calcul de la dynamique d’une classe de transformations linéaires contractantes mod 1 et arbre de Farey*, *Acta Arithmetica* 88 (1999), 201–218, https://doi.org/10.4064/aa-88-3-201-218 (bibliographic comparator, not inspected in full).
