# Frozen alphabet phases and exact first-entry laws for NOR dynamics on Kautz digraphs

## Finding

Fix integers \(q\ge2\) and \(d\ge1\). Give every vertex of the directed Kautz word graph \(K(q,d)\) a Boolean state, updated synchronously by the NOR of its \(q\) incoming neighbors. The recurrent set consists of precisely \(q+1\) fixed configurations and one primitive two-cycle. Every initial configuration reaches it within \(d\) updates, and this bound is sharp for every \(q,d\).

More strongly, take independent Bernoulli\((p)\) initial states and set
\[
 p_0=p,\qquad p_{t+1}=(1-p_t)^q.
\]
Write \(T\) for the first update at which the full configuration is periodic, including \(T=0\) for an initially periodic state. Then, for every integer \(0\le t<d\), setting \(h_t=q^{d-t-1}\) and \(m_t=(q+1)h_t\),
\[
 \boxed{\Pr_p(T\le t)=p_t^{m_t}+(1-p_t)^{m_t}
 +(q+1)p_t^{h_t}(1-p_t)^{q h_t}.}
\]
For \(t\ge d\), this probability is \(1\); exact first-entry probabilities are consecutive cumulative differences. The probability of eventual absorption in a fixed configuration is
\[
 \boxed{\Pr_p(\mathrm{fixed})=(q+1)p_{d-1}(1-p_{d-1})^q.}
\]
Each fixed configuration has exactly the same basin probability, \(p_{d-1}(1-p_{d-1})^q\).

There is a critical initial-bias distinction as \(d\to\infty\), with \(q\) fixed. Let \(p_*\in(0,1)\) uniquely satisfy \(p_*=(1-p_*)^q\). Then
\[
 \lim_{d\to\infty}\Pr_p(\mathrm{fixed})=
 \begin{cases}
 (q+1)p_*^2,&p=p_*,\\
 0,&p\ne p_*.
 \end{cases}
\]
This is an exact isolated survival peak: at the critical bias, frozen alphabet phases retain positive basin probability despite exponentially increasing graph size; at every other fixed bias, the uniform-zero/uniform-one oscillator attracts asymptotically all configurations.

## Assumptions and scope

Let \(A\) be an alphabet of \(q+1\) distinct symbols. The vertices of \(K(q,d)\) are words \(w=w_1\cdots w_d\in A^d\) with \(w_i\ne w_{i+1}\) for each adjacent pair. The graph has \((q+1)q^{d-1}\) vertices. It has an arc from \(b w_1\cdots w_{d-1}\) into \(w_1\cdots w_d\) for each \(b\in A\setminus\{w_1\}\), including the interpretation for \(d=1\) as the directed complete graph without loops. There are no self-inputs or extra edges. Explicitly,
\[
 (F x)(w_1\cdots w_d)
 =\prod_{b\in A\setminus\{w_1\}}
 \left(1-x(b w_1\cdots w_{d-1})\right).
\]
The product is a Boolean product of zeros and ones. All sites update simultaneously. The probabilistic claims require independent, identically distributed initial states, not an arbitrary correlated initialization. The limiting statement fixes \(q\) and \(p\) while the word length \(d\) grows; it does not claim a uniform limit in \(p\) or in \(q\).

## Proof

**1. Word-prefix collapse.** For each integer \(0\le t\le d-1\), the state \(F^t x(w)\) depends only on the first \(d-t\) symbols of \(w\). Indeed this is immediate for \(t=0\); if \(F^t x(w)\) depends only on the prefix of length \(d-t\), applying the stated NOR rule shows that \(F^{t+1}x(w)\) depends only on the prefix of length \(d-t-1\). Consequently \(F^{d-1}x(w)=z(w_1)\) for some vector \(z\in\{0,1\}^{A}\). The subsequent update reduces exactly to
\[
 (Hz)(a)=\prod_{b\ne a}(1-z(b)).
\]
If \(z\) has no ones, \(Hz\) is all ones. If it has exactly one one, \(Hz=z\). If it has at least two ones, \(Hz\) is all zeros. Therefore the only periodic vectors for \(H\) are its \(q+1\) one-hot fixed vectors and the all-zero/all-one two-cycle, and every vector becomes periodic after at most one update. Lifting those vectors to the word graph gives the stated recurrent configurations. There are no other periodic states: any periodic orbit is permuted bijectively by \(F\), hence its image under \(F^{d-1}\) is the same orbit, whose states must belong to this first-letter subspace. Thus \(T\le d\) for every initial state.

