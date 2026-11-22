# Affine rigidity of the complete gap-run spectrum of two-generator numerical semigroups

## Finding

Let \(a\ge2\), \(1\le d<a\), \(\gcd(a,d)=1\) be integers. For every integer \(q\ge1\), write \(b=qa+d\) and \(S_{a,b}=\{ua+vb:u,v\in\mathbb Z_{\ge0}\}\). A *gap run* (also called a finite desert) is an inclusion-maximal interval of consecutive nonnegative integers missing from \(S_{a,b}\). Let \(H_\ell(a,b)\) be the number of such intervals with exactly \(\ell\) integers.

Put \(\tau_0=\tau_a=0\). For each \(1\le r<a\), define \(\tau_r\) to be the unique integer in \(\{1,\dots,a-1\}\) satisfying \(d\tau_r\equiv r\pmod a\). For \(1\le\ell<a\) and \(1\le r\le a-\ell\), put
\[
  U_{r,\ell}=\min_{r\le s<r+\ell}\tau_s,\qquad
  V_{r,\ell}=\max\{\tau_{r-1},\tau_{r+\ell}\}.
\]
Then for all the specified integers, simultaneously,
\[
\boxed{H_\ell(a,qa+d)=qA_\ell(a,d)+B_\ell(a,d)}
\]
where the explicit nonnegative integer coefficients are
\[
 A_\ell(a,d)=\sum_{r=1}^{a-\ell}\mathbf1_{U_{r,\ell}>V_{r,\ell}}(U_{r,\ell}-V_{r,\ell}),
\]
\[
 B_\ell(a,d)=\sum_{r=1}^{a-\ell}\mathbf1_{U_{r,\ell}>V_{r,\ell}}
 \left(\left\lfloor\frac{dU_{r,\ell}}a\right\rfloor-\left\lfloor\frac{dV_{r,\ell}}a\right\rfloor\right).
\]
There are no runs longer than \(a-1\). **Every individual run-length frequency is affine in the quotient \(q\), with no initial exceptions; the set of lengths with positive frequency is independent of \(q\).** In particular,
\[
 \boxed{H_{a-1}(a,qa+d)=q.}
\]
This is a complete, constructive length spectrum for every coprime pair of generators, not merely a statement about the longest block or the isolated gaps.

For example, when \((a,d)=(8,3)\), the complete gap-run polynomial is
\[
 \sum_{\ell\ge1}H_\ell(8,8q+3)z^\ell
 =q(9z+4z^2+z^4+z^7)+(3z+2z^2).
\]
Thus at \(q=1\) the frequencies at lengths \(1,2,4,7\) are \(12,6,1,1\), and at \(q=2\) they are \(21,10,2,2\); all other lengths have frequency zero.

## Assumptions and scope

All generators are positive coprime integers with \(2\le a<b\), uniquely expressed as \(b=qa+d\), \(q\ge1\), \(1\le d<a\). No probabilistic limit or additional regularity assumption is needed. The theorem counts *maximal consecutive intervals of missing nonnegative integers*, not differences between successive gaps and not factorization-length sets. The running variable \(z\) only marks the number of integers in a gap run. The coefficient formula includes \(a=2\) and \(d=1\). The case \(q=0\), in which \(a\) would not be the smaller generator, is not asserted.

## Proof

**Step 1: exact least elements in residues.** Since \(\gcd(a,d)=1\), the integers \(tb\) for \(0\le t<a\) give the Apéry representatives of \(S_{a,b}\) modulo \(a\). Indeed, if \(ua+vb\equiv tb\pmod a\), with \(u,v\ge0\), then \(v\equiv t\pmod a\), whence \(v\ge t\) and \(ua+vb\ge tb\). Conversely \(tb\in S_{a,b}\). Write
\[
 \tau_r b=a k_r+r,\qquad k_r=q\tau_r+\left\lfloor\frac{d\tau_r}{a}\right\rfloor
 \quad(1\le r<a),\qquad k_0=k_a=0.
\]
The number \(ja+r\), for \(j\ge0\) and \(1\le r<a\), is a gap if and only if \(j<k_r\). Every multiple of \(a\) is in the semigroup.

**Step 2: unique run locations.** A run cannot cross a multiple of \(a\). A run of exactly \(\ell\) missing integers must therefore be \(ja+r,\dots,ja+r+\ell-1\) with \(1\le r\le a-\ell\). Such an interval is maximal precisely when all its interior residues are gaps while its two neighboring residues are nongaps. Using \(k_0=k_a=0\), this is equivalent to
\[
 \max\{k_{r-1},k_{r+\ell}\}\le j<\min_{r\le s<r+\ell}k_s.
\]
The number of nonnegative integer \(j\) satisfying this is the positive part of the right endpoint minus the left endpoint. There is no double counting because a maximal run has a unique left endpoint \(ja+r\).

