# Reciprocal-integer rigidity and exact absorption laws for stochastic rounding of contractions

## Finding

Write \(R(z)\) for unbiased rounding to the nearest two integers: \(R(z)=\lfloor z\rfloor\) with probability \(1-\{z\}\) and \(R(z)=\lceil z\rceil\) with probability \(\{z\}\), with the obvious deterministic convention when \(z\) is integral. All rounding choices are conditionally independent given the past. For \(0<q<1\), start from any integer \(n\geq0\) and iterate \(X_0=n\), \(X_{t+1}=R(qX_t)\).

**Exact distributional collapse and its rigidity.** The identity
\[
\mathcal L(X_t)=\mathcal L(R(q^t n))\quad\text{for all integers }n\geq0\text{ and }t\geq0
\]
holds if and only if \(q=1/b\) for an integer \(b\geq2\). It is enough to require the identity just for \(t=2\) and all \(n\). In the reciprocal-integer case it remains true with possibly different factors \(1/b_j\) at successive steps, where each \(b_j\geq2\) is an integer, replacing \(q^t\) by \(1/(b_1\cdots b_t)\). Thus the variance at each fixed step is exactly
\[
\operatorname{Var}(X_t)=\{q^t n\}(1-\{q^t n\})\leq\frac14,
\]
and is not a sum of one-step error variances.

**Exact absorption and lattice phase.** Fix an integer \(b\geq2\), let \(q=1/b\), assume \(n\geq1\), and define \(\tau=\inf\{t\geq0:X_t=0\}\). For every integer \(t\geq0\),
\[
\Pr(\tau>t)=\min\{1,n/b^t\}.
\]
Let \(k=\lfloor\log_b n\rfloor\) and \(u=n/b^k\in[1,b)\). Then
\[
\mathbb E\tau=k+1+\frac{u}{b-1},\qquad
\mathbb E\tau-\log_b n=\Phi_b(\{\log_b n\}),
\]
where \(\Phi_b(x)=1+b^x/(b-1)-x\) on \(0\leq x<1\), extended continuously with period one. It is positive and nonconstant, has maximum \(b/(b-1)\) at the integer-phase endpoints, and has its unique phase minimum at
\[
 x_b=\log_b\!\left(\frac{b-1}{\log b}\right)\in(0,1).
\]
The hitting-time law is consequently fully explicit, not just its order \(\log_b n\).

## Assumptions and scope

The computation is on the exact unit-spaced integer lattice, with ideal, unbiased, fresh nearest-neighbor stochastic rounding, deterministic contraction factors, nonnegative integral initial data, and no added forcing. This is a model of repeatedly rounded scalar linear decay, not a theorem for arbitrary floating-point lattices, other randomized rounding rules, finite-precision pseudorandomness, nonlinear contraction maps, or rounding with nonzero bias. At \(n=0\) the chain is absorbed immediately; the stated formulas for \(\mathbb E\tau\) are for \(n\geq1\). Every probability and variance refers to randomness of the rounding, not to an ensemble of initial conditions.

## Proof

**Sufficiency and even time-varying reciprocals.** For an integer \(b\geq2\) and adjacent integers \(j,j+1\), both transition laws \(\mathcal L(R(j/b))\) and \(\mathcal L(R((j+1)/b))\) are supported on the same pair of consecutive integers. Indeed, writing \(j=ab+r\) with \(0\leq r<b\), both outcomes belong to \(\{a,a+1\}\), including the boundary case \(r=b-1\). Thus rounding the image under \(1/b\) of a random variable supported on adjacent integers always yields a law on adjacent integers. Conditional unbiasedness gives \(\mathbb E[R(z)\mid z]=z\). By induction, after applying any finite sequence \(1/b_1,\ldots,1/b_t\), the law is supported on the two integers bracketing \(n/(b_1\cdots b_t)\), and its mean equals that number. A probability measure on that adjacent pair is uniquely determined by its mean, so it is precisely the single-rounding law. This proves distributional collapse and the asserted variance identity, without any independence assumption between the final state and previous rounding errors.

