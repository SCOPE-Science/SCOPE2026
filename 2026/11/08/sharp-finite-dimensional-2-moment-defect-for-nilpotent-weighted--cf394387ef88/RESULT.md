# Sharp finite-dimensional \(2\)-moment defect for nilpotent weighted shifts

## Finding
For every integer \(N\ge1\), consider all norm-one nilpotent one-step weighted shifts \(T\) on \(\mathbb C^{N+1}\), defined by
\[
T e_j=w_j e_{j+1}\quad(1\le j\le N),\qquad T e_{N+1}=0,\qquad \max_{1\le j\le N}|w_j|=1.
\]
Write the single-exponent Embry moment defect as
\[
\Delta_2(T)=\left\|(T^*T)^2-T^{*2}T^2\right\|.
\]
Define \(R_0=0\) and, for each integer \(k\ge1\),
\[
R_k=\frac{R_{k-1}+\sqrt{R_{k-1}^2+4}}2.
\]
Then the **exact dimension-dependent minimum** is
\[
\boxed{\min_{\|T\|=1}\Delta_2(T)=R_N^{-2}.}
\]
Equality holds if and only if the weight moduli satisfy
\[
\boxed{|w_j|^2=\frac{R_{N+1-j}}{R_N}\qquad(1\le j\le N).}
\]
Their complex phases are arbitrary; consequently the squared moduli are uniquely determined and strictly decreasing. Furthermore,
\[
\boxed{R_N^2=2N-\tfrac12\log N+O(1),\qquad
\min\Delta_2(T)=\frac1{2N}+\frac{\log N}{8N^2}+O(N^{-2})}
\qquad(N\to\infty).
\]
In particular, the best possible uniform positive lower bound on this defect for finite nilpotent shifts **depends on dimension** and tends to zero.

## Assumptions and scope
All matrices act on a standard complex Hilbert space; their norms are operator norms. The integer \(N\) counts weights, so the matrix size is \(N+1\). Zero weights are permitted in the class, but the normalization requires at least one unit-modulus weight. The defect uses the exponent \(2\) only; it is not a distance to the set of quasinormal operators. All assertions concern one-step nilpotent shifts, not arbitrary nilpotent matrices, other operator classes or higher moments. The asymptotic uses the natural logarithm and constants independent of \(N\).

## Proof
**1. Exact diagonal defect.** Set \(x_j=|w_j|^2\) for \(1\le j\le N\), and \(x_{N+1}=0\). Directly on the basis, \(T^*T\) has diagonal entries \(x_1,\ldots,x_N,0\), and \(T^{*2}T^2\) has diagonal entries \(x_1x_2,\ldots,x_{N-1}x_N,0,0\). Therefore
\[
\Delta_2(T)=\max_{1\le j\le N}x_j|x_j-x_{j+1}|,
\qquad x_j\ge0,\quad\max_jx_j=1. \tag{1}
\]
This step also shows that phases are irrelevant.

**2. Universal backward envelope.** Fix \(\delta=\Delta_2(T)>0\). Equation (1) gives
\(x_j(x_j-x_{j+1})\le\delta\), whether or not \(x_j\ge x_{j+1}\). Because \(x_j\ge0\), the quadratic inequality forces
\[
x_j\le\Phi_\delta(x_{j+1}),\qquad
\Phi_\delta(t)=\frac{t+\sqrt{t^2+4\delta}}2\quad(t\ge0). \tag{2}
\]
The map \(\Phi_\delta\) is strictly increasing. Starting with \(x_{N+1}=0\), repeated application of (2) yields
\[
x_j\le\sqrt\delta\,R_{N+1-j}\qquad(1\le j\le N). \tag{3}
\]
Indeed, \(\Phi_\delta(\sqrt\delta\,R_{k-1})=\sqrt\delta\,R_k\). The positive sequence \((R_k)\) is strictly increasing, so (3) and the norm normalization give
\[
1=\max_jx_j\le\sqrt\delta\,R_N.
\]
Thus \(\delta\ge R_N^{-2}\).

**3. Attainment and equality.** Define \(x_j=R_{N+1-j}/R_N\) and choose any weights of these squared moduli. The recurrence is equivalent to
\[
R_k(R_k-R_{k-1})=1\qquad(k\ge1). \tag{4}
\]
Therefore every term of (1) equals \(R_N^{-2}\). Since \(x_1=1\), this operator is admissible, proving sharpness. Conversely, suppose the lower bound is an equality. Since for \(j>1\) the envelope in (3) is strictly less than one, normalization forces \(x_1=1\). Any strict inequality at any backward step of (2) propagates through the strictly increasing map \(\Phi_\delta\) and makes \(x_1<\sqrt\delta R_N=1\), a contradiction. Hence equality holds at every step and the stated squared moduli are the only possibility. This covers \(N=1\) as well.