**Step 3: sign rigidity.** Define \(f_q(t)=qt+\lfloor dt/a\rfloor\) on \(\{0,\dots,a-1\}\). For \(q\ge1\), \(f_q\) is strictly increasing. Therefore the previous interval is nonempty exactly when \(U_{r,\ell}>V_{r,\ell}\), independently of \(q\). When this inequality holds, its length is
\[
 f_q(U_{r,\ell})-f_q(V_{r,\ell})
 =q(U_{r,\ell}-V_{r,\ell})
 +\left\lfloor\frac{dU_{r,\ell}}a\right\rfloor
 -\left\lfloor\frac{dV_{r,\ell}}a\right\rfloor.
\]
Summing the contributions over all starting residues \(r\) proves the formula. Each term in both coefficients is nonnegative; the slope is strictly positive whenever the corresponding window is eligible. Thus \(H_\ell\) is positive for one positive \(q\) if and only if it is positive for *every* positive \(q\). The maximum possible length is \(a-1\); for \(\ell=a-1\), the sole start is \(r=1\), the interior ranks are \(1,\dots,a-1\), and both boundary ranks are zero. Hence \(A_{a-1}=1\), \(B_{a-1}=0\), proving \(H_{a-1}=q\).

**Consistency: genus and known total block count.** Each missing integer lies in exactly one run. The above Apéry thresholds give the total number of gaps
\[
 \sum_{\ell=1}^{a-1}\ell H_\ell(a,qa+d)
 =\sum_{r=1}^{a-1}k_r
 =q\frac{a(a-1)}2+\frac{(a-1)(d-1)}2
 =\frac{(a-1)(b-1)}2.
\]
Here the middle floor-sum identity follows by pairing the residues \(dt\pmod a\) for \(1\le t<a\). This is the classical Sylvester genus formula, not claimed as new. Likewise, the known formula of Moree for the *total* number of gap blocks is a consistency check, not part of the novelty claim.

## Verification

Run `python verify.py` with Python 3.8 or later. The checker constructs semigroup membership by independent forward coin-addition, extracts its maximal missing intervals, and compares their complete length histogram to the coefficient formula for all coprime \(2\le a<50\), \(1\le d<a\), and \(1\le q\le5\): **3,765 exact comparisons**. It also verifies the genus identity, modular-inverse slope and intercept sums, the count \(H_{a-1}=q\), and the explicit \((a,d)=(8,3)\) example. These finite checks are corroboration; the all-parameter theorem follows from Steps 1–3.

## Relationship to prior work

Komatsu and Ying [1] develop the \(p\)-Apéry approach to Frobenius and Sylvester invariants for triples in arithmetic progression, providing a number-theoretic starting point for this question. Moree [2], especially Lemma 4 and Theorem 12, establishes the **largest gap-run length** and the **total number of blocks** for two-generated semigroups, using the binary inclusion–exclusion polynomial; it also provides explicit polynomial coefficient support from which any fixed example can in principle be reconstructed. Singh and Ram [3] classify the isolated gaps, corresponding to runs of length one. A related published special-family result [4] concerns \(a=dt+1\) with second generator \(a+d\). These cover valuable boundaries, but none of the inspected statements gives the full coefficient-wise affine-in-\(q\) law, its entire length-spectrum invariance, and its all-pairs formula.

## Limitations

The result concerns two minimal generators only. It is an exact finite combinatorial theorem, not an asymptotic for random semigroups, and it does not classify three-generator gap spectra. The coefficient recipe depends on a residue permutation and requires finite arithmetic for each \((a,d)\); it does not supply uniform closed elementary polynomials in both \(a\) and \(d\). A fixed-instance gap histogram is computable from existing Apéry or binary-polynomial data; the contribution claimed here is the simultaneous parametric affine structure, and an unlocated equivalent derivation remains a priority risk. The theorem has not undergone independent external validation.

## References

[1] T. Komatsu and H. Ying, *The \(p\)-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052 (first public version 27 June 2022); *Symmetry* 15 (2023), 1328. https://arxiv.org/abs/2206.13052 ; https://doi.org/10.3390/sym15071328. The published article lists 11D07 first among its MSC codes.

[2] P. Moree, *Numerical semigroups, cyclotomic polynomials and Bernoulli numbers*, arXiv:1308.3972 (2013), especially Sections 2, 6, 7 and Theorem 12. https://arxiv.org/abs/1308.3972.

[3] S. N. Singh and R. K. Ram, *On Isolated Gaps of Numerical Semigroups of Embedding Dimension Two*, arXiv:2406.09848v1 (14 June 2024), especially Theorems 3.4 and 4.8. https://arxiv.org/abs/2406.09848.

[4] *Exact run-length frequencies for binary semigroups with \(a=dt+1\) and \(b=a+d\)*, published mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-run-length-frequencies-for-binary-semigroups-with-a-dt-1-a--584c998005ae. Only the indexed summary of [4] was accessible for comparison.

[5] The NumericalSgps documentation, `Deserts` operation (gap-run enumeration). https://gap-packages.github.io/numericalsgps/doc/chap3_mj.html.
