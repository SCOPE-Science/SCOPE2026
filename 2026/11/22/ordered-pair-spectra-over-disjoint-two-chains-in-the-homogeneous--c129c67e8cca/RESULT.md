# Ordered-pair spectra over disjoint two-chains in the homogeneous partial order

## Finding
Let \(\mathbb P\) be the countable universal homogeneous strict partial order. Fix \(m\geq0\) individually named, pairwise incomparable two-element chains
\[
A_m=\{a_1<b_1\}\sqcup\cdots\sqcup\{a_m<b_m\}.
\]
Write \(N_m\) for complete nonalgebraic one-point types over \(A_m\); write \(C_m\) for complete types of **ordered distinct new elements** \((x,y)\) with \(x<y\), and \(I_m\) for those with \(x\parallel y\). All new elements are different from every named parameter. Then, for every integer \(m\geq0\),
\[
\boxed{N_m=2\cdot3^m+m-1,}
\]
\[
\boxed{\begin{aligned}
C_m&=9^m+2\cdot6^m+\left(\frac{4m}{3}-2\right)3^m+m,\\
I_m&=2\cdot9^m+2\cdot6^m+\left(\frac{8m}{3}-4\right)3^m+(m-1)^2.
\end{aligned}}
\]
The number with \(y<x\) is also \(C_m\). Thus the total injective ordered-pair count is
\[
\boxed{T_m=2C_m+I_m=4\cdot9^m+6\cdot6^m+\left(\frac{16m}{3}-8\right)3^m+m^2+1.}
\]
In particular the proportion of comparable ordered-pair types is strictly greater than one half at **every** finite \(m\), and has the sharp first correction
\[
\boxed{\frac{2C_m}{T_m}=\frac12+\frac14\left(\frac23\right)^m+O\!\left(\left(\frac49\right)^m\right)\quad(m\longrightarrow\infty).}
\]
The first values \((C_m,I_m,T_m)\) are \((1,1,3)\), \((20,26,66)\), \((161,247,569)\), and \((1218,2002,4438)\) for \(m=0,1,2,3\), respectively.

## Assumptions and scope
The relation is a strict partial order: irreflexive and transitive. Each of the \(2m\) old points is named **individually**, not identified modulo permutations of blocks. There are exactly the \(m\) stated old comparabilities; different old blocks are incomparable. The new tuple points are ordered, distinct, and not equal to old points. Counts refer to complete first-order types, not to frequencies of actual vertices of the infinite structure. The case \(m=0\) is included.

Since \(\mathbb P\) is the Fraïssé limit of all finite partial orders, every finite labelled poset extension of \(A_m\) occurs, and ultrahomogeneity identifies complete tuple types precisely with the induced strict-order patterns over the named base. Thus the problem is a finite-poset extension count.

## Proof
**1. The unary identity.** An old point below a new point belongs to a down-set, and an old point above it belongs to an up-set; any point of the down-set must be below any point of the up-set. In \(A_m\), there are \(3^m\) down-sets (independently choose zero, one, or two points from each two-chain), and as many up-sets. Extensions with only a down-set or only an up-set contribute \(2\cdot3^m-1\), subtracting the all-incomparable extension counted twice. Any extension with both sides nonempty must have all old comparable points in a *single* two-chain, with its lower point below the new point and its upper point above. This contributes exactly \(m\) extra extensions.

**2. Local two-point signatures.** First prescribe either \(x<y\) or \(x\parallel y\). In one old block \(a<b\), assign each of the four old-to-new pairs \((a,x),(a,y),(b,x),(b,y)\) one of three relations: old below new, old above new, or incomparable. Retain the assignment exactly when its transitive closure is the prescribed induced four-point strict poset, without changing any of the four assigned comparisons. There are respectively \(20\) and \(26\) retained assignments.

