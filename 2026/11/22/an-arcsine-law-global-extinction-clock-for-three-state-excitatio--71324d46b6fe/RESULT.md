# An arcsine-law global extinction clock for three-state excitation on open paths

## Finding

For each open path \(P_n\) with \(n\ge1\), start the synchronous three-state Greenberg–Hastings system from independent uniform colors \(\{0,1,2\}\). Let \(T_n\) be the first all-rest time. Then

\[
\frac{T_n}{n}\ \Longrightarrow\ Y=\max\{U,1-U\},
\]

where \(U\) has the Lévy arcsine distribution on \([0,1]\). In particular,

\[
\Pr(Y\le y)=\begin{cases}
0,&y<1/2,\\
\frac4\pi\arcsin\sqrt y-1,&1/2\le y\le1,\\
1,&y>1,
\end{cases}
\qquad \lim_{n\to\infty}\frac{\mathbb ET_n}{n}=\frac12+\frac1\pi.
\]

The limiting median is \(\sin^2(3\pi/8)=(2+\sqrt2)/4\). The law is nondegenerate and supported on the upper half of the maximal possible linear-time scale. A deterministic height lemma below gives the mechanism and proves the all-size extinction bound \(T_n\le n+1\).

## Assumptions and scope

Index the vertices by \(i=0,\dots,n-1\), with only the edges between successive indices. Missing exterior neighbors do not contribute. A site of color \(1\) changes to \(2\) and one of color \(2\) changes to \(0\); a color-\(0\) site changes to \(1\) if and only if at least one actual neighbor has color \(1\). All changes use the preceding configuration, not sequential updates. Initial colors are independent, each with probability \(1/3\). The first extinction time is \(T_n=\min\{t\ge0:x_i(t)=0\ \text{for every }i\}\); an initially all-zero word has \(T_n=0\). This is a finite open path, **not** an infinite lattice, a ring, or a higher-contact-threshold model.

For any deterministic initial color word, choose an integer height \(h_0=x_0\); inductively choose the unique increment \(h_i-h_{i-1}\in\{-1,0,1\}\) whose residue modulo three is \(x_i-x_{i-1}\). Let

\[
M=\max_{0\le i<n}h_i,\quad K=3\lceil M/3\rceil,\quad
I=\{i:h_i=M\},\quad S=\{i:h_i\ge K-2\}.
\]

Both \(I\) and \(S\) are nonempty; \(K-M\in\{0,1,2\}\). The following bounds hold pointwise for **every** initial word:

\[
\boxed{\max\{\min S,n-1-\max S\}\ \le T_n\le\ K-M+\min_{j\in I}\max\{j,n-1-j\}.}
\tag{1}
\]

## Proof

**Step 1 (integer-height dynamics).** Extend the height sequence through time by the synchronous rule

\[
h_i(t+1)=h_i(t)+\mathbf 1\!\left\{h_i(t)\not\equiv0\pmod3\ \text{or}\ \exists j\sim i:\ h_j(t)=h_i(t)+1\right\}.\tag{2}
\]

Initially each height has the correct color modulo three and adjacent heights differ by at most one. Assume this at time \(t\). For colors \(1\) and \(2\) the increment in (2) agrees with the automatic Greenberg–Hastings update. If a height is divisible by three (color \(0\)), the existence of a neighbor of color \(1\) is equivalent, using the adjacent-height bound, to the existence of a neighbor precisely one unit higher. Thus the residues of (2) equal the cellular-automaton colors at time \(t+1\). The 1-Lipschitz property persists: equal adjacent heights can separate by at most one; when adjacent heights are \(a\) and \(a+1\), the lower height must increment (it is nonzero modulo three, or its higher neighbor triggers it), so their new difference is zero or one. Induction establishes the lift, and every height is nondecreasing.

**Step 2 (ceiling and propagation).** No height can ever exceed \(K\). Indeed, a site at \(K\), being a multiple of three, could increment only if it had a neighbor at \(K+1\); starting from heights at most \(M\le K\), a first crossing is impossible. Any initial maximum-height vertex \(j\in I\) reaches \(K\) in exactly \(K-M\) updates: until it reaches that multiple of three, its color is \(1\) or \(2\) and it increments automatically. After a vertex has reached \(K\), each of its neighbors has height at least \(K-1\) by the Lipschitz property; if not already \(K\), it is at \(K-1\equiv2\pmod3\) and becomes \(K\) in the next update. Hence \(K\) propagates through the path at unit speed. Choosing the best vertex in \(I\) proves the upper bound in (1); it is at most \((K-M)+(n-1)\le n+1\), and at that time all colors are zero.

**Step 3 (a lower bound using an irreversible threshold).** Let \(A_t=\{i:h_i(t)\ge K-2\}\). If an initially lower site first attains \(K-2\), it previously had height \(K-3\), which is divisible by three; the update therefore needed a neighboring site already at \(K-2\). Thus \(A_t\) is contained in the graph-distance-\(t\) neighborhood of \(A_0=S\). At first extinction all heights are multiples of three; adjacent heights differ by at most one, so **all heights are equal**. Their common value is \(K\), because the ceiling is invariant once an initial maximizer reaches it and cannot be exceeded; more directly, the maximal height can only rise until \(K\), while if extinction occurs earlier the maximizer and every site must share a multiple of three at least \(M\), necessarily \(K\). Consequently both endpoints must have joined \(A_t\), requiring at least their distances from \(S\), which proves the lower bound in (1). This completes the deterministic proof.

