# Exact polynomial-time anchored-BV sensitivity of Euclidean \(\ell_1\)-ball projection

## Finding
For each integer \(n\ge2\) and radius \(R>0\), write
\[
B_1(R)=\{z\in\mathbb R^n:\sum_{i=1}^n|z_i|\le R\},\qquad P_R(x)=\operatorname{argmin}_{z\in B_1(R)}\|x-z\|_2^2,
\]
and use the **anchored variation norm**
\[
\|h\|_{\mathrm{BV},0}=|h_1|+\sum_{i=1}^{n-1}|h_{i+1}-h_i|.
\]
Let \(C_n=\sup_{x\ne y}\|P_R(x)-P_R(y)\|_{\mathrm{BV},0}/\|x-y\|_{\mathrm{BV},0}\). The following are exact statements.

1. \(C_n\) does not depend on \(R\). It is rational and is attained by two distinct finite vectors in a common affine projection chamber.
2. The signed-active-set dynamic program below computes \(C_n\) **exactly in \(O(n^6)\) integer arithmetic operations and \(O(n^2)\) working space**, instead of enumerating the exponential family of signed supports.
3. For every \(n\ge3\),
\[
\boxed{n-\frac4n\le C_n\le\sqrt{n(4n-3)}<2n.}
\]
More precisely, set \(m=\lceil n/2\rceil\); the lower bound improves to \(C_n\ge n\) when \(m\) is even, to \(C_n\ge n-1/m\) when \(n\) and \(m\) are odd, and to \(C_n\ge n-2/m\) when \(n\) is even and \(m\) is odd. The following initial coefficients were certified by the exact dynamic program, independently cross-checked by exhaustive ternary enumeration for \(2\le n\le8\):

| \(n\) | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| \(C_n\) | \(3/2\) | \(3\) | \(4\) | \(14/3\) | \(16/3\) | \(7\) | \(8\) |

| \(n\) | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|
| \(C_n\) | \(44/5\) | \(48/5\) | \(11\) | \(12\) | \(90/7\) | \(96/7\) | \(15\) |

## Assumptions and scope
All vectors and weights are real; the number of coordinates is at least two; the Euclidean projection radius is strictly positive. The norm is **anchored**, not the seminorm \(\sum_i|h_{i+1}-h_i|\): the anchor term is essential because ordinary \(\ell_1\)-ball projection does not commute with adding constants. The coefficient compares **two inputs**, not output variation against the variation of a single input. All bounds refer to the exact continuous Euclidean nearest-point map, not an iterative approximation.

