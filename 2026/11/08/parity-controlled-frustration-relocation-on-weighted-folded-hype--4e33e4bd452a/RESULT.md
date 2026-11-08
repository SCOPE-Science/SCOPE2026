# Parity-controlled frustration relocation on weighted folded hypercubes

## Finding

For every integer \(d\ge2\), the anisotropic Ising Hamiltonian on a hypercube with an additional antipodal matching has an exact two-branch ground-energy law and a complete, finite list of zero-temperature spin configurations. Write
\[
J_*=\min_{1\le i\le d}J_i,\qquad I_*=\{i:J_i=J_*\},\qquad m=|I_*|,\qquad t=(-1)^dK.
\]
Then
\[
\boxed{E_{\min}=2^{d-1}\left(-\sum_{i=1}^dJ_i+\min\{t,2J_*-t\}\right).}
\]
The exact ground-state multiplicity is \(2\) for \(t<J_*\), \(2m\) for \(t>J_*\), and \(2(m+1)\) at equality. The configurations are specified explicitly below, with no additional ground states.

## Assumptions and scope

Let \(d\ge2\), and let \(V=\{-1,+1\}^d\). For each \(x\in V\), denote by \(x^{(i)}\) its neighbor obtained by flipping coordinate \(i\). Place spins \(\sigma_x\in\{-1,+1\}\) on \(V\). The coordinate couplings satisfy \(J_i>0\) and the antipodal coupling satisfies \(K\in\mathbb R\). Each undirected edge below is counted once:
\[
H(\sigma)=\sum_{i=1}^dJ_i\sum_{\{x,x^{(i)}\}}\sigma_x\sigma_{x^{(i)}}+K\sum_{\{x,-x\}}\sigma_x\sigma_{-x}.
\]
This is a finite classical, zero-field, zero-temperature model. The antipodal edges are distinct from the coordinate edges for \(d\ge2\). For \(S\subseteq[d]\), define the Boolean character \(\chi_S(x)=\prod_{i\in S}x_i\), with \(\chi_\varnothing\equiv1\). The full-parity character is \(\chi_{[d]}\).

The entire set of energy minimizers is
\[
\mathcal G=\begin{cases}
\{\pm\chi_{[d]}\},&t<J_*,\\
\{\pm\chi_{[d]\setminus\{i\}}:i\in I_*\},&t>J_*,\\
\{\pm\chi_{[d]}\}\cup\{\pm\chi_{[d]\setminus\{i\}}:i\in I_*\},&t=J_*.
\end{cases}
\]
Each listed configuration has zero total magnetization because its Boolean character has nonempty support (as \(d\ge2\)).

For positive \(K\), odd \(d\) gives \(t=-K<J_*\), hence exactly two unfrustrated Néel configurations. For even \(d\), the threshold lies at \(K=J_*\): below it every coordinate bond is antialigned and the antipodal matching is aligned; above it every antipodal bond is antialigned, while precisely one direction of weakest coordinate bonds is aligned. The two families coexist only at the threshold. For \(K<0\), the same theorem holds with \(t=(-1)^dK\); it is not necessary to regard the antipodal bond as antiferromagnetic.

## Proof

Define the symmetric weighted adjacency operator on functions \(f:V\to\mathbb R\) by
\[
(Af)(x)=\sum_{i=1}^dJ_i f(x^{(i)})+Kf(-x).
\]
Each edge is counted at both ends in \(\langle\sigma,A\sigma\rangle\), so \(H(\sigma)=\frac12\langle\sigma,A\sigma\rangle\). The characters form an orthogonal basis, each with squared norm \(2^d\). Flipping one coordinate multiplies \(\chi_S\) by \(-1\) exactly when that coordinate belongs to \(S\); antipodal inversion multiplies it by \((-1)^{|S|}\). Thus \(A\chi_S=\lambda_S\chi_S\), where
\[
\lambda_S=\sum_{i=1}^dJ_i(-1)^{\mathbf1_{i\in S}}+K(-1)^{|S|}.
\]
Put \(T=[d]\setminus S\), so that \(|S|=d-|T|\). Reorganizing gives
\[
\lambda_S=-\sum_{i=1}^dJ_i+2\sum_{i\in T}J_i+(-1)^{|T|}t.
\]
When \(|T|\) is even, the positive \(J_i\) make the unique least eigenvalue in this parity sector occur at \(T=\varnothing\), giving \(-\sum_iJ_i+t\). When \(|T|\) is odd, the least one occurs at \(T=\{i\}\) with \(J_i=J_*\), giving \(-\sum_iJ_i+2J_*-t\). Larger odd subsets have strictly greater eigenvalue; no other sectors compete. Therefore
\[
\lambda_{\min}=-\sum_iJ_i+\min\{t,2J_*-t\}.
\]
For every spin configuration, \(\|\sigma\|_2^2=2^d\), and the Rayleigh inequality yields \(H(\sigma)\ge2^{d-1}\lambda_{\min}\). Equality is attained by the characters associated with the minimum eigenvalue, since they are themselves valid binary spin configurations. This proves the energy formula without assuming a priori that an energy minimizer is a character.

