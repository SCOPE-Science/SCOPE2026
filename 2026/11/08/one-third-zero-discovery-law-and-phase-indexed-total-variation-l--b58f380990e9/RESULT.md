# One-third zero-discovery law and phase-indexed total-variation limits for dyadic occupancy

## Finding
Let \(Z_1,Z_2,\ldots\) be independent draws from \(\Pr(Z_i=j)=2^{-j}\), \(j=1,2,\ldots\). Let \(K_n=|\{Z_1,\ldots,Z_n\}|\) and let \(D_n=K_{2n}-K_n\), the number of previously unseen categories discovered in the next \(n\) draws. For every \(v>0\), define
\[
 a_k(v)=e^{-v2^{-k}}-e^{-2v2^{-k}},\quad k\in\mathbb Z,
 \qquad L_v=\sum_{k\in\mathbb Z} B_k(v),
\]
where the \(B_k(v)\) are independent Bernoulli variables with probabilities \(a_k(v)\). The sum is almost surely finite because \(\sum_{k\in\mathbb Z}a_k(v)=1\). Define the dyadic phase \(\eta_n=n/2^{\lfloor\log_2 n\rfloor}\in[1,2)\).

**Theorem.** There is an absolute constant \(C<\infty\) such that for every positive integer \(n\),
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(D_n),\mathcal L(L_{\eta_n})\bigr)
 \le C n^{-1/3}.
\]
Every phase law satisfies, **exactly**,
\[
 \mathbb E L_v=1,\qquad
 \Pr(L_v=0)=\frac13,\qquad
 \operatorname{Var}(L_v)=1-\sum_{k\in\mathbb Z}a_k(v)^2<1.
\]
Consequently,
\[
 \Pr(D_n=0)=\frac13+O(n^{-1/3}),\qquad
 \mathbb E D_n=1+O(n^{-1}),
\]
and no limiting law \(L_v\) is Poisson. In particular, the zero-discovery probability differs from that of a mean-one Poisson variable by the fixed positive gap \(e^{-1}-1/3\). Along any integers \(n_m\) with \(\eta_{n_m}\to v\in[1,2]\), the laws of \(D_{n_m}\) converge in total variation to \(L_v\), with \(L_2\overset d=L_1\). Conversely every \(v\in[1,2)\) occurs along \(n_m=\lfloor v2^m\rfloor\).

The exact Poissonized identities underlying the result hold at every real \(t>0\). If unit-rate Poisson arrival times are independently marked with the same box probabilities and \(N(t)\) counts boxes first hit during \((t,2t]\), then
\[
 \mathbb E N(t)=1-e^{-t},\qquad
 \Pr(N(t)=0)=\frac{1+e^{-t}+e^{-2t}}3.
\]

## Assumptions and scope
All draws are iid and use the **fixed** geometric mass function \(2^{-j}\) on positive integer boxes. The second observation interval has exactly the same length as the first: draws \(n+1,\ldots,2n\), or times \((t,2t]\) in the Poisson embedding. The asserted rate is asymptotic (an unspecified absolute constant); no independence between fixed-sample category-discovery indicators is assumed. \(d_{\mathrm{TV}}\) is total-variation distance for integer-valued laws. Poissonization is an exact coupling construction, not a replacement of the fixed-sample claim.

## Proof
**1. Independent first-hit times.** Mark a unit-rate Poisson process with iid box labels. Poisson thinning gives independent rate-\(2^{-j}\) clocks, hence independent first-hit times \(E_j\sim\operatorname{Exp}(2^{-j})\). The indicator of \(t<E_j\le2t\) is Bernoulli with probability
\[
 q_j(t)=e^{-t2^{-j}}-e^{-t2^{-(j-1)}}.
\]
It follows that \(N(t)=\sum_{j\ge1}\mathbf1\{t<E_j\le2t\}\) in distribution. The expectation telescopes:
\[
 \mathbb E N(t)=\sum_{j\ge1}q_j(t)=1-e^{-t}.
\]
This expectation identity is already contained in the variance calculation of Bogachev, Gnedin and Yakubovich (2008, Example 2.2); it is **not** asserted to be new.

