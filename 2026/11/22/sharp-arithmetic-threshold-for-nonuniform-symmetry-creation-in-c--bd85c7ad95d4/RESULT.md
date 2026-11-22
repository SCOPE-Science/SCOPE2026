# Sharp arithmetic threshold for nonuniform symmetry creation in cyclic majority dynamics

## Finding

Let \(n\ge3\), and let \(F_n\) be the synchronous binary three-neighbor majority cellular automaton on the indexed ring \(\mathbb Z/n\mathbb Z\):
\[
(F_nx)_i=\mathbf 1\{x_{i-1}+x_i+x_{i+1}\ge 2\}.
\]
A configuration \(x\) is *spatially asymmetric* if its least positive rotational period is \(n\), and *nonuniformly symmetric* if it is nonconstant and has least rotational period strictly smaller than \(n\). Let \(p_{\min}(n)\) be the least prime factor of \(n\).

**Theorem (sharp ring-length classification).** A spatially asymmetric \(x\) can evolve under \(F_n\) into a nonuniformly symmetric configuration at some positive time if and only if
\[
\boxed{\frac{n}{p_{\min}(n)}\ge6.}
\]
Equivalently, \(n\) has a proper positive divisor \(d\ge6\). Whenever the condition holds, such symmetry can first appear after **exactly one update**, and for every eligible divisor \(d\) there is an explicit one-step witness whose output has least spatial period \(d\).

The key stronger rigidity fact is: if a nonconstant output of least spatial period \(d\in\{2,3,4,5\}\) occurs as the image of any cyclic configuration (on any ring length divisible by \(d\)), then **every** such preimage is already \(d\)-periodic. Thus one-step creation of a new nonuniform rotational symmetry cannot first occur with such a short output period. Uniform outputs (least period one) are deliberately excluded: their symmetry can arise from asymmetric states on smaller rings.

## Assumptions and scope

All indices are taken modulo \(n\). The cellular automaton is exactly Wolfram's Rule 232, with simultaneous updates and a closed three-site neighborhood. A symmetry is a rotation of site indices; neither reflections nor binary complementation count as spatial rotations. Period always means **spatial**, not temporal, except where explicitly described as an update time. The theorem is an existence statement for at least one initial configuration, not an assertion that all asymmetric states become nonuniformly symmetric. The finite-state lemma is about arbitrary repeated nonconstant outputs of spatial period at most five, including outputs that have no preimage. The claimed threshold concerns *nonconstant* newly symmetric outputs, not the all-zero or all-one states.

## Proof

**1. Translation equivariance reduces all delayed creation to one step.** Let \(\sigma\) be the left rotation of the indexed ring. The local rule gives \(F_n\sigma=\sigma F_n\), so every rotational symmetry of an input persists at every later time. Suppose some asymmetric initial configuration first produces a nonconstant symmetric configuration \(y=F_n^t x\) at time \(t\ge1\). Its immediately preceding configuration \(z=F_n^{t-1}x\) is asymmetric: if \(z\) had a proper rotational period, then (as its output is nonconstant) the earlier forward orbit already contained a nonconstant symmetric state; a constant \(z\) would remain constant forever. Thus a necessary and sufficient classification of delayed *existence* is given by one-step asymmetric preimages of nonconstant symmetric outputs.

**2. Exact finite-state short-period rigidity.** Order the input-pair states as \(00,01,10,11\). For an output letter \(b\in\{0,1\}\), define the integer transition matrix \(A_b\) with entry \(A_b[(u,v),(v,w)]=1\) exactly when \(\operatorname{maj}(u,v,w)=b\), and all other entries zero. Directly from the eight local triples,
\[
A_0=\begin{pmatrix}
1&1&0&0\\0&0&1&0\\1&0&0&0\\0&0&0&0
\end{pmatrix},\qquad
A_1=\begin{pmatrix}
0&0&0&0\\0&0&0&1\\0&1&0&0\\0&0&1&1
\end{pmatrix}.
\]
For a length-\(d\) nonconstant output block \(w=w_0\cdots w_{d-1}\), put \(P_w=A_{w_0}\cdots A_{w_{d-1}}\), using **ordinary integer matrix multiplication** (so multiplicities of internal paths are retained). If the full output is the block \(w\) repeated \(m\ge1\) times, every indexed preimage is in bijection with a closed walk of length \(m\) in the directed *multi*graph with adjacency matrix \(P_w\). This is the standard overlapping-pairs correspondence: each edge records a length-\(d\) block of local input triples, and the closing edge enforces cyclic consistency.

The following finite statement is an exact exhaustive certificate. For every nonconstant binary word \(w\) of lengths \(d=2,3,4,5\): (i) every diagonal entry of \(P_w\) is at most one; (ii) no two distinct vertices are mutually reachable by positive-length directed paths in the support graph of \(P_w\). This is verified by the standalone `checker.py`, which constructs both matrices from the majority truth table and checks all \(2^d-2\) nonconstant blocks, without a stored list of favorable cases. It uses exact integer products and four-vertex Boolean transitive closure. Its independently reproducible complete tally is:

| \(d\) | Blocks tested | Blocks with a diagonal loop | Maximum diagonal trace | Violations of (i) or (ii) |
|---:|---:|---:|---:|---:|
| 2 | 2 | 2 | 1 | 0 |
| 3 | 6 | 0 | 0 | 0 |
| 4 | 14 | 6 | 1 | 0 |
| 5 | 30 | 20 | 1 | 0 |

