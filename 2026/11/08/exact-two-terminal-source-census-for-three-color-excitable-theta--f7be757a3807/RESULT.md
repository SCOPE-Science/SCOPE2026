# Exact two-terminal source census for three-color excitable theta networks

## Finding
For deterministic threshold-one three-state Greenberg–Hastings dynamics, the number of configurations **already** on a primitive three-cycle of a generalized theta network is given exactly by a two-variable polynomial marking the numbers of paths exciting its two terminals. The formula works for every \(m\ge3\) internally disjoint terminal-to-terminal paths of lengths \(L_i\ge2\) and remains unchanged after arbitrary finite trees are attached to core vertices.

Let \(u,v\) be the distinguished terminals, and orient each core path from \(u\) toward \(v\). For \(a,b\ge1\), let \(N_{a,b}\) count primitive-three configurations with exactly \(a\) core paths supplying the next color at \(u\) and exactly \(b\) core paths supplying the next color at \(v\). For \(d\in\{0,1,2\}\) define
\[
\begin{aligned}
c_L(d)&=\sum_{j=0}^{L}{\mathbf{1}}_{L-2j\equiv d\ (\mathrm{mod}\ 3)}+\sum_{j=0}^{L-1}{\mathbf{1}}_{L-1-2j\equiv d\ (\mathrm{mod}\ 3)},\\
p_L(d)&={\mathbf{1}}_{L\equiv d\ (\mathrm{mod}\ 3)},\qquad
q_L(d)={\mathbf{1}}_{-L\equiv d\ (\mathrm{mod}\ 3)},\\
W_{L,d}(s,t)&=c_L(d)-p_L(d)-q_L(d)+p_L(d)s+q_L(d)t.
\end{aligned}
\]
All indicators are either zero or one. Then the complete source census is
\[
\boxed{\sum_{a,b\ge1}N_{a,b}s^a t^b=3\sum_{d=0}^{2}\left[
\prod_{i=1}^m W_{L_i,d}(s,t)
-\prod_{i=1}^m W_{L_i,d}(0,t)
-\prod_{i=1}^m W_{L_i,d}(s,0)
+\prod_{i=1}^m W_{L_i,d}(0,0)\right].}
\]
At \(s=t=1\), this gives the exact total primitive-three population \(P_3(G)\), and \(P_3(G)/3\) counts distinct three-state orbits. The nonzero criterion is the existence of distinct \(i,j\) with \(L_i+L_j\equiv0\pmod3\).

When all paths have length \(3h\), the count reduces to
\[
P_3(G)=3\left[(2h+1)^m-2(2h)^m+(2h-1)^m\right],
\]
while equal path lengths not divisible by three give zero. Thus fixed \(m\) has polynomial growth \(P_3(G)\sim3m(m-1)(2h)^{m-2}\) as \(h\to\infty\), despite an exponentially growing ambient state space. For three paths with lengths \(3h_1,3h_2,3h_3\), the count simplifies further to \(12(h_1+h_2+h_3)\).

## Assumptions and scope
The core is a simple graph with exactly \(m\ge3\) internally vertex-disjoint \(u\)-to-\(v\) paths, each of length \(L_i\ge2\), and no edges other than those in these paths. A finite tree may be attached by identifying its root with any core vertex; repeated attachments and empty attachments are allowed. All vertices are labelled and carry one of the states \(\{0,1,2\}\). All sites update simultaneously: a site in state \(1\) becomes \(2\), a site in state \(2\) becomes \(0\), and a site in state \(0\) becomes \(1\) iff at least one neighbor is currently in state \(1\), otherwise remaining \(0\). A configuration is *initially primitive-three* when \(U^3x=x\) but \(Ux\ne x\). This does not count states that enter a three-cycle only after a transient. Source multiplicities refer only to paths of the core, not tree edges.

## Proof
**1. Classification of states of primitive period three.** For a single site in a state of temporal period dividing three, either its state is constantly zero or it traverses \(0\to1\to2\to0\) at every three steps. Indeed, an occurrence of state \(1\) forces \(2\) and \(0\) in the next two steps and, by three-periodicity, another \(1\) thereafter. If no \(1\) occurs, a state \(2\) cannot recur periodically and the site stays zero. A permanently zero site cannot have a rotating neighbor, because that neighbor occupies state \(1\) at some time. Connectivity therefore implies that every nonzero three-periodic state rotates at all vertices. Its time evolution is the global cyclic color shift. It is valid exactly when each vertex has at least one neighbor whose color is one greater modulo three.

**2. Admissible words along paths.** Write \(x_0=u,x_1,\ldots,x_L=v\) for the vertices along one core path and denote the initial coloring by \(\sigma\); put \(\delta_j=\sigma(x_j)-\sigma(x_{j-1})\pmod3\), using representatives \(-1,0,+1\). At each internal site \(x_j\), the required successor-color neighbor exists exactly when \(\delta_j=-1\) or \(\delta_{j+1}=+1\). Therefore every admissible sequence of length \(L\) has one of the two unique shapes
\[
(-1)^a(+1)^{L-a}\quad(0\le a\le L),\qquad
(-1)^a0(+1)^{L-1-a}\quad(0\le a\le L-1).
\]
There are \(2L+1\) such words. If the terminals differ by \(d=\sigma(v)-\sigma(u)\pmod3\), then the sum of the increments is \(d\), and precisely \(c_L(d)\) words have that terminal difference. The first edge has increment \(+1\) only in the all-\(+1\) word, so that path supplies the required successor-color neighbor to \(u\) precisely in that word; this word occurs in class \(d\) exactly when \(p_L(d)=1\). Likewise the last edge has increment \(-1\) only in the all-\(-1\) word, and this is a supplier to \(v\), counted by \(q_L(d)\). The two special words are distinct for \(L\ge2\).

