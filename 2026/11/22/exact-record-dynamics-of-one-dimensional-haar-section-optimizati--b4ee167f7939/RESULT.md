# Exact record dynamics of one-dimensional Haar-section optimization on the disk

## Finding

**Theorem (complete record-process law for planar random-section linear minimization).** Let \(B=\{x\in\mathbb R^2:\|x\|_2\le1\}\), let \(f(x)=1+x_1\), and initialize \(x_0=(1,0)\). At every integer \(j\ge1\), independently sample a Haar-uniform unoriented line \(U_j=\operatorname{span}(u_j)\), calculate an **exact** linear minimizer \(s_j\) on \(B\cap(x_{j-1}+U_j)\), and perform the full/exact-line-search step \(x_j=s_j\). This full-step specialization is distinct from the prescribed damped steps in [1]. Write \(H_N=f(x_N)\), let \(M_N\) count strict changes of iterate through \(N\) calls, and put
\[
F(t)=\frac{\arccos(1-t)}{\pi},\qquad 0\le t\le2.
\]
Then for every integer \(N\ge1\):

1. The entire objective-value process is distributionally identical to the running minimum of \(N\) independent samples of \(1+\cos\Theta\), with \(\Theta\) uniform on \([0,2\pi)\). In particular,
\[
\Pr(H_N>t)=[1-F(t)]^N\quad(0\le t<2),\qquad
\mathbb E H_N=\pi\int_0^1 u^N\sin(\pi u)\,du.
\]
2. The sharp expected and distributional rates are
\[
N^2\mathbb EH_N\longrightarrow\pi^2,\qquad
\Pr(N^2H_N>z)\longrightarrow\exp\!\left(-\frac{\sqrt{2z}}{\pi}\right)\quad(z\ge0),
\]
and \(\log H_N/\log N\to-2\) almost surely.
3. For \(0<\varepsilon<2\), the first oracle count \(T_\varepsilon=\min\{j\ge1:H_j\le\varepsilon\}\) is geometric with success probability \(F(\varepsilon)\); hence
\[
\mathbb ET_\varepsilon=\frac{\pi}{\arccos(1-\varepsilon)}
\sim\frac{\pi}{\sqrt{2\varepsilon}}.
\]
The strict-move indicators are independent Bernoulli random variables with success probabilities \(1/j\). Consequently \(\mathbb EM_N=\sum_{j=1}^N 1/j\) and \(M_N/\log N\to1\) almost surely.
4. For any current boundary point with objective gap \(h=f(x)\in(0,2]\), the conditional expected one-call reduction divided by the *full-space* Frank--Wolfe gap is exactly
\[
\frac{\mathbb E[f(x)-f(s)\mid x]}{h}
=\frac{\sqrt{h(2-h)}-(1-h)\arccos(1-h)}{\pi h}
\sim\frac{2\sqrt2}{3\pi}\sqrt h\quad(h\downarrow0).
\]
This provides a local quantitative explanation for vanishing uniform one-dimensional section efficiency, **not** a new proof of the previously established zero global efficiency infimum [3].

## Assumptions and scope

The feasible domain is the **closed Euclidean unit disk**, the objective is the displayed affine function, and the initial point is the specified boundary maximizer. Directions are independent Haar-uniform **unoriented lines**, equivalently \(u_j=(\cos\theta_j,\sin\theta_j)\) with independent \(\theta_j\sim\mathrm{Unif}[0,\pi)\). Every section minimization is exact; the update takes the section minimizer with full step \(\alpha_j=1\), which is also the exact step-size line search for an affine objective. The process is in exact real arithmetic. A tangential section (probability zero) is defined by keeping the current boundary point, and ties in linear values are likewise resolved by keeping the current point. All almost-sure statements refer to the product Haar measure on infinitely many independent draws. Rotation/scaling transfers the theorem to any nonconstant affine functional and any disk, with the appropriate objective scaling.

**No result about the source's damped open-loop steps, short steps for nonlinear objectives, or higher-dimensional balls is asserted.** The primary classification is convex optimization, MSC2020 `90C25`.

## Proof

