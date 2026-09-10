# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Tagged-skein versus upper-cluster sharp boundary for the quantum once-punctured torus

## The target and the verdict

**Target claim.** For $\Sigma=S_{1,1}$ with frozen tagged triangulation $T_0$ of Markov type
$B(T_0)=\left(\begin{smallmatrix}0&2&-2\\-2&0&2\\2&-2&0\end{smallmatrix}\right)$
(two plain arcs plus one notched arc at the puncture),
$Sk^{ta}_q(S_{1,1}) = U_q(S_{1,1})$, certified by Laurent logs putting every
MCG-orbit generator of each algebra in the other.

**Verdict: the target is FALSE.** We disprove it rigorously:

1. **Classically**, $Sk^{ta}(S_{1,1}) \subsetneq U(S_{1,1})$: the Markov invariant
   $W=(A_1^2+A_2^2+A_3^2)/(A_1A_2A_3)$ lies in $U$ but not in $Sk^{ta}$.
2. **At the quantum level**, the equality cannot even be repaired by quantisation:
   (i) the coefficient-free Markov seed admits *no* Berenstein–Zelevinsky compatible
   form, so the stated $U_q(S_{1,1})$ at $B(T_0)$ is undefined; (ii) with principal
   coefficients, where a quantum upper algebra exists, the defining notched-arc
   generator is expressly excluded from Mandel–Qin quantum bracelet theory; (iii) a
   putative quantum equality would specialise to the false classical equality.

The obstruction is sharp: it is exactly the notched-arc/extra-wall phenomenon of
Mandel–Qin plus the $A^{can}\subsetneq A^{up}$ theorem of Zhou, transported into the
skein-vs-upper comparison by Li. All computations are reproduced by the stdlib script
`output/artifacts/verify_target.py` ($\to$ `VERIFY_OK`).

## 1. The frozen seed audit

Label the three arcs of $T_0$ by $1,2,3$ and take
$B(T_0)=\left(\begin{smallmatrix}0&2&-2\\-2&0&2\\2&-2&0\end{smallmatrix}\right)$.
The script verifies:

- $\det B(T_0)=0$, $\operatorname{rank}B(T_0)=2$, with kernel spanned by
  $n_0=(1,1,1)$: $B(T_0)n_0=0$.
- Each Fomin–Zelevinsky mutation $\mu_k(B(T_0))$ equals $-B(T_0)$, hence a permutation
  of $B(T_0)$ (logged permutations $(0,2,1)$): the Markov mutation class is stable.
- The tag vector $(\mathrm{plain},\mathrm{plain},\mathrm{notched})$ is **not** a tagged
  triangulation: distinct arcs sharing the lone puncture must carry equal tags, and the
  two cross pairs $(\gamma_1,\gamma_3)$, $(\gamma_2,\gamma_3)$ fail. So $T_0$ as stated
  defines no cluster; any proof attempt must already choose plain-side or notched-side.

The g-vector/wall table used below is:

| MCG-orbit representative | $g$ | $\langle g,n_0\rangle$ | Position |
|---|---|---|---|
| plain arc $\gamma_1$ | $(1,0,0)$ | $+1$ | $H^+$: cluster complex side, theta = cluster variable |
| notched arc $\gamma_1^\diamond$ | $(-1,0,0)$ | $-1$ | $H^-$: notched side, bracelet $=4\vartheta$ classically |
| arc-pair/loop-adjacent (Zhou $\vartheta_{f_i-f_{i+1}}$) | $(1,-1,0)$ | $0$ | central wall $H=n_0^\perp$, 3-term broken-line expansion |

## 2. Classical separator: $W \in U \setminus Sk^{ta}$

Let $(A_1,A_2,A_3)$ be the initial Markov cluster and
$$W=\frac{A_1^2+A_2^2+A_3^2}{A_1A_2A_3}
= A_1^{-1}A_2^{-1}A_3 + A_1^{-1}A_2A_3^{-1} + A_1A_2^{-1}A_3^{-1}.$$
With Markov exchange $A_kA_k' = A_i^2+A_j^2$, the script checks the exact Laurent
identities $N'D-ND'=0$ (empty monomial difference) at each $k=1,2,3$, where $N,D$ are
the numerator/denominator of $W$. Hence $W$ is Laurent in every seed of the Markov
mutation class: **$W\in U(S_{1,1})$**. This is the Matherne–Muller generator quoted in
Zhou [22, Prop. 6.2.2/7.1.1].

