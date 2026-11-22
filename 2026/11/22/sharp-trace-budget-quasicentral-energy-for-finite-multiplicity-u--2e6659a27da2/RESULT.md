# Sharp trace-budget quasicentral energy for finite-multiplicity unilateral shifts

## Finding

Let \(r\geq 1\) be an integer, \(H=\ell^2(\mathbb N_0)\otimes\mathbb C^r\), \(T=S\otimes I_r\), with \(Se_n=e_{n+1}\), and let \(P\) project onto \(e_0\otimes\mathbb C^r\). For every real \(B\geq r\), define
\[
\mathcal E_r(B)=\inf\left\{\|[T,R]\|_{\mathcal S_2}^2:\ R\text{ finite rank},\quad 0\leq R\leq I,\quad RP=P,\quad\operatorname{Tr}R\leq B\right\}.
\]
Then \(\mathcal E_r(r)=r\), uniquely attained at \(R=P\). If \(B>r\), put \(b=B/r\) and \(m=\lceil 3b-2\rceil\). Then \(m\geq2\) and
\[
\boxed{\mathcal E_r(B)=r\left[\frac1m+\frac{3(m+1-2b)^2}{m(m^2-1)}\right].}
\]
The unique minimizer is \(R_*=\operatorname{diag}(x_0,x_1,\ldots)\otimes I_r\), where
\[
q=\frac{3(m+1-2b)}{m(m^2-1)},\qquad p=\frac1m-mq,\qquad
x_n=\begin{cases}(m-n)[p+q(m-n)],&0\leq n<m,\\0,&n\geq m.\end{cases}
\]
The trace budget is exactly saturated. The optimum is continuous and continuously differentiable in \(B>r\), and is strictly convex and quadratic between the cutoff transitions \(B/r=(m+2)/3\). Its second derivative changes at these transitions. For each fixed positive integer \(r\),
\[
\boxed{\mathcal E_r(B)\sim\frac{4r^2}{9B}\quad(B\longrightarrow\infty).}
\]
The optimal constant is genuinely different from a linear cutoff: along linear-cutoff budgets \(B=r(m+1)/2\), the linear taper has energy \(r/m\sim r^2/(2B)\), so the optimal-to-linear asymptotic ratio is \(8/9\).

## Assumptions and scope

The Hilbert spaces and Schatten norms are complex. The operator \(S\) is the *unweighted isometric unilateral shift*, \(r\) is finite and positive, and the admissible operators must be finite-rank positive contractions fixing the entire \(r\)-dimensional wandering subspace and satisfying a *real* upper trace bound \(B\geq r\). The minimization is over arbitrary such operators, not only diagonal or block-diagonal ones. The objective is the square of the standard, unnormalized Hilbert--Schmidt norm of the commutator \([T,R]=TR-RT\). A finite trace budget is necessary: a nonzero fixed wandering projection already costs trace \(r\).

## Proof

**1. Symmetry reduction without presupposing diagonal admissibility.** For \(z\in\mathbb T\) define \(W_z e_n=z^n e_n\). Then \(W_z S W_z^*=zS\), so the conjugations \(\operatorname{Ad}(W_z\otimes U)\), with \(U\in U(r)\), preserve positivity, contractivity, the condition \(RP=P\), trace and the commutator Hilbert--Schmidt norm. Averaging over both compact groups in trace-class norm gives the positive trace-class operator
\[
\overline R=\operatorname{diag}(x_0,x_1,\ldots)\otimes I_r,
\]
with \(x_0=1\), \(0\leq x_n\leq1\), \(\sum_{n\geq0}x_n\leq b\). Jensen's inequality for the Hilbert-space norm gives
\[
\|[T,\overline R]\|_2^2\leq\|[T,R]\|_2^2,
\quad
\|[T,\overline R]\|_2^2=r\sum_{n\geq0}(x_n-x_{n+1})^2.
\]
The averaged operator need not have finite rank, but this only relaxes the lower-bound problem. The explicit optimizer constructed below is finite rank, so the relaxation is exact.

**2. Exact active set.** For \(b>1\) choose the unique integer \(m\geq2\) such that
\[
\frac{m+1}{3}<b\leq\frac{m+2}{3};\qquad m=\lceil3b-2\rceil.
\]
Define \(p,q,x_n\) as in the finding. Direct summation using \(\sum_{t=1}^m t=m(m+1)/2\) and \(\sum_{t=1}^m t^2=m(m+1)(2m+1)/6\) gives
\[
x_0=1,\qquad \sum_{n=0}^{m-1}x_n=b.
\]
The budget inequalities imply \(q>0\), \(q\geq p\), and \(p+q>0\). The successive differences are
\[
x_n-x_{n+1}=p+q[2(m-n)-1]>0\qquad(0\leq n<m).
\]
Thus \(1=x_0>x_1>\dots>x_{m-1}>x_m=0\), with every coordinate within the contraction constraint.

