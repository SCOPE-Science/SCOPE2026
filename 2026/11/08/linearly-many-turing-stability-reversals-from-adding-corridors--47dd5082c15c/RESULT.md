# Linearly many Turing stability reversals from adding corridors

## Finding

For every integer \(n\ge 4\), there is a connected, unweighted network of \(n\) habitats and a succession of
\[
2\left\lfloor\frac{n-1}{3}\right\rfloor
\]
distinct corridor additions, with **no deletions**, such that the same two-species reaction–diffusion equilibrium is linearly stable, then unstable, then stable, and so on after **every** addition. The same local reaction laws and migration rates work for every \(n\). There is also a universal linear upper bound: no fixed two-species system with a single Turing-unstable spectral band can reverse strict linear stability more than \(2(n-1)\) times under monotone edge addition. Thus the maximal possible number of reversals grows as \(\Theta(n)\) for the displayed fixed model.

The four-habitat case is the minimum number of habitats that allows two successive additions from a connected graph; it already realizes stable–unstable–stable. This is a result about separate, fixed-topology linearizations, not the actual time-dependent dynamics during rewiring.

## Assumptions and scope

Let \(G=(V,E)\) be any simple connected undirected graph on \(n\) habitats. Each vertex supports prey \(u_i\ge0\) and predator \(v_i\ge0\), with the same local reactions at every habitat and undirected unit-weight migration. Take
\[
\begin{aligned}
\dot u_i&=u_i\bigl[(u_i-1)-5(v_i-1)-(u_i-1)^2\bigr]
 +\frac1{10}\sum_{j:\,ij\in E}(u_j-u_i),\\
\dot v_i&=v_i\bigl[\frac{39}{4}(u_i-1)-40(v_i-1)\bigr]
 +10\sum_{j:\,ij\in E}(v_j-v_i).
\end{aligned}
\]
The positive uniform equilibrium has \(u_i=v_i=1\) for every vertex. Nonnegativity is forward invariant: at a zero population coordinate the local term is zero and each migration inflow is nonnegative. The prey local term contains positive density feedback near equilibrium and a negative cubic regulation; this is an illustrative ecology-inspired kinetic system, not an empirically calibrated species pair.

We call the uniform state **linearly asymptotically stable** when all eigenvalues of the full \(2n\)-dimensional Jacobian have strictly negative real parts, and **linearly unstable** if at least one has strictly positive real part. No statement is made about global convergence, persistence of a pattern, or the stability of time-varying rewiring systems.

For a fixed \(n\), define a *strict reversal* along nested connected graphs \(G_0\subset G_1\subset\dots\) as an adjacent pair where the uniform state changes between these two strict statuses; marginal eigenvalues are not counted. Let \(M_n\) denote the maximum number of strict reversals along any one-edge-at-a-time addition sequence for the fixed local system above.

## Proof

### 1. A fixed exact spectral window

The reaction Jacobian at \((1,1)\) and the two diffusion coefficients are
\[
J=\begin{pmatrix}1&-5\\39/4&-40\end{pmatrix},
\qquad D=\operatorname{diag}(1/10,10).
\]
If \(L_G\) is the nonnegative graph Laplacian, the full linearization is \(I_n\otimes J-L_G\otimes D\). Because \(L_G\) is real symmetric, each Laplacian eigenvalue \(\ell\ge0\) yields a modal matrix \(J-\ell D\), whose trace and determinant are exactly
\[
\operatorname{tr}(J-\ell D)=-39-\frac{101}{10}\ell<0,
\qquad
\det(J-\ell D)=(\ell-5/2)(\ell-7/2).
\]
The elementary two-dimensional Hurwitz criterion now gives strict stability for \(\ell\notin[5/2,7/2]\), a positive real modal eigenvalue for \(5/2<\ell<7/2\), and a neutral zero eigenvalue at either endpoint. Every graph constructed below has integer eigenvalues and avoids both endpoints. The uniform mode \(\ell=0\) is stable.

### 2. A family with one independent instability switch per pair of edges

Fix any \(n\ge4\), and uniquely write \(n=3k+r+1\) where \(k=\lfloor(n-1)/3\rfloor\ge1\) and \(r\in\{0,1,2\}\). Label one hub \(0\), partition \(3k\) leaves into triples \((a_i,b_i,c_i)\), and leave \(r\) additional singleton leaves. Initially join every leaf to the hub and add no other edge, making a star.

For \(i=1,\ldots,k\), consecutively add the edges \(a_i b_i\), then \(a_i c_i\), before moving to the next triple. Let \(G_s\) be the graph after \(s\) added edges, where \(0\le s\le2k\). Each \(G_s\) remains connected, every added edge is new and unit-weight, and all previous edges persist.

On the subspace of leaf vectors that sum to zero separately within a given triple and vanish elsewhere (including at the hub), the graph Laplacian acts as \(I_3+L_{H_i}\), where \(H_i\) is the induced graph of that triple. The two nonconstant eigenvalues within the triple are therefore
\[
\begin{array}{c|c|c}
\text{number of added internal edges}&H_i&\text{two eigenvalues}\;\\ \hline
0&\text{three isolated leaves}&(1,1)\\
1&\text{one edge plus an isolated leaf}&(1,3)\\
2&\text{three-vertex path}&(2,4).
\end{array}
\]
The orthogonal complement consists of the hub and vectors constant on each triple and on each extra singleton leaf. Its Laplacian eigenvalues are exactly \(0\), \(n\), and \(1\) with multiplicity \(k+r-1\): the all-ones vector has eigenvalue zero; a hub-versus-leaves vector has eigenvalue \(n\); and leaf group-constant vectors of total sum zero have eigenvalue one. This proves the **entire** Laplacian spectrum of every \(G_s\), with the correct count \(2+(k+r-1)+2k=n\).