It remains to exclude noncharacter spin configurations from degenerate minimal eigenspaces. Equality in the Rayleigh inequality requires \(\sigma\) to belong entirely to the least-eigenvalue eigenspace. Off the threshold this eigenspace has dimension one or \(m\), spanned respectively by \(\chi_{[d]}\) or the \(m\) characters \(\chi_{[d]\setminus\{i\}}\), \(i\in I_*\). At the threshold it is their direct sum. Multiplying by \(\chi_{[d]}\), a binary minimizer in any of these spaces becomes a function of the form
\[
g(x)=a_0+\sum_{i\in I_*}a_ix_i\in\{-1,+1\}.
\]
Consequently \(g(x)^2\equiv1\). Comparing the distinct degree-one and degree-two Boolean Fourier coefficients of this identity shows
\[
a_0a_i=0\quad(i\in I_*),\qquad a_ia_j=0\quad(i\ne j).
\]
Thus at most one real coefficient is nonzero. Its square equals one by the constant Fourier coefficient, so \(g=\pm1\) or \(g=\pm x_i\) for an allowed \(i\). In the off-threshold sectors the irrelevant coefficients are simply absent. This proves that the listed characters exhaust all binary ground states. Their supports are nonempty; orthogonality to the constant character gives zero magnetization. All claims follow.

## Verification

The standalone `folded_cube_verifier.py` uses integer arithmetic and requires only Python 3. It exhaustively checks every spin assignment for a selection of anisotropic and signed-antipodal cases in dimensions \(d=2,3,4\); in particular, it checks the **full set** of minimizers rather than energy alone. It separately checks the exact Walsh spectrum and predicted minimum over dimensions \(d=2,\ldots,12\) and additional parameter choices. The recorded run returned `VERIFY_OK exhaustive_cases=26 spectral_cases=561 max_exhaustive_dimension=4`. The all-dimension theorem rests on the proof above, not on the finite tests.

As a nontrivial special case, the isotropic \(d=4\) folded hypercube, also called the Clebsch graph, at \(J_i=K=J>0\) lies exactly at the threshold. Its ground energy is \(-24J\) and its degeneracy is \(10\); the theorem identifies all ten configurations.

## Relationship to prior work

Xu and Meng (2009) give the adjacency spectrum of the ordinary unweighted folded hypercube. Liu, Pan, Wang and Cao (2014) study its Laplacian spectrum and Kirchhoff index. Mosseri (2014) develops a general Hadamard-transform framework for Ising energy enumeration on graphs, including ordinary hypercubic graphs. The spectral approach used here is compatible with these established methods, but the present claim adds an all-dimension, arbitrarily anisotropic two-branch ground-state formula and a proof that every binary minimizing configuration is one of the specified Walsh characters, including at critical degeneracy. The previous spectral results and general enumeration algorithm are not claimed as new.

A later study of weighted folded-hypercube spectra (Dai and collaborators, 2019) was located, but its full text was not accessible during comparison; its available abstract concerns network spectra and coherence rather than this Ising ground-state classification. Consequently an unindexed equivalent signed-MaxCut or Ising ground-state theorem remains a priority risk, and no global uniqueness of the formulation is asserted.

## Limitations

The result assumes strictly positive weights on each coordinate direction, a single uniform real coupling along the antipodal matching, zero field, classical Ising spins, and no further interactions. Vanishing coordinate weights can create additional eigenspace degeneracies and are excluded. It does not classify excited levels, positive-temperature Gibbs states, field-induced magnetization plateaux or quantum transverse-field effects. Historical priority is provisional pending broader specialist examination; independent scientific validation has not been performed.

## References

1. Y. Xu and J. Meng, *On the Folded Hypercube and Bi-folded Hypercube*, *Ars Combinatoria* 92 (2009), 3–9. https://combinatorialpress.com/ars-articles/volume-092-ars-articles/on-the-folded-hypercube-and-bi-folded-hypercube/
2. J. Liu, X.-F. Pan, Y. Wang and J. Cao, *The Kirchhoff Index of Folded Hypercubes and Some Variant Networks*, *Mathematical Problems in Engineering* (2014), 380874. https://doi.org/10.1155/2014/380874
3. R. Mosseri, *Ising-like models on arbitrary graphs: The Hadamard way*, arXiv:1409.0147 (first submitted 30 August 2014). https://arxiv.org/abs/1409.0147
4. M. Dai and collaborators, *Spectra analysis and network coherence for weighted folded hypercube*, *International Journal of Modern Physics B* 33 (2019), 1950094. https://doi.org/10.1142/S0217979219500942
