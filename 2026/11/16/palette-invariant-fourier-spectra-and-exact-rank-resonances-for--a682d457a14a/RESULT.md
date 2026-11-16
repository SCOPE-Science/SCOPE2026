# Palette-invariant Fourier spectra and exact rank resonances for cactus colourings

## Finding

Let \(H\) be any finite abelian group of order \(q\ge3\), and let \(G\) be any finite connected simple cactus graph, including the one-vertex graph. Write \(e\) for its number of bridge blocks and \(\ell_1,\ldots,\ell_b\ge3\) for its cycle-block lengths. Colour the vertices properly using elements of \(H\). On \(H^{V(G)}\), let \(T_G\) be counting convolution by the indicator of all proper colourings, with the unnormalized Fourier convention defined below.

**Complete signed-spectrum law.** The entire multiset of Fourier multipliers of \(T_G\), including signs and multiplicities, depends only on \(q,e,\{\ell_1,\ldots,\ell_b\}\), not on the isomorphism type of \(H\), the attachment pattern of the blocks, or any orientation of their edges. Define the bridge list \(\mathcal E_q\) to contain \(q-1\) once and \(-1\) exactly \(q-1\) times. Define the cycle list \(\mathcal C_{q,\ell}\) by taking all \(q^{\ell-1}\) words \((s_1,\ldots,s_\ell)\) over \(q\) symbols with the first symbol fixed and recording
\[
 c_q(s)=\frac{(-1)^\ell}{q}\sum_{a=1}^q (1-q)^{m_a(s)},
 \qquad m_a(s)=|\{i:s_i=a\}|.
\]
Every such value is an integer. The nonzero or zero balanced multiplier list is exactly the multiplicative Cartesian list
\[
 q\,\mathcal E_q^{\times e}\prod_{j=1}^b\mathcal C_{q,\ell_j},
\]
where products mean all products with multiplicity, not ordinary arithmetic products of lists. Precisely \(q^{|V(G)|}-q^{|V(G)|-1}\) additional multipliers are zero because of global colour translation.

**Exact cancellation and rank.** For \(\ell\ge3\) set
\[
 Z_q(\ell)=
 \begin{cases}
 \displaystyle\frac{\ell!}{(t+1)!(t!)^{q-1}},&\ell=qt+1,\quad t\ge1,\\
 0,&\text{otherwise}.
 \end{cases}
\]
Then \(Z_q(\ell)\) is exactly the number of *balanced* zero Fourier multipliers on the labelled cycle \(C_\ell\), and
\[
 \boxed{\operatorname{rank}T_G=q^e\prod_{j=1}^b\bigl(q^{\ell_j-1}-Z_q(\ell_j)\bigr).}
\]
In particular, all \(q^{|V(G)|-1}\) balanced modes survive if and only if no cycle length belongs to \(\{q+1,2q+1,3q+1,\ldots\}\). This is sharp: a single resonant cycle forces additional nullity. For example, at \(q=5\), \(C_6\) has precisely \(360\) balanced Fourier zeros and convolution rank \(2765\), whereas all its other \(3125-360\) balanced modes survive.

## Assumptions and scope

Graphs are finite, undirected, simple, connected and cactus: each graph edge lies in at most one simple cycle, equivalently its blocks are individual bridges or simple cycles. Both vertices and edges are labelled, and proper means adjacent vertices have unequal colours in the same set \(H\); no group-operation constraint is imposed on properness. The character group \(\widehat H\) is written multiplicatively, and
\[
 W_G(\chi)=\sum_{c:V\to H\atop c\text{ proper}}\prod_{v\in V}\chi_v(c_v),\quad \chi\in\widehat H^V.
\]
The convolution operator is \((T_Gf)(x)=\sum_y1_{\mathrm{proper}}(y)f(x-y)\), so its Fourier multipliers agree with \(W_G\), up to replacing every character by its inverse; this inversion permutes the complete multiset. Rank is over \(\mathbb C\). The empty product is one; the one-vertex case has rank one.

## Proof

**1. Translation and block splitting.** Translating every colour by the same \(h\in H\) preserves properness. Thus \(W_G(\chi)=0\) unless \(\prod_{v\in V}\chi_v=1\) as a character. Call such a frequency balanced. If \(G\) is the one-vertex amalgam of connected graphs \(G_1,G_2\), there is a *unique* factorization of every balanced global frequency into balanced frequencies on both pieces: inherit the characters at all non-shared vertices, and determine the two cut-vertex characters by the separate balance conditions. Conditional on the shared vertex colour, each balanced piece sum is constant by diagonal translation. Consequently
\[
 W_G(\chi)=\frac{W_{G_1}(\chi^{(1)})W_{G_2}(\chi^{(2)})}{q}.
\]
The frequencies on each constituent block run freely and independently over their balanced frequency sets. Induction on the block-cut tree proves the complete multiset is the product of the *normalized* block multiplier lists, with one overall factor \(q\). The identity \(|V|=1+e+\sum_j(\ell_j-1)\) counts its balanced frequencies.

**2. Bridge multiplier.** For \(K_2\), balance requires the characters to be \((\eta,\eta^{-1})\). Summing over all distinct colours gives \(q(q-1)\) for \(\eta=1\), and \(-q\) for each nontrivial \(\eta\). Dividing by \(q\) gives \(\mathcal E_q\).

