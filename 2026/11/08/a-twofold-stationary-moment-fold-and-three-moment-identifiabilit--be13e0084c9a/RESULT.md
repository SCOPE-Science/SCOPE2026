# The sixth stationary position moment resolves the two-rate ambiguity in a harmonic run-and-tumble particle

## Finding

For a one-dimensional harmonic run-and-tumble particle with no propulsion during tumbles, let the trap relaxation rate and the active speed be known. On the domain of finite, strictly positive run-to-tumble and tumble-to-run rates, the **second, fourth, and sixth stationary position moments uniquely identify both rates**. In particular, the sixth moment distinguishes the two branches at every ambiguous pair of second and fourth moments, not just at a witness pair.

The two-moment fold is an antecedent: *An exact two-moment inverse fold in a trapped run-and-tumble particle* [2] already classifies all finite positive rate pairs given the second and fourth moments, including a region with exactly two solutions and an example with unequal sixth moments. The result here is the global exclusion of a tie in all three moments. Together with [2], it shows that three moments are necessary and sufficient when taking consecutive even moments starting at the second.

## Model and observations

Let \(\dot X=-bX+vS\), where \(b,v>0\) are known and \(S\in\{-1,0,1\}\) is a continuous-time Markov chain. Each of \(\pm1\) jumps to \(0\) at rate \(\gamma_R>0\), and \(0\) jumps to each of \(\pm1\) at rate \(\gamma_T/2>0\). There is no translational diffusion, no directional bias, and no residual propulsion in state \(0\). Use \(Y=bX/v\), dimensionless time, and dimensionless rates \(a=\gamma_R/b\) and \(c=\gamma_T/b\). Write \(m_j=\mathbb E[Y^j]\) in stationarity; the observations are exact population moments. With the internal chain stationary, the pullback \(Y_t=\int_{-\infty}^t e^{-(t-u)}S_u\,du\) defines the stationary position and has \(|Y_t|\le1\). The internal chain is irreducible, and positions driven by the same internal path contract exponentially, ensuring uniqueness of the joint stationary law.

## Proof

**Forward formulas.** For \(R_j=\mathbb E[Y^j\mathbf1_{|S|=1}]\), \(T_j=\mathbb E[Y^j\mathbf1_{S=0}]\), and \(H_j=\mathbb E[Y^jS]\), the stationary generator gives, for \(j\ge1\),
\[
(j+a)R_j=jH_{j-1}+cT_j,\qquad
(j+c)T_j=aR_j,\qquad (j+a)H_j=jR_{j-1}.
\]
Using \(R_0=c/(a+c)\), these relations yield
\[
m_2=\frac{c}{(a+c)(a+1)},\qquad
\frac{m_4}{3m_2}=\frac{c+2}{(a+3)(a+c+2)},\qquad
\frac{m_6}{5m_4}=\frac{c+4}{(a+5)(a+c+4)}.
\]
Indeed stationarity of \(Y^j\) gives \(m_j=H_{j-1}\); for even \(j\), substitute \(H_{j-1}=(j-1)R_{j-2}/(j-1+a)\) and use \(R_{j-2}/m_{j-2}=(j-2+c)/(j-2+a+c)\), including \(j=2\). These are the forward moments of the known model [1, 2].

**Fixed variance.** Set \(s=m_2\), \(q=m_4/(3m_2)\), and \(r=m_6/(5m_4)\). Finite positive rates with that variance satisfy exactly
\[
0<s<1,\qquad 0<a<A_s:=\frac{1-s}{s},\qquad c=\frac{as(1+a)}{1-s(1+a)}.
\]
On this interval both normalized higher moments are given by \(F_d(a)\), with \(q=F_2(a)\) and \(r=F_4(a)\), where
\[
F_d(a)=\frac{d+s(a+1)(a-d)}{(a+d+1)(a+d-ds(a+1))},\qquad d\in\{2,4\}.
\]
The denominators are positive because \(s(a+1)<1\) and \(a>0\). For context, the known two-moment fold [2] counts two admissible roots precisely when \(q_*(s)<q<s/(1+2s)\), where \(q_*(s)=\min_{0<a<A_s}F_2(a)\). The minimum admits the explicit form in [2], which also gives the complete count outside the two-solution region.

