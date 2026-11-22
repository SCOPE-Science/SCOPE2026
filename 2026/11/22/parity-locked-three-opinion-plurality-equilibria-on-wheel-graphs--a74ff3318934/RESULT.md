# Parity-locked three-opinion plurality equilibria on wheel graphs

## Finding

For each integer \(n\ge3\), let \(W_n=K_1\vee C_n\) have one distinguished hub and \(n\) individually indexed rim vertices. Each vertex holds an opinion in \(\{0,1,2\}\). In parallel, it adopts the *unique* most frequent opinion of its open neighbors; when the maximum frequency is attained by two or more opinions it keeps its current opinion, even if that opinion is not among the maximizers.

**Theorem.** For odd \(n\), the only fixed configurations are the three unanimities. For even \(n=2m\ge4\), in addition to unanimity, every fixed configuration consists of a hub of one opinion and a cyclic rim word using exactly the other two opinions, each on exactly \(m\) vertices, with every monochromatic cyclic run of length at least two. All such words are fixed. The number of labelled fixed configurations is exactly

\[
E_{2m}=3\left(1+\sum_{r=1}^{\lfloor m/2\rfloor}\frac{2m}{r}\binom{m-r-1}{r-1}^{\!2}\right),\qquad E_{2m+1}=3\quad(m\ge1).
\]

Writing \(\varphi=(1+\sqrt5)/2\) and \(\sigma^2=(5+3\sqrt5)/40\), the even-subsequence has the precise asymptotic

\[
E_n\sim \frac{3\varphi^n}{\sqrt{2\pi\sigma^2n}}\qquad(n\longrightarrow\infty,\ n\ \mathrm{even}),
\]

whereas the odd-subsequence stays equal to three. This gives an exact parity-controlled transition between constant and exponentially numerous equilibria on the *same growing wheel family*. By comparison, with only two opinions, every wheel of this form has only the two unanimous fixed configurations.

## Assumptions and scope

The graphs are simple, loopless and undirected; the two rim neighbors of each rim vertex are distinct for \(n\ge3\). Colors are named, and vertices are indexed. Configurations differing by a rotation, reflection or permutation of the three opinion labels are counted separately. A fixed configuration means \(F(x)=x\) under one simultaneous update; the claim makes no statement about attraction basins, nonstationary recurrent orbits or convergence of arbitrary initial states.

The tie convention is important: a tie between two leading neighbor opinions, whether or not the incumbent is one of them, means no change. The hub is not frozen externally; its state is updated under exactly the same rule as a rim vertex.

## Proof

**1. No coexistence of the hub opinion and other opinions on the rim.** Relabel opinions so the hub holds \(0\). If a rim vertex holds \(0\) and another holds a nonzero opinion, connectedness of the rim cycle produces an adjacent \(0\)/nonzero pair. At the nonzero endpoint, two of the three neighbors are then opinion \(0\): the hub and the adjacent rim vertex. Hence its unique neighbor plurality is \(0\), and it cannot be fixed. Therefore any fixed state either has the entire rim equal to \(0\), yielding unanimity, or has no \(0\) on the rim.

**2. Local characterization of nonunanimous rims.** Suppose the rim contains only \(1\) and \(2\). For a rim site of color \(c\in\{1,2\}\), the neighbor colors are the hub's \(0\) and the colors of the two adjacent rim sites. If both rim neighbors have the other nonzero color, that color has unique plurality and the site changes. In all other cases either its own opinion has unique plurality (both rim neighbors equal \(c\)) or all three neighbor opinions differ (one rim neighbor of each nonzero color) and the site keeps \(c\) on a tie. Thus the rim is locally fixed exactly when it contains no cyclic monochromatic run of length one.

**3. The hub condition.** When the rim avoids \(0\), its opinion counts are \((0,a,b)\), with \(a+b=n\). The hub can retain \(0\) precisely if \(a=b\), since otherwise the larger of \(a,b\) is a unique maximizer. Hence \(n\) must be even and \(a=b=m\). Conversely these two local requirements imply that every vertex is fixed, proving the structural assertion.

**4. Exact enumeration.** For a balanced cyclic binary rim of length \(n=2m\), write \(r\) for the number of runs of \(1\), which also equals the number of runs of \(2\). Each run has length at least two, so \(1\le r\le\lfloor m/2\rfloor\). The ordered \(r\)-tuples of lengths of the \(1\)-runs form the positive compositions of \(m-r\) into \(r\) pieces; their number is \(\binom{m-r-1}{r-1}\), and similarly for the \(2\)-runs. Select the indexed beginning of one distinguished \(1\)-run in \(n\) ways. Every indexed cyclic word has \(r\) such choices, so its multiplicity is \(n/r\). The number of balanced rims is therefore

\[
B_{2m}=\sum_{r=1}^{\lfloor m/2\rfloor}\frac{2m}{r}\binom{m-r-1}{r-1}^{\!2}.
\]

There are three possible hub colors, and one unanimous configuration for each. This proves the exact formula.

**5. Sharp even-length asymptotic.** Consider the four ordered consecutive-pair states \(00,01,10,11\) of a binary rim word, and let an edge from \(ab\) to \(bc\) have weight \(z^c\) when the triple \(abc\) is not \(010\) or \(101\). In this state order the weighted transfer matrix is