Zhou (SIGMA 2020.013, Thm 1.3, §5.3) proves the full Fock–Goncharov conjecture
**fails** for $A_{T_{1,1}}$: $can=mid\subsetneq\Gamma=U$, with the same $W$ as the extra
generator. Mandel–Qin (Thm 9.6 + Eq. (161), Remark 3.19) identify $can$ with the tagged
skein $Sk^\Box$ up to scalars and state $Sk^\Box(S_{1,1})\ne A^{up}$, equal instead to
the intersection of the plain and notched upper structures. Li (§7, Thm 7.1, Remark 7.2)
concurs: for $\Sigma_{g,1}$ the inclusion $Sk^{ta}\subset U$ is strict, witnessed by the
potential, and $Sk^{ta}=\Gamma(\widetilde A)$ for $S_{1,1}$ rather than $\Gamma(A)=U$.
Therefore **$W\notin Sk^{ta}(S_{1,1})$** and
$$Sk^{ta}(S_{1,1}) \subsetneq U(S_{1,1})\quad\text{classically.}$$

The extra-wall formula quantifies the gap (Mandel–Qin Thm B.4, Lemma B.6, Remark B.5):
notched bracelets satisfy $\langle C\rangle_{\mathrm{Brac}}=\lambda(m)\vartheta_m$ with
$\lambda(m)=4^{[-\langle m,n_0\rangle]_+}$, i.e. a factor $4$ for weight-one notched arcs,
and $P_H=(1+z^{m_0})^2=1+2z^{m_0}+z^{2m_0}$ with coefficients summing to $4$ (verified
numerically in the log).

## 3. Quantum impossibility (three independent blocks)

**(i) No coefficient-free quantum seed at $B(T_0)$.**
A Berenstein–Zelevinsky compatible pair requires $\Lambda B = dI$ $(d>0)$.
Right-multiplying by $n_0$: $(\Lambda B)n_0=\Lambda(Bn_0)=0$ while $dIn_0=dn_0\ne 0$ —
contradiction; equivalently $\det B(T_0)=0$ forbids $\det(\Lambda B)=d^3\det\Lambda\ne0$.
Hence the target's $U_q(S_{1,1})$ at the stated frozen seed is undefined. The script logs
both the determinant and the kernel contradiction.

**(ii) The notched generator has no quantum bracelet.**
Mandel–Qin §7.4 defines quantum tagged bracelets for loops and for tagged arcs
*except* notched arcs on once-punctured closed surfaces; for genus $\ge 2$ they are
defined indirectly via the DT transformation, and for the once-punctured torus they are
explicitly excluded (Thm 9.4(i) caveat; §7.4.3). Thus the target's MCG-orbit generator
comparison — which must include the notched arc — cannot be completed in the quantum
theory where it is defined.

**(iii) Specialisation.**
Any quantisation $Sk^{ta}_q$, $U_q$ with $q\to1$ limit the classical algebras would send a
quantum equality to the classical equality of §2, which is false. So no such pair of
quantisations can be equal either.

Together, (i)–(iii) show the quantum target is impossible as stated, not merely
unproved.

## 4. What remains true (boundary, not replacement)

The failure is exactly at the known boundary: Li's $Sk^{ta}=U$ for $p\ge 2$,
Mandel–Qin's bracelet=theta theorem away from notched once-punctured tori, Mou's
central-wall difference between stability and cluster scattering diagrams for the Markov
quiver, and Zhou's $can=\Gamma(\widetilde A)$ enlarged-variety equality all stand. Our
separator $W$ with its Laurent-invariance log plus the $\lambda/P_H$ table is the sharpness
witness for that boundary.

## References

- Mandel–Qin, *Bracelets bases are theta bases*, arXiv:2301.11101 (Thms 1.1/9.4/9.6/B.4,
  Lemma B.6, Remark 3.19/B.5, §7.4).
- Li, *Skein and cluster algebras of punctured surfaces*, arXiv:2503.15037 (Thm 1.1,
  Cor. 1.2, §7/Thm 7.1/Remark 7.2, Props. 2.34–2.37).
- Zhou, *Cluster Structures and Subfans in Scattering Diagrams*, SIGMA 16 (2020) 013
  (Thms 1.1–1.4, §5).
- Mou, *Scattering diagrams of quivers with potentials and mutations*, arXiv:1910.13714
  (Ex. 5.15, Prop. 5.16: Markov central wall).
- Matherne–Muller, *Computing upper cluster algebras* (generator $W$); Muller,
  *Skein and cluster algebras of marked surfaces*; Fomin–Shapiro–Thurston (tagged
  compatibility).

## Reproduction

Run `python3 output/artifacts/verify_target.py` (stdlib only) → `VERIFY_OK`:
seed rank/kernel/no-$\Lambda$ proof, three Markov mutation logs, three $W$-invariance
identities with empty monomial difference, mixed-tag incompatibility table,
$P_H$ coefficient sum $1+2+1=4$, $\lambda$ spot checks, g-vector/wall table.
