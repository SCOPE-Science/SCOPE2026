# Spectral-radius distortion exactly recovers the completely bounded identity norm
## Finding
Let \(E_1\) and \(E_2\) be operator-space structures on \(\mathbb C^d\), with the same standard coordinate vectors, and let \(u=\operatorname{id}:E_1\to E_2\). Define
\[
D_\rho(E_1,E_2)=\sup\left\{\frac{\rho_{E_2}(T)}{\rho_{E_1}(T)}:\ T\text{ is an operator }d\text{-tuple},\ \rho_{E_1}(T)>0\right\}.
\]
Then
\[
D_\rho(E_1,E_2)=\|u\|_{\mathrm{cb}}.
\]
If \(\rho_E^{\min}\) denotes the minimal Shalit--Shamovich spectral radius, then also
\[
\sup_{\rho^{\min}_{E_1}(T)>0}\frac{\rho^{\min}_{E_2}(T)}{\rho^{\min}_{E_1}(T)}=\|u\|_{\mathrm{cb}}.
\]
In fact, every nonzero matrix-level ratio is exactly realized by one of the universal tuples from Tornes's construction: for every \(m\ge1\) and every \(0\ne X\in M_m(\mathbb C^d)\), there is an operator tuple \(T_X\) such that
\[
\frac{\rho_{E_2}(T_X)}{\rho_{E_1}(T_X)}
=
\frac{\rho^{\min}_{E_2}(T_X)}{\rho^{\min}_{E_1}(T_X)}
=
\frac{\|X\|_{M_m(E_2)}}{\|X\|_{M_m(E_1)}}.
\]

## Assumptions and scope
The two operator spaces have the same underlying coordinate vector space \(\mathbb C^d\), and the map whose completely bounded norm is recovered is the coordinate identity. The supremum defining \(D_\rho\) ranges over operator \(d\)-tuples on arbitrary Hilbert spaces. No claim is made that the supremum is attained. The result concerns multiplicative distortion of the full operator-tuple spectral-radius functions; it does not assert that finite-dimensional matrix tuples alone detect the same distortion for arbitrary pairs of operator spaces.

## Proof
Set \(C=\|u\|_{\mathrm{cb}}\). For an operator tuple \(T=(T_1,\ldots,T_d)\), the Shalit--Shamovich formula writes the \(n\)-th term before taking the root as the norm of
\[
S_n(T)=\sum_{|\omega|=n}T^\omega\otimes e_{\omega_1}\otimes\cdots\otimes e_{\omega_n}
\]
in \(B(K)\otimes_{\min}E^{\otimes_h n}\). Functoriality of the Haagerup tensor product and of the minimal tensor product gives
\[
\|I_{B(K)}\otimes u^{\otimes_h n}\|_{\mathrm{cb}}\le C^n.
\]
The map sends the algebraic tensor representing \(S_n(T)\) for \(E_1\) to the same coefficient tensor for \(E_2\). Hence
\[
\|S_n(T)\|_{E_2}\le C^n\|S_n(T)\|_{E_1}.
\]
Taking \(n\)-th roots and the defining limit yields
\[
\rho_{E_2}(T)\le C\rho_{E_1}(T).
\]
This upper inequality also appears, for completely bounded maps, in the proof of Lemma 3.13 of Scherer--Shalit--Shamovich. The same argument with the spatial tensor powers in the definition of \(\rho_E^{\min}\) gives
\[
\rho^{\min}_{E_2}(T)\le C\rho^{\min}_{E_1}(T).
\]
Therefore both spectral-radius distortion suprema are at most \(C\).

For the reverse inequality, fix \(m\ge1\) and \(0\ne X\in M_m(\mathbb C^d)\). Corollary 3.2 of Tornes constructs a single operator tuple \(T_X\), independent of the operator-space structure, for which every operator-space structure \(E\) on \(\mathbb C^d\) satisfies
\[
\rho_E(T_X)=\rho_E^{\min}(T_X)=\|X\|_{M_m(E)}.
\]
Applying this simultaneously to \(E_1\) and \(E_2\) gives the exact ratio identity stated above. Taking the supremum over all \(m\) and all nonzero \(X\in M_m(\mathbb C^d)\) gives
\[
D_\rho(E_1,E_2)\ge
\sup_{m,X\ne0}\frac{\|X\|_{M_m(E_2)}}{\|X\|_{M_m(E_1)}}
=
\|u\|_{\mathrm{cb}}.
\]
The same witnesses give the same lower bound for the minimal spectral radius. Combined with the upper bounds, both equalities follow.

## Verification
The proof separates into two independent checks. First, the completely bounded tensor-power estimate gives the universal upper bound at every word length before any limit is taken. Second, Tornes's Corollary 3.2 gives a tuple \(T_X\) satisfying both spectral-radius equalities for every operator-space structure simultaneously; therefore each matrix-level norm ratio is reproduced without approximation. The definition of \(\|u\|_{\mathrm{cb}}\) is exactly the supremum of these matrix-level ratios. If \(\rho_{E_1}(T)=0\), the upper inequality forces \(\rho_{E_2}(T)=0\), so excluding zero denominators loses no finite ratio. No numerical experiment or finite enumeration is used.

## Relationship to prior work
Shalit and Shamovich introduced the operator-space spectral radius and proved its basic functorial behavior. Scherer, Shalit and Shamovich explicitly record the one-sided estimate
\[
\rho_{E_2}(v(x))\le\|v\|_{\mathrm{cb}}\rho_{E_1}(x)
\]
for a completely bounded map \(v:E_1\to E_2\), and used it as an inequality in separation arguments. Tornes then constructed, for every operator tuple \(X\), a universal tuple \(T_X\) with \(\rho_E(T_X)=\rho_E^{\min}(T_X)=\|X\|_E\) for every operator-space structure \(E\), and deduced the qualitative result that equality of the spectral-radius functions forces complete isometry. Combining the earlier sharp upper inequality with Tornes's simultaneous universal witnesses yields the exact distortion formula above. The inspected focal and predecessor texts do not state this quantitative identity.

## Limitations
The formula recovers the completely bounded norm of the fixed coordinate identity; it is not a formula for the infimum over all linear isomorphisms between two unrelated operator spaces. The supremum can require arbitrarily large matrix levels and need not be attained by a single matrix tuple. The theorem also does not replace the full operator-tuple domain by finite-dimensional tuples; Tornes emphasizes that infinite-dimensional witnesses are essential in the general rigidity problem.

## References
1. Maximilian Tornes, *On the Shalit--Shamovich Spectral Radius*, arXiv:2610.00816v1, especially Theorem 3.1 and Corollaries 3.2--3.3.
2. Marcel Scherer, Orr Moshe Shalit, and Eli Shamovich, *On the spectral radius of operator tuples*, arXiv:2605.09354v1, especially the proof of Lemma 3.13 and Question 1.1.
3. Orr Moshe Shalit and Eli Shamovich, *A spectral radius for matrices over an operator space*, arXiv:2501.01325v1, especially Remark 2.4 and the definitions of the two spectral radii.
4. Gilles Pisier, *Introduction to Operator Space Theory*, Cambridge University Press, 2003, for functoriality of the Haagerup and minimal operator-space tensor products.