**Necessity.** Suppose \(q\) is not the reciprocal of an integer. Set \(m=\lfloor 1/q\rfloor\), so \(qm<1<q(m+1)\), and choose \(n=\lfloor m/q\rfloor+1\). Since \(q<1\), we have \(m<qn<m+1\). Put \(f=qn-m\in(0,1)\). The first step gives \(X_1=m\) with probability \(1-f\) and \(X_1=m+1\) with probability \(f\). The next step has strictly positive probabilities
\[
\Pr(X_2=0)=(1-f)(1-qm)>0,
\qquad
\Pr(X_2=2)=f(q(m+1)-1)>0,
\]
and \(\Pr(X_2=1)>0\), because \(0<qm<1<q(m+1)<2\), so each first-step branch also gives a positive probability of one. In contrast, the law of \(R(q^2 n)\) has support of at most two adjacent integers. Therefore distributional equality at \(t=2\) already fails. As a transparent example, for \(q=1/\sqrt2\), \(n=2\), the one-shot answer is deterministically \(1\), but \(X_2\) takes values \(0,1,2\) with probabilities \(3-2\sqrt2,\,4\sqrt2-5,\,3-2\sqrt2\), respectively.

**Absorption.** For integer \(n\geq1\), the chain is nonnegative and zero is absorbing. Accordingly \(\{\tau>t\}=\{X_t\ne0\}\). The distributional identity gives \(X_t=R(n/b^t)\) in law. If \(n/b^t\geq1\), its zero probability vanishes; if \(n/b^t<1\), it is Bernoulli with success probability \(n/b^t\). Hence \(\Pr(\tau>t)=\min(1,n/b^t)\). The tail-sum identity then gives
\[
\mathbb E\tau=\sum_{t=0}^{\infty}\Pr(\tau>t)
=(k+1)+\sum_{t=k+1}^{\infty}\frac{n}{b^t}
=k+1+\frac{n}{b^k(b-1)}.
\]
The period-one representation follows by setting \(x=\{\log_b n\}\) and \(u=b^x\). On \((0,1)\), \(\Phi'_b(x)=b^x\log b/(b-1)-1\) is strictly increasing, negative at zero and positive at one because \(\log b<b-1<b\log b\) for \(b>1\). The unique critical point is therefore the specified strict minimum. Endpoint values coincide, proving the periodic extension and the maximum.

## Verification

The accompanying `verify_rounding.py` is an executable, dependency-free Python 3 checker based on exact rational arithmetic. It computes stepwise stochastic-rounding transition laws, verifies collapse for multiple integer reciprocal scales and horizons, checks the exact absorbing tail sum, and tests the constructive three-point failure for nonreciprocal rational factors. It additionally validates a rational enclosing interval for \(\sqrt2\), establishing positivity of the illustrative irrational probabilities without relying on floating point. At packaging, it returned `PASS: 13234 exact rational kernel/absorption assertions; 144 nonreciprocal two-step witnesses; radical-sign certificate.` The proof above, rather than these finite tests, establishes the universal quantifiers.

## Relationship to prior work

Unbiased rounding and conditional first-moment preservation are standard; see Croci, Fasi, Higham, Mary and Mikaitis, and the 2022 analyses of El Arar and collaborators. General conditional unbiasedness gives \(\mathbb E X_t=q^t n\), but does not imply equality of the **entire distribution** with one stochastic rounding; the explicit nonreciprocal witness shows the gap. The result here identifies exactly when the kernel composes without enlarging support and translates that phenomenon into a sharp, phase-dependent absorption law. It does not claim invention of stochastic rounding or of conditional-expectation methods.

## Limitations

The only-if direction concerns equality for every integer starting value; isolated nonreciprocal pairs of starting state and horizon may coincide. No uniform claim is made for floating-point grids with variable spacing, correlated rounding randomness, or nonlinear dynamics. The exact logarithmic phase is a discrete initial-condition effect and does not imply a continuous limiting density. An equivalent formulation in a broader literature on integer-grid linear interpolation kernels remains a possible publication-precedence risk; this manuscript does not establish publication priority.

## References

- Croci, Fasi, Higham, Mary and Mikaitis, *Stochastic Rounding: Implementation, Error Analysis, and Applications*, public manuscript deposited 14 October 2021, https://eprints.maths.manchester.ac.uk/2836/ ; full revised survey https://eprints.maths.manchester.ac.uk/2843/1/cfhm22.pdf .
- El Arar and collaborators, *The Positive Effects of Stochastic Rounding in Numerical Algorithms*, first arXiv version dated 8 July 2022, https://arxiv.org/abs/2207.03837 .
- El Arar and collaborators, *Stochastic Rounding Variance and Probabilistic Bounds: A New Approach*, first arXiv version dated 21 July 2022, https://arxiv.org/abs/2207.10321 .
