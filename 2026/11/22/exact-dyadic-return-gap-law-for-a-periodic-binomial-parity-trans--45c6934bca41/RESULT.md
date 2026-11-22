# Exact dyadic return-gap law for a periodic binomial-parity transform

## Finding
Let \(n\ge0\), and adopt the convention \(\binom uv=0\) when \(u<v\) or \(v<0\). Define the integer sequence
\[
T(n)=\sum_{k=0}^{n}\left[\binom{-2n+8k}{n+k}\binom nk\bmod2\right].
\]
The brackets return the remainder \(0\) or \(1\) of the product, before the summands are added. A published run-length identity (References 1 and 2) implies \(T(n)\in\{0,1\}\), with \(T(n)=1\) precisely when no maximal run of ones in the binary expansion of \(n\) has length congruent to \(2\pmod3\). Let
\[
\mathcal A_L=\{n:0\le n<2^L,\ T(n)=1\},\qquad L\ge0.
\]
For \(L\ge1\), enumerate \(\mathcal A_L\) increasingly as \(a_1<\cdots<a_h\), and let \(M_L(g)=\#\{1\le i<h:a_{i+1}-a_i=g\}\) for every integer \(g\ge1\). Define
\[
D(z)=1-z-z^2-z^3,\qquad g_j=2^j+1+\mathbf1_{j\equiv1\pmod3}\quad(j\ge1).
\]
All nonzero gap-count generating functions are exactly
\[
\boxed{\begin{aligned}
\sum_{L\ge1}M_L(1)z^L&=\frac{z+z^2}{(1-z^3)D(z)},\\
\sum_{L\ge1}M_L(2)z^L&=\frac{2z^3-z^6}{(1-z^3)D(z)},\\
\sum_{L\ge1}M_L(g_j)z^L&=\frac{z^{j+3}}{D(z)}\quad(j\ge1).
\end{aligned}}
\]
Every other \(M_L(g)\) vanishes identically. In particular, the exact global return-gap spectrum is
\[
\boxed{\{1,2\}\cup\{2^j+1+\mathbf1_{j\equiv1\pmod3}:j\ge1\}}
=\{1,2,4,5,9,18,33,65,130,257,513,1026,\ldots\}.
\]
Each \(g_j\) first occurs between two indices smaller than \(2^{j+3}\).

Write \(\lambda>1\) for the unique positive root of \(\lambda^3=\lambda^2+\lambda+1\), and \(q=\lambda^{-1}\). For every fixed permitted gap, its limiting *dyadic-prefix* share exists:
\[
\boxed{\begin{aligned}
\pi(1)&=\frac{q}{1-q^3},\\
\pi(2)&=\frac{2q^3-q^6}{(1-q^3)(1+q)},\\
\pi(g_j)&=\frac{q^{j+3}}{1+q}\quad(j\ge1).
\end{aligned}}
\]
These probabilities sum to one; in particular the limiting gap distribution has **infinite first moment** despite every finite list of observed gaps having finite mean.

## Assumptions and scope
All indices are nonnegative integers; the ordinary binomial coefficient convention is used even when \(-2n+8k\) is negative. A consecutive gap joins adjacent elements of the set \(\mathcal A_L\) in increasing *integer* order, not adjacent binary words in lexicographic order. The formulas are formal power-series identities with integer coefficients, valid for all integers \(L\ge1\) and \(j\ge1\). The probabilities are limits along precisely \(\{0,\ldots,2^L-1\}\), not asserted to be the same for arbitrary cutoffs \(N\). No claim is made that the published run-length identity is new.

## Proof
**1. Published parity support.** The binomial-to-run-length-transform formula of Rampersad and Wiebe (Reference 1, new-transform section) expresses \(T(n)\) as the product of terms \(s_r\) over the lengths \(r\) of maximal one-runs, where \(s_r=1\) for \(r\equiv0,1\pmod3\) and \(s_r=0\) for \(r\equiv2\pmod3\). The empty product at \(n=0\) equals one. Thus the exact support rule follows and we now derive the remaining claims independently of that source.

**2. Three prefix-state sets.** For an integer \(L\ge0\), let \(A_L,B_L,C_L\) be the integers represented by \(L\) binary digits which are accepted when the current unfinished one-run has length respectively \(0,1,2\pmod3\) immediately before those digits. On reading \(0\), a run in state two is rejected; on reading \(1\), its state advances cyclically. At the right end, states zero and one are accepted. Consequently \(A_0=B_0=\{0\}\), \(C_0=\varnothing\), and, writing \(h=2^{L-1}\),
\[
\boxed{\begin{aligned}
A_L&=A_{L-1}\ \dot\cup\ (h+B_{L-1}),\\
B_L&=A_{L-1}\ \dot\cup\ (h+C_{L-1}),\\
C_L&=h+A_{L-1}.
\end{aligned}}
\tag{1}
\]
The unions are disjoint because the first sets are below \(h\), and the translated sets are above or equal to \(h\). Leading zeroes are harmless and \(A_L=\mathcal A_L\).

By following the lexicographically greatest admissible length-\(L\) binary word, \(\max A_L=2^L-1-\mathbf1_{L\equiv2\pmod3}\) for all \(L\ge0\). Indeed, if \(L\not\equiv2\pmod3\) all ones is allowed; otherwise replacing the final one by zero yields the maximal possible acceptable integer. Also \(\min B_L=0\), and \(\min C_L=2^{L-1}\) for \(L\ge1\). The last formula follows from \(C_L=2^{L-1}+A_{L-1}\) and \(0\in A_{L-1}\).

**3. Boundary gaps.** For a finite increasing set \(X\), write \(H(X)\) for its formal multiset of distances between consecutive entries, and \(\delta_g\) for one occurrence of gap \(g\). From (1), for \(L\ge1\) the boundary separating the two blocks of \(A_L\) has length
\[
u_L=2^{L-1}-\max A_{L-1}=1+\mathbf1_{L\equiv0\pmod3}.
\]
For \(L\ge2\), the boundary in \(B_L\) has length
\[
v_L=2^{L-1}+\min C_{L-1}-\max A_{L-1}
=2^{L-2}+1+\mathbf1_{L\equiv0\pmod3}.
\]
Let \(H_L^A=H(A_L)\), and analogously \(H_L^B,H_L^C\). Their complete recurrences are
\[
H_L^A=H_{L-1}^A+H_{L-1}^B+\delta_{u_L},\quad
H_L^B=H_{L-1}^A+H_{L-1}^C+\delta_{v_L},\quad
H_L^C=H_{L-1}^A,
\]
when all displayed blocks are nonempty. In particular, combining them for \(L\ge3\) gives
\[
\boxed{H_L^A=H_{L-1}^A+H_{L-2}^A+H_{L-3}^A
+\delta_{1+\mathbf1_{L\equiv0\pmod3}}
+\delta_{2^{L-3}+1+\mathbf1_{L\equiv1\pmod3}}.}\tag{2}
\]
The initial data are \(H_0^A=\varnothing\), \(H_1^A=\delta_1\), and \(H_2^A=2\delta_1\). Formula (2) is exact as a multiset identity; its last term is gap two at \(L=3\) and equals \(g_{L-3}\) thereafter.

**4. Exact generating functions and spectrum.** Coefficientwise, the homogeneous part of (2) has denominator \(D(z)\). For gap one the initial terms contribute \(z+z^2\), while new gap-one boundaries occur precisely for \(L\ge3\) not divisible by three. Therefore the numerator is \((z+z^2)/(1-z^3)\). For gap two there are the two sources at \(L=3\), and one further boundary source for each multiple of three at least six; thus its numerator is \(2z^3+z^6/(1-z^3)=(2z^3-z^6)/(1-z^3)\). For each \(j\ge1\), the final term of (2) introduces gap \(g_j\) once at \(L=j+3\), with no other source. This yields all three claimed generating functions. The \(g_j\) are strictly increasing, so there is no double counting, and the recurrences exclude all other gaps.

**5. Limiting dyadic frequencies.** Let \(a_L=|A_L|\). Taking sizes in (1) yields \(a_0=1\), \(a_1=2\), \(a_2=3\), and \(a_L=a_{L-1}+a_{L-2}+a_{L-3}\) for \(L\ge3\); hence
\[
\sum_{L\ge0}a_Lz^L=\frac{1+z}{D(z)}.
\]
The unique positive smallest-modulus zero of \(D(z)\) is \(q=1/\lambda\), and it is simple; the other roots have strictly larger modulus. Hence each fixed-gap count divided by \(a_L-1\) converges to the numerator of its generating function evaluated at \(q\), divided by \(1+q\). This gives the displayed \(\pi\)-formulas. Their sum is one by
\[
\frac q{1-q^3}+\frac{2q^3-q^6}{(1-q^3)(1+q)}
+\frac{q^4}{(1-q)(1+q)}=1
\]
using \(1=q+q^2+q^3\). Finally \(g_j\ge2^j\) and \(\pi(g_j)=q^{j+3}/(1+q)\); since \(2q>1\), the infinite series \(\sum_{j\ge1}g_j\pi(g_j)\) diverges.

## Verification
The standalone file `verify_gap_law.py` independently calculates the defining binomial sum for \(301\) indices, checks the period-three run product and the older Fibonacci-transform parity support, verifies all three automaton start states through binary length ten, and checks every exact gap histogram for lengths one through eighteen. The latter covers \(121395\) adjacent pairs; direct binomial results agree with the digit characterization at each tested index. Run with `python3 verify_gap_law.py` from a standard Python installation. These finite results are diagnostic; the complete proof is (1)–(2) and its generating-function consequences.

## Relationship to prior work
Rampersad and Wiebe (2023, Reference 1) proved the binomial representation and its period-three run-length transform, but their inspected new-transform, mean-value, and family sections do not formulate the ordered consecutive-support gap spectrum or the exact multiscale frequency laws. Chai Wah Wu (Reference 2), predating that representation, proves that another binomial sum is the run-length transform of Fibonacci numbers; modulo two it has **the same support** because Fibonacci numbers \(1,1,2,3,5,\ldots\) have parity \(1,1,0\) repeated. The present gap spectrum therefore applies to both support-equivalent sequences, and novelty is claimed only for the gap enumeration and its distribution, **not** for that equivalence or for the established run transforms. The Baum–Sweet return-gap laws concern a distinct automatic word with distinct permitted distances; those do not imply this theorem.

## Limitations
The only distribution limit established is along dyadic prefixes. No independent external validation has been performed, and not all potentially relevant uncatalogued literature is accessible. A pre-existing unpublished or unindexed classification of the same Fibonacci-parity support's return gaps would cover the present result even without identifying this binomial sum by name. The infinite theorem does not rest on the finite checker.

## References
1. N. Rampersad and M. Wiebe, *Sums of products of binomial coefficients mod 2 and 2-regular sequences*, arXiv:2309.04012v1 (first made public 2023-09-07), especially the theorem on the period-\(1,1,0\) transform; final open-access text: *INTEGERS* 24 (2024), article A73, Theorem 15, https://math.colgate.edu/~integers/y73/y73.pdf .
2. C. W. Wu, *Sums of products of binomial coefficients mod 2 and run length transforms of sequences*, arXiv:1610.06166 (2016); later published in *INTEGERS* 22 (2022). The Fibonacci-transform theorem provides the same parity support, not its return-gap census.
3. OEIS A246028, Fibonacci run-length transform, https://oeis.org/A246028 . The entry is a sequence reference rather than an exact return-gap-spectrum result.
