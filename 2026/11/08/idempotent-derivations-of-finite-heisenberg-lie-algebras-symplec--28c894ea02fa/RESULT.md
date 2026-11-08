# Idempotent derivations of finite Heisenberg Lie algebras: symplectic rank strata and a rare characteristic-two phase

## Finding

Let \(q\) be any prime power, let \(n\geq2\), and let \(H_{2n+1}(q)=V\oplus\mathbb F_q z\) be the Heisenberg Lie algebra, where \(\dim V=2n\), \(\omega\colon V\times V\to\mathbb F_q\) is a fixed nondegenerate alternating form, and \([u,v]=\omega(u,v)z\), \([z,H]=0\). A derivation means an \(\mathbb F_q\)-linear map satisfying the Leibniz identity. Count derivations \(D\) satisfying \(D^2=D\) by ordinary linear-operator rank; write \(F_{n,q}(x)=\sum_D x^{\operatorname{rank}D}\).

Set
\[
L_{n,q}=q^{n(n+3)/2}\prod_{j=1}^{n}(q^j+1),\qquad
S_j(q)=q^{j^2}\prod_{i=1}^{j}(q^{2i}-1),\quad S_0(q)=1.
\]

For **odd** \(q\), the complete rank enumerator is
\[
F_{n,q}(x)=1+L_{n,q}x^{n+1}.
\]
Every nonzero idempotent derivation therefore has rank \(n+1\). For **even** \(q\), it is
\[
\boxed{F_{n,q}(x)=L_{n,q}x^{n+1}
+\sum_{r=0}^{n}q^{2r}\frac{S_n(q)}{S_r(q)S_{n-r}(q)}x^{2r}.}
\]
If \(n\) is odd, the coefficient of \(x^{n+1}\) receives contributions from **both** displayed terms. The term \(r=0\) is the zero derivation.

Let \(\lambda\in\{0,1\}\) denote the scalar by which \(D\) acts on the derived ideal \(\mathbb F_qz\). For fixed even \(q\), the exceptional branch \(\lambda=0\) has probability \(\Theta_q(q^{-n})\) among all idempotent derivations. Conditional on this branch, put \(r=\operatorname{rank}(D)/2\). Along even \(n\), \(r-n/2\) converges in total variation on \(\mathbb Z\) to the distribution with probabilities proportional to \(q^{-4j^2+2j}\). Along odd \(n\), \(r-(n+1)/2\) converges in total variation to the distribution with probabilities proportional to \(q^{-4j^2-2j}\). These two discrete-Gaussian limits are reflections of one another. In either characteristic, the unconditional rank equals \(n+1\) with probability tending to one.

## Assumptions and scope

All vector spaces, subspaces, derivations, and ranks are over \(\mathbb F_q\). The bracket is alternating even in characteristic two; no assumption that \(q\) is prime is needed for the proof. The symplectic form is nondegenerate and the center is exactly \(\mathbb F_qz\). Throughout \(n\geq2\), although the formulas also hold at \(n=1\), a dimension covered by existing free class-two calculations. \(\Theta_q\) indicates positive constants depending on fixed \(q\) but not on \(n\). The conditional limits refer to the actual scalar \(\lambda\), not merely the rank, since ranks can coincide between the branches.

## Proof

**Derivation normal form.** The derived ideal is characteristic, so any derivation has uniquely determined \(A\in\operatorname{End}(V)\), \(f\in V^*\), and \(\lambda\in\mathbb F_q\) with
\[
D(v)=Av+f(v)z,\quad D(z)=\lambda z,\qquad
\omega(Au,v)+\omega(u,Av)=\lambda\omega(u,v)\quad(\forall u,v\in V).
\]
Conversely this identity gives a derivation, since brackets involving \(z\) vanish. Its square is itself precisely when
\[
A^2=A,\qquad \lambda^2=\lambda,\qquad fA+\lambda f=f.
\]
The field condition gives \(\lambda\in\{0,1\}\). Write \(U=\operatorname{im}A\) and \(W=\ker A\), a direct sum \(V=U\oplus W\). Evaluating the form identity on \(U\times U\), \(W\times W\), and \(U\times W\) yields
\[
(2-\lambda)\omega|_{U\times U}=0,\qquad
\lambda\omega|_{W\times W}=0,\qquad
(1-\lambda)\omega|_{U\times W}=0.
\]

**The \(\lambda=1\) branch in all characteristics.** Both \(U\) and \(W\) are isotropic and complementary, hence Lagrangian of dimension \(n\). Conversely any ordered pair of complementary Lagrangians defines a projection \(A\) satisfying the derivation equation. The remaining condition is \(f|_U=0\), giving \(q^n\) options and full derivation rank \(n+1\). There are \(\prod_{i=1}^n(q^i+1)\) Lagrangian subspaces: by symplectic-basis transitivity, this is \(|\operatorname{Sp}_{2n}(q)|\) divided by the stabilizer of one Lagrangian, whose order is \(q^{n(n+1)/2}|\operatorname{GL}_n(q)|\). Once a Lagrangian \(U\) is fixed, choose one Lagrangian complement \(W_0\); all others are graphs of symmetric linear maps \(W_0\to U\), giving \(q^{n(n+1)/2}\) complements. This proves the multiplicity \(L_{n,q}\).

