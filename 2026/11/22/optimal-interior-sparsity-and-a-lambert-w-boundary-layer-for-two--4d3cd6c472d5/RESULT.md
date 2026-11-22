# Optimal interior sparsity and a Lambert-W boundary layer for two-column signed sketches

## Finding

For every integer \(m\ge 2\) and every \(p\in(0,1]\), let \(S_{m,p}\in\mathbb R^{m\times2}\) have mutually independent entries, with each entry equal to zero with probability \(1-p\) and to each of \(\pm p^{-1/2}\) with probability \(p/2\). Its entries have zero mean and unit variance. Define the exact column-rank failure probability \(F_m(p)=\Pr\{\operatorname{rank} S_{m,p}<2\}\).

Set \(a=1-p\) and \(b=1-2p+\tfrac32p^2\). The exact probability, for every stated parameter, is
\[
 F_m(p)=2a^m+2b^m-3a^{2m}.
\]
For each \(m\ge2\), this probability has a **unique** minimizing density \(p_m\in(2/3,1)\). It is the unique root in that interval of
\[
 (3p-2)b^{m-1}=a^{m-1}(1-3a^m).
\]
In particular, \(p_2=\sqrt{2/3}\), with \(F_2(p_2)=1/3\), versus \(F_2(1)=1/2\). For \(W\) denoting the nonnegative inverse of \(w\mapsto we^w\),
\[
 p_m=\frac23+\frac{W(m)}{3m}+o(m^{-1}),\qquad
 F_m(p_m)\sim 2\,3^{-m}.
\]
For comparison, dense independent signs have \(F_m(1)=2^{1-m}\); hence the optimized-to-dense failure ratio is asymptotic to \((2/3)^m\). The fixed density \(p=2/3\) has \(F_m(2/3)=4\,3^{-m}-3\,9^{-m}\): its leading failure coefficient is twice the optimized one, despite the optimizing density tending to \(2/3\).

## Assumptions and scope

All ranks are over the real numbers, in exact arithmetic; a global nonzero rescaling of all sketch entries does not change the result. Rows and all entries are independent. The column dimension is **exactly two**, the number of rows is any integer \(m\ge2\), and the density \(p\) is common to all entries. This is a rank-survival benchmark for a two-dimensional coordinate subspace, not a uniform subspace-embedding guarantee on all orientations or a bound on its condition number. In applications to sketched QR, lost column rank is a necessary failure condition for constructing a full-column-rank sketched factorization; full rank by itself is not a numerical stability guarantee.

## Proof

**1. Exact rank law.** Each row is either zero or lies on one of exactly four projective lines in \(\mathbb R^2\): the horizontal axis, vertical axis, positive diagonal, and negative diagonal. Their individual nonzero-row probabilities are, respectively, \(p(1-p)\), \(p(1-p)\), \(p^2/2\), \(p^2/2\); the zero-row probability is \(a^2\). Thus the probabilities that a row lies *in* a given line, including the origin, are \(a\), \(a\), \(b\), \(b\). Rank is less than two exactly when **all** rows lie on at least one of these lines. Any intersection of two distinct line events consists precisely of all-zero rows and has probability \(a^{2m}\). The union-of-four-events formula therefore yields \(2a^m+2b^m-3a^{2m}\), including at \(p=1\).

