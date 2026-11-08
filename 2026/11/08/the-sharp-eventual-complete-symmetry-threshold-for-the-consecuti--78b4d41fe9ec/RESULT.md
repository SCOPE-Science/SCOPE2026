# The sharp eventual complete-symmetry threshold for the consecutive triple 17, 18, 19

## Finding
For each integer \(p\ge0\), let \(r(n)\) count the nonnegative integer triples \((x,y,z)\) satisfying \(17x+18y+19z=n\), and define \(S_p=\{n\in\mathbb Z_{\ge0}:r(n)>p\}\). Write \(\ell_p=\min S_p\) and \(g_p=\max(\mathbb Z_{\ge0}\setminus S_p)\). Then **the least integer \(P\) such that every \(S_p\) with \(p\ge P\) is \(p\)-completely symmetric is exactly \(P=505\)**. Equivalently, for every integer \(p\ge505\), \(S_p=\{n\in\mathbb Z_{\ge0}:n\ge\ell_p\}\); at \(p=504\), this property fails.

The decisive boundary is the exact representation-count drop
\[
 r(2394)=505,\qquad r(2395)=504.
\]

## Assumptions and scope
Representations are **ordered by the named generators**, with \(x,y,z\) nonnegative integers, and the three coefficients are fixed as \(17,18,19\). Here \(p\) ranges over *all* nonnegative integers. Following the standard definition, \(S_p\) is \(p\)-symmetric if each integer \(t\notin S_p\) has \(\ell_p+g_p-t\in S_p\), and is \(p\)-completely symmetric if also \(\ell_p=g_p+1\). The latter condition is equivalent to \(S_p\) being a consecutive final segment of the nonnegative integers. The claim determines the least universal cutoff for this stronger property, **not** the complete set of isolated smaller levels that might happen to satisfy it.

## Proof
Set \(L=17\cdot18\cdot19=5814\), \(R(X)=\sum_{n\ge0}r(n)X^n\), and
\[
 B(X)=(1-X^{17})(1-X^{18})(1-X^{19}).
\]
Then \(R(X)=1/B(X)\). Define \(d(n)=r(n+1)-r(n)\); since \(r(0)=1\), its generating function is
\[
 D(X)=\sum_{n\ge0}d(n)X^n=\frac{(1-X)-B(X)}{XB(X)}.
\]
Let \(Q(X)=\sum_{j=0}^{L-1}d(j)X^j\), with the first-period coefficients generated exactly from \(R(X)\). The following finite polynomial identity holds coefficient-by-coefficient over the integers:
\[
 (1-X)(1-X^L)((1-X)-B(X))
 =XB(X)((1-X)Q(X)+X^L).
\]
The accompanying self-contained certificate rebuilds \(B,Q\) and checks all coefficients of this equality, rather than assuming a numerical extrapolation. Dividing in the ring of rational formal power series yields
\[
 (1-X^L)D(X)=Q(X)+\frac{X^L}{1-X},
\]
and hence, for **every** integer \(n\ge0\),
\[
 \boxed{d(n+5814)=d(n)+1.}
\]

The finite first-period calculation gives \(\min_{0\le n<5814}d(n)=-1\), with exactly \(120\) negative positions and no difference below \(-1\). Consequently all \(d(n)\) for \(n\ge5814\) are nonnegative, and **every** downward step in the entire infinite denumerant sequence lies in the first period. Among those \(120\) certified downward steps, the maximum preceding representation count is
\[
 \max_{\substack{0\le n<5814\\d(n)<0}}r(n)=505,
\]
attained at \(n=2394\), where \(d(2394)=-1\). These numerical assertions are complete finite exact computations; the finite domain and independent coefficient-building algorithm are specified in the verifier.

Now fix \(p\ge505\). Suppose \(r(n)>p\) and let \(m\ge n\) be the first index at which the sequence would drop from a value greater than \(p\) to a value at most \(p\). Such an index would require \(d(m)<0\) with \(r(m)>p\ge505\), contradicting the certified all-index bound that each decrease starts at \(r(m)\le505\). Thus once \(r(n)>p\), the inequality holds at every later index; since \(r(n)\) grows without bound, \(S_p\) is a consecutive final segment. Therefore \(\ell_p=g_p+1\), proving complete symmetry for all \(p\ge505\).

At \(p=504\), the certified pair \(r(2394)=505>504\) and \(r(2395)=504\le504\) exhibits an included integer immediately followed by an excluded integer. Accordingly \(S_{504}\) is not a final segment, so no smaller universal cutoff works.

## Verification
Execute `python3 verify.py` using only Python's standard library. It independently direct-enumerates \(103\) coefficient instances, reconstructs the first \(5814\) representation coefficients and the difference polynomial, checks the exact integer polynomial identity (residual length \(5870\), identically zero), checks the complete list of \(120\) negative differences and their preceding counts, and independently reproduces the boundary counts. Output is recorded in `CERTIFICATE.txt`. A finite scan alone is not claimed as a proof of eventual behavior: the polynomial identity supplies the necessary infinite step.

## Relationship to prior work
Komatsu and Ying, *The p-numerical semigroup of the triple of arithmetic progressions* (arXiv:2206.13052, first posted 27 June 2022), obtain generalized Frobenius formulas for three-term progressions at bounded representation levels \(p\le\lfloor a/2\rfloor\) and identify the larger-level regime as a question. Komatsu and Ying, *p-numerical semigroups with p-symmetric properties* (arXiv:2207.08962, first posted 18 July 2022), define the symmetry notions and prove several low-level structural statements, not this sharp threshold. Komatsu, *p-numerical semigroups with p-symmetric properties, II* (arXiv:2409.02394, first posted 4 September 2024), explicitly uses the same triple \((17,18,19)\) to illustrate irregular early \(p\)-symmetry and complete symmetry, listing small values but not a universal all-high-level cutoff. The polynomial counting approach is elementary; the asserted contribution is the **specific sharp all-level cutoff** for this published test case, not a general claim that denumerants eventually become monotone.

## Limitations
This is not a classification of every lower \(p\)-level, and it is not a general formula for all consecutive triples. The finite certificate relies on exact integer computations; its completeness follows from the proved period-shift identity. The available literature and index searches cannot exclude every unindexed equivalent result. Independent external validation has not been performed.

## References
1. T. Komatsu and H. Ying, *The p-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052 (2022), https://arxiv.org/abs/2206.13052.
2. T. Komatsu and H. Ying, *p-numerical semigroups with p-symmetric properties*, arXiv:2207.08962 (2022), https://arxiv.org/abs/2207.08962.
3. T. Komatsu, *p-numerical semigroups with p-symmetric properties, II*, arXiv:2409.02394 (2024), https://arxiv.org/abs/2409.02394.
