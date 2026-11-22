# The eight-level annihilation spectrum at the minimum order for noncommutative centrally essential rings

## Finding

Let \(R\) range over the 88 isomorphism classes of associative unital noncommutative centrally essential rings of minimum possible order \(64\), classified by Abyzov, Lyubimtsev and Tuganbaev. For the intrinsic ordered zero-product count
\[
N(R)=|\{(x,y)\in R\times R:xy=0\}|,
\]
the complete distribution, with one representative per ring isomorphism class, is:

| \(N(R)\) | Number of classes |
|---:|---:|
| 320 | 8 |
| 352 | 12 |
| 384 | 6 |
| 416 | 5 |
| 448 | 18 |
| 480 | 24 |
| 512 | 8 |
| 608 | 7 |
| **Total** | **88** |

Thus \(N(R)\) lies in the sharp interval \([320,608]\), with every displayed level attained. The zero-product probability of two independent uniform ring elements belongs to precisely the eight corresponding fractions \(N(R)/4096\). The count detects the three radical regimes \(\dim_{\mathbb F_2}W_0=2\), \(\dim W_0=1\) with \(J^2\subseteq W_0\), and \(\dim W_0=1\) with \(J^2\not\subseteq W_0\), except that the level \(480\) occurs in the first and third regimes (15 and 9 classes respectively). No two of the other regimes share a value.

## Assumptions and scope

Here \(J=J(R)\) is the Jacobson radical, \(Z_0=Z(R)\cap J\), and \(W_0=\operatorname{Ann}(J)\cap Z_0\). The classification theorem in [1] establishes \(|J|=32\), \(|Z_0|=8\), \(J/Z_0\cong\mathbb F_2^2\), \(2Z_0=0\), \(Z_0^2=0\), \(J^2\subseteq Z_0\), \(JZ_0\subseteq W_0\), and \(\dim_{\mathbb F_2}W_0\in\{1,2\}\). It also supplies exactly 88 representatives: 19 of characteristic two and 69 of characteristic four, through Tables 1–3 and Propositions 4.1–4.3. We use those classification and completeness statements as inputs, not as results proved here. All counts include pairs with zero factors and are ordered; they are not counts of ideals or of unordered pairs.

## Proof

**Reduction to the radical.** Since \(R/J\cong\mathbb F_2\), every element outside \(J\) is a unit. Products involving a unit vanish only when the other factor is zero. There are 32 such pairs in each of the two disjoint cases where the first or second factor is a unit. Consequently
\[
N(R)=64+\left|\{(u,v)\in J^2:uv=0\}\right|.
\tag{1}
\]

