# A complete cubic census of 3-Abelian observations of Dyck words

## Finding

Let \(\mathcal D_m\) denote the binary Dyck words of semilength \(m\geq1\), with `1` an up-step and `0` a down-step. A *3-Abelian observation* is the vector of occurrences, with overlaps, of **every** contiguous binary factor of lengths one, two, and three. Let \(P_m\) count distinct observations obtained from \(\mathcal D_m\). Then

\[
\boxed{P_m=\frac{m(m^2-3m+5)}{3}\qquad(m\geq1).}
\]

In particular,
\[
\sum_{m\geq1}P_m z^m=\frac{z(1-2z+3z^2)}{(1-z)^4},
\]
with initial terms \(1,2,5,12,25,46,77,120,177,250,341,452\). Every feasible observation has a constructible Dyck-word representative, and the following theorem characterizes **all** feasible observations without any search over Dyck words.

## Assumptions and scope

A Dyck word \(w=w_1\cdots w_{2m}\) has exactly \(m\) occurrences of each bit and every prefix has at least as many ones as zeros. The observation records ordinary **linear**, overlapping factor counts, without wraparound. It is not a scattered-subsequence spectrum or a vector of occurrence positions. Equivalence means equality of all fourteen counts for the two one-letter, four two-letter and eight three-letter factors. The theorem concerns attainable observations and hence the maximum one-representative-per-profile zero-error code size for that observation rule; it does **not** determine all equivalence-class cardinalities.

Every nonempty Dyck word has a unique alternating-run decomposition
\[
w=1^{a_1}0^{b_1}\cdots1^{a_p}0^{b_p},\qquad
 a_i,b_i\geq1,\quad\sum_i a_i=\sum_i b_i=m.
\]
Put \(p\) equal to the number of up-runs (equivalently, peaks), \(u=|\{i:a_i=1\}|\), \(v=|\{i:b_i=1\}|\), \(\alpha=[a_1=1]\), and \(\beta=[b_p=1]\), where brackets denote an indicator. Thus \(\alpha,\beta\in\{0,1\}\).

**Feasibility theorem.** For \(p=m\), the unique parameter tuple is \((p,u,v,\alpha,\beta)=(m,m,m,1,1)\). For \(1\leq p<m\), a parameter tuple occurs for a Dyck word if and only if
\[
\alpha,\beta\in\{0,1\},\qquad
\max(0,2p-m,\alpha+\beta)\leq u,v\leq p-1.
\]
Every tuple in this statement gives a **different** 3-Abelian observation, and every observation occurs in precisely one of these tuples.

## Proof

**1. Recover the run parameters from the observed factors.** Write \(c_{abc}\) for the occurrence count of the triple `abc`. Counting within and across alternating runs gives
\[
\begin{aligned}
c_{111}&=m-2p+u,&c_{000}&=m-2p+v,\\
c_{110}&=p-u,&c_{100}&=p-v,\\
c_{011}&=p-1-u+\alpha,&c_{001}&=p-1-v+\beta,\\
c_{010}&=u-\alpha,&c_{101}&=v-\beta.
\end{aligned}
\]
These identities remain valid at \(m=1\), when all triple counts vanish. Conversely they yield
\[
p=m-c_{110}-c_{111},\qquad
u=p-c_{110},\qquad v=p-c_{100},\qquad
\alpha=u-c_{010},\qquad\beta=v-c_{101}.
\]
The one-letter counts are both \(m\); the two-letter counts are \(c_{10}=p\), \(c_{01}=p-1\), and \(c_{00}=c_{11}=m-p\). Consequently the complete observation and the five parameters determine one another.

**2. Necessary constraints.** When \(p<m\), at least one up-run and one down-run have length greater than one, giving \(u,v\leq p-1\). A positive composition of \(m\) into \(p\) parts with \(u\) singleton parts requires \(m\geq u+2(p-u)=2p-u\), whence \(u\geq2p-m\), and likewise for \(v\). A Dyck word whose first up-run has length one must begin with `10`; a Dyck word whose last down-run has length one must end with `10`. These forced boundary blocks are distinct when \(p<m\), so \(u,v\geq\alpha+\beta\). All other constraints are the binary indicator conditions. If \(p=m\), the only word is \((10)^m\).

**3. Construct every feasible tuple.** Let \(t=\alpha+\beta\), delete the forced initial `10` if \(\alpha=1\) and the forced final `10` if \(\beta=1\), and seek an interior Dyck word with semilength \(M=m-t\), \(r=p-t\) peaks, and \(u-t\), \(v-t\) singleton up- and down-runs. The inequalities above ensure \(r\geq1\) and both positive compositions exist. Choose the \(r\) up-run lengths as a weakly **decreasing** positive composition of \(M\) with exactly \(u-t\) parts equal to one. Independently choose the \(r\) down-run lengths as a weakly **increasing** positive composition of \(M\) with exactly \(v-t\) parts equal to one. One explicit choice allocates all excess above two to the first nonsingleton up-run, respectively the final nonsingleton down-run.

