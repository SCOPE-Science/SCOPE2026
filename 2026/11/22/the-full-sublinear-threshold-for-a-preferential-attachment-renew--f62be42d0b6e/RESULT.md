# The full sublinear threshold for a preferential-attachment renewal series

## Finding

For \(0\leq\gamma\leq1\), set
\[
\Phi(\gamma)=\sum_{k=1}^{\infty}a_k(\gamma),\qquad
 a_k(\gamma)=\prod_{j=1}^{k}
 \frac{j^\gamma}{j^\gamma+3^\gamma-1}.
\]
Then
\[
\boxed{\Phi(\gamma)>1\quad(0\leq\gamma<1),\qquad \Phi(1)=1.}
\]
At \(\gamma=0\) the series is interpreted as \(+\infty\). For every \(0<\gamma\leq1\) it converges. Moreover, the proof gives the explicit differential estimate
\[
\Phi'(\gamma)<-\frac{29}{50}
\qquad\text{for }\frac{99}{100}\leq\gamma\leq1.
\]
The strict inequality settles the parameter condition (2)/(22) of Ben-Hamou, Broutin and Cazaux (2026) on the entire strictly sublinear range. Their conditional convergence theorem for the one-community preferential-attachment degree distribution therefore applies to every \(0\leq\gamma<1\). The classical endpoint \(\gamma=1\) is not inferred from its strict condition and is already handled separately in that work.

## Assumptions and scope

The parameter \(\gamma\) is real, in the closed unit interval. The series is scalar, nonnegative and has no randomness in its definition. The related preferential-attachment model is the single-community setting of the cited paper, not the two-community model. The certificate relies on exact rational endpoints, directed decimal arithmetic and a finite set of inequalities. It does not assert strict monotonicity of \(\Phi\) throughout the entire parameter interval.

## Proof

**Convergence and the small-parameter region.** Write \(q(\gamma)=3^\gamma-1\) and \(r_j(\gamma)=j^\gamma/(j^\gamma+q(\gamma))\). For \(0<\gamma<1\), since \(q(\gamma)>0\) and \(\sum j^{-\gamma}=\infty\), the product \(a_k\) decreases at least stretched-exponentially, hence its sum is finite. The case \(\gamma=1\) telescopes:
\[
a_k(1)=\frac{2}{(k+1)(k+2)},\qquad \sum_{k\geq1}a_k(1)=1.
\]
If \(0<\gamma\leq63/100\), then \(q(\gamma)<1\), as certified by the exact integer inequality \(3^{63}<2^{100}\). As \(j^\gamma\geq1\),
\[
\Phi(\gamma)\geq\sum_{k\geq1}(1+q(\gamma))^{-k}
=\frac1{q(\gamma)}>1.
\]
At \(\gamma=0\), every factor equals one and the sum is infinite.

**A short finite certificate for the intermediate range.** For rational \(63/100\leq s\leq t\leq99/100\), monotonicity of \(x/(x+q)\) in its two positive arguments gives, simultaneously for all \(\gamma\in[s,t]\),
\[
\Phi(\gamma)\geq
L(s,t):=\sum_{k=1}^{300}\prod_{j=1}^{k}
\frac{j^s}{j^s+3^t-1}.
\]
The accompanying independent script `CHECKER.py` divides \([63/100,99/100]\) into exactly 14 consecutive intervals with *rational* endpoints, evaluates outward-rounded enclosures for each \(L(s,t)\), and verifies the strict, uniform inequalities
\[
L(s,t)>\frac{1001}{1000}>1
\qquad\text{for each certified interval.}
\]
The smallest certified lower bound exceeds one by more than \(0.0011064\). This finite check establishes the stated inequality at **every real parameter**, not just at sampled mesh points. Its complete arithmetic is reproducible using Python's standard-library decimal operations; logarithms and exponentials are widened outward by a unit in the last place after their correctly-rounded evaluation.

**The near-linear endpoint.** Put \(q_0=49/25\). The exact integer inequality
\[
3^{99}25^{100}>74^{100}
\]
shows that \(q(\gamma)>q_0\) on \([99/100,1]\). Set
\[
u_k=\prod_{j=1}^{k}\frac{j}{j+q_0},\quad
B_j(\gamma)=\sum_{k\geq j}a_k(\gamma),\quad
 d_j(\gamma)=\frac{q(\gamma)\log j-3^\gamma\log3}{j^\gamma+q(\gamma)}.
\]
As \(j^\gamma\leq j\), one has \(a_k(\gamma)\leq u_k\). The beta-integral identity gives, for every \(j\geq1\),
\[
B_j(\gamma)\leq\sum_{k\geq j}u_k
=u_j\frac{j+q_0}{q_0-1}.
\]
These estimates also ensure absolute, locally uniform convergence of the differentiated series, and thus
\[
\Phi'(\gamma)=\sum_{j\geq1}d_j(\gamma)B_j(\gamma).
\]
For \(1\leq j\leq5\), set
\[
\ell_k=\prod_{i=1}^{k}\frac{i^{99/100}}{i^{99/100}+2},
\qquad A_j=\sum_{k=j}^{200}\ell_k.
\]
Here \(d_j<0\), \(B_j\geq A_j\), and
\[
d_j(\gamma)\leq
\frac{2\log j-(1+q_0)\log3}{j+2}<0.
\]
For \(j\geq6\), the positive contributions are bounded above by
\[
\frac{\max\{0,2\log j-(1+q_0)\log3\}}
{j^{99/100}+q_0}\,
 u_j\frac{j+q_0}{q_0-1}.
\]
The directed-arithmetic certificate verifies that the sum of the five negative upper bounds is **less than** \(-1.47\), while the positive upper bounds for \(6\leq j\leq1000\) sum to **less than** \(0.81\).

