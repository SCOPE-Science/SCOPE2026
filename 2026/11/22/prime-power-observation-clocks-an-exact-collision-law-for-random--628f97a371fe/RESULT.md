# Prime-power observation clocks: an exact collision law for random cellular-automaton cylinders

## Finding

For the bilateral difference cellular automaton \((Fx)_i=x_i-x_{i+1}\) over \(\mathbb F_p\), choose \(m\) observed sites uniformly without replacement in a window of length \(pb\), with \(b=p^a\). For any prescribed symbols on the sites, their cylinder first covers the entire configuration space at a **sampled Frobenius clock** \(\ell b\), with \(1\le\ell\le p\), if and only if no residue class modulo \(b\) contains more than \(\ell\) observed sites. This gives an exact finite-size distribution and sharp multi-level Poisson transition.

Write \(c_r=|E\cap\{r,r+b,\ldots,r+(p-1)b\}|\), \(0\le r<b\). Then, for all nonempty supports \(E\subseteq\{0,\ldots,pb-1\}\), symbols \(v\), and \(1\le\ell\le p\),

\[
\operatorname{rank}\bigl(\ker F^{\ell b}|_E\bigr)=\sum_{r=0}^{b-1}\min(c_r,\ell),\qquad
F^{\ell b}(C_E(v))=X\iff\max_r c_r\le\ell.
\]

The first successful time **among** \(b,2b,\ldots,pb\) is \(bT_b\), where \(T_b=\max_r c_r\). In particular this clock is independent of the values of the observed symbols. For a uniform size-\(m\) support, with \(1\le m\le pb\), its exact cumulative distribution is

\[
\mathbb P(T_b\le\ell)=
\frac{[z^m]\bigl(\sum_{j=0}^{\ell}\binom pj z^j\bigr)^b}{\binom{pb}{m}},
\quad 1\le\ell\le p.
\]

The complete deficiency distribution at time \(\ell b\), where \(D_{b,\ell}=\sum_r(c_r-\ell)_+\), is given by

\[
\mathbb E\,u^{D_{b,\ell}}=
\frac{[z^m]\bigl(\sum_{j=0}^{p}\binom pj z^j u^{(j-\ell)_+}\bigr)^b}{\binom{pb}{m}}.
\]

For fixed \(p\), fixed \(1\le\ell<p\), and \(a\to\infty\), with \(m\sim c b^{\ell/(\ell+1)}\) and \(c>0\),

\[
D_{b,\ell}\Rightarrow\operatorname{Poisson}(\lambda),\quad
\lambda=\binom p{\ell+1}(c/p)^{\ell+1};\quad
\bigl(\mathbb P(T_b=\ell),\mathbb P(T_b=\ell+1)\bigr)
\to(e^{-\lambda},1-e^{-\lambda}).
\]

If \(m=o(b^{\ell/(\ell+1)})\), the probability of full image at clock \(\ell b\) tends to one. If \(m/b^{\ell/(\ell+1)}\to\infty\), it tends to zero. The thresholds for successive \(\ell\) are distinct.

## Assumptions and scope

\(p\) is a fixed prime, \(a\ge1\), and \(b=p^a\). Work in the full two-sided shift \(X=\mathbb F_p^{\mathbb Z}\) and define the left shift by \((Sx)_i=x_{i+1}\), so \(F=I-S\). Choose a nonempty support \(E\) in \(\{0,\ldots,pb-1\}\). The cylinder \(C_E(v)\) fixes only sites of \(E\), not the intervening coordinates. A random support is sampled **uniformly without replacement** among the \(m\)-subsets; randomness does not involve the prescribed symbols. In the asymptotic statements, \(p\) and \(\ell\) are fixed and \(b\) runs through prime powers; the threshold assertions allow any positive integer sequence \(m=m_b\le pb\). The sampled covering time does not assert an exact first covering time at intervening integer times.

## Proof

**1. Kernel decomposition.** In characteristic \(p\), the Frobenius identity gives \(F^b=(I-S)^b=I-S^b\), and therefore \(F^{\ell b}=(I-S^b)^\ell\). On each residue class \(r\pmod b\), the kernel equation is the \(\ell\)-th forward finite difference equation \((I-T)^\ell f=0\), with \(f(j)=x_{r+jb}\), \(j\in\mathbb Z\). Its complete solution space has dimension \(\ell\), with basis \(j\mapsto\binom jh\bmod p\), \(0\le h<\ell\): Pascal's difference identity verifies membership, and the initial values at \(j=0,\ldots,\ell-1\) give a unit lower-triangular matrix, hence independence and completeness by the order-\(\ell\) recurrence. As \(\ell\le p\), each basis member is a genuine polynomial in \(j\bmod p\) of degree \(h\), with invertible leading coefficient \(1/h!\). Thus evaluation at any \(c_r\) distinct elements of \(\{0,\ldots,p-1\}\) has rank \(\min(c_r,\ell)\) by the usual Vandermonde argument. Different residue classes are independent; adding ranks gives the asserted formula.