For every \(1\leq j\leq r\), the first \(j\) entries of a decreasing sequence with average \(M/r\) sum to at least \(jM/r\), while the first \(j\) entries of an increasing sequence with the same average sum to at most \(jM/r\). Therefore
\[
\sum_{i=1}^j a_i\geq\sum_{i=1}^j b_i
\]
for each completed down-run. All intermediate prefixes within an up-run increase, and those within a down-run decrease, so this is a Dyck word. The unforced first up-run and last down-run are nonsingleton when their corresponding boundary flags are zero, because \(u,v\leq p-1\). Appending the forced boundary `10` blocks realizes exactly the prescribed tuple. This proves both sufficiency and constructive feasibility.

**4. Count tuples.** For each \(1\leq p<m\), the numbers of options for each of \(u,v\), according to \((\alpha,\beta)=(0,0),(1,0)\text{ or }(0,1),(1,1)\), respectively, are
\[
f_p=\min(p,m-p),\qquad
g_p=\min(p-1,m-p),\qquad
h_p=\max(0,\min(p-2,m-p)).
\]
Hence, including the unique \(p=m\) profile,
\[
P_m=1+\sum_{p=1}^{m-1}(f_p^2+2g_p^2+h_p^2).
\]
Splitting the three finite sums at their crossover near \(m/2\) and evaluating \(\sum_{j=1}^q j^2=q(q+1)(2q+1)/6\) yields
\[
P_{2q}=\frac{2q(4q^2-6q+5)}3,\qquad
P_{2q+1}=\frac{(2q+1)(4q^2-2q+3)}3.
\]
Both are the asserted cubic. Standard generating functions for \(\sum m z^m\), \(\sum m^2 z^m\), and \(\sum m^3 z^m\) give the displayed rational series. As any error-free code under a deterministic observation contains at most one word of each profile, and the construction supplies one word per profile, its maximal size is \(P_m\). This completes the proof.

## Verification

Two self-contained Python 3 standard-library scripts accompany this statement. `check_enumeration.py` enumerates every Dyck word of semilength \(1\) through \(11\), computes all fourteen factor counts directly, verifies the run-parameter bijection and feasibility support, and checks the cubic count. `check_constructive.py` independently builds one word for each asserted feasible tuple through semilength \(22\), verifies the Dyck prefix property, recovered tuple, pairwise distinct complete profiles, and the polynomial. Run with:

```
python3 check_enumeration.py
python3 check_constructive.py
```

Both programs passed on the packaged source. These finite checks test the proof and are not offered as substitutes for the all-length arguments in Steps 1–4.

## Relationship to prior work

Karhumäki–Saarela–Zamboni (2013) introduce \(k\)-Abelian equivalence and prove general growth statements. Karhumäki–Puzynina–Rao–Whiteland (2016) study sizes of unrestricted \(k\)-Abelian classes. Neither inspected text yields the exact joint triple-profile support of the Dyck language. Manes–Sapounakis–Tasoulas–Tsikouras (2015) study Dyck and ballot paths equivalenced by **positions** of occurrences of a fixed pattern; their single-pattern position equivalences do not imply the complete simultaneous histogram classification proved here. An unrestricted binary linear-triple-profile enumeration has quartic growth and does not characterize the Dyck-restricted subset.

The **numerical sequence** and **rational generating function** above are not numerically new: OEIS A116731 has the same cubic sequence, first listed for permutation-avoidance classes on 2006-02-26 (the explicit cubic formula was added on 2006-09-13). The claim here is a distinct constructive characterization of all realizable Dyck 3-Abelian profiles and its exact reconstruction-capacity interpretation, not priority for those numbers alone.

## Limitations

This result concerns nonempty Dyck words at every semilength and complete linear overlapping observations of lengths at most three. It does not classify sizes of the inverse-image fibers, noisy observations, height-constrained Dyck words, longer factor profiles, or nonlinear cyclic readings. The search did not locate an exact previous Dyck 3-Abelian version; absence from those sources is not proof that no earlier equivalent interpretation exists. No independent mathematical audit has been performed.

## References

1. J. Karhumäki, A. Saarela and L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104 (first public 2013-01-22), https://arxiv.org/abs/1301.5104.
2. K. Manes, A. Sapounakis, I. Tasoulas and P. Tsikouras, *Equivalence classes of ballot paths modulo strings of length 2 and 3*, arXiv:1510.01952 (first public 2015-10-07), https://arxiv.org/abs/1510.01952.
3. J. Karhumäki, S. Puzynina, M. A. Rao and M. Whiteland, *On cardinalities of k-Abelian equivalence classes*, arXiv:1605.03319 (first public 2016-05-11), https://arxiv.org/abs/1605.03319.
4. OEIS Foundation, *A116731*, https://oeis.org/A116731 (same polynomial sequence, with a different combinatorial interpretation).
5. K. Manes, A. Sapounakis, I. Tasoulas and P. Tsikouras, *General results on the enumeration of strings in Dyck paths*, Electronic Journal of Combinatorics 18 (2011), Paper P74, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v18i1p74 (abstract and public description checked, not full text).
