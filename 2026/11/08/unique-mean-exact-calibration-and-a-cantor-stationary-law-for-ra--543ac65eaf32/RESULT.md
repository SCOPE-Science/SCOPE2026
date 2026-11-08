# Unique mean-exact calibration and a Cantor stationary law for randomized two-state generator splitting

## Finding

**Theorem.** Fix rates \(a,b>0\), an exact-flow stepsize \(h>0\), and \(p\in(0,1)\). Let the two-state continuous-time generator and its one-way pieces be
\[
Q=\begin{pmatrix}-a&a\\ b&-b\end{pmatrix},\qquad
Q_+=\begin{pmatrix}-a&a\\0&0\end{pmatrix},\qquad
Q_-=\begin{pmatrix}0&0\\b&-b\end{pmatrix}.
\]
Independently at each step, advance a row probability vector by \(\exp(hQ_+/p)\) with probability \(p\), or by \(\exp(hQ_-/(1-p))\) with probability \(1-p\). This is an importance-scaled, one-piece-per-step, exact-subflow randomized splitting: the randomly selected generator has expectation \(Q\).

Let \(Z_n\in[0,1]\) be the resulting probability of state 1, starting at any deterministic \(Z_0=z_0\in[0,1]\). Its unique invariant *distribution* exists for every \(p,h\), and its invariant mean equals the target continuous-time stationary probability \(b/(a+b)\) **if and only if**
\[
p=p_*:=\frac{a}{a+b}.
\]
At this unique choice the method is stronger than equilibrium-unbiased: **its entire mean trajectory is exactly the continuous-time solution at every grid point**, for every initial probability vector and every positive stepsize:
\[
\mathbb E Z_n=\frac{b}{a+b}+e^{-(a+b)nh}\left(z_0-\frac{b}{a+b}\right).
\]
Write \(s=a+b\), \(q=e^{-sh}\), and \(r=b/s=1-p_*\). For \(p=p_*\) the unique invariant law is the biased Bernoulli convolution
\[
Z_\infty\ \stackrel{\mathrm d}=\ (1-q)\sum_{j=0}^{\infty}q^j B_j,\qquad
\Pr(B_j=1)=r,\quad\Pr(B_j=0)=p_*,
\]
with independent bits. Here \(Z_\infty\) denotes a random variable with the limiting *law*, not an almost-sure limit of forward trajectories. Its exact variance and the finite-horizon squared numerical error are
\[
\operatorname{Var}(Z_\infty)=p_*r\frac{1-q}{1+q},\qquad
\mathbb E\!\left[\left(Z_n-z(nh)\right)^2\right]
=p_*r\frac{1-q}{1+q}\left(1-q^{2n}\right),
\]
where \(z(t)=r+e^{-st}(z_0-r)\) is the original ODE solution. In particular for any fixed \(T>0\), with \(n=T/h\) an integer and \(h\downarrow0\), the root-mean-square error is asymptotic to
\[
\sqrt{\frac{ab}{2(a+b)}\left(1-e^{-2(a+b)T}\right)}\,\sqrt h.
\]

There is a sharp qualitative transition at \(h=(\log2)/s\). For \(h>(\log2)/s\), the invariant support is a two-branch Cantor set with Hausdorff dimension \(\log2/(sh)\), and the invariant measure is exact-dimensional with dimension
\[
\dim_H\mu_h=\frac{-p_*\log p_*-r\log r}{sh}<1.
\]
At equality the support fills \([0,1]\) and the invariant measure has dimension \(H(p_*)/\log2\); it is Lebesgue-uniform **exactly** in the balanced-rate case \(a=b\), and is singular for unequal rates. For coarse steps satisfying \(q<\min(p_*,r)\), the true equilibrium \(r\) lies in a gap of the invariant support and every invariant realization obeys the sharp first-level bound
\[
|Z_\infty-r|\ge\min(p_*,r)-q>0\quad\text{almost surely}.
\]
For every deterministic \(z_0\in[0,1]\), after any \(n\) steps the analogous pathwise lower bound is
\[
|Z_n-r|\ge\min(p_*,r)-q-q^n.
\]
Thus an **exact mean numerical solution** can have a singular invariant numerical law and a nonzero forbidden neighborhood around the true equilibrium for every individual late-time realization.

