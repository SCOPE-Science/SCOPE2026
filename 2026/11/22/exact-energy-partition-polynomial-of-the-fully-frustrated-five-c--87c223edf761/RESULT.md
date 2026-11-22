# Exact energy partition polynomial of the fully frustrated five-cube

## Finding

On the binary five-cube \(Q_5\), let the canonical sign on the edge \(x\leftrightarrow x\oplus e_i\), for coordinates \(i=0,\ldots,4\), be
\[
\varepsilon(x,i)=(-1)^{\sum_{j<i}x_j}.
\]
For every spin assignment \(\sigma:\{0,1\}^5\to\{-1,+1\}\), define its signed agreement score
\[
S(\sigma)=\sum_{\{x,y\}\in E(Q_5)}\varepsilon_{xy}\sigma_x\sigma_y,
\qquad Z_5(t)=\sum_{\sigma}t^{S(\sigma)}.
\]
The **complete exact finite-temperature partition polynomial** is
\[
\boxed{\begin{aligned}
Z_5(t)={}&10240(t+t^{-1})^8(t^3+t^{-3})^8\\
&+45056(t+t^{-1})^{10}(t^3+t^{-3})^5(t^5+t^{-5})\\
&+10240(t+t^{-1})^{12}(t^3+t^{-3})^2(t^5+t^{-5})^2.
\end{aligned}}
\]
All \(2^{32}\) labeled spin assignments are counted, once each. The coefficient at the maximum score \(S=32\) equals \(10240\). The next score \(S=30\) has coefficient \(126976\). Since \(Q_5\) has \(80\) edges, the number of negative edges after switching is \((80-S)/2\). Hence exactly \(5120\) distinct fully frustrated edge signings have the minimum \(24\) negative edges: the two global-opposite spin assignments produce the same signing. The minimum frustration count \(24\) itself was already known; the claims here are the *complete counting polynomial* and its new multiplicity consequences.

## Assumptions and scope

The cube is the labeled graph on five-bit vectors, and each coordinate \(i\) represents one undirected edge whenever \(x_i=0\). Spins are unrestricted independent \(\pm1\) variables at its \(32\) distinct vertices; there is no external field. Every square has sign product \(-1\), since changing the smaller of two distinct coordinates reverses the sign contribution of the larger. All fully frustrated edge signings are switching equivalent because the square boundaries span the cube's cycle space. Therefore the partition polynomial does not depend on the chosen fully frustrated gauge. The statistical-mechanical energy is \(E=-S\) for unnormalized coupling strength one, and the physical partition function at inverse temperature \(\beta\) is \(Z_5(e^\beta)\). This is an exact finite-graph statement, not a thermodynamic-limit claim.

## Proof

**1. Eliminate one bipartition.** Partition the vertices into \(16\) even-weight vertices \(X\) and \(16\) odd-weight vertices \(Y\). For an arbitrary even-side spin assignment \(u\in\{-1,+1\}^X\), put
\[
H_y(u)=\sum_{x\sim y}\varepsilon_{xy}u_x
\qquad (y\in Y).
\]
The signed even-to-odd incidence matrix \(B\) satisfies \(B^TB=5I_{16}\): its diagonal entries are five, and for two distinct odd vertices any common even neighbors correspond to a square, whose two path-sign products are opposite. Consequently,
\[
\sum_{y\in Y}H_y(u)^2=5\sum_{x\in X}u_x^2=80.
\]
Each odd field lies in \(\{\pm1,\pm3,\pm5\}\). Let \(a,b,c\) respectively count the odd vertices with field magnitudes \(1,3,5\). From
\[
a+b+c=16,\qquad a+9b+25c=80,
\]
it follows that \(b+3c=8\) and \(a=8+2c\).

**2. Classify the possible five-fields.** For an odd vertex \(y\), let \(E_y\) be the event \(|H_y(u)|=5\) among the \(2^{16}\) even-side assignments. It forces the five neighboring spins to coincide, after multiplication by their incident signs, and permits a common choice of sign. Hence \(|E_y|=2\cdot2^{11}=4096\). If distinct odd vertices \(y,z\) have Hamming distance two, their two common even neighbors lie in a negative square. Forcing both five-fields would require the two corresponding length-two path-sign products to agree, a contradiction. Thus \(E_y\cap E_z=\varnothing\) whenever \(d_H(y,z)=2\).

If \(d_H(y,z)=4\), their even neighborhoods are disjoint, so \(|E_y\cap E_z|=2^2\cdot2^{16-10}=256\). Among the \(16\) odd vertices there are \(16\cdot5/2=40\) unordered distance-four pairs. No three distinct odd vertices can be pairwise distance four: two distinct weight-four difference vectors differ in exactly two coordinates, not four. Therefore no triple intersection exists; every even assignment has \(c\in\{0,1,2\}\).