For a retained assignment, encode which directions appear from the block to each new point by a four-bit integer \(s\in\{0,\ldots,15\}\): bit \(0\) records some old point below \(x\), bit \(1\) some old point above \(x\), and bits \(2,3\) do the same for \(y\). Let \(w_{<}(s)\), \(w_{\parallel}(s)\) count retained assignments having that mask. In order of mask \(s=0,1,\ldots,15\), direct checking of the three possibilities on each of the four pairs gives
\[
\begin{aligned}
(w_{<}(s))_{s=0}^{15}&=(1,0,2,0,2,3,4,2,0,0,3,0,0,0,2,1),\\
(w_{\parallel}(s))_{s=0}^{15}&=(1,2,2,1,2,4,1,1,2,1,4,1,1,1,1,1).
\end{aligned}
\]
Their sums are \(20\) and \(26\). The standalone checker derives the vectors by enumerating all \(3^4\) signatures, rather than assuming them.

**3. Exact global compatibility.** For each new coordinate separately, record one of four states of the *processed* old blocks: \(0\) (no comparable old point), \(+\) (old predecessors only), \(-\) (old successors only), and \(\pm\) (both old predecessors and successors, all in one processed block). If a fresh block has a local status \(v\in\{0,+,-,\pm\}\), a transition is allowed precisely by the following rules:
\[
\begin{array}{c|c}
\text{previous state}&\text{permitted next local state and resulting state}\\\hline
0&v\mapsto v\ \text{for every }v\\
+&0,+\mapsto +\\
-&0,-\mapsto -\\
\pm&0\mapsto\pm.
\end{array}
\]
A missing case is forbidden. Apply the rule simultaneously to \(x\) and \(y\), giving \(16\) joint states. These transitions are *necessary*: if old predecessors and successors of the same new point lay in distinct old blocks, transitivity would create a forbidden comparability between those blocks. They are also *sufficient*. All within-block two-step paths were checked in Step 2. A path creating an old comparison between different blocks must pass through \(x\) or \(y\). If \(x<y\), a path using both new points still makes one new point intermediate between old elements of different blocks and is therefore excluded by the same rule. If \(x\parallel y\), no path between the new points is available; a path that would imply such a comparison from within one block was already rejected in Step 2. Consequently no untested transitivity or antisymmetry condition remains.

Let \(M_{<}\) and \(M_{\parallel}\) be the \(16\times16\) integer matrices whose entry for two joint states counts local masks with the indicated weight and the permitted transitions. Explicitly, for joint states \(u,v\in\{0,+,-,\pm\}^2\),
\[
M_{\rho}(u,v)=\sum_{s=0}^{15}w_{\rho}(s)\,\mathbf1\{\operatorname{step}(u,s)=v\},\qquad\rho\in\{<,\parallel\}.
\]
With \(e_0\) the row vector concentrated at state \((0,0)\) and \(\mathbf1\) the all-ones column vector, the exact all-index enumerators are
\[
C_m=e_0M_{<}^m\mathbf1,\qquad I_m=e_0M_{\parallel}^m\mathbf1.
\]
This is an enumeration of the actual extensions, not merely a transfer approximation.

**4. Closed-form certificate and unrestricted induction.** Define the polynomials
\[
p_{<}(t)=(t-9)(t-6)(t-3)^2(t-1)^2,
\qquad
p_{\parallel}(t)=(t-9)(t-6)(t-3)^2(t-1)^3.
\]
A finite integer matrix multiplication using the explicit weight vectors and step rule above gives the *row identities*
\[
e_0p_{<}(M_{<})=0,\qquad e_0p_{\parallel}(M_{\parallel})=0.
\]
These identities are exactly reproduced by the standalone certificate; only addition and multiplication of finite integers are used. Right-multiplying by a power of the corresponding matrix and by \(\mathbf1\) proves homogeneous linear recurrences of orders six and seven respectively, for **every** \(m\ge0\). The first six comparable and first seven incomparable values obtained directly from the state transitions agree with the displayed closed forms, which themselves solve these recurrences because they are linear combinations of \(9^m,6^m,3^m,m3^m,1,m,m^2\) with the indicated characteristic factors. Induction using the recurrences therefore proves the boxed identities for all \(m\), without extrapolating from finite data.