**3. Global lower bound including infinite tails.** Let \(y=(y_n)\) be any feasible scalar profile from the relaxation, and set \(z_n=y_n-x_n\). The sequence \(z\) is summable and \(z_0=0\). Write \(D(y)=\sum_{n\geq0}(y_n-y_{n+1})^2\). Expansion and discrete summation by parts give
\[
D(y)-D(x)=D(z)-4q\left(\sum_{n\geq0}y_n-b\right)
 +2(q-p)y_m+4q\sum_{n>m}y_n.
\]
All terms on the right are nonnegative: \(q>0\), \(q\geq p\), \(y_n\geq0\), and \(\sum y_n\leq b\). Therefore \(D(y)\geq D(x)\). Equality implies \(D(z)=0\), so \(z\) is constant, and since \(z_0=0\), it vanishes identically. Thus the scalar optimizer is unique. The telescoping energy can be computed exactly:
\[
D(x)=\sum_{t=0}^{m-1}\left[\frac1m+q(2t-m+1)\right]^2
=\frac1m+\frac{q^2m(m^2-1)}3
=\frac1m+\frac{3(m+1-2b)^2}{m(m^2-1)}.
\]
This proves the claimed operator infimum and gives a finite-rank minimizer.

**4. Uniqueness among all operators.** Suppose \(R_1,R_2\) are two admissible optimal finite-rank operators. Their midpoint is admissible, and the Hilbert-space parallelogram law gives
\[
\left\|\left[T,\frac{R_1+R_2}{2}\right]\right\|_2^2
=\frac{\|[T,R_1]\|_2^2+\|[T,R_2]\|_2^2}{2}-\frac14\|[T,R_1-R_2]\|_2^2.
\]
Optimality forces \([T,R_1-R_2]=0\). If a compact operator \(K\) commutes with \(T\), then \(T^nv\rightharpoonup0\), so \(KT^nv\to0\) in norm; yet \(KT^nv=T^nKv\) has constant norm \(\|Kv\|\). Therefore \(K=0\). Hence \(R_1=R_2\). For \(B=r\), positivity, \(RP=P\), and \(\operatorname{Tr}R\leq r\) directly force \(R=P\).

**5. Cutoff transitions and asymptotics.** On each open budget interval where \(m\) is fixed, differentiation gives
\[
\frac{d\mathcal E_r}{dB}=-4q,
\qquad
\frac{d^2\mathcal E_r}{dB^2}=\frac{24}{r\,m(m^2-1)}.
\]
At \(b=(m+2)/3\), the \(m\)- and \((m+1)\)-site formulae agree together with their first derivatives; their distinct positive second derivatives establish genuine smooth-fit active-set transitions. As \(b\to\infty\), \(m=3b+O(1)\), giving \(D(x)\sim4/(9b)\). Multiplication by \(r\) yields the stated \(4r^2/(9B)\) law.

## Verification

An accompanying standalone exact-rational Python 3 program, `check_trace_shift.py`, tests 263,215 assertions on rational budgets and active sets, including normalized trace, positivity, strict coordinate decrease except at support transitions, stationarity, complementary slackness, exact energy, adjacent cutoffs, multiplicity scaling, and the \(B/r=3/2\) example. This is a consistency check, not an infinite-dimensional proof. For the latter example the unique profile is \((1,5/12,1/12,0,\ldots)\), with trace \(3/2\) and energy \(11/24\), all exact.

## Relationship to prior work

Liu and Zhao (arXiv:2611.15604v1, first posted 11 November 2026) prove qualitative vanishing of the Hilbert--Schmidt quasicentral modulus for almost normal operators. Their construction and theorem do not provide the sharp finite-trace budget for the shift. Voiculescu's *The condenser quasicentral modulus* (arXiv:2109.07633v7) develops general operator-condenser variational methods and computes a bilateral-shift example with prescribed disjoint boundary projections. Section 8 discusses abstract minimizers and Euler equations; the inspected results impose boundary projections rather than the finite trace constraint and do not state this exact full-budget formula. Voiculescu's *Capacity and the quasicentral modulus* (arXiv:2107.11924) supplies the capacity analogy underlying this quantitative problem. The present theorem treats an explicit resource-constrained variational invariant, its unique non-diagonal-class optimizer, and all support transitions. Standard discrete Dirichlet convexity is used in its proof and is not itself claimed as a new principle.

## Limitations

The theorem concerns isometric unilateral shifts of **finite** multiplicity, the Hilbert--Schmidt commutator, positive finite-rank contractions, and the specific wandering-subspace constraint. It does not extend its formula to arbitrary almost normal operators, other Schatten exponents, general weighted shifts, or infinite multiplicity. The asymptotic is for fixed multiplicity \(r\) and budget \(B\to\infty\); no joint high-multiplicity limit is asserted. A general, differently named mass-constrained noncommutative capacity result could subsume this explicit example and remains a bibliographic risk. Published absence is not logically certified by unsuccessful searches. Independent external validation has not been performed.

## References

1. Shiqi Liu and Hongyin Zhao, *Quasicentral modulus for almost normal operators*, arXiv:2611.15604v1 (first public 2026-11-11), https://arxiv.org/html/2611.15604v1.
2. Dan-Virgil Voiculescu, *The condenser quasicentral modulus*, arXiv:2109.07633v7 (2022), https://arxiv.org/pdf/2109.07633, especially Sections 5 and 8.
3. Dan-Virgil Voiculescu, *Capacity and the quasicentral modulus*, arXiv:2107.11924 (2021), https://arxiv.org/abs/2107.11924.
4. AMS, *Mathematics Subject Classification 2020*, class 47L20, https://mathscinet.ams.org/msc/msc2020.html?t=47L20.