**Exact benchmark.** Take \(a=2\), \(b=3\), \(h=(\log3)/5\), and the calibrated probability \(p_*=2/5\). Then \(q=1/3\), the target equilibrium and stationary mean are \(r=3/5\), the stationary variance is \(3/25\), the support dimension is \(\log2/\log3\), the measure dimension is \(H(2/5)/\log3\), and \(|Z_\infty-3/5|\ge1/15\) almost surely.

## Assumptions and scope

All rates and stepsizes are strictly positive; both sampling probabilities are strictly between zero and one. The two subflows are exact matrix exponentials, not Euler approximations. Each time step uses one fresh independent choice. The random object is the propagated **probability vector**, not a sampled individual two-state Markov trajectory. Expectations and distributional statements refer to randomness in the selected numerical operators. The invariant law is a probability measure on \([0,1]\), whereas the true CTMC equilibrium is a deterministic probability vector.

The Hausdorff dimension of a measure means \(\inf\{\dim_H(E):\mu(E)=1\}\). The entropy symbol is \(H(p)=-p\log p-(1-p)\log(1-p)\), with natural logarithms. The dimension formula uses strong separation for \(q<1/2\) and binary-cylinder entropy at \(q=1/2\); no dimension assertion is made for \(q>1/2\).

## Proof

**1. Exact scalar recursion and invariant-law existence.** For a probability row vector \((z,1-z)\), the forward-only flow moves state-1 mass out at rate \(a/p\); the backward-only flow moves state-2 mass in at rate \(b/(1-p)\). Hence the two selected exact maps are
\[
T_+(z)=q_+z,\quad q_+=e^{-ah/p},\qquad
T_-(z)=q_-z+(1-q_-),\quad q_-=e^{-bh/(1-p)}.
\]
Both map \([0,1]\) into itself and have contraction factors in \((0,1)\). Coupling two trajectories with the same operator choices contracts their distance by at most \(\max(q_+,q_-)^n\). The Markov operator on probability laws is therefore a strict contraction in Wasserstein-1 distance, proving existence and uniqueness of its invariant law and convergence in distribution (indeed in Wasserstein distance) from any initial state.

**2. Uniqueness of equilibrium-unbiased sampling.** Taking expectations in the recursion and solving the scalar fixed-point equation gives the invariant mean
\[
\bar z_p=\frac{(1-p)(1-q_-)}{p(1-q_+)+(1-p)(1-q_-)}.
\]
The equality \(\bar z_p=b/(a+b)\) is equivalent to
\[
\frac{1-e^{-ah/p}}{a/p}=\frac{1-e^{-bh/(1-p)}}{b/(1-p)}.
\]
For every \(h>0\), \(\phi_h(x)=(1-e^{-hx})/x=\int_0^h e^{-tx}\,dt\) is strictly decreasing for \(x>0\). The equality therefore forces \(a/p=b/(1-p)\), or \(p=p_*=a/(a+b)\), and this choice indeed satisfies it. Thus no other fixed positive sampling law can be equilibrium-unbiased.

**3. Exact mean evolution and all finite-time errors.** At \(p=p_*\), both exponents in step 1 equal \(-sh\), so the two maps reduce to \(qz\) and \(qz+1-q\). With independent Bernoulli variables \(B_n\) of success probability \(r\), the recursion becomes
\[
Z_{n+1}=qZ_n+(1-q)B_n.
\]
Its conditional mean equals \(qZ_n+(1-q)r\), which is the exact time-\(h\) semigroup map of \(\dot z=b-sz\). Iteration proves exact mean evolution. Expanding the recursion gives
\[
Z_n=q^nz_0+(1-q)\sum_{j=0}^{n-1}q^{n-1-j}B_j.
\]
Independence of the bits and \(\operatorname{Var}(B_j)=p_*r\) yield the displayed exact finite-time variance. Because the mean equals the exact deterministic solution, that variance is precisely the mean-square numerical error. Taking \(n\to\infty\) gives the invariant law and variance. Finally \((1-q)/(1+q)=\tanh(sh/2)\), and a Taylor expansion at \(h=0\) gives the sharp fixed-\(T\) root-mean-square constant.

