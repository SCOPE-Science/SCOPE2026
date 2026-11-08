# Sharp one-spoke defect tolerance for fourth-order Gauss graph-heat integration

## Finding

Let \(m\ge4\) be an integer. Form the weighted star with \(m\) leaves, \(m-1\) edges of conductance \(a>0\) and one exceptional edge of conductance \(at\), where \(t>0\). Let \(L_{m,t,a}\) be its positive-semidefinite combinatorial Laplacian. The completed two-stage fourth-order Gauss–Legendre Runge–Kutta heat step is
\[
T_{m,t,a}(h)=F(hL_{m,t,a}),\qquad F(z)=\frac{z^2-6z+12}{z^2+6z+12},\qquad h\ge0.
\]
Then the following equivalence is exact, with both endpoints included:
\[
\boxed{T_{m,t,a}(h)\text{ is entrywise nonnegative for every }h\ge0
\quad\Longleftrightarrow\quad
\frac12\le t\le\frac{m}{m-1}.}
\]
Within this range every entry of \(T_{m,t,a}(h)\) is strictly positive for every finite \(h>0\). If \(0<t<1/2\), the hub-to-ordinary-leaf entry is strictly negative at every sufficiently large timestep. If \(t>m/(m-1)\), the hub-to-exceptional-leaf entry is strictly negative at every sufficiently large timestep. All these matrices are symmetric and preserve row sums one for every timestep, regardless of positivity.

The upper tolerance \(m/(m-1)=1+1/(m-1)\) decreases strictly to one as the degree increases, while the lower tolerance remains exactly one-half. For example, at \(m=8\) and \(t=5/4\), the exceptional hub-edge entry is negative for \(h>(4+4\sqrt2)/a\).

## Assumptions and scope

The graph is an undirected star with exactly one anomalous spoke, all conductances positive, and the standard *unnormalized* symmetric graph Laplacian \(L=D-W\). The initial state may be any nonnegative column vector; the endpoint matrix preserves all such vectors precisely when it is entrywise nonnegative. The statement concerns completed Gauss–Legendre endpoint values, not internal Runge–Kutta stages. By the positive scaling \(h\mapsto ah\), we may set \(a=1\) in the proof. The assertion is for every integer \(m\ge4\) and every real \(t>0\), not just a sampled list of degrees or ratios.

## Proof

Put \(k=m-1\). Label the hub \(0\), the ordinary leaves \(1,\ldots,k\), and the exceptional leaf \(e\). On vectors constant across the ordinary leaves, the Laplacian acts by the equitable quotient
\[
Q=\begin{pmatrix}k+t&-k&-t\\-1&1&0\\-t&0&t\end{pmatrix}.
\]
On the orthogonal complement supported on the ordinary leaves with coordinate sum zero, the Laplacian is the identity. The two nonzero eigenvalues of \(Q\) are the positive roots \(\lambda_\pm\) of
\[
\lambda^2-(m+2t)\lambda+(m+1)t=0.
\]
Set
\[
\Delta(h)=12\prod_{\sigma\in\{-,+\}}
(\lambda_\sigma^2h^2+6\lambda_\sigma h+12)>0,
\qquad E(h)=h^2+6h+12>0.
\]
Here and below \(h>0\). Direct multiplication of \((h^2Q^2-6hQ+12I)\operatorname{adj}(h^2Q^2+6hQ+12I)\), followed by dividing the ordinary-leaf orbit into its mean and contrast parts, gives **all four off-diagonal entry types**. For an ordinary leaf \(i\) and two distinct ordinary leaves \(i\ne j\):
\[
T_{0i}(h)=\frac{144h\{t(2t-1)h^2+6th+12\}}{\Delta(h)},
\]
\[
T_{0e}(h)=\frac{144ht\{[m-(m-1)t]h^2+6h+12\}}{\Delta(h)},
\]
\[
T_{ie}(h)=\frac{144h^2t\{(m+2t)h+6\}}{\Delta(h)},
\]
\[
T_{ij}(h)=\frac{144h^2 B_m(h,t)}{E(h)\Delta(h)},
\]
where
\[
B_m(h,t)=t[(m+3)t-1]h^3+[6(m+1)t+12t^2]h^2
+[12(m+1)+48t]h+72.
\]
Symmetry supplies transposed entries. The identities are exact rational polynomial identities for arbitrary \(k,t,h\); the accompanying verifier independently checks the quotient adjugate identities and finite full-matrix instances.

