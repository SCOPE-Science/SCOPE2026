# Fat-Cantor bounded-orbit fibers and geometric escape in a two-saddle border-collision map

## Finding

For every real \(0<s<1\), consider the continuous piecewise-affine planar map
\[
F_s(x,y)=\begin{cases}
((s+2)x+y+1,-2s x),&x\leq0,\\
((s-2)x+y+1,2s x),&x\geq0.
\end{cases}
\]
The two affine branches have stable multiplier \(s\) and unstable multipliers \(2\) and \(-2\). Both fixed points are saddles, and neither determinant vanishes.

Set \(z=(1-s)x\) and \(q=((1-s)(y+s x)-s)/(2-s)\). For each fixed real \(q\), let \(\mathcal B_{s,q}\) be the set of initial values \(z\) for which the corresponding entire forward planar orbit is bounded. Then the following **complete fiber classification** holds:

1. For \(q<-1\), \(\mathcal B_{s,q}=\varnothing\).
2. For \(-1\leq q\leq0\), \(\mathcal B_{s,q}=[-1-q,1+q]\), including the singleton at \(q=-1\).
3. For every \(q>0\), \(\mathcal B_{s,q}\) is a perfect nowhere-dense **positive-measure Cantor set** of exact Lebesgue length \(2\), independent of \(s\) and \(q\).

More precisely, put \(I_n=[-1-q s^n,1+q s^n]\) and let \(S_N\) consist of initial \(z\in I_0\) whose first \(N\) iterates satisfy \(z_n\in I_n\). For every \(N\geq0\), \(S_N\) consists of exactly \(2^N\) disjoint closed intervals, each of length \(2^{1-N}(1+q s^N)\). At deletion stage \(j\geq0\), exactly \(2^j\) disjoint open gaps of length \(2(1-s)q(s/2)^j\) are removed. Therefore \(\mathcal B_{s,q}=\bigcap_{N\geq0} S_N\), and its length is \(\lim_N |S_N|=2\).

If \(q>0\), an initial \(z\) is selected uniformly from \(I_0\), and \(\tau=\min\{n\geq1:z_n\notin I_n\}\), with \(\tau=\infty\) if there is no exit, then
\[
\Pr(\tau=\infty)=\frac1{1+q},\qquad
\Pr(\tau=j+1)=\frac{(1-s)q s^j}{1+q}\quad(j=0,1,\ldots).
\]
Conditional on finite exit, \(\Pr(\tau=j+1\mid\tau<\infty)=(1-s)s^j\) and \(\mathbb E(\tau\mid\tau<\infty)=1/(1-s)\). Every exited orbit tends to \(-\infty\) in the \(z\)-coordinate. In particular, the set of bounded planar initial states has **infinite two-dimensional Lebesgue area**, despite the two saddle fixed points and the positive-measure Cantor structure on each \(q>0\) fiber.

## Assumptions and scope

All coordinates, parameters, orbits and measures are real. The parameter interval is strictly \(0<s<1\). Lebesgue length of a fiber is measured in its normalized \(z\)-coordinate; the Euclidean arc length of each \(q>0\) bounded fiber in the original \((x,y)\) plane is \(2\sqrt{1+s^2}/(1-s)\). The fibers for fixed \(q\neq0\) are **initial-condition sections**, not individually invariant under \(F_s\); after one iteration the fiber parameter becomes \(sq\). All probability claims use normalized one-dimensional Lebesgue measure on \(I_0\), not an invariant probability measure.

## Proof

**1. Exact triangular normal form.** Writing \(w=y+s x\), the planar map gives \(x'=1+w-2|x|\) and \(w'=s(w+1)\) on both branches. Hence \(w_n=s/(1-s)+(2-s)s^n q/(1-s)\), and the invertible affine transformation in the statement gives
\[
q_{n+1}=sq_n,\qquad z_{n+1}=1-2|z_n|+(2-s)q_n.
\]
The Jacobian eigenvalues on the left branch are \((s,2)\), and on the right \((s,-2)\). Since the transformation is invertible and \(q_n=s^nq\) is bounded, a planar orbit is bounded exactly when its \(z\)-sequence is bounded.

**2. Exact escape threshold.** For every \(q\geq-1\), define \(L_n=-1-q s^n\leq0\) and \(R_n=1+q s^n\geq0\). The time-\(n\) scalar map \(T_n(z)=1-2|z|+(2-s)q s^n\) satisfies
\[
T_n(L_n)=T_n(R_n)=L_{n+1}.
\]
If \(z_n<L_n\), the left affine branch gives \(z_{n+1}-L_{n+1}=2(z_n-L_n)\); induction shows escape to \(-\infty\). If \(z_n>R_n\), its next image is below \(L_{n+1}\), hence likewise escapes. Therefore all bounded orbits must stay in the moving bands \(I_n=[L_n,R_n]\).

For \(-1\leq q\leq0\), the maximum of \(T_n\) on \(I_n\) is \(1+(2-s)q s^n\leq1+q s^{n+1}=R_{n+1}\), and its minimum is \(L_{n+1}\). Thus \(T_n(I_n)\subset I_{n+1}\), establishing the interval classification including the endpoints.

For \(q<-1\), the first iterate of any real initial \(z_0\) satisfies \(z_1\leq 1+(2-s)q<0\). For \(n\geq1\), let \(M_n=-1-q s^n+2^n(1+q)\). We have \(z_1\leq M_1\), and \(M_n<0\) since \(M_n|_{q=-1}=-1+s^n<0\) and \(\partial M_n/\partial q=2^n-s^n>0\). If \(z_n\leq M_n<0\), then \(z_{n+1}\leq1+2M_n+(2-s)q s^n=M_{n+1}\). Since \(M_n\to-\infty\), no bounded initial condition exists.