**3. Inclusion-exclusion.** Let \(N_c\) be the number of even assignments producing exactly \(c\) five-fields. The pair count gives \(N_2=40\cdot256=10240\). Counting individual events gives
\[
N_1+2N_2=16\cdot4096=65536,
\]
so \(N_1=45056\), and subtracting from \(2^{16}=65536\) gives \(N_0=10240\). The three possible field-multiplicity profiles \((a,b,c)\) are consequently
\[
(8,8,0),\quad(10,5,1),\quad(12,2,2)
\]
with multiplicities \(10240,45056,10240\), respectively.

**4. Reinsert the odd spins.** Conditional on \(u\), the score equals \(\sum_{y\in Y}\sigma_yH_y(u)\). Summing the independent odd spins thus contributes
\[
\prod_{y\in Y}(t^{H_y(u)}+t^{-H_y(u)})
=(t+t^{-1})^a(t^3+t^{-3})^b(t^5+t^{-5})^c.
\]
Multiplication by the three \(N_c\) values proves the boxed identity for every spin assignment, with no computational or asymptotic assumption.

**5. Optimizers and first excitation.** For fixed even spins, the largest possible score is the sum of the absolute odd fields, equal to \(32-2c\). Only \(c=0\) can reach \(32\), and for each such assignment the odd spins are uniquely forced by field signs; hence there are exactly \(10240\) maximizing spin assignments. To attain score \(30\), either a \(c=0\) profile flips exactly one of its eight unit fields, giving \(8\cdot10240\) states, or a \(c=1\) profile aligns all fields, giving \(45056\) states. Their total is \(126976\). Since every switched edge sign is \(\varepsilon_{xy}\sigma_x\sigma_y\), a connected graph has exactly two switching spin assignments per resulting edge signing, namely global opposites. The \(10240\) optimum spin assignments therefore yield \(5120\) optimal edge signings.

## Verification

Run the standalone `verify.py` with Python 3. It tests all \(80\) signed square constraints, the exact orthogonality identity, and independently enumerates all \(65536\) even-side spin assignments. It checks the three field profiles, constructs the Laurent polynomial by exact integer convolution, verifies total mass \(2^{32}\), score support and symmetry, and separately spot-checks the \(80\)-edge score directly. A passing execution terminates with `VERIFY_OK`. The unrestricted identity and optimizer count follow from the preceding proof, independently of the finite replay.

## Relationship to prior work

Wang's 2026 study proves \(F_{r^2+1}=(r^2-r+1)2^{r^2-1}\), so \(F_5=24\), and establishes the signed adjacency identity underpinning the mean-square bound. It does not state the present complete partition polynomial or the numbers of five-cube optimal signings or first excited states. The minimum \(F_5=24\) and an explicit optimal configuration were in fact known already to Derrida, Pomeau, Toulouse and Vannimenus (1979), who also identified the \(16+16\) ground-state internal-field split. Neither this earlier result nor Wang's sharpened general theorem counts all 32-spin energy levels. These were the actual new questions considered here; the prior minimum is not claimed anew. Minamoto's 2026 work concentrates on extremal square-free edge sets and fully frustrated configurations for dimensions six, seven and eight, rather than an exact five-dimensional spin partition polynomial. Parisi and Potters' 1995 article develops mean-field and TAP-equation analysis in the infinite-dimensional fully frustrated hypercube limit and not an exact 32-spin energy census. No stronger equivalent finite-dimensional formula was identified in the consulted sources or indexed mathematical records, but historical priority is provisional.

## Limitations

The formula is for \(Q_5\) with zero magnetic field only. It gives neither an all-dimensional partition formula nor full geometry/orbit classification of maximizing switchings. A complete novelty audit over nonindexed early statistical-mechanics reports was not possible; any such source could modify the historical originality claim. The finite checker is corroboration rather than independent certification.

## References

1. Lujia Wang, *The frustration index of fully frustrated hypercubes*, arXiv:2611.14906v1 (2026-11-11), https://arxiv.org/html/2611.14906v1.
2. Minamo Minamoto, *C4-Free Subgraphs of the Hypercubes Q6, Q7, and Q8: Odd Squares, Fully Frustrated Models, and Computational Structure*, arXiv:2603.29127v5 (2026), https://arxiv.org/html/2603.29127v5.
3. Giorgio Parisi and Marc Potters, *Mean-Field Equations for Spin Models with Orthogonal Interaction Matrices*, arXiv:cond-mat/9503009v2 (1995), https://arxiv.org/html/cond-mat/9503009v2.
4. B. Derrida, Y. Pomeau, G. Toulouse and J. Vannimenus, *Fully frustrated simple cubic lattices and the overblocking effect*, Journal de Physique 40 (1979), 617–626, https://www.lps.ens.fr/~derrida/PAPIERS/1979/f-frustr-79.pdf.