**Step 4 (random-walk invariance principle).** Under independent uniform initial colors, the mapping

\[
(x_0,\ldots,x_{n-1})\longleftrightarrow (x_0,\delta_1,\ldots,\delta_{n-1}),\qquad
\delta_i=h_i-h_{i-1}\in\{-1,0,1\}
\]

is bijective: given the right side, recover each color by cumulative summation modulo three. Hence the increments \(\delta_i\) are independent, uniformly distributed on \(\{-1,0,1\}\), with mean zero and variance \(2/3\). Donsker's theorem gives uniform-topology weak convergence of the linearly interpolated profile

\[
\left(\frac{h_{\lfloor(n-1)s\rfloor}-h_0}{\sqrt{(2/3)(n-1)}}\right)_{0\le s\le1}\Longrightarrow (B_s)_{0\le s\le1},
\]

with the obvious interpolation between grid values. Brownian motion has an almost surely unique maximizer \(U\), so the normalized positions of **all** indices in \(I\) and \(S\) converge to \(U\): after normalization the \(S\) heights are within \(2/\sqrt{(2/3)(n-1)}\) of the global maximum, which vanishes, and uniqueness of the limiting maximizer precludes a macroscopic separation. The lower and upper bounds in (1), divided by \(n\), therefore both converge in distribution to \(\max(U,1-U)\). Slutsky's theorem proves the claimed limit.

Lévy's Brownian argmax theorem gives \(\Pr(U\le u)=(2/\pi)\arcsin\sqrt u\). By symmetry of this CDF,

\[
\Pr\{\max(U,1-U)\le y\}=\Pr(1-y\le U\le y)
=\frac4\pi\arcsin\sqrt y-1
\]

for \(1/2\le y\le1\). Finally \(0\le T_n/n\le1+1/n\), so boundedness permits passage to expectations. Direct integration of the arcsine law gives \(\mathbb E|U-1/2|=1/\pi\), completing the proof.

## Verification

The included dependency-free program `verify.py` implements both the direct color update and the independent integer-height update. It checks their equality at every step, the residue and spatial Lipschitz invariants, the invariant height ceiling, both bounds in (1), and the terminal constant height for **every** one of the \(3^n\) initial colorings at each \(1\le n\le10\). A separate integer-state implementation independently checks the full extinction-time histograms through \(n=9\). The exact observed maximum time was \(n+1\) at every tested length. In particular, the numbers attaining the maximal delay at lengths \(n=8,9,10\) were \(534\), \(1500\), and \(4246\), respectively. `verification_output.txt` records the actual output. These are finite checks supporting the lemma; the proof above establishes the result for all lengths and the limit distribution without extrapolating from experiments.

## Relationship to prior work

Durrett and Steif (1991) proved the inverse-square-root decay of **activity at a fixed site on the infinite one-dimensional lattice**, rather than the distribution of the **first global all-zero time on a length-\(n\) open path**. Fisch and Gravner (1995) investigated multistate one-dimensional Greenberg–Hastings dynamics and local relaxation, again with a distinct observable and setting. Gravner, Lyu and Sivakoff (first public preprint 2016-10-24; journal 2018) proved a finite-graph synchronization criterion and a diameter bound, and supplied a maximum-ranking representation. Their broad comparison machinery is relevant and is credited; neither their diameter statement nor their infinite-tree activity results state the nondegenerate global extinction-time law here. A later exact enumeration of the maximally delayed open-path states gives a square-root **endpoint** probability \(\Pr(T_n=n+1)\), but does not by that statement determine the typical linear-scale clock. Deriving a full random limiting law requires the initial-height near-maximum localization and Brownian-argmax argument above. Historical priority remains qualified, particularly for material not available in full text.

## Limitations

The result assumes a uniform independent three-color initialization and an open path with free ends. It does not give finite-\(n\) closed forms for the entire extinction-time distribution, quantitative convergence rates, or universality under nonuniform initial densities. It does not claim a new finite-graph synchronization theorem or a new Lévy arcsine law. The full text of the nearest published maximal-delay enumeration was not accessible at review time, and equivalent historical derivations may exist. Independent external scientific validation has not yet been performed.

## References

1. R. Durrett and J. E. Steif, *Some Rigorous Results for the Greenberg–Hastings Model*, Journal of Theoretical Probability 4 (1991), 669–690. https://sites.math.duke.edu/~rtd/reprints/paper66.pdf
2. R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, Complex Systems 9 (1995), 329–348. https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (public 2016-10-24); Annals of Applied Probability 28 (2018), 3324–3357. https://arxiv.org/abs/1610.07320 ; https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf
4. *A square-root law for maximal extinction times in three-state excitation on finite paths*, published research record dated 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-square-root-law-for-maximal-extinction-times-in-three-state-ex--2a387c4efac2 (full text not accessible in this review).
5. P. Lévy, *Sur certains processus stochastiques homogènes*, Compositio Mathematica 7 (1939), 283–339 (classical Brownian arcsine theorem); Donsker's functional central limit theorem (classical).