The bound is sharp. Every prescribed first-letter output vector at time \(d-1\) can be realized: the \(q+1\) input trees described below are disjoint, and a NOR tree of any finite height can attain each Boolean output by choosing its leaves. Specify exactly two ones in the output vector and zero elsewhere. Since \(q+1\ge3\), this is neither a one-hot fixed vector nor a uniform vector; the configuration at time \(d-1\) is not periodic, but its next iterate is uniform zero. Thus its first periodic entry is exactly update \(d\).

**2. Disjoint predecessor trees.** Fix \(0\le t\le d-1\), and write \(\ell=d-t\). For a word prefix \(u\) of length \(\ell\), the common value of \(F^t x\) on all vertices starting with \(u\) is the output of a full \(q\)-ary NOR tree of height \(t\) with leaves
\[
 \{x(vu):\ |v|=t,\ vu\text{ is an admissible Kautz word}\}.
\]
There are exactly \(q^t\) leaves. Distinct admissible prefixes \(u\) give disjoint sets of initial vertices, since their final \(\ell\) symbols differ. These sets partition all initial sites. If the initial states are independent Bernoulli\((p)\), the reduced prefix values are independent, identically distributed Bernoulli\((p_t)\), where \(p_{t+1}=(1-p_t)^q\) is the exact NOR-tree recursion. There are \(m_t=(q+1)q^{\ell-1}\) such reduced values, partitioned into \(q+1\) first-symbol blocks, each of size \(h_t=q^{\ell-1}\).

A configuration in the prefix subspace is recurrent precisely when all reduced values are zero, all are one, or exactly one first-symbol block is all one and every other block all zero. The three mutually exclusive event types have probabilities \((1-p_t)^{m_t}\), \(p_t^{m_t}\), and \((q+1)p_t^{h_t}(1-p_t)^{q h_t}\). This proves the cumulative first-entry law. At \(t=d-1\), all blocks have size one. Precisely the one-hot vectors produce fixed states, proving the fixed-basin probability formula and the equality of the individual fixed basins.

**3. Exact integer census.** For uniform initial bits, let \(B_0=1\), \(S_0=2\), and recursively define
\[
 B_{t+1}=(S_t-B_t)^q,\qquad S_{t+1}=S_t^q.
\]
Then \(B_t\) is the number of leaf assignments making a height-\(t\) NOR tree output one, and \(S_t=2^{q^t}\) counts all leaf assignments. For \(0\le t<d\), the exact number of labelled initial states with \(T\le t\) is
\[
 B_t^{m_t}+(S_t-B_t)^{m_t}
 +(q+1)B_t^{h_t}(S_t-B_t)^{q h_t}.
\]
At \(t=d\), the count is \(2^{(q+1)q^{d-1}}\). The basin of each fixed configuration has size \(B_{d-1}(S_{d-1}-B_{d-1})^q\), and the remaining states enter the unique two-cycle. This gives a finite exact all-depth orbit and entrance census without enumerating all configurations.

