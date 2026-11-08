# Effective high-multiplicity symmetry for even arithmetic triples and the exact \(6,7,8\) spectrum

## Finding
Let \(a\ge4\) be even, \(d\ge1\) with \(\gcd(a,d)=1\), and let \(S_p\) consist of the integers admitting strictly more than \(p\) representations by the three positive integers \(a,a+d,a+2d\), where \(p\ge0\). Put \(u=a/2\), \(v=u+d\), \(w=u+v=a+d\), and let \(h(t)\) count nonnegative solutions of \(ux+vy+wz=t\) (zero for negative \(t\)). Define
\[
M=uvw,\qquad \delta=\min_{0\le r<M}\bigl(h(r+1)-h(r)\bigr),\quad T_0=M\max(0,1-\delta),\quad P=\max_{0\le t<T_0}h(t),
\]
with \(P=0\) if the final range is empty. These are finite, explicitly computable integers. Then for **every** \(p\ge P\), and \(E_p=\min\{t\ge0:h(t)>p\}\),
\[
S_p=\{2t:t\ge E_p\}\;\cup\;\{2t+w:t\ge E_p\}.
\]
Consequently \(S_p\) is \(p\)-symmetric and its multiplicity, generalized Frobenius number, and number of gaps satisfy
\[
\ell_p=2E_p,\qquad g_p=2E_p+w-2,\qquad n_p=2E_p+\frac{w-1}{2}.
\]
For the first case beyond the smallest even triple, \((a,d)=(6,1)\), **all levels are classified**: \(S_p(6,7,8)\) is \(p\)-symmetric exactly when \(p=0\) or \(p\ge2\). Its displayed two-tail form is valid exactly for \(p=2,3,4,5,6\) or \(p\ge8\); the isolated level \(p=7\) remains symmetric but has a different gap shape.

## Assumptions and scope
All generators and representation coefficients are nonnegative integers, with generators positive. The strict inequality is \(d_A(N)>p\); in particular \(0\notin S_p\) for \(p\ge1\). The \(p\)-gaps are \(G_p=\mathbb N_0\setminus S_p\), their maximum is \(g_p\), and \(\ell_p\) is the minimum of \(S_p\). Symmetry means the reflection \(x\mapsto \ell_p+g_p-x\) sends every integer not in \(S_p\) into \(S_p\), equivalently exactly one of each reflected pair in \([\ell_p,g_p]\) lies in \(S_p\). The hypotheses imply \(u,v,w\) are pairwise coprime and \(w\) is odd. No claim is made for odd initial generator \(a\).

## Proof
**Parity splitting.** Every representation of even \(2t\) has an even coefficient of odd generator \(w\). Halving all even contributions gives a bijection with the solutions counted by \(h(t)\). Every representation of odd \(2t+w\) has an odd coefficient of \(w\), giving the same bijection after subtracting one \(w\). Therefore
\[
d_A(2t)=h(t),\qquad d_A(2t+w)=h(t)\quad(t\ge0),
\]
and odd arguments below \(w\) have no representations. These two progressions partition \(\mathbb N_0\) into even and odd arguments (the odd part is indexed by \(t\ge0\) only when the argument is at least \(w\)).

**Exact quasipolynomial shift.** The generating series of \(h(t)\) is \(\bigl((1-z^u)(1-z^v)(1-z^w)\bigr)^{-1}\). Pairwise coprimality makes every pole at a nontrivial root of unity simple; its coefficient contribution is periodic with period dividing \(M\). Expansion of the order-three pole at \(z=1\) shows that the nonperiodic coefficient polynomial is \(t^2/(2M)+wt/M+\mathrm{constant}\). Hence, for each \(0\le r<M\) and \(q\ge0\),
\[
h(r+qM)=h(r)+\frac{M q^2}{2}+(r+w)q,
\qquad
h(r+qM+1)-h(r+qM)=h(r+1)-h(r)+q.
\]
The latter identity also holds for \(r=M-1\), using the shift formula at the next period. Since \(M\) is even, every displayed integer is integral. By the definitions of \(\delta,T_0\), \(h(t+1)>h(t)\) for all \(t\ge T_0\). Also \(h(t)\to\infty\).