**2. From ranks to images.** The extreme coefficients of \((I-S)^t\) are units, so for every \(y\in X\), the difference recurrence \(F^t x=y\) can be solved bilaterally by assigning \(t\) initial values and solving in both directions. Hence \(F^t\) is onto. Fix a target \(y\) and one antecedent \(x_0\). The set of possible traces on \(E\) among all antecedents is the affine space \(x_0|_E+(\ker F^t)|_E\). Every trace \(v\) is possible for every target exactly when this kernel trace has full dimension \(|E|\). Applying step 1 shows that this happens exactly when each \(c_r\le\ell\). Since \(1\le c_r\le p\) for occupied buckets and \(E\ne\varnothing\), the first successful sampled clock is \(T_b=\max_r c_r\).

**3. Exact probabilities.** A residue class modulo \(b\) consists of exactly \(p\) sites in the sampling window. Choosing \(j\) of them contributes \(\binom pj z^j\). Multiplying independent combinatorial choice enumerators over the \(b\) disjoint classes and extracting coefficient \([z^m]\) counts every \(m\)-subset once. Restricting \(j\le\ell\) counts full-image supports. Weighting by \(u^{(j-\ell)_+}\) tracks the exact kernel-rank deficiency. Division by \(\binom{pb}{m}\) proves both generating-function identities.

**4. Poisson window.** Put \(s=\ell+1\) and let \(Z_b\) be the number of residue classes containing exactly \(s\) sampled sites. For each fixed positive integer \(k\),

\[
\mathbb E(Z_b)_k=(b)_k\binom ps^k
\frac{\binom{p(b-k)}{m-sk}}{\binom{pb}{m}},
\]

where a binomial with an inadmissible lower index is zero. When \(m\sim c b^{(s-1)/s}\), we have \(m\to\infty\), \(m/b\to0\), and the displayed expression tends to \(\bigl(\binom ps(c/p)^s\bigr)^k=\lambda^k\). The factorial-moment criterion gives \(Z_b\Rightarrow\operatorname{Poisson}(\lambda)\). Meanwhile the expected number of classes with at least \(s+1\) sites is bounded by

\[
 b\binom p{s+1}\frac{(m)_{s+1}}{(pb)_{s+1}}
 =O\bigl(b(m/b)^{s+1}\bigr)=o(1)
\]

when \(s<p\); for \(s=p\) such classes are impossible. Hence \(D_{b,\ell}=Z_b\) with probability tending to one. This proves the deficiency limit and \(\mathbb P(T_b\le\ell)\to e^{-\lambda}\). The scales of an \(\ell\)-fold versus \((\ell+2)\)-fold collision are different: for \(\ell>1\), \(\mathbb P(T_b\le\ell-1)\to0\), and for \(\ell+1<p\), \(\mathbb P(T_b\le\ell+1)\to1\); at either boundary these statements are automatic. This yields the stated two-point limit.

**5. Sharpness on both sides.** Below the critical scale, the expected number of classes containing any \(s\) selected sites is at most \(b\binom ps(m)_s/(pb)_s=o(1)\). Above it, choose any fixed \(C>0\) and couple uniform samples by selecting prefixes of one random permutation of the \(pb\) sites. The larger sample contains the \(\lfloor Cb^{(s-1)/s}\rfloor\)-sample for all sufficiently large \(b\), so its probability of no \(s\)-fold collision is bounded above by \(\exp\{-\binom ps(C/p)^s\}+o(1)\). Sending \(C\to\infty\) gives zero. This proves the claimed sharp regimes. \(\square\)

## Verification

Run `python3 verify_cylinder.py` using Python's standard library. The script independently computes full Pascal-binomial evaluation-matrix ranks over finite fields and compares them with the residue-class rank formula in 7,080 finite cases. It exhaustively checks the full deficiency enumerator for three small parameters and simulates uniform-without-replacement sampling against an exact finite probability. These tests support, but do not replace, the all-parameter algebraic proof or the asymptotic factorial-moment argument.

## Relationship to prior work

Haugland, Larsen, Omland and Rustad (2026) establish qualitative sufficient criteria for locally eventually onto cellular automata (their Theorem 5.4), motivating an exact, random-support **covering clock** for a canonical linear rule. That theorem does not give the residue-class rank law or its occupancy distribution. The classical generalized birthday problem studies multiple occupancy and Poisson limits (Henze, 1998); its random independent placements have no cellular-automaton image interpretation, and our supports are sampled without replacement from groups of fixed capacity \(p\). Thus the occupancy asymptotic is a familiar probabilistic ingredient, **not** claimed as a newly discovered Poisson mechanism. Previously available special-geometry difference-automaton restriction results for regularly spaced sites and two separated blocks do not supply the stated all-subset rank identity or the random-clock classification. No claim of priority beyond checked sources is made.

## Limitations

The theorem is confined to the particular bilateral linear automaton \(I-S\), to prime-power windows of length \(pb\), and to clocks divisible by \(b\), at most \(pb\). It does not determine the absolute first successful iterate among all integer times, nor address general nonlinear rules. The asymptotic parameter \(p\) is fixed. An earlier equivalent presentation in unrestricted finite-field coding or occupancy literature cannot be excluded by a finite literature search. There has been no independent mathematical audit.

## References

- J. K. Haugland, N. S. Larsen, T. Omland, H. G. Rustad, *Locally eventually onto cellular automata*, arXiv:2610.33131v1, first posted October 23, 2026. https://arxiv.org/abs/2610.33131
- N. Henze, *A Poisson limit law for a generalized birthday problem*, Statistics & Probability Letters **39** (1998), 333–336, DOI:10.1016/S0167-7152(98)00076-5. https://publikationen.bibliothek.kit.edu/16098