**Step 1 (the exact circle-chord coupling).** Identify \(\mathbb R^2\) with \(\mathbb C\), and let a current boundary point be \(x=e^{i\varphi}\). For the unit direction \(u=e^{i\theta}\) with \(\theta\in[0,\pi)\), the only other boundary intersection of the affine line \(x+\mathbb Ru\) is
\[
q=x-2\langle x,u\rangle u=-e^{i(2\theta-\varphi)}.
\]
Indeed \(\|x+tu\|^2=1+2t\langle x,u\rangle+t^2\), whose roots are \(t=0\) and \(t=-2\langle x,u\rangle\); the complex identity follows from elementary double-angle formulas. Since \(2\theta\) is uniform modulo \(2\pi\), **the conditional distribution of \(q\) is uniform on the circle, independent of every previous iterate**. Induction using conditional distributions shows that the proposals \(q_1,q_2,\ldots\) are independent uniform circle points. A linear functional on the chord is minimized at whichever of its endpoints has smaller value. Thus the selected iterate is the best of the initial point and all proposals. The initial objective is the maximum possible value \(2\), so \(H_N=\min_{1\le j\le N}(1+\operatorname{Re}q_j)\) almost surely. This is equality in the joint law of the entire process, not merely an identity of expectations.

**Step 2 (finite-time law).** A uniform circle point has angular coordinate \(\Theta\sim\mathrm{Unif}[0,2\pi)\). For \(0\le t\le2\), the angular measure satisfying \(1+\cos\Theta\le t\) is \(2\arccos(1-t)\), so its probability is \(F(t)\) as stated. Independence gives the exact survival function for the minimum. Tail integration followed by \(t=1+\cos(\pi u)\), reversing limits, gives
\[
\mathbb EH_N=\int_0^2[1-F(t)]^N\,dt
=\pi\int_0^1u^N\sin(\pi u)\,du.
\]
This formula is finite and valid at every positive integer \(N\).

**Step 3 (sharp scaling in distribution and expectation).** As \(t\downarrow0\),
\[
F(t)=\frac{\sqrt{2t}}{\pi}+O(t^{3/2}).
\]
For fixed \(z\ge0\), substitution into the survival function proves
\(\Pr(N^2H_N>z)\to\exp(-\sqrt{2z}/\pi)\). To justify expectation convergence, the elementary inequality \(\arccos(1-t)\ge\sqrt{2t}\) for \(0\le t\le2\) (from \(\cos v\ge1-v^2/2\)) implies
\[
\Pr(N^2H_N>z)\le e^{-\sqrt{2z}/\pi}
\]
whenever \(0\le z\le2N^2\); the left side is zero beyond that interval. Dominated convergence in the tail-integral representation gives
\[
\lim_{N\to\infty}N^2\mathbb EH_N
=\int_0^\infty e^{-\sqrt{2z}/\pi}\,dz=\pi^2.
\]
For each fixed \(\delta>0\), at dyadic times \(N=2^k\), the union bound and the small-\(t\) estimate give \(\Pr(H_N\le N^{-2-\delta})=O(N^{-\delta/2})\). Conversely the lower bound on \(F\) gives \(\Pr(H_N>N^{-2+\delta})\le\exp(-cN^{\delta/2})\) for a constant \(c>0\). Both probabilities are summable over dyadic \(N\); Borel--Cantelli and monotonicity of \(H_N\) extend the resulting two-sided log bounds to all integers, proving \(\log H_N/\log N\to-2\) almost surely.

**Step 4 (hitting time and move count).** As long as \(H_{j-1}>\varepsilon\), success at step \(j\) is precisely the event \(1+\operatorname{Re}q_j\le\varepsilon\), with independent probability \(F(\varepsilon)\). This proves the geometric hitting-time law and mean. The small-t expansion proves its sharp leading constant. Since the proposal values have an atomless distribution, the strict-move event at time \(j\) is exactly the event that the \(j\)-th observation is the smallest of the first \(j\). In an i.i.d. continuous sample, successive insertion ranks are mutually independent and each is uniform on \(\{1,\ldots,j\}\): every permutation of ranks has probability \(1/N!\), and the map from a permutation to its sequence of insertion ranks is a bijection. The move indicators are therefore independent Bernoulli\((1/j)\). Summing expectations yields the harmonic mean. Bernstein's inequality applied at dyadic \(N\) to these independent bounded variables, followed by Borel--Cantelli and monotone interpolation, gives \(M_N/\log N\to1\) almost surely.