**4. Asymptotics.** From (4) one has the exact identity
\[
R_k^2-R_{k-1}^2=2-R_k^{-2},\qquad
R_N^2=2N-\sum_{k=1}^N R_k^{-2}. \tag{5}
\]
Since \(R_1^2=1\) and every increment in (5) lies between \(1\) and \(2\), induction gives \(k\le R_k^2\le2k\). Hence the sum in (5) is \(O(\log N)\), and \(R_k^2=2k+O(\log(k+1))\). Expanding the reciprocal,
\[
R_k^{-2}=\frac1{2k}+O\!\left(\frac{\log(k+1)}{k^2}\right).
\]
The error series converges, and the harmonic sum is \(\log N+O(1)\); inserting this into (5) proves \(R_N^2=2N-(1/2)\log N+O(1)\). Taking its reciprocal and using \(\log^2 N/N^3=O(N^{-2})\) gives the second asymptotic formula.

## Verification
A standalone standard-library checker `check_embry_defect.py` constructs the matrices and their products with exact rational arithmetic for many small shift sizes and weight patterns. It tests the minimizer and envelope with 65-digit decimal arithmetic for dimensions up to \(151\), tests additional randomized feasible weights, and performs finite asymptotic diagnostics. A successful invocation emits `EMBRY_DEFECT_CHECK_OK 29038 assertions`. The analytical backward envelope and summable-error argument above, not the finite tests, establish the claims for all dimensions and the limit.

## Relationship to prior work
Embry's moment identities are a classical characterization of quasinormality when all exponents are imposed. Pietrzycki's recent reduced-Embry theorem proves that two distinct nontrivial exponents suffice for a general bounded operator, and surveys when individual identities are insufficient or sufficient under extra hypotheses. Its results are qualitative exact-equality implications; they do not calculate the optimal nonzero residual of one identity in dimension \(N+1\). The present theorem asks the quantitatively different, norm-one nilpotent weighted-shift extremal problem for exponent \(2\).

Related published results on Schatten-fourth numerical radii of nilpotent shifts, power-quasinormality index sets and Schatten self-commutators address different invariants: respectively fourth Schatten norms of rotated combinations, exact exponents of commutation and ideal membership of a first-order commutator. None of those examined statements implies the recurrence minimax formula (1)–(5). This does not establish global publication priority; a classical extremal-sequence inequality or an unlocated moment-defect result could subsume the claim.

## Limitations
The exact formula does not extend as stated to all nilpotent matrices; no optimal bound for arbitrary operators, a second simultaneous residual, the operator-norm distance to quasinormality or higher Embry powers is obtained. The uniqueness concerns squared weight magnitudes only. Finite computational checks are independent diagnostics, not a substitute for proof. The novelty assessment is a best-knowledge comparison with the inspected sources rather than an exhaustive verification of older moment-defect or weighted-shift literature.

## References
1. Paweł Pietrzycki, *Reduced Embry characterizations of quasinormal operators*, arXiv:2610.17303v1, first publicly submitted 2026-10-12; primary MSC2020 47B20. https://arxiv.org/abs/2610.17303
2. M. R. Embry, *A generalization of the Halmos–Bram criterion for subnormality*, Acta Sci. Math. (Szeged) 35 (1973), 61–64 (classical identity, cited in reference 1).
3. *Sharp weighted Schatten-fourth radii of nilpotent shifts*, published published-finding corpus research record, 2026-10-11, identifier `17db4dbf42a4` (different fourth-norm functional).
4. *Exact minimal dimensions for power-quasinormality index sets*, published published-finding corpus research record, 2026-10-04, identifier `28e6775c2cf2` (different power-commutation invariant).
5. *A quasinilpotent Schatten self-commutator counterexample*, published published-finding corpus research record, 2026-09-20, identifier `8ac62c6f153b` (different first-order commutator invariant).
6. Adnan and A. A. S. Jibril, *On operators for which \(T^{*2}T^2=(T^*T)^2\)*, International Mathematical Forum 5 (2010), no. 46, 2255–2262 (bibliographic citation inspected; full text not obtained).
