# Parity-resolved first-order entropic transition in a matched bipartite Ising model

## Finding

For \(n\ge3\), consider two spin populations \(A\) and \(B\) of size \(n\), coupled antiferromagnetically on each off-diagonal cross edge and ferromagnetically on each designated matched cross edge. The zero-temperature ground-state manifold has a sharp, parity-resolved coupling threshold:

\[
\frac{K_c}{J}=\begin{cases}\frac{n-2}{2n},&n\text{ even},\\[2pt]\frac{(n-1)^2}{2n^2},&n\text{ odd}.\end{cases}
\]

For \(0\le K<K_c\), exactly two ground states exist, with opposite uniform spins across the populations. For \(K>K_c\), all ground states have every matched pair aligned, and the spins within each population are as balanced as parity permits. The exact ground-state degeneracy is

\[
g_n=\begin{cases}\binom{n}{n/2},&n\text{ even},\\2\binom{n}{(n+1)/2},&n\text{ odd}.\end{cases}
\]

At \(K=K_c\), the only minimizers are the union of these sets, so there are \(g_n+2\) ground states. The matched-pair correlation \(Q_n=n^{-1}\sum_i a_ib_i\) jumps exactly from \(-1\) to \(+1\). The limiting zero-temperature entropy per physical spin, with the limit \(n\to\infty\) taken at fixed \(K/J\), is zero for \(K/J<1/2\) and \((\log 2)/2\) for \(K/J\ge1/2\).

## Assumptions and scope

Let \(n\in\mathbb Z\), \(n\ge3\). For each \(i\in\{1,\dots,n\}\), choose \(a_i,b_i\in\{-1,+1\}\), with \(J>0\) and \(K\ge0\). The classical Ising Hamiltonian has zero external field and is

\[
H_n(a,b)=\frac{J}{n}\sum_{1\le i\ne j\le n} a_i b_j-K\sum_{i=1}^n a_i b_i.
\]

The off-diagonal cross interactions have positive coefficient \(J/n\) (antiferromagnetic); the \(n\) matched edges have coefficient \(-K\) (ferromagnetic). No same-population edges exist. Spins are labeled, and symmetry-distinct orientations are counted separately. Write \(r_n=0\) for even \(n\) and \(r_n=1\) for odd \(n\).

## Proof

Set \(M_A=\sum_i a_i\), \(M_B=\sum_i b_i\) and \(t=1+nK/J\). Then

\[
H_n=\frac{J}{n}\left[M_A M_B-t\sum_i a_i b_i\right].
\]

At fixed \(a\), minimization over the independent \(b_i\) yields exactly

\[
\min_b H_n=-\frac{J}{n}\sum_i|M_A-ta_i|.
\]

Put \(p=|M_A|\), with \(p\in\{r_n,r_n+2,\ldots,n\}\). There are \((n+p)/2\) spins in the majority sign of \(a\) and \((n-p)/2\) in the minority sign. Consequently the exact minimum at fixed \(p\) equals

\[
E(p)=\begin{cases}\frac{J}{n}(p^2-nt),&0\le p\le t,\\[2pt]-\frac{J}{n}(n-t)p,&t\le p\le n.\end{cases}
\]

When \(t\ge n\), the first branch covers every admissible \(p\), and its unique minimum occurs at \(p=r_n\). When \(1\le t<n\), the first branch strictly increases with the nonnegative \(p\), and the second strictly decreases. Every global minimizing \(p\) must therefore be either \(r_n\) or \(n\). Their energies are

\[
E_{\rm bal}=\frac{Jr_n^2}{n}-J-Kn,
\qquad E_{\rm AF}=-J(n-1)+Kn.
\]

Comparing these gives \(K_c/J=(n-2+r_n^2/n)/(2n)\), precisely the stated parity-dependent threshold. For \(K\ge K_c\), one has \(t>r_n\), so the \(b\)-minimizers at \(p=r_n\) are uniquely \(b_i=a_i\). For \(0\le K\le K_c\), one has \(t<n\), so the \(b\)-minimizers at \(p=n\) are uniquely \(b_i=-a_i\). There are no intervening minima or additional degeneracies at the crossing. Counting all balanced labeled \(a\) configurations gives \(g_n\); the two uniform antialigned configurations give the other two states.

Finally \(g_n=2^n n^{-1/2+o(1)}\) up to a positive constant by Stirling's formula. Hence \((\log g_n)/(2n)\to(\log2)/2\), whereas \((\log 2)/(2n)\to0\). Since the finite-size critical threshold satisfies \(K_c/J\to1/2\) from below, the claimed entropy and pair-correlation limits follow, including the equality \(K/J=1/2\).

## Verification

Run `python verify_landscape.py` using Python's standard library. It exhaustively compares energy and the **complete minimizing spin sets** over \(3\le n\le8\) at 36 rational parameter selections including the critical values, and independently enumerates exact four-type pair-populations for \(9\le n\le60\) at 208 rational selections. These finite checks test the proof; the argument above supplies the all-size result.

## Relationship to prior work

Vieira and Gonçalves study a closed one-dimensional Ising chain with random nearest-neighbor couplings and a uniform all-spin infinite-range interaction. Their explicit Hamiltonian in section 2 is different from this deterministic bipartite cross interaction with a matched ferromagnetic perturbation; neither its chain parameters nor its phase descriptions directly imply the finite \(n\) parity threshold and all labeled minimizers here. Grousson, Tarjus and Viot consider spatial long-range Coulombic antiferromagnetic frustration with nearest-neighbor ferromagnetism on a different lattice, identifying modulated phases rather than this matched bipartite counting problem. These works motivate examining how sparse ferromagnetic bonds compete with extensive frustrated interactions. Related general mean-field techniques are known; no novelty is claimed for fixing one population and minimizing the other one spin at a time.

## Limitations

Only strictly positive \(J\), nonnegative \(K\), equal population sizes, a perfect matched pairing, zero field, and zero-temperature ground states are treated. Finite-temperature phase structure, robustness to perturbations, and dynamical relaxation are unproved. Priority against all historical equivalent formulations is not conclusively established, especially inaccessible studies of two-subpopulation Ising models. The transition's thermodynamic statement takes fixed \(K/J\) before \(n\to\infty\).

## References

- A. P. Vieira and L. L. Gonçalves, *One-dimensional Ising model with long-range and random short-range interactions*, arXiv:cond-mat/9809050 (first public 1998-09-02). https://arxiv.org/abs/cond-mat/9809050
- M. Grousson, G. Tarjus and P. Viot, *Phase diagram of an Ising model with long-range frustrating interactions: a theoretical analysis*, arXiv:cond-mat/0006262 (first public 2000-06-16). https://arxiv.org/abs/cond-mat/0006262
