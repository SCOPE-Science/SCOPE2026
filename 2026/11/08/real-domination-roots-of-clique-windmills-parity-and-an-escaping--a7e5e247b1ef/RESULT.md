# Real domination roots of clique windmills: parity and an escaping root

## Finding

For integers \(k,m\ge2\), form the clique windmill \(W_{k,m}=K_1\vee(mK_k)\), that is, \(m\) copies of \(K_{k+1}\) sharing exactly their central vertex. Let \(D_{k,m}(z)\) be its ordinary domination polynomial. Its previously known closed form is
\[
D_{k,m}(z)=z(1+z)^{km}+\big((1+z)^k-1\big)^m.
\]
Its **complete real-zero spectrum** is as follows. The zero \(0\) is always simple. All other real zeros, when present, are simple:

| Parities | Nonzero real zeros |
| --- | --- |
| \(k\) even, \(m\) odd | None |
| \(k\) odd, \(m\) odd | Exactly one in \(( -\infty,-2)\) |
| \(k\) even, \(m\) even | Exactly one in each of \((-2,-1)\) and \((-1,0)\) |
| \(k\) odd, \(m\) even | Exactly one in each of \(( -\infty,-2)\) and \((-1,0)\) |

For fixed \(k\), letting even \(m\to\infty\), the zero in \((-1,0)\) tends to \(-1+2^{-1/k}\). For even \(k\), the other zero tends to \(-1-2^{-1/k}\). For odd \(k\), the other zero instead escapes to negative infinity: writing it \(-1-s_{k,m}\), one has
\[
s_{k,m}\sim\left(\frac{k m}{\log m}\right)^{1/k}
\quad(m\to\infty).
\]
For odd \(k\), this asymptotic also holds along odd \(m\). For all \(k,m\ge2\), no nonzero integer is a domination root.

## Assumptions and scope

Graphs are finite, simple, undirected, and unweighted. A dominating set \(S\) is a subset of vertices such that every vertex outside \(S\) has a neighbor in \(S\). The domination polynomial is \(D_G(z)=\sum_{S\text{ dominating}}z^{|S|}\). The parameters \(k\) (number of noncentral vertices per blade) and \(m\) (number of blades) are integers at least two. The asymptotics fix \(k\) and allow \(m\) to grow. All real roots are counted without multiplicity unless simplicity is specified.

## Proof

**Exact starting polynomial.** If a dominating set contains the central vertex, any subset of the \(km\) remaining vertices is permitted, contributing \(z(1+z)^{km}\). Without the central vertex, the set must intersect every one of the \(m\) mutually nonadjacent blades, contributing \(((1+z)^k-1)^m\). This proves the displayed polynomial independently of its previous appearance in the literature. Its coefficient of \(z\) is one, so \(0\) is simple. There are no positive real zeros because all nonzero polynomial coefficients are positive. At \(z=-1\), the value is \((-1)^m\ne0\).

**Roots in \((-1,0)\).** Put \(z=t-1\) with \(0<t<1\). Then
\[
D_{k,m}(t-1)=-(1-t)t^{km}+(t^k-1)^m.
\]
If \(m\) is odd, both summands are negative. If \(m\) is even, a zero is equivalent to
\[
\frac{(t^{-k}-1)^m}{1-t}=(1-t)^{m-1}\left(\sum_{j=1}^{k}t^{-j}\right)^m=1.
\]
For \(m\ge2\), the left side is strictly decreasing from \(+\infty\) to \(0\) as \(t\) increases from \(0\) to \(1\). Thus there is exactly one root here, with nonzero derivative.

**Roots below \(-1\), odd \(k\).** Put \(z=-1-s\), \(s>0\). For odd \(k\),
\[
D_{k,m}(-1-s)=(-1)^m\big((1+s^k)^m-(1+s)s^{km}\big).
\]
A zero is therefore equivalent to
\[
(1+s^{-k})^m=1+s.
\]
The left side strictly decreases from \(+\infty\) to \(1\) whereas the right side strictly increases from \(1\) to \(+\infty\). There is exactly one simple root. At \(s=1\), the left side is \(2^m>2\) because \(m\ge2\), so the root has \(s>1\), or \(z<-2\).

**Roots below \(-1\), even \(k\).** For even \(k\),
\[
D_{k,m}(-1-s)=(s^k-1)^m-(1+s)s^{km}.
\]
When \(s\ge1\), the first term is at most \(s^{km}\), so the expression is strictly negative. When \(0<s<1\), odd \(m\) again makes both terms negative. For even \(m\), the equation becomes
\[
(s^{-k}-1)^m=1+s.
\]
The left side decreases strictly from \(+\infty\) to \(0\), while the right side increases from \(1\) to \(2\). Exactly one simple solution \(s\in(0,1)\) exists, corresponding to \(z\in(-2,-1)\). These cases exhaust the entire negative real axis, proving the classification and simplicity.