**No tie in both higher moments.** If two distinct admissible values \(x,y\) have the same \(q\) and \(r\), cross-multiply the two equalities \(F_d(x)=F_d(y)\) and divide by \(-d(x-y)\). The result, for each \(d\in\{2,4\}\), is
\[
\big((2d+1)s^2-3s\big)xy+
\big((2d+1)s^2-(2d+2)s+1\big)(x+y)+(2d+1)(1-s)^2=0.
\]
For example, for numerator coefficients \(u_2,u_1,u_0\) and denominator coefficients \(w_2,w_1,w_0\), the cross-multiplied difference divided by \(x-y\) has coefficients \(u_2w_1-u_1w_2, u_2w_0-u_0w_2, u_1w_0-u_0w_1\) on \(xy,x+y,1\), respectively. This yields the displayed equations by substitution. The determinant of the system in \(xy,x+y\) is \(-8s^2(s-1)\), which is nonzero. Solving gives \(xy=A_s^2/2\) and \(x+y=3A_s/2\); hence the roots are \(A_s/2\) and \(A_s\). The latter is not admissible for a finite positive \(c\). This contradiction establishes injectivity. Constructively, solve the quadratic after clearing denominators in \(F_2(a)=q\), keep only roots in \((0,A_s)\), and use \(F_4(a)=r\) to select the unique rate for compatible data. The variance formula gives \(c\); multiplication by \(b\) gives both physical rates.

As an illustration, the rate pairs \((a,c)=(3/4,21/4)\) and \((11/15,143/30)\) share \(m_2=1/2\) and \(m_4=29/80\); they give \(m_6=1073/3680\) and \(7627/26144\), respectively. The proof controls all ties, not just this example.

## Verification and limitations

`verify_moments.py` is a reproducible Python/SymPy check of the generator formulas at thirty rational rate pairs, the two symmetric polynomial identities, their joint solution, and the example. Its finite rate checks illustrate the proof; the all-rate result is the symbolic elimination on the admissible open interval. This is structural identifiability, not a bound on conditioning, confidence intervals, or accuracy from finitely many noisy positions. It requires the known trap and propulsion calibration, the stated three-state dynamics, and strict finiteness and positivity of both rates. In particular, it makes no uniqueness assertion at the infinite-rate boundary used to exclude a tie.

## Relationship to prior work

Sun, Ye and Podgornik [1] give the model, its stationary distribution and forward moment structure. The earlier two-moment inverse record [2] already establishes the exact fold and multiplicity; its Limitations expressly leave open uniform disambiguation by the sixth moment. The present proof separates every finite ambiguous pair. Basu et al. [3] treat an equal-rate subfamily; Frydel [4] studies forward moments of run-and-tumble oscillators; Ceccarelli, Browning and Baker [5] study identifiability from dynamic observations for a different velocity-jump model. These comparisons do not establish historical priority for the global uniqueness claim.

## References

1. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, https://arxiv.org/abs/2409.00578.
2. *An exact two-moment inverse fold in a trapped run-and-tumble particle*, 2026-11-02, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-an-exact-two-moment-inverse-fold-in-a-trapped-run-and-tumble-par--432388eb4847.
3. U. Basu et al., *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, https://arxiv.org/abs/1910.10083.
4. D. Frydel, *Run-and-tumble oscillator: moment analysis of stationary distributions*, https://arxiv.org/abs/2309.12537.
5. J. Ceccarelli, A. P. Browning and R. E. Baker, *Structural identifiability of partially-observed stochastic processes: from single-particle trajectories to total particle density data*, https://arxiv.org/abs/2605.13504.
