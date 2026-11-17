# One pendant leaf splits the stochastic-minority attractor of an odd clique without changing its population

## Finding
For each integer \(m\ge1\), form \(G_m\) by adjoining one pendant vertex \(\ell\) to a distinguished hub \(h\) of the complete graph \(K_{2m+1}\). Under uniformly asynchronous binary closed-neighborhood minority updating, with opinion retention on an exact tie, the transition chain has **exactly two recurrent communicating classes**. Every initial configuration reaches one of them almost surely. In each class, the hub and leaf have opposite, permanently fixed opinions; the clique has either \(m\) or \(m+1\) vertices of opinion \(1\).

Each class has \(\binom{2m+1}{m}\) configurations; hence the total recurrent population is \(2\binom{2m+1}{m}\), precisely the population of the **single** recurrent class on the unperturbed odd clique. The two recurrent classes are nonabsorbing and each has a uniform stationary measure. Its one-step transition matrix has exact spectral gap
\[
\gamma_m=\frac{1}{2m+2}.
\]
More precisely, set \(d_j=\binom{2m}{j}-\binom{2m}{j-1}\), with \(\binom{2m}{-1}=0\), and \(e_m=\binom{2m}{m}-\binom{2m}{m-1}\). The full within-class transition spectrum comprises
\[
1-\frac{j}{2m+2}\quad\text{and}\quad 1-\frac{2m+1-j}{2m+2}
\qquad(0\le j\le m-1),
\]
with multiplicity \(d_j\) for each of these two values, together with \(1-\frac{m}{2m+2}\) of multiplicity \(e_m\). All these multiplicities are nonnegative; values that happen to coincide are counted additively. The unperturbed odd clique has gap \(1/(2m+1)\), by its known middle-level hypercube dynamics. Thus the leaf changes the number of recurrent classes, rather than the total number of recurrent states, and freezes two designated opinions forever once recurrence is reached.

## Assumptions and scope
The vertex set is \(\{h\}\cup R\cup\{\ell\}\), with \(|R|=2m\). The vertices in \(\{h\}\cup R\) form a complete graph; the only neighbor of \(\ell\) is \(h\). Opinions are \(0\) and \(1\). At each integer time a single vertex is selected independently and uniformly from the \(2m+2\) vertices. It adopts the strictly less frequent opinion in its **closed** neighborhood; at equal frequencies it retains its old opinion. Distinct labelled configurations are counted separately. A recurrent class means a closed irreducible communicating class of this finite transition matrix. The spectral gap means \(1-\lambda_2\), with \(\lambda_2\) its second-largest (real) eigenvalue on one recurrent class; no global unique stationary distribution is asserted.

For \(b\in\{0,1\}\), define \(\mathcal C_b\) as the configurations satisfying \(h=b\), \(\ell=1-b\), and \(\sum_{v\in\{h\}\cup R}\sigma_v\in\{m,m+1\}\). Each is a recurrent class.

## Proof
**Step 1: all configurations can reach the asserted set.** Let \(k\) count opinion-\(1\) vertices in the clique. Whenever an ordinary vertex \(v\in R\) is selected, its closed neighborhood is the entire odd clique of order \(2m+1\). Thus, if \(k<m\), a selected ordinary zero changes to one; if \(k>m+1\), a selected ordinary one changes to zero; if \(k=m\), only ordinary zeros can change; and if \(k=m+1\), only ordinary ones can change. First select \(\ell\). Its two-vertex closed neighborhood makes its opinion opposite that of \(h\), unless already opposite, in which case it stays so. Then choose ordinary vertices, keeping \(h\) unselected, until \(k\in\{m,m+1\}\). Whenever a change is required, a suitable ordinary vertex exists, even if \(h\) is of the overrepresented or underrepresented opinion. This is a finite permitted path into \(\mathcal C_0\cup\mathcal C_1\) from every initial state.

**Step 2: closure and irreducibility.** Inside \(\mathcal C_b\), the leaf already disagrees with its only neighbor and never changes. The hub's closed neighborhood contains the whole clique and the leaf. If \(b=1\), its opinion-\(1\) count is \(k\in\{m,m+1\}\), and the hub is strictly in the minority or tied; if \(b=0\), that count is \(k+1\in\{m+1,m+2\}\), and the hub is tied or in the minority. Hence the hub never changes. Ordinary updates only alternate between clique counts \(m\) and \(m+1\). For \(b=1\), the set \(S\subseteq R\) of ordinary opinion-\(1\) vertices changes by adding one element from size \(m-1\) to size \(m\), or deleting one element in the reverse direction. For \(b=0\), complement all the opinions and obtain the same graph. Therefore each induced transition graph is the inclusion graph between ranks \(m-1\) and \(m\) of the Boolean lattice on \(2m\) elements. That graph is connected: two sets of the same rank are linked by repeatedly exchanging one element through the other rank, and sets in adjacent ranks also connect. Each class has nontrivial transitions for every \(m\ge1\).

Since both sets are closed and strongly connected, and every state has a positive-probability path to their union, no other closed communicating class exists. Finiteness implies eventual entrance into that union almost surely. By Pascal's identity, the size of either class is \(\binom{2m}{m-1}+\binom{2m}{m}=\binom{2m+1}{m}\). The two classes give the asserted total population.

**Step 3: stationary law and exact spectrum.** An edge of the inclusion graph is traversed by flipping one ordinary vertex. Each direction has probability exactly \(1/(2m+2)\) in a step. Hence the uniform probability measure on either finite connected class is stationary and reversible; all other selected updates contribute self-loops. Let \(L\) be the unweighted combinatorial Laplacian of the inclusion graph. The actual transition matrix is \(P=I-L/(2m+2)\).