**Regime A: \(\dim W_0=2\).** By [1, Theorem 1.4], \(J^2\subseteq W_0\). Choose \(c\in Z_0\setminus W_0\). The map \(\theta:J/Z_0\longrightarrow W_0\), \(\theta(\bar u)=uc\), is an isomorphism by the nondegenerate central action established in [1]. Write \(V=J/Z_0\cong\mathbb F_2^2\). For fixed cosets \(v,w\in V\), the product of lifts \(u+z\) and \(u'+z'\) is
\[
B(v,w)+\theta(v)\varepsilon(z')+\theta(w)\varepsilon(z),
\]
where \(\varepsilon:Z_0\to\mathbb F_2\) is the quotient coordinate modulo \(W_0\). The 64 ordered central-offset choices therefore give: 64 zeros when \(v=w=0\); 32 zeros for each of the six cases with exactly one nonzero coset; 16 zeros for each of the six ordered independent nonzero pairs; and either 32 or zero zeros for each of the three nonzero diagonal pairs. A diagonal pair \((v,v)\) contributes 32 exactly when \(u^2\in\langle uc\rangle\), a condition independent of the lift because \((u+z)^2=u^2\) for \(z\in Z_0\). Let \(t\) be the number of such nonzero cosets. Then
\[
N(R)=64+64+6\cdot32+6\cdot16+32t=416+32t.
\tag{2}
\]
Using the canonical multiplication coordinates \(a^2=\alpha\), \(b^2=\beta\), \(ac=s_1\), \(bc=s_2\), \(ab=s_1\), \(ba=0\), write \(\alpha,\beta\in\mathbb F_2^2\). The three diagonal conditions give the explicit rule
\[
\begin{split}
t={}&\mathbf1_{\alpha\in\{0,s_1\}}+\mathbf1_{\beta\in\{0,s_2\}}\\
&+\mathbf1_{\alpha+\beta+s_1\in\{0,s_1+s_2\}}.
\end{split}
\tag{3}
\]
The representative list contains three blocks of 10 classes indexed by Table 1 (characteristic two; characteristic four with \(2\cdot1=s_1\); characteristic four with \(2\cdot1=c\)), and one block of 16 classes with \(2\cdot1=s_2\). Each block of 10 has distribution \((1,4,3,2)\) for \(t=0,1,2,3\), and the block of 16 has \((2,6,6,2)\). Therefore the 46 classes in Regime A have \((5,18,15,8)\) for \(t=0,1,2,3\) respectively, or the levels \(416,448,480,512\).

**Regime B: \(\dim W_0=1\).** The pairing
\[
(J/Z_0)\times(Z_0/W_0)\longrightarrow W_0,
\qquad(\bar u,\bar z)\longmapsto uz,
\]
is perfect by the structural lemmas in [1]. For each \((v,w)\in V^2\) other than \((0,0)\), the linear map on the 64 central-offset pairs to \(W_0\) has rank one. Hence there are 32 lift pairs with zero product if the product of the cosets vanishes in \(Z_0/W_0\), and none otherwise. For \((0,0)\), there are 64 zeros. Define
\[
h=|\{(v,w)\in V^2:B(v,w)\bmod W_0=0\}|.
\]
Since \((0,0)\) is included in \(h\), equation (1) gives
\[
N(R)=64+64+32(h-1)=96+32h.
\tag{4}
\]
When \(J^2\subseteq W_0\), all 16 quotient pairs vanish, so \(h=16\) and \(N(R)=608\). The representative lists contain seven such classes: two in characteristic two, two in characteristic four with \(2\cdot1\in W_0\), and three with \(2\cdot1\notin W_0\).

When \(J^2\not\subseteq W_0\), associativity and \([J,J]\subseteq W_0\) make the reduced multiplication the polarization of a binary cubic with coefficients \(\lambda_1,\lambda_2,\lambda_3,\lambda_4\in\mathbb F_2\), not all zero. Relative to the dual bases in [1, (3.4)], the linear map \(w\mapsto B(v,w)\bmod W_0\) at \(v=(x,y)\) has matrix
\[
L_{x,y}=\begin{pmatrix}
\lambda_1x+\lambda_2y & \lambda_2x+\lambda_3y\\
\lambda_2x+\lambda_3y & \lambda_3x+\lambda_4y
\end{pmatrix}.
\]
Thus
\[
h=\sum_{(x,y)\in\mathbb F_2^2}2^{2-\operatorname{rank}_{\mathbb F_2}L_{x,y}}.
\tag{5}
\]
For the 15 nonzero binary coefficient quadruples, the possible values are exactly \(7,8,9,12\). The seven characteristic-two representatives of Table 2 give class counts \((2,2,1,2)\) for \(h=(7,8,9,12)\); the corresponding seven characteristic-four representatives with \(2\cdot1\in W_0\) repeat these counts; and the 21 classes of Table 3 with \(2\cdot1\notin W_0\) contribute \((4,8,4,5)\). Adding produces \((8,12,6,9)\) for \(h=(7,8,9,12)\), hence the levels \((320,352,384,480)\) in 35 classes.

Summing the 46 Regime A classes, seven Regime B classes with \(J^2\subseteq W_0\), and 35 Regime B classes with \(J^2\not\subseteq W_0\) gives all 88 classes and the claimed eight-level table. The only numerical intersection between the two nontrivial regimes is \(480\). The minimum and maximum levels are both represented by explicit classes in the classification tables. \(\square\)

## Verification

Run `python verify_zero_products.py`. The script encodes the canonical radical multiplication tables in [1] for all 88 representatives, including the additive groups with cyclic order-four summands, and independently counts all \(32^2\) ordered radical pairs per representative. It compares each direct count with equations (2), (4), and (5), checks all regime totals and the final eight-level histogram, and prints `MINIMAL_CENTRAL_ESSENTIAL_ZERO_PAIRS_OK 88` followed by the eight rows. This exhaustive finite verification checks the application of the already complete 88-class list; it does not independently prove that the list is complete or replace the symbolic rank argument.

## Relationship to prior work

[1] supplies the fundamental order-64 classification, all ring representatives, the nondegenerate central multiplication pairing, the binary cubic normal form, and distributions of **square-zero elements**, but does not supply an ordered **zero-product pair** distribution or compare its fibers across all 88 isomorphism classes. [2] establishes the minimum size, structural invariants and only a partial classification. The present result instead evaluates a distinct natural two-variable invariant through the radical rank argument, revealing eight levels, two sharp extremes and a unique collision between two radical types. The classification is indispensable input; this is not claimed as an independent classification theorem. General zero-product enumeration literature for other finite ring families does not give the eight-level statement here.

## Limitations

The conclusion concerns only the 88 isomorphism classes of noncommutative centrally essential rings of minimum cardinality 64 and counts each isomorphism class once rather than weighting by number of labeled ring tables. It does not describe larger rings, complete multiplication distributions or other two-variable word laws. Historical priority beyond the inspected primary sources and published search results remains provisional; independent mathematical audit has not been performed.

## References

1. A. N. Abyzov, O. V. Lyubimtsev and A. A. Tuganbaev, *Minimal Finite Non-Commutative Centrally Essential Rings*, arXiv:2611.16086v1 (first submitted 11 November 2026). https://arxiv.org/abs/2611.16086 . Relevant materials: Theorem 1.4, Tables 1–3, Propositions 3.2, 3.4, 3.6 and 4.1–4.3.
2. A. Abyzov, O. Lyubimtsev and A. Tuganbaev, *Finite Non-Commutative Centrally Essential Rings of Minimal Order*, arXiv:2610.36174v1 (26 October 2026). https://arxiv.org/abs/2610.36174 . Relevant materials: Theorems 1.1–1.3.