For clarity on why this finite calculation establishes an *unbounded* statement: every positive-length closed walk of any length in a finite directed graph is contained in a strongly connected component. Condition (ii) makes every cyclic component a single vertex; condition (i) gives that vertex exactly one available one-block loop. Hence a closed walk of any length repeats one and the same length-\(d\) input block, forcing the input itself to be \(d\)-periodic. There is no extrapolation from finitely many ring lengths.

Consequently, if an asymmetric one-step preimage has nonconstant symmetric output of least period \(d\), then \(d\) cannot be 2, 3, 4, or 5. The output cannot have period 1 because it is nonconstant. Since \(d\mid n\) and \(d<n\), the ring has a proper divisor \(d\ge6\).

**3. Explicit one-step witnesses for every eligible divisor.** Conversely, suppose \(n=md\), \(m\ge2\), \(d\ge6\). Choose the period-\(d\) word
\[
w=000\underbrace{11\cdots1}_{d-3\text{ ones}}
\]
and put \(y=w^m\). Every zero and one run in \(y\) has length at least three, so each site has at least one agreeing neighbor and \(F_ny=y\). Its least rotational period is \(d\), because the unique run of three zeros within each block has a unique starting phase modulo \(d\).

Construct \(x\) from \(y\) by changing only the first copy's adjacent symbols at positions \(2,3\) from \(01\) to \(10\). Only updates at positions \(1,2,3,4\) can be affected, and their input triples (in that order) have majorities \(0,0,1,1\), exactly the original corresponding output bits. Every other neighborhood is unchanged from the fixed word \(y\). Thus \(F_nx=y\).

If a nonzero rotation fixed \(x\), equivariance would make it a period of \(F_nx=y\), so its shift would be a nonzero multiple of \(d\). But the modification occurs in only one of the \(m\ge2\) copies of \(w\), while all other copies remain intact, ruling out every such rotation. Thus \(x\) is asymmetric, \(y\) is nonuniformly symmetric, and the creation occurs at time one.

**4. Arithmetic equivalence.** A proper divisor of \(n\) is at most \(n/p_{\min}(n)\), with equality attained by removing the smallest prime factor. Therefore a proper divisor at least six exists if and only if \(n/p_{\min}(n)\ge6\), completing the proof.

## Verification

The dependency-free `checker.py` independently rebuilds both four-state matrices, tests every one of the \(52\) nonconstant target words of lengths \(2\) through \(5\), verifies both directed-graph conditions, and prints the exact four-row tally above. It additionally checks the explicit witnesses for \(6\le d\le30\), \(2\le m\le6\), confirming the output, its primitive period, and complete asymmetry of its predecessor in each of \(125\) instances. Finally, for every \(3\le n\le16\), it directly enumerates asymmetric input words until a valid witness is found, or exhausts all such inputs to confirm impossibility, matching the arithmetic criterion. Run `python3 checker.py` using only Python's standard library. The short-period matrix certificate and general closed-walk deduction, not the finite-ring witness tests, prove the infinite-size exclusion.

## Relationship to prior work

Banda, Caughman and Lehman (2026) prove that translation symmetries are irreversible under equivariant updates and enumerate symmetric configurations in arbitrary dimensions. That result supplies the monotonicity premise but **does not** specify when a particular nonlinear update first creates a nonuniform symmetry. Nakar and Ron (2022) analyze stable cells, temporal periodicity and transient behavior for one-dimensional majority automata; their classification concerns temporal attractors rather than the present first-appearance arithmetic.

Three closely relevant published Rule-232 research results provide exact one-step image counts, a full distribution of times to **temporal** periodicity, and the absence of transient predecessors of primitive temporal two-cycles at radius one. Their complete available statements and proofs were compared. None determines the short spatial-period preimage rigidity or the sharp \(n/p_{\min}(n)\) threshold, nor does its statement imply the present witness construction. The transfer-matrix method itself is standard and is not claimed as new. Earlier preimage-enumeration literature, especially Jen (1989), is a possible source of equivalent hidden special cases; priority is assessed only relative to inspected material.

## Limitations

The theorem is restricted to synchronous radius-one binary majority on cyclic rings with \(n\ge3\), and to creation of **nonuniform** spatial rotation symmetry. Constant-target entry, exact probabilities of creation, first-appearance time distributions for all initial states, larger radii, and noncyclic graphs are not classified. Finite computer calculations are used solely for an explicitly bounded, exhaustively stated 52-case matrix lemma and corroboration; the general quantifiers follow from the written graph argument. The result has not undergone independent mathematical validation, and the possibility of an equivalent formula implicit in older preimage-counting work is a residual originality risk.

## References

1. P. Banda, J. Caughman and T. Lehman, *Shift-Symmetric Configurations in \(d\)-Dimensional Cellular Automata: Enumeration, Bounds, Irreversibility, and Detection*, arXiv:2611.15751v1 (first publicly posted 2026-11-11), https://arxiv.org/abs/2611.15751 .
2. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972 (first publicly posted 2022-05-18), https://arxiv.org/abs/2205.08972 .
3. E. Jen, *Enumeration of preimages in cellular automata*, *Complex Systems* 3 (1989), 421–456, https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf . Historical comparison partially inspected via a later research discussion; its full paper was not re-read here.