**4. The critical-bias spike.** The map \(f(p)=(1-p)^q\) is strictly decreasing and has a unique fixed point \(p_*\in(0,1)\). To exclude other interior two-cycles, set \(g=f\circ f\). For \(0<x<1\), with \(s=1-x\),
\[
 \frac{g(x)}{x}=J(s),\qquad J(s)=\frac{(1-s^q)^q}{1-s}.
\]
The sign of \(J'(s)\) equals the sign of \(\sum_{j=0}^{q-1}s^j-q^2s^{q-1}\). Dividing that expression by \(s^{q-1}\) gives \(\sum_{j=0}^{q-1}s^{-j}-q^2\), a strictly decreasing function on \((0,1)\) with limits \(+\infty\) and \(q-q^2<0\). Thus \(J\) first increases and then decreases; \(J(0)=1\) and \(J(1)=0\). It follows that \(J(s)=1\) has exactly one solution in \((0,1)\). Since \(g(p_*)=p_*\), this is the only interior fixed point of \(g\). Moreover \(g(x)<x\) for \(0<x<p_*\), while \(g(x)>x\) for \(p_*<x<1\). Hence even iterates \(g^k(p)\) converge to zero for \(p<p_*\), to one for \(p>p_*\), and stay at \(p_*\) if \(p=p_*\); odd iterates converge to the complementary endpoint or stay at \(p_*\). Substituting in the fixed-basin probability proves the stated limit, including \(p=0,1\).

## Verification

The standalone standard-library program `kautz_verify.py` directly constructs each Kautz digraph, iterates NOR on all Boolean states of the five cases \((q,d)=(2,1),(2,2),(2,3),(3,1),(3,2)\), and independently computes the cumulative shell and fixed-basin formulas using exact integer arithmetic. The numbers of initial states in the successive first-entry shells are, respectively:

- \((2,1)\): \(5,3\) out of \(8\).
- \((2,2)\): \(5,50,9\) out of \(64\).
- \((2,3)\): \(5,968,1422,1701\) out of \(4096\).
- \((3,1)\): \(6,10\) out of \(16\).
- \((3,2)\): \(6,3768,322\) out of \(4096\).

The same program checks that these finite cases have exactly \(q+1\) recurrent fixed states and the single universal two-cycle, and checks 4000 deterministic-seed random states on the 36-vertex \((q,d)=(3,3)\) instance. Execute `python3 kautz_verify.py` with Python 3. The finite checks corroborate, but do not replace, the all-size argument in the proof.

## Relationship to prior work

Kautz word networks and their connection to de Bruijn graphs are classical; their definition is not new (Lavault, archived 2010). The general Boolean graph-dynamics literature allows complicated periods on arbitrary directed graphs and does not by itself supply the present special-network orbit census (Aledo, Martínez and Valverde, 2015, Sections 3.2 and 4.1). A closely relevant predecessor by the same authors studies several special digraphs, including simple directed paths, cycles, stars and arborescences (2012 conference contribution and 2013 journal work). Its full journal text was not accessible during the source comparison, leaving a bounded historical-coverage risk.

For perspective, the corresponding full-word de Bruijn incoming-NOR network has a unique recurrent uniform oscillator: allowing repeated adjacent symbols removes the first-letter frozen modes. The new mathematical content here is the complete Kautz recurrent classification, exact first-entry law, labelled basin census and isolated critical-density fixed-phase survival. The NOR-tree recursion alone is elementary and is not presented as a new probability transform.

## Limitations

The result uses directed incoming-neighbor NOR, not an undirected neighborhood NOR, not outgoing edges, not NAND, and not a rule that automatically reads the site's own state. It concerns finite word graphs and independent equal-bias initial bits. The asymptotic frozen probability is a fixed-\(q\), fixed-\(p\), increasing-\(d\) statement, with no claim about the critical scaling window for \(p\) varying with \(d\). No claim of exhaustive historical priority is made; plausible unindexed or inaccessible work could contain an equivalent result. Independent external scientific verification has not yet occurred.

## References

1. C. Lavault, *Interconnection Networks: Graph- and Group-Theoretic Modelling*, archived version 1 on 2010-03-08, HAL identifier `hal-00461923`, https://hal.science/hal-00461923. Structural definition and motivation for Kautz word graphs.
2. J. A. Aledo, S. Martínez and J. C. Valverde, *Parallel dynamical systems over special digraph classes*, *International Journal of Computer Mathematics* **90** (2013), 2039–2048, https://doi.org/10.1080/00207160.2012.742191; author version reported online 2012-10-26.
3. J. A. Aledo, S. Martínez and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, *Journal of Applied Mathematics* (2015), Article 594294, first published 2015-03-24, https://doi.org/10.1155/2015/594294.
4. J. A. Aledo, S. Martínez and J. C. Valverde, *Dynamics of some Parallel Dynamical Systems over Digraphs*, in *Proceedings of CMMSE 2012*, pp. 49–53, https://www.unioviedo.es/bayon/osh/Proceedings-Vol-1-cmmse-2012.pdf. Accessible extended abstract and stated classes; not a substitute for the inaccessible journal full text.
