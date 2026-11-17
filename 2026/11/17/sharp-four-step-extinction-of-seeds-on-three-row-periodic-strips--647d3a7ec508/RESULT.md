# Sharp four-step extinction of Seeds on three-row periodic strips

## Finding

For every integer \(n\ge3\), Seeds (B2/S) on the fully periodic, labelled Moore grid \(\mathbb Z_3\times\mathbb Z_n\) is **uniformly nilpotent**: \(F_n^4(x)=0\) for every initial binary configuration \(x\). The exact smallest global extinction exponent is
\[
 e(n)=\begin{cases}2,&n=3,\\3,&n=4,\\4,&n\ge5.\end{cases}
\]
Consequently the all-dead state is the unique fixed configuration and unique temporal attractor, and there are no nontrivial periodic states of any temporal period.

## Assumptions and scope

Coordinates are \((r,i)\in\mathbb Z_3\times\mathbb Z_n\), with \(n\ge3\). Moore neighbors are the eight **distinct** sites at offsets \((\delta_r,\delta_i)\in\{-1,0,1\}^2\setminus\{(0,0)\}\), reduced modulo the two circumferences. The update is simultaneous. A dead site becomes alive exactly when two neighbors are alive; a live site always dies. Both directions are periodic; this is **not** the vertically open three-row strip.

For a binary state \(x\), set \(w_i(x)=\sum_{r\in\mathbb Z_3}x_{r,i}\). Thus \(0\le w_i\le3\). Call \(e(n)\) the least nonnegative integer \(k\) for which \(F_n^k\) sends every state to the all-dead state.

## Proof

**Column-weight factor.** A dead cell in column \(i\) has as its eight neighbors all three cells in columns \(i-1\) and \(i+1\) and the other two cells in its own column. Its number of living neighbors is therefore \(s_i=w_{i-1}+w_i+w_{i+1}\). If \(s_i=2\), all currently dead cells of this column are born and its living cells die, so its new weight is \(3-w_i\). Otherwise the new column is empty. Hence the entire column-weight evolution obeys
\[
 (Tw)_i=\begin{cases}3-w_i,&w_{i-1}+w_i+w_{i+1}=2,\\0,&\text{otherwise.}\end{cases}
\]
This identity is exact for every binary state, and no information about positions of the live cells within a column is needed to predict future column weights.

**Two local finite lemmas.** On a finite word of column weights, define \(\mathcal U(a_0,\ldots,a_{m-1})=(\tau(a_{j-1},a_j,a_{j+1}))_{1\le j<m-1}\), where \(\tau(u,v,w)=3-v\) when \(u+v+w=2\), and zero otherwise. Complete base-four enumeration of all \(4^5=1024\) words of length five gives the central coordinate of \(\mathcal U^2(a)\) with frequencies \(963\) at zero, \(18\) at one, \(0\) at two and \(43\) at three. Complete enumeration of all \(4^6=4096\) words of length six gives **zero** occurrences where the two coordinates of \(\mathcal U^2(a)\) are both one. Both finite lemmas are proved by the complete explicit loops in `verify_weight_cones.py`, with deterministic comparisons against these integers; they quantify over all local initial words, not sampled trajectories.

**Uniform extinction.** After two steps, all weights belong to \(\{0,1,3\}\), and adjacent columns cannot both have weight one. If a column is nonzero after the third step, its preceding three-weight sum must equal two, necessarily using two weights of one and a weight zero. The two ones cannot be adjacent, so this triple must be \((1,0,1)\), and the central weight is zero. The third-step output at that column is therefore three. Thus every column at time three is either empty or completely alive. A full column contains no dead cells and so dies at the next step; for an empty column, its two neighboring column weights are each zero or three, so the number of living neighbors of a dead cell is in \(\{0,3,6\}\), never two. Every column is empty at time four, proving \(F_n^4=0\) for every \(n\ge3\).

**Sharpness.** For \(n=3\), direct enumeration of the \(4^3=64\) column-weight words establishes \(T^2=0\) and the word \((2,0,0)\) needs two steps. For \(n=4\), enumeration of all \(4^4=256\) weight words establishes \(T^3=0\); the word \((1,1,0,0)\) has a nonzero second iterate. For each \(n\ge5\), take \(w=(1,1,1,0,\ldots,0)\), realizable by exactly one live cell in each of three adjacent columns. Direct application of \(T\), with cyclic indexing, gives a column of weight three at time three (column index one) for all \(n\ge5\). Thus no smaller uniform exponent works. The two short-ring exhaustive claims are independently corroborated by a bit-level enumeration of all \(2^9\) and \(2^{12}\) binary configurations, respectively.

## Verification

`verify_weight_cones.py` exhaustively checks the two decisive local lemmas (\(1024+4096\) base-four words), the full three-step central-output distribution over \(4^7=16384\) local words, all cyclic weight states for lengths three and four, and sharp witnesses through length nineteen. Its recorded output is `weight_output.txt`.

`verify_binary.cpp` separately computes the original eight-neighbor birth rule for every labelled binary state at circumferences three through six (a total of \(299520\) states). Its `binary_output.txt` reports exact extinction-time histograms and checks the sharp exponents. Compile with `g++ -O2 -std=c++17 verify_binary.cpp -o verify_binary` and execute `./verify_binary`; run the first checker with `python3 verify_weight_cones.py`. The scripts require no external data or optional packages.

## Relationship to prior work

The Seeds rule was studied by Brian Silverman and named by Mirek Wójtowicz. Eppstein's *Growth and Decay in Life-Like Cellular Automata* (arXiv:0911.2890v1, 15 November 2009), especially Section 4, proves that every B2 rule has a growth pattern on the **infinite plane**, not a nilpotency result on a period-three-width torus. Martínez, Seck-Tuoh-Mora and Zenil, *Computation and Universality: Class IV versus Class III Cellular Automata* (arXiv:1304.1242v1, 4 April 2013), Section 2.3, discuss Seeds and Diffusion Rule gliders and computation on an infinite plane but do not supply this all-circumference finite-strip extinction theorem. The known Seeds oscillator and spaceship catalogue addresses patterns in ordinary planar space, not the present torus.

This theorem exploits the exact three-row cyclic Moore-neighbor collapse. Its conclusion does not follow from the absence of survivals, since Seeds on the infinite plane has nontrivial oscillators. Searches of relevant primary literature and indexed mathematical findings did not identify an equivalent width-three nilpotency theorem; this is a best-knowledge priority assessment rather than a proof of worldwide novelty.

## Limitations

The proof concerns exactly three periodic rows and at least three periodic columns. It does not extend to vertically open strips, larger heights, random updating, or a general classification of Seeds on arbitrary tori. It makes no claim about primitive periods in those other geometries. A 1996 Silverman article was identified bibliographically but its complete original text was not available for direct comparison; unindexed archival material remains a priority risk. Independent expert validation has not been performed.

## References

- D. Eppstein, *Growth and Decay in Life-Like Cellular Automata*, arXiv:0911.2890v1, posted 2009-11-15, https://arxiv.org/html/0911.2890v1 .
- G. J. Martínez, J. C. Seck-Tuoh-Mora, H. Zenil, *Computation and Universality: Class IV versus Class III Cellular Automata*, arXiv:1304.1242v1, posted 2013-04-04, https://arxiv.org/abs/1304.1242 .
- LifeWiki, *OCA:Seeds* (B2/S rule and catalogued planar oscillators), https://conwaylife.com/wiki/OCA:Seeds .
