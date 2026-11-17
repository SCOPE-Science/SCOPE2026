# Exact relaxation law for three-color successor dynamics on transitive tournaments

## Finding
For every integer \(n\ge1\), orient the complete graph on the ordered vertices \(1,\ldots,n\) by an arc \(i\to j\) when \(i<j\). Let each vertex have one of the three colors in \(\mathbb Z/3\mathbb Z\). At each synchronous step, vertex \(i\) advances from \(c\) to \(c+1\pmod3\) exactly when at least one out-neighbor \(j>i\) currently has color \(c+1\pmod3\); otherwise it retains \(c\). Write \(T_n(x)\) for the smallest \(t\ge0\) such that the configuration reached after \(t\) steps is fixed.

Every trajectory fixes. For every integer \(n\ge1\), its complete first-fixation-time polynomial is
\[
\sum_{x\in\{0,1,2\}^{n}}z^{T_n(x)}=3H_n(z),\qquad
H_n(z)=\frac{2z(2+z)^{n-1}+(1-z)(n+(n-1)z)}{1+z}.
\]
The displayed rational expression is a polynomial. Equivalently, \(H_1(z)=1\) and for every \(n\ge2\),
\[
H_n(z)=(2+z)H_{n-1}(z)+(n-2)(z^2-1).
\]
There are exactly \(3n\) fixed configurations. The sharp maximal transient is \(n-1\) steps; exactly three initial colorings achieve it when \(n=2\), and exactly six when \(n\ge3\). The case \(n=1\) has three fixed states and zero transient.

For a uniform random initial coloring, write \(T_n\) for its fixation time. Then
\[
\mathbb E T_n=\frac n3+\frac16-\frac{6n-3}{2\cdot3^n},
\qquad
\frac{T_n-n/3}{\sqrt{2n/9}}\ \Longrightarrow\ \mathcal N(0,1).
\]
In particular \(\operatorname{Var}(T_n)=2n/9+O(1)\), while for \(n\ge3\) the probability of the worst-case delay is exactly \(6/3^n\). This separates a typical linear-time relaxation near \(n/3\) from the sharp \(n-1\) bound, with exponentially rare extremizers.

## Assumptions and scope
The digraph is the **transitive tournament**: out-neighbors are precisely the later vertices. Its direction is essential; replacing each arc by an undirected edge changes the dynamical problem. Updates are synchronous, successor contact has threshold one, colors are taken cyclically modulo three, and each of the \(3^n\) colorings is distinguished by vertex labels. No probabilistic independence is needed for the deterministic counts; the central limit statement assumes the uniform distribution over these colorings.

For clarity, a fixed configuration has no vertex with a successor-colored later vertex. Such strings are exactly \((c+1)^k c^{n-k}\), for some \(c\in\mathbb Z/3\mathbb Z\) and \(0\le k<n\), where exponent notation denotes repetition, not arithmetic power. These are \(3n\) distinct strings.

## Proof
**Two-color collapse.** Suppose a suffix of the ordered tournament currently uses one or two colors. With one color it is fixed. With two, write its color set as \(\{c,c+1\}\). The \(c+1\)-colored vertices have no later successor \(c+2\), so they stay put. The \(c\)-colored vertices advance exactly when a \(c+1\) occurs to their right. After one update, the suffix has the form \((c+1)^k c^{m-k}\) and is fixed. These two colors cannot generate the absent third color at any future update. Conversely, a three-color suffix cannot become fixed in one update. To see this, select the rightmost occurrence of each of its three colors, in left-to-right order at positions \(p<q<r\), with respective colors \(a,b,c\). If \(c=b+1\) modulo three, the selected sites update to \(b,c,c\), and the site at \(p\) remains enabled by the one at \(q\). If \(c=b-1\), the sites update to \(c,b,c\), and again \(p\) remains enabled by \(q\). No later occurrence of the third color can affect the middle site, by the rightmost-occurrence choice. Hence, if a suffix has positive fixation time \(\tau\), its configurations at times \(0,\ldots,\tau-2\) use all three colors and its configuration at time \(\tau-1\) uses exactly two colors.

**Prepending one vertex.** Take a suffix of length \(m\) with initial fixation time \(\tau>0\). At each step before \(\tau-1\), the suffix uses all three colors; therefore any new leftmost vertex necessarily advances at every one of those steps. Write the two colors at time \(\tau-1\) as \(c,c+1\), and write the new vertex's then-current color as \(b\). This is a cyclic permutation of its initial color as the latter varies over the three possibilities. If \(b=c+1\), the new vertex stops, and the full word fixes at time \(\tau\). If \(b=c\), it advances once to \(c+1\) and also fixes by time \(\tau\). If \(b=c-1\), it advances to \(c\) and then advances again to \(c+1\): at time \(\tau\), the unchanged \(c+1\) representatives of the suffix are still present, providing the second contact. It is fixed thereafter, and the full word has fixation time \(\tau+1\). Consequently, each nonfixed suffix has precisely two one-vertex extensions with the same fixation time and one with a time greater by one.