## Proof
**1. Active affine derivatives and attainment.** The classical threshold rule is \(P_R(x)_i=\operatorname{sgn}(x_i)(|x_i|-\tau)_+\), with \(\tau=0\) inside the ball and, outside, \(\sum_i(|x_i|-\tau)_+=R\). Fix an exterior open chamber and let \(q\in\{-1,0,1\}^n\) encode the active signs. Write \(m=\#\{i:q_i\ne0\}\). On that chamber the Jacobian is
\[
J_q=\operatorname{diag}(1_{q_i\ne0})-\frac{qq^\mathsf T}m.
\]
For \(m=1\), this is zero. For every \(m\ge2\), every ternary sign word \(q\) of support \(m\) is realized in an open chamber: choose \(x_i=q_i(\rho+R/m)\) on its support, \(x_i=0\) elsewhere, for any \(\rho>0\). This has threshold \(\rho\), strictly positive active outputs and strictly inactive complement. Hence the norm of any such derivative is realized by distinct nearby inputs within the same chamber. Inside the ball the derivative is the identity. The map is continuous piecewise affine with finitely many chambers; subdividing a segment gives
\[
C_n=\max\left\{1,\max_{q\in\{-1,0,1\}^n,\;m\ge2}\|J_q\|_{\mathrm{BV},0\to\mathrm{BV},0}\right\}.
\]
This maximum is independent of the radius and is attained.

**2. A finite exact integer formula.** The linear isometry from anchored BV to coordinate \(\ell_1^n\) sends \(h\) to \((h_1,h_2-h_1,\ldots,h_n-h_{n-1})\); the inverse sends the \(k\)-th coordinate unit vector to the tail \(b^{(k)}\), where \(b^{(k)}_i=1_{i\ge k}\). Thus the anchored-BV norm of \(J_q\) is the maximum over \(1\le k\le n\) of \(\|J_q b^{(k)}\|_{\mathrm{BV},0}\). Let \(t=\sum_{i=k}^n q_i\), and put \(q_0=0\), \(h_0=0\), and
\[
h_i=1_{q_i\ne0}\big(m1_{i\ge k}-t q_i\big),\quad 1\le i\le n.
\]
Then \(J_qb^{(k)}=h/m\), so the exact formula is
\[
\boxed{C_n=\max\left\{1,\max_{2\le m\le n,\;1\le k\le n,\;-m\le t\le m}\frac1m
\max_{\substack{q_i\in\{-1,0,1\};\;\#\{i:q_i\ne0\}=m\\\sum_{i=k}^n q_i=t}}\sum_{i=1}^n|h_i-h_{i-1}|\right\}.}\]
Every maximization is over finite integer data; there is no continuous optimization or unproved limiting step.

**3. Polynomial-time dynamic program.** For each triple \((m,k,t)\), scan coordinates \(i=1,\ldots,n\). Retain a state \((a,b,p)\): the number \(a\) of used nonzero symbols, the partial signed sum \(b=\sum_{j=k}^i q_j\) (zero for \(i<k\)), and preceding symbol \(p=q_i\). The stored score is the maximum running sum of \(|h_j-h_{j-1}|\). Initialize the empty prefix at \((0,0,0)\) with score zero; for each next symbol \(q\in\{-1,0,1\}\), update
\[
a'=a+1_{q\ne0},\qquad b'=b+1_{i\ge k}q,
\]
and add \(|1_{q\ne0}(m1_{i\ge k}-tq)-1_{p\ne0}(m1_{i-1\ge k}-tp)|\) to the score, retaining only the best score for each new state. After the last coordinate take states with \((a,b)=(m,t)\). There are \(O(n^3)\) triples \((m,k,t)\), \(n\) scan positions, \(O(n^2)\) states per position and three transitions, giving \(O(n^6)\) arithmetic operations and two \(O(n^2)\) state layers of memory. Induction on prefix length proves the dynamic-programming invariant, so the output is exactly the formula in Step 2.

**4. Near-dimension amplification.** For \(n=2m\) or \(n=2m-1\), take \(q\) supported at indices \(1,3,\ldots,2m-1\), with the signs as balanced as possible, and choose \(k=1\). If \(m\) is even, the signed sum is zero. Then \(J_qb^{(1)}\) is one at those indices and zero elsewhere, giving variation \(n\). If \(m\) is odd, take \(m\) signs with sum \(-1\) and final active sign \(-1\). The active output values are \(1+q_i/m\), their sum is \(m-1/m\), and the anchored variation is twice that sum minus the last output when \(n\) is odd, or twice that sum when \(n\) is even. This gives exactly \(n-1/m\) or \(n-2/m\), respectively. These are genuine finite-pair derivative witnesses by Step 1. Since \(m\ge n/2\), all cases imply \(C_n\ge n-4/n\).

**5. Universal upper bound.** Let \(D\) be the first-anchored difference matrix, so \(Dh=(h_1,h_2-h_1,\ldots,h_n-h_{n-1})\). Its norm from coordinate \(\ell_2\) to \(\ell_1\) satisfies \(\|D\|_{2\to1}=\sqrt{4n-3}\): duality makes its square the maximum of \(\|D^\mathsf T\varepsilon\|_2^2\) over signs \(\varepsilon\in\{-1,1\}^n\); alternating signs achieve \(4(n-1)+1\). The inverse cumulative-sum matrix satisfies \(\|D^{-1}\|_{1\to2}=\sqrt n\), attained by its first column. Since Euclidean projection onto any closed convex set is nonexpansive in \(\ell_2\),
\[
\|P_R(x)-P_R(y)\|_{\mathrm{BV},0}
\le \sqrt{4n-3}\,\|x-y\|_2
\le\sqrt{n(4n-3)}\,\|x-y\|_{\mathrm{BV},0}.
\]
This concludes the theorem.

## Verification
The standalone standard-library checker `verification/check.py` implements the exact integer dynamic program, checks its answer against an independent exhaustive ternary enumeration through dimension eight, and certifies the listed rational values through dimension fifteen. It checks all analytic patterned witnesses through dimension one hundred. It additionally constructs exact-rational external inputs and perturbed inputs, evaluates their actual Euclidean \(\ell_1\)-ball projections, and checks the derivative formula for a deterministic family of chambers. One completed run ended with `ALL_ANCHORED_BV_CROSSPOLYTOPE_CHECKS_PASS`. The unbounded-dimension assertions rely on the proofs above; finite tests are not substitutes.

## Relationship to prior work
Duchi, Shalev-Shwartz, Singer and Chandra (2008) establish the Euclidean \(\ell_1\)-ball threshold formula and efficient projection algorithms. The two published cross-polytope-projection results listed below express Lipschitz coefficients in **coordinate \(\ell_p\) norms**, which do not determine the induced norm after the non-diagonal anchored-difference change of coordinates. The published real \(\ell_1\) nearest-point-selection theorem concerns a different metric projection, which can be multivalued. The contribution here is the polynomial exact optimization over signed active patterns in anchored variation and the near-dimension amplification family. This is not a claim to discover soft thresholding or Hilbert nonexpansivity.

## Limitations
A simple closed expression for \(C_n\) in every dimension is not proved; the all-dimensional **exact answer is algorithmic**. The general upper bound may not be asymptotically optimal, even though the lower bound is asymptotically at least \(n\). The theorem is limited to Euclidean projection onto a *single* real unweighted \(\ell_1\) ball and a fixed anchored nonperiodic path norm. It does not treat periodic, unanchored-seminorm, weighted, or vector-valued variants. Historical priority against unindexed older work remains uncertain; no independent validation is claimed.

## References
1. J. Duchi, S. Shalev-Shwartz, Y. Singer, and T. Chandra, *Efficient Projections onto the \(\ell_1\)-Ball for Learning in High Dimensions*, ICML 2008, pp. 272–279, first publicly evidenced 5 July 2008, DOI:10.1145/1390156.1390191; author text https://web.stanford.edu/~jduchi/projects/DuchiShSiCh08.pdf.
2. *Exponent-invariant cross-polytope projection and its sharp Lipschitz threshold*, published research record, identifier 5177ec842d41, https://github.com/published-finding corpus/2026.
3. *Exact Lipschitz stability and contractivity threshold for weighted cross-polytope projections*, published research record, identifier c92b6dad1bd0, https://github.com/published-finding corpus/2026.
4. *Optimal Lipschitz nearest-point selections for real \(\ell_1\) balls*, published research record, identifier 77979dc14d49, https://github.com/published-finding corpus/2026.
