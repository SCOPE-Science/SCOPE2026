# Constant-probability quadratic avalanches on a rooted chain of triangles

## Finding

For every integer \(k\ge2\), consider the triangle-chain graph and sandpile dynamics below. One added grain at the distal articulation vertex causes, with **exact probability \(1/9\)** under the uniform recurrent measure, an avalanche of the **maximum possible** number of individual vertex topplings:

\[
\max T_k=2k^2+k-1,\qquad
\Pr(T_k=2k^2+k-1)=\frac19.
\]

There are exactly \(3^k\) recurrent stable configurations. The maximum is attained for precisely \(3^{k-2}\) of them, characterized by a purely local condition on the last two triangular blocks. The exact mean is

\[
\mathbb E[T_k]=\frac{2k^2+k}{3}.
\]

Thus quadratic total-toppling avalanches have a nonvanishing, exactly computable probability, even though all nonsink degrees are at most four and the graph is a one-dimensional chain of triangles.

## Assumptions and scope

Fix \(k\in\mathbb Z\) with \(k\ge2\). The undirected simple graph \(C_k\) has vertex set \(\{v_0,\ldots,v_k,w_1,\ldots,w_k\}\) and, for every \(1\le i\le k\), exactly the three edges \(v_{i-1}v_i\), \(v_{i-1}w_i\), and \(v_iw_i\). The unique dissipative sink is \(v_0\). Every nonsink vertex \(x\) has an integer height \(h(x)\) in the stable range \(0\le h(x)<\deg(x)\), and a toppling of unstable \(x\) sends one grain along each incident edge, with grains reaching the sink removed. The \(2k\) nonsink vertices are \(v_1,\ldots,v_k,w_1,\ldots,w_k\); \(\deg(v_i)=4\) for \(1\le i<k\), \(\deg(v_k)=2\), and \(\deg(w_i)=2\). Each avalanche adds exactly one grain at \(v_k\) and stabilizes. Its size counts **individual topplings, including repeated topplings**, not distinct toppled vertices or first-wave cells.

The sample space is the set of all stable recurrent configurations with the uniform measure. Recurrent means the stationary recurrent class of the usual one-sink sandpile group; standard burning and recurrent-class uniqueness properties apply. No thermodynamic or arbitrary-drive assertion is made.

## Proof

### 1. Exact recurrent-state parametrization

For \(1\le i\le k\), choose a code \(s_i\) from

\[
A=(1,1),\quad B=(1,0),\quad C=(0,1).
\]

If \(s_i=(a_i,b_i)\), assign heights

\[
h(w_i)=b_i,\qquad
h(v_i)=\begin{cases}2+a_i,&i<k,\\a_i,&i=k.\end{cases}
\]

These are stable. To apply Dhar's burning test, burn the sink \(v_0\) first and proceed toward the opposite end. After \(v_{i-1}\) burns, \(w_i\) can burn before \(v_i\) exactly if \(b_i=1\), because its one remaining neighbor in its triangle is \(v_i\). For \(i<k\), \(v_i\) can burn before \(w_i\) exactly if \(a_i=1\): it then has height three and precisely three unburned neighbors. If \(w_i\) burns first, \(v_i\) can subsequently burn even when \(a_i=0\), because only its two neighbors in the next triangular block remain unburned. At the terminal block \(i=k\), the same two alternatives hold with thresholds one and zero instead of three and two. Thus a block admits complete burning exactly when at least one of \(a_i,b_i\) is one. Since none of the vertices strictly beyond \(v_i\) can burn before \(v_i\), no blocked \((0,0)\) block can be rescued from its far side. The criterion is necessary and sufficient for all blocks. Exactly \(3^k\) recurrent states result; uniform recurrent states correspond to independent uniform letters in \(\{A,B,C\}\).

### 2. Exact maximal odometer

Let \(L\) be the reduced graph Laplacian (rows and columns indexed by nonsinks). Define a nonnegative integer function \(U\) by

\[
U(v_i)=\begin{cases}2i,&1\le i<k,\\2k-1,&i=k,\end{cases}
\qquad U(w_i)=2i-1\quad(1\le i\le k).
\]

A direct calculation at every vertex gives the exact identity

\[
L U=e_{v_{k-1}}+e_{v_k}+e_{w_k}.
\]

Take the all-\(A\) recurrent configuration \(h^A\). Adding a grain at \(v_k\) and subtracting \(LU\) gives

\[
h^A+e_{v_k}-LU=h^A-e_{v_{k-1}}-e_{w_k}.
\]

This is stable and recurrent: the last two letters change from \(A,A\) to \(C,B\), while all earlier letters remain \(A\). By uniqueness of the recurrent stable representative in each reduced-Laplacian equivalence class, this is the actual stabilization of \(h^A+e_{v_k}\). As the reduced Laplacian is invertible, the actual odometer equals \(U\). Therefore

\[
T_k(h^A)=\sum_{i=1}^{k-1}2i+(2k-1)+\sum_{i=1}^{k}(2i-1)=2k^2+k-1.
\]

Every recurrent configuration \(h\) is coordinatewise at most \(h^A\). Sandpile least-action monotonicity, applied to the same single-site addition, shows its odometer is coordinatewise at most \(U\). Hence the above mass is the **global** maximum on the recurrent state space.

### 3. Exact maximizing condition and probability

Suppose a recurrent \(h\) has maximum total toppling mass. Coordinatewise odometer domination and nonnegativity force every odometer coordinate to equal \(U\). The final configuration must then equal