If \(1/2\le t\le m/(m-1)\), each brace in the first two displayed off-diagonal formulas is strictly positive for \(h>0\). The third is manifestly strictly positive. In the fourth, the leading coefficient satisfies \((m+3)t-1\ge(m+3)/2-1>0\) and every other coefficient is positive. Thus all off-diagonal entries are strictly positive for finite \(h>0\). To treat diagonals, for every real \(z\ge0\),
\[
F(z)=\frac{(z-3)^2+3}{z^2+6z+12}>0.
\]
The spectral theorem makes \(F(hL)\) positive definite, hence each diagonal entry is positive. At \(h=0\) the matrix equals the identity. This proves sufficiency, including the boundary ratios.

For necessity, when \(t<1/2\), the leading coefficient \(t(2t-1)\) of the hub-to-ordinary-leaf numerator is strictly negative. All denominators are positive, so that entry is negative for every sufficiently large \(h\). When \(t>m/(m-1)\), the leading coefficient \(m-(m-1)t\) in the hub-to-exceptional-leaf numerator is negative, giving the other large-step obstruction. This proves the equivalence. Finally \(F(0)=1\) and \(L\mathbf 1=0\) yield \(T(h)\mathbf1=\mathbf1\), and symmetry follows from symmetric functional calculus. The example follows by solving \(-3h^2/4+6h+12=0\) for normalized \(a=1\).

## Verification

Run `python verify.py` in the directory containing the extracted files (requires Python 3 and SymPy). It reconstructs the quotient matrix, checks the four exact adjugate numerators and the ordinary-leaf contrast identity symbolically for unrestricted parameters, checks the quotient characteristic polynomial, and then performs 90 exact-rational full-star tests including endpoint cases and large-step negative witnesses. Its expected final message is `VERIFY_OK 96`. The analytic proof above supplies the infinite quantified result; the finite tests are independent checks of algebra and examples, not a replacement for the argument.

## Relationship to prior work

The general theory of strong stability preservation in Ketcheson, Gottlieb and Macdonald, *Strong Stability Preserving Two-step Runge–Kutta Methods* (first public preprint 18 June 2011), concerns universal SSP coefficient guarantees rather than the exact all-step sign of this fixed symmetric Gauss matrix. The general graph-Laplacian positivity difficulty is discussed in Blanes, Iserles and Macnamara (2021). Kirkland and Neumann (1998) and Carmona, Encinas, Patra and Sivakumar (2026, Theorems 4.2 and 4.6) characterize when the weighted-star Laplacian **group inverse** is an M-matrix. Specializing their group-inverse criterion already yields the same bounds \(1/2\le t\le m/(m-1)\) as a *necessary large-timestep sign condition*, so the parameter bounds in isolation are not claimed to be new. The new conclusion assessed here is **sufficiency at every finite timestep** of the fourth-order Gauss rational step, established by explicit nonnegative rational numerators for every degree. Earlier exact fourth-order Gauss positivity calculations for three-leaf weighted stars cover \(m=3\) and are not claimed again; the present result applies to every \(m\ge4\). A known sharp eight-state Markov positivity barrier concerns general, possibly nonsymmetric generators and does not imply this symmetric-star all-step classification.

## Limitations

This theorem does not classify arbitrary independently weighted stars, multiple anomalous spokes, nonstar graphs, other integrators, or internal-stage positivity. A general weighted-star group-inverse characterization must not be mistaken for finite-step Gauss positivity without the additional rational-sign proof. The 1998 group-inverse source was available in abstract and later full-text citations but not itself in full text in the consulted access route; an unindexed earlier derivation of the integrator-specific theorem remains a publication-priority risk. Independent mathematical and literature review is not included.

## References

1. D. I. Ketcheson, S. Gottlieb, and C. B. Macdonald, *Strong Stability Preserving Two-step Runge–Kutta Methods*, arXiv:1106.3626v1 (first posted 2011-06-18), https://arxiv.org/html/1106.3626v1.
2. S. J. Kirkland and M. Neumann, *The M-Matrix Group Generalized Inverse Problem for Weighted Trees*, SIAM J. Matrix Anal. Appl. 19 (1998), 226–234, https://doi.org/10.1137/S0895479896304927.
3. Á. Carmona, A. M. Encinas, S. Patra, and K. C. Sivakumar, *The M-matrix group inverse problem for star networks*, Comput. Appl. Math. 45 (2026), article 272, https://doi.org/10.1007/s40314-026-03651-2.
4. S. Blanes, A. Iserles, and S. Macnamara, *Positivity-preserving methods for population models*, arXiv:2102.08242v1 (2021), https://arxiv.org/abs/2102.08242.