**The \(\lambda=0\) branch.** Here \(U\perp W\). Nondegeneracy and \(V=U\oplus W\) imply both restrictions of \(\omega\) are nondegenerate. In odd characteristic, also \(2\omega|_{U\times U}=0\), forcing \(U=0\), then \(A=f=0\). In characteristic two, every nondegenerate symplectic subspace \(U\) of dimension \(2r\), \(0\le r\le n\), determines the unique allowable projection \(A\) with kernel \(U^\perp\). The constraint \(fA=f\) gives exactly \(q^{2r}\) functionals \(f\), and \(D\) has rank exactly \(2r\): on \(U\) its image is the graph of \(f|_U\), and on \(W\oplus\mathbb F_qz\) it vanishes. The symplectic group acts transitively on nondegenerate \(2r\)-subspaces with stabilizer \(\operatorname{Sp}_{2r}(q)\times\operatorname{Sp}_{2(n-r)}(q)\). Choosing successive hyperbolic pairs of a symplectic basis gives
\[
|\operatorname{Sp}_{2j}(q)|=S_j(q)=q^{j^2}\prod_{i=1}^{j}(q^{2i}-1).
\]
The orbit-stabilizer ratio proves the stated finite sum without hidden multiplicities.

**Rarity and conditional fluctuations.** Put \(d_j(q)=\prod_{i=1}^{j}(1-q^{-2i})\) and \(d_\infty(q)=\prod_{i\ge1}(1-q^{-2i})>0\). The \(\lambda=0\) summand of index \(r\) is exactly
\[
q^{4r(n-r)+2r}\frac{d_n(q)}{d_r(q)d_{n-r}(q)}.
\]
For \(q\) fixed, its product factor is bounded above and below by positive constants independent of \(n,r\), and tends to \(d_\infty(q)^{-1}\) when both \(r\) and \(n-r\) diverge. The exponent is maximized at an integer \(r\) with value \(n^2+n\). For even \(n\), setting \(r=n/2+j\) gives exponent \(n^2+n-4j^2+2j\); for odd \(n\), setting \(r=(n+1)/2+j\) gives exponent \(n^2+n-4j^2-2j\). Summable discrete-Gaussian tails give both claimed total-variation limits and show that the entire branch has size \(\Theta_q(q^{n^2+n})\). In contrast,
\[
L_{n,q}=q^{n^2+2n}\prod_{i=1}^{n}(1+q^{-i})=\Theta_q(q^{n^2+2n}),
\]
which proves exceptional-branch probability \(\Theta_q(q^{-n})\), and the unconditional rank concentration. The odd-characteristic count is \(1+L_{n,q}\), so its rank concentration also follows.

## Verification

The independent-enumeration program `verify.py` uses only the Python standard library. Run `python3 verify.py` to enumerate every \(2n\times2n\) matrix \(A\) over the specified small prime fields, test \(A^2=A\) and the defining symplectic derivation equation, then enumerate admissible \(f\) and independently test the full \((2n+1)\times(2n+1)\) matrix for idempotency, the Lie derivation identity, and ordinary rank. The computed histograms are:

- \((n,q)=(1,2)\): \(1+16x^2\) (small-dimensional boundary comparison).
- \((1,3)\): \(1+36x^2\); \((1,5)\): \(1+150x^2\) (boundary comparisons).
- \((2,2)\): \(1+80x^2+480x^3+16x^4\) (within the new scope).

All cases matched, and the script printed `VERIFY_OK`. The code also checks that the group-order formulas yield integral, nonnegative rank counts for multiple larger dimensions and prime powers; those arithmetic tests are not exhaustive field enumeration. The general statement and limits rest on the preceding proof, not on finite numerical extrapolation.

## Relationship to prior work

La Rosa and Mancini, *Derivations of two-step nilpotent algebras*, arXiv:2301.11058 (first public January 26, 2023), analyze derivation algebras of two-step nilpotent Lie and Leibniz algebras, particularly over real and complex fields. Their derivation setting motivates this finite-field rank question, but the inspected source does not enumerate idempotent derivations, does not treat the characteristic-two exceptional branch, and does not provide its rank strata or conditional law. General symplectic subspace transitivity, finite symplectic group orders, and Lagrangian-complement counts are standard tools used here, not claimed as new.

At dimension three, the displayed polynomial agrees with prior calculations for the free class-two nilpotent Lie algebra on two generators, which is the Heisenberg algebra of dimension three. This overlap is excluded from the novelty scope \(n\ge2\). Counts of Heisenberg *subalgebras*, idempotent Lie *endomorphisms*, and *automorphisms* concern different constraints and do not entail the enumerated idempotent derivation rank fibers for higher dimensions.

## Limitations

This concerns the standard Heisenberg Lie algebra with one-dimensional derived ideal over finite fields, not general two-step nilpotent Lie algebras, nonidempotent derivations, or Lie algebra endomorphisms. The asymptotics fix the field size while \(n\) increases. The program exhaustively checks small prime fields only. Other literature could contain a general result subsuming the rank enumerator; full independent publication-priority review has not been performed.

## References

1. G. La Rosa and M. Mancini, *Derivations of two-step nilpotent algebras*, arXiv:2301.11058v1 (January 26, 2023), https://arxiv.org/abs/2301.11058. Full preprint inspected, especially Introduction, §1, and §§2–4.
2. M. Mancini and G. La Rosa, *Two-step nilpotent Leibniz algebras*, arXiv:2106.12904 (June 24, 2021), https://arxiv.org/abs/2106.12904 (classification background).
3. Standard finite-field symplectic linear algebra: symplectic-basis enumeration, Lagrangian graphs and orbit–stabilizer (the relevant formulas are derived in the proof above).