\[
T(z)=\begin{pmatrix}1&z&0&0\\0&0&0&z\\1&0&0&0\\0&0&1&z\end{pmatrix},
\qquad
\det(\lambda I-T(z))=\lambda^4-(1+z)\lambda^3+z\lambda^2-z^2.
\]

The coefficient \([z^k]\operatorname{tr}(T(z)^n)\) counts indexed cyclic binary rim words of length \(n\), without singleton runs, with exactly \(k\) entries equal to one. At \(z=1\) the characteristic polynomial factors as \((\lambda^2-\lambda-1)(\lambda^2-\lambda+1)\). The matrix is primitive with simple dominant eigenvalue \(\varphi\). Denote its analytic continuation by \(\lambda(e^t)\). Implicit differentiation of the displayed characteristic equation gives

\[
\left.\frac{d}{dt}\log\lambda(e^t)\right|_{t=0}=\frac12,
\qquad
\left.\frac{d^2}{dt^2}\log\lambda(e^t)\right|_{t=0}=\frac{5+3\sqrt5}{40}=\sigma^2>0.
\]

The transfer is strongly connected, has a loop at \(00\) of weight one and a loop at \(11\) of weight \(z\). For any complex \(|z|=1\), equality in the Perron–Frobenius spectral-radius bound can occur only if the edge phases are a common vertex coboundary times a global phase. The two loops then force that global phase to be both \(1\) and \(z\), so \(z=1\). This proves aperiodicity of the additive count. Standard Fourier inversion with analytic perturbation of the simple Perron eigenvalue therefore yields the lattice local central limit estimate

\[
[z^{n/2}]\operatorname{tr}(T(z)^n)
\sim\frac{\varphi^n}{\sqrt{2\pi\sigma^2n}}
\quad(n\to\infty,\ n\text{ even}).
\]

The positive variance and strict spectral inequality exclude other leading saddle points. Multiplication by three and addition of the three unanimous states finish the asymptotic formula.

**6. Two-color comparison.** For only two available opinions, the argument in step 1 still forces the rim to be either entirely the hub opinion or entirely the opposite one. In the latter case, the hub sees a unique opposite neighbor majority and changes. Thus no nonunanimous fixed configuration is possible, and exactly two unanimities remain.

## Verification

`verify_direct.py` independently implements each vertex's open-neighbor frequency update, without using the run formula, and exhaustively checks all \(3^{n+1}\) initial states for every \(3\le n\le11\). It confirms the respective fixed-state counts \(3,15,3,21,3,39,3,93,3\).

`verify_transfer.py` computes balanced cyclic-word counts by polynomial closed walks on the four-state automaton and compares them with the run-composition formula for all even lengths \(4\le n\le80\). The source contains only standard-library Python and can be run independently with `python3 verify_direct.py` and `python3 verify_transfer.py`. Both programs check finite examples and are **not** substitutes for the all-length proof or the analytic local limit argument.

## Relationship to prior work

The 2012 preprint of Mossel, Neeman and Tamuz studies plurality/majority opinion aggregation and consensus on social networks, but does not derive a wheel-specific equilibrium count. Apt, de Keijzer, Rahn, Schäfer and Simon study neighbor-agreement coordination games, a relevant but *not equivalent* stationary rule. In such a game a player must choose a maximally represented neighbor color, whereas our incumbent-retaining plurality rule also freezes a hub with zero supporters when two other colors tie for the lead. Thus the fixed states counted here need not be pure Nash equilibria, and the coordination-game existence results do not imply our wheel enumeration. The later three-opinion analysis by Di Ianni studies different deterministic update prescriptions and computational complexity. Previously published binary-majority wheel fixed-point and two-cycle descriptions address only two colors; the extra balanced two-color rim surrounding an absent third-color hub cannot occur in that setting. Previously published ternary plurality classifications on other graph families do not imply a wheel result.

## Limitations

The theorem is restricted to exactly three available opinions and the specified incumbent-retaining tie rule. It counts immediate fixed configurations, not their attraction basins, all eventual periods or random-start fixation probabilities. The local central limit argument is standard transfer-matrix asymptotic analysis, not an independently formalized proof. Bibliographic and indexed searches found no statement covering the exact wheel result, but absence from those sources does not certify absolute historical novelty.

## References

1. E. Mossel, J. Neeman and O. Tamuz, *Majority Dynamics and Aggregation of Information in Social Networks*, first public version 2012-07-04, arXiv:1207.0893, https://arxiv.org/abs/1207.0893.
2. K. R. Apt, B. de Keijzer, M. Rahn, G. Schäfer and S. Simon, *Coordination Games on Graphs*, arXiv:1501.07388, https://arxiv.org/abs/1501.07388.
3. M. Di Ianni, *Three Majority-Based Deterministic Dynamics for Three Opinions*, AppliedMath (2025), https://doi.org/10.3390/appliedmath5040147.
4. Related published descriptions of synchronous binary-majority wheel equilibria and two-cycles are compared in the accompanying `REVIEW.md` and `AUDIT.json`.