**2. Exact void product.** Put \(y=e^{-t2^{-j}}\). The factor for box \(j\) is \(1-q_j(t)=1-y+y^2\). The polynomial factorization
\[
 1-y+y^2=\frac{(1-y^6)(1-y)}{(1-y^3)(1-y^2)}
\]
turns the product through box \(J\) into
\[
 \prod_{j=1}^J(1-q_j(t))
 =\frac{1-e^{-3t}}{1-e^{-t}}
  \frac{1-e^{-t2^{-J}}}{1-e^{-3t2^{-J}}}.
\]
As \(J\to\infty\), the last ratio tends to \(1/3\). The infinite product converges because \(\sum_j q_j(t)<\infty\). Therefore
\[
 \Pr(N(t)=0)=\frac{1-e^{-3t}}{3(1-e^{-t})}
 =\frac{1+e^{-t}+e^{-2t}}3.
\]
This is a distributional identity, not determined by the prior mean/variance formula.

**3. Uniform logarithmic-phase approximation.** For real \(v>0\), the sequence \((a_k(v))_{k\in\mathbb Z}\) sums to one by telescoping as \(k\) runs to both infinities. Thus \(L_v\) is well-defined and almost surely finite. If \(n=v2^m\) for an integer \(m\ge0\), reindexing \(j=m+k\) in the Poissonized representation identifies \(N(n)\) with \(\sum_{k\ge1-m}B_k(v)\). Construct this and \(L_v\) using the same independent Bernoulli variables. The omitted negative-index tail has total mean
\[
 \sum_{k\le-m}a_k(v)=e^{-v2^m}=e^{-n}.
\]
Therefore \(d_{\mathrm{TV}}(\mathcal L(N(n)),\mathcal L(L_v))\le e^{-n}\). For an integer \(n\), take \(m=\lfloor\log_2 n\rfloor\), \(v=\eta_n\), giving this bound without rounding.

**4. De-Poissonization in total variation.** Let \(T_r\) be the time of arrival \(r\) in the same marked unit-rate Poisson process. The marks at the first \(2n\) arrivals reproduce exactly the original \(2n\) iid draws, and hence \(D_n\) counts first-hit times in \((T_n,T_{2n}]\). Define the expected instantaneous first-hit rate
\[
 \lambda(u)=\sum_{j\ge1}2^{-j}e^{-u2^{-j}},\quad u>0.
\]
For \(u\ge1\), write \(m=\lfloor\log_2 u\rfloor\). The terms with \(j>m\) satisfy \(\sum_{j>m}u2^{-j}<2\). For \(j\le m\), setting \(h=m-j\ge0\), we have \(u2^{-j}\in[2^h,2^{h+1})\), so
\[
 \sum_{j\le m}(u2^{-j})e^{-u2^{-j}}
 \le\sum_{h\ge0}2^{h+1}e^{-2^h}<3.
\]
The last estimate follows, for example, from \(e^{-2^h}\le2^{-2h}\) for integers \(h\ge1\). Hence \(\lambda(u)\le5/u\).

Let \(\delta=n^{2/3}\). Because \(\mathbb E T_n=n\), \(\operatorname{Var}(T_n)=n\), and likewise for \(T_{2n}\), Chebyshev gives
\[
 \Pr\bigl(|T_n-n|>\delta\ \text{or}\ |T_{2n}-2n|>\delta\bigr)
 \le3n^{-1/3}.
\]
On the complementary event, the counts in \((T_n,T_{2n}]\) and \((n,2n]\) can differ only if a first-hit time lies in one of the two deterministic bands of width \(2\delta\) centered on \(n\) and \(2n\). For all sufficiently large \(n\), these bands stay within \([n/2,3n]\). Their expected number of first hits is bounded by the integral of \(\lambda(u)\le5/u\), hence is \(O(\delta/n)=O(n^{-1/3})\). Markov's inequality and the coupling inequality give
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(D_n),\mathcal L(N(n))\bigr)
 =O(n^{-1/3}).
\]
Combining with the \(e^{-n}\) bound from step 3 proves the stated uniform result. Enlarging the absolute constant covers the finitely many smaller \(n\).

