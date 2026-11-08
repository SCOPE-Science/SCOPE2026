# Arbitrarily long fifth-power factoradic runs for two nontrivial attractors

## Finding

Let \(S_{5,!}(n)\) be the sum of fifth powers of the factorial-base digits of a nonnegative integer, with \(S_{5,!}(0)=0\). For each \(p\in\{34,1058\}\) and each positive integer \(m\), **there is an integer \(N\ge1\) such that all \(m\) consecutive integers \(N+1,\ldots,N+m\) eventually iterate to \(p\) under \(S_{5,!}\)**. Equivalently, there exist \(r_1,\ldots,r_m\ge0\) with

\[
S_{5,!}^{r_i}(N+i)=p\qquad(1\le i\le m).
\]

Both \(34\) and \(1058\) are fixed points of \(S_{5,!}\). The statement concerns their individual basins, *not* the standard \(1\)-happy basin; no assertion about arbitrarily long fifth-power factoradic \(1\)-happy runs is made.

## Assumptions and scope

Every integer \(n\ge0\) has a unique factorial expansion \(n=\sum_{j\ge1}a_jj!\) with \(0\le a_j\le j\) and finitely many nonzero digits. Define

\[
S_{5,!}(n)=\sum_{j\ge1}a_j^5.
\]

Let \(U\) be the set of positive periodic points of this map (fixed points and members of nontrivial cycles). The key finite set is

\[
U=\{1,34,35,308,309,1058,1059,2114,3401\}.
\]

Here \(2114\mapsto3401\mapsto2114\) is the unique nontrivial positive cycle. The other seven elements are fixed. The result is unconditional for the displayed exponent and two targets, but does not classify all target basins or their densities.

## Proof

**1. Reduction to an exact finite dynamical system.** For every digit \(0\le a\le j\),

\[
a j!-a^5=a(j!-a^4).
\]

For \(j=1,\ldots,6\), the minimum contributions over allowed digits are respectively \(0,-28,-225,-928,-2525,-3456\), whose sum is \(-7162\). For every \(j\ge7\), the contribution is nonnegative. If \(n\ge8!\), its top nonzero digit has index \(k\ge8\), and the corresponding contribution is at least \(k!-k^4\ge8!-8^4=36224\). Thus

\[
n-S_{5,!}(n)\ge 36224-7162>0\quad(n\ge40320).
\]

For \(1\le n<40320\), its digit positions have indices at most \(7\); hence

\[
1\le S_{5,!}(n)\le\sum_{j=1}^{7}j^5=29008<40320.
\]

It follows that every positive orbit eventually enters the invariant interval \([1,40319]\). A complete *finite* examination of all its \(40319\) states under the explicitly defined map gives the seven singleton cycles

\[
(1),(34),(35),(308),(309),(1058),(1059)
\]

and the two-cycle \((2114,3401)\), with no further cycles. This enumeration is reproduced from first principles by both standalone exact-integer programs `verify.py` and `verify_greedy.py`. Their methods of extracting factorial digits differ; the finite check is exhaustive rather than a sampled experiment.

**2. Two synchronization certificates.** Put \(\lambda_{34}=1373\) and \(\lambda_{1058}=75004\). Direct fifth-power factoradic iteration establishes

\[
\begin{aligned}
&\forall u\in U,\ \exists q_u\ge0:\quad S_{5,!}^{q_u}(1373+u)=34,\\
&\forall u\in U,\ \exists s_u\ge0:\quad S_{5,!}^{s_u}(75004+u)=1058.
\end{aligned}
\]

These are \(18\) explicit finite paths, given without omission in `witnesses.txt` and checked term-by-term by `verify.py`. The longest recorded paths have lengths \(17\) and \(7\), respectively. In particular, the two nontrivial cyclic points are included among the inputs; checking only the fixed points would not suffice.

**3. A lifting lemma.** Define the digit-shift map

\[
f_t\left(\sum_{j\ge1}a_jj!\right)=\sum_{j\ge1}a_j(j+t)!.
\]

If the factorial digits of \(y\) use only positions up to \(t\), then the digits of \(f_t(x)+y\) are disjoint, so

\[
S_{5,!}(f_t(x)+y)=S_{5,!}(x)+S_{5,!}(y).
\]

Moreover, \(S_{5,!}\) is surjective on the nonnegative integers: for each \(c\ge1\), the integer \(\sum_{j=1}^{c}j!\) has digit-power sum exactly \(c\); the input \(0\) maps to \(0\).