For the remaining positive tail, the gamma-moment Jensen inequality and log-convexity of the gamma function give
\[
u_j=\frac{\Gamma(1+q_0)\Gamma(j+1)}{\Gamma(j+1+q_0)}
\leq\frac2{(j+1)^{q_0}}.
\]
Therefore, for \(j\geq1001\),
\[
B_j\leq\frac{2(j+2)}{(q_0-1)(j+1)^{q_0}}
\leq2.1j^{-24/25},\qquad
(d_j)_+\leq\frac{2\log j}{j^{99/100}}.
\]
Since \(x\mapsto (\log x)x^{-39/20}\) is decreasing for \(x\geq1000\), the tail is bounded by
\[
4.2\int_{1000}^{\infty}\frac{\log x}{x^{39/20}}\,dx
=4.2\,1000^{-19/20}
\left(\frac{\log1000}{19/20}+\frac1{(19/20)^2}\right)
<0.08.
\]
The final strict inequality follows using the elementary rational bounds \(1000^{-19/20}<1/500\), \(\log1000<7\) (the latter certified from the finite Taylor sum for \(e^7\)), and the exact rational estimate \(3213/45125<0.08\). Consequently,
\[
\Phi'(\gamma)<-1.47+0.81+0.08=-0.58
\]
uniformly on \([99/100,1]\). Since \(\Phi(1)=1\), the required strict inequality follows for every \(99/100\leq\gamma<1\). Combining all three parameter regions proves the claim.

## Verification

Run `python3 CHECKER.py` using Python 3.11 or newer, without external packages or downloaded inputs. The script checks the integer exponential comparison, discovers and exhaustively certifies 14 rational subintervals, verifies their non-overlapping coverage and their minimum lower bound, checks the endpoint derivative's finite positive and negative contributions by directed arithmetic, and checks the exact rational tail estimate. Its principal output is:

```
CERTIFIED: phi(gamma)>1 for all gamma in [0,1), phi(1)=1
Finite enclosures: 14 intervals; min positive margin >= 0.001106456924412927748074433285
Derivative bound: phi prime < -0.58 on [0.99,1]
```

These finite enclosures prove the global assertion because all continuum and infinite-tail reductions above are analytic, and no finite enumeration is treated as an exhaustive simulation of the series.

## Relationship to prior work

Ben-Hamou, Broutin and Cazaux (2026), Theorem 2 and Lemma 14, formulate this exact strict inequality and prove it on the initial range through \(\log2/\log3\), together with a qualitative one-sided neighborhood of the endpoint. Their Remark 8 leaves the full range unresolved and sketches, without supplying, a possible numerical proof. The present contribution is the complete, reproducible proof with only 14 rational parameter intervals and a uniform derivative bound. It does **not** claim new independent preferential-attachment convergence machinery, and it does **not** resolve the paper's two-community convergence conjecture. Older results of Rudas, Tóth and Valkó (2007) already treat degree-distribution convergence for a broad single-community family by a different general branching-process method. The new statement is the specific unresolved series inequality and its consequence for the newer coupling-based sufficient condition, not a priority claim over older convergence results.

## Limitations

This is a finite enclosure proof rather than a closed-form pointwise comparison for all parameters. It relies on the documented correct rounding of `decimal` elementary functions followed by explicit outward widening and directed operations. The estimates establish a negative derivative only on the final parameter subinterval; no assertion of global monotonicity is made. The broader two-community problem is untouched. Historical coverage cannot be ruled out beyond examined literature and searches; no independent review or machine-formal proof is claimed.

## References

1. A. Ben-Hamou, N. Broutin, and C. Cazaux, *Sublinear multi-type preferential attachment*, arXiv:2611.06904v1, first submitted November 4, 2026, Sections 1.1, 4.3, Lemma 14 and Remark 8. https://arxiv.org/abs/2611.06904
2. A. Rudas, B. Tóth, and B. Valkó, *Random trees and general branching processes*, *Random Structures & Algorithms* 31 (2007), 186–202; open preprint arXiv:math/0503728. https://arxiv.org/abs/math/0503728
3. Python Software Foundation, `decimal` library reference (correctly rounded `exp`/`ln`; rounding modes). https://docs.python.org/3/library/decimal.html
