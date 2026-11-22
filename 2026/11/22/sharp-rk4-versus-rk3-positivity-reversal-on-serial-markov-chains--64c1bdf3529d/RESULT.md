# Sharp RK4-versus-RK3 positivity reversal on serial Markov chains

## Finding

For each integer \(n\ge5\), consider a continuous-time pure-birth Markov chain with \(n\) states, positive rates \(r_0,\ldots,r_{n-2}\), and terminal absorbing state. Let \(H_3\) and \(H_4\) be the largest positive steps for which the respective **completed** third-order, three-stage and classical fourth-order, four-stage explicit Runge–Kutta maps are entrywise nonnegative. Set \(\rho=1.5960716379833215\ldots\), the unique positive zero of \(1-z+z^2/2-z^3/6\), and \(\delta=2.7852935634052818\ldots\), the unique positive zero of \(1-z/2+z^2/6-z^3/24\). Then the **sharp universal two-method comparison** is

\[
\boxed{\frac{4}{3+\rho}\le\frac{H_4}{H_3}<\frac{\delta}{\rho}.}
\]

The lower constant is \(4/(3+\rho)=0.8703084536243505\ldots\) and is **attained** already on a five-state chain with consecutive positive rates
\[
\left(\rho,\frac{3-\rho}{2},\frac{3-\rho}{2},\rho\right),
\quad H_3=1,\quad H_4=\frac4{3+\rho}.
\]

The upper constant \(\delta/\rho=1.7450930754740892\ldots\) is a **supremum**, approached on five-state chains with rates \((1,\varepsilon,\varepsilon,\varepsilon)\) as \(\varepsilon\downarrow0\). In particular, RK4 can have a sharp positivity step about 12.97% *smaller* than RK3's, or a step almost 74.51% *larger*. Five states are minimal for the loss: for every pure-birth chain with two, three, or four states and arbitrary positive rates, \(H_4\ge H_3\).

## Assumptions and scope

Use the **row-generator** convention: \(Q_{ii}=-r_i\), \(Q_{i,i+1}=r_i\) for \(0\le i<n-1\), with all other entries zero and \(r_{n-1}=0\). All displayed rates before the terminal state are strictly positive. An order-\(p\) completed update for \(p=3,4\) is \(R_p(hQ)=\sum_{j=0}^p h^jQ^j/j!\), \(h\ge0\). Row sums are one for every step; hence entrywise nonnegativity is equivalent to stochasticity and to preservation of every nonnegative probability vector. \(H_p\) is the maximum of all admissible steps, not a spectral stability endpoint or a claim about internal stages. No other transition edges, nonlinearities, or rate changes during a step are permitted.

## Proof

**1. Exact local positivity structure.** Put \(M=\max_{0\le i<n-1}r_i\). For the padded sequence \(r_0,\ldots,r_{n-2},r_{n-1}=0\), define
\[
T=\max_{0\le i\le n-3}(r_i+r_{i+1}+r_{i+2}),\qquad
S=\max_{0\le i\le n-4}(r_i+r_{i+1}+r_{i+2}+r_{i+3}).
\]