Write \(N=2m\), and let \(V_r\) be the real vector space on the \(r\)-subsets of \([N]\). Define the up-incidence map \(U_r:V_r\to V_{r+1}\) by \((U_rf)(A)=\sum_{B\subset A,\,|B|=r}f(B)\), and put \(D_{r+1}=U_r^{\!*}\). Directly counting the coefficient of each set gives
\[
D_{r+1}U_r-U_{r-1}D_r=(N-2r)I.
\]
For \(r<N/2\), this proves that \(U_r\) is injective, since its squared norm differs from \(\|D_rf\|^2\) by \((N-2r)\|f\|^2\). Let \(H_j=\ker D_j\), of dimension \(d_j\) for \(0\le j\le m-1\). The recursively propagated subspaces \(U_{m-2}\cdots U_j H_j\) form an orthogonal direct-sum decomposition of \(V_{m-1}\). Repeated use of the commutator shows that \(D_mU_{m-1}\) acts on the propagated \(H_j\) by the scalar
\[
(m-j)(m+1-j).
\]
Relative to \(V_{m-1}\oplus V_m\), the inclusion-graph Laplacian is
\[
L=\begin{pmatrix}(m+1)I&-D_m\\-U_{m-1}&mI\end{pmatrix}.
\]
For each singular value \(\sqrt{(m-j)(m+1-j)}\) of \(U_{m-1}\), the associated two-dimensional block has eigenvalues \(j\) and \(2m+1-j\), each of multiplicity \(d_j\). The remaining \(e_m=\dim V_m-\dim V_{m-1}\) directions in \(\ker D_m\) give eigenvalue \(m\). This yields the complete stated spectrum of \(P\). The smallest positive Laplacian eigenvalue is \(1\): it is the \(j=1\) eigenvalue for \(m\ge2\), and the extra \(m=1\) eigenvalue for \(m=1\). Therefore \(\gamma_m=1/(2m+2)\).

For the unperturbed odd clique, its recurrent class is the inclusion graph between ranks \(m\) and \(m+1\) of the \((2m+1)\)-cube, as in the published clique classification. The same incidence calculation gives Laplacian gap \(1\) and a one-vertex-choice denominator \(2m+1\); hence its transition gap is \(1/(2m+1)\).

## Verification
Two independent standalone Python checkers are included. The first builds the actual single-vertex closed-neighborhood update graph from scratch, enumerates all labelled states for \(m=1,2,3,4\), computes terminal strongly connected components and compares them with the two formula-defined classes. It examined \(16+64+256+1024=1360\) states and checked the absence of absorbing configurations in the recurrent classes. The second independently constructs the Boolean-lattice incidence graph, computes exact symbolic Laplacian characteristic polynomials for \(m=1,2,3\), and compares them with the proposed full spectrum. All checks passed. Execute `python check_exhaustive.py` and `python check_spectrum.py` in a Python environment with SymPy installed; captured outputs are included. Exhaustive finite testing supports, but does not replace, the all-\(m\) proof.

## Relationship to prior work
Rouquier, Regnault and Thierry, *Stochastic Minority on Graphs*, arXiv:1011.5119v1 (first public version 2010-11-23), Definition 2 and Theorem 19, provide the precise minority rule and show that odd complete graphs have one recurrent class of size \(2\binom{2m+1}{m}\). Their clique argument does not describe the effect of attaching a leaf, nor a two-class decomposition or the spectral data for the altered graph. The present statement preserves the known unperturbed count while making the graph change destroy communication between two equal-size pieces.

Qiu, Qiu, Jiang and Shen, *On the Spectrum of Middle-Cubes*, arXiv:0911.0126v1 (2009-11-01), explicitly characterize spectra of two middle layers of odd-dimensional cubes using Johnson graph eigenvalues. The incidence-operator technique used here is classical and its spectral algebra is **not** presented as an independently novel general graph-spectrum theorem. That source concerns the regular two-middle-level graph of an odd cube, rather than the stochastic update graph on a pendant-clique or the unbalanced adjacent ranks of an even cube. The claimed new statement is the complete dynamical classification and its exact perturbation comparison.

## Limitations
The proof treats the uniformly chosen, single-site, binary closed-neighborhood rule and exactly one pendant vertex on odd cliques; it does not assert identical behavior for parallel updates, open neighborhoods, multiple leaves, or even cliques. The global chain is not irreducible, so there is no globally unique stationary measure or global mixing time; spectral gaps refer only to either recurrent class. A separate absorption-time distribution or basin-probability formula is not determined. Earlier unindexed work on antiferromagnetic single-spin dynamics with one leaf might cover an equivalent special case; the literature comparison does not establish exhaustive historical priority. No independent scientific audit has been performed.

## References
1. J.-B. Rouquier, D. Regnault and E. Thierry, *Stochastic Minority on Graphs*, arXiv:1011.5119v1, 2010-11-23, https://arxiv.org/abs/1011.5119. Relevant material: Definitions 1–3, energy reversibility, Theorem 19 and its proof.
2. K. Qiu, R. Qiu, Y. Jiang and J. Shen, *On the Spectrum of Middle-Cubes*, arXiv:0911.0126v1, 2009-11-01, https://arxiv.org/abs/0911.0126. Relevant material: Theorem 1 and the Johnson-incidence argument in Section 2.