**Bounded limits.** Write \(a=2^{-1/k}\). For even \(m\), the unique positive parameter \(t_m\in(0,1)\) of the root in \((-1,0)\) satisfies \((t_m^{-k}-1)^m=1-t_m\). At \(t=a\), the left side equals \(1>1-a\), so \(t_m>a\). For every fixed \(b\) with \(a<b<1\), the left side at \(b\) tends to zero and is eventually smaller than \(1-b\); hence \(t_m<b\) eventually. Thus \(t_m\to a\). For even \(k\), the parameter \(s_m\) of the root in \((-2,-1)\) satisfies \((s_m^{-k}-1)^m=1+s_m\), giving \(s_m<a\); for any fixed \(0<b<a\), its left side at \(b\) diverges and eventually exceeds \(1+b\). Hence \(s_m\to a\).

**Escaping root.** For fixed odd \(k\), its parameter \(s_m>1\) satisfies
\[
m\log(1+s_m^{-k})=\log(1+s_m).
\]
If \(s_m\) remained bounded along an unbounded subsequence of \(m\), the left side would diverge while the right side stayed bounded. Therefore \(s_m\to\infty\). Expanding the logarithms gives \(m/s_m^k\sim\log s_m\), or \(m\sim s_m^k\log s_m\). Taking logarithms shows \(\log s_m^k\sim\log m\); substituting yields \(s_m^k\sim km/\log m\), proving the claimed escape rate. The reasoning is independent of the parity of \(m\).

**Integer-root exclusion.** The bounded nonzero roots lie strictly between consecutive integers. The only other possible nonzero real roots occur for odd \(k\) at \(z=-1-s\) with \(s>1\). If such a root were an integer, \(s\ge2\) would be an integer and
\[
(1+s^k)^m=(1+s)s^{km}.
\]
The left side is congruent to \(1\) modulo \(s\), whereas the right side is divisible by \(s\), a contradiction.

## Verification

The accompanying `verify.py` has two independent finite checks. It constructs the graph directly and enumerates dominating vertex subsets in nine labelled graph instances, comparing every polynomial coefficient with the stated formula. It also uses SymPy exact real-root isolation (Sturm-based root counts) for all \(2\le k,m\le7\), distinguishing the intervals \(( -\infty,-2)\), \((-2,-1)\), \((-1,0)\), and \((0,\infty)\). The successful run prints `GRAPH_DEFINITION_EXHAUSTIVE_OK 9`, `EXACT_STURM_INTERVAL_COUNTS_OK 36`, and `VERIFY_OK`. The unrestricted proof and asymptotic statement do not rely on these finite experiments.

## Relationship to prior work

The polynomial of a related diagonal subfamily \(K_1\vee(nK_n)\) and an annular bound on its complex zeros are in B. A. Rather, *On domination polynomials of some graphs* (2025), Theorem 2.10 and Proposition 2.13. They do not classify its real roots. Rather, *On roots of domination polynomials for friendship and book graphs* (arXiv:2604.08998, initially posted 2026-04-10), establishes the \(k=2\) friendship subfamily, including its two bounded limits for even \(m\); this case is **prior work**, not claimed new here. Jahari and Alikhani (arXiv:1501.05856) study flowers built from cycles and generalized books, different from the clique blades studied here. The real-root density result of Beaton and Brown concerns the union of domination roots across all graphs, not the exact root spectrum of this family. The present result extends the exact classification to all blade-clique sizes \(k\ge3\), and identifies the previously unreported unbounded left-root regime for odd \(k\).

## Limitations

Only real roots are classified; no full complex-root locus or general complex-root bounds are proved. The graph must be a windmill of identical complete blades with a single common universal vertex and at least two blades. The escape law holds as the number of blades increases with fixed odd \(k\); it makes no assertion about joint growth of \(k\) and \(m\). The classification is a mathematical proof with finite computational checks, not an independent external validation. Priority against undiscovered works remains provisional.

## References

1. B. A. Rather, *On roots of domination polynomials for friendship and book graphs*, arXiv:2604.08998 (initial public posting 2026-04-10), https://arxiv.org/abs/2604.08998.
2. B. A. Rather, *On domination polynomials of some graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing 126 (2025), 279–289, DOI: 10.61091/jcmcc126-19, https://combinatorialpress.com/jcmcc-articles/volume-126/on-domination-polynomials-of-some-graphs/.
3. S. Jahari and S. Alikhani, *Domination polynomial of generalized friendship and generalized book graphs*, arXiv:1501.05856 (2015), https://arxiv.org/abs/1501.05856.
4. I. Beaton and J. I. Brown, *On the real roots of domination polynomials*, Contributions to Discrete Mathematics 16 (2021), DOI: 10.55016/ojs/cdm.v16i3.72075, https://cdm.ucalgary.ca/article/view/72075.