Fix \(m\ge1\) and one target \(p\). Because every positive orbit eventually enters \(U\), choose \(r\ge1\) such that \(S_{5,!}^{r}(i)\in U\) for all \(1\le i\le m\). Choose \(t\) larger than every factorial-digit position appearing in any \(S_{5,!}^{j}(i)\), for \(1\le i\le m\) and \(0\le j<r\). Take \(\lambda=1373\) when \(p=34\), and \(\lambda=75004\) when \(p=1058\).

Set \(L_r=\lambda\). Recursively for \(j=r-1,r-2,\ldots,0\), choose a nonnegative \(v_j\) with \(S_{5,!}(v_j)=L_{j+1}\), and set \(L_j=f_t(v_j)\). By repeated application of the disjoint-digit identity,

\[
S_{5,!}^{r}(L_0+i)=\lambda+S_{5,!}^{r}(i)\qquad(1\le i\le m).
\]

The right-hand side belongs to \(\lambda+U\). The synchronization certificate in Step 2 sends every such value to \(p\), after a possibly different additional number of iterations. Thus all \(L_0+1,\ldots,L_0+m\) reach \(p\). Since \(\lambda>0\), the construction gives \(L_0>0\), which completes the proof.

## Verification

Run `python3 verify.py` and `python3 verify_greedy.py` from the directory containing the supplied files. Both use only the Python standard library, exact integer arithmetic, and explicit loop bounds. The first enumerates the entire finite recurrent state graph and checks every transition of the \(18\) synchronization paths; the second uses an independent greedy factorial expansion to enumerate the same recurrent state graph and test both certificates. Their expected concluding lines are `verification=PASS` and `independent_greedy_check=PASS`.

The programs explicitly check all \(40319\) positive states below \(8!\). An infinite search is not performed and is not needed: Step 1 establishes the reduction of arbitrary positive orbits to these states, while Step 3 proves the infinite-length consequence.

## Relationship to prior work

Carlson, Goedhart, and Harris (2019/2020) introduced this map, computed its periodic points through exponent six, and proved a general **conditional** lifting theorem: if the periodic set is absolute and possesses a common translation into one fixed point's basin, then arbitrarily long consecutive runs reaching that fixed point exist. They established the required condition for exponents \(1\) through \(4\), but did not provide it for exponent \(5\), where nontrivial cycles first appear. Our contribution is the two explicit translations, their complete verification for *all* periodic states, and the resulting unconditional theorem for the two named targets; the general lifting principle and the pre-existing periodic-point table are not claimed as new.

Sánchez Garza and Treviño (2021) extend the general eventual-decrease bound to arbitrary exponents; this does not supply a synchronization translation or a consecutive-run result for exponent five. Goedhart, Gurtas, and Harris (2025, preprint 2024) study preimage trees for fixed positional bases, a distinct digit system. A 2022 survey describes related happy-function literature but its full text was not available for line-by-line comparison.

## Limitations

This is a theorem about the basins of \(34\) and \(1058\), not the basin of \(1\). It neither establishes natural or logarithmic densities nor gives optimal smallest starts of intervals. The infinite conclusion rests on the given symbolic lifting lemma; the finite enumeration supplies exactly the list of periodic states and synchronization certificates required by that lemma. A previously unindexed equivalent result remains a possible priority risk.

## References

1. J. Carlson, E. G. Goedhart, P. E. Harris, *Sequences of consecutive factoradic happy numbers*, arXiv:1912.02044v1, first posted 4 December 2019; Rocky Mountain Journal of Mathematics 50 (2020), 1241–1252. https://arxiv.org/abs/1912.02044
2. M. Sánchez Garza, E. Treviño, *On a Sequence Related to the Factoradic Representation of an Integer*, Journal of Integer Sequences 24 (2021), Article 21.8.5. https://campus.lakeforest.edu/trevino/SequenceFactoradic.pdf
3. E. G. Goedhart, Y. Gurtas, P. E. Harris, *A Tree Approach to the Happy Function*, arXiv:2410.13990; La Matematica 4 (2025), 419–432. https://doi.org/10.1007/s44007-025-00157-x
4. H. G. Grundman, L. L. Hall-Seelig, *Happy Numbers, Happy Functions, and Their Variations: A Survey*, La Matematica 1 (2022), 404–430. https://doi.org/10.1007/s44007-021-00010-x