**Step 5 (exact conditional drift).** For any fixed current objective gap \(h\in(0,2]\), the conditional proposal law remains uniform. Hence the next gap is distributed as \(\min\{h,Y\}\), where \(Y\) has CDF \(F\). Tail integration yields
\[
\mathbb E[h-\min\{h,Y\}]=\int_0^h F(t)\,dt
=\frac{\sqrt{h(2-h)}-(1-h)\arccos(1-h)}{\pi}.
\]
The full-disk oracle minimizes \(f\) at \((-1,0)\), so its exact gap is \(h\). Division and the expansion of \(F\) prove the final sharp local ratio. The uniform-efficiency infimum being zero was already proved in [3]; the present novelty lies in the **full exact trajectory law and the sharp state-dependent drift and complexity constants**.

## Verification

The self-contained `verify.py` checks the exact angular-reflection map with rational circular coordinates, enumerates independent record indicators for all permutations through seven observations, compares the two exact forms of the mean and the conditional-drift formula using numerical integration, and checks the scaling constants. Execute `python3 verify.py` with Python 3 standard library; it prints `VERIFY_OK`. Numerical tests are diagnostics; the analytic proof above, not finite sampling or quadrature, establishes statements for all integer horizons and almost every infinite trajectory.

## Relationship to prior work

Poirion, Pokutta and Takeda [1] introduce Haar-section Frank--Wolfe and prove dimension-explicit convergence guarantees for their **damped** steps. Their main expected section-efficiency bound assumes section dimension at least three, and their high-probability and short-step arguments do not give this disk's exact one-dimensional full-step trajectory law. The present specialization uses the same section oracle but an exact full step, justified for a linear objective; it does **not** strengthen the published convergence theorem for the prescribed source steps.

The published result [3], *Exact Haar-section efficiency and the two-dimensional Frank--Wolfe threshold*, proves that the sharp worst-case one-dimensional expected section efficiency is **zero**. That result is broader and stronger for the **uniform one-step infimum**, which is excluded here from any claim of novelty. Its exact projection-norm inequality and worst-angle limit do not imply the pathwise iid chord coupling, finite-horizon distribution, optimality-gap constants, geometric first-passage law or logarithmic accepted-move count established here. Stich, Müller and Gärtner [2] analyze unconstrained random-direction optimization and line search; their full text treats the unconstrained problem on \(\mathbb R^n\), not repeated minimization of a linear functional over random chords of a disk. Classical univariate record/order statistics supplies the standard consequences **once** the new section-oracle coupling has been proved; none of those classical record statements is claimed new in isolation.

## Limitations

The complete record equivalence depends on the circle's angle-doubling reflection geometry, independent Haar directions, boundary initialization, an affine objective, and exact full steps. It need not hold for higher-dimensional balls, other convex bodies, inexact section oracles, nonlinear objectives, damped schedules, or finite-precision computations. The \(N^{-2}\) rate is specific to this model; it is not a rate guarantee for the source algorithm in general. The published and indexed searches do not certify historical uniqueness beyond the inspected sources; an unindexed prior treatment of the **identical one-dimensional disk chord algorithm** could still exist. Independent mathematical verification has not been performed.

## References

[1] P.-L. Poirion, S. Pokutta, A. Takeda, *Random-Subspace Frank--Wolfe over Strongly Convex Sets*, arXiv:2605.24819v1, first public 2026-05-24, https://arxiv.org/abs/2605.24819v1 . Complete openly available preprint text, especially Sections 2--4 and the low-dimensional restrictions, inspected.

[2] S. U. Stich, C. L. Müller, B. Gärtner, *Optimization of Convex Functions with Random Pursuit*, arXiv:1111.0194, https://arxiv.org/abs/1111.0194 . Full publicly accessible preprint, Introduction and Section 2 with scope and direction sampling inspected.

[3] *Exact Haar-section efficiency and the two-dimensional Frank--Wolfe threshold*, publicly available mathematical result, 2026-10-13, https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-exact-haar-section-efficiency-and-the-two-dimensional-frank-wolf--4928d0ff7055/RESULT.md . Complete result and proof inspected; the prior sharp zero one-dimensional infimum is explicitly excluded from the new claim.