**3. Two-terminal inclusion--exclusion.** Fix \(d\) and the color of \(u\). Every path independently selects one of its \(c_{L_i}(d)\) words. The polynomial \(W_{L_i,d}(s,t)\) marks the three disjoint possibilities: supplies neither terminal, supplies \(u\), or supplies \(v\). Both terminals must have at least one supplying path. Subtract the choices with no supplier at \(u\) and with no supplier at \(v\), and add their intersection. The color of \(u\) has three independent choices, yielding the boxed formula exactly. Each such coloring advances at all vertices under one update and returns after three; there are no shorter nonzero cycles in this class.

**4. Attached trees.** In any rotating state, a leaf in an attached tree must have its parent in the successor color. Inducting from leaves toward the attachment point shows that every child is uniquely forced to have its parent's color minus one modulo three. Such child colors cannot provide a successor-color neighbor to their parent; every nonroot tree vertex is already supported by its parent. Thus all attachment colors are forced and introduce no new choices or support at core vertices. The source polynomial is unchanged.

**5. Nonzero criterion and special cases.** A path supplies \(u\) only if its length is congruent to the common terminal difference \(d\), while a (different) path supplies \(v\) only if the negative of its length is congruent to \(d\). Hence \(P_3(G)>0\) requires distinct \(i,j\) with \(L_i+L_j\equiv0\pmod3\). Conversely, such a pair supplies both ends; each remaining path admits a valid word of the required terminal difference, since \(c_L(d)\ge1\) for \(L\ge2\). For equal length \(3h\), only \(d=0\) supports both roles, with \(c_{3h}(0)=2h+1\) and both special words available on each path. Inclusion--exclusion gives the stated second finite difference. If equal lengths are not divisible by three, the possible supplier roles require different terminal differences and cannot coexist. If there are precisely three paths of lengths \(3h_i\), applying the same product identity gives \(12\sum_i h_i\). These assertions prove every stated quantifier and boundary.

## Verification
Two independent standard-library Python programs are included as `verify_source.py` and `verify_dynamics.py`; their exact stdout is saved in `verify_source.out` and `verify_dynamics.out`. Execute `python verify_source.py` and `python verify_dynamics.py` from the directory containing the files. The first expands the source polynomial and enumerates direct neighbor-support colorings, comparing every source-multiplicity coefficient in 110 core topologies (3,325,212 candidate colorings). It also evaluates 49 equilateral formula cases. The second directly iterates the original Greenberg--Hastings update through three time steps over 44 core topologies (1,025,946 states) and checks four extra tree-attachment examples. Enumeration is finite evidence; the arbitrary-length theorem rests on the preceding proof.

## Relationship to prior work
Durrett and Steif (1991) establish the period-three *clock* mechanism for a lattice implementation; Durrett and Griffeath (1993) study excitable-media stable periodic objects and threshold/range phenomena. Gravner, Lyu and Sivakoff (first arXiv version October 24, 2016; Annals of Applied Probability 2018, Theorem 3) give circulation-based criteria and excitation rates on arbitrary finite connected graphs. Doba (2018, Sections 3, 6 and 7) likewise derives generic eventual-activity and cycle-density results. These works do not state the current labelled theta-graph **initial primitive-three source-multiplicity polynomial** in the inspected material. General circulation results distinguish eventual activity from immediate three-periodicity and do not themselves determine this full count.

Related exact computations for theta-graph long-run excitation rates, and for the primitive-three population on full subdivisions of arbitrary graphs, address different invariants. In the latter case some all-even-length theta graphs are indeed covered at the *unmarked total-count* level; the present claim does not assert novelty for that subcase alone. The two-terminal multivariate census, odd-arm cases and polynomial equilateral laws do not follow by simply reading those earlier claims. A separate one-hub bouquet formula concerns a cactus, not the two-pole theta core. See the accompanying review for residual priority limitations.

## Limitations
The theorem counts only configurations initially of primitive period three and their multiplicities of core source paths. Other periodic lengths, basin sizes, transient entry times, and different excitation thresholds are not classified. Attached trees are finite and meet the core only at their identified root. The result does not claim that the prerequisite successor-neighbor characterization or the general winding-number/circulation principle is new. Historical priority beyond the material inspected remains provisional, particularly for older excitable-media texts without accessible complete full text. Independent mathematical audit has not yet been performed.

## References
- R. Durrett and J. E. Steif, *Some Rigorous Results for the Greenberg--Hastings Model*, Journal of Theoretical Probability 4 (1991), 669--690. Full-text author-hosted PDF: https://sites.math.duke.edu/~rtd/reprints/paper66.pdf.
- R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, initial public arXiv posting March 22, 1993, arXiv:patt-sol/9303002; https://arxiv.org/abs/patt-sol/9303002.
- J. Gravner, H. Lyu and D. Sivakoff, *Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs*, first arXiv posting October 24, 2016, arXiv:1610.07320, and Annals of Applied Probability 28 (2018), 3324--3357; lawful full text: https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf.
- N. Doba, *The Time Evolution of a Greenberg--Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101--126; https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf.