**5. Sharp comparability law.** Subtraction yields the exact identity
\[
2C_m-I_m=2\cdot6^m-m^2+4m-1.
\]
It is positive for \(m=0\). For \(m\ge1\), the elementary bound \(6^m\ge m^2\) shows it is positive. Finally, \(T_m=4\cdot9^m(1+O((2/3)^m))\), and the displayed difference is \(2\cdot6^m(1+o(1))\). Using \(2C_m/T_m=1/2+(2C_m-I_m)/(2T_m)\), and bounding the remaining exponential and polynomial terms, gives precisely the first-correction formula with error \(O((4/9)^m)\).

## Verification
The standalone `verify.py` uses only the Python standard library. It independently enumerates all ternary four-point old/new relation assignments to construct the two local weight vectors, builds the \(16\)-state transfer matrices, and checks the exact row annihilations for the stated degree-six and degree-seven polynomials. This is a finite algebraic certificate of all-index recurrences, combined with explicit initial values, not interpolation or testing a finite prefix alone. Separately, it performs a full-bitset transitive-closure reconstruction on all permissible block signatures for \(0\le m\le3\), independently comparing actual global-poset validity with the proposed transition condition (\(8{,}421\) and \(18{,}279\) cases in the two orientations). The recorded output ends `EXACT_RECURRENCE_AND_TRANSITIVITY_OK`.

Reproduction: place `verify.py` in the current directory and run `python3 verify.py`. No network access, packages, other files, or random inputs are needed.

## Relationship to prior work
The generic homogeneous poset and its finite extension property are classical; Hubička's construction and proof of the extension property are an accessible initiating source. The general correspondence between complete finite-base tuple types and finite labelled extensions is not new.

Published exact enumerations over an antichain base count arbitrary fixed-arity extensions when *all old points are incomparable*, and published exact two-point formulas over a complete height-two base impose *every* lower-to-upper comparison. The latter overlaps the present base at one old pair, but for \(m\ge2\) the matching base has only \(m\) comparabilities instead of \(m^2\). Its formulas do not specialize to these missing-comparability bases. Published order-polynomial formulas over one long named chain likewise do not cover a growing family of disjoint chains. General unary-type inequalities, finite-poset extension parametrizations and computational hardness results are background and do not imply the pair-channel identities or their sharp asymptotic correction. This work's claimed contribution is precisely the new matching-base pair spectrum and its strict/exponentially sharp half-comparability law.

## Limitations
The result applies only to an individually named disjoint union of two-element chains, not arbitrary height-two posets, longer disjoint chains, or tuple arities greater than two. Uniform counting over logical types is not a probability law for random points of the countably infinite poset. The row-identity certificate is exact but still requires inspecting or executing the short checker to reproduce its finite integer arithmetic. Originality is based on available indexed and inspected literature and does not exclude an unindexed historical equivalent. No independent mathematical audit is asserted.

## References
1. J. Hubička, *Combinatorial Properties of Finite Models*, arXiv:1009.0566, first posted 2010-09-03; Chapter 3, especially Theorems 3.10 and 3.11. https://arxiv.org/abs/1009.0566
2. *Exact ordered-pair type spectrum over complete height-two parameter posets*, published mathematical record, 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-ordered-pair-type-spectrum-over-complete-height-two-parame--8b01eae861b0
3. *Exact two-point and fixed-arity type spectra over antichains in the random poset*, published mathematical record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-two-point-and-fixed-arity-type-spectra-over-antichains-in--3d742ffe8f7d
4. *Order-polynomial spectra of tuple types over chains in the generic partial order*, published mathematical record, 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-order-polynomial-spectra-of-tuple-types-over-chains-in-the-gener--67a71af3c8ab
