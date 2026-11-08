# Polylogarithmic return-time obstruction for a mixing accumulative backward shift

## Finding

For every \(1<p<\infty\) there is one explicitly specified accumulative backward shift \(B\), with the *same matrix independent of* \(p\), whose successive interval-sum rows have length at most three, such that \(B\) is topologically mixing on \(\ell^p(\mathbb N_0)\) but **no vector is upper frequently hypercyclic**. More strongly, for every \(x\in\ell^p\), every \(\varepsilon>0\) and every \(N\ge1\),

\[
\#\{1\le n\le N: |(B^n x)_1|>\varepsilon\}
\le \varepsilon^{-p}\|x\|_p^p\bigl(\tfrac12\log_2(N+4)\bigr)^{p-1}.
\]

The *same* matrix acting on \(c_0(\mathbb N_0)\) satisfies the Frequent Hypercyclicity Criterion by the established theorem of López-Martínez. Thus a single degree-two symbol gives a sharp qualitative change between the \(c_0\) and \(\ell^p\) dynamics.

A companion classification identifies the full hypercyclic/mixing regime for this family: if \(\varphi:\mathbb N_0\to\mathbb N_0\) is strictly increasing, \(\varphi(0)>0\), and has bounded adjacent gaps, then on \(\ell^p(\mathbb N_0)\), \(1<p<\infty\),

\[
 B_\varphi\text{ is hypercyclic}\quad\Longleftrightarrow\quad
 B_\varphi\text{ is mixing}\quad\Longleftrightarrow\quad
 \varphi^n(j)-\varphi^n(j-1)\longrightarrow\infty
 \quad\text{for every integer }j\ge1.
\]

The known general rooted-tree mixing theory provides important context but does not directly identify the quantitative upper-density obstruction here. The origin has a self-loop in the predecessor diagram of an accumulative shift, so that diagram is not literally the loop-free directed tree of the standard classification.

## Assumptions and scope

All spaces are over \(\mathbb C\); \(\mathbb N_0=\{0,1,2,\ldots\}\). For any strictly increasing map \(\varphi:\mathbb N_0\to\mathbb N_0\) with \(\varphi(0)>0\) and \(D=\sup_{j\ge1}(\varphi(j)-\varphi(j-1))<\infty\), define

\[
 (B_\varphi x)_0=\sum_{k=0}^{\varphi(0)}x_k,
 \qquad (B_\varphi x)_j=\sum_{k=\varphi(j-1)+1}^{\varphi(j)}x_k\quad (j\ge1).
\]

These are disjoint finite rows. Therefore \(B_\varphi\) is bounded on every \(\ell^p\), \(1\le p<\infty\), and \(\|B_\varphi\|=\max\{\varphi(0)+1,D\}^{1-1/p}\). For \(p=1\) the norm equals one and hypercyclicity is impossible.

For the explicit example, for each integer \(t\ge0\), define

\[
 s_t=2^{\lfloor\log_2\log_2(t+4)\rfloor},\qquad
 N_0=0,\qquad N_{t+1}=N_t+s_t.
\]

Let \(J_t=[N_t,N_{t+1}-1]\cap\mathbb N_0\). Since \(s_{t+1}/s_t\in\{1,2\}\), the formula

\[
 \varphi(N_t+u)=N_{t+1}+\frac{s_{t+1}}{s_t}u,
 \qquad 0\le u<s_t,
\]

defines a strictly increasing map of \(\mathbb N_0\) into itself. It satisfies \(\varphi(0)=2\) and \(1\le\varphi(j)-\varphi(j-1)\le2\) for every \(j\ge1\). Hence the resulting shift \(B\) has all rows of size at most three (the root row has three entries); \(\|B\|_{\ell^p\to\ell^p}=3^{1-1/p}\).

"Frequently hypercyclic" means a vector whose visit times to every nonempty open set have positive lower natural density. "Upper frequently hypercyclic" replaces lower by upper density. Thus a set with sublinear counting function precludes both properties.

## Proof

**A. Powers and an exact mixing criterion.** Let \(\varphi^n\) denote iteration, with \(\varphi^0\) the identity. The row sets

\[
 I_{n,0}=\{0,\ldots,\varphi^n(0)\},\qquad
 I_{n,j}=\{\varphi^n(j-1)+1,\ldots,\varphi^n(j)\}\quad(j\ge1)
\]

