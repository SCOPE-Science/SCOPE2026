# Weak off-diagonal necessity for monomial-curve commutators in every dimension

## Statement

Let \(n\ge 2\), let
\[
\gamma(t)=
\begin{cases}
(\varepsilon_1 |t|^{\beta_1},\ldots,\varepsilon_n |t|^{\beta_n}),&t\ge0,\\
(\varepsilon'_1 |t|^{\beta_1},\ldots,\varepsilon'_n |t|^{\beta_n}),&t<0,
\end{cases}
\]
be a monomial curve, where \(0<\beta_1<\cdots<\beta_n\), each sign is in
\(\{-1,1\}\), and the two sign vectors are not identical. Write
\[
H_\gamma f(x)=\operatorname{p.v.}\int_{\mathbb R}f(x-\gamma(t))\,\frac{dt}{t}
\]
and \(T_b=[b,H_\gamma]\).

For a \(\gamma\)-rectangle \(Q\), the side lengths are
\(r^{\beta_1},\ldots,r^{\beta_n}\) for some \(r>0\). Put
\[
|\beta|=\beta_1+\cdots+\beta_n,\qquad
\delta=\frac1p-\frac1q,\qquad
\alpha=|\beta|\delta ,
\]
and
\[
\|b\|_{\operatorname{BMO}^{\gamma,\alpha}}
=
\sup_Q |Q|^{-\delta}
\frac1{|Q|}\int_Q |b-b_Q|.
\]

**Theorem.** If \(1<p\le q<\infty\), \(b\in L^1_{\rm loc}(\mathbb R^n)\), and
\[
T_b:L^p(\mathbb R^n)\longrightarrow L^{q,\infty}(\mathbb R^n)
\]
is bounded, then
\[
\boxed{
\|b\|_{\operatorname{BMO}^{\gamma,\alpha}}
\lesssim_{\gamma,p,q}
\|T_b\|_{L^p\to L^{q,\infty}} .
}
\]

Thus strong \(L^p\to L^q\) boundedness has the same necessary anisotropic
Campanato condition in every dimension. More strongly, weak \(L^q\) control
already forces it.

## Consequence in the known sufficiency range

Oikari proved that for \((1/p,1/q)\) in his admissible region \(\Xi(n)\), with
\(p\le q\) and \(\alpha/|\beta|=1/p-1/q\),
\[
\|T_b\|_{L^p\to L^q}
\lesssim
\|b\|_{\operatorname{BMO}^{\gamma,\alpha}} .
\]
Combining that result with the theorem above gives, throughout this region and
in every dimension \(n\ge2\),
\[
\boxed{
\|b\|_{\operatorname{BMO}^{\gamma,\alpha}}
\lesssim
\|T_b\|_{L^p\to L^{q,\infty}}
\le
\|T_b\|_{L^p\to L^q}
\lesssim
\|b\|_{\operatorname{BMO}^{\gamma,\alpha}} .
}
\]
Consequently weak \(L^p\to L^{q,\infty}\) boundedness and strong
\(L^p\to L^q\) boundedness are equivalent there.

Oikari's 2023 necessity theorem was restricted to monomial curves in the
plane. Li and Zeng's 2026 higher-dimensional necessity theorem treats the
diagonal case \(p=q\). The statement above supplies the off-diagonal
higher-dimensional necessity and strengthens the target to weak \(L^q\).

## Lorentz norm lemma