For the third-order map the diagonal equals \(R_3(-hr_i)\), nonnegative precisely for \(hr_i\le\rho\), and the entry two forward jumps away equals
\[
\frac{h^2r_ir_{i+1}}6\left[3-h(r_i+r_{i+1}+r_{i+2})\right].
\]
One-jump entries are always positive because their divided-difference integrand is \(R_3'(z)=1+z+z^2/2>0\), and three-jump entries are positive. Thus for every \(n\ge3\)
\[
\boxed{H_3=\min\{\rho/M,3/T\}.}
\]
For \(n=2\), \(H_3=\rho/M\) instead.

For RK4, the distance-one entry from vertex \(i\) equals \(hr_iF_{r_i,r_{i+1}}(h)\), where
\[
F_{a,b}(h)=1-\frac{a+b}{2}h+\frac{a^2+ab+b^2}{6}h^2-\frac{a^3+a^2b+ab^2+b^3}{24}h^3.
\]
Let \(\vartheta(a,b)\) be its unique positive zero, including the allowed terminal value \(b=0\). Indeed,
\[
F_{a,b}(h)=\int_0^1R_3\bigl(-h((1-t)a+tb)\bigr)\,dt
\]
strictly decreases from one to negative infinity for \(a>0,b\ge0\), since its derivative is the negative integral of a positive quantity \(uR_2(-hu)\), and \(R_2(-x)=1-x+x^2/2>0\). Moreover, \(\vartheta(a,b)\ge\rho/\max\{a,b\}\), because \(R_3(-x)\ge0\) for \(0\le x\le\rho\).

Every RK4 diagonal \(R_4(-hr_i)\) is strictly positive, as is every distance-two entry (second divided differences of \(R_4\) are positive because \(R_4''(z)=R_2(z)>0\)); distance-four entries are positive. A distance-three entry is exactly
\[
\frac{h^3r_ir_{i+1}r_{i+2}}{24}
\left[4-h(r_i+r_{i+1}+r_{i+2}+r_{i+3})\right].
\]
Consequently for \(n\ge4\) the complete and nonreentrant endpoint formula is
\[
\boxed{H_4=\min\left\{\min_{0\le i<n-1}\vartheta(r_i,r_{i+1}),\frac4S\right\}.}
\]
For \(n=2,3\), omit the \(4/S\) term. These local formulas are proof ingredients, not claimed here as an independent new classification; closely related RK4 formulas occur in the prior literature for heterogeneous directed cycles.

**2. Lower bound.** For every pair, \(\vartheta(r_i,r_{i+1})\ge\rho/M\ge H_3\). Fix any four consecutive padded rates \(a,b,c,d\), with sum \(s>0\). The two associated triple sums are at most \(T\). We claim
\[
H_3\le\frac{3+\rho}{s}.
\]
If \(M\ge\rho s/(3+\rho)\), this follows from \(H_3\le\rho/M\). Otherwise \(d\le M<\rho s/(3+\rho)\), so \(T\ge a+b+c=s-d>3s/(3+\rho)\), and \(H_3\le3/T<(3+\rho)/s\). Maximizing \(s\) shows \(4/S\ge[4/(3+\rho)]H_3\). Intersecting the pair and three-jump limits proves the lower bound.

**3. Upper bound.** If \(H_3=\rho/M\), take a row whose departure rate equals \(M\). Nonnegative entries summing to one force its diagonal \(R_4(-Mh)\le1\). Yet \(R_4(-z)=1-z(1-z/2+z^2/6-z^3/24)\), and the cubic in parentheses has the unique positive zero \(\delta\); hence \(H_4\le\delta/M\) and \(H_4/H_3\le\delta/\rho\). If instead \(H_3=3/T\), every length-three window extends to a length-four window for \(n\ge5\), so \(S\ge T\), and \(H_4/H_3\le(4/S)/(3/T)\le4/3<\delta/\rho\). The upper constant cannot be attained with all transition rates positive: if \(H_3=\rho/M\), a pair containing \(M\) and another positive rate has \(\vartheta<\delta/M\) because \(R_3(-hu)\) decreases strictly with \(u\): at \(h=\delta/M\), its average over any interval \([m,M]\) with \(m>0\) is smaller than its zero average over \([0,M]\), the latter being \((1-R_4(-\delta))/\delta=0\). In the other case the upper bound is at most \(4/3\).

**4. Sharpness and minimal state count.** Choose \(n=5\) and \((r_0,r_1,r_2,r_3)=(\rho,(3-\rho)/2,(3-\rho)/2,\rho)\). Then \(M=\rho\), \(T=3\), \(S=3+\rho\), so \(H_3=1\). Every pair root is at least \(\rho/M=1\), hence \(H_4=4/(3+\rho)<1\). On \((1,\varepsilon,\varepsilon,\varepsilon)\), as \(\varepsilon\to0^+\), \(H_3\to\rho\), the first pair root tends to \(\vartheta(1,0)=\delta\), other pair roots diverge and \(4/S\to4\), so \(H_4\to\delta\). For \(n=2,3\), no distance-three obstruction exists and every pair root is at least \(\rho/M\ge H_3\). For \(n=4\), the unique four-term sum equals \(r_0+r_1+r_2\), which also equals the maximal triple sum; thus \(4/S\ge3/T\ge H_3\), and every pair root is at least \(H_3\). No shorter chain exhibits a fourth-order positivity disadvantage. This completes the proof.

## Verification

Run `python3 verify.py` with Python 3 standard library. The script reconstructs the third- and fourth-order matrices from exact rational matrix powers, independently checks every positive-distance coefficient against complete-homogeneous-polynomial formulas, tests row sums, and checks finite boundary and sharpness examples. The recorded run reports `PASS 2441 exact matrix/entry checks and finite boundary/ratio checks`. The proof of all-rate and all-dimension results is analytic; finite samples only check implementation and transcriptions.

## Relationship to prior work

Horváth, Song and Terlaky provide polynomial-root methods for positivity/invariance timestep bounds, not this exact two-method sharp extremal comparison. Blanes, Iserles and Macnamara motivate the nonsymmetric Markov-generator positivity question and develop alternative schemes rather than a global RK3-versus-RK4 ratio for heterogeneous birth paths. Earlier published mathematical findings classify **homogeneous** RK4 pure-birth positivity by state count and **heterogeneous directed-cycle** RK4 positivity through pair cubics and four-rate sums. Those results cover important local ingredients here, which are explicitly acknowledged; the claim under investigation is instead the sharp rate-uniform **cross-order comparison**, the attained four-rate extremizer, the opposite supremum, and five-state minimality. An RK3-versus-RK2 directed-cycle bound is not a statement about RK4 versus RK3. The analytical comparison is not established by citation-title mismatch alone; priority against uncatalogued work remains provisional.

## Limitations

The theorem compares completed matrix positivity and is not a comparison of accuracy, work per step, error constants, internal-stage nonnegativity, or practical method superiority. No conclusion is made for bidirectional birth–death generators, arbitrary directed networks, nonlinear problems, or variable steps. The asserted strict upper endpoint requires strictly positive rates; the limit family degenerates as rates tend to zero. The local formulas are shared with or closely related to preceding Markov-positivity results and are not separately claimed as original.

## References

1. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for population models* (earliest arXiv public version 2021-02-16), https://arxiv.org/abs/2102.08242 .
2. Z. Horváth, Y. Song and T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron* (arXiv:1406.6755, initial 2014), https://arxiv.org/abs/1406.6755 .
3. *Exact state-count positivity thresholds for classical RK4 on pure-birth chains*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-state-count-positivity-thresholds-for-classical-rk4-on-pur--f681978f4cc7 .
4. *Exact RK4 positivity on heterogeneous directed cycles and a sharp CFL gain*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-rk4-positivity-on-heterogeneous-directed-cycles-and-a-shar--36d0a038ee0c .
5. *A sharp 25%-loss/50%-gain law for RK3 versus RK2 positivity on directed Markov cycles*, previous mathematical record; distinct method comparison.