partition \(\mathbb N_0\). Induction using the disjoint sum formula gives \((B_\varphi^n x)_j=\sum_{k\in I_{n,j}}x_k\). Because \(\varphi\) is strictly increasing and \(\varphi(0)>0\), \(\varphi(k)\ge k+1\) for every \(k\); the left endpoint of \(I_{n,j}\) tends to infinity for each fixed \(j\ge1\). The width \(d_{n,j}=|I_{n,j}|=\varphi^n(j)-\varphi^n(j-1)\) is nondecreasing in \(n\), since a strictly increasing integer map never contracts a positive integer gap.

If some \(d_{n,j}\) fails to diverge, it is bounded by some \(C\), and Hölder's inequality yields, for every \(x\in\ell^p\),

\[
 |(B_\varphi^n x)_j|\le C^{1-1/p}\Big(\sum_{k>\varphi^n(j-1)}|x_k|^p\Big)^{1/p}\longrightarrow0.
\]

No orbit can be dense: an orbit that eventually has arbitrarily small \(j\)-th coordinate cannot visit an open neighborhood of a nonzero \(j\)-th coordinate at arbitrarily large times. This proves necessity.

Conversely suppose all \(d_{n,j}\to\infty\). Set \(X_0=\{x\in c_{00}:\sum_{k\ge0}x_k=0\}\). This set is dense in \(\ell^p\) when \(p>1\): to approximate a standard basis vector, subtract an equal positive average of mass one over \(M\) far-away distinct coordinates; that correction has norm \(M^{1/p-1}\to0\). Finite linear combinations give density. Every \(x\in X_0\) satisfies \(B_\varphi^n x=0\) for all sufficiently large \(n\), because \(I_{n,0}\) eventually contains its entire finite support, with total sum zero.

For \(y\in X_0\) and each \(n\), define \(R_ny\) by putting the constant \(y_j/|I_{n,j}|\) at every coordinate of the block \(I_{n,j}\), for each nonzero coordinate \(j\) of \(y\), and zero elsewhere. Then \(B_\varphi^nR_ny=y\) and

\[
 \|R_ny\|_p^p=\sum_{j\in\operatorname{supp}y}|y_j|^p|I_{n,j}|^{1-p}\longrightarrow0,
\]

because \(|I_{n,0}|=\varphi^n(0)+1\to\infty\) and \(|I_{n,j}|=d_{n,j}\to\infty\) for \(j\ge1\). Given nonempty open sets \(U,V\), choose \(x\in U\cap X_0\) and \(y\in V\cap X_0\). For every sufficiently large \(n\), \(x+R_ny\in U\) while \(B_\varphi^n(x+R_ny)=y\in V\). Thus the operator is topologically mixing; mixing implies hypercyclicity on this separable Banach space.

**B. Exact iterates of the sparse symbol.** As \(t\) grows, \(s_t\) is a nondecreasing sequence of powers of two, unbounded, and \(s_{t+1}/s_t\) equals one or two. The definition of \(\varphi\) preserves the rescaled within-level coordinate. Consequently, for every \(n,t\ge0\) and \(0\le u<s_t\),

\[
 \varphi^n(N_t+u)=N_{t+n}+\frac{s_{t+n}}{s_t}u.
\]

If \(j=N_t+u\), \(1\le u<s_t\), its iterated gap is \(s_{t+n}/s_t\to\infty\). At a level boundary \(j=N_t\), \(t\ge1\), its iterated gap is \(s_{t+n-1}/s_{t-1}\to\infty\). Thus the classification proved in A makes \(B\) mixing on all \(\ell^p\), \(p>1\), and the cited \(c_0\) theorem gives the Frequent Hypercyclicity Criterion there.

**C. Uniform subpolynomial frequency bound.** Because \(s_0=2\), the exact power identity gives for each \(n\ge1\)

\[
 (B^n x)_1=\sum_{k=N_n+1}^{N_n+s_n/2}x_k.
\]

These summation blocks are pairwise disjoint, lying in distinct \(J_n\), and have size \(m_n=s_n/2\). Hölder implies

\[
 |(B^n x)_1|^p\le m_n^{p-1}\sum_{k=N_n+1}^{N_n+m_n}|x_k|^p.
\]

If \(|(B^n x)_1|>\varepsilon\), the corresponding block carries at least \(\varepsilon^p/m_n^{p-1}\) of \(\ell^p\)-mass. Summing over such \(n\in\{1,\ldots,N\}\) and using disjointness gives

\[
 \#\{1\le n\le N: |(B^n x)_1|>\varepsilon\}
 \le\varepsilon^{-p}\|x\|_p^p\max_{1\le n\le N}m_n^{p-1}.
\]