**Uniform effective threshold.** For any \(p\ge P\), no \(t<T_0\) has \(h(t)>p\); monotonicity thereafter gives \(h(t)>p\) if and only if \(t\ge E_p\). The parity splitting gives the two-tail description. The gaps are exactly the even integers below \(2E_p\) and the odd integers below \(2E_p+w\). Hence the formulas for \(\ell_p,g_p,n_p\). In the interval \([\ell_p,g_p]\) exactly the even numbers are in \(S_p\), while \(\ell_p+g_p\) is odd; reflection exchanges the even elements and the odd gaps. For \(x<\ell_p\) the reflected element exceeds \(g_p\) and belongs to \(S_p\); thus full \(p\)-symmetry follows.

**Sharp all-level instance.** For \(u=3,v=4,w=7\), the finite coefficient recurrence for \(h\) gives \(M=84\), \(\delta=-1\), \(T_0=168\), and \(P=180\). Exact finite enumeration of all integer levels \(0\le p\le180\), checking each reflected pair and each possible crossing of the threshold before \(T_0\), gives precisely \(\{1\}\) as the nonsymmetric levels and \(\{0,1,7\}\) as the levels failing the two-tail form; the complete executable enumeration is in `verify.py`. At \(p=1\), \(\ell_1=14\), \(g_1=25\), and both \(16\) and \(23\) are gaps, disproving symmetry. At \(p=7\), \(\ell_7=56\), \(g_7=65\), with exactly \(56,60,62,63,64\) inside \(S_7\) between these endpoints; their reflected complements are precisely the other five positions. At \(p=0\), \(\ell_0=0\), \(g_0=17\), with the nine represented elements in the interval \(0,6,7,8,12,13,14,15,16\), reflected against the nine gaps. For \(p\ge181\) the general theorem applies; \(p=180\) is included in the finite check. This proves the complete classification.

## Verification
Run `python3 verify.py`. It computes all denumerants by exact integer dynamic programming, checks the period-shift identity through four periods for six parameter pairs, independently verifies direct \((6,7,8)\) representation counts against parity splitting, tests all \(181\) finite levels against exact reflection and two-tail predicates, and confirms \(M=84,\delta=-1,T_0=168,P=180\). The infinite range rests on the analytic coefficient proof above; computation only certifies the explicitly finite residue and level ranges.

## Relationship to prior work
Komatsu and Ying (2022, 2023 journal version) calculate generalized Frobenius and related quantities for three-term arithmetic progressions through \(p\le\lfloor a/2\rfloor\) and explicitly identify the larger-level case as difficult. Their separate 2022 paper introduces \(p\)-symmetry and proves it for even triples at \(p=a/2-1\). Komatsu (2024) proves a \(p\)-Watanabe equivalence for certain odd-generator gluing operations; the parity reduction here is compatible with it, and **the reduction/gluing mechanism is not claimed as independently novel**. The additional result is an effective entire high-level tail formula and a sharp classification of every level for the natural \((6,7,8)\) case, including the nonmonotone but symmetric exceptional level. General rational-generating-function quasipolynomial facts are likewise standard ingredients.

## Limitations
Originality is assessed against the inspected primary texts and searched mathematical records; implicit appearances of this exact high-level formula or exceptional spectrum in unindexed literature cannot be excluded. The computable bound \(P\) is sufficient and generally not minimal. The exact \((6,7,8)\) levels rely on fully enumerated finite certificates plus an infinite analytic argument, rather than finite extrapolation. Independent validation has not been performed.

## References
Komatsu, T., and Ying, H., *The p-numerical semigroup of the triple of arithmetic progressions*, first preprint 2022-06-27, arXiv:2206.13052, https://arxiv.org/abs/2206.13052.

Komatsu, T., and Ying, H., *p-numerical semigroups with p-symmetric properties*, first preprint 2022-07-18, arXiv:2207.08962, https://arxiv.org/abs/2207.08962.

Komatsu, T., *p-numerical semigroups with p-symmetric properties, II*, first preprint 2024-09-04, arXiv:2409.02394, https://arxiv.org/abs/2409.02394.