At even \(s\), each processed triple is in state \((2,4)\) and each unprocessed triple is in state \((1,1)\); there is no eigenvalue in \((5/2,7/2)\). At odd \(s\), exactly one current triple is in state \((1,3)\), producing exactly one unstable Laplacian eigenvalue \(3\). All others lie in \(\{0,1,2,4,n\}\), outside the instability band. The uniform equilibrium is therefore linearly asymptotically stable for even \(s\) and unstable for odd \(s\), giving \(2k=2\lfloor(n-1)/3\rfloor\) successive reversals and a stable final topology.

### 3. Universal linear upper bound

Along *any* one-by-one addition of undirected edges, the Laplacian increment for an added link \(xy\) equals
\[
(e_x-e_y)(e_x-e_y)^{\mathsf T}\succeq0.
\]
Consequently the ordered eigenvalues \(\ell_1\le\dots\le\ell_n\) are nondecreasing from snapshot to snapshot by the Courant–Fischer principle. The smallest eigenvalue is always zero because connectedness is maintained. For each of the other \(n-1\) eigenvalue sequences, membership in the open interval \((5/2,7/2)\) occurs on at most one consecutive block of snapshots: the eigenvalue can enter the interval once and leave it once, but cannot reenter. Thus the number of changes of all such membership indicators together is at most \(2(n-1)\). A strict change of whole-system stability requires one or more of these indicators to change, hence
\[
2\left\lfloor\frac{n-1}{3}\right\rfloor\le M_n\le2(n-1).
\]
In particular \(M_n=\Theta(n)\). For \(n\le3\), a connected simple graph has at most one absent edge after taking a spanning tree, so two distinct successive edge additions—and hence stable–unstable–stable—are impossible. The displayed four-site star realizes the first possible example.

### 4. Robustness

All the exhibited Laplacian eigenvalues are integers in \(\{0,1,2,3,4,n\}\). The two spectral-window endpoints \(5/2\) and \(7/2\) lie strictly between \(2,3\) and \(3,4\) respectively, and the modal traces are strictly negative. Therefore every sufficiently small fixed perturbation of the local Jacobian and positive diffusion coefficients that retains these strict inequalities preserves **every** reversal in the construction, for any \(n\). This is a qualitative open-parameter phenomenon, not a knife-edge tuning of the kinetic parameters.

## Verification

The standalone `corridor_verifier.py` uses exact rational characteristic polynomials of the graph Laplacians and independently compares full \(2n\)-dimensional Jacobian eigenvalues for smaller cases. Run `python corridor_verifier.py` with Python, SymPy and NumPy. Its recorded replay verified 72 exact graph spectra for \(k=1,2,3,4\), \(r=0,1,2\), and all \(0\le s\le2k\); it also verified 24 independent full-Jacobian stability decisions for \(k=1,2\). The proof for arbitrary \(n\) is the invariant-subspace factorization above, not the finite numerical checks.

## Relationship to prior work

Hata, Nakao and Mikhailov (2014) establish the network Laplacian-modal framework and show dispersal can destabilize ecological networks, concentrating on three-species oscillatory Turing instability. Their full open-access article does not present an arbitrary-length monotone edge-addition construction for alternating stability of a fixed two-species system.

Mimar et al. (2019) explain how network connectivity can induce a two-species Turing instability; the accessible abstract and excerpts concern network pattern selection and topology, rather than the specific claimed \(\Theta(n)\) sequence. A complete-text priority comparison was not possible and remains a risk.

Van Gorder (2021) develops Turing criteria on evolving networks and discusses transient instabilities, including monotone changes of edge weights and repeated periodic topology changes. Those general criteria are consistent with the present static spectral calculation, but the inspected article does not explicitly give a sequence of strictly *adding distinct unweighted edges*, with fixed kinetic parameters, that produces arbitrarily many whole-system alternating stability reversals. The novelty asserted here is the exact scalable construction and linear upper/lower reversal bounds, **not** the classical Turing modal criterion, the possibility of topology-induced instability, or transient patterns in moving networks.

## Limitations

The result concerns linear stability at the same uniform equilibrium of a *separate autonomous model* for each frozen topology. Switching the graph in continuous time has memory effects and cannot be inferred to follow these instantaneous stability statuses. Nor does linear instability prove a stable nonlinear pattern, persistent species, actual extinction, or any conservation-management improvement. The synthetic positive model and equal corridor conductances are mathematical benchmarks, not calibrated ecological forecasts. The lower and upper linear bounds are not claimed to have matching optimal constants. Historical priority beyond examined material remains subject to independent review, especially unread complete texts of closely related topology studies.

## References

1. S. Hata, H. Nakao and A. S. Mikhailov, *Dispersal-induced destabilization of metapopulations and oscillatory Turing patterns in ecological networks*, Scientific Reports **4**, 3585 (2014). First public 2014-01-07. https://doi.org/10.1038/srep03585 . Full text https://pmc.ncbi.nlm.nih.gov/articles/PMC3882759/ .
2. S. Mimar, M. Mussa Juane, J. Park, A. P. Muñuzuri and G. Ghoshal, *Turing patterns mediated by network topology in homogeneous active systems*, Physical Review E **99**, 062303 (2019). https://doi.org/10.1103/PhysRevE.99.062303 ; preprint https://arxiv.org/abs/1903.03845 .
3. R. A. Van Gorder, *A theory of pattern formation for reaction–diffusion systems on temporal networks*, Proceedings of the Royal Society A **477**, 20200753 (2021). https://doi.org/10.1098/rspa.2020.0753 .