For \(1<q<\infty\), define
\[
\|h\|_{q,\infty,*}
=
\sup_{0<|F|<\infty}
|F|^{-1/q'}\int_F |h|.
\]
Then
\[
\|h\|_{L^{q,\infty}}
\le
\|h\|_{q,\infty,*}
\le
q'\|h\|_{L^{q,\infty}}.
\]
The second inequality follows by integrating the distribution estimate
\(|\{|h|>t\}|\le(\|h\|_{q,\infty}/t)^q\), splitting at
\(t=\|h\|_{q,\infty}|F|^{-1/q}\).
The reverse inequality follows by testing on a level set (and truncating it
when necessary).

Unlike the usual weak quasi-norm, \(\|\cdot\|_{q,\infty,*}\) satisfies the
triangle inequality, and it also has the integral Minkowski property
\[
\left\|\int h_u\,d\mu(u)\right\|_{q,\infty,*}
\le
\int\|h_u\|_{q,\infty,*}\,d\mu(u).
\]
Indeed this follows immediately by integrating the absolute value over each
finite-measure test set \(F\).

## Proof of the theorem

Fix a \(\gamma\)-rectangle \(Q\), and put
\[
m_Q=\frac1{|Q|}\int_Q |b-b_Q|.
\]
Use the companion rectangle \(P\) and the change-of-variables decomposition
constructed by Li and Zeng. It has \(|P|=|Q|\). Their geometric lemma and
Jacobian normalization are independent of the output exponent; after a fixed
choice of the geometric parameters, they split the argument according to
\[
E=\{z\in P:|b(z)-b_Q|\ge m_Q\}.
\]

### Case 1: \(|E|\ge |P|/2\)

Li and Zeng's pointwise decomposition on \(E\) expresses
\(|b-b_Q|\) up to a fixed factor as a sum of parameter averages of translates
of
\[
T_b 1_{Q+\xi},
\]
where every translated input set has measure \(|Q|\). The Jacobian error is
absorbed pointwise before any function-space estimate is used.

Take the norm \(\|\cdot\|_{q,\infty,*}\). The integral Minkowski property,
translation invariance, and the assumed weak bound give exactly the same
dimensionless parameter integrals as in the diagonal proof, but now
\[
\|T_b1_{Q+\xi}\|_{q,\infty,*}
\lesssim_q
\|T_b\|_{L^p\to L^{q,\infty}}\,|Q|^{1/p}.
\]
On the other hand, \(|b-b_Q|\ge m_Q\) on \(E\), so
\[
m_Q |E|^{1/q}
\le
\|(b-b_Q)1_E\|_{q,\infty,*}.
\]
Since \(|E|\ge |Q|/2\), it follows that
\[
m_Q\lesssim_{\gamma,p,q}
\|T_b\|_{L^p\to L^{q,\infty}}
|Q|^{1/p-1/q}.
\]

### Case 2: \(|P\setminus E|>|P|/2\)

Li and Zeng use
\[
g=
\left(
\operatorname{sgn}(b-b_Q)
-\left\langle\operatorname{sgn}(b-b_Q)\right\rangle_Q
\right)1_Q,
\qquad |g|\le2,
\]
and obtain on \(P\setminus E\) a pointwise estimate of \(m_Q\) by the same
kind of parameter averages of translates of \(T_bg\); again the Jacobian
error is absorbed pointwise. Since
\[
\|g\|_p\le2|Q|^{1/p},
\]
the Lorentz norm lemma and integral Minkowski inequality yield
\[
m_Q |P\setminus E|^{1/q}
\lesssim_{\gamma,p,q}
\|T_b\|_{L^p\to L^{q,\infty}}
|Q|^{1/p}.
\]
Using \(|P\setminus E|>|Q|/2\) gives the same estimate
\[
m_Q\lesssim_{\gamma,p,q}
\|T_b\|_{L^p\to L^{q,\infty}}
|Q|^\delta .
\]

Multiplying by \(|Q|^{-\delta}\) and taking the supremum over all
\(\gamma\)-rectangles proves the theorem.

The higher-dimensional companion construction is the one in Li--Zeng:
their paper writes the geometry explicitly in dimension three to simplify
notation and states that the determinant argument extends to arbitrary
dimension; their main theorem is correspondingly stated in all dimensions.

## Checks and boundary cases

- When \(q=p\), \(\delta=\alpha=0\), so the result recovers the usual
  \(\operatorname{BMO}_\gamma\) necessity while weakening the hypothesis from
  strong \(L^p\) boundedness to weak \(L^p\) boundedness.
- No interpolation is used. The factor \(|Q|^{1/p-1/q}\) comes directly
  from the size of the input rectangle and of the major output subset.
- The proof requires \(q>1\) for the normable Lorentz functional above; this
  is automatic under \(1<p\le q<\infty\).
- The theorem is a necessity statement for every \(p\le q\). Strong
  sufficiency is claimed only in Oikari's established region \(\Xi(n)\).
- Nothing here treats \(q<p\), compactness/VMO, weighted commutators, or
  endpoint exponents.

## Prior literature and originality scope

Li and Zeng, *Curved commutators in higher dimensions*,
arXiv:2609.18613v1 (16 September 2026), prove the all-dimensional converse
for the diagonal mapping \(L^p\to L^p\). Their Sections 2--3 provide the
companion-rectangle and pointwise commutator decomposition used above.

Oikari, *On the \(L^p\)-to-\(L^q\) boundedness and compactness of commutators
along monomial curves*, arXiv:2304.00621, proves the all-dimensional
off-diagonal sufficiency theorem in the region \(\Xi(n)\), but explicitly
restricts necessity to the plane.

Bongers--Guo--Li--Wick, *Commutators of Hilbert transforms along monomial
curves*, Studia Math. 257 (2021), established the foundational diagonal
upper bound and a weaker testing-space lower bound.

To the best of our knowledge, the weak-\(L^q\) all-dimensional necessity
above, and hence the all-dimensional off-diagonal characterization in
Oikari's sufficiency region, have not previously been stated. Exact and
synonymous searches for weak/Lorentz, off-diagonal, higher-dimensional,
monomial-curve commutator necessity located the works above but no matching
statement. The principal residual originality risk is unindexed simultaneous
work following the very recent Li--Zeng preprint.

No highly relevant inaccessible source was identified in this review.

## References

1. K. Li and Y. Zeng, *Curved commutators in higher dimensions*,
   arXiv:2609.18613v1, 2026. https://arxiv.org/abs/2609.18613
2. T. Oikari, *On the \(L^p\)-to-\(L^q\) boundedness and compactness of
   commutators along monomial curves*, arXiv:2304.00621, 2023.
   https://arxiv.org/abs/2304.00621
3. T. Bongers, Z. Guo, J. Li, B. D. Wick, *Commutators of Hilbert transforms
   along monomial curves*, Studia Math. 257 (2021), 295--311.
   https://arxiv.org/abs/1909.02118
