# Vertex corners and isotropy point masses in Kumjian–Pask algebras

Let \(R\) be a nonzero unital commutative ring and let \(\Lambda\) be a row-finite \(k\)-graph with no sources, \(k\ge 1\). Write
\[
A=KP_R(\Lambda)\cong A_R(\mathcal G_\Lambda)
\]
for the Kumjian–Pask algebra in its Steinberg-algebra realization. For \(v\in\Lambda^0\), put \(U_v=Z(v)\subseteq\Lambda^\infty\), so that \(s_v\) corresponds to \(1_{U_v}\).

## Main correction criteria

### 1. Vertex corners

There is a canonical identification
\[
 s_v A s_v\cong A_R(\mathcal G_\Lambda|_{U_v}),
\qquad
\mathcal G_\Lambda|_{U_v}:=r^{-1}(U_v)\cap s^{-1}(U_v).
\]
Consequently,
\[
\boxed{
 s_v A s_v=R s_v
 \iff
 U_v=\{x\}\text{ for some }x\in\Lambda^\infty\text{ and }\operatorname{Per}(x)=\{0\}.
}
\]
Thus a vertex corner is the scalar corner exactly when the vertex supports a unique infinite path and that path is aperiodic.

**Proof.** Multiplication by \(1_{U_v}\) on both sides cuts a Steinberg function down to the reduction \(\mathcal G_\Lambda|_{U_v}\), giving the displayed corner identification.

Suppose first that \(s_vAs_v=Rs_v\). If \(U_v\) contained distinct points \(x,y\), then, because \(U_v\) is a compact open subset of the locally compact Boolean unit space, there would be a compact open set \(C\) with
\[
 x\in C\subseteq U_v,\qquad y\notin C.
\]
Then \(1_C\in 1_{U_v}A_R(\mathcal G_\Lambda)1_{U_v}\), but \(1_C\) is not a scalar multiple of \(1_{U_v}\), a contradiction. Hence \(U_v=\{x\}\). The reduction is then the isotropy group at \(x\), so
\[
 s_vAs_v\cong R[\mathcal G_{\Lambda,x}]
 \cong R[\operatorname{Per}(x)].
\]
This is the scalar copy of \(R\) exactly when \(\operatorname{Per}(x)=0\). The converse follows from the same identification. \(\square\)

A useful finite-vertex consequence is immediate:

\[
\boxed{
 |\Lambda^0|<\infty\quad\Longrightarrow\quad s_vAs_v\ne Rs_v
 \text{ for every }v\in\Lambda^0.
}
\]

Indeed, if \(Z(v)=\{x\}\), then every vertex occurring along \(x\) also supports a unique infinite path: any alternative tail could be prefixed by the initial segment of \(x\) to produce a second path from \(v\). Along the sequence of vertices \(x(0),x(e_i),x(2e_i),\ldots\) for any coordinate \(i\), finiteness forces a repeated vertex. The corresponding two shifts of \(x\) are then the same unique tail, producing a nonzero period and contradicting \(\operatorname{Per}(x)=0\).

### 2. Isotropy point masses

Let \(\mathcal G\) be any Hausdorff ample groupoid, let \(x\in\mathcal G^{(0)}\), and let \(\gamma\in x\mathcal Gx\). Then
\[
\boxed{
1_{\{\gamma\}}\in A_R(\mathcal G)
\iff
\{x\}\text{ is open in }\mathcal G^{(0)}.
}
\]

**Proof.** If \(1_{\{\gamma\}}\) lies in the Steinberg algebra, local constancy at \(\gamma\) gives an open neighborhood of \(\gamma\) contained in \(\{\gamma\}\); hence \(\{\gamma\}\) is open. Since the source map of an étale groupoid is open, \(\{x\}=s(\{\gamma\})\) is open.

Conversely, assume \(\{x\}\) is open. Choose a compact open bisection \(B\ni\gamma\). Then
\[
 B\cap s^{-1}(\{x\})=\{\gamma\},
\]
because \(s|_B\) is injective. This singleton is an open compact bisection, so its characteristic function belongs to \(A_R(\mathcal G)\). \(\square\)

For the boundary-path groupoid this means that the point-mass formula
\[
 u^p\longmapsto 1_{\{(x,p,x)\}},\qquad p\in\operatorname{Per}(x),
\]
defines a map into \(A_R(\mathcal G_\Lambda)\) exactly when \(x\) is isolated in \(\Lambda^\infty\). The obstruction already occurs at \(p=0\): if \(x\) is nonisolated then \(1_{\{(x,0,x)\}}\) is not locally constant and hence is not a Steinberg-algebra element.