If the suffix is already fixed, its form is \((c+1)^k c^{m-k}\). For each of the three monochromatic suffixes (\(k=0\)), two choices of the new color give zero delay and one gives one-step delay. For each of the \(3(m-1)\) mixed fixed suffixes (\(k\ge1\)), the three choices give delays zero, one, and two, respectively. Thus the three contributions from initially fixed suffixes are \(3(m+1)\), \(3m\), and \(3(m-1)\) at delays zero, one, and two.

**Generating polynomial.** Put \(H_n(z)=\tfrac13\sum_xz^{T_n(x)}\). The nonfixed extensions supply \((2+z)(H_m(z)-m)\), while initially fixed suffixes supply \((m+1)+mz+(m-1)z^2\). Therefore \(H_{m+1}(z)=(2+z)H_m(z)+(m-1)(z^2-1)\), beginning with \(H_1(z)=1\). Solving the recurrence gives the formula stated in the finding. Because its coefficients count configurations, the rational expression has no pole and is a polynomial. Also \(H_n(0)=n\), showing the fixed-state count directly.

For \(n=2\), the polynomial is \(H_2(z)=2+z\), so the maximal depth one is attained three times. For \(n=3\), \(H_3(z)=3+4z+2z^2\), so six inputs have maximal depth two. For \(n\ge4\), the top-degree coefficient is inherited unchanged from the preceding polynomial; hence it remains two, and the sharp maximum is \(n-1\). Such extremizers can equivalently be constructed recursively: begin with any of the six three-letter permutations of the colors and, at every extension to the left, choose the unique new color that increases fixation time by one.

**Fluctuation law.** Divide the probability generating polynomial by \(3^{n-1}\). In a neighborhood of \(z=1\),
\[
\mathbb E[z^{T_n}]=\frac{2z}{1+z}\left(\frac{2+z}{3}\right)^{n-1}+\frac{(1-z)(n+(n-1)z)}{(1+z)3^{n-1}}.
\]
Differentiation at one gives the exact mean above and \(\operatorname{Var}(T_n)=2n/9+O(1)\). Substituting \(z=e^{it/\sqrt{2n/9}}\), expanding the logarithm of the leading term around zero, and centering at \(n/3\) gives the limiting standard normal characteristic function \(e^{-t^2/2}\); the second term is exponentially small uniformly for bounded \(t\). The continuity theorem proves the claimed central limit.

## Verification
The standalone program `verify_direct.py` directly applies the synchronous update to all \(3^n\) states for \(1\le n\le9\), checks the first fixed time, and compares the complete histograms with the polynomial recurrence. A separately written C++ implementation in `verify_cpp.cpp` enumerates all states for \(1\le n\le11\), independently constructs the transition map, and compares every histogram with its own integer recurrence. The captured outputs are `verify_python_output.txt` and `verify_cpp_output.txt`. Both programs completed without assertion failures when run from their included source. These finite checks are corroboration: the proof's one-vertex extension argument establishes every \(n\), without relying on any finite cutoff.

## Relationship to prior work
The three-color cyclic successor-contact update is classical (Fisch, Gravner, and Griffeath, arXiv:patt-sol/9304001v1, public submission 1993-04-02). Gravner, Lyu, and Sivakoff (arXiv:1610.07320v1, 2016-10-24) study the same three-color update on **undirected** connected graphs, giving a fixation/synchronization dichotomy in terms of winding and graph cycles. Their hypothesis explicitly requires a simple undirected graph and does not cover the transitive orientation of a complete graph: symmetrizing it yields the complete undirected graph and changes the dynamics. Neither inspected statement supplies the present all-size first-fixation-time polynomial, linear Gaussian scaling, or six-extremizer law. This is a best-knowledge literature comparison, not a proof of historical priority. A full-text historical search beyond accessible records remains warranted.

## Limitations
This classification is restricted to exactly three colors, threshold-one successor contact, and the unique transitive orientation of a labelled tournament. It does not assert the same formula for a general acyclic digraph, a tournament with directed cycles, or undirected cyclic automata. The finite checks through eleven sites do not establish the infinite-family theorem by themselves. External independent mathematical audit has not been performed. An unindexed or inaccessible older formulation may already contain part of the result.

## References
1. R. Fisch, J. Gravner, D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, arXiv:patt-sol/9304001v1, submitted 1993-04-02; https://arxiv.org/abs/patt-sol/9304001 . The accessible arXiv page gives the update definition and dated submission; its original full paper was not accessible in the inspected online representation.
2. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, submitted 2016-10-24; https://arxiv.org/abs/1610.07320 . Its introduction, model equations, and Theorem 3 were inspected in the accessible full text and concern undirected graphs.