Since \(m_n=s_n/2\le\tfrac12\log_2(n+4)\), this is the claimed polylogarithmic bound. It is \(o(N)\) for every fixed \(p\). In particular, for the nonempty open cylinder \(V_\varepsilon=\{y\in\ell^p:|y_1|>\varepsilon\}\), every orbit has zero upper visit density; no vector can be upper frequently hypercyclic.

## Verification

A standalone `checks.py` contains exact integer/fraction tests of the level recurrence, strictly increasing degree-two symbol, iterative level formula, and disjoint-block right inverses. It ran successfully and reported 6,594 grouped finite assertions, as well as an exhaustive adjacent-step check over the first several hundred level blocks. The infinite assertions are established by the proofs in A–C, *not* by a finite computation.

To reproduce, extract `checks.py` from this package and run `python checks.py` with an ordinary Python 3 interpreter; it uses only the standard library. The symbolic estimates depend on \(1<p<\infty\) and the exact double-logarithmic level law, not on floating-point approximations.

## Relationship to prior work

López-Martínez (2025, revised 2026), Theorem 3.1 and Remark 3.2(e), introduces these interval-summing accumulative shifts, proves the corresponding \(c_0\) Frequent Hypercyclicity Criterion, and explicitly identifies the \(\ell^p\) dynamics as a future problem. His \(c_0\) theorem is used here as a cited input, not claimed as new. The general mixing criterion and especially the explicit slow-level example with a quantitative return-density obstruction are the findings here.

Grosse-Erdmann and Papathanasiou (arXiv:2012.15542, Theorem 4.4) already characterize hypercyclicity/mixing of weighted backward shifts **on loop-free rooted directed trees** by descendant growth. Their theorem is broad prior motivation and overlaps the proof method. The predecessor map underlying \(B_\varphi\), however, maps the index zero to itself; it is not literally the rooted-tree backward shift of that theorem. The present frequency obstruction is also not a conclusion of its mixing characterization. Their 2024 chaotic-tree paper provides an additional general-dynamics framework.

Menet and Papathanasiou (2025) and Karim and Amouch (2026) give broad dynamics of operator-valued shifts on \(\ell^p\)- and \(c_0\)-sums. Only their abstracts were available for this comparison; an abstract does *not* exclude a stronger covering result. Chen, Cheng, Zhang and Zhou (arXiv:2609.21752) study different Cesàro sequence spaces on trees; their abstract highlights related distinctions between return-time notions and frequent hypercyclicity, without addressing the specific logarithmic block mechanism here.

## Limitations

This proves a hypercyclic/mixing classification and one sharp qualitative contrast; it does **not** classify frequent hypercyclicity for every accumulative shift on \(\ell^p\). The polylogarithmic estimate is a universal upper bound on a particular coordinate cylinder, not an optimality assertion about the exponent or a matching lower bound. The original numerical symbol is selected for its slow unbounded block growth; different growth laws can yield different quantitative bounds.

The complete texts of the two operator-valued-shift papers named above were inaccessible; these are real publication-priority risks. No claim of independently certified novelty is made.

## References

1. Antoni López-Martínez, *Frequently hypercyclic composition operators on the little Lipschitz space of a rooted tree*, arXiv:2505.02397, first public May 5, 2025; see Theorem 3.1 and Remark 3.2(e). https://arxiv.org/html/2505.02397
2. Karl-G. Grosse-Erdmann and Dimitris Papathanasiou, *Dynamics of weighted shifts on directed trees*, arXiv:2012.15542, Theorem 4.4, subsequently Indiana Univ. Math. J. 72 (2023). https://arxiv.org/pdf/2012.15542
3. Karl-G. Grosse-Erdmann and Dimitris Papathanasiou, *Chaotic weighted shifts on directed trees*, arXiv:2303.03980 (2023; revised 2024). https://arxiv.org/pdf/2303.03980
4. Quentin Menet and Dimitrios Papathanasiou, *Dynamics of weighted shifts on \(\ell^p\)-sums and \(c_0\)-sums*, Adv. Math. 470 (2025), 110250. https://doi.org/10.1016/j.aim.2025.110250
5. Noureddine Karim and Mohamed Amouch, *Strong dynamics of weighted shifts on \(\ell^p\)-sums and \(c_0\)-sums*, Topology Appl. 391 (2026), 109912. https://doi.org/10.1016/j.topol.2026.109912
6. Xiang Chen, Meng-Huan Cheng, Liang Zhang and Ze-Hua Zhou, *Dynamics of Weighted Backward Shifts on Cesàro Spaces of Rooted Trees*, arXiv:2609.21752 (2026). https://arxiv.org/abs/2609.21752