When \(x\) is isolated, put \(e_x=1_{\{x\}}\). Then
\[
R[\mathcal G_{\Lambda,x}]\cong e_xAe_x.
\]
For unital module categories, the natural corner adjunction is therefore
\[
 A e_x\otimes_{e_xAe_x}-\dashv e_x(-).
\]
In particular, simply viewing an arbitrary unital \(A\)-module \(M\) as a module over the isotropy group algebra through the corner inclusion does **not** in general produce a unital isotropy module: the identity of \(R[\mathcal G_{\Lambda,x}]\) acts as \(e_x\), not as the identity on all of \(M\). The unital restriction is \(e_xM\). For nonisolated \(x\), the usual Steinberg-algebra induction from isotropy is instead constructed from the source-fiber bimodule and does not require a point-mass subalgebra embedding.

## Consequences for arXiv:2609.20230v1

The recent preprint *Induced and Restricted Representations of Kumjian--Pask Algebras of Higher-Rank Graphs* states in Section 3.1 that every vertex corner \(s_vKP_R(\Lambda)s_v\) is isomorphic to \(R\), and in Section 4.1 defines an isotropy embedding by singleton characteristic functions for every infinite path \(x\). The two criteria above show that both statements need additional hypotheses.

The first issue has an internal counterexample already present in the preprint. For the one-vertex one-loop graph,
\[
KP_R(\Lambda)\cong R[t,t^{-1}],
\]
and the unique vertex idempotent is \(1\), so its corner is the whole Laurent polynomial ring, not \(R\). The preprint itself records this Laurent-polynomial example. Its later two-vertex rank-two example likewise explicitly produces non-scalar Laurent-type vertex corners. Thus the scalar-corner assertion cannot hold under the standing row-finite/no-source hypotheses.

The second issue is witnessed by the one-vertex two-loop graph. Its infinite-path space is \(\{e,f\}^{\mathbb N}\), which has no isolated points. For \(x=e^\infty\), one has \(\operatorname{Per}(x)\cong\mathbb Z\), but none of the singleton functions \(1_{\{(x,p,x)\}}\) belongs to the Steinberg algebra. Hence the point-mass embedding and the restriction functor defined from it are not available as written for this \(x\).

These observations do not invalidate results in the preprint that are independent of the two constructions. They show specifically that:

- the Section 3.1 construction is not induction from the full vertex corner unless the scalar-corner criterion holds; the tensor product over \(R\) remains a separate scalar-extension construction;
- the claimed path-only decomposition of \(KP_R(\Lambda)s_v\) also fails already for the one-loop graph, where negative Laurent powers are present;
- Proposition 4.1 and constructions depending on its point-mass embedding require isolation of \(x\), and unital restriction through the resulting corner requires replacing \(M\) by \(e_xM\);
- for arbitrary nonisolated paths, established Steinberg-algebra isotropy induction should be used instead of a singleton-subalgebra embedding.

## Relation to prior literature

The groupoid-corner mechanism is standard: Abrams--Dokuchaev--Nam identify corners of Steinberg algebras with Steinberg algebras of reductions. Clark--Gil Canto--Martín Barquero--Martín González--Ruiz Campos show that open singleton units lead to isotropy corners and, for Kumjian--Pask algebras, identify line points by the condition that the vertex supports a unique aperiodic boundary path. Thus the structural ingredients of the vertex-corner criterion are prior work. Nguyen--Nguyen also treats induction from isotropy for Steinberg algebras by the standard source-fiber construction.

The contribution recorded here is the application of these structural facts to diagnose the two universal assertions in arXiv:2609.20230v1, the exact missing hypotheses, the unital-module correction, and the explicit counterexamples (including the contradiction with examples contained in that preprint itself).

## Limitations

Originality is asserted only to the best of our knowledge. The corner and open-singleton facts themselves are not claimed as new. No public correction or revised version of arXiv:2609.20230 was located at the time of publication; the source is a recent v1 and may subsequently be revised. The discussion concerns the specific vertex-corner and isotropy point-mass constructions and does not assess unrelated theorems in the preprint.

## References

1. B. V. Nguyen, *Induced and Restricted Representations of Kumjian--Pask Algebras of Higher-Rank Graphs*, arXiv:2609.20230v1 (2026).
2. G. Abrams, M. Dokuchaev, T. G. Nam, *Realizing corners of Leavitt path algebras as Steinberg algebras, with corresponding connections to graph C*-algebras*, J. Algebra 593 (2022), 72–104; arXiv:1909.03964.
3. L. O. Clark, C. Gil Canto, D. Martín Barquero, C. Martín González, I. Ruiz Campos, *On the socle of a class of Steinberg algebras*, arXiv:2502.15574 (2025).
4. Q. L. Nguyen, B. V. Nguyen, *On induced graded simple modules over graded Steinberg algebras with applications to Leavitt path algebras*, arXiv:2006.09931 (2020).
5. G. Aranda Pino, L. O. Clark, A. an Huef, I. Raeburn, *Kumjian--Pask algebras of higher-rank graphs*, Trans. Amer. Math. Soc. 365 (2013), 3613–3641; arXiv:1106.4361.