\[
h+e_{v_k}-LU=h-e_{v_{k-1}}-e_{w_k}.
\]

This must be stable and recurrent, because addition sends a recurrent configuration to a recurrent configuration. At the penultimate block, subtracting from \(v_{k-1}\) turns the local code \(A\) into \(C\), \(B\) into the forbidden \((0,0)\), and \(C\) into a negative height. At the final block, subtracting from \(w_k\) turns \(A\) into \(B\), \(B\) into a negative height, and \(C\) into forbidden \((0,0)\). Consequently **both last letters must be \(A\)**. Conversely, if those last letters are \(A\), the displayed candidate final state is recurrent with final letters \(C,B\), and again uniqueness of the recurrent representative forces odometer \(U\), irrespective of preceding letters. Exactly \(3^{k-2}\) configurations attain the maximum, proving the exact probability \(3^{k-2}/3^k=1/9\).

### 4. Exact mean by stationarity and the Green function

Uniform recurrence is invariant under the addition operator at \(v_k\), which permutes recurrent configurations. Writing \(u\) for the random avalanche odometer and \(h'\) for its final configuration gives \(h'=h+e_{v_k}-Lu\). Expectations therefore yield \(L\mathbb E[u]=e_{v_k}\). The unique solution is

\[
\mathbb E[u(v_i)]=\frac{2i}{3},\qquad
\mathbb E[u(w_i)]=\frac{2i-1}{3}
\quad(1\le i\le k),
\]

verified directly by substitution into the reduced-Laplacian equation. Summing all \(2k\) coordinates establishes \(\mathbb E T_k=(2k^2+k)/3\).

## Verification

Two independent standard-library Python checks are supplied as `verify_enumeration.py` and `verify_linear.py`; run `python verify_enumeration.py` and `python verify_linear.py` from this document's directory. The first independently constructs the graph and runs full stabilization for every one of the \(3^k\) code configurations for \(1\le k\le9\); it checks maximal masses, maximizing-letter equivalence, and exact rational means, and separately exhausts **all stable configurations** through \(k=5\) with Dhar's burning algorithm to verify completeness of the recurrence classification. The second separately constructs reduced Laplacians, checks integer odometer and mean-potential identities through \(k=50\), checks exact rational inversions for \(k\le12\), and tests distinct random recurrent configurations through \(k=50\). Both scripts successfully replayed. Finite checks support, but do not replace, the preceding all-\(k\) proof.

## Relationship to prior work

Ali and Dhar's 1994 preprint and 1995 full study prove that decorated one-dimensional Abelian sandpiles can have quadratic toppling scales and non-simple avalanche scaling. Their examined models use alternating single and double bonds or diamond cells **joined by single bonds**, and their drive averages across sites; they do not state an exact fixed-terminal-source \(1/9\) maximal-event law for sequentially shared triangular articulation vertices. Thus quadratic scaling by itself is **not** asserted as new; the claim is the sharp complete finite-size maximum and exact local maximizing criterion with size-independent probability.

Gauthier's 2011 expanded-cactus analysis concerns a branched cactus, boundary dissipation, and primarily the number of **first-wave cells** rather than the total number of repeated topplings in a single path of triangles. Austin and collaborators' 2016 general avalanche-polynomial framework analyzes trees, cycles, wheels, and complete graphs; it does not present the claimed triangle-chain theorem. Fairchild and collaborators' 2016 fractal-graph analysis includes a *ring of triangles with separate sink connections*, but neither this graph nor this stationary distal single-addition observable. Another previously derived finite friendship graph has all triangles sharing the same hub and at most linear maximum mass in the compared protocol, so it cannot imply this quadratic path result.

## Limitations

The law is for precisely the specified finite simple graph, single sink, single fixed addition site, uniform recurrent stationary measure, and total individual topplings. It does not establish a complete avalanche-mass distribution, universal finite-size scaling on all cactus graphs, an infinite-volume stationary measure, or statistics for uniformly random deposition sites. Historical priority remains uncertain to the extent that obscure or inaccessible equivalent treatments may exist; checked literature supports the narrower originality comparison, not an exhaustive proof of novelty. Independent scientific review has not been performed.

## References

1. A. A. Ali and D. Dhar, *Breakdown of Simple Scaling in Abelian Sandpile Models in One Dimension*, first available 1994-12-16, https://arxiv.org/abs/cond-mat/9412085.
2. A. A. Ali and D. Dhar, *Structure of avalanches and breakdown of simple scaling in the Abelian sandpile model in one dimension*, Phys. Rev. E 52 (1995), https://doi.org/10.1103/PhysRevE.52.4804; publicly readable complete text: https://www.researchgate.net/publication/13325280_Structure_of_avalanches_and_breakdown_of_simple_scaling_in_the_Abelian_sandpile_model_in_one_dimension.
3. G. Gauthier, *Avalanche dynamics of the Abelian sandpile model on the expanded cactus graph*, first available 2011-10-28, https://arxiv.org/abs/1110.6263.
4. D. Austin, M. Chambers, R. Funke, L. D. García Puente and L. Keough, *The Avalanche Polynomial of a Graph*, first available 2016-05-09, https://arxiv.org/abs/1605.02713.
5. S. Fairchild, I. Haim, R. G. Setra, R. S. Strichartz and T. Westura, *The Abelian Sandpile Model on Fractal Graphs*, first available 2016-02-10, https://arxiv.org/abs/1602.03424.
