# The twist-dependent transient clock on cubic circular ladders

## Finding
Let \(n\ge3\) and let \(Q\) be any power of two. On each of the two cubic graphs with \(2n\) vertices—the ordinary circular ladder \(P_n=C_n\square K_2\) and the Möbius ladder \(M_n\), obtained from a \(2n\)-cycle by adding opposite-vertex chords—consider the synchronous neighbor-sum automaton \(B_G:\mathbb F_Q^{2n}\to\mathbb F_Q^{2n}\),
\[
(B_Gu)(v)=\sum_{w\sim_G v}u(w).
\]
Let \(h=2^{\nu_2(n)}\). Both maps are bijective if and only if \(3\nmid n\). When \(3\mid n\), their **complete zero-primary Jordan partitions** are
\[
\begin{array}{c|cc}
& n\ \mathrm{odd}\ (h=1)&n\ \mathrm{even}\ (h\ge2)\\ \hline
P_n&J_2(0)^{\oplus2}&J_h(0)^{\oplus4}\\
M_n&J_1(0)^{\oplus4}&J_{2h}(0)^{\oplus2}
\end{array}.
\]
In particular, both have exactly \(Q^{2n-4h}\) initially periodic configurations even though their temporal entrance distributions differ.

For \(G\in\{P_n,M_n\}\), let \(T_G(u)\) be the least nonnegative integer such that \(B_G^{T_G(u)}u\) is periodic. Put \(r=2n-4h\) when \(3\mid n\), and define \(d_G(t)\) for integers \(t\ge0\) by
\[
\begin{aligned}
 d_{P_n}(t)&=\begin{cases}2\min(t,2),&n\ \mathrm{odd},\\4\min(t,h),&n\ \mathrm{even},\end{cases}\\
 d_{M_n}(t)&=\begin{cases}4\min(t,1),&n\ \mathrm{odd},\\2\min(t,2h),&n\ \mathrm{even}.\end{cases}
\end{aligned}
\]
Then, for \(3\mid n\) and \(t\ge0\),
\[
\#\{u:T_G(u)\le t\}=Q^{r+d_G(t)}.
\]
Thus \(\#\{T_G=0\}=Q^r\); for every \(t\ge1\), the number first entering periodic behavior at \(t\) is \(Q^{r+d_G(t)}-Q^{r+d_G(t-1)}\). For \(3\nmid n\), all \(Q^{2n}\) states have \(T_G=0\). In the non-bijective cases, the sharp maximum entrance times are respectively \(2\) and \(1\) for \(P_n,M_n\) when \(n\) is odd, and \(h\) and \(2h\) when \(n\) is even.

In particular, for \(n=6\), there are \(16\) recurrent binary states in either graph. For the prism their entry-time histogram at times \(0,1,2\) is \((16,240,3840)\); for its Möbius twist, the histogram at \(0,1,2,3,4\) is \((16,48,192,768,3072)\). This is a genuine temporal distinction even though the recurrent population is identical.

## Assumptions and scope
All graphs are undirected, simple, and have the indicated vertex-labeled construction, with \(n\ge3\). The field is any finite field of characteristic two; all sums and matrix operations are in that field. The ordinary prism has cyclic edges within two layers and a perfect matching between corresponding vertices. The Möbius ladder has cycle vertices numbered modulo \(2n\), cyclic edges between consecutive indices and one chord joining each index to its antipode. The Jordan notation refers only to the generalized zero eigenspace; the invertible complement is not classified by primitive-period type. The primitive period of a state is a separate invariant from its first-periodic-entry time.

## Proof
**Step 1: the only possible zero eigenvalues are cubic-root resonances.** Work over an algebraic closure \(K\) of \(\mathbb F_Q\). Every spatial shift decomposes into local factors at roots of unity. Let \(\omega\) be a nontrivial cube root of unity in \(K\), so \(\omega^2+\omega+1=0\). The Laurent polynomial
\[
 a(x)=x+x^{-1}+1=(x^2+x+1)/x
\]
vanishes exactly at \(\omega\) and \(\omega^2\), and its zeros are simple because \(a'(\omega)=1+\omega^{-2}\ne0\). If \(3\nmid n\), these are not roots of \(x^n-1\) (nor of \(x^{2n}-1\)), and both operators are invertible, as will also follow from the local forms below.

**Step 2: prism local form.** Use the ring \(R=K[x,x^{-1}]/(x^n-1)\) for each layer. Let \(S\) be multiplication by \(x\) and \(W\) the layer swap. The update is \((S+S^{-1})I+W=a(S)I+N\), where \(N=W+I\) is a rank-one square-zero operator on the two layer coordinates. Factor \(n=hm\), with odd \(m\). In characteristic two, \(x^n-1=(x^m-1)^h\). If \(3\mid n\), each of the roots \(\omega,\omega^2\) contributes a local factor \(K[y]/(y^h)\), where \(y=a(x)\) is a local uniformizer. On this factor the prism operator is multiplication by \(y+e\) on \(K[y,e]/(y^h,e^2)\), where \(e\) realizes the rank-one nilpotent layer swap. For \(h=1\), this is \(J_2(0)\). For \(h\ge2\), the \(h\)-th power of \(y+e\) vanishes by the Frobenius identity. Its kernel has dimension
\[
\dim_K K[y,e]/(y^h,e^2,y+e)=\dim_K K[y]/(y^h,y^2)=2.
\]
The local factor has total dimension \(2h\); hence exactly two Jordan blocks occur, both of length \(h\) (their lengths are at most \(h\) and sum to \(2h\)). Summing over the two cube roots yields the prism partition. On other factors \(a(x)\) is a unit; since \(N^2=0\), \(a(x)I+N\) is invertible there.

**Step 3: Möbius local form.** On \(K[x,x^{-1}]/(x^{2n}-1)\), the operator is multiplication by
\[
 b_n(x)=x+x^{-1}+x^n.
\]
All distinct roots \(\alpha\) of \(x^{2n}-1\) obey \(\alpha^n=1\) in characteristic two, and therefore \(b_n(\alpha)=a(\alpha)\). Thus only the cube roots can give zero-primary factors, again only when \(3\mid n\). The local exponent of each such root in \(x^{2n}-1=(x^m-1)^{2h}\) is \(2h\). If \(n\) is even, the derivative \(b_n'(\omega)=1+\omega^{-2}\ne0\), so multiplication by \(b_n\) is a single nilpotent Jordan block of length \(2h\) on each root factor. If \(n\) is odd, then \(h=1\) and
\[
 b_n'(\omega)=1+\omega^{-2}+\omega^{n-1}=1+\omega+\omega^2=0.
\]
Since \(b_n(\omega)=0\), multiplication by \(b_n\) vanishes on the length-two local factor. Each root therefore contributes two one-dimensional zero blocks. This proves the Möbius partition.

**Step 4: count entrance times.** The Fitting decomposition of a finite-dimensional linear map over a finite field is the direct sum of its nilpotent zero-primary component and its invertible component. Every point in the invertible component is periodic because that component is a permutation of a finite set; a state becomes periodic exactly when its nilpotent component has vanished. For a nilpotent Jordan block of length \(s\), the kernel of the \(t\)-th power has dimension \(\min(t,s)\). Adding these kernel dimensions over the stated partitions gives \(d_G(t)\). Every state in the complementary invertible component can be chosen independently in \(Q^r\) ways, proving the cumulative and exact formulas. The largest zero block gives the asserted sharp entrance time, attained by taking a terminal basis vector in that block. The proof applies over \(\mathbb F_Q\), since kernel dimensions and zero-primary block sizes are unchanged by extending scalars to \(K\).

## Verification
Two independent GF(2) checks accompany this result. `checker_matrix.py` constructs graph adjacency matrices directly and compares \(1,250\) exact power-kernel ranks to the formula across 75 circumferences. `checker_states.py` separately enumerates every binary configuration on both graph families for each circumference \(3\le n\le8\), classifies the entire functional graph via indegree elimination, and verifies \(33\) cumulative entrance counts on \(174,720\) configurations. Their exact outputs are included. These are finite corroborations; the all-length and all-characteristic-two-field statement is proved by Steps 1–4, not by extrapolating finite experiments.

To reproduce: run `python3 checker_matrix.py` and `python3 checker_states.py` using Python 3.8 or later. No third-party packages are required.

## Relationship to prior work
Guy and Harary introduced and studied the Möbius ladder family, without considering the update dynamics. Macfarlane's work treats reversible second-order cellular automata and their matrix representations, whereas the present maps are first-order neighbor-sum automata on specified cubic graphs. Ward develops general arithmetic and periodic-point methods for additive cellular automata on infinite symbolic spaces; these do not supply the finite-graph transient Jordan partitions. Azimi and Farrokhi analyze both circular and Möbius ladders using real Laplacians, incidence pseudoinverses, resistances and spanning-tree counts, rather than the characteristic-two adjacency dynamics. A published calculation of the binary rank of a single triangular prism is a special instance of an instantaneous rank, not the claimed all-length Jordan and temporal classification. The local ring argument is provided to make these distinctions explicit rather than relying only on search results.

## Limitations
No claim is made about the primitive periods on the invertible recurrent subspace, nor about positive-characteristic fields other than characteristic two. The earliest graph-origin citation dates to October 1967 without a verified day; its day has not been inferred. Historical-priority risk remains from unindexed modular adjacency calculations or uninspected specialized sources, including possible generalizations of published single-graph binary-rank examples. An independent external audit has not been performed.

## References
1. Richard K. Guy and Frank Harary, *On the Möbius Ladders*, Canadian Mathematical Bulletin 10(4) (October 1967), 493–496. DOI: 10.4153/CMB-1967-046-4.
2. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A 37 (published 28 October 2004), 10791–10814. DOI: 10.1088/0305-4470/37/45/006.
3. Thomas B. Ward, *Additive cellular automata and volume growth*, Entropy 2 (2000), 142–167. DOI: 10.3390/e2030142.
4. Ali Azimi and Mohammad Farrokhi Derakhshandeh Ghouchan, *Explicit formulas for matrices associated to ladder, circular ladder, and Möbius ladder graphs*, arXiv:2306.10497v1 (18 June 2023).
5. *The Quantum States of a Graph*, Mathematics 11 (2023), 2310, DOI: 10.3390/math11102310. Its reported triangular-prism binary rank is a finite one-graph comparison; full-text retrieval was rate-limited.