**3. Cycle multiplier.** Orient the edges of a simple labelled cycle cyclically, and write
\[
 1_{x\ne y}=\frac1q\sum_{\eta\in\widehat H}b(\eta)\eta(x-y),\qquad
 b(1)=q-1,\quad b(\eta)=-1\ (\eta\ne1).
\]
Expanding each edge factor and summing over vertex colours enforces one character conservation equation at each vertex. Those equations are soluble exactly when the input frequency is balanced. The edge characters then form one coset of the diagonal character subgroup: \((\eta s_1,\ldots,\eta s_\ell)\), indexed by \(\eta\in\widehat H\). The underlying potential \((s_i)\) is uniquely pinned by \(s_1=1\), and the map from balanced vertex frequencies to pinned potentials is bijective. Hence
\[
 W_{C_\ell}(\chi)=\sum_{\eta\in\widehat H}\prod_{i=1}^\ell b(\eta s_i)
 =(-1)^\ell\sum_{\eta\in\widehat H}(1-q)^{m_\eta(s)}.
\]
In particular this is an integer divisible by \(q\): the sum is invariant modulo \(q\) under replacing each base \(1-q\) by one. The right side depends only on the multiplicities of the \(q\) symbols, so its *signed* distribution does not depend on the group law.

**4. Classification of every cancellation.** Write \(a=q-1\ge2\), and suppose \(\sum_{j=1}^q(-a)^{m_j}=0\). Set \(t=\min_jm_j\) and \(d_j=m_j-t\). Then \(\sum_j(-a)^{d_j}=0\). Modulo \(a\), the number \(r\) of zero exponents is divisible by \(a\), and \(1\le r\le q=a+1\), forcing \(r=a\). Exactly one exponent remains, say \(d\ge1\), and its equation is \(a+(-a)^d=0\), which holds exactly when \(d=1\). Conversely this pattern plainly cancels. Thus the only vanishing occupancy vectors have \(q-1\) counts equal to \(t\) and one count equal to \(t+1\), so \(\ell=qt+1\). For \(\ell\ge3\) the integer \(t\) must be at least one. The number of unpinned words with this occupancy pattern is \(q\ell!/((t+1)!(t!)^{q-1})\): choose the exceptional symbol and arrange the multiset. Translation of *all* potential symbols by a common group element acts freely; each orbit has exactly one word with \(s_1=1\). Dividing by \(q\) proves the displayed formula for \(Z_q(\ell)\).

**5. Rank.** All bridge multipliers are nonzero. There are \(q^{\ell-1}\) balanced characters per cycle, of which exactly \(Z_q(\ell)\) vanish. Independent block contributions multiply and the remaining globally unbalanced characters vanish. Their nonzero count is the stated rank, with the if-and-only-if support criterion.

## Verification

Two independent, standalone exact-integer programs accompany the result. `verify_formula.py` independently enumerates all pinned potential words at \(q=3,4,5,6\), compares the zero counts to the factorial formula through cycle length ten where feasible, checks block-product histograms, and verifies the explicit small-cycle ranks. `verify_transform.py` directly enumerates proper colourings and computes full group Fourier transforms by separate fourth-root-of-unity integer-pair arithmetic and Walsh character signs for \(C_4\) and \(C_2\times C_2\). It checks the complete signed histograms for a triangle-square bouquet and for a two-square bouquet. Both programs passed; their finite checks are illustrations, not substitutes for the all-graph proof above.

## Relationship to prior work

Classical finite-group graph Fourier theory and Tutte/Potts expansions supply the edge-character calculation. Goodall's archived graphical Fourier work develops Fourier methods for graph-colouring and flow enumeration, whereas Babson and Beck study enumerative group-valued graph colourings. The separate ideas of balanced character support and block factorization are elementary; the claimed result is their combination into a complete, group-law invariant *signed coefficient multiset* for every cactus and the exact all-palette cycle cancellation/rank classification. Existing first-coordinate colouring-sampling results concern restricted Gram systems rather than these full convolution multipliers. Special cases for ternary or four-colour cycles, and for bridge-triangle block graphs, do not imply the stated all-palette all-cycle classification.

## Limitations

The assertion concerns finite *abelian* palette groups, counting convolution on all vertex-coordinate colourings, and connected cactus graphs. It is not claimed for arbitrary graphs with overlapping cycles. No uniqueness beyond the inspected literature and accessible records is asserted. An independent human or external audit has not been performed. The theorem determines Fourier ranks and full coefficient lists but does not assert a closed-form sorted histogram or optimal inverse norm for arbitrary cactus graphs.

## References

- A. Goodall, *Parity, eulerian subgraphs and the Tutte polynomial*, arXiv:0707.2306 (public 2007-07-16), https://arxiv.org/abs/0707.2306.
- A. Goodall, *Fourier Analysis on Finite Abelian Groups: Some Graphical Applications*, in *Surveys in Combinatorics* (2007); accessible manuscript https://www.researchgate.net/publication/266250848_Fourier_Analysis_on_Finite_Abelian_Groups_Some_Graphical_Applications.
- E. Babson and M. Beck, *Counting Group Valued Graph Colorings*, arXiv:1204.1283 (public 2012-04-05), https://arxiv.org/abs/1204.1283.