**4. Cantor support, measure dimension, and the forbidden gap.** The invariant law satisfies \(\mu_h=p_*(T_0)_\#\mu_h+r(T_1)_\#\mu_h\) for similarities \(T_0(z)=qz\) and \(T_1(z)=qz+1-q\). When \(q<1/2\), their images of \([0,1]\) are the disjoint intervals \([0,q]\) and \([1-q,1]\). At level \(k\) there are \(2^k\) disjoint intervals of length \(q^k\), with fixed positive relative gaps. The elementary separated self-similar set covering/mass-distribution argument gives support dimension \(\log2/(-\log q)\). The measure of a digit cylinder containing \(j\) zeros and \(k-j\) ones is \(p_*^j r^{k-j}\). The strong law gives asymptotic mass exponent \(-H(p_*)k\) for almost every digit sequence, and fixed separation identifies cylinders and balls up to bounded neighboring scales. Therefore the local dimension is almost surely \(H(p_*)/(-\log q)\); the standard mass-distribution and covering argument yields the asserted measure dimension. At \(q=1/2\), the same digit law is the binary expansion measure. Binary-cylinder frequencies give dimension \(H(p_*)/\log2\); unbiased binary digits give Lebesgue measure, while for unequal probabilities the dimension is below one, implying singularity.

For \(q<1/2\), the support lies in \([0,q]\cup[1-q,1]\). If \(q<\min(p_*,r)\), then \(r\in(q,1-q)\), and the distance from \(r\) to that union is \(\min(p_*,r)-q\), giving the stationary lower bound. The finite sum representing \(Z_n\) differs by at most \(q^n\) from a point in the invariant support (extend its finite digit prefix by zeros), which proves the finite-time lower bound. For the exact benchmark, direct substitution yields \(r=3/5\), \(q=1/3\), and the gap \(\min(2/5,3/5)-1/3=1/15\).

## Verification

Run `python verify.py` using Python's standard library. This checks 6,557 assertions, including exact-rational enumeration of all binary operator-choice paths through seven steps across multiple probabilities, contractions, and starting states; exact-rational gap checks through nine steps for the benchmark; and numerical boundary checks of the arbitrary-probability invariant-mean formula. The program prints `VERIFIED checks= 6557` and the benchmark values. These finite tests support, but do not replace, the infinite-time contraction proof, the uniqueness argument, or the entropy dimension theorem.

## Relationship to prior work

Veldman and Zuazua [1] introduced importance-rescaled randomized exact subflows in finite-dimensional time-splitting and prove finite-time convergence/error estimates, without the specific two-state exact mean calibration or its invariant self-similar probability law. Eisenmann and Stillfjord [2] analyze a related randomized *implicit* splitting in a monotone evolution setting, not the exact-subflow two-state result. Classical iterated-function-system theory [3] explains contraction invariant measures and dimensions **once the scalar affine recursion has been identified**; the Bernoulli convolution and its self-similar dimension are not claimed to be new as abstract probability objects. Chakraborty [4] studies products of random \(2\times2\) stochastic matrices from a different Bernoulli-entry distribution, providing a closely related conceptual comparison rather than an identified implication of this splitting classification. The contribution asserted here is the **scheme-specific** uniqueness of exact semigroup-mean sampling together with an exact sharp finite-horizon error constant and the coarse-step singular-support/forbidden-equilibrium phenomenon.

## Limitations

The result concerns only a two-state Markov generator and exact one-edge importance-scaled flows, with iid choices. It does not extend by the presented argument to arbitrary finite generators, overlapping splitting blocks, inexact solvers, or state-dependent probabilities. The probabilistic splitting output is not itself an exact simulation of a CTMC sample path. The support dimension and singularity analysis deliberately makes no claims about the overlapping range \(q>1/2\), where Bernoulli-convolution regularity can be delicate. The numerical example is exact but not a claim about computational speed. Publication precedence in the specialist random-stochastic-matrix literature cannot be completely excluded.

## References

[1] D. W. M. Veldman and E. Zuazua, *A framework for randomized time-splitting in linear-quadratic optimal control*, arXiv:2109.13798 (first posted 2021-09-28), subsequently *Numerische Mathematik* 151 (2022), 495–549. https://arxiv.org/abs/2109.13798 ; https://doi.org/10.1007/s00211-022-01290-3

[2] M. Eisenmann and T. Stillfjord, *A randomized operator splitting scheme inspired by stochastic optimization methods*, arXiv:2210.05375 (first posted 2022-10-11). https://arxiv.org/abs/2210.05375

[3] J. E. Hutchinson, *Fractals and self-similarity*, *Indiana University Mathematics Journal* 30 (1981), 713–747. https://doi.org/10.1512/iumj.1981.30.30055

[4] S. Chakraborty, *Limit distributions of products of independent and identically distributed random \(2\times2\) stochastic matrices: A treatment with the reciprocal of the golden ratio*, *Mathematics* 11 (2023), 4993. https://doi.org/10.3390/math11244993