**5. Consequences and phase limits.** Sending \(t\to\infty\) in the exact Poissonized void identity and using the coupling gives \(\Pr(L_v=0)=1/3\) for every \(v>0\). Direct independent-Bernoulli moments show \(\mathbb EL_v=1\) and \(\operatorname{Var}(L_v)=\sum_k a_k(v)(1-a_k(v))=1-\sum_k a_k(v)^2<1\), excluding Poisson(1). For the fixed-sample mean, use
\[
 \mathbb E D_n=\sum_{j\ge1}\bigl((1-2^{-j})^n-(1-2^{-j})^{2n}\bigr).
\]
The estimate \(0\le e^{-nx}-(1-x)^n\le nx^2e^{-nx}\) for \(0\le x\le1\), combined with the uniform dyadic bound \(\sum_j(n2^{-j})^2e^{-n2^{-j}}=O(1)\), shows that this differs from \(\mathbb E N(n)=1-e^{-n}\) by \(O(n^{-1})\).

For \(v\) in the compact interval \([1,2]\), the two tails of the series \(\sum_k a_k(v)\) vanish uniformly. A Bernoulli coupling and dominated convergence therefore show \(v\mapsto\mathcal L(L_v)\) is continuous in total variation. Reindexing gives \(L_{2v}\overset d=L_v\). The phase subsequences in the theorem follow immediately.

## Verification
The bundled `verify_one_third.py` checks the polynomial factorization with integer coefficients; rational finite-sample occupancy subevents; the finite telescoping formula and phase moments using numerics. It passed **120 checks** in a clean Python standard-library run. Those checks are supporting reproducibility evidence: the all-size distributional and total-variation statements follow from the analytic argument above, not from a finite enumeration. For a finite illustration, exact sampling gives \(\Pr(D_1=0)=1/3\) but \(\Pr(D_2=0)=97/315\), showing that the fixed-sample law is not simply equal to its limit at every size.

## Relationship to prior work
Derbazi, Gnedin and Marynych (arXiv:2308.01739, 2023; *ALEA* 2024) prove Poisson approximation for record processes under conditions that exclude geometric frequencies, and explicitly identify the bounded-small-count contraction-scale case as outside their article. Bogachev, Gnedin and Yakubovich (arXiv:math/0609498, 2006/2008), Example 2.2 and equations (2.12)–(2.13), **already prove** the exact identity \(\operatorname{Var}K(t)=\mathbb E[N(t)]=1-e^{-t}\) for geometric probabilities \(2^{-j}\). That known identity is used here, not claimed as novel. Their variance and occupancy-count analysis does not state the one-third no-discovery probability, its fixed-sample transfer, or the phase-indexed total-variation law. Barbour and Gnedin (arXiv:0809.4387, 2008/2009) address small occupancy-count distributions and the bounded/oscillatory geometric regime, rather than the temporal first-hit count on a doubling interval.

## Limitations
The exact \(1/3\) constant depends on the dyadic ratio of box masses **and** the doubling time window; this proof does not extend it to arbitrary geometric ratios or observation-window lengths. The convergence rate \(O(n^{-1/3})\) comes from elementary clock concentration and is not asserted optimal. Independent historical-priority verification has not been performed. Generic formulas for the probability generating function of a Poisson-binomial sum are standard; the claim is the specific exact product reduction and uniform fixed-sample limit, not the existence of a Bernoulli decomposition under Poisson thinning.

## References
- Z. Derbazi, A. Gnedin, A. Marynych, *Records in the Infinite Occupancy Scheme*, arXiv:2308.01739v1 (first public 2023-08-03), https://arxiv.org/abs/2308.01739; *ALEA* 21 (2024), https://alea.impa.br/articles/v21/21-55.pdf.
- L. V. Bogachev, A. V. Gnedin, Yu. V. Yakubovich, *On the Variance of the Number of Occupied Boxes*, arXiv:math/0609498 (2006), https://arxiv.org/pdf/math/0609498; see Section 2.2, Example 2.2 and Section 2.3.
- A. D. Barbour, A. Gnedin, *Small Counts in the Infinite Occupancy Scheme*, arXiv:0809.4387 (2008), https://arxiv.org/pdf/0809.4387; see introduction and Section 4.