**3. Finite Markov-like survival geometry for \(q>0\).** The peak of \(T_n\) on \(I_n\) is \(1+(2-s)q s^n>R_{n+1}\); the images of both monotone half-bands cover all of \(I_{n+1}\). Each inverse branch is an affine contraction of ratio \(1/2\), and their two images are disjoint closed intervals separated by a positive gap. Thus, after \(N\) pullbacks, the complete survivor set \(S_N\) has exactly \(2^N\) intervals with equal length \(|I_N|/2^N=2^{1-N}(1+q s^N)\). At one time-\(j\) parent band, the excluded central gap has length \(|I_j|-|I_{j+1}|=2q(1-s)s^j\); pulling it through each of the \(2^j\) possible preceding inverse branches multiplies the gap length by \(2^{-j}\). Consequently \(2^j\) gaps of exact length \(2(1-s)q(s/2)^j\) are removed at stage \(j\), giving total deletion length
\[
\sum_{j=0}^{\infty}2^j\,2(1-s)q(s/2)^j=2q.
\]
Since \(|I_0|=2(1+q)\), the intersection has length \(2\). Every finite-stage component is subsequently split by a positive interior gap and its length tends to zero: the intersection is closed, has empty interior, has no isolated points and is totally disconnected, hence is a perfect nowhere-dense Cantor set. The survival condition exactly characterizes bounded orbits by step 2.

**4. Exact first exit and planar area.** For uniform initial \(z\in I_0\), the total length of all \(2^N\) survivor intervals is \(2(1+q s^N)\). Therefore
\[
\Pr(\tau>N)=\frac{1+q s^N}{1+q},\qquad N\geq0.
\]
Accordingly successive differences give \(\Pr(\tau=j+1)=q(1-s)s^j/(1+q)\), and \(\lim_N\Pr(\tau>N)=1/(1+q)\). Conditioning on exit gives the geometric law and its mean. This latter expression is the one used throughout the theorem and verification.

Finally the affine \((x,y)\mapsto(z,q)\) Jacobian has absolute determinant \((1-s)^2/(2-s)\). Fubini's theorem applied to the bounded-orbit set, whose \(z\)-sections have length \(2\) at every \(q>0\), shows the total planar area is infinite. The claimed Euclidean arc length follows from \(dy/dx=-s\) along each fiber and \(dz=(1-s)dx\). This completes the proof.

## Verification

The file `checks/cantor_checker.py` is a standalone Python 3 exact-rational checker using only the standard library. Run `python checks/cantor_checker.py`; it asserts the affine skew-product identity, the precise number, endpoints, lengths and gap multisets of all survivor cylinders for four rational values of \(s\), four rational values of \(q>0\), and depths \(0\) through \(9\), plus negative-fiber invariance checks. It returns `FIBER_CANTOR_EXACT_INTERVAL_GAPS_OK 160 cylinders_max 512` and `AFFINE_SKEW_PRODUCT_AND_FIBER_PHASE_CHECK_OK`. The general theorem is proved symbolically above; these finite checks are supplementary and not an infinite certificate.

## Relationship to prior work

Ghosh, McLachlan and Simpson (2024), arXiv:2402.05393v1, study the same two-dimensional border-collision normal form and in Proposition 10.1 describe the invariant line corresponding here to \(q=0\), where the map is conjugate to a skew tent map. Their restriction explicitly assumes an additional strict interior parameter condition; the full tent boundary and its off-line bounded-orbit fibers require separate analysis. The present result classifies the *entire plane* by the decaying transverse parameter, not merely the invariant line or an attractor in it. Fatoyinbo and Simpson (2022), arXiv:2210.14445, survey noninvertible border-collision dynamics and bifurcations; Ghosh, McLachlan and Simpson (2023), arXiv:2307.05144, construct trapping regions and robust chaotic attractors. Neither inspected result supplies the all-fiber Cantor measure, exact gap distribution or first-escape law. Fat-Cantor constructions in other nonautonomous expanding systems are conceptually related but do not imply this exact planar classification.

## Limitations

The theorem is for the specific symmetric-unstable-eigenvalue family \((2,-2)\), with common stable eigenvalue \(s\in(0,1)\), and is not an assertion about arbitrary four-parameter border-collision normal forms. The positive-measure Cantor fibers consist of **bounded initial data**, not independent invariant attractors. There is no claim that a generic perturbation retains the exact measure or gap law. The claimed originality is limited by accessible prior literature and research-record searches; unindexed or independently developed equivalent results may exist. Independent mathematical validation is not claimed.

## References

1. I. Ghosh, R. I. McLachlan and D. J. W. Simpson, *The bifurcation structure within robust chaos for two-dimensional piecewise-linear maps*, arXiv:2402.05393v1 (first posted 2024-02-08), especially §§1, 2, 3 and 10; published in *Communications in Nonlinear Science and Numerical Simulation* 134 (2024), 108025. https://arxiv.org/html/2402.05393v1
2. H. O. Fatoyinbo and D. J. W. Simpson, *A synopsis of the non-invertible, two-dimensional, border-collision normal form with applications to power converters*, arXiv:2210.14445 (2022). https://arxiv.org/abs/2210.14445
3. I. Ghosh, R. I. McLachlan and D. J. W. Simpson, *Robust chaos in orientation-reversing and non-invertible two-dimensional piecewise-linear maps*, arXiv:2307.05144 (2023). https://arxiv.org/html/2307.05144v1