**2. Unique optimum.** Direct differentiation gives \(F'_m(p)=2m\,a^{m-1}H_m(p)\) for \(0<p<1\), where
\[
 H_m(p)=-1+(3p-2)(b/a)^{m-1}+3a^m.
\]
For \(0<p<2/3\), equivalently write \(F'_m(p)/(2m)=-a^{m-1}-(2-3p)b^{m-1}+3a^{2m-1}\). Since \(b-a^2=p^2/2>0\) and \(2-3p>0\), this is strictly smaller than or equal to \(-a^{m-1}+a^{2m-2}<0\). The derivative at \(p=2/3\) is also negative since \(H_m(2/3)=-1+3^{1-m}<0\).

For \(2/3<p<1\), \(b/a\ge1\) is strictly increasing. Consequently
\[
 H'_m(p)\ge 3(b/a)^{m-1}-3m a^{m-1}
 \ge 3\bigl(1-m/3^{m-1}\bigr)>0
\]
for every integer \(m\ge2\); the omitted product-rule contribution is positive. As \(p\uparrow1\), \(H_m(p)\to+\infty\). There is exactly one zero of \(H_m\) in \((2/3,1)\), with the derivative negative before and positive after it. This proves the unique global optimum on \((0,1]\). For \(m=2\), simplification gives \(F_2(p)=1-2p^2+\tfrac32p^4\), whose minimizing positive root is \(\sqrt{2/3}\).

**3. Sharp limiting density and risk.** Write \(p_m=2/3+\delta_m\), so
\[
 a=\frac13-\delta_m,\qquad b=\frac13+\frac32\delta_m^2,
\qquad
 3\delta_m=(a/b)^{m-1}(1-3a^m).
\]
Because \(a/b\le1-3\delta_m\), the last equality implies \(3\delta_m\le e^{-3(m-1)\delta_m}\). Hence
\[
 0<\delta_m\le\frac{W(m-1)}{3(m-1)}
\]
and in particular \(\delta_m=O(\log m/m)\), \(m\delta_m^2\to0\). Taking logarithms of the exact stationarity equation, using \(3a^m\to0\) and \(\log(a/b)=-3\delta_m+O(\delta_m^2)\), gives
\[
 \log(3\delta_m)=-3m\delta_m+o(1).
\]
With \(x_m=3m\delta_m\), this is \(x_m+\log x_m=\log m+o(1)\). Since \(x\mapsto x+\log x\) has derivative at least one on positive arguments, \(x_m=W(m)+o(1)\). The expansion for \(p_m\) follows.

Next \((3a)^m=(1-3\delta_m)^m=e^{-W(m)+o(1)}=o(1)\), while \((3b)^m=(1+\tfrac92\delta_m^2)^m\to1\), and \(3^ma^{2m}\to0\). Substitution into the exact formula proves \(F_m(p_m)\sim2\,3^{-m}\). The displayed fixed-density and dense comparisons follow by direct substitution.

## Verification

Running `python3 check.py` with Python 3.9 or later (standard library only) checks the rank law by explicit row-outcome enumeration using exact rational arithmetic for every \(m\in\{2,3,4\}\) and five rational densities, plus derivative sign and numerical root diagnostics for \(2\le m\le160\). The supplied run reports 497 checks passed. These finite checks supplement, but do not replace, the analytic all-\(m\) proof above.

## Relationship to prior work

Balabanov, *Randomized Cholesky QR factorizations* (first arXiv public version October 18, 2022), describes rank-revealing sketched QR with Gaussian and structured sign sketches and general embedding bounds, not this i.i.d. ternary two-column exact rank distribution or sparsity optimizer. Coja-Oghlan and collaborators study sparse-random-matrix rank at growing dimensions and prescribed degree distributions; their asymptotic regime does not imply the fixed-two-column probability law or its optimal interior density. Litvak and Tikhomirov study square Bernoulli-matrix singularity in a different dimension and entry model. Dense Rademacher rank-two bounds cover the endpoint \(p=1\), not the full sparsity optimization and Lambert-\(W\) boundary layer. These distinctions are comparison of implications, not claims that all possible literature has been exhausted.

## Limitations

The statement concerns **exact rank** only. It does not optimize numerical conditioning, stable embedding distortion, running time, or all subspaces simultaneously. The event probabilities are for independent zero/signed entries, not fixed-count sparsification, CountSketch, SRHT, stochastic rounding of an existing matrix, or a dense Gaussian projection. The Lambert-\(W\) asymptotic concerns increasing row count with exactly two columns. Independent mathematical validation and publication-priority adjudication have not been performed; equivalent niche formulations outside the inspected sources remain possible.

## References

- A. E. Litvak and K. E. Tikhomirov, *Singularity of sparse Bernoulli matrices*, arXiv:2004.03131, first publicly posted April 7, 2020, https://arxiv.org/abs/2004.03131.
- O. Balabanov, *Randomized Cholesky QR factorizations*, arXiv:2210.09953, first publicly posted October 18, 2022, https://arxiv.org/abs/2210.09953.
- A. Coja-Oghlan, A. A. Ergür, P. Gao, S. Hetterich and M. Rolvien, *The rank of sparse random matrices*, *Random Structures & Algorithms*, DOI:10.1002/rsa.21085, first published April 23, 2022, https://doi.org/10.1002/rsa.21085.
- A. Coja-Oghlan et al., *The full rank condition for sparse random matrices*, arXiv:2112.14090, first publicly posted December 28, 2021, https://arxiv.org/abs/2112.14090.
